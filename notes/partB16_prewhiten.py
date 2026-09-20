"""
partB16_prewhiten.py — B16: the sixteen atoms and the DMT contrast after prewhitening.
Pre-run entry: manuscript/analysis_record.md, "Prewhitening (B16): pre-run entry, 20 Sep 2026" (specification,
prediction and rule as in notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5).

Two whitened variants of each released regional series (ts_gsr and ts_demean), per region and run:
  (a) "arp": the residuals of the region's own AR(p) fit by ordinary least squares on the run's finite TRs, p chosen
      by BIC over 1–5 (BIC = n ln(RSS/n) + (p + 1) ln n, the intercept counted, on the n = T − 5 residuals every candidate order can produce,
      then the chosen order refitted on all its available samples); the first p TRs of the run are set to non-finite
      and dropped downstream exactly as scripts/01 drops non-finite TRs (so each whitened run keeps 840 − max_p TRs
      across regions);
  (b) "ar1": p = 1 (the diagonal AR(1) innovations).
For each of the four series: the sixteen MMI atoms (PairPhiID.atoms_mean per W = 60 window; atoms_bins for the
global fit's 28 bins of 30 TRs) and the CCS atoms (PairPhiID.atoms_ccs, phyid's mask), exactly as partB2_ccs_run.py
computes them on the raw series; the DMT contrast of MMI-sts and CCS-sts (and MMI xtx + yty) with the primary
inference (rev_inference.Engine on the window/bin series with their TR-local series: DiD, subject bootstrap, exact
sign-flip p, phase-randomised null, FD residualisation); the whitened series' mean lag-1 autocorrelation
(rev_series.autocorr_series, window mode for W = 60 and run mode for the bins) with the same inference; and the
residual diagnostic of partB4 (per-pair AR(1) prediction from the whitened window's (a_x, a_y, q); observed,
predicted and residual whole-brain series and their DiDs).
Free choices: BIC range 1–5; OLS with intercept on the run's finite TRs; W = 60; bins of 30 TRs; region 20
excluded; seed 20261120 (Engine's generator, as everywhere).
Outputs (notes/review_results/partB/): prewhiten_tables.md, inference_rows_prewhiten.csv (+ .pkl, with the
per-subject DiDs), prewhiten_atoms_<whitening>_<variant>_{mmi_win60,mmi_bins,ccs_win60,ccs_bins}.npy,
prewhiten_orders.csv (chosen p per region and run), prewhiten_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB16_prewhiten.py   (the longest of B14–B20; hours)
"""
import pickle
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio
from scipy.stats import pearsonr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_inference import Engine, fmt, window_sets
from rev_series import autocorr_series
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
S = IX["sts"]
SEED = 20261120
P_MAX = 5
t0 = time.time()
ts = sio.loadmat(MAT)
raw_rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))


def raw_did(label, st="primary"):
    return [r for r in raw_rows if r["label"] == label and r["set"] == st][0]["did_subjects"]


def ar_fit(x, p):
    """OLS AR(p) with intercept on the finite samples of x (1-D); returns residuals aligned to x (NaN where undefined)."""
    n = x.size
    idx = np.arange(p, n)
    fin = np.isfinite(x)
    ok = idx[np.all(np.stack([fin[idx - k] for k in range(p + 1)], 0), 0)]
    Y = x[ok]
    X = np.c_[np.ones(ok.size), np.stack([x[ok - k] for k in range(1, p + 1)], 1)]
    beta, *_ = np.linalg.lstsq(X, Y, rcond=None)
    res = np.full(n, np.nan)
    res[ok] = Y - X @ beta
    return res, beta


def whiten(X, mode):
    """X (R, T) → residual series (R, T) and chosen orders (R,)."""
    R, T = X.shape
    W = np.full((R, T), np.nan); orders = np.zeros(R, int)
    for i in range(R):
        x = X[i]
        if mode == "ar1":
            p = 1
        else:
            # BIC on the common sample every candidate can produce (t ≥ P_MAX)
            best = None
            for pc in range(1, P_MAX + 1):
                res, _ = ar_fit(x, pc)
                common = np.arange(P_MAX, T)
                r = res[common]; r = r[np.isfinite(r)]
                bic = r.size * np.log(np.mean(r ** 2)) + (pc + 1) * np.log(r.size)
                if best is None or bic < best[0]:
                    best = (bic, pc)
            p = best[1]
        res, _ = ar_fit(x, p)
        W[i] = res
        orders[i] = p
    return W, orders


def run_pipeline(Xw_all, var, tag):
    """Xw_all: object array (14, 2) of whitened (115, 840) series. Returns the window/bin arrays like partB2 and the diagnostic series."""
    mmi_win = np.full((14, 2, 14, 16), np.nan); mmi_win_local = np.full((14, 2, 840, 16), np.nan)
    mmi_bins = np.full((14, 2, 28, 16), np.nan); mmi_bins_local = np.full((14, 2, 840, 16), np.nan)
    ccs_win = np.full((14, 2, 14, 16), np.nan); ccs_win_local = np.full((14, 2, 840, 16), np.nan)
    ccs_bins = np.full((14, 2, 28, 16), np.nan); ccs_bins_local = np.full((14, 2, 840, 16), np.nan)
    obs = np.full((14, 2, 14), np.nan); pred = np.full((14, 2, 14), np.nan)
    local_obs = np.full((14, 2, 840), np.nan); local_res = np.full((14, 2, 840), np.nan)
    for s in range(14):
        for c in range(2):
            X = Xw_all[s, c]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            for w in range(14):
                in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                am = pp.atoms_mean()
                mmi_win[s, c, w] = am.mean(0)
                loc = pp.atoms_local_pairmean()
                mmi_win_local[s, c, in_w[:pp.n]] = loc
                ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]; q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
                p = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
                obs[s, c, w], pred[s, c, w] = am[:, S].mean(), p.mean()
                local_obs[s, c, in_w[:pp.n]] = loc[:, S]; local_res[s, c, in_w[:pp.n]] = loc[:, S] - p.mean()
                cm, _, cloc, _ = pp.atoms_ccs()
                ccs_win[s, c, w] = cm.mean(0); ccs_win_local[s, c, in_w[:pp.n]] = cloc
            pp = PairPhiID(X[:, kept])
            slot = kept[:pp.n] // 30
            ab = pp.atoms_bins(slot, 28)
            mmi_bins[s, c] = np.nanmean(ab, axis=1)
            mmi_bins_local[s, c, kept[:pp.n]] = pp.atoms_local_pairmean()
            cm, cb, cloc, _ = pp.atoms_ccs(slot, 28)
            ccs_bins[s, c] = np.nanmean(cb, axis=1); ccs_bins_local[s, c, kept[:pp.n]] = cloc
        print(f"   {tag} {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    for name, arr in (("mmi_win60", mmi_win), ("mmi_bins", mmi_bins), ("ccs_win60", ccs_win), ("ccs_bins", ccs_bins)):
        np.save(OUT / f"prewhiten_atoms_{tag}_{var}_{name}.npy", arr)
    return dict(mmi_win=mmi_win, mmi_win_local=mmi_win_local, mmi_bins=mmi_bins, mmi_bins_local=mmi_bins_local, ccs_win=ccs_win, ccs_win_local=ccs_win_local,
                ccs_bins=ccs_bins, ccs_bins_local=ccs_bins_local, obs=obs, pred=pred, local_obs=local_obs, local_res=local_res)


rows = []
lines = ["# The atoms and the DMT contrast after prewhitening (partB16_prewhiten.py)", f"git={SHA}", "",
         f"Whitening per region and run: 'arp' = residuals of the region's AR(p) fit, p by BIC over 1–{P_MAX}; 'ar1' = p = 1. The first p TRs of each run are dropped (non-finite). "
         f"Atoms as partB2_ccs_run.py (MMI: PairPhiID.atoms_mean / atoms_bins; CCS: atoms_ccs, phyid's mask); inference as the primary (rev_inference.Engine, seed {SEED}); "
         "the diagnostic as partB4 (per-pair AR(1) prediction from the whitened window's a_x, a_y, q). Level = DMT pre-injection (windows 1–4; bins 1–8); DiD = post minus pre, DMT minus placebo.", ""]
orders_csv = ["whitening,variant,subject,run,region_index,p"]
for tag in ("arp", "ar1"):
    for var in ("ts_gsr", "ts_demean"):
        Xw_all = np.empty((14, 2), dtype=object)
        ord_all = np.zeros((14, 2, 115), int)
        for s in range(14):
            for c in range(2):
                X = np.asarray(ts[var][s, c], float)[REGIONS]
                Wx, orders = whiten(X, tag)
                Xw_all[s, c] = Wx; ord_all[s, c] = orders
                for i, r in enumerate(REGIONS):
                    orders_csv.append(f"{tag},{var},{s + 1},{'DMT' if c == 0 else 'PCB'},{r},{orders[i]}")
        print(f"   {tag} {var}: whitened ({time.time() - t0:.0f}s); orders: " + ", ".join(f"p={p}: {int((ord_all == p).sum())}" for p in range(1, P_MAX + 1)), flush=True)
        R = run_pipeline(Xw_all, var, tag)
        # autocorrelation of the whitened series (window mode for W = 60; run mode for the bins)
        ts_w = np.empty((14, 2), dtype=object)
        for s in range(14):
            for c in range(2):
                full = np.full((116, 840), np.nan); full[REGIONS] = Xw_all[s, c]; ts_w[s, c] = full
        ac_w, ac_w_local = autocorr_series(ts_w, 60, "window")
        ac_r, ac_r_local = autocorr_series(ts_w, 30, "run")
        # inference
        for est, W in (("W60", 60), ("global-bins", 30)):
            series = ([("MMI sts", R["mmi_win"][..., S], R["mmi_win_local"][..., S]), ("MMI xtx+yty", R["mmi_win"][..., IX["xtx"]] + R["mmi_win"][..., IX["yty"]], R["mmi_win_local"][..., IX["xtx"]] + R["mmi_win_local"][..., IX["yty"]]),
                       ("CCS sts", R["ccs_win"][..., S], R["ccs_win_local"][..., S]), ("autocorr", ac_w, ac_w_local),
                       ("diag observed sts", R["obs"], R["local_obs"]), ("diag predicted sts", R["pred"], None), ("diag residual sts", R["obs"] - R["pred"], R["local_res"])]
                      if est == "W60" else
                      [("MMI sts", R["mmi_bins"][..., S], R["mmi_bins_local"][..., S]), ("MMI xtx+yty", R["mmi_bins"][..., IX["xtx"]] + R["mmi_bins"][..., IX["yty"]], R["mmi_bins_local"][..., IX["xtx"]] + R["mmi_bins_local"][..., IX["yty"]]),
                       ("CCS sts", R["ccs_bins"][..., S], R["ccs_bins_local"][..., S]), ("autocorr", ac_r, ac_r_local)])
            for qname, x, xl in series:
                E = Engine(W)
                rs = E.run(x, xl, label=f"prewhiten {tag} {qname} {var} {est}")
                for r in rs:
                    print(fmt(r), flush=True)
                rows.extend(rs)
        # tables
        Sx = window_sets(60); PRE, POST = Sx["PRE"], Sx["primary"]
        Sb = window_sets(30); PRE_B, POST_B = Sb["PRE"], Sb["primary"]
        for est, A, C, PRE_, POST_ in (("W60", R["mmi_win"], R["ccs_win"], PRE, POST), ("global-bins", R["mmi_bins"], R["ccs_bins"], PRE_B, POST_B)):
            lvl_m = A[:, 0, PRE_].mean((0, 1)); lvl_c = C[:, 0, PRE_].mean((0, 1))
            did_m = (A[:, 0, POST_].mean(1) - A[:, 0, PRE_].mean(1)) - (A[:, 1, POST_].mean(1) - A[:, 1, PRE_].mean(1))
            did_c = (C[:, 0, POST_].mean(1) - C[:, 0, PRE_].mean(1)) - (C[:, 1, POST_].mean(1) - C[:, 1, PRE_].mean(1))
            lines += [f"## {tag} {var} {est}: sixteen atoms, DMT pre-injection level and primary DiD, MMI and CCS (nats)", "",
                      "| atom | MMI level | MMI DiD (neg/14) | CCS level | CCS DiD (neg/14) |", "|---|---|---|---|---|"]
            for a, n in enumerate(ATOMS):
                lines.append(f"| {n} | {lvl_m[a]:+.4f} | {did_m[:, a].mean():+.4f} ({int((did_m[:, a] < 0).sum())}) | {lvl_c[a]:+.4f} | {did_c[:, a].mean():+.4f} ({int((did_c[:, a] < 0).sum())}) |")
            lines.append(f"| TDMI (sum) | {lvl_m.sum():+.4f} | {did_m.sum(1).mean():+.4f} | {lvl_c.sum():+.4f} | {did_c.sum(1).mean():+.4f} |")
            ac = ac_w if est == "W60" else ac_r
            d_ac = (ac[:, 0, POST_].mean(1) - ac[:, 0, PRE_].mean(1)) - (ac[:, 1, POST_].mean(1) - ac[:, 1, PRE_].mean(1))
            raw_label = f"autocorr {var} W60" if est == "W60" else f"autocorr {var} run-standardised bins"
            raw_sts = raw_did(f"sts {var} W60" if est == "W60" else f"sts {var} global-bins")
            lines += ["", f"Whitened series: mean lag-1 autocorrelation, DMT pre-injection {np.nanmean(ac[:, 0, PRE_]):+.4f}; its DiD {d_ac.mean():+.4f} (raw series {raw_did(raw_label).mean():+.4f}); "
                      f"per subject r(MMI sts DiD, whitened autocorrelation DiD) = {pearsonr(did_m[:, S], d_ac)[0]:+.3f}; r(MMI sts DiD, raw autocorrelation DiD) = {pearsonr(did_m[:, S], raw_did(raw_label))[0]:+.3f}; "
                      f"r(MMI sts DiD whitened, MMI sts DiD raw) = {pearsonr(did_m[:, S], raw_sts)[0]:+.3f}; raw MMI sts DiD {raw_sts.mean():+.4f}."]
            if est == "W60":
                d_obs = (R["obs"][:, 0, POST].mean(1) - R["obs"][:, 0, PRE].mean(1)) - (R["obs"][:, 1, POST].mean(1) - R["obs"][:, 1, PRE].mean(1))
                d_pred = (R["pred"][:, 0, POST].mean(1) - R["pred"][:, 0, PRE].mean(1)) - (R["pred"][:, 1, POST].mean(1) - R["pred"][:, 1, PRE].mean(1))
                lines.append(f"Diagnostic on the whitened series (W = 60): observed sts level {np.nanmean(R['obs']):.4f}, predicted {np.nanmean(R['pred']):.4f}, residual {np.nanmean(R['obs'] - R['pred']):+.4f}; "
                             f"DiD observed {d_obs.mean():+.4f}, predicted {d_pred.mean():+.4f}, residual {(d_obs - d_pred).mean():+.4f} (negative in {int(((d_obs - d_pred) < 0).sum())}/14).")
            lines.append("")
        lines += [f"Chosen AR orders ({tag} {var}), count over 115 regions × 28 runs: " + ", ".join(f"p = {p}: {int((ord_all == p).sum())}" for p in range(1, P_MAX + 1)) + ".", ""]

(OUT / "prewhiten_orders.csv").write_text(f"# partB16_prewhiten.py; chosen AR order per region and run; git={SHA}\n" + "\n".join(orders_csv) + "\n")
(RR / "inference_rows_prewhiten.csv").write_text(f"# partB16_prewhiten.py; git={SHA}\n" + pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows]).to_csv(index=False))
with open(RR / "inference_rows_prewhiten.pkl", "wb") as fh:
    pickle.dump(rows, fh)
lines += ["## Reading under the rule of the pre-run entry", "",
          "A remedy check, reported as such: not a finding about DMT, and the primary result (the raw MMI-sts DiD at W = 60) is unchanged by it. The prediction recorded — MMI-sts near zero after whitening and the DMT contrast shrunk to the order of the cross-lag contrast — is read against the tables above in the outcome entry."]
(OUT / "prewhiten_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
