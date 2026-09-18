"""
rev_extra.py — supporting facts for the review computations (not requested as separate items;
they bear on reading items 1 and 3):

  (a) per-subject agreement between the contrasts: Spearman/Pearson r between the 14 subject
      DiDs of mean lag-1 autocorrelation and of sts (and of ΦR and sts), W60, both variants
  (b) the group-mean window series of autocorrelation vs sts (14 windows × 2 conditions):
      Pearson r, and the within-condition r
  (c) what the lag-1 autocorrelation level is for band-passed data: r1 of white noise passed
      through an ideal 0.01–0.08 Hz band-pass at TR 2 s, N = 840, versus the observed run-level r1;
      the in-band spectral centroid (0.01–0.08 Hz) pre (TRs 0–239) vs post (TRs 300–839) per
      subject × condition, DiD with exact sign-flip p and bootstrap CI
  (d) variance non-stationarity: window variance / run variance (mean over regions, W = 60), raw
      and deconvolved series, DiD in the primary form; group means by window
  (e) correlation of each estimator's series with the window-variance ratio (per run, and of
      the group-mean series): global-fit sts per bin, run-standardised autocorrelation per bin,
      windowed W60 sts, window-standardised autocorrelation W60
  (f) the slopes behind the two trend corrections (sts, W60): placebo-run slope, the shared
      slope b of model (b), the DMT run's slope over its post windows; implied placebo changes
  (g) the rsHRF outputs: time-to-peak and events per region of the estimated HRFs by run;
      run-level r1 and in-band power share of the deconvolved series
Reads notes/review_results/inference_rows_raw.pkl (rev_run.py), the source .mat, the saved atom
arrays and the deconvolution outputs (rev_deconv.py) when present.
"""
import pickle
import sys
from itertools import product
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.stats import pearsonr, spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_series import autocorr_series, phir_from_atoms, IX, REGIONS
from rev_git import SHA
print(f"git={SHA}", flush=True)

SEED = 20261120
rng = np.random.default_rng(SEED)
SIGNS = np.array(list(product((-1, 1), repeat=14)))
REPO = Path(__file__).resolve().parents[1]
ORIG = REPO / "results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
RR = REPO / "notes" / "review_results"
rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))


def get(label, s="primary"):
    return [r for r in rows if r["label"] == label and r["set"] == s][0]


def signflip_p(v):
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= abs(v.mean()) - 1e-12))


def boot(v, n=10000):
    d = v[rng.integers(0, v.size, (n, v.size))].mean(1)
    return np.percentile(d, [2.5, 97.5])


print("(a) per-subject DiD agreement (primary set):")
for var in ("ts_gsr", "ts_demean"):
    for W in ("W60",):
        a = get(f"autocorr {var} {W}")["did_subjects"]
        s = get(f"sts {var} {W}")["did_subjects"]
        p = get(f"PhiR {var} {W}")["did_subjects"]
        print(f"   {var} {W}: autocorr vs sts  Pearson r = {pearsonr(a, s)[0]:+.3f} (p = {pearsonr(a, s)[1]:.4f}), Spearman rho = {spearmanr(a, s)[0]:+.3f}"
              f" | PhiR vs sts  Pearson r = {pearsonr(p, s)[0]:+.3f} (p = {pearsonr(p, s)[1]:.3f}), Spearman rho = {spearmanr(p, s)[0]:+.3f}")
        print(f"      subject DiDs autocorr: {np.array2string(a, precision=4, floatmode='fixed', max_line_width=200)}")
        print(f"      subject DiDs sts     : {np.array2string(s, precision=4, floatmode='fixed', max_line_width=200)}")
    a = get(f"autocorr {var} run-standardised bins")["did_subjects"]
    s = get(f"sts {var} global-bins")["did_subjects"]
    print(f"   {var} global/bins: autocorr(run-std) vs sts  Pearson r = {pearsonr(a, s)[0]:+.3f} (p = {pearsonr(a, s)[1]:.4f}), Spearman rho = {spearmanr(a, s)[0]:+.3f}")

print("\n(b) group-mean window series (W60), autocorr vs sts:")
ts = sio.loadmat(MAT)
for var in ("ts_gsr", "ts_demean"):
    A = np.load(ORIG / f"atoms_win60_115regions-all_{var}_window.npy")
    sts = A[..., IX["sts"]].mean(0)                       # (2, 14)
    ac = autocorr_series(ts[var], 60, "window")[0].mean(0)
    r_all = pearsonr(ac.ravel(), sts.ravel())[0]
    print(f"   {var}: r over 28 condition-windows = {r_all:+.3f}; within DMT r = {pearsonr(ac[0], sts[0])[0]:+.3f}; within PCB r = {pearsonr(ac[1], sts[1])[0]:+.3f}")
    print(f"      DMT autocorr by window: {np.array2string(ac[0], precision=3, floatmode='fixed', max_line_width=200)}")
    print(f"      DMT sts      by window: {np.array2string(sts[0], precision=3, floatmode='fixed', max_line_width=200)}")
    print(f"      PCB autocorr by window: {np.array2string(ac[1], precision=3, floatmode='fixed', max_line_width=200)}")
    print(f"      PCB sts      by window: {np.array2string(sts[1], precision=3, floatmode='fixed', max_line_width=200)}")

print("\n(c) band-pass and the level of r1:")
N, TR = 840, 2.0
f = np.fft.rfftfreq(N, TR)
band = (f >= 0.01) & (f <= 0.08)
r1_flat = np.sum(np.cos(2 * np.pi * f[band] * TR)) / band.sum()
print(f"   ideal 0.01–0.08 Hz band-pass, flat in-band spectrum, TR 2 s: implied lag-1 autocorrelation r1 = {r1_flat:.4f}")
for var in ("ts_gsr", "ts_demean"):
    r1_obs = []
    frac_in = []
    cent = np.full((14, 2, 2), np.nan)                       # subject, cond, (pre, post)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts[var][s, c], float)[REGIONS]
            keep = np.all(np.isfinite(X), axis=0)
            Xk = X[:, keep]
            Z = (Xk - Xk.mean(1, keepdims=True)) / Xk.std(1, ddof=1, keepdims=True)
            r1_obs.append(np.mean((Z[:, :-1] * Z[:, 1:]).mean(1) * (Xk.shape[1] - 1) / (Xk.shape[1] - 1)))
            P = np.abs(np.fft.rfft(Xk - Xk.mean(1, keepdims=True), axis=1)) ** 2
            fk = np.fft.rfftfreq(Xk.shape[1], TR)
            bk = (fk >= 0.01) & (fk <= 0.08)
            frac_in.append(P[:, bk].sum() / P.sum())
            for j, sl in enumerate((slice(0, 240), slice(300, 840))):
                Xs = X[:, sl]
                Xs = Xs[:, np.all(np.isfinite(Xs), axis=0)]
                Ps = np.abs(np.fft.rfft(Xs - Xs.mean(1, keepdims=True), axis=1)) ** 2
                fs = np.fft.rfftfreq(Xs.shape[1], TR)
                bs = (fs >= 0.01) & (fs <= 0.08)
                cent[s, c, j] = np.mean((Ps[:, bs] * fs[bs]).sum(1) / Ps[:, bs].sum(1))
    d = (cent[:, 0, 1] - cent[:, 0, 0]) - (cent[:, 1, 1] - cent[:, 1, 0])
    lo, hi = boot(d)
    print(f"   {var}: observed run-level r1 (mean over subjects × conditions × regions) = {np.mean(r1_obs):.4f}; share of power inside 0.01–0.08 Hz = {np.mean(frac_in):.3f}")
    print(f"      in-band spectral centroid (Hz): DMT pre {cent[:, 0, 0].mean():.4f} post {cent[:, 0, 1].mean():.4f} | PCB pre {cent[:, 1, 0].mean():.4f} post {cent[:, 1, 1].mean():.4f}"
          f" | DiD {d.mean():+.5f} Hz [{lo:+.5f}, {hi:+.5f}] sign-flip p = {signflip_p(d):.4f}, {(d > 0).sum()}/14 positive")


# ----------------------------------------------------------------------------- (d), (e)
DECONV_MAT = next((p for p in (RR / "deconv" / MAT.name, REPO.parent / "deconv_run" / "sandbox" / "external" / "DMT_NCT" / "data" / MAT.name) if p.exists()), RR / "deconv" / MAT.name)  # rev_deconv.py output


def variance_ratio(ts_obj, W):
    out = np.full((14, 2, 840 // W), np.nan)
    for s in range(14):
        for c in range(2):
            X = np.asarray(ts_obj[s, c], float)[REGIONS]
            keep = np.all(np.isfinite(X), axis=0)
            rv = X[:, keep].var(1, ddof=1)
            for w in range(840 // W):
                m = keep.copy()
                m[:w * W] = False
                m[(w + 1) * W:] = False
                out[s, c, w] = np.mean(X[:, m].var(1, ddof=1) / rv)
    return out


print("\n(d) variance non-stationarity: window variance / run variance (mean over regions), W60, primary-form DiD:")
sources = [("raw", ts)]
if DECONV_MAT.exists():
    sources.append(("deconvolved", sio.loadmat(DECONV_MAT)))
for tag, obj in sources:
    for var in ("ts_gsr", "ts_demean"):
        vr = variance_ratio(obj[var], 60)
        pre, post = vr[:, :, :4].mean(2), vr[:, :, 5:14].mean(2)
        ch = post - pre
        d = ch[:, 0] - ch[:, 1]
        lo, hi = boot(d)
        print(f"   {tag:11s} {var:9s}: DMT pre {pre[:, 0].mean():.3f} post {post[:, 0].mean():.3f} | PCB pre {pre[:, 1].mean():.3f} post {post[:, 1].mean():.3f}"
              f" | DiD {d.mean():+.4f} [{lo:+.4f}, {hi:+.4f}] p = {signflip_p(d):.4f}, {(d < 0).sum()}/14 negative")
        print("      DMT group mean by window:", np.array2string(vr[:, 0].mean(0), precision=3, floatmode="fixed", max_line_width=200))
        print("      PCB group mean by window:", np.array2string(vr[:, 1].mean(0), precision=3, floatmode="fixed", max_line_width=200))

print("\n(e) correlation of each series with the window-variance ratio (raw data):")
for var in ("ts_gsr", "ts_demean"):
    vr30, vr60 = variance_ratio(ts[var], 30), variance_ratio(ts[var], 60)
    G = np.load(ORIG / f"atoms_bins_115regions-all_{var}_global.npy")[..., IX["sts"]]
    Wn = np.load(ORIG / f"atoms_win60_115regions-all_{var}_window.npy")[..., IX["sts"]]
    ac_run = autocorr_series(ts[var], 30, "run")[0]
    ac_win = autocorr_series(ts[var], 60, "window")[0]
    for name, Y, V in (("global-fit sts per 30-TR bin", G, vr30), ("run-standardised autocorr per bin", ac_run, vr30),
                       ("windowed W60 sts", Wn, vr60), ("window-standardised autocorr W60", ac_win, vr60)):
        rs = [pearsonr(Y[s, c], V[s, c])[0] for s in range(14) for c in range(2)]
        rg = pearsonr(Y.mean(0).ravel(), V.mean(0).ravel())[0]
        print(f"   {var} {name:36s}: mean r over the 28 runs {np.mean(rs):+.3f} (min {np.min(rs):+.3f}, max {np.max(rs):+.3f}); group-mean series r = {rg:+.3f}")

# ----------------------------------------------------------------------------- (f)
print("\n(f) slopes behind the trend corrections (sts, W60, nats per window, mean over subjects):")
for var in ("ts_gsr", "ts_demean"):
    X = np.load(ORIG / f"atoms_win60_115regions-all_{var}_window.npy")[..., IX["sts"]]
    w = np.arange(14.)
    PRE, post = np.arange(0, 4), np.arange(5, 14)
    keep = np.r_[PRE, post]
    b_pcb, b_shared, b_dmt = [], [], []
    for s in range(14):
        b_pcb.append(np.polyfit(w, X[s, 1], 1)[0])
        y = np.r_[X[s, 0, keep], X[s, 1, keep]]
        cond = np.r_[np.zeros(keep.size), np.ones(keep.size)]
        tt = np.r_[w[keep], w[keep]]
        drug = np.r_[np.isin(keep, post).astype(float), np.zeros(keep.size)]
        b_shared.append(np.linalg.lstsq(np.c_[np.ones(y.size), cond, tt, drug], y, rcond=None)[0][2])
        b_dmt.append(np.polyfit(w[post], X[s, 0, post], 1)[0])
    gap = post.mean() - PRE.mean()
    print(f"   {var}: placebo run over all 14 windows {np.mean(b_pcb):+.5f}; shared slope b of model (b) {np.mean(b_shared):+.5f}; DMT run over windows 6–14 alone {np.mean(b_dmt):+.5f}")
    print(f"      window-index gap post − pre = {gap:.2f}; implied placebo change: placebo line {np.mean(b_pcb) * gap:+.4f}, shared slope {np.mean(b_shared) * gap:+.4f}; raw placebo change {(X[:, 1, post].mean(1) - X[:, 1, PRE].mean(1)).mean():+.4f}")

# ----------------------------------------------------------------------------- (g)
print("\n(g) rsHRF outputs:")
for var, d in (("ts_gsr", "gsr"), ("ts_demean", "demean")):
    hp = RR / "deconv" / f"hrf_{var}.npy"
    if not hp.exists() or not DECONV_MAT.exists():
        print(f"   {var}: deconvolution outputs not present")
        continue
    H = np.load(hp)[:, :, REGIONS, :]
    E = np.load(RR / "deconv" / f"events_{var}.npy")[:, :, REGIONS]
    ttp = H.argmax(-1) * 2.0
    print(f"   {var}: estimated HRF (per region per run, TR resolution, 24 s) time-to-peak DMT run {ttp[:, 0].mean():.2f} s, PCB run {ttp[:, 1].mean():.2f} s;"
          f" events per region (1 SD threshold, 840 TRs) DMT {E[:, 0].mean():.1f}, PCB {E[:, 1].mean():.1f}")
    td = sio.loadmat(DECONV_MAT)[var]
    r1d, frd = [], []
    for s in range(14):
        for c in range(2):
            X = np.asarray(td[s, c], float)[REGIONS]
            Xk = X[:, np.all(np.isfinite(X), axis=0)]
            Z = (Xk - Xk.mean(1, keepdims=True)) / Xk.std(1, ddof=1, keepdims=True)
            r1d.append(np.mean((Z[:, :-1] * Z[:, 1:]).mean(1)))
            P = np.abs(np.fft.rfft(Xk - Xk.mean(1, keepdims=True), axis=1)) ** 2
            fk = np.fft.rfftfreq(Xk.shape[1], TR)
            bk = (fk >= 0.01) & (fk <= 0.08)
            frd.append(P[:, bk].sum() / P.sum())
    print(f"      deconvolved series: run-level r1 = {np.mean(r1d):.4f}; share of power inside 0.01–0.08 Hz = {np.mean(frd):.3f}")
