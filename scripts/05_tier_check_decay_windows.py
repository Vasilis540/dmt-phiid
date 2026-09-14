"""
05_tier_check_decay_windows.py — tier statistics on the real-data primary
decay windows (W = 60: windows 6-14; W = 30: windows 11-28), recomputed from
the non-stationary bias-check tables.

Pre-registered 13 Sep 2026 (manuscript/analysis_record.md, "Decay windows on real data"): the
tier is ASSIGNED from the 20,000-run bias check on the pre-registered windows
(W = 60: 5-14) and does not move. This script is the CHECK that the tier
survives excluding the onset-adjacent window (window 5 = bins 9-10), decided
on the placebo injection response at bins 8-10 seen in Robustness A.

Inputs (per decay condition, W, M): the per-pair tracking table
(p_correct_sign_analytic and its interval) and the per-window table
(est_mean, est_sd, analytic). Both are read from a git commit (`--tables-commit`,
so the 2,000-run tables at 18ad8b4 can be used while the working tree is being
overwritten) or from a directory (`--tables-dir`, for the 20,000-run tables
once they land).

Statistics
  S_analytic on a pair set = mean of p_correct_sign_analytic over the pairs,
    interval = mean of the per-pair lo/hi (reproduces the criterion table's
    S_analytic on the full set; checked and printed).
  R on a window set = sign-corrected Spearman between the pooled window-mean
    sts and the intensity template f per window. Point estimate from the
    table's est_mean; interval PARAMETRIC: each window's pooled mean drawn as
    N(est_mean, est_sd / sqrt(M)) independently, N_DRAWS draws, 2.5-97.5 %.
    This is the analytic counterpart of the bootstrap R (which needs the
    per-run arrays the bias check does not save); windows are treated as
    independent, which the 60-TR windows of a VAR(1) with spectral radius
    <= 0.75 are to a close approximation.
"""

import argparse
import csv
import importlib.util
import io
import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

SEED = 20261120
N_DRAWS = 2000
THRESHOLD = 0.80
CONDITIONS = ("nonstat_decay_coupling", "nonstat_decay_noisecorr")
# pre-registered decay windows (1-based, inclusive) and the primary real-data set
WINDOWS = {60: dict(prereg=(5, 14), primary=(6, 14)),
           30: dict(prereg=(10, 28), primary=(11, 28))}
M_VALUES = (1338, 742, 151)

ap = argparse.ArgumentParser()
g = ap.add_mutually_exclusive_group(required=True)
g.add_argument("--tables-commit", help="git commit holding results/bias_check_nonstat*.csv")
g.add_argument("--tables-dir", type=Path, help="directory holding bias_check_nonstat*.csv")
ap.add_argument("--out", type=Path, default=Path("results/tier_check_decay_windows.csv"))
args = ap.parse_args()

_argv = sys.argv
sys.argv = [_argv[0]]
spec = importlib.util.spec_from_file_location("bc", "scripts/02_bias_check.py")
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)
sys.argv = _argv
F_BIN = np.asarray(bc.INTENSITY_SCALE, dtype=float)     # f per rating bin, 28 bins
assert F_BIN.shape == (28,) and abs(F_BIN[8] - 0.9154) < 1e-6 and not F_BIN[:8].any(), F_BIN


def read_table(name):
    if args.tables_commit:
        txt = subprocess.check_output(["git", "show", f"{args.tables_commit}:results/{name}"], text=True)
    else:
        txt = (args.tables_dir / name).read_text()
    header = next(l for l in io.StringIO(txt) if l.startswith("#")).strip()
    rows = list(csv.DictReader(l for l in io.StringIO(txt) if not l.startswith("#")))
    return header, rows


hdr_track, track = read_table("bias_check_nonstat_tracking.csv")
hdr_win, win = read_table("bias_check_nonstat.csv")
_, crit = read_table("bias_check_nonstat_criterion.csv")
source = args.tables_commit or str(args.tables_dir)
print(f"tables: {source}\n  {hdr_track}")

rng = np.random.default_rng(SEED)
try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

out = []
for cond in CONDITIONS:
    for W, sets in WINDOWS.items():
        wrows = sorted((r for r in win if r["condition"] == cond and int(r["window"]) == W and r["atom"] == "sts"),
                       key=lambda r: int(r["window_index"]))
        idx = np.array([int(r["window_index"]) for r in wrows])
        est = np.array([float(r["est_mean"]) for r in wrows])
        sd = np.array([float(r["est_sd"]) for r in wrows])
        truth = np.array([float(r["analytic"]) for r in wrows])
        bins_per = W // 30
        f_win = np.array([F_BIN[(i - 1) * bins_per:i * bins_per].mean() for i in idx])
        for M in M_VALUES:
            prow = [r for r in track if r["condition"] == cond and int(r["window"]) == W and int(r["M"]) == M]
            crow = next((r for r in crit if r["condition"] == cond and int(r["window"]) == W and int(r["M"]) == M), None)
            for label, (lo_w, hi_w) in sets.items():
                pairs = [r for r in prow if lo_w <= int(r["pair"].split("->")[0]) and int(r["pair"].split("->")[1]) <= hi_w]
                S = np.mean([float(r["p_correct_sign_analytic"]) for r in pairs])
                S_lo = np.mean([float(r["p_analytic_lo"]) for r in pairs])
                S_hi = np.mean([float(r["p_analytic_hi"]) for r in pairs])
                m = (idx >= lo_w) & (idx <= hi_w)
                sgn = np.sign(spearmanr(truth[m], f_win[m]).correlation)
                R_point = sgn * spearmanr(est[m], f_win[m]).correlation
                draws = est[m] + rng.standard_normal((N_DRAWS, m.sum())) * (sd[m] / np.sqrt(M))
                R_draws = sgn * np.array([spearmanr(d, f_win[m]).correlation for d in draws])
                R_lo, R_hi = np.percentile(R_draws, [2.5, 97.5])
                rep = ""
                if label == "prereg" and crow is not None:
                    rep = (f"  [criterion table: S_analytic {float(crow['S_analytic']):.3f} "
                           f"[{float(crow['S_analytic_lo']):.3f}, {float(crow['S_analytic_hi']):.3f}], "
                           f"R_boot {float(crow['R']):.3f} [{float(crow['R_lo']):.3f}, {float(crow['R_hi']):.3f}]]")
                print(f"{cond:26s} W={W:2d} M={M:4d} {label:7s} windows {lo_w:2d}-{hi_w:2d} ({len(pairs):2d} pairs): "
                      f"S_analytic {S:.3f} [{S_lo:.3f}, {S_hi:.3f}] {'pass' if S >= THRESHOLD else 'FAIL'}"
                      f"{' straddles' if S_lo < THRESHOLD <= S_hi else ''} | "
                      f"R {R_point:.3f} [{R_lo:.3f}, {R_hi:.3f}] {'pass' if R_point >= THRESHOLD else 'FAIL'}"
                      f"{' straddles' if R_lo < THRESHOLD <= R_hi else ''}{rep}")
                out.append(dict(condition=cond, window=W, M=M, window_set=label, first_window=lo_w,
                                last_window=hi_w, n_pairs=len(pairs), S_analytic=S, S_lo=S_lo, S_hi=S_hi,
                                R_point=R_point, R_lo=R_lo, R_hi=R_hi, sign_truth_vs_f=sgn,
                                S_pass=int(S >= THRESHOLD), S_straddles=int(S_lo < THRESHOLD <= S_hi),
                                R_pass=int(R_point >= THRESHOLD), R_straddles=int(R_lo < THRESHOLD <= R_hi)))

with open(args.out, "w") as fh:
    fh.write(f"# script=05_tier_check_decay_windows.py tables={source} n_draws={N_DRAWS} "
             f"threshold={THRESHOLD} seed={SEED} git={sha}\n")
    w = csv.DictWriter(fh, fieldnames=list(out[0]))
    w.writeheader()
    w.writerows(out)
print(f"wrote {args.out}")
