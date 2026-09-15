"""
rev_phir_items.py — the three whole-brain items of notes/prespec_regional_phir_deconv_2026-09-14.md:
  (1) the deconvolved ΦR contrast at W = 30, both variants, with the full inference of
      rev_inference.Engine (the W = 30 window means and TR-local pair-mean series are computed
      with rev_phiid_fast, validated to ~1e-14 against phyid), plus sts at W = 30 as a by-product
      and the raw ts_gsr W = 30 ΦR from the saved atoms for reference
      → notes/review_results/inference_rows_w30.csv (+ .pkl), deconvolved W30 atom arrays in
        notes/review_results/deconv/
  (2) the 14 per-subject ΦR DiDs (W = 60, deconvolved and raw, both variants) with the DMT and
      placebo changes that make them up
  (3) the placebo-run and DMT-run ΦR by window (W = 60, deconvolved and raw, both variants):
      group mean and SE per window, and the per-subject placebo change
"""
import pickle
import sys
import time
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_inference import Engine, fmt, window_sets
from rev_phiid_fast import PairPhiID, phir, ATOMS

REPO = Path(__file__).resolve().parents[1]
RR = REPO / "notes" / "review_results"
DEC = RR / "deconv"
MAT = "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
t0 = time.time()

dec_path = next(p for p in (DEC / MAT, REPO.parent / "deconv_run" / "sandbox" / "external" / "DMT_NCT" / "data" / MAT) if p.exists())
ts_dec = sio.loadmat(dec_path)


def windowed(ts_obj, W):
    """window means (14, 2, n_win, 16) and TR-local pair-mean series (14, 2, 840, 16), as 01 stores them."""
    n_win = 840 // W
    means = np.full((14, 2, n_win, 16), np.nan)
    local = np.full((14, 2, 840, 16), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts_obj[s, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            for w in range(n_win):
                in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
                if in_w.size <= 5:
                    continue
                pp = PairPhiID(X[:, in_w])
                loc = pp.atoms_local_pairmean()
                local[s, c, in_w[:pp.n]] = loc
                means[s, c, w] = loc.mean(0)
    return means, local


# ------------------------------------------------------------------ (1) W = 30
rows = []
for var in ("ts_gsr", "ts_demean"):
    fm, fl = DEC / f"atoms_win30_115regions-all_{var}_window.npy", DEC / f"atoms_win30_local_115regions-all_{var}_window.npy"
    if fm.exists() and fl.exists():
        A, L = np.load(fm), np.load(fl)
    else:
        A, L = windowed(ts_dec[var], 30)
        np.save(fm, A)
        np.save(fl, L)
    print(f"deconvolved W30 atoms ready for {var} ({time.time() - t0:.0f}s)", flush=True)
    for label, x, xl in ((f"PhiR_deconv {var} W30", phir(A), phir(L)), (f"sts_deconv {var} W30", A[..., IX["sts"]], L[..., IX["sts"]])):
        E = Engine(30)
        rs = E.run(x, xl, label=label)
        for r in rs:
            print(fmt(r), flush=True)
        rows.extend(rs)
# raw ts_gsr W30 ΦR from the saved atoms (reference)
A = np.load(REPO / "results" / "atoms_win30_115regions-all_ts_gsr_window.npy")
L = np.load(REPO / "results" / "atoms_win30_local_115regions-all_ts_gsr_window.npy")
E = Engine(30)
rs = E.run(phir(A), phir(L), label="PhiR ts_gsr W30")
for r in rs:
    print(fmt(r), flush=True)
rows.extend(rs)
pd.DataFrame([{k: v for k, v in r.items() if k != "did_subjects"} for r in rows]).to_csv(RR / "inference_rows_w30.csv", index=False)
with open(RR / "inference_rows_w30.pkl", "wb") as fh:
    pickle.dump(rows, fh)
print(f"wrote {RR / 'inference_rows_w30.csv'} ({len(rows)} rows)")

# ------------------------------------------------------------------ (2) per-subject ΦR DiDs, W = 60
S = window_sets(60)
PRE, POST = S["PRE"], S["primary"]
print("\n(2) per-subject ΦR, W = 60, primary set (windows 6–14 vs 1–4): DMT change, PCB change, DiD")
subj_tables = {}
for series, base in (("deconv", DEC), ("raw", REPO / "results")):
    for var in ("ts_gsr", "ts_demean"):
        A = np.load(base / f"atoms_win60_115regions-all_{var}_window.npy")
        P = phir(A)
        ch = P[:, :, POST].mean(2) - P[:, :, PRE].mean(2)
        d = ch[:, 0] - ch[:, 1]
        subj_tables[(series, var)] = (ch, d, P)
        print(f"   {series:6s} {var:9s}: DiD {np.array2string(d, precision=4, floatmode='fixed', max_line_width=250)}")
        print(f"          DMT change {np.array2string(ch[:, 0], precision=4, floatmode='fixed', max_line_width=250)}")
        print(f"          PCB change {np.array2string(ch[:, 1], precision=4, floatmode='fixed', max_line_width=250)}")
        print(f"          mean DiD {d.mean():+.4f}; positive {int((d > 0).sum())}/14; DMT rise {int((ch[:, 0] > 0).sum())}/14; PCB fall {int((ch[:, 1] < 0).sum())}/14; "
              f"median DiD {np.median(d):+.4f}; DiD without subject of max |DiD| {np.delete(d, np.argmax(np.abs(d))).mean():+.4f}")
# agreement of per-subject DiDs, deconvolved vs raw, and ΦR vs sts (deconvolved)
from scipy.stats import pearsonr, spearmanr
for var in ("ts_gsr", "ts_demean"):
    d_dec, d_raw = subj_tables[("deconv", var)][1], subj_tables[("raw", var)][1]
    A = np.load(DEC / f"atoms_win60_115regions-all_{var}_window.npy")
    sts = A[..., IX["sts"]]
    d_sts = (sts[:, 0, POST].mean(1) - sts[:, 0, PRE].mean(1)) - (sts[:, 1, POST].mean(1) - sts[:, 1, PRE].mean(1))
    print(f"   {var}: per-subject ΦR DiD deconvolved vs raw r = {pearsonr(d_dec, d_raw)[0]:+.3f} (Spearman {spearmanr(d_dec, d_raw)[0]:+.3f}); "
          f"deconvolved ΦR DiD vs deconvolved sts DiD r = {pearsonr(d_dec, d_sts)[0]:+.3f} (Spearman {spearmanr(d_dec, d_sts)[0]:+.3f})")

# ------------------------------------------------------------------ (3) ΦR by window
print("\n(3) ΦR by window, W = 60: group mean (SE over 14 subjects)")
for series in ("deconv", "raw"):
    for var in ("ts_gsr", "ts_demean"):
        ch, d, P = subj_tables[(series, var)]
        for c, cn in enumerate(("DMT", "PCB")):
            m, se = P[:, c].mean(0), P[:, c].std(0, ddof=1) / np.sqrt(14)
            print(f"   {series:6s} {var:9s} {cn}: " + " ".join(f"{v:.4f}({e:.4f})" for v, e in zip(m, se)))
        pcb_pre, pcb_post = P[:, 1, PRE].mean(1), P[:, 1, POST].mean(1)
        print(f"          PCB pre-mean {pcb_pre.mean():.4f} → post-mean {pcb_post.mean():.4f}; per-subject PCB change "
              f"{np.array2string(ch[:, 1], precision=4, floatmode='fixed', max_line_width=250)}; fall in {int((ch[:, 1] < 0).sum())}/14")
        # where in the run the placebo fall sits: pcb mean of windows 1-4, 5, 6-9, 10-14
        g = P[:, 1].mean(0)
        print(f"          PCB group mean by block: windows 1–4 {g[:4].mean():.4f}, 5 {g[4]:.4f}, 6–9 {g[5:9].mean():.4f}, 10–14 {g[9:].mean():.4f} | "
              f"DMT: {P[:, 0].mean(0)[:4].mean():.4f}, {P[:, 0].mean(0)[4]:.4f}, {P[:, 0].mean(0)[5:9].mean():.4f}, {P[:, 0].mean(0)[9:].mean():.4f}")
print(f"done ({time.time() - t0:.0f}s)")
