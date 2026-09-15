"""
partB1_overlay_points.py — the per-pair (r1, q) overlay points of the B1 scope map, saved so that
scripts/15_figures_v2.py draws Figure 2 from saved results only (B1 left them uncommitted).
For subject 1 (index 0), ts_gsr, DMT window 6 and placebo window 2 (W = 60; the two windows of the
B1/B2 per-pair checks), and the pooled pre-injection windows 1–4 of both runs: r1 = mean of the two
regions' within-window lag-1 autocorrelations, q = the pair's within-window lag-0 correlation (mean of
the past- and future-block values), observed window sts, all 6,555 pairs.
Output: notes/review_results/partB/scope_map_overlay_points.npz
Run from the repository root: .venv/bin/python notes/partB1_overlay_points.py
"""
import sys
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, ATOMS

REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
ts = sio.loadmat(MAT)["ts_gsr"]
out = {}
for name, cells in (("dmt_w6", [(0, 0, 5)]), ("pcb_w2", [(0, 1, 1)]), ("pre_w1to4", [(0, c, w) for c in (0, 1) for w in range(4)])):
    r1, q, sts = [], [], []
    for (s, c, w) in cells:
        X = np.asarray(ts[s, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
        pp = PairPhiID(X[:, in_w])
        r1.append(0.5 * (pp.C[:, 0, 2] + pp.C[:, 1, 3])); q.append(0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])); sts.append(pp.atoms_mean()[:, IX["sts"]])
    out[f"{name}_r1"], out[f"{name}_q"], out[f"{name}_sts"] = np.concatenate(r1), np.concatenate(q), np.concatenate(sts)
    print(f"{name}: n = {out[f'{name}_r1'].size}, r1 median {np.median(out[f'{name}_r1']):.3f}, |q| median {np.median(np.abs(out[f'{name}_q'])):.3f}")
np.savez(REPO / "notes" / "review_results" / "partB" / "scope_map_overlay_points.npz", **out)
