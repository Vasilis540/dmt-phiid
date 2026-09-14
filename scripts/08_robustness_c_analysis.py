"""
08_robustness_c_analysis.py — inference for Robustness C (placebo-fitted model).

Robustness C (manuscript/analysis_record.md, "Robustness C (placebo-fitted model)"): per subject
and pair, the Gaussian is fitted on the FIRST HALF of that subject's placebo run
(PCB TRs 0-419), the MMI selections are fixed from that model, and local atoms
are evaluated under that one model on the held-out placebo half (TRs 420-839,
i.e. bins 15-28) and on the FULL DMT run (bins 1-28). Both evaluations are
therefore OUT-OF-SAMPLE under a model fitted to a different segment, which is
what the split-half design was for: local entropy is a negative log-likelihood,
so in-sample data score systematically lower than held-out data regardless of
any drug effect, and only an out-of-sample-vs-out-of-sample comparison is
symmetric.

Because PCB has no pre-injection evaluation (bins 1-14 are in-sample and are
not scored), the Primary B difference-in-differences form does not apply. What
C can show, and what this script reports, on the whole-brain pair-mean atoms
from atoms_bins_115regions-all_{variant}_placebo.npy:

  (i)  the within-DMT step: DMT bins 11-28 minus DMT bins 1-8 (primary; bins
       9-28 vs 1-8 as sensitivity, matching the Primary B post sets), per
       subject, both segments scored under the placebo-fitted model;
  (ii) the between-condition comparison on MATCHED out-of-sample bins: DMT
       minus PCB on bins 15-28, per subject, both scored under the same
       subject's placebo-fitted model.

Tests as in 06/07: exact sign-flip permutation over all 2^14 assignments
(two-sided), subject-bootstrap 95 % CI (N_BOOT draws, seed 20261120). The same
two contrasts are re-summarised from the native global fit
(atoms_bins_115regions-all_{variant}_global.npy) on the identical bins, as the
like-for-like reference: under the native fit each run is scored in-sample
under its own model. Atoms: sts, rtr, total (sum of 16 atoms = TDMI).
No temporal null and no motion handling: Robustness C is a check on the
estimator's model dependence, not a new claim. Nothing here is interpreted;
manuscript/analysis_record.md records the numbers.
Output: results/robustness_c_{variant}.csv.
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
N_BINS = 28
REPORT = ("sts", "rtr", "total")
PLACEBO_FIT_TRS = 420          # must match 01_synergy_timecourse.py
FIRST_OOS_BIN = PLACEBO_FIT_TRS // 30   # 0-based bin 14 = 1-based bin 15

ap = argparse.ArgumentParser()
ap.add_argument("--variant", default="ts_gsr", choices=("ts_gsr", "ts_demean", "ts_z", "ts"))
args = ap.parse_args()
V = args.variant

RESULTS = Path("results")
PLACEBO_NPY = RESULTS / f"atoms_bins_115regions-all_{V}_placebo.npy"
GLOBAL_NPY = RESULTS / f"atoms_bins_115regions-all_{V}_global.npy"
OUT_CSV = RESULTS / f"robustness_c_{V}.csv"

PRE = np.arange(0, 8)                      # bins 1-8
POST = {"primary (bins 11-28)": np.arange(10, 28),
        "sensitivity (bins 9-28)": np.arange(8, 28)}
MATCHED = np.arange(FIRST_OOS_BIN, 28)     # bins 15-28: PCB out-of-sample half

rng = np.random.default_rng(SEED)
_SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))


def series(a, name):
    return a.sum(-1) if name == "total" else a[..., ATOMS.index(name)]


def boot_ci(v):
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])


def signflip_p(v):
    return float(np.mean(np.abs((_SIGNS * v).mean(1)) >= abs(v.mean()) - 1e-12))


try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"], text=True).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

plc = np.load(PLACEBO_NPY)
glb = np.load(GLOBAL_NPY)
assert plc.shape == (N_SUBJ, 2, N_BINS, 16) and glb.shape == (N_SUBJ, 2, N_BINS, 16), (plc.shape, glb.shape)
# expected NaN pattern of the placebo-fitted file: DMT all bins scored; PCB
# bins 1-14 in-sample (not scored, NaN), bins 15-28 out-of-sample (scored).
assert np.all(np.isfinite(plc[:, 0])), "DMT must be scored on every bin"
assert np.all(np.isnan(plc[:, 1, :FIRST_OOS_BIN])), "PCB in-sample bins must be NaN"
assert np.all(np.isfinite(plc[:, 1, FIRST_OOS_BIN:])), "PCB out-of-sample bins must be scored"
assert np.all(np.isfinite(glb)), "global-fit file must be finite"
print(f"variant={V}  placebo-fitted={PLACEBO_NPY.name}  global={GLOBAL_NPY.name}  git={sha}")
print(f"PCB scored on bins {FIRST_OOS_BIN + 1}-28 only (fit on TRs 0-{PLACEBO_FIT_TRS - 1}); "
      f"DMT scored on bins 1-28. Both out-of-sample under the placebo-fitted model.")

rows = []


def report(estimator, contrast, name, v, level_a, level_b, label_a, label_b):
    lo, hi = boot_ci(v)
    p = signflip_p(v)
    rows.append(dict(estimator=estimator, contrast=contrast, atom=name,
                     level_a=level_a, level_b=level_b, label_a=label_a, label_b=label_b,
                     diff_mean=v.mean(), ci_lo=lo, ci_hi=hi, p_signflip=p,
                     n_negative=int((v < 0).sum()), diff_over_level_b=v.mean() / level_b))
    print(f"  {name:6s} {label_a:>14s}={level_a:8.4f} {label_b:>14s}={level_b:8.4f}  "
          f"diff={v.mean():+8.4f} [{lo:+8.4f}, {hi:+8.4f}]  p={p:7.4f}  neg/14={(v < 0).sum():2d}  "
          f"share={100 * v.mean() / level_b:+6.1f} %")


for est, a in (("placebo-fitted", plc), ("global (native fit, same bins)", glb)):
    for label, post in POST.items():
        print(f"\n[{est}]  (i) within-DMT step, {label} minus bins 1-8")
        for name in REPORT:
            x = series(a, name)[:, 0]                        # DMT
            v = x[:, post].mean(1) - x[:, PRE].mean(1)
            report(est, f"(i) within-DMT step, {label}", name, v,
                   x[:, post].mean(), x[:, PRE].mean(), "DMT post", "DMT pre")
    print(f"\n[{est}]  (ii) DMT minus PCB on matched out-of-sample bins {MATCHED[0] + 1}-28")
    for name in REPORT:
        x = series(a, name)
        v = x[:, 0, MATCHED].mean(1) - x[:, 1, MATCHED].mean(1)
        report(est, f"(ii) DMT minus PCB, bins {MATCHED[0] + 1}-28", name, v,
               x[:, 0, MATCHED].mean(), x[:, 1, MATCHED].mean(), "DMT", "PCB")

with open(OUT_CSV, "w") as fh:
    fh.write(f"# script=08_robustness_c_analysis.py variant={V} placebo_fit_trs={PLACEBO_FIT_TRS} "
             f"pre_bins=1-8 post_primary=11-28 post_sensitivity=9-28 matched_bins={MATCHED[0] + 1}-28 "
             f"n_boot={N_BOOT} seed={SEED} placebo_file={PLACEBO_NPY.name} global_file={GLOBAL_NPY.name} "
             f"git={sha}\n")
    w = csv.DictWriter(fh, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)
print(f"\nwrote {OUT_CSV}")
