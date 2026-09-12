"""
00_verify.py — confirm the data and method are intact before doing any science.

Re-run this whenever the environment changes. If it fails, nothing downstream
is trustworthy.
"""

import itertools
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

DATA = Path("external/DMT_NCT/data")
SEED = 20261120
np.random.seed(SEED)

ok = True


def check(label, condition, detail=""):
    global ok
    mark = "PASS" if condition else "FAIL"
    if not condition:
        ok = False
    print(f"  [{mark}] {label}" + (f"  {detail}" if detail else ""))


print("=" * 62)
print("DATA")
print("=" * 62)

check("data directory present", DATA.is_dir(), str(DATA))
if not DATA.is_dir():
    sys.exit("Data missing. Run setup.sh first.")

ts_file = DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
d = sio.loadmat(ts_file)

for variant in ("ts", "ts_demean", "ts_gsr", "ts_z"):
    check(f"variant '{variant}' present", variant in d)

ts = d["ts_gsr"]
check("shape is (14 subjects, 2 conditions)", ts.shape == (14, 2), str(ts.shape))

X = ts[0, 0]
check("timeseries is (116 regions, 840 TRs)", X.shape == (116, 840), str(X.shape))
check("timeseries is finite", np.all(np.isfinite(X)))

r = sio.loadmat(DATA / "intensity_ratings.mat")
dmt_i = r["dmt_intensity"].astype(float)
pcb_i = r["pcb_intensity"].astype(float)

check("DMT ratings are (14, 28)", dmt_i.shape == (14, 28), str(dmt_i.shape))
check("ratings are per-subject, not group-mean", dmt_i.std(axis=0).sum() > 0)
check(
    "TRs divide evenly into rating bins",
    X.shape[1] % dmt_i.shape[1] == 0,
    f"{X.shape[1] // dmt_i.shape[1]} TRs per bin",
)
check("DMT intensity exceeds placebo", dmt_i.mean() > pcb_i.mean() * 5,
      f"DMT {dmt_i.mean():.2f} vs PCB {pcb_i.mean():.2f}")

sc = sio.loadmat(DATA / "Schaefer116_HCP_DTI_count.mat")
check("structural connectome is (116, 116)", sc["connectivity"].shape == (116, 116))

ht = sio.loadmat(DATA / "5HTvecs_sch116.mat")
check("5-HT2A map present and (116, 1)", ht["mean5HT2A_sch116"].shape == (116, 1))

fd = sio.loadmat(DATA / "FDlong.mat")
check("framewise displacement is (840, 14)", fd["FDDMT"].shape == (840, 14))

print()
print("=" * 62)
print("METHOD")
print("=" * 62)

try:
    from phyid.calculate import calc_PhiID
    from phyid.utils import PhiID_atoms_abbr
    check("phyid imports", True)
except ImportError as e:
    check("phyid imports", False, str(e))
    sys.exit("phyid missing. pip install git+https://github.com/Imperial-MIND-lab/integrated-info-decomp.git")

atoms, _ = calc_PhiID(X[0, :], X[1, :], tau=1, kind="gaussian", redundancy="MMI")
calc = np.array([atoms[a] for a in PhiID_atoms_abbr])

check("returns 16 atoms", calc.shape[0] == 16, str(calc.shape))
check("atoms are finite", np.all(np.isfinite(calc)))
check("synergy atom 'sts' present", "sts" in atoms)
check("redundancy atom 'rtr' present", "rtr" in atoms)

t0 = time.time()
for i, j in itertools.combinations(range(12), 2):
    calc_PhiID(X[i, :], X[j, :], tau=1, kind="gaussian", redundancy="MMI")
per_pair = (time.time() - t0) / 66
full_min = per_pair * 6670 * 14 * 2 / 60

print(f"  [INFO] {per_pair * 1000:.1f} ms/pair")
print(f"  [INFO] full pairwise run ~{full_min:.1f} min single-core")
check("full run under 60 min", full_min < 60)

print()
print("=" * 62)
print("ALL CHECKS PASSED" if ok else "SOMETHING FAILED — fix before proceeding")
print("=" * 62)
sys.exit(0 if ok else 1)
