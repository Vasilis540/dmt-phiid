"""
review_v2_residual_null.py — null for the B4 residual diagnostic (adversarial review of draft_v2, 15 Sep 2026).

Question: does the finite-sample scatter of the two cross-lag correlations about a_y q, at the data's own
operating points, produce the residual level (observed − AR(1)-predicted sts, −0.0489 at W = 60, ts_gsr)
and the residual DiD (+0.0115) that draft_v2 attributes to "the diagnostic's single model assumption"?

Null: each pair = one linear filter applied to two white noises with correlation q, so the population
cross-lag correlation is exactly r1·q (the AR(1) substitution is exact in population) and any residual is
finite-sample. The filter is a smooth 0.01–0.08 Hz band-pass with a low-frequency tilt exp(−β f²) fitted to
the pooled placebo ACF (lags 1–6: 0.868, 0.539, 0.172, −0.085, −0.174, −0.145; review item 5) and, for the
DMT-post cell, to the DMT-post ACF (0.858, 0.507, 0.123, −0.130, −0.194, −0.133). Per-pair heterogeneity:
β ~ N(β̄, 0.5 β̄) (window-level a SD ≈ 0.03, as in the data), q ~ N(0, σ_q). β̄ and σ_q are solved so that the
WINDOW-level mean pair a and mean pair |q| equal the values in notes/review_results/partB/residual_source.log:
DMT pre (0.8632, 0.2842), DMT post (0.8532, 0.2662), PCB pre (0.8603, 0.2839), PCB post (0.8657, 0.2824).
Residual per window exactly as partB4_diagnostic.py: sts(measured 4×4) − sts(ar1_corr(a_x, a_y, mean q)).
Run from the repository root: .venv/bin/python notes/review_v2_residual_null.py   (≈ 4 min)
"""
import sys, os, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS
from rev_git import SHA
from scipy.optimize import brentq
rng = np.random.default_rng(20261120)
TR = 2.0; STS = ATOMS.index("sts")
TARGET_ACF = {"placebo": [0.868, 0.539, 0.172, -0.085, -0.174, -0.145],
              "DMTpost": [0.858, 0.507, 0.123, -0.130, -0.194, -0.133]}
CELLS = {"DMT pre": (0.8632, 0.2842, "placebo"), "DMT post": (0.8532, 0.2662, "DMTpost"),
         "PCB pre": (0.8603, 0.2839, "placebo"), "PCB post": (0.8657, 0.2824, "placebo")}

def psd_weights(f, beta, lo, hi, edge=0.004):
    w = np.zeros_like(f)
    m = (f >= lo - edge) & (f <= lo + edge); w[m] = 0.5 * (1 - np.cos(np.pi * (f[m] - (lo - edge)) / (2 * edge)))
    w[(f > lo + edge) & (f < hi - edge)] = 1
    m = (f >= hi - edge) & (f <= hi + edge); w[m] = 0.5 * (1 + np.cos(np.pi * (f[m] - (hi - edge)) / (2 * edge)))
    return w[None, :] * np.exp(-np.atleast_1d(beta)[:, None] * f[None, :] ** 2)

def acf_of(beta, lo, hi, nfft=4096):
    f = np.fft.rfftfreq(nfft, d=TR); r = np.fft.irfft(psd_weights(f, beta, lo, hi)[0], n=nfft); return r[:7] / r[0]

def fit_filter(target):
    best = None
    for lo in np.linspace(0.003, 0.02, 6):
        for hi in np.linspace(0.07, 0.10, 4):
            for beta in np.linspace(0, 600, 31):
                r = acf_of(beta, lo, hi); err = np.sum((r[1:] - np.array(target)) ** 2)
                if best is None or err < best[0]: best = (err, beta, lo, hi, r)
    return best

def gen(n_pairs, T, betas, lo, hi, q):
    f = np.fft.rfftfreq(T, d=TR); H = np.sqrt(psd_weights(f, betas, lo, hi))
    e1 = rng.standard_normal((n_pairs, T)); e2 = rng.standard_normal((n_pairs, T))
    e2 = q[:, None] * e1 + np.sqrt(1 - q[:, None] ** 2) * e2
    return (np.fft.irfft(np.fft.rfft(e1, axis=1) * H, n=T, axis=1), np.fft.irfft(np.fft.rfft(e2, axis=1) * H, n=T, axis=1))

def window_corr(X, Y, W):
    """phyid-style 4×4 correlation of [x_t, y_t, x_t+1, y_t+1] per non-overlapping window (past/future blocks standardised separately)."""
    n_pairs, T = X.shape; Cs = []
    for w in range(T // W):
        xs = X[:, w * W:(w + 1) * W]; ys = Y[:, w * W:(w + 1) * W]
        P = np.stack([xs[:, :-1], ys[:, :-1]], 1); F = np.stack([xs[:, 1:], ys[:, 1:]], 1)
        P = (P - P.mean(2, keepdims=True)) / P.std(2, ddof=1, keepdims=True); F = (F - F.mean(2, keepdims=True)) / F.std(2, ddof=1, keepdims=True)
        Z = np.concatenate([P, F], 1); Cs.append(np.einsum('nit,njt->nij', Z, Z) / (W - 2))
    return np.concatenate(Cs, 0)

def residual(C):
    obs = atoms_from_corr(C)[:, STS]
    ax, ay, qm = C[:, 0, 2], C[:, 1, 3], 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    pred = atoms_from_corr(ar1_corr(ax, ay, qm))[:, STS]
    return obs, pred, 0.5 * (ax + ay), np.abs(qm)

def cell(target_a, target_q, lo, hi, W=60, n_pairs=3000, T=3000, bsd=0.5, label=""):
    def stats(bmean, qsd):
        betas = np.clip(rng.normal(bmean, bsd * bmean, n_pairs), 5, None); q = np.clip(rng.normal(0, qsd, n_pairs), -0.95, 0.95)
        X, Y = gen(n_pairs, T, betas, lo, hi, q); return residual(window_corr(X, Y, W))
    bmean = brentq(lambda b: stats(b, 0.27)[2].mean() - target_a, 20, 800, xtol=3)
    qsd = brentq(lambda s: stats(bmean, s)[3].mean() - target_q, 0.05, 0.9, xtol=0.005)
    obs, pred, a, aq = stats(bmean, qsd); res = obs - pred
    print(f"{label:9s}: window a={a.mean():.4f} (SD {a.std():.3f}) |q|={aq.mean():.4f}  obs sts={obs.mean():.4f}  AR(1) pred={pred.mean():.4f}  residual={res.mean():+.4f} ({100*res.mean()/obs.mean():+.1f} %)")
    return res.mean(), obs.mean()

if __name__ == "__main__":
    print(f"git={SHA}", flush=True)
    fits = {k: fit_filter(t) for k, t in TARGET_ACF.items()}
    for k, b in fits.items():
        print(f"filter fitted to the {k} ACF: beta={b[1]:.0f} lo={b[2]:.4f} hi={b[3]:.3f}; lags 1-6 {np.round(b[4][1:],3)} (target {TARGET_ACF[k]})")
    print("\n== residual level under the null, homogeneous filter (placebo ACF), by window length ==")
    for W in (30, 60, 840):
        betas = np.clip(rng.normal(200, 100, 2000), 5, None); q = np.clip(rng.normal(0, 0.27, 2000), -0.95, 0.95)
        X, Y = gen(2000, 8400, betas, fits["placebo"][2], fits["placebo"][3], q); obs, pred, a, aq = residual(window_corr(X, Y, W))
        print(f"W={W:3d}: a={a.mean():.3f} |q|={aq.mean():.3f} residual={(obs-pred).mean():+.4f} ({100*(obs-pred).mean()/obs.mean():+.2f} %)   [data: W30 -9.7 %, W60 -4.3 %, run-level -1.1 %]")
    print("\n== residual at the four operating points of residual_source.log (W = 60) ==")
    out = {}
    for name, (ta, tq, acf) in CELLS.items():
        out[name] = cell(ta, tq, fits[acf][2], fits[acf][3], label=name)
    dmt = out["DMT post"][0] - out["DMT pre"][0]; pcb = out["PCB post"][0] - out["PCB pre"][0]
    print(f"\nnull residual change: DMT {dmt:+.4f}, PCB {pcb:+.4f}, DiD {dmt-pcb:+.4f}")
    print( "data (residual_source.log): DMT +0.0077, PCB -0.0038, DiD +0.0115 [+0.0021, +0.0211]")
