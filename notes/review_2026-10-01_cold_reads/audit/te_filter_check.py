"""te_filter_check.py — evidence for finding C01 of findings_citations.md (audit of bundle 35B, the citations).

Question: is the pair of lag-1 Gaussian transfer entropies of the 4 x 4 matrix of (x_t, y_t, x_{t+1}, y_{t+1}),
I(y_t; x_{t+1} | x_t) and I(x_t; y_{t+1} | y_t), invariant under an invertible filter, as the main text's Results 7
says with Barnett & Seth (2011) and Seth et al. (2013)?

Method (population values, no data, no random numbers): a stable VAR(1), X_t = A X_{t-1} + e_t with cov(e) = S, has
autocovariances Gamma_0 = A Gamma_0 A' + S and Gamma_k = A^k Gamma_0. The same scalar FIR filter h(L) applied to both
series gives Gamma~_k = sum_i sum_j h_i h_j Gamma_{k-i+j}. The filter 1 + 0.6 L + 0.3 L^2 is invertible (its zeros have
modulus 1.83). The transfer entropies are Gaussian conditional mutual informations from the filtered covariances,
conditioning on one lag (the 4 x 4 matrix) or on p lags of the past. For each case the script also prints, before and
after the filter, the lag-0 correlation q, the two lag-1 autocorrelations and the two cross-lag correlations beside the
values r1(y) q and r1(x) q they take on the paper's AR(1) family (where the lag-1 pair is zero).

Usage: python3 te_filter_check.py     (NumPy and SciPy only)
"""
import numpy as np
from scipy.linalg import solve_discrete_lyapunov


def gammas(A, S, K):
    """Gamma_k = E[X_t X_{t-k}'] for k = -K..K of the VAR(1) with coefficient A and innovation covariance S."""
    g0 = solve_discrete_lyapunov(A, S)
    out = {0: g0}
    for k in range(1, K + 1):
        out[k] = np.linalg.matrix_power(A, k) @ g0
        out[-k] = out[k].T
    return out


def filtered(G, h, K):
    """Autocovariances of the series filtered by the scalar FIR h (same filter on both components)."""
    m = len(h)
    return {k: sum(h[i] * h[j] * G[k - i + j] for i in range(m) for j in range(m)) for k in range(-K, K + 1)}


def cmi(C, a, b, c):
    """Gaussian I(a; b | c) in nats from the covariance C (index lists)."""
    ld = lambda idx: np.linalg.slogdet(C[np.ix_(idx, idx)])[1] if idx else 0.0
    return 0.5 * (ld(a + c) + ld(b + c) - ld(c) - ld(a + b + c))


def te(G, p):
    """(TE y->x, TE x->y) conditioning on p lags: I(x_t; y_{t-1..t-p} | x_{t-1..t-p}) and its mirror."""
    n = 2 * (p + 1)
    C = np.zeros((n, n))
    for i in range(p + 1):
        for j in range(p + 1):
            C[2 * i:2 * i + 2, 2 * j:2 * j + 2] = G[j - i]      # E[X_{t-i} X_{t-j}'] = Gamma_{j-i}
    xp = [2 * i for i in range(1, p + 1)]
    yp = [2 * i + 1 for i in range(1, p + 1)]
    return cmi(C, [0], yp, xp), cmi(C, [1], xp, yp)


def crosslag(G):
    """q, r1 of x and y, and the two cross-lag correlations beside the family's values r1(y) q and r1(x) q."""
    g0, g1 = G[0], G[1]                                         # g1 = E[X_t X_{t-1}']
    sx, sy = np.sqrt(g0[0, 0]), np.sqrt(g0[1, 1])
    q, ax, ay = g0[0, 1] / (sx * sy), g1[0, 0] / g0[0, 0], g1[1, 1] / g0[1, 1]
    return q, ax, ay, g1[1, 0] / (sx * sy), ay * q, g1[0, 1] / (sx * sy), ax * q


h = [1.0, 0.6, 0.3]
print("zeros of the filter 1 + 0.6 z + 0.3 z^2, modulus:", np.round(np.abs(np.roots([0.3, 0.6, 1.0])), 3))
cases = [
    ("two AR(1), a = (0.90, 0.70), innovation correlation 0.3, no lagged coupling",
     np.diag([0.90, 0.70]), np.array([[1, 0.3], [0.3, 1]])),
    ("two AR(1), a = (0.85, 0.80), innovation correlation 0.25, no lagged coupling",
     np.diag([0.85, 0.80]), np.array([[1, 0.25], [0.25, 1]])),
    ("the symmetric family, a = (0.85, 0.85), innovation correlation 0.25",
     np.diag([0.85, 0.85]), np.array([[1, 0.25], [0.25, 1]])),
    ("VAR(1) with coupling, A = [[0.6, 0.3], [0, 0.6]], innovations uncorrelated",
     np.array([[0.6, 0.3], [0.0, 0.6]]), np.eye(2)),
]
for name, A, S in cases:
    G = gammas(A, S, 80)
    Gf = filtered(G, h, 60)
    print("\n" + name)
    for lab, g in (("unfiltered", G), ("filtered  ", Gf)):
        print("  %s: q %.4f, r1 %.4f and %.4f; corr(x_t, y_t+1) %.4f against r1(y) q %.4f; "
              "corr(y_t, x_t+1) %.4f against r1(x) q %.4f" % ((lab,) + crosslag(g)))
    print("  lag-1 TE (y->x, x->y), unfiltered: %.6f  %.6f" % te(G, 1))
    print("  lag-1 TE (y->x, x->y), filtered:   %.6f  %.6f" % te(Gf, 1))
    for p in (2, 5, 10, 30):
        print("  conditioning on %2d lags, unfiltered: %.6f  %.6f   filtered: %.6f  %.6f" % ((p,) + te(G, p) + te(Gf, p)))
