"""
rev_sts_matched_null.py — the null the record named as a precondition and never ran:
"A pair of conditions with equal analytic sts but different covariance … would test whether
condition-dependent bias can manufacture an sts difference from nothing."

Three families, each a pair (baseline, shifted) with IDENTICAL analytic (true) sts under the
Gaussian-MMI model, obtained by root-finding one compensating parameter:

  F1  the record's asymmetric VAR(1) family (a ≈ 0.5): (i) autocorrelation a lowered by 0.05,
      compensated by cross-coupling c; (ii) noise correlation q raised to 0.60, compensated by a
  F2  the record's AR family at a = 0.87: a lowered by 0.02, compensated by c
  F3  Gaussian processes with the EMPIRICAL pooled autocorrelation function of the data:
      baseline = placebo-run ACF, shifted = DMT post-injection ACF (TRs 300-839), each region
      pair generated as the same linear filter applied to two white noises with correlation q;
      analytic sts matched by solving for q of the shifted condition
      (the 4-vector covariance is then [[1, q, r1, q r1], [q, 1, q r1, r1], …]).

For each pair and W in (30, 60, 840): N_WIN independent windows per condition, phyid's
calc_PhiID per window, window-mean sts; the "manufactured" difference = mean(shifted) −
mean(baseline) with its SE, in nats and as a share of the real primary DiD (−0.0809).
Analytic atoms via the same phyid downstream functions as 02_bias_check.py.
"""
import sys
import time
from pathlib import Path

import numpy as np
import scipy.io as sio
from scipy.optimize import brentq

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_git import SHA
print(f"git={SHA}", flush=True)
import importlib
bc = importlib.import_module("02_bias_check")
from phyid.calculate import calc_PhiID

SEED = 20261120
N_WIN = 4000
WINDOWS = (30, 60, 840)
REAL_DID = -0.0809
rng = np.random.default_rng(SEED)
t0 = time.time()
ONLY = sys.argv[1:] or ["f1", "f2", "f3"]


def sts_of_params(p):
    A, Q = bc.var1_matrices(**p)
    S4 = bc.joint_lag_cov(A, Q, bc.TAU)
    atoms, calc = bc.analytic_atoms(S4, "MMI")
    return atoms["sts"], atoms, S4


def set_comp(shifted, comp, v):
    p = dict(shifted)
    if comp == "c":
        r = shifted["c"][1] / shifted["c"][0] if shifted["c"][0] else 1.0
        p["c"] = (v, v * r)
    elif comp == "a":
        r = shifted["a"][1] / shifted["a"][0]
        p["a"] = (v, v * r)
    else:
        p["q"] = v
    return p


def match(base, shifted, comp, lo, hi):
    """Find the value of `comp` in [lo, hi] (stable region only) at which the shifted condition's
    analytic sts equals the baseline's; grid scan for a sign change, then brentq."""
    target = sts_of_params(base)[0]

    def f(v):
        try:
            return sts_of_params(set_comp(shifted, comp, v))[0] - target
        except AssertionError:
            return np.nan

    grid = np.linspace(lo, hi, 400)
    vals = np.array([f(v) for v in grid])
    ok = np.isfinite(vals)
    if not ok.any():
        raise ValueError("no stable value of the compensating parameter in range")
    g, fv = grid[ok], vals[ok]
    idx = np.where(np.sign(fv[:-1]) != np.sign(fv[1:]))[0]
    if idx.size == 0:
        raise ValueError(f"no sign change: sts difference ranges {fv.min():+.4f} .. {fv.max():+.4f} over the stable range {g.min():.3f}-{g.max():.3f}")
    i = idx[0]
    v = brentq(f, g[i], g[i + 1], xtol=1e-10)
    return set_comp(shifted, comp, v)


def estimate_var1(p, W, n):
    A, Q = bc.var1_matrices(**p)
    z = bc.simulate(A, Q, W, n, rng)
    return np.array([np.mean(calc_PhiID(z[i, 0], z[i, 1], tau=1, kind="gaussian", redundancy="MMI")[0]["sts"]) for i in range(n)])


def report_pair(name, pb, ps, est_fn, describe):
    print(f"\n=== {name}")
    print("   baseline:", describe(pb))
    print("   shifted :", describe(ps))
    for W in WINDOWS:
        eb = est_fn(pb, W, N_WIN)
        es = est_fn(ps, W, N_WIN)
        d = es.mean() - eb.mean()
        se = np.sqrt(eb.var(ddof=1) / N_WIN + es.var(ddof=1) / N_WIN)
        print(f"   W={W:3d}: est sts baseline {eb.mean():.4f}, shifted {es.mean():.4f}; manufactured difference {d:+.4f} ± {se:.4f}"
              f"  = {d / abs(REAL_DID) * 100:+.0f} % of the real |DiD|   ({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ F1, F2: VAR(1)
def describe_var1(p):
    sts, atoms, S4 = sts_of_params(p)
    c = bc.implied_correlations(S4)
    return (f"a={tuple(round(v, 4) for v in p['a'])} c={tuple(round(v, 4) for v in p['c'])} q={p['q']:.4f} s={p['s']} | "
            f"autocorr ({c['auto_x']:.3f},{c['auto_y']:.3f}) corr(x,y) {c['xy']:.3f} | analytic sts {sts:.4f} rtr {atoms['rtr']:.4f} xtx {atoms['xtx']:.4f}")


base = bc.CONDITIONS["asym_baseline"]
sh = dict(base); sh["a"] = (0.50, 0.40 * 0.50 / 0.55)
if "f1" not in ONLY:
    pass
try:
    if "f1" in ONLY: report_pair("F1-i asym VAR(1): a 0.55->0.50 (both scaled), c compensates", base, match(base, sh, "c", 0.001, 0.6), estimate_var1, describe_var1)
except ValueError as e:
    print("F1-i: no compensating c in range:", e)
sh = dict(base); sh["q"] = 0.60
try:
    if "f1" in ONLY: report_pair("F1-ii asym VAR(1): q 0.20->0.60, a compensates", base, match(base, sh, "a", 0.05, 0.9), estimate_var1, describe_var1)
except ValueError as e:
    print("F1-ii: no compensating a in range:", e)
base2 = bc.AR_CONDITIONS["ar_baseline"]
if "f2" in ONLY:
    sh = dict(base2); sh["a"] = (0.85, 0.85)
    done = False
    for comp, lo, hi in (("c", 0.001, 0.25), ("q", -0.9, 0.9)):
        try:
            report_pair(f"F2 AR VAR(1) a=0.87: a -> 0.85, {comp} compensates", base2, match(base2, sh, comp, lo, hi), estimate_var1, describe_var1)
            done = True
            break
        except ValueError as e:
            print(f"F2 ({comp}): {e}")
    sh = dict(base2); sh["q"] = 0.30
    try:
        report_pair("F2-ii AR VAR(1) a=0.87: q 0.05 -> 0.30, a compensates", base2, match(base2, sh, "a", 0.5, 0.95), estimate_var1, describe_var1)
    except ValueError as e:
        print(f"F2-ii (a): {e}")

# ------------------------------------------------------------------ F3: empirical-ACF Gaussian processes
if "f3" not in ONLY and "f3b" not in ONLY:
    print("done"); sys.exit(0)
ts = sio.loadmat(REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat")["ts_gsr"]
regs = [r for r in range(116) if r != 20]
LMAX = 40


def pooled_acf(cond, tr_slice):
    acf = np.zeros(LMAX + 1); n = 0
    for s in range(14):
        X = ts[s, cond][regs][:, tr_slice]
        X = X[:, np.all(np.isfinite(X), axis=0)]
        X = X - X.mean(1, keepdims=True); v = (X ** 2).mean(1)
        for k in range(LMAX + 1):
            acf[k] += np.mean((X[:, :X.shape[1] - k] * X[:, k:]).mean(1) / v)
        n += 1
    return acf / n


NFFT = 2048


def psd_from_acf(acf):
    taper = 0.5 * (1 + np.cos(np.pi * np.arange(LMAX + 1) / LMAX))       # Hann taper to zero at LMAX
    g = acf * taper
    full = np.zeros(NFFT); full[:LMAX + 1] = g; full[NFFT - LMAX:] = g[1:][::-1]
    psd = np.real(np.fft.fft(full)); psd = np.clip(psd, 0, None)
    acf_eff = np.real(np.fft.ifft(psd))[:LMAX + 1]                        # ACF actually realised
    return psd, acf_eff / acf_eff[0]


def gp_params(acf_eff, q):
    r1 = acf_eff[1]
    S4 = np.array([[1, q, r1, q * r1], [q, 1, q * r1, r1], [r1, q * r1, 1, q], [q * r1, r1, q, 1]], float)
    atoms, _ = bc.analytic_atoms(S4, "MMI")
    return atoms, S4


def simulate_gp(psd, q, W, n):
    amp = np.sqrt(psd / NFFT)
    out = np.empty((n, 2, W))
    for i in range(n):
        w1 = rng.standard_normal(NFFT); w3 = rng.standard_normal(NFFT)
        w2 = q * w1 + np.sqrt(1 - q ** 2) * w3
        x = np.real(np.fft.ifft(np.fft.fft(w1) * amp)) * np.sqrt(NFFT)
        y = np.real(np.fft.ifft(np.fft.fft(w2) * amp)) * np.sqrt(NFFT)
        st = rng.integers(0, NFFT - W)
        out[i, 0] = x[st:st + W]; out[i, 1] = y[st:st + W]
    return out


acf_pcb = pooled_acf(1, slice(0, 840))
acf_dmt = pooled_acf(0, slice(300, 840))
psd_p, acf_p = psd_from_acf(acf_pcb)
psd_d, acf_d = psd_from_acf(acf_dmt)
print("\nF3 empirical ACFs (realised after taper/clip): placebo lags 1-6", np.round(acf_p[1:7], 3), "| DMT post", np.round(acf_d[1:7], 3))

# (a) how the analytic sts of this family depends on r1 and q
print("   analytic sts as a function of lag-1 autocorrelation r1 (rows) and cross-correlation q (cols):")
qs = [0.0, 0.2, 0.4, 0.6, 0.8]
print("        q=  " + "  ".join(f"{q:6.2f}" for q in qs))
for r1 in (0.80, 0.84, 0.86, 0.87, 0.88, 0.90):
    row = []
    for q in qs:
        S4 = np.array([[1, q, r1, q * r1], [q, 1, q * r1, r1], [r1, q * r1, 1, q], [q * r1, r1, q, 1]], float)
        row.append(bc.analytic_atoms(S4, "MMI")[0]["sts"])
    print(f"   r1={r1:.2f}  " + "  ".join(f"{v:6.3f}" for v in row))
q0 = 0.20
f = lambda q: gp_params(acf_d, q)[0]["sts"] - gp_params(acf_p, q0)[0]["sts"]
print(f"   matching by q: sts difference over q in [0, 0.95] ranges {min(f(q) for q in np.linspace(0, 0.95, 40)):+.4f} .. {max(f(q) for q in np.linspace(0, 0.95, 40)):+.4f} -> "
      f"{'a matched pair exists' if min(f(q) for q in np.linspace(0, 0.95, 40)) < 0 < max(f(q) for q in np.linspace(0, 0.95, 40)) else 'NO matched pair: the true sts cannot be held fixed while r1 falls, at any cross-correlation'}")

# (b) identical 4-vector covariance (same r1, same q -> every analytic atom equal), different dependence beyond lag 1
# tilt the DMT-post PSD by exp(-beta w^2) (a valid, low-pass tilt) and solve beta so the
# realised lag-1 autocorrelation equals the placebo's; every lag beyond 1 then differs from the placebo ACF
w_grid = 2 * np.pi * np.arange(NFFT) / NFFT
def tilted(beta):
    p = psd_d * np.exp(-beta * np.minimum(w_grid, 2 * np.pi - w_grid) ** 2)
    a = np.real(np.fft.ifft(p))[:LMAX + 1]
    return p, a / a[0]
beta = brentq(lambda b: tilted(b)[1][1] - acf_p[1], 0.0, 50.0, xtol=1e-12)
psd_m, acf_m = tilted(beta)
print(f"\n=== F3-b identical S4 (r1 {acf_p[1]:.4f} vs {acf_m[1]:.4f}, q = {q0}), DMT-like higher-lag ACF: lags 2-6 placebo {np.round(acf_p[2:7], 3)} vs modified-DMT {np.round(acf_m[2:7], 3)}")
tb = gp_params(acf_p, q0)[0]; tm = gp_params(acf_m, q0)[0]
print(f"   analytic sts baseline {tb['sts']:.4f} vs shifted {tm['sts']:.4f} (difference {tm['sts'] - tb['sts']:+.5f}); xtx {tb['xtx']:.4f} vs {tm['xtx']:.4f}")
for W in WINDOWS:
    zb = simulate_gp(psd_p, q0, W, N_WIN); zs = simulate_gp(psd_m, q0, W, N_WIN)
    eb = np.array([np.mean(calc_PhiID(zb[i, 0], zb[i, 1], tau=1, kind="gaussian", redundancy="MMI")[0]["sts"]) for i in range(N_WIN)])
    es = np.array([np.mean(calc_PhiID(zs[i, 0], zs[i, 1], tau=1, kind="gaussian", redundancy="MMI")[0]["sts"]) for i in range(N_WIN)])
    d = es.mean() - eb.mean(); se = np.sqrt(eb.var(ddof=1) / N_WIN + es.var(ddof=1) / N_WIN)
    print(f"   W={W:3d}: est sts baseline {eb.mean():.4f}, shifted {es.mean():.4f}; manufactured difference {d:+.4f} ± {se:.4f} = {d / abs(REAL_DID) * 100:+.0f} % of the real |DiD|  ({time.time() - t0:.0f}s)")

# (c) reference: the actual DMT-post ACF at the same q (true sts differs) -> what the windowed estimator returns vs the truth
at_d = gp_params(acf_d, q0)[0]
print(f"\n=== F3-c reference, unmatched: placebo ACF vs DMT-post ACF at q = {q0}: analytic sts {tb['sts']:.4f} vs {at_d['sts']:.4f} (true difference {at_d['sts'] - tb['sts']:+.4f}; real windowed DiD {REAL_DID})")
for W in WINDOWS:
    zb = simulate_gp(psd_p, q0, W, N_WIN); zs = simulate_gp(psd_d, q0, W, N_WIN)
    eb = np.array([np.mean(calc_PhiID(zb[i, 0], zb[i, 1], tau=1, kind="gaussian", redundancy="MMI")[0]["sts"]) for i in range(N_WIN)])
    es = np.array([np.mean(calc_PhiID(zs[i, 0], zs[i, 1], tau=1, kind="gaussian", redundancy="MMI")[0]["sts"]) for i in range(N_WIN)])
    d = es.mean() - eb.mean(); se = np.sqrt(eb.var(ddof=1) / N_WIN + es.var(ddof=1) / N_WIN)
    print(f"   W={W:3d}: est sts baseline {eb.mean():.4f} (analytic {tb['sts']:.4f}), shifted {es.mean():.4f} (analytic {at_d['sts']:.4f}); estimated difference {d:+.4f} ± {se:.4f} vs true {at_d['sts'] - tb['sts']:+.4f}  ({time.time() - t0:.0f}s)")
print("done")
