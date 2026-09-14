"""
partB3_lag.py — Part B item 3: lag dependence. τ = 2, 3, 5 on ts_gsr, W = 60 and global fit:
the primary sts contrast with the full inference engine, the 16-atom level/DiD table, the
per-subject correlation of the sts DiD with (i) the lag-1 autocorrelation contrast and (ii) the
lag-τ autocorrelation contrast, and where the real pairs sit on the scope map at lag τ (the
AR(1) model's lag-τ 4-vector has the same S4 with a → r_τ; the map of B1 is re-evaluated on
r ∈ [−0.95, 0.95] since windowed r_τ of band-passed BOLD is negative at τ = 5).
Prediction recorded in notes/partB_prespec_2026-09-14.md (B3) before this ran. τ = 1 is recomputed
with the same code as a consistency check (it must reproduce results/atoms_win60_* and the Table 1 rows).

Outputs (notes/review_results/partB/): lag_atoms_win60_tau<τ>.npy, lag_atoms_win60_local_tau<τ>.npy,
  lag_atoms_bins_tau<τ>.npy, lag_atoms_bins_local_tau<τ>.npy, inference_rows_lag.csv (+ .pkl) in
  notes/review_results/, lag_tables.md, lag_run.log
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
IX = {n: i for i, n in enumerate(ATOMS)}
VAR = "ts_gsr"
TAUS = (1, 2, 3, 5)                                        # τ = 1 recomputed as a consistency check against results/
t0 = time.time()
ts = sio.loadmat(MAT)[VAR]

# ------------------------------------------------------------------ scope map at general r (incl. negative), for classification
H = 1e-3
r_grid = np.round(np.arange(-0.95, 0.95 + 1e-9, 0.01), 4)
q_grid = np.round(np.arange(-0.95, 0.95 + 1e-9, 0.01), 4)
Rg, Qg = np.meshgrid(r_grid, q_grid, indexing="ij")
S = IX["sts"]
sts_map = atoms_from_corr(ar1_corr(Rg.ravel(), Rg.ravel(), Qg.ravel()))[:, S].reshape(Rg.shape)
d_r = (atoms_from_corr(ar1_corr((Rg + H).ravel(), (Rg + H).ravel(), Qg.ravel()))[:, S] - atoms_from_corr(ar1_corr((Rg - H).ravel(), (Rg - H).ravel(), Qg.ravel()))[:, S]).reshape(Rg.shape) / (2 * H)
d_q = (atoms_from_corr(ar1_corr(Rg.ravel(), Rg.ravel(), (Qg + H).ravel()))[:, S] - atoms_from_corr(ar1_corr(Rg.ravel(), Rg.ravel(), (Qg - H).ravel()))[:, S]).reshape(Rg.shape) / (2 * H)
region = np.where((np.abs(d_r) < 1e-3) & (np.abs(d_q) < 1e-3), 0, np.where(np.abs(d_r) > np.abs(d_q), 1, 2))
lines = ["# Lag-dependence tables (partB3_lag.py)", "",
         f"Scope map re-evaluated on r ∈ [−0.95, 0.95] × q ∈ [−0.95, 0.95]: r-dominated {100 * (region == 1).mean():.1f} %, q-dominated {100 * (region == 2).mean():.1f} %, flat {100 * (region == 0).mean():.1f} % of cells; "
         f"q-dominated cells lie at |r| ≤ {np.abs(Rg[region == 2]).max() if (region == 2).any() else 0:.2f}.", ""]
# model sts vs r at q = 0.25 for reference
lines += ["| r (lag-τ autocorrelation) | model sts at |q| = 0.25 | ∂sts/∂r | ∂sts/∂q | ratio |", "|---|---|---|---|---|"]
for r in (-0.3, -0.2, -0.1, 0.0, 0.1, 0.15, 0.2, 0.3, 0.5, 0.85):
    i = int(np.argmin(np.abs(r_grid - r))); j = int(np.argmin(np.abs(q_grid - 0.25)))
    lines.append(f"| {r:+.2f} | {sts_map[i, j]:.4f} | {d_r[i, j]:+.3f} | {d_q[i, j]:+.3f} | {abs(d_r[i, j]) / abs(d_q[i, j]) if abs(d_q[i, j]) > 1e-12 else float('inf'):.1f} |")
lines.append("")


def classify(r, q):
    ii = np.clip(np.round((r - r_grid[0]) / 0.01).astype(int), 0, r_grid.size - 1)
    jj = np.clip(np.round((q - q_grid[0]) / 0.01).astype(int), 0, q_grid.size - 1)
    return region[ii, jj]


# ------------------------------------------------------------------ atoms at each τ
rows = []
raw_rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))
d_ac1 = [r for r in raw_rows if r["label"] == f"autocorr {VAR} W60" and r["set"] == "primary"][0]["did_subjects"]
d_sts1 = [r for r in raw_rows if r["label"] == f"sts {VAR} W60" and r["set"] == "primary"][0]["did_subjects"]
d_sts1g = [r for r in raw_rows if r["label"] == f"sts {VAR} global-bins" and r["set"] == "primary"][0]["did_subjects"]
mmi1 = np.load(REPO / "results" / f"atoms_win60_115regions-all_{VAR}_window.npy")
mmi1g = np.load(REPO / "results" / f"atoms_bins_115regions-all_{VAR}_global.npy")
summary = ["| τ | estimator | DMT pre r_τ (window-std.) | sts level (DMT pre) | xtx+yty level | sts DiD [CI], p, phase p, neg/14 | survives FD | r(sts DiD, lag-1 autocorr DiD) | r(sts DiD, lag-τ autocorr DiD) | r_τ DiD [CI], p | real pairs r-dominated (subj. 1, w1–4 & 6) | pair r_τ median | ∂sts/∂r ÷ ∂sts/∂q at (median r_τ, median \\|q\\|) |",
           "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]


def summarise(tau, est, A, W, d_ac_tau, ac_tau_pre, frac_dom, r_med, ratio, r_row):
    Sx = window_sets(W)
    PRE, POST = Sx["PRE"], Sx["primary"]
    lvl = A[:, 0, PRE].mean((0, 1))
    did = (A[:, 0, POST].mean(1) - A[:, 0, PRE].mean(1)) - (A[:, 1, POST].mean(1) - A[:, 1, PRE].mean(1))
    d = did[:, S]
    summary.append(f"| {tau} | {est} | {ac_tau_pre:.3f} | {lvl[S]:.4f} | {lvl[IX['xtx']] + lvl[IX['yty']]:.4f} | {r_row['did']:+.4f} [{r_row['did_lo']:+.4f}, {r_row['did_hi']:+.4f}], {r_row['did_p']:.4f}, {r_row['phase_p']:.4f}, {r_row['n_neg']} | {'yes' if r_row['survives'] else 'no'} | "
                   f"{pearsonr(d, d_ac1)[0]:+.3f} | {pearsonr(d, d_ac_tau)[0]:+.3f} | {d_ac_tau.mean():+.4f}, {signflip_p(d_ac_tau):.4f} | {100 * frac_dom:.1f} % | {r_med:+.3f} | {ratio:.1f} |")
    lines.append(f"## τ = {tau}, {est}: 16-atom DMT pre level and primary DiD (τ = 1 MMI in brackets)")
    lines.append("")
    lines.append("| atom | level τ | DiD τ (neg/14) |")
    lines.append("|---|---|---|")
    ref = mmi1 if W == 60 else mmi1g
    ref_lvl = ref[:, 0, PRE].mean((0, 1)); ref_did = (ref[:, 0, POST].mean(1) - ref[:, 0, PRE].mean(1)) - (ref[:, 1, POST].mean(1) - ref[:, 1, PRE].mean(1))
    for a, n in enumerate(ATOMS):
        lines.append(f"| {n} | {lvl[a]:+.4f} ({ref_lvl[a]:+.4f}) | {did[:, a].mean():+.4f} ({int((did[:, a] < 0).sum())}) [{ref_did[:, a].mean():+.4f}] |")
    lines.append(f"| TDMI | {lvl.sum():+.4f} ({ref_lvl.sum():+.4f}) | {did.sum(1).mean():+.4f} [{ref_did.sum(1).mean():+.4f}] |")
    lines.append("")
    return d


from itertools import product as _product
_SIGNS = np.array(list(_product((-1, 1), repeat=14)))


def signflip_p(v):
    v = np.asarray(v, float)
    return float(np.mean(np.abs(_SIGNS @ v) / v.size >= abs(v.mean()) - 1e-12))


for tau in TAUS:
    win = np.full((14, 2, 14, 16), np.nan); win_local = np.full((14, 2, 840, 16), np.nan)
    bins = np.full((14, 2, 28, 16), np.nan); bins_local = np.full((14, 2, 840, 16), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            for w in range(14):
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= tau + 4:
                    continue
                pp = PairPhiID(X[:, in_w], tau=tau)
                loc = pp.atoms_local_pairmean()
                win[s, c, w] = loc.mean(0)
                win_local[s, c, in_w[:pp.n]] = loc
            pp = PairPhiID(X[:, kept], tau=tau)
            ab = pp.atoms_bins(kept[:pp.n] // 30, 28)
            bins[s, c] = np.nanmean(ab, axis=1)
            bins_local[s, c, kept[:pp.n]] = pp.atoms_local_pairmean()
        print(f"   τ = {tau}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    for name, arr in (("win60", win), ("win60_local", win_local), ("bins", bins), ("bins_local", bins_local)):
        np.save(OUT / f"lag_atoms_{name}_tau{tau}.npy", arr)
    # lag-τ autocorrelation contrast (window-standardised, W60) and the real pairs' position on the map
    ac_tau, ac_tau_local = autocorr_series(ts, 60, "window", lag=tau)
    Sx = window_sets(60)
    d_ac_tau = (ac_tau[:, 0, Sx["primary"]].mean(1) - ac_tau[:, 0, Sx["PRE"]].mean(1)) - (ac_tau[:, 1, Sx["primary"]].mean(1) - ac_tau[:, 1, Sx["PRE"]].mean(1))
    ac_tau_pre = ac_tau[:, 0, Sx["PRE"]].mean()
    E = Engine(60)
    rs_ac = E.run(ac_tau, ac_tau_local, label=f"autocorr lag{tau} {VAR} W60")
    for r in rs_ac:
        print(fmt(r), flush=True)
    rows.extend(rs_ac)
    r_all, q_all, dom = [], [], []
    for c in range(2):
        X = np.asarray(ts[0, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        for w in (0, 1, 2, 3, 5):
            in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
            pp = PairPhiID(X[:, in_w], tau=tau)
            r_pair = 0.5 * (pp.C[:, 0, 2] + pp.C[:, 1, 3]); q_pair = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
            r_all.append(r_pair); q_all.append(q_pair); dom.append(classify(r_pair, q_pair) == 1)
    r_all, q_all, dom = np.concatenate(r_all), np.concatenate(q_all), np.concatenate(dom)
    i = int(np.argmin(np.abs(r_grid - np.median(r_all)))); j = int(np.argmin(np.abs(q_grid - np.median(np.abs(q_all)))))
    ratio = abs(d_r[i, j]) / abs(d_q[i, j]) if abs(d_q[i, j]) > 1e-12 else float("inf")
    lines.append(f"τ = {tau}: subject-1 pairs (both runs, windows 1–4 and 6): r_τ median {np.median(r_all):+.3f} (5–95 % {np.percentile(r_all, 5):+.3f}–{np.percentile(r_all, 95):+.3f}), |q| median {np.median(np.abs(q_all)):.3f}; "
                 f"r-dominated {100 * dom.mean():.1f} %, q-dominated {100 * (classify(r_all, q_all) == 2).mean():.1f} %, flat {100 * (classify(r_all, q_all) == 0).mean():.1f} %; ∂sts/∂r = {d_r[i, j]:+.3f}, ∂sts/∂q = {d_q[i, j]:+.3f} at the medians")
    lines.append("")
    for est, A, L, W in (("W60", win, win_local, 60), ("global-bins", bins, bins_local, 30)):
        E = Engine(W)
        rs = E.run(A[..., S], L[..., S], label=f"sts tau{tau} {VAR} {est}")
        for r in rs:
            print(fmt(r), flush=True)
        rows.extend(rs)
        r_row = rs[0]
        d = summarise(tau, est, A, W, d_ac_tau, ac_tau_pre, dom.mean(), np.median(r_all), ratio, r_row)
        lines.append(f"τ = {tau} {est}: per-subject sts DiD vs lag-1 autocorrelation contrast r = {pearsonr(d, d_ac1)[0]:+.3f} (Spearman {spearmanr(d, d_ac1)[0]:+.3f}); vs lag-{tau} autocorrelation contrast r = {pearsonr(d, d_ac_tau)[0]:+.3f} (Spearman {spearmanr(d, d_ac_tau)[0]:+.3f}); vs the τ = 1 sts DiD of the same estimator r = {pearsonr(d, d_sts1 if W == 60 else d_sts1g)[0]:+.3f}")
        lines.append("")

lines.insert(2, "\n".join(["## Summary across τ (ts_gsr)", ""] + summary + [""]))
pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows]).to_csv(RR / "inference_rows_lag.csv", index=False)
with open(RR / "inference_rows_lag.pkl", "wb") as fh:
    pickle.dump(rows, fh)
(OUT / "lag_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[:40]))
print(f"done ({time.time() - t0:.0f}s)")
