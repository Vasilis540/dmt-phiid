"""
07_windowed_atoms_did.py — rtr, total TDMI and the other independently moving
atoms under the windowed W = 60 estimator, same DiD form and tests as sts.

Purpose: the global-fit results recorded in CLAUDE.md (Robustness A, ts_gsr)
were rtr DiD −0.0091 (peak bins 9–14 vs pre bins 1–8) and total TDMI DiD
−0.118. This script reports the same quantities under the windowed estimator
(atoms_win60_*_window.npy) with the Primary B inference machinery: per-subject
DiD = (post − pre)_DMT − (post − pre)_PCB, exact sign-flip test over 2^14
assignments (two-sided), subject-bootstrap 95 % CI (N_BOOT draws). No temporal
null and no motion handling here: this is a descriptive comparison of
estimators, not a new claim.

Window sets, matching 06: pre = windows 1–4; post primary = windows 6–14;
sensitivity = windows 5–14. For comparability with the recorded global-fit
numbers a third set, "peak" = windows 5–7 (bins 9–14), is also reported, and
the global-fit atoms file is re-summarised on the identical bin sets so the
two estimators are compared like for like (pre bins 1–8; primary bins 11–28;
sensitivity bins 9–28; peak bins 9–14).

Atoms reported: sts, rtr, total (sum of 16 atoms = TDMI), xtx, yty (the
within-region self-transfer atoms that carried most of the remaining global-
fit decrease), rts (mirrored by xts/yts/stx/sty and cancelling in the total).
Output: results/windowed_atoms_did_{variant}_win{W}.csv.
"""

import argparse
import csv
import subprocess
from itertools import product
from pathlib import Path

import numpy as np

from phyid.utils import PhiID_atoms_abbr as ATOMS

SEED = 20261120
N_BOOT = 10000
N_SUBJ = 14
REPORT = ("sts", "rtr", "total", "xtx", "yty", "rts")

ap = argparse.ArgumentParser()
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean", "ts_z", "ts"))
ap.add_argument("--window-trs", type=int, default=60, choices=(60,))
args = ap.parse_args()
V, W = args.variant, args.window_trs

RESULTS = Path("results")
WIN_NPY = RESULTS / f"atoms_win{W}_115regions-all_{V}_window.npy"
GLOBAL_NPY = RESULTS / f"atoms_bins_115regions-all_{V}_global.npy"
OUT_CSV = RESULTS / f"windowed_atoms_did_{V}_win{W}.csv"

# window / bin index sets (0-based)
SETS_WIN = {"primary": (np.arange(0, 4), np.arange(5, 14)),
            "sensitivity": (np.arange(0, 4), np.arange(4, 14)),
            "peak(bins 9-14)": (np.arange(0, 4), np.arange(4, 7))}
SETS_BIN = {"primary": (np.arange(0, 8), np.arange(10, 28)),
            "sensitivity": (np.arange(0, 8), np.arange(8, 28)),
            "peak(bins 9-14)": (np.arange(0, 8), np.arange(8, 14))}

rng = np.random.default_rng(SEED)
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))


def series(a, name):
    """(14, 2, n_t) for one reported quantity from an atoms array (14, 2, n_t, 16)."""
    return a.sum(-1) if name == "total" else a[..., ATOMS.index(name)]


def did(x, pre, post):
    ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
    return ch[:, 0] - ch[:, 1]


def boot_ci(v):
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def signflip_p(v):
    return float(np.mean(np.abs((_SIGNS * v).mean(1)) >= abs(v.mean()) - 1e-12))


try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "CLAUDE.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

win = np.load(WIN_NPY)
glb = np.load(GLOBAL_NPY)
assert win.shape == (N_SUBJ, 2, 840 // W, 16) and glb.shape == (N_SUBJ, 2, 28, 16), (win.shape, glb.shape)
print(f"variant={V} W={W}  windowed={WIN_NPY.name}  global={GLOBAL_NPY.name}  git={sha}")

rows = []
for est, a, sets in (("windowed", win, SETS_WIN), ("global", glb, SETS_BIN)):
    for label, (pre, post) in sets.items():
        print(f"\n[{est}, {label}]  {'atom':6s} {'pre DMT':>8s} {'pre PCB':>8s} {'DMT ch':>8s} {'PCB ch':>8s} "
              f"{'DiD':>8s} {'CI lo':>8s} {'CI hi':>8s} {'p':>7s}  neg/14")
        for name in REPORT:
            x = series(a, name)
            ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
            d = did(x, pre, post)
            lo, hi = boot_ci(d)
            p = signflip_p(d)
            pre_dmt, pre_pcb = x[:, 0, pre].mean(), x[:, 1, pre].mean()
            print(f"  {'':22s}{name:6s} {pre_dmt:8.4f} {pre_pcb:8.4f} {ch[:, 0].mean():+8.4f} {ch[:, 1].mean():+8.4f} "
                  f"{d.mean():+8.4f} {lo:+8.4f} {hi:+8.4f} {p:7.4f}  {(d < 0).sum()}")
            rows.append(dict(estimator=est, window_set=label, atom=name, pre_dmt=pre_dmt, pre_pcb=pre_pcb,
                             change_dmt=ch[:, 0].mean(), change_pcb=ch[:, 1].mean(), did_mean=d.mean(),
                             ci_lo=lo, ci_hi=hi, p_signflip=p, n_negative=int((d < 0).sum()),
                             did_over_pre_dmt=d.mean() / pre_dmt))

with open(OUT_CSV, "w") as fh:
    fh.write(f"# script=07_windowed_atoms_did.py variant={V} window_trs={W} n_boot={N_BOOT} seed={SEED} "
             f"windowed_file={WIN_NPY.name} global_file={GLOBAL_NPY.name} git={sha}\n")
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"\nwrote {OUT_CSV}")
