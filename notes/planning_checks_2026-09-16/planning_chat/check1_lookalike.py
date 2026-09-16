# (a) shared-component formula, population and simulated; (b) tau=1 equivalence with a symmetric VAR(1)
import numpy as np
rng = np.random.default_rng(1)

def ar1(n, T, a):
    e = rng.standard_normal((n, T)); x = np.empty((n, T)); x[:, 0] = e[:, 0]
    for t in range(1, T): x[:, t] = a * x[:, t-1] + np.sqrt(1 - a*a) * e[:, t]
    return x

lam, a_s, a_n = 0.25, 0.95, 0.80
a = lam*a_s + (1-lam)*a_n; q = lam; cross = lam*a_s
d_pop = cross - a*q
print(f"population: a={a:.4f} q={q:.4f} cross-lag={cross:.5f} a*q={a*q:.5f} d={d_pop:.6f} formula={lam*(1-lam)*(a_s-a_n):.6f}")

# simulate, both signs of loading
n, T = 4000, 3000
s = ar1(n, T, a_s); nx = ar1(n, T, a_n); ny = ar1(n, T, a_n)
for sign in (+1, -1):
    x = np.sqrt(lam)*s + np.sqrt(1-lam)*nx
    y = sign*np.sqrt(lam)*s + np.sqrt(1-lam)*ny
    P = np.stack([x[:, :-1], y[:, :-1]], 1); F = np.stack([x[:, 1:], y[:, 1:]], 1)
    P = (P - P.mean(2, keepdims=True))/P.std(2, ddof=1, keepdims=True); F = (F - F.mean(2, keepdims=True))/F.std(2, ddof=1, keepdims=True)
    Z = np.concatenate([P, F], 1); C = np.einsum('nit,njt->nij', Z, Z)/(T-2)
    ax, ay = C[:, 0, 2], C[:, 1, 3]; qq = 0.5*(C[:, 0, 1] + C[:, 2, 3])
    d = 0.5*((C[:, 0, 3] - ay*qq) + (C[:, 1, 2] - ax*qq))
    print(f"sim sign {sign:+d}: mean q={qq.mean():+.4f} mean d={d.mean():+.5f} (expected {sign*d_pop:+.5f}); mean sign(q)*d={np.mean(np.sign(qq)*d):+.5f}")

# unequal loadings: directional formula q(1-lam_y)(a_s - a_n)
lx, ly = 0.4, 0.1
qx = np.sqrt(lx*ly); ay_ = ly*a_s + (1-ly)*a_n
print(f"unequal: d(x->y) pop={qx*a_s - ay_*qx:.6f} formula={qx*(1-ly)*(a_s-a_n):.6f}")

# (b) tau=1 equivalence: A = G1 G0^-1, innovation covariance PSD
G0 = np.array([[1, q], [q, 1]]); G1 = np.array([[a, cross], [cross, a]])   # G1[i,j] = cov(z_{t+1,i}, z_{t,j})
A = G1 @ np.linalg.inv(G0); Se = G0 - A @ G0 @ A.T
print("A =", np.round(A, 6).tolist(), " eig(Sigma_e) =", np.round(np.linalg.eigvalsh(Se), 5).tolist())
c = A[0, 1]; print(f"c={c:.6f}  c(1-q^2)={c*(1-q*q):.6f}  d={d_pop:.6f}")
# check the VAR(1) with A, Se reproduces G1 and G0 (stationary covariance solves G0 = A G0 A' + Se)
G0v = np.linalg.solve(np.eye(4) - np.kron(A, A), Se.ravel()).reshape(2, 2)
print("VAR(1) stationary G0 =", np.round(G0v, 6).tolist(), " G1 =", np.round(A @ G0v, 6).tolist())
