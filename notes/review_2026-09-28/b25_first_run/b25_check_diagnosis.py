"""
b25_check_diagnosis.py — the check that B25's first run failed, recomputed three ways (record, "The binarised
estimators on the AR(1) family (B25): the first run and the correction of one check").

The first run's check compared, for each of the sixteen atoms, two means over the 99,999 samples of each of the ten
series of 10⁵ samples at the operating point (0.85, 0.25): the mean of phyid's local CCS atoms (numpy's mean of a
one-dimensional array, which sums pairwise) and the atoms of the mean of the local knowns recomputed from phyid's local
mutual informations under its mask (numpy's mean over the first axis of a two-dimensional array, which adds the terms
one after another). This script draws the ten series again as the run draws them (np.random.default_rng(20261120),
whose first draws are these series), with the definitions it takes from notes/partB25_binarised.py (the simulation, the
seed, the operating point, phyid's call, the knowns and the map from the knowns to the atoms), which the correction left
unchanged, and prints for each series the largest difference over the sixteen atoms
  (i)   as the first run's check computed it (its two lines, which the correction replaced, are restated below);
  (ii)  with each of the two means from an exact sum (math.fsum, rounded once), which leaves the difference between the
        two sides that no rounding of a sum over the samples makes;
  (iii) sample by sample: phyid's local CCS atoms against the atoms of the recomputed local knowns, what the corrected
        check compares;
and, beside them, how far the means of each side of (i) lie from their exact-sum values (the largest over the sixteen
knowns, and over the sixteen atoms), and the largest mean absolute local known.

Run from the repository root: .venv/bin/python notes/review_2026-09-28/b25_first_run/b25_check_diagnosis.py
About ten seconds. It writes nothing; its output is b25_check_diagnosis.out beside it.
"""
import math
import platform
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[3]
SRC = REPO / "notes" / "partB25_binarised.py"
src = SRC.read_text(encoding="utf-8")
ns = {"__file__": str(SRC), "__name__": "partB25_definitions"}
exec(compile(src[:src.index("\nif SELFTEST:")], str(SRC), "exec"), ns)   # the definitions only: nothing is run
import phyid  # noqa: E402  (imported by the definitions above; named here for its version)
import scipy  # noqa: E402

print(f"python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}, phyid {phyid.__version__}")
calc_PhiID, KN_CODE, MINV_T, ATOMS = ns["calc_PhiID"], ns["KN_CODE"], ns["_MINV_T"], ns["ATOMS"]
simulate_family, SEED, OP = ns["simulate_family"], ns["SEED"], ns["OP"]
rng = np.random.default_rng(SEED)
n = 100_000
worst = [0.0, 0.0, 0.0]
print(f"ten series of {n:,} samples at the operating point {OP}; each value the largest over the sixteen atoms (in the "
      f"column of the knowns' means, over the sixteen knowns)")
print("| series | (i) as the first run's check | (ii) exact sums | (iii) sample by sample | mean of the knowns (first "
      "axis) − exact | mean of the atoms (pairwise) − exact | largest mean \\|local known\\| |")
print("|---|---|---|---|---|---|---|")
for s in range(10):
    x, y = simulate_family(OP[0], OP[1], rng.standard_normal((2, n)))
    at_c, cr = calc_PhiID(x, y, 1, kind="discrete", redundancy="CCS")
    Kc, _, _ = KN_CODE(cr["I_res"])
    mean_c = np.array([np.mean(at_c[k]) for k in ATOMS])
    # (i): the first run's two lines, as they stood in phyid_quantities at 820cacd
    rec_c = Kc.mean(0) @ MINV_T
    dev_i = float(np.max(np.abs(rec_c - mean_c)))
    A = np.stack([at_c[k] for k in ATOMS], axis=-1)
    m = Kc.shape[0]
    K_exact = np.array([math.fsum(Kc[:, j]) for j in range(Kc.shape[1])]) / m
    A_exact = np.array([math.fsum(A[:, j]) for j in range(A.shape[1])]) / m
    dev_ii = float(np.max(np.abs(K_exact @ MINV_T - A_exact)))
    dev_iii = float(np.max(np.abs(Kc @ MINV_T - A)))
    e_k = float(np.max(np.abs(Kc.mean(0) - K_exact)))
    e_a = float(np.max(np.abs(mean_c - A_exact)))
    worst = [max(w, d) for w, d in zip(worst, (dev_i, dev_ii, dev_iii))]
    print(f"| {s + 1} | {dev_i:.3g} | {dev_ii:.3g} | {dev_iii:.3g} | {e_k:.3g} | {e_a:.3g} | "
          f"{float(np.max(np.mean(np.abs(Kc), 0))):.3g} |", flush=True)
print(f"largest over the ten series: (i) {worst[0]:.3g}; (ii) {worst[1]:.3g}; (iii) {worst[2]:.3g}; the tolerance 1e-12")
