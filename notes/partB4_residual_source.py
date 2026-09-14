"""
partB4_residual_source.py — Part B item 4, supplement: where the residual of the AR(1) prediction
comes from. At τ = 1 the closed-form atoms depend only on the 4 × 4 correlation matrix of
(x_t, y_t, x_{t+1}, y_{t+1}); the diagonal VAR(1) prediction of partB4_diagnostic.py keeps the
measured a_x = corr(x_t, x_{t+1}), a_y = corr(y_t, y_{t+1}) and q (mean of the two lag-0
correlations) and replaces (i) the two cross-lag entries corr(x_t, y_{t+1}), corr(y_t, x_{t+1})
by a_y q, a_x q and (ii) the two lag-0 entries by their mean q. This script applies the two
substitutions separately to every window (ts_gsr, W = 60, all subjects, both runs) and reports
which one carries the residual, the signed and absolute deviation of the measured cross-lag
correlations from a_y q / a_x q, and how those deviations move between the pre-injection and
primary windows (the residual DiD of the diagnostic can then be traced to them).

Output: notes/review_results/partB/residual_source.log (printed)
"""
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_inference import window_sets

REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
S = ATOMS.index("sts")
t0 = time.time()
ts = sio.loadmat(MAT)
W = 60
obs = np.full((14, 2, 14), np.nan); pred = np.full((14, 2, 14), np.nan)
p_cross = np.full((14, 2, 14), np.nan); p_lag0 = np.full((14, 2, 14), np.nan)
dev_signed = np.full((14, 2, 14), np.nan); dev_abs = np.full((14, 2, 14), np.nan); dev_sd = np.full((14, 2, 14), np.nan)
lag0_gap = np.full((14, 2, 14), np.nan); a_mean = np.full((14, 2, 14), np.nan); q_abs = np.full((14, 2, 14), np.nan)
for s in range(14):
    for c in range(2):
        X = np.asarray(ts["ts_gsr"][s, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        for w in range(14):
            in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
            if in_w.size <= 5:
                continue
            pp = PairPhiID(X[:, in_w]); C = pp.C.copy()
            ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
            obs[s, c, w] = pp.atoms_mean()[:, S].mean()
            pred[s, c, w] = atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean()
            CA = C.copy(); CA[:, 0, 3] = CA[:, 3, 0] = ay * q; CA[:, 1, 2] = CA[:, 2, 1] = ax * q          # cross-lag substitution only
            CB = C.copy(); CB[:, 0, 1] = CB[:, 1, 0] = q; CB[:, 2, 3] = CB[:, 3, 2] = q                   # lag-0 substitution only
            p_cross[s, c, w] = atoms_from_corr(CA)[:, S].mean(); p_lag0[s, c, w] = atoms_from_corr(CB)[:, S].mean()
            dev = np.r_[C[:, 0, 3] - ay * q, C[:, 1, 2] - ax * q]
            dev_signed[s, c, w] = dev.mean(); dev_abs[s, c, w] = np.abs(dev).mean(); dev_sd[s, c, w] = dev.std()
            lag0_gap[s, c, w] = np.abs(C[:, 0, 1] - C[:, 2, 3]).mean(); a_mean[s, c, w] = (0.5 * (ax + ay)).mean(); q_abs[s, c, w] = np.abs(q).mean()
    print(f"   subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
Sx = window_sets(W); PRE, POST = Sx["PRE"], Sx["primary"]
res = obs - pred
lines = ["# Residual source (partB4_residual_source.py; ts_gsr, W = 60, all subjects, both runs, 14 windows)", ""]
lines.append(f"Means over all cells: observed sts {np.nanmean(obs):.4f}; AR(1) prediction {np.nanmean(pred):.4f} (residual {np.nanmean(res):+.4f}); "
             f"cross-lag substitution only {np.nanmean(p_cross):.4f} (residual {np.nanmean(obs - p_cross):+.4f}); lag-0 substitution only {np.nanmean(p_lag0):.4f} (residual {np.nanmean(obs - p_lag0):+.4f}). "
             f"max |prediction − cross-lag-only| over cells {np.nanmax(np.abs(pred - p_cross)):.5f}.")
lines.append(f"Cross-lag deviation corr(x_t, y_(t+1)) − a_y q (and the y→x mirror), pooled over pairs: mean signed {np.nanmean(dev_signed):+.5f} (per-cell range {np.nanmin(dev_signed):+.4f} to {np.nanmax(dev_signed):+.4f}); "
             f"mean absolute {np.nanmean(dev_abs):.4f}; SD across pairs within a window {np.nanmean(dev_sd):.4f}. Mean |lag-0 correlation of the past block − of the future block| {np.nanmean(lag0_gap):.4f}. "
             f"Mean pair a {np.nanmean(a_mean):.3f}, mean pair |q| {np.nanmean(q_abs):.3f}. For reference, 1/sqrt(60) = {1 / np.sqrt(60):.3f}.")


def did(x):
    return ((x[:, 0, POST].mean(1) - x[:, 0, PRE].mean(1)) - (x[:, 1, POST].mean(1) - x[:, 1, PRE].mean(1)))


for name, x in (("residual", res), ("cross-lag |deviation|", dev_abs), ("cross-lag deviation SD", dev_sd), ("cross-lag signed deviation", dev_signed), ("pair a", a_mean), ("pair |q|", q_abs)):
    d = did(x)
    lines.append(f"{name}: DMT pre {x[:, 0, PRE].mean():+.4f} post {x[:, 0, POST].mean():+.4f}; PCB pre {x[:, 1, PRE].mean():+.4f} post {x[:, 1, POST].mean():+.4f}; primary DiD {d.mean():+.4f} (negative in {int((d < 0).sum())}/14)")
d_res, d_dev = did(res), did(dev_abs)
from scipy.stats import pearsonr
lines.append(f"Per subject: r(residual DiD, cross-lag |deviation| DiD) = {pearsonr(d_res, d_dev)[0]:+.3f}; r(residual DiD, cross-lag deviation SD DiD) = {pearsonr(d_res, did(dev_sd))[0]:+.3f}; r(residual DiD, pair a DiD) = {pearsonr(d_res, did(a_mean))[0]:+.3f}; r(residual DiD, pair |q| DiD) = {pearsonr(d_res, did(q_abs))[0]:+.3f}")
# per-window (cell-level) relation between residual and cross-lag scatter, pooled over all cells
m = np.isfinite(res) & np.isfinite(dev_sd)
lines.append(f"Across all {int(m.sum())} subject × run × window cells: r(residual, cross-lag deviation SD) = {pearsonr(res[m], dev_sd[m])[0]:+.3f}; r(residual, pair a) = {pearsonr(res[m], a_mean[m])[0]:+.3f}; r(residual, pair |q|) = {pearsonr(res[m], q_abs[m])[0]:+.3f}; "
             f"r(cross-lag deviation SD, pair a) = {pearsonr(dev_sd[m], a_mean[m])[0]:+.3f}")
# joint linear regression of the cell residual on standardised (a, |q|, scatter SD): standardised coefficients and partial correlations
Z = np.column_stack([a_mean[m], q_abs[m], dev_sd[m]]); Z = (Z - Z.mean(0)) / Z.std(0); y = (res[m] - res[m].mean()) / res[m].std()
beta = np.linalg.lstsq(np.column_stack([np.ones(len(y)), Z]), y, rcond=None)[0][1:]


def partial_r(k):
    others = np.column_stack([np.ones(len(y))] + [Z[:, j] for j in range(3) if j != k])
    ry = y - others @ np.linalg.lstsq(others, y, rcond=None)[0]; rk = Z[:, k] - others @ np.linalg.lstsq(others, Z[:, k], rcond=None)[0]
    return pearsonr(ry, rk)[0]


lines.append(f"Joint regression of the cell residual on (pair a, pair |q|, cross-lag deviation SD), standardised: coefficients {beta[0]:+.3f}, {beta[1]:+.3f}, {beta[2]:+.3f}; partial correlations {partial_r(0):+.3f}, {partial_r(1):+.3f}, {partial_r(2):+.3f}; R² {1 - np.var(y - np.column_stack([np.ones(len(y)), Z]) @ np.linalg.lstsq(np.column_stack([np.ones(len(y)), Z]), y, rcond=None)[0]):.3f}")
lines.append(f"Group-mean window series of the cross-lag deviation SD: DMT {np.array2string(np.nanmean(dev_sd[:, 0], 0), precision=4, floatmode='fixed', max_line_width=250)}; PCB {np.array2string(np.nanmean(dev_sd[:, 1], 0), precision=4, floatmode='fixed', max_line_width=250)}")
txt = "\n".join(lines) + "\n"
(REPO / "notes" / "review_results" / "partB" / "residual_source.log").write_text(txt)
print(txt)
print(f"done ({time.time() - t0:.0f}s)")
