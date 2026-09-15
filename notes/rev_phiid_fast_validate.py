"""
rev_phiid_fast_validate.py — check rev_phiid_fast against the saved phyid outputs:
  (1) window means, W = 60, both variants, raw: results/atoms_win60_115regions-all_<v>_window.npy
  (2) window means, W = 30, ts_gsr, raw: results/atoms_win30_115regions-all_ts_gsr_window.npy
  (3) global-fit bin means, both variants, raw: results/atoms_bins_115regions-all_<v>_global.npy
  (4) 11's per-region global-fit sts and rtr, both variants, raw:
      results/regional_atoms_bins_115regions-all_<v>_global.npy  (14, 2, 28, 115, 2)
  (5) the deconvolved W60 window means and global bin means in notes/review_results/deconv/
  (6) 200 random (pair, window) draws compared directly with phyid.calc_PhiID, all 16 atoms
Prints the max absolute difference of each check and the time taken.
"""
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, incidence, ATOMS
from phyid.calculate import calc_PhiID

REPO = Path(__file__).resolve().parents[1]
RES = REPO / "results"
DEC = REPO / "notes" / "review_results" / "deconv"
MAT = "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
rng = np.random.default_rng(20261120)


def kept_trs(X):
    return np.where(np.all(np.isfinite(X), axis=0))[0]


def window_means(ts_obj, W):
    out = np.full((14, 2, 840 // W, 16), np.nan)
    per_region = np.full((14, 2, 840 // W, 115, 16), np.nan)
    inc = None
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts_obj[s, c], float)[REGIONS]
            kept = kept_trs(X)
            for w in range(840 // W):
                in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                if inc is None:
                    inc = incidence(115, pp.pairs)
                a = pp.atoms_mean()
                out[s, c, w] = a.mean(0)
                per_region[s, c, w] = (inc @ a) / 114.0
    return out, per_region


def bin_means(ts_obj):
    out = np.full((14, 2, 28, 16), np.nan)
    per_region = np.full((14, 2, 28, 115, 16), np.nan)
    inc = None
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts_obj[s, c], float)[REGIONS]
            kept = kept_trs(X)
            pp = PairPhiID(X[:, kept])
            if inc is None:
                inc = incidence(115, pp.pairs)
            slot = kept[:pp.n] // 30
            ab = pp.atoms_bins(slot, 28)                     # (28, n_pairs, 16)
            out[s, c] = np.nanmean(ab, axis=1)
            for t in range(28):
                if np.isfinite(ab[t]).all():
                    per_region[s, c, t] = (inc @ ab[t]) / 114.0
    return out, per_region


def report(name, a, b):
    m = np.isfinite(a) & np.isfinite(b)
    print(f"  {name:70s} max|diff| = {np.nanmax(np.abs(a[m] - b[m])):.2e}   (nan pattern equal: {np.array_equal(np.isfinite(a), np.isfinite(b))})")


t0 = time.time()
raw = sio.loadmat(REPO / "external" / "DMT_NCT" / "data" / MAT)
print("== raw data")
for var in ("ts_gsr", "ts_demean"):
    wm, wr = window_means(raw[var], 60)
    report(f"(1) W60 window means vs saved, {var}", wm, np.load(RES / f"atoms_win60_115regions-all_{var}_window.npy"))
    if var == "ts_gsr":
        wm30, _ = window_means(raw[var], 30)
        report("(2) W30 window means vs saved, ts_gsr", wm30, np.load(RES / "atoms_win30_115regions-all_ts_gsr_window.npy"))
    bm, br = bin_means(raw[var])
    report(f"(3) global bin means vs saved, {var}", bm, np.load(RES / f"atoms_bins_115regions-all_{var}_global.npy"))
    reg = np.load(RES / f"regional_atoms_bins_115regions-all_{var}_global.npy")
    report(f"(4) 11's per-region global sts vs closed form, {var}", br[..., ATOMS.index("sts")], reg[..., 0])
    report(f"(4) 11's per-region global rtr vs closed form, {var}", br[..., ATOMS.index("rtr")], reg[..., 1])
    print(f"     ({time.time() - t0:.0f}s)")

print("== deconvolved data")
dec_mat = next((p for p in (DEC / MAT, REPO.parent / "deconv_run" / "sandbox" / "external" / "DMT_NCT" / "data" / MAT) if p.exists()), None)
if dec_mat is not None:
    dec = sio.loadmat(dec_mat)
    for var in ("ts_gsr", "ts_demean"):
        wm, _ = window_means(dec[var], 60)
        report(f"(5) deconvolved W60 window means vs saved, {var}", wm, np.load(DEC / f"atoms_win60_115regions-all_{var}_window.npy"))
        bm, _ = bin_means(dec[var])
        report(f"(5) deconvolved global bin means vs saved, {var}", bm, np.load(DEC / f"atoms_bins_115regions-all_{var}_global.npy"))
        print(f"     ({time.time() - t0:.0f}s)")
else:
    print("  deconvolved .mat not present; skipped")

print("== (6) direct comparison with phyid.calc_PhiID on 200 random (subject, condition, window, pair) draws, W = 60, ts_gsr")
worst = 0.0
for _ in range(200):
    s, c, w = rng.integers(14), rng.integers(2), rng.integers(14)
    X = np.asarray(raw["ts_gsr"][s, c], float)[REGIONS]
    kept = kept_trs(X)
    in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
    pp = PairPhiID(X[:, in_w])
    k = rng.integers(len(pp.pairs))
    i, j = pp.pairs[k]
    ref, _ = calc_PhiID(X[i, in_w], X[j, in_w], tau=1, kind="gaussian", redundancy="MMI")
    mine = pp.atoms_mean()[k]
    worst = max(worst, max(abs(np.mean(ref[n]) - mine[a]) for a, n in enumerate(ATOMS)))
print(f"  max|diff| over 200 draws × 16 atoms = {worst:.2e}")
print(f"done in {time.time() - t0:.0f}s")
