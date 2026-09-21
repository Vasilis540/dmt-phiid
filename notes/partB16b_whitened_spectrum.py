"""
partB16b_whitened_spectrum.py — B16b: where the power of the prewhitened series lies.
Pre-run entry: manuscript/analysis_record.md, "The whitened series' spectrum (B16b): pre-run entry, 21 Sep 2026"
(specification, prediction and rule as commissioned on 21 Sep 2026, round 14, Stage A).

For each region and run of both released variants (ts_gsr, ts_demean): the raw series and four residual series —
"ar1": AR(1); "arp": AR(p) with p by BIC over 1–5 (partB16_prewhiten.py's ar_fit and whiten, copied verbatim below,
recomputed here and not saved); "p10": fixed p = 10; "p20": fixed p = 20 (ordinary least squares with intercept on
the run's finite samples; the first p samples of the run non-finite). For each of the five series:
  - the share of power inside 0.01–0.08 Hz exactly as rev_extra.py (c) computes it: the periodogram |rfft(x − x̄)|²
    of the run's kept samples (the TRs finite in every region, concatenated) at TR 2 s, summed over the 115 regions,
    the in-band sum (0.01 ≤ f ≤ 0.08 Hz) divided by the total; the shares below 0.01 Hz and above 0.08 Hz the same way;
  - the run-level lag-1 autocorrelation as rev_extra.py's r1_obs: each region's kept samples standardised over the
    run (ddof = 1), the mean product of the series with its lag-1 copy, averaged over regions;
  - the W = 60 window-level mean r₁ of DMT windows 1–4 (rev_series.autocorr_series, window mode, on the series with
    its non-finite samples in place, averaged over windows 1–4 of the DMT run and over subjects), as B16 reports it.
Table per variant: one row per series, the five quantities averaged over region–runs (the shares over the 28 runs,
the run-level autocorrelation over the 28 runs of the region means, the window-level r₁ over the 14 subjects), with
the SD over runs in brackets. Reference values (header): the raw in-band share 0.992 and the r₁ of ideal flat-spectrum
noise on the band at TR 2 s, 0.8176 (rev_extra.log); the band's share of the Nyquist range, 0.07/0.25 = 0.28.
Consistency lines: the BIC orders recomputed (B16: p = 5 for 3,218 of 3,220 region–runs on ts_gsr, 3,215 on
ts_demean); the raw window-level r₁ against inference_rows_raw.csv (0.8479 on ts_gsr, DMT windows 1–4).
No atoms are computed at any order. Free choices: BIC range 1–5 as B16; fixed orders 10 and 20; band edges 0.01 and
0.08 Hz inclusive as rev_extra.py; region 20 excluded; seed 20261120 (no random draws).
Outputs (notes/review_results/partB/): whitened_spectrum_tables.md; whitened_spectrum_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB16b_whitened_spectrum.py   (minutes)
"""
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_series import autocorr_series
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
SEED = 20261120
P_MAX = 5
TR = 2.0
F_LO, F_HI = 0.01, 0.08
REF_SHARE_RAW, REF_R1_FLAT, REF_BAND_SHARE = 0.992, 0.8176, 0.07 / 0.25
RAW_WIN_R1 = {"ts_gsr": "0.8479", "ts_demean": "0.8382"}       # inference_rows_raw.csv, the committed raw values, for the consistency line
SERIES = (("raw", None), ("ar1", "ar1"), ("arp", "arp"), ("p10", 10), ("p20", 20))
t0 = time.time()
ts = sio.loadmat(MAT)


# ---- copied verbatim from partB16_prewhiten.py (the whitening of B16) ----
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
# ---- end of the copied block ----


def fixed_order(X, p):
    return np.stack([ar_fit(X[i], p)[0] for i in range(X.shape[0])], 0)


def spectrum_and_r1(Y):
    """Y (115, T) with non-finite samples: (in-band share, share below, share above, run-level r1) as rev_extra.py (c)."""
    kept = np.all(np.isfinite(Y), axis=0)
    Yk = Y[:, kept]
    P = np.abs(np.fft.rfft(Yk - Yk.mean(1, keepdims=True), axis=1)) ** 2
    f = np.fft.rfftfreq(Yk.shape[1], TR)
    tot = P.sum()
    band = (f >= F_LO) & (f <= F_HI)
    Z = (Yk - Yk.mean(1, keepdims=True)) / Yk.std(1, ddof=1, keepdims=True)
    r1 = np.mean((Z[:, :-1] * Z[:, 1:]).mean(1))
    return P[:, band].sum() / tot, P[:, f < F_LO].sum() / tot, P[:, f > F_HI].sum() / tot, r1, int(kept.sum())


lines = ["# Where the power of the prewhitened series lies (partB16b_whitened_spectrum.py)", f"git={SHA}", "",
         f"Per region and run: the raw series and the residuals of AR(1), AR(p) with p by BIC over 1–{P_MAX} (B16's whitening, recomputed), and fixed p = 10 and p = 20 (OLS with intercept; the first p samples dropped). "
         f"In-band share = periodogram power at {F_LO} ≤ f ≤ {F_HI} Hz over the total, the run's kept samples pooled over regions, as rev_extra.py (c); run-level r₁ as rev_extra.py's r1_obs; window-level r₁ = rev_series.autocorr_series (window mode, W = 60), DMT windows 1–4, as B16. "
         f"Reference values: raw in-band share {REF_SHARE_RAW} and r₁ of ideal flat-spectrum noise on the band at TR {TR:.0f} s {REF_R1_FLAT} (rev_extra.log); the band's share of the Nyquist range {F_HI - F_LO:.2f}/{1 / (2 * TR):.2f} = {REF_BAND_SHARE:.2f}. "
         f"Seed {SEED} (no random draws). Region 20 excluded.", ""]
for var in ("ts_gsr", "ts_demean"):
    acc = {name: {k: [] for k in ("in", "below", "above", "r1", "kept")} for name, _ in SERIES}
    ts_w = {name: np.empty((14, 2), dtype=object) for name, _ in SERIES}
    orders_all = np.zeros((14, 2, 115), int)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            series = {"raw": X}
            series["ar1"], _ = whiten(X, "ar1")
            series["arp"], orders_all[s, c] = whiten(X, "arp")
            series["p10"] = fixed_order(X, 10)
            series["p20"] = fixed_order(X, 20)
            for name, _ in SERIES:
                sh_in, sh_below, sh_above, r1, n_kept = spectrum_and_r1(series[name])
                for k, v in (("in", sh_in), ("below", sh_below), ("above", sh_above), ("r1", r1), ("kept", n_kept)):
                    acc[name][k].append(v)
                full = np.full((116, 840), np.nan); full[REGIONS] = series[name]; ts_w[name][s, c] = full
        print(f"   {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
    lines += [f"## {var}: power shares and lag-1 autocorrelation of the raw and the whitened series (mean over the 28 runs; SD over runs in brackets)", "",
              "| series | in-band share (0.01–0.08 Hz) | share below 0.01 Hz | share above 0.08 Hz | run-level r₁ | W = 60 r₁, DMT windows 1–4 | kept samples per run |", "|---|---|---|---|---|---|---|"]
    win_r1 = {}
    for name, _ in SERIES:
        ac, _ = autocorr_series(ts_w[name], 60, "window")
        win_r1[name] = np.nanmean(ac[:, 0, 0:4], axis=1)                   # per subject, DMT windows 1–4
        A = {k: np.array(v) for k, v in acc[name].items()}
        lines.append(f"| {name} | {A['in'].mean():.3f} ({A['in'].std(ddof=1):.3f}) | {A['below'].mean():.3f} ({A['below'].std(ddof=1):.3f}) | {A['above'].mean():.3f} ({A['above'].std(ddof=1):.3f}) | "
                     f"{A['r1'].mean():+.4f} ({A['r1'].std(ddof=1):.4f}) | {win_r1[name].mean():+.4f} ({win_r1[name].std(ddof=1):.4f}) | {A['kept'].mean():.1f} |")
    lines += ["", f"Consistency: BIC orders recomputed ({var}), count over 115 regions × 28 runs: " + ", ".join(f"p = {p}: {int((orders_all == p).sum())}" for p in range(1, P_MAX + 1)) +
              f" (B16: p = 5 for {'3,218' if var == 'ts_gsr' else '3,215'}); raw in-band share {np.mean(acc['raw']['in']):.3f} (rev_extra.log: {REF_SHARE_RAW}); "
              f"raw W = 60 r₁ of DMT windows 1–4 {win_r1['raw'].mean():.4f} (inference_rows_raw.csv, pre_dmt of 'autocorr {var} W60': {RAW_WIN_R1[var]}).", ""]
lines += ["## Prediction and rule of the pre-run entry", "",
          "Prediction: the AR(1) residual keeps most of its power in band (share above 0.9) with r₁ near 0.75; the AR(p ≤ 5) residual's in-band share falls to about 0.5–0.6 (a mixture of flattened in-band noise at r₁ = 0.82 and amplified above-band residue at r₁ ≈ −0.4 has r₁ = 0.26 at an in-band share of 0.54); "
          "at p = 10 and 20 the share falls further toward 0.28 as r₁ approaches zero — the whitened series is increasingly the amplified stop-band residue. "
          "Rule: descriptive; quoted in the Remedies paragraph; no atoms are computed at p = 10 or 20. If the prediction fails (the AR(p) share stays above 0.9), the \"amplified residue\" explanation is dropped from the text and the remaining autocorrelation is reported without it."]
(OUT / "whitened_spectrum_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
