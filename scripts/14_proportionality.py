"""
14_proportionality.py — is the DMT synergy decrease selective, or proportional
to the decrease in total time-delayed mutual information?

POST-HOC analysis, specified 14 Sep 2026 after the primary result (Primary B,
whole-brain sts DiD negative, tier 3) and reported regardless of outcome.
Not pre-registered; decides nothing about the primary claim.

Quantity. Per subject, condition and window (windowed W = 60 estimator) or
30-TR bin (global fit): ratio = sts / TDMI, where TDMI is the sum of all 16
ΦID atoms (the total time-delayed mutual information between the pair's
past and future, averaged over the 6,555 pairs as every atom is). Then the
same DiD form as the primary analysis on that ratio:
(post − pre)_DMT − (post − pre)_PCB, pre and post being the mean ratio over
the window set; exact sign-flip test across the 14 subjects (2^14
assignments, two-sided); subject-bootstrap 95 % CI (10,000 draws, seed
20261120). Four cells: windowed W = 60 on ts_gsr and ts_demean (pre =
windows 1–4, post = primary windows 6–14) and the global fit on both
variants (pre = bins 1–8, post = bins 11–28). No temporal null, no motion
handling.

Also reported per cell, so the two can be compared directly: (i) sts as a
share of TDMI at pre-injection baseline on the DMT run (per-subject share
averaged over subjects, with CI; and the ratio of group means), and (ii)
sts's share of the TDMI DiD, i.e. DiD_sts / DiD_TDMI on the group means,
with a subject-bootstrap CI of that ratio of means. Under exact
proportionality (ii) equals (i).

INTERPRETATION RULE, RECORDED BEFORE RUNNING.
- Ratio DiD with a 95 % CI including zero → synergy falls in proportion to
  total predictable information; no evidence of a selective effect on
  synergy.
- Ratio DiD significantly negative → synergy falls MORE than proportionally
  (a selective synergy reduction on top of the TDMI reduction).
- Ratio DiD significantly positive → synergy falls LESS than
  proportionally (the TDMI reduction is carried more by the other atoms).
- The directional refutation of the up-regulation hypothesis stands under
  all three outcomes: it concerns the sign of the sts change, not its
  selectivity.

Outputs: results/proportionality.csv (all cells), log
results/run_14_proportionality.log.
"""
import csv
import subprocess
from itertools import product
from pathlib import Path

import numpy as np

SEED = 20261120
N_BOOT = 10000
N_SUBJ = 14
STS = 15                                            # phyid atom order: rtr ... sts
RESULTS = Path("results")
OUT = RESULTS / "proportionality.csv"
CELLS = [  # (estimator, variant, atoms file, pre index set, post index set, unit)
    ("windowed_W60", "ts_gsr", "atoms_win60_115regions-all_ts_gsr_window.npy", np.arange(0, 4), np.arange(5, 14), "windows 1-4 vs 6-14"),
    ("windowed_W60", "ts_demean", "atoms_win60_115regions-all_ts_demean_window.npy", np.arange(0, 4), np.arange(5, 14), "windows 1-4 vs 6-14"),
    ("global_fit", "ts_gsr", "atoms_bins_115regions-all_ts_gsr_global.npy", np.arange(0, 8), np.arange(10, 28), "bins 1-8 vs 11-28"),
    ("global_fit", "ts_demean", "atoms_bins_115regions-all_ts_demean_global.npy", np.arange(0, 8), np.arange(10, 28), "bins 1-8 vs 11-28"),
]

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

rng = np.random.default_rng(SEED)
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))


def boot_idx():
    return rng.integers(0, N_SUBJ, (N_BOOT, N_SUBJ))


def boot_ci_mean(v):
    return np.percentile(v[boot_idx()].mean(1), [2.5, 97.5])


def boot_ci_ratio_of_means(num, den):
    """CI of mean(num)/mean(den) over subject resamples; the same resample is used for both."""
    idx = boot_idx()
    r = num[idx].mean(1) / den[idx].mean(1)
    return np.percentile(r, [2.5, 97.5])


def signflip_p(v):
    obs = abs(v.mean())
    return float(np.mean(np.abs((_SIGNS * v).mean(1)) >= obs - 1e-12))


def did(x, pre, post):
    """x: (14, 2, T) → per-subject (post − pre)_DMT − (post − pre)_PCB, means over the index sets."""
    change = np.nanmean(x[:, :, post], axis=2) - np.nanmean(x[:, :, pre], axis=2)
    return change[:, 0] - change[:, 1]


rows = []


def rec(est, var, stat, value, lo=np.nan, hi=np.nan, p=np.nan, note=""):
    rows.append(dict(estimator=est, variant=var, statistic=stat, value=value, ci_lo=lo, ci_hi=hi, p=p, note=note))
    ci = f" [{lo:+.4f}, {hi:+.4f}]" if np.isfinite(lo) else ""
    pp = f"  p={p:.4f}" if np.isfinite(p) else ""
    print(f"  {stat:52s} {value:+.4f}{ci}{pp}  {note}")


print(f"14_proportionality.py git={sha} seed={SEED} n_boot={N_BOOT} signflip=exact 2^14 two-sided; POST-HOC")
for est, var, fname, pre, post, unit in CELLS:
    atoms = np.load(RESULTS / fname)                # (14, 2, T, 16)
    assert atoms.shape[:2] == (N_SUBJ, 2) and atoms.shape[3] == 16, atoms.shape
    sts = atoms[..., STS]
    tdmi = atoms.sum(axis=3)
    assert np.isfinite(sts).all() and np.isfinite(tdmi).all(), "non-finite atoms"
    assert (tdmi > 0).all(), "TDMI must be positive for the ratio"
    ratio = sts / tdmi                              # (14, 2, T)
    print(f"\n== {est}, {var}: {fname}, {unit}")

    d_ratio = did(ratio, pre, post)
    lo, hi = boot_ci_mean(d_ratio)
    p = signflip_p(d_ratio)
    verdict = ("proportional (CI includes zero)" if lo <= 0 <= hi
               else "MORE than proportional (ratio DiD < 0)" if hi < 0
               else "LESS than proportional (ratio DiD > 0)")
    rec(est, var, "ratio sts/TDMI: DiD", d_ratio.mean(), lo, hi, p,
        f"negative in {(d_ratio < 0).sum()}/14; {verdict}")
    for c, cname in enumerate(("DMT", "PCB")):
        ch = np.nanmean(ratio[:, c, post], axis=1) - np.nanmean(ratio[:, c, pre], axis=1)
        lo_c, hi_c = boot_ci_mean(ch)
        rec(est, var, f"ratio sts/TDMI: {cname} post - pre", ch.mean(), lo_c, hi_c, signflip_p(ch))

    # (i) baseline share on DMT
    share_pre = np.nanmean(sts[:, 0, pre], axis=1) / np.nanmean(tdmi[:, 0, pre], axis=1)   # per subject
    lo_s, hi_s = boot_ci_mean(share_pre)
    rec(est, var, "(i) sts share of TDMI, pre-injection DMT (subject mean)", share_pre.mean(), lo_s, hi_s,
        note=f"ratio of group means {np.nanmean(sts[:, 0, pre]) / np.nanmean(tdmi[:, 0, pre]):.4f}")
    share_pre_pcb = np.nanmean(sts[:, 1, pre], axis=1) / np.nanmean(tdmi[:, 1, pre], axis=1)
    rec(est, var, "sts share of TDMI, pre-injection PCB (subject mean)", share_pre_pcb.mean(), *boot_ci_mean(share_pre_pcb))

    # (ii) sts share of the TDMI DiD
    d_sts = did(sts, pre, post)
    d_tdmi = did(tdmi, pre, post)
    lo1, hi1 = boot_ci_mean(d_sts)
    rec(est, var, "sts DiD (nats)", d_sts.mean(), lo1, hi1, signflip_p(d_sts), f"negative in {(d_sts < 0).sum()}/14")
    lo2, hi2 = boot_ci_mean(d_tdmi)
    rec(est, var, "TDMI DiD (nats)", d_tdmi.mean(), lo2, hi2, signflip_p(d_tdmi), f"negative in {(d_tdmi < 0).sum()}/14")
    share_did = d_sts.mean() / d_tdmi.mean()
    lo_r, hi_r = boot_ci_ratio_of_means(d_sts, d_tdmi)
    rec(est, var, "(ii) sts share of TDMI DiD (ratio of group means)", share_did, lo_r, hi_r,
        note=f"compare with (i) {share_pre.mean():.4f}; bootstrap ratio CI is unstable if TDMI DiD draws cross zero")
    rec(est, var, "(ii) - (i)", share_did - share_pre.mean(),
        note="> 0: sts carries more of the TDMI drop than its baseline share")

with open(OUT, "w", newline="") as fh:
    fh.write(f"# script=14_proportionality.py git={sha} seed={SEED} n_boot={N_BOOT} signflip=exact 2^14 two-sided; "
             "POST-HOC analysis specified after the primary result; interpretation rule in the script docstring\n")
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
print(f"\nwrote {OUT}")
