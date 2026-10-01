# Replays partB15_directed_crosslag.py's finite-sample null section (lines 146-224), no data, read-only;
# counts per configuration the substituted matrices not PD and the pairs left out of the responses.
import sys, time
sys.dont_write_bytecode = True
REPO = sys.argv[1] if len(sys.argv) > 1 else '.'  # the repository root; the audit ran it on a copy at d5a65bd
sys.path.insert(0, REPO + '/notes')
import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import brentq
from rev_phiid_fast import atoms_from_corr, ar1_corr, ATOMS
import review_v2_residual_null as NULL
S = ATOMS.index("sts"); SEED = 20261120
t0 = time.time()
def deviations(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]
    q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    d_xy = C[:, 0, 3] - ay * q
    d_yx = C[:, 1, 2] - ax * q
    return ax, ay, q, 0.5 * (d_xy + d_yx), 0.5 * (d_xy - d_yx)
def with_deviation(ax, ay, q, d_xy, d_yx):
    C = ar1_corr(ax, ay, q)
    C[:, 0, 3] = C[:, 3, 0] = ay * q + d_xy
    C[:, 1, 2] = C[:, 2, 1] = ax * q + d_yx
    return C
def response(ax, ay, q, sym, anti):
    base = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
    r_anti = atoms_from_corr(with_deviation(ax, ay, q, anti, -anti))[:, S] - base
    r_sym = atoms_from_corr(with_deviation(ax, ay, q, sym, sym))[:, S] - base
    r_both = atoms_from_corr(with_deviation(ax, ay, q, sym + anti, sym - anti))[:, S] - base
    return base, r_anti, r_sym, r_both
NULL.rng = np.random.default_rng(SEED)
fits = {k: NULL.fit_filter(t) for k, t in NULL.TARGET_ACF.items()}
lo_f, hi_f = fits["placebo"][2], fits["placebo"][3]
target_a, target_q = NULL.CELLS["DMT pre"][0], NULL.CELLS["DMT pre"][1]
n_pairs, T, W = 3000, 3000, 60
def stats_sym(bmean, qsd, r):
    betas = np.clip(r.normal(bmean, 0.5 * bmean, n_pairs), 5, None); q = np.clip(r.normal(0, qsd, n_pairs), -0.95, 0.95)
    X, Y = NULL.gen(n_pairs, T, betas, lo_f, hi_f, q)
    return X, Y, betas, q
NULL.rng = np.random.default_rng(SEED)
bmean = brentq(lambda b: NULL.residual(NULL.window_corr(*NULL.gen(n_pairs, T, np.clip(NULL.rng.normal(b, 0.5 * b, n_pairs), 5, None), lo_f, hi_f, np.clip(NULL.rng.normal(0, 0.27, n_pairs), -0.95, 0.95)), W))[2].mean() - target_a, 20, 800, xtol=3)
print('bmean', repr(bmean), f'({time.time()-t0:.0f}s)', flush=True)
qsd = brentq(lambda s: NULL.residual(NULL.window_corr(*NULL.gen(n_pairs, T, np.clip(NULL.rng.normal(bmean, 0.5 * bmean, n_pairs), 5, None), lo_f, hi_f, np.clip(NULL.rng.normal(0, s, n_pairs), -0.95, 0.95)), W))[3].mean() - target_q, 0.05, 0.9, xtol=0.005)
print('qsd', repr(qsd), f'({time.time()-t0:.0f}s)', flush=True)
def report(name, X, Y):
    C = NULL.window_corr(X, Y, W)
    obs, pred, a, aq = NULL.residual(C)
    ax, ay, q, sym, anti = deviations(C)
    base, r_anti, r_sym, r_both = response(ax, ay, q, sym, anti)
    ok = np.isfinite(r_anti) & np.isfinite(r_sym) & np.isfinite(r_both)
    res = np.mean(obs) - np.nanmean(pred)
    print(f"{name}: window a {a.mean():.4f}, |q| {aq.mean():.4f}; residual {res:+.5f} ({100 * res / obs.mean():+.2f} %); RMS δ_anti {np.sqrt(np.mean(anti ** 2)):.5f}, RMS δ_sym {np.sqrt(np.mean(sym ** 2)):.5f}; "
          f"closed-form response to δ_anti {r_anti[ok].mean():+.5f}, to δ_sym {r_sym[ok].mean():+.5f}, to both {r_both[ok].mean():+.5f}.")
    print(f"   COUNTS: pair-windows {C.shape[0]}; substituted not PD {int((~np.isfinite(pred)).sum())} (base {int((~np.isfinite(base)).sum())}); "
          f"anti NaN {int((~np.isfinite(r_anti)).sum())}, sym NaN {int((~np.isfinite(r_sym)).sum())}, both NaN {int((~np.isfinite(r_both)).sum())}; left out of the responses {int((~ok).sum())}  ({time.time()-t0:.0f}s)", flush=True)
    return res
X, Y, betas, q = stats_sym(bmean, qsd, NULL.rng)
res0 = report("(0) symmetric filter null, as review_v2_residual_null.py (solved bmean %.0f, qsd %.3f)" % (bmean, qsd), X, Y)
r1 = np.random.default_rng(SEED + 10)
betas1 = np.clip(r1.normal(bmean, 0.5 * bmean, n_pairs), 5, None); q1 = np.clip(r1.normal(0, qsd, n_pairs), -0.95, 0.95)
X1, N1 = NULL.gen(n_pairs, T + 1, betas1, lo_f, hi_f, np.zeros(n_pairs))
Xd = X1[:, 1:]; Xlag = X1[:, :-1]; N1 = N1[:, 1:]
sx = Xd.std(1, keepdims=True); Xd = Xd / sx; Xlag = Xlag / sx; N1 = N1 / N1.std(1, keepdims=True)
a1 = (Xd * Xlag).mean(1)
wmix = np.clip(q1 / a1, -0.99, 0.99)
Y1 = wmix[:, None] * Xlag + np.sqrt(1 - wmix[:, None] ** 2) * N1
res1 = report("(1) y = x delayed by one sample mixed with independent noise at the pair's q (w = q / r₁ of x, clipped to ±0.99)", Xd, Y1)
def var1_pair(a0, cc, qsd_v, seed):
    r = np.random.default_rng(seed)
    A = np.array([[a0, cc], [-cc, a0]])
    def lag0_corr(qe):
        G0 = solve_discrete_lyapunov(A, np.array([[1.0, qe], [qe, 1.0]]))
        return G0[0, 1] / np.sqrt(G0[0, 0] * G0[1, 1])
    lo_q, hi_q = lag0_corr(-0.999), lag0_corr(0.999)
    qs = np.clip(r.normal(0, qsd_v, n_pairs), lo_q + 1e-6, hi_q - 1e-6)
    qe = np.array([brentq(lambda e, qt=qt: lag0_corr(e) - qt, -0.999, 0.999) for qt in qs])
    burn = 300
    E1 = r.standard_normal((n_pairs, T + burn)); E2 = r.standard_normal((n_pairs, T + burn))
    E2 = qe[:, None] * E1 + np.sqrt(1 - qe[:, None] ** 2) * E2
    Xv = np.zeros((n_pairs, T + burn)); Yv = np.zeros((n_pairs, T + burn))
    for t in range(1, T + burn):
        Xv[:, t] = a0 * Xv[:, t - 1] + cc * Yv[:, t - 1] + E1[:, t]
        Yv[:, t] = a0 * Yv[:, t - 1] - cc * Xv[:, t - 1] + E2[:, t]
    return Xv[:, burn:], Yv[:, burn:], (lo_q, hi_q)
for k_c, cc in enumerate((0.02, 0.04, 0.06)):
    Xv, Yv, (lo_q, hi_q) = var1_pair(target_a, cc, qsd, SEED + 21 + k_c)
    report(f"(2) symmetric VAR(1), population a = {target_a}, c_xy = +{cc}, c_yx = −{cc}, q ~ N(0, {qsd:.3f}) clipped to the reachable lag-0 range {lo_q:+.3f} to {hi_q:+.3f} (window a and |q| as measured, see the note in the script)", Xv, Yv)
