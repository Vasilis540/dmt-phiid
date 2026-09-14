"""
partB4_diagnostic.py — Part B item 4: the diagnostic. Per pair, subject, run and window, the
closed-form sts of the diagonal VAR(1) pair with the pair's measured lag-1 autocorrelations
(a_x, a_y) and lag-0 correlation q (rev_phiid_fast.ar1_corr + atoms_from_corr) is the sts
predicted "from measured r1 and q alone"; residual = observed sts − predicted sts.

Estimators: W = 60 (primary; both variants) and W = 30 (ts_gsr and ts_demean; W30 windows have
their own (a_x, a_y, q)). At the global fit the run-level (r1, q) are constant within a run, so
the prediction is constant across bins and the residual DiD equals the observed DiD by
construction; that cell is reported as such.

Reported: residual magnitude relative to observed sts (whole-brain means; per-pair R² of
predicted vs observed within windows); whole-brain residual series and its DiD with the primary
tests (sign-flip, bootstrap, FD residualisation; phase-randomised null on the TR-local observed
sts series minus the window's predicted value); the per-subject correlation of the residual DiD,
the predicted DiD and the observed DiD with the autocorrelation contrast; the AR(1) lag-1
cross-correlation check (observed corr(x_t, y_{t+1}) vs a_y q). Prediction recorded in
notes/partB_prespec_2026-09-14.md (B4) before this ran.

Outputs (notes/review_results/partB/): diag_series_<variant>_W<W>.npz, diag_tables.md, diag_run.log;
notes/review_results/inference_rows_diag.csv (+ .pkl)
"""
import pickle
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.stats import pearsonr, spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_inference import Engine, fmt, window_sets
from rev_series import autocorr_series

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
S = ATOMS.index("sts")
t0 = time.time()
ts = sio.loadmat(MAT)
raw_rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))


def raw_did(label, s="primary"):
    return [r for r in raw_rows if r["label"] == label and r["set"] == s][0]["did_subjects"]


rows, lines = [], ["# Diagnostic tables (partB4_diagnostic.py)", ""]
for var in ("ts_gsr", "ts_demean"):
    for W in (60, 30):
        n_win = 840 // W
        obs = np.full((14, 2, n_win), np.nan); pred = np.full((14, 2, n_win), np.nan); pred_sym = np.full((14, 2, n_win), np.nan)
        local_obs = np.full((14, 2, 840), np.nan); local_res = np.full((14, 2, 840), np.nan)
        r2 = np.full((14, 2, n_win), np.nan); xcorr_dev = np.full((14, 2, n_win), np.nan); xcorr_r = np.full((14, 2, n_win), np.nan)
        pair_stats = []
        for s in range(14):
            for c in range(2):
                X = np.asarray(ts[var][s, c], float)[REGIONS]
                kept = np.where(np.all(np.isfinite(X), axis=0))[0]
                for w in range(n_win):
                    in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
                    if in_w.size <= 5:
                        continue
                    pp = PairPhiID(X[:, in_w])
                    o = pp.atoms_mean()[:, S]
                    ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]
                    q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
                    p = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
                    ps = atoms_from_corr(ar1_corr(0.5 * (ax + ay), 0.5 * (ax + ay), q))[:, S]
                    obs[s, c, w], pred[s, c, w], pred_sym[s, c, w] = o.mean(), p.mean(), ps.mean()
                    r2[s, c, w] = pearsonr(o, p)[0] ** 2
                    # AR(1) lag-1 cross-correlation check: model says corr(x_t, y_{t+1}) = a_y q and corr(y_t, x_{t+1}) = a_x q
                    dev = np.r_[pp.C[:, 0, 3] - ay * q, pp.C[:, 1, 2] - ax * q]
                    xcorr_dev[s, c, w] = np.abs(dev).mean()
                    xcorr_r[s, c, w] = pearsonr(np.r_[pp.C[:, 0, 3], pp.C[:, 1, 2]], np.r_[ay * q, ax * q])[0]
                    loc = pp.atoms_local_pairmean()[:, S]
                    local_obs[s, c, in_w[:pp.n]] = loc
                    local_res[s, c, in_w[:pp.n]] = loc - p.mean()
                    if s == 0 and w in (1, 5):
                        pair_stats.append((c, w, o, p, ax, ay, q))
            print(f"   {var} W{W}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
        res = obs - pred
        np.savez(OUT / f"diag_series_{var}_W{W}.npz", obs=obs, pred=pred, pred_sym=pred_sym, res=res, r2=r2, xcorr_dev=xcorr_dev, xcorr_r=xcorr_r, local_obs=local_obs, local_res=local_res)
        Sx = window_sets(W)
        PRE, POST = Sx["PRE"], Sx["primary"]
        lines += [f"## {var}, W = {W}", ""]
        lines.append(f"Levels (all subjects, runs, windows): observed sts {np.nanmean(obs):.4f}, predicted (AR(1) from a_x, a_y, q) {np.nanmean(pred):.4f}, residual {np.nanmean(res):+.4f} ({100 * np.nanmean(res) / np.nanmean(obs):+.1f} % of observed); "
                     f"SD of the residual across subject × run × window {np.nanstd(res):.4f} vs SD of observed {np.nanstd(obs):.4f}; symmetric-a prediction {np.nanmean(pred_sym):.4f}.")
        lines.append(f"Per-pair R² of predicted vs observed sts within a window: mean {np.nanmean(r2):.3f} (min {np.nanmin(r2):.3f}, max {np.nanmax(r2):.3f}). "
                     f"AR(1) lag-1 cross-correlation check: mean |corr(x_t, y_(t+1)) − a_y q| = {np.nanmean(xcorr_dev):.4f}; correlation across pairs between observed and model lag-1 cross-correlations, mean {np.nanmean(xcorr_r):.3f} (min {np.nanmin(xcorr_r):.3f}).")
        for c, w, o, p, ax, ay, q in pair_stats:
            lines.append(f"Subject 1 {'DMT' if c == 0 else 'PCB'} window {w + 1}: pair-level r(obs, pred) = {pearsonr(o, p)[0]:+.3f}; obs mean {o.mean():.4f} SD {o.std():.4f}; pred mean {p.mean():.4f} SD {p.std():.4f}; residual mean {np.mean(o - p):+.4f} SD {np.std(o - p):.4f}; r(residual, mean a) = {pearsonr(o - p, 0.5 * (ax + ay))[0]:+.3f}, r(residual, |q|) = {pearsonr(o - p, np.abs(q))[0]:+.3f}, r(residual, |a_x − a_y|) = {pearsonr(o - p, np.abs(ax - ay))[0]:+.3f}")
        # engine inference: observed, predicted, residual
        for qname, x, xl in (("observed sts", obs, local_obs), ("predicted sts", pred, None), ("residual sts", res, local_res)):
            E = Engine(W)
            rs = E.run(x, xl, label=f"diag {qname} {var} W{W}")
            for r in rs:
                print(fmt(r), flush=True)
            rows.extend(rs)
        d_obs = (obs[:, 0, POST].mean(1) - obs[:, 0, PRE].mean(1)) - (obs[:, 1, POST].mean(1) - obs[:, 1, PRE].mean(1))
        d_pred = (pred[:, 0, POST].mean(1) - pred[:, 0, PRE].mean(1)) - (pred[:, 1, POST].mean(1) - pred[:, 1, PRE].mean(1))
        d_res = d_obs - d_pred
        d_ac = raw_did(f"autocorr {var} W60")
        lines.append(f"Primary DiD: observed {d_obs.mean():+.4f}, predicted {d_pred.mean():+.4f} ({100 * d_pred.mean() / d_obs.mean():.0f} % of observed), residual {d_res.mean():+.4f}. Per subject: r(residual DiD, autocorrelation contrast) = {pearsonr(d_res, d_ac)[0]:+.3f} (Spearman {spearmanr(d_res, d_ac)[0]:+.3f}); "
                     f"r(predicted DiD, autocorrelation contrast) = {pearsonr(d_pred, d_ac)[0]:+.3f}; r(observed DiD, autocorrelation contrast) = {pearsonr(d_obs, d_ac)[0]:+.3f}; r(predicted DiD, observed DiD) = {pearsonr(d_pred, d_obs)[0]:+.3f}; r(residual DiD, observed DiD) = {pearsonr(d_res, d_obs)[0]:+.3f}; residual DiD negative in {int((d_res < 0).sum())}/14.")
        lines.append(f"Per-subject residual DiDs: {np.array2string(d_res, precision=4, floatmode='fixed', max_line_width=250)}")
        lines.append(f"Group-mean window series: observed DMT {np.array2string(obs[:, 0].mean(0), precision=3, floatmode='fixed', max_line_width=250)}; predicted DMT {np.array2string(pred[:, 0].mean(0), precision=3, floatmode='fixed', max_line_width=250)}; residual DMT {np.array2string(res[:, 0].mean(0), precision=3, floatmode='fixed', max_line_width=250)}; residual PCB {np.array2string(res[:, 1].mean(0), precision=3, floatmode='fixed', max_line_width=250)}")
        lines.append("")

# global fit: run-level (a_x, a_y, q) -> one prediction per run; the residual DiD equals the observed DiD
lines += ["## Global fit (run-level r1 and q)", ""]
for var in ("ts_gsr", "ts_demean"):
    A = np.load(REPO / "results" / f"atoms_bins_115regions-all_{var}_global.npy")[..., S]
    pred_run = np.full((14, 2), np.nan); obs_run = np.full((14, 2), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            pp = PairPhiID(X[:, kept])
            ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]; q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
            pred_run[s, c] = atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean(); obs_run[s, c] = pp.atoms_mean()[:, S].mean()
    lines.append(f"{var}: run-level observed sts (whole run, plug-in) {obs_run.mean():.4f} vs AR(1) prediction from run-level (a_x, a_y, q) {pred_run.mean():.4f} (residual {np.mean(obs_run - pred_run):+.4f}, {100 * np.mean(obs_run - pred_run) / obs_run.mean():+.1f} %); "
                 f"the prediction is constant across the run's bins, so the bin-level residual DiD equals the observed global-fit DiD ({((A[:, 0, 10:28].mean(1) - A[:, 0, :8].mean(1)) - (A[:, 1, 10:28].mean(1) - A[:, 1, :8].mean(1))).mean():+.4f}); no decomposition is possible at this estimator.")
pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows]).to_csv(RR / "inference_rows_diag.csv", index=False)
with open(RR / "inference_rows_diag.pkl", "wb") as fh:
    pickle.dump(rows, fh)
(OUT / "diag_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
