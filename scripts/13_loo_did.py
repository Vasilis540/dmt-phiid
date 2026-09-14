"""
13_loo_did.py — leave-one-out robustness of the primary step-contrast DiD.

POST-HOC robustness check (specified 14 Sep 2026, after the Primary B result
was recorded). Motivation on record: on the primary windows one subject
(index 7, "subject 8") carries a DiD of about −0.28 against a group mean of
−0.08 (ts_gsr) and −0.31 against −0.10 (ts_demean), and one subject (index
13, "subject 14") is the only positive DiD on both variants. The question
is whether the group result depends on any single subject.

Statistic: the raw whole-brain mean sts DiD from the windowed W = 60
estimator, primary windows (pre = windows 1–4, post = windows 6–14),
exactly as `06_primary_b_analysis.py` computes it (same atoms file, same
window sets, same STS index). For each subject dropped in turn (14 refits
per variant): mean DiD over the remaining 13, subject-bootstrap 95 % CI
(10,000 draws, seed 20261120), exact sign-flip p over 2^13 = 8,192
assignments, two-sided. The full 14-subject fit is recomputed alongside as
a check that it reproduces the recorded value. Reported per variant: the
14 leave-one-out rows, the range of the leave-one-out mean, and whether
any leave-one-out CI includes zero.

Not pre-registered; decides nothing; reported regardless of outcome. No
motion handling, no temporal null (the raw DiD only, as asked).

Output: results/loo_did_win60.csv, log results/run_13_loo_did.log.
"""
import csv
import subprocess
from itertools import product
from pathlib import Path

import numpy as np

SEED = 20261120
N_BOOT = 10000
N_SUBJ, N_TRS, W = 14, 840, 60
N_WIN = N_TRS // W
STS = 15                       # phyid atom index of sts (as in 06)
PRE = np.arange(0, 4)          # windows 1–4
POST = np.arange(5, 14)        # windows 6–14 (primary)
VARIANTS = ("ts_gsr", "ts_demean")
RESULTS = Path("results")
OUT = RESULTS / "loo_did_win60.csv"

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

rng = np.random.default_rng(SEED)


def boot_ci(v):
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def signflip_p(v):
    signs = np.array(list(product((-1, 1), repeat=v.size)))
    obs = abs(v.mean())
    perm = np.abs((signs * v).mean(1))
    return float(np.mean(perm >= obs - 1e-12))


rows = []
print(f"13_loo_did.py git={sha} seed={SEED} W={W} pre={list(PRE + 1)} post={list(POST + 1)}")
for v in VARIANTS:
    atoms = np.load(RESULTS / f"atoms_win{W}_115regions-all_{v}_window.npy")
    assert atoms.shape == (N_SUBJ, 2, N_WIN, 16), atoms.shape
    sts = atoms[..., STS]
    change = sts[:, :, POST].mean(2) - sts[:, :, PRE].mean(2)
    d = change[:, 0] - change[:, 1]                       # (14,) per-subject DiD
    lo, hi = boot_ci(d)
    p = signflip_p(d)
    print(f"\n{v}: full 14-subject DiD {d.mean():+.4f} [{lo:+.4f}, {hi:+.4f}] p={p:.4f}; "
          f"negative in {(d < 0).sum()}/14")
    print("  per-subject DiD: " + " ".join(f"{x:+.3f}" for x in d))
    rows.append(dict(variant=v, dropped_subject="none", n=14, mean_did=d.mean(), ci_lo=lo, ci_hi=hi,
                     p_signflip=p, n_negative=int((d < 0).sum()), ci_includes_zero=bool(lo <= 0 <= hi),
                     dropped_subject_did=np.nan))
    loo_means = []
    for s in range(N_SUBJ):
        keep = np.delete(d, s)
        lo, hi = boot_ci(keep)
        p = signflip_p(keep)
        inc0 = bool(lo <= 0 <= hi)
        loo_means.append(keep.mean())
        print(f"  drop subject {s + 1:2d} (DiD {d[s]:+.3f}): mean {keep.mean():+.4f} "
              f"[{lo:+.4f}, {hi:+.4f}] p={p:.4f} neg {(keep < 0).sum()}/13"
              + ("  CI INCLUDES ZERO" if inc0 else ""))
        rows.append(dict(variant=v, dropped_subject=s + 1, n=13, mean_did=keep.mean(), ci_lo=lo, ci_hi=hi,
                         p_signflip=p, n_negative=int((keep < 0).sum()), ci_includes_zero=inc0,
                         dropped_subject_did=d[s]))
    loo_means = np.array(loo_means)
    print(f"  leave-one-out mean range: [{loo_means.min():+.4f}, {loo_means.max():+.4f}] "
          f"(least negative when dropping subject {loo_means.argmax() + 1}, "
          f"most negative when dropping subject {loo_means.argmin() + 1}); "
          f"CIs including zero: {sum(r['ci_includes_zero'] for r in rows if r['variant'] == v and r['n'] == 13)}/14")

with open(OUT, "w", newline="") as fh:
    fh.write(f"# script=13_loo_did.py git={sha} seed={SEED} window_trs={W} pre={list(PRE + 1)} "
             f"post={list(POST + 1)} n_boot={N_BOOT} signflip=exact 2^n two-sided; POST-HOC robustness check\n")
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(f"\nwrote {OUT}")
