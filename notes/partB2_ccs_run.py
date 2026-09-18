"""
partB2_ccs_run.py — Part B item 2, step 2: the primary sts contrast and the 16-atom table under
CCS (phyid's definitions, verified against an independent Ince-2017 implementation and a binary
hand case in partB2_ccs_verify.py), both variants, W = 60 and global fit; per-subject correlation
of the CCS sts DiD with the autocorrelation contrast; the CCS analogue of the sts ≈ xtx + yty
structure; and whether the CCS sts level tracks r1 across windows and pairs.
Prediction recorded in notes/partB_prespec_2026-09-14.md (B2) before this ran.

Outputs (notes/review_results/partB/):
  ccs_atoms_win60_<variant>.npy (14, 2, 14, 16), ccs_atoms_win60_local_<variant>.npy (14, 2, 840, 16),
  ccs_atoms_bins_<variant>.npy (14, 2, 28, 16), ccs_atoms_bins_local_<variant>.npy, ccs_agree_share_<variant>.npy,
  inference_rows_ccs.csv (+ .pkl), ccs_tables.md, ccs_run.log
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
from rev_phiid_fast import PairPhiID, ATOMS
from rev_inference import Engine, fmt, window_sets
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
t0 = time.time()
ts = sio.loadmat(MAT)


def run_variant(var):
    win = np.full((14, 2, 14, 16), np.nan)
    win_local = np.full((14, 2, 840, 16), np.nan)
    bins = np.full((14, 2, 28, 16), np.nan)
    bins_local = np.full((14, 2, 840, 16), np.nan)
    agree = np.full((14, 2, 15), np.nan)                       # windows 1–14 + global
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            for w in range(14):
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                am, _, loc, ag = pp.atoms_ccs()
                win[s, c, w] = am.mean(0)
                win_local[s, c, in_w[:pp.n]] = loc
                agree[s, c, w] = ag.mean()
            pp = PairPhiID(X[:, kept])
            am, ab, loc, ag = pp.atoms_ccs(kept[:pp.n] // 30, 28)
            bins[s, c] = np.nanmean(ab, axis=1)
            bins_local[s, c, kept[:pp.n]] = loc
            agree[s, c, 14] = ag.mean()
        print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    for name, arr in (("win60", win), ("win60_local", win_local), ("bins", bins), ("bins_local", bins_local), ("agree_share", agree)):
        np.save(OUT / f"ccs_atoms_{name}_{var}.npy" if name != "agree_share" else OUT / f"ccs_agree_share_{var}.npy", arr)
    return win, win_local, bins, bins_local, agree


rows, lines = [], ["# CCS tables (partB2_ccs_run.py)", f"git={SHA}", ""]
raw_rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))


def raw_did(label, s="primary"):
    return [r for r in raw_rows if r["label"] == label and r["set"] == s][0]["did_subjects"]


for var in ("ts_gsr", "ts_demean"):
    win, win_local, bins, bins_local, agree = run_variant(var)
    mmi_win = np.load(REPO / "results" / f"atoms_win60_115regions-all_{var}_window.npy")
    mmi_bins = np.load(REPO / "results" / f"atoms_bins_115regions-all_{var}_global.npy")
    for est, A, L, MMI, W in (("W60", win, win_local, mmi_win, 60), ("global-bins", bins, bins_local, mmi_bins, 30)):
        S = window_sets(W)
        PRE, POST = S["PRE"], S["primary"]
        # engine inference on CCS sts, CCS xtx+yty, CCS rtr
        for qname, x, xl in (("sts", A[..., IX["sts"]], L[..., IX["sts"]]),
                             ("xtx+yty", A[..., IX["xtx"]] + A[..., IX["yty"]], L[..., IX["xtx"]] + L[..., IX["yty"]]),
                             ("rtr", A[..., IX["rtr"]], L[..., IX["rtr"]])):
            E = Engine(W)
            rs = E.run(x, xl, label=f"CCS {qname} {var} {est}")
            for r in rs:
                print(fmt(r), flush=True)
            rows.extend(rs)
        # 16-atom table: DMT pre level, MMI pre level, CCS DiD, MMI DiD
        lvl = A[:, 0, PRE].mean((0, 1)); lvl_m = MMI[:, 0, PRE].mean((0, 1))
        did = ((A[:, 0, POST].mean(1) - A[:, 0, PRE].mean(1)) - (A[:, 1, POST].mean(1) - A[:, 1, PRE].mean(1)))      # (14, 16)
        did_m = ((MMI[:, 0, POST].mean(1) - MMI[:, 0, PRE].mean(1)) - (MMI[:, 1, POST].mean(1) - MMI[:, 1, PRE].mean(1)))
        lines += [f"## {var} {est}: 16 atoms, DMT pre-injection level and primary DiD, CCS vs MMI (nats)", "",
                  "| atom | CCS level | MMI level | CCS DiD (mean, neg/14) | MMI DiD |", "|---|---|---|---|---|"]
        for a, n in enumerate(ATOMS):
            lines.append(f"| {n} | {lvl[a]:+.4f} | {lvl_m[a]:+.4f} | {did[:, a].mean():+.4f} ({int((did[:, a] < 0).sum())}) | {did_m[:, a].mean():+.4f} |")
        lines.append(f"| TDMI (sum) | {lvl.sum():+.4f} | {lvl_m.sum():+.4f} | {did.sum(1).mean():+.4f} | {did_m.sum(1).mean():+.4f} |")
        # correlations
        d_sts = did[:, IX["sts"]]
        d_ac = raw_did(f"autocorr {var} W60") if est == "W60" else raw_did(f"autocorr {var} run-standardised bins")
        d_ac1 = raw_did(f"autocorr {var} W60")
        lines += ["", f"Per-subject CCS sts DiD vs the autocorrelation contrast (W60, window-standardised r1): Pearson r = {pearsonr(d_sts, d_ac1)[0]:+.3f} (p = {pearsonr(d_sts, d_ac1)[1]:.3f}), Spearman {spearmanr(d_sts, d_ac1)[0]:+.3f}; "
                  f"vs the MMI sts DiD of the same estimator: r = {pearsonr(d_sts, did_m[:, IX['sts']])[0]:+.3f}; "
                  f"CCS (xtx+yty) DiD vs autocorrelation contrast: r = {pearsonr(did[:, IX['xtx']] + did[:, IX['yty']], d_ac1)[0]:+.3f}",
                  f"CCS sts level / CCS (xtx + yty) level (DMT pre): {lvl[IX['sts']]:+.4f} / {lvl[IX['xtx']] + lvl[IX['yty']]:+.4f}; MMI: {lvl_m[IX['sts']]:+.4f} / {lvl_m[IX['xtx']] + lvl_m[IX['yty']]:+.4f}",
                  f"share of samples with all five signs agreeing (mean over runs): {np.nanmean(agree[:, :, :14] if est == 'W60' else agree[:, :, 14]):.3f}"]
        # tracking of the CCS sts level with r1 across windows: group-mean window series vs group-mean autocorrelation series
        if est == "W60":
            from rev_series import autocorr_series
            ac = autocorr_series(ts[var], 60, "window")[0].mean(0)                   # (2, 14)
            g = A[..., IX["sts"]].mean(0)                                           # (2, 14)
            gm = MMI[..., IX["sts"]].mean(0)
            lines.append(f"Group-mean window series, CCS sts vs mean r1 (28 condition-windows): r = {pearsonr(g.ravel(), ac.ravel())[0]:+.3f}; MMI sts vs r1: {pearsonr(gm.ravel(), ac.ravel())[0]:+.3f}; CCS sts vs MMI sts: {pearsonr(g.ravel(), gm.ravel())[0]:+.3f}")
            # per-pair, within one window (subject 1, DMT window 6 and PCB window 2): CCS sts vs pair r1 and vs |q|
            for (s, c, w) in ((0, 0, 5), (0, 1, 1)):
                X = np.asarray(ts[var][s, c], float)[REGIONS]
                kept = np.where(np.all(np.isfinite(X), axis=0))[0]
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                pp = PairPhiID(X[:, in_w])
                am, _, _, ag = pp.atoms_ccs()
                r1p = 0.5 * (pp.C[:, 0, 2] + pp.C[:, 1, 3]); qp = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
                mm = pp.atoms_mean()
                lines.append(f"Per-pair, subject 1 {'DMT' if c == 0 else 'PCB'} window {w + 1}: CCS sts vs pair r1 r = {pearsonr(am[:, IX['sts']], r1p)[0]:+.3f}, vs |q| {pearsonr(am[:, IX['sts']], np.abs(qp))[0]:+.3f}, vs MMI sts {pearsonr(am[:, IX['sts']], mm[:, IX['sts']])[0]:+.3f}; "
                             f"MMI sts vs r1 {pearsonr(mm[:, IX['sts']], r1p)[0]:+.3f}; CCS sts pair mean {am[:, IX['sts']].mean():+.4f} (SD {am[:, IX['sts']].std():.4f}), CCS xtx+yty {am[:, IX['xtx']].mean() + am[:, IX['yty']].mean():+.4f}, MMI sts {mm[:, IX['sts']].mean():+.4f}; agree share {ag.mean():.3f}")
        lines.append("")

(RR / "inference_rows_ccs.csv").write_text(f"# partB2_ccs_run.py; git={SHA}\n" + pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows]).to_csv(index=False))
with open(RR / "inference_rows_ccs.pkl", "wb") as fh:
    pickle.dump(rows, fh)
(OUT / "ccs_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
