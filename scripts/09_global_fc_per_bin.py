#!/usr/bin/env python3
"""
09_global_fc_per_bin.py — global functional connectivity per 30-TR bin.

For each subject, condition and 30-TR rating bin, the Pearson correlation of
every region pair (115 regions, region 20 excluded as in
01_synergy_timecourse.py; 6,555 pairs) is computed on that bin's TRs alone and
averaged over pairs. Non-finite TRs are dropped (subject index 2, PCB, TR 839).

Outputs (per variant):
  results/global_fc_bins_115regions-all_<variant>.npy   (14, 2, 28) mean r
  results/global_fc_bins_115regions-all_<variant>.csv   same, long format
  results/global_fc_did_<variant>.csv                   per-bin group means and
        the pre/post difference-in-differences with the exact sign-flip test
        and subject-bootstrap CI, alongside the whole-brain sts DiD from the
        global-fit atoms file on the identical bins (no interpretation).

Contrast form mirrors 06/07: per subject, (post - pre) on DMT minus
(post - pre) on PCB; pre = bins 1-8; post primary = bins 11-28,
sensitivity = bins 9-28, peak = bins 9-14 (1-based bin labels).
"""
import argparse
import subprocess
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio

SEED = 20261120
N_BOOT = 10000
EXCLUDE_REGIONS = (20,)
BIN_TRS = 30
N_BINS = 28
N_SUBJ = 14
STS = 15  # phyid atom index of sts in the atoms files

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean", "ts_z", "ts"))
args = ap.parse_args()
V = args.variant

DATA = Path("external/DMT_NCT/data")
RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)
rng = np.random.default_rng(SEED)

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

# ------------------------------------------------------------------ data
ts_all = sio.loadmat(DATA / f"DMT_clean_mni_continuous_fullPreprocsch116.mat")[V]
assert ts_all.shape == (N_SUBJ, 2)
n_total = ts_all[0, 0].shape[0]
region_idx = np.array([r for r in range(n_total) if r not in EXCLUDE_REGIONS])
n_regions = region_idx.size
n_pairs = n_regions * (n_regions - 1) // 2
iu = np.triu_indices(n_regions, 1)
print(f"variant={V} regions={n_regions} pairs={n_pairs} git={sha}")

fc = np.full((N_SUBJ, 2, N_BINS), np.nan)
n_tr_used = np.zeros((N_SUBJ, 2, N_BINS), int)
for s, c in product(range(N_SUBJ), range(2)):
    X = ts_all[s, c][region_idx]                  # (115, 840)
    assert X.shape[1] == BIN_TRS * N_BINS, X.shape
    for b in range(N_BINS):
        blk = X[:, b * BIN_TRS:(b + 1) * BIN_TRS]
        keep = np.all(np.isfinite(blk), axis=0)
        blk = blk[:, keep]
        n_tr_used[s, c, b] = blk.shape[1]
        if blk.shape[1] < 3:
            continue
        R = np.corrcoef(blk)
        fc[s, c, b] = R[iu].mean()
dropped = [(s, c, b, n) for (s, c, b), n in np.ndenumerate(n_tr_used) if n != BIN_TRS]
print(f"bins with fewer than {BIN_TRS} TRs (subject, cond, bin0, n): {dropped}")
assert np.isfinite(fc).all()

TAG = f"115regions-all_{V}"
np.save(RESULTS / f"global_fc_bins_{TAG}.npy", fc)
with open(RESULTS / f"global_fc_bins_{TAG}.csv", "w") as f:
    f.write(f"# 09_global_fc_per_bin.py variant={V} regions={n_regions} pairs={n_pairs} "
            f"excluded_regions={','.join(map(str, EXCLUDE_REGIONS))} bin_trs={BIN_TRS} git={sha}\n")
    f.write("subject,condition,bin,mean_r,n_tr\n")
    for s, c, b in product(range(N_SUBJ), range(2), range(N_BINS)):
        f.write(f"{s},{'DMT' if c == 0 else 'PCB'},{b + 1},{fc[s, c, b]:.6f},{n_tr_used[s, c, b]}\n")

# ------------------------------------------------------------------ stats
PRE = np.arange(0, 8)
SETS = {"primary_bins11-28": np.arange(10, 28),
        "sensitivity_bins9-28": np.arange(8, 28),
        "peak_bins9-14": np.arange(8, 14)}
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))


def signflip_p(v):
    v = np.asarray(v, float)
    obs = abs(v.mean())
    return float(np.mean(np.abs((_SIGNS * v).mean(1)) >= obs - 1e-12))


def boot_ci(v):
    v = np.asarray(v, float)
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def contrasts(x, post, label, unit):
    """x: (14, 2, 28). Returns rows for DMT change, PCB change, DiD."""
    change = x[:, :, post].mean(2) - x[:, :, PRE].mean(2)           # (14, 2)
    rows = []
    for name, v in (("DMT_post_minus_pre", change[:, 0]),
                    ("PCB_post_minus_pre", change[:, 1]),
                    ("DiD", change[:, 0] - change[:, 1])):
        lo, hi = boot_ci(v)
        rows.append((label, unit, name, v.mean(), lo, hi, signflip_p(v),
                     int((v < 0).sum()), int((v > 0).sum())))
    pre_dmt = x[:, 0, PRE].mean()
    pre_pcb = x[:, 1, PRE].mean()
    rows.append((label, unit, "pre_DMT_mean", pre_dmt, np.nan, np.nan, np.nan, 0, 0))
    rows.append((label, unit, "pre_PCB_mean", pre_pcb, np.nan, np.nan, np.nan, 0, 0))
    rows.append((label, unit, "post_DMT_mean", x[:, 0, post].mean(), np.nan, np.nan, np.nan, 0, 0))
    rows.append((label, unit, "post_PCB_mean", x[:, 1, post].mean(), np.nan, np.nan, np.nan, 0, 0))
    rows.append((label, unit, "DiD_share_of_pre_DMT", (change[:, 0] - change[:, 1]).mean() / pre_dmt,
                 np.nan, np.nan, np.nan, 0, 0))
    return rows


atoms_path = RESULTS / f"atoms_bins_115regions-all_{V}_global.npy"
sts = np.load(atoms_path)[:, :, :, STS] if atoms_path.exists() else None
if sts is None:
    print(f"[note] {atoms_path} not found; sts side-by-side column omitted")

rows = []
for label, post in SETS.items():
    rows += contrasts(fc, post, label, "mean_r")
    if sts is not None:
        rows += contrasts(sts, post, label, "sts_global_fit_nats")

gm = fc.mean(0)          # (2, 28)
gsd = fc.std(0, ddof=1)
out = RESULTS / f"global_fc_did_{V}.csv"
with open(out, "w") as f:
    f.write(f"# 09_global_fc_per_bin.py variant={V} regions={n_regions} pairs={n_pairs} "
            f"pre=bins1-8 sign-flip exact 2^14 two-sided; bootstrap {N_BOOT} draws seed={SEED}; "
            f"sts from {atoms_path.name if sts is not None else 'n/a'}; git={sha}\n")
    f.write("section,quantity,name,value,ci_lo,ci_hi,p_signflip,n_neg,n_pos\n")
    for b in range(N_BINS):
        f.write(f"per_bin,mean_r,DMT_bin{b + 1},{gm[0, b]:.6f},,,,,\n")
        f.write(f"per_bin,mean_r,PCB_bin{b + 1},{gm[1, b]:.6f},,,,,\n")
        f.write(f"per_bin,mean_r_sd_subjects,DMT_bin{b + 1},{gsd[0, b]:.6f},,,,,\n")
        f.write(f"per_bin,mean_r_sd_subjects,PCB_bin{b + 1},{gsd[1, b]:.6f},,,,,\n")
    for (label, unit, name, val, lo, hi, p, nn, npos) in rows:
        f.write(f"{label},{unit},{name},{val:.6f},{'' if np.isnan(lo) else f'{lo:.6f}'},"
                f"{'' if np.isnan(hi) else f'{hi:.6f}'},{'' if np.isnan(p) else f'{p:.4f}'},"
                f"{nn if name in ('DMT_post_minus_pre', 'PCB_post_minus_pre', 'DiD') else ''},"
                f"{npos if name in ('DMT_post_minus_pre', 'PCB_post_minus_pre', 'DiD') else ''}\n")

# ------------------------------------------------------------------ report
np.set_printoptions(precision=4, linewidth=150, suppress=True)
print("\nmean pairwise Pearson r per bin, 14-subject group mean")
print("bin :", " ".join(f"{b + 1:6d}" for b in range(N_BINS)))
print("DMT :", " ".join(f"{v:6.4f}" for v in gm[0]))
print("PCB :", " ".join(f"{v:6.4f}" for v in gm[1]))
print("D-P :", " ".join(f"{v:+6.4f}" for v in gm[0] - gm[1]))
print()
print(f"{'set':22s} {'quantity':22s} {'name':22s} {'value':>9s} {'ci_lo':>9s} {'ci_hi':>9s} {'p':>7s} neg pos")
for (label, unit, name, val, lo, hi, p, nn, npos) in rows:
    if name in ("DMT_post_minus_pre", "PCB_post_minus_pre", "DiD", "pre_DMT_mean", "pre_PCB_mean", "DiD_share_of_pre_DMT"):
        print(f"{label:22s} {unit:22s} {name:22s} {val:+9.4f} "
              f"{'' if np.isnan(lo) else f'{lo:+9.4f}':>9s} {'' if np.isnan(hi) else f'{hi:+9.4f}':>9s} "
              f"{'' if np.isnan(p) else f'{p:7.4f}':>7s} "
              f"{nn if name in ('DMT_post_minus_pre', 'PCB_post_minus_pre', 'DiD') else '':>3} "
              f"{npos if name in ('DMT_post_minus_pre', 'PCB_post_minus_pre', 'DiD') else '':>3}")
print(f"\nwrote {out}")
