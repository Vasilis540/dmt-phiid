"""
partB10_crosslag_deviation.py — run-level mean cross-lag deviation (the test of the pooling mechanism named
in Results 4 as a candidate explanation of the run-level residual; Limitations listed it as not run).
Pre-run entry: manuscript/analysis_record.md, "Run-level mean cross-lag deviation and the regional sts–r₁ test:
pre-run entry, 15 Sep 2026" (prediction recorded there).

Per subject and run, from the run-level 4 × 4 correlation matrices of every pair (all finite TRs of the run,
the matrices of partB4_diagnostic.py's run-level rows): the mean over the 6,555 pairs of
    corr(x_t, y_{t+1}) − a_y q   and   corr(y_t, x_{t+1}) − a_x q,
where a_x = corr(x_t, x_{t+1}), a_y = corr(y_t, y_{t+1}) are the run-level lag-1 autocorrelations and q the mean
of the two lag-0 correlations, exactly as the diagnostic defines them. Both variants. Reported: the per-run
means (DMT, placebo), the grand mean over the 28 runs with a subject-bootstrap 95 % CI (10,000 draws, seed
20261120) and an exact sign-flip p over the 14 subjects (2^14 assignments, two-sided, on the per-subject mean of
the two runs), the SD of the deviation across pairs for scale, the run-level residual of the diagnostic for the
same runs, and the correlation of the deviation with that residual across the 28 runs.

Outputs: notes/review_results/partB/crosslag_deviation_tables.md, crosslag_deviation.csv (one row per run),
crosslag_deviation_run.log (via run_all.sh's nstep, or stdout).
Run from the repository root: .venv/bin/python notes/partB10_crosslag_deviation.py   (about a minute)
"""
import subprocess
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS

REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
OUT = REPO / "notes" / "review_results" / "partB"
OUT.mkdir(parents=True, exist_ok=True)
REGIONS = np.array([r for r in range(116) if r != 20])
S = ATOMS.index("sts")
SEED = 20261120
N_BOOT = 10000
CONDITIONS = ("DMT", "PCB")

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=REPO).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "notes/*.py", "manuscript/analysis_record.md"],
                               text=True, cwd=REPO).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

lines = [f"# Run-level mean cross-lag deviation (partB10_crosslag_deviation.py; git={sha}; seed={SEED})", "",
         "Per subject and run, mean over the 6,555 pairs of corr(x_t, y_(t+1)) − a_y q and corr(y_t, x_(t+1)) − a_x q, from the "
         "run-level 4 × 4 correlation matrices (all finite TRs of the run; a_x, a_y and q as in partB4_diagnostic.py). "
         "Prediction recorded before the run (analysis_record.md, pre-run entry of 15 Sep 2026): negative on ts_gsr and near zero "
         "on ts_demean if pooling of non-stationary segments explains the run-level residual; near zero on both otherwise. "
         "'Near zero' = subject-bootstrap 95 % CI includes zero.", ""]
rows = []
ts = sio.loadmat(MAT)
rng = np.random.default_rng(SEED)
t0 = time.time()
for var in ("ts_gsr", "ts_demean"):
    dev = np.full((14, 2), np.nan); dev_sd = np.full((14, 2), np.nan); dev_abs = np.full((14, 2), np.nan)
    obs = np.full((14, 2), np.nan); pred = np.full((14, 2), np.nan)
    a_mean = np.full((14, 2), np.nan); q_abs = np.full((14, 2), np.nan)
    for s, c in product(range(14), range(2)):
        X = np.asarray(ts[var][s, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        pp = PairPhiID(X[:, kept]); C = pp.C
        ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
        d = np.r_[C[:, 0, 3] - ay * q, C[:, 1, 2] - ax * q]
        dev[s, c] = d.mean(); dev_sd[s, c] = d.std(); dev_abs[s, c] = np.abs(d).mean()
        obs[s, c] = pp.atoms_mean()[:, S].mean(); pred[s, c] = atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean()
        a_mean[s, c] = (0.5 * (ax + ay)).mean(); q_abs[s, c] = np.abs(q).mean()
        rows.append(dict(variant=var, subject=s + 1, condition=CONDITIONS[c], n_trs=int(kept.size), mean_crosslag_deviation=dev[s, c],
                         sd_across_pairs=dev_sd[s, c], mean_abs_deviation=dev_abs[s, c], observed_sts=obs[s, c], predicted_sts=pred[s, c],
                         residual=obs[s, c] - pred[s, c], mean_pair_a=a_mean[s, c], mean_pair_abs_q=q_abs[s, c]))
    res = obs - pred
    per_subj = dev.mean(1)                                   # mean of the two runs
    grand = per_subj.mean()
    boot = per_subj[rng.integers(0, 14, (N_BOOT, 14))].mean(1)
    lo, hi = np.percentile(boot, [2.5, 97.5])
    signs = ((np.arange(1 << 14)[:, None] >> np.arange(14)) & 1) * 2 - 1        # 16,384 sign assignments
    null = (signs * per_subj).mean(1)
    p_flip = np.mean(np.abs(null) >= abs(grand) - 1e-15)
    r_res = np.corrcoef(dev.ravel(), res.ravel())[0, 1]
    lines.append(f"## {var}")
    lines.append("")
    lines.append(f"Mean cross-lag deviation: DMT {dev[:, 0].mean():+.5f}, PCB {dev[:, 1].mean():+.5f}; grand mean {grand:+.5f} "
                 f"[{lo:+.5f}, {hi:+.5f}] (subject bootstrap, {N_BOOT} draws), exact sign-flip p = {p_flip:.4f}, "
                 f"positive in {int((per_subj > 0).sum())}/14 subjects. SD of the deviation across pairs within a run {dev_sd.mean():.4f}; "
                 f"mean absolute deviation {dev_abs.mean():.4f}. Run-level residual of the diagnostic on the same runs: {res.mean():+.4f} "
                 f"({100 * res.mean() / obs.mean():+.1f} % of observed {obs.mean():.4f}); r(deviation, residual) across the 28 runs {r_res:+.3f}. "
                 f"Mean pair a {a_mean.mean():.4f}, mean pair |q| {q_abs.mean():.4f}.")
    lines.append(f"Per-subject mean deviation (two runs): {np.array2string(per_subj, precision=5, floatmode='fixed', max_line_width=250)}")
    verdict = "near zero (CI includes zero)" if lo <= 0 <= hi else ("negative" if grand < 0 else "positive")
    lines.append(f"Reading under the pre-run entry: {verdict}.")
    lines.append("")
    print("\n".join(lines[-5:]), flush=True)
print(f"done in {time.time() - t0:.0f} s")
pd.DataFrame(rows).to_csv(OUT / "crosslag_deviation.csv", index=False)
(OUT / "crosslag_deviation_tables.md").write_text("\n".join(lines) + "\n")
print(f"wrote {OUT / 'crosslag_deviation_tables.md'} and crosslag_deviation.csv")
