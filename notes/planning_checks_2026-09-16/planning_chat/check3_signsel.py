# (d) toy AR(1) (a = 0.86), zero population cross-lag deviation by construction (same coefficient, correlated innovations):
#     is the sign(q_hat)-weighted mean deviation zero? NOT the null's band-pass generator; no data.
import numpy as np
rng = np.random.default_rng(3)
a, T, W = 0.86, 840, 60

def c4(X, Y):
    P = np.stack([X[:, :-1], Y[:, :-1]], 1); F = np.stack([X[:, 1:], Y[:, 1:]], 1)
    P = (P - P.mean(2, keepdims=True))/P.std(2, ddof=1, keepdims=True); F = (F - F.mean(2, keepdims=True))/F.std(2, ddof=1, keepdims=True)
    Z = np.concatenate([P, F], 1); return np.einsum('nit,njt->nij', Z, Z)/(Z.shape[2]-1)

def dev(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5*(C[:, 0, 1] + C[:, 2, 3])
    return 0.5*((C[:, 0, 3] - ay*q) + (C[:, 1, 2] - ax*q)), q

for label, qdraw in (("q = 0 for every pair", lambda n: np.zeros(n)), ("q ~ N(0, 0.2)", lambda n: np.clip(rng.normal(0, 0.2, n), -0.9, 0.9)),
                     ("|q| = 0.25, random sign", lambda n: 0.25*rng.choice([-1, 1], n))):
    n = 40000; qt = qdraw(n)
    e1 = rng.standard_normal((n, T)); e2 = qt[:, None]*e1 + np.sqrt(1 - qt[:, None]**2)*rng.standard_normal((n, T))
    x = np.empty((n, T)); y = np.empty((n, T)); x[:, 0] = e1[:, 0]; y[:, 0] = e2[:, 0]
    for t in range(1, T):
        x[:, t] = a*x[:, t-1] + np.sqrt(1 - a*a)*e1[:, t]; y[:, t] = a*y[:, t-1] + np.sqrt(1 - a*a)*e2[:, t]
    d_run, q_run = dev(c4(x, y)); s = np.sign(q_run)
    dw = np.stack([dev(c4(x[:, w*W:(w+1)*W], y[:, w*W:(w+1)*W]))[0] for w in range(T//W)], 1)
    qw = np.stack([dev(c4(x[:, w*W:(w+1)*W], y[:, w*W:(w+1)*W]))[1] for w in range(T//W)], 1)
    se = lambda v: v.std()/np.sqrt(v.size)
    print(f"{label:26s}: run-level mean d {d_run.mean():+.5f}; sign(q_run)-weighted {np.mean(s*d_run):+.5f} (SE {se(s*d_run):.5f}); "
          f"W60 with run-level sign {np.mean(s[:, None]*dw):+.5f}; W60 with window sign {np.mean(np.sign(qw)*dw):+.5f}; "
          f"true sign weight {np.mean(np.sign(qt + 1e-12)*d_run):+.5f}; mean |q_run| {np.abs(q_run).mean():.3f}")
