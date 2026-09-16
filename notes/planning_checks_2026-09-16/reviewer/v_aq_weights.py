# delta_aq with q CONSTANT across windows (no a-q covariance), each region's a co-varying with its own window variance,
# independent x and y profiles. Population d_w = 0 in every window. Synthetic only.
import sys, numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify")
from budget import budget
rng = np.random.default_rng(5)
W, NW, n = 60, 14, 20000; T = W * NW
for kappa in (0.0, 0.3, 0.5):
    X = np.empty((n, T)); Y = np.empty((n, T))
    sgn = rng.choice([-1, 1], n); q = 0.25
    for w in range(NW):
        zx, zy = rng.standard_normal(n), rng.standard_normal(n)
        ax = np.clip(0.80 + 0.06 * zx, 0.6, 0.93); ay = np.clip(0.80 + 0.06 * zy, 0.6, 0.93)
        rho = np.clip(q * (1 - ax * ay) / np.sqrt((1 - ax ** 2) * (1 - ay ** 2)), -0.999, 0.999)
        e1 = rng.standard_normal((n, W)); e2 = rho[:, None] * e1 + np.sqrt(1 - rho[:, None] ** 2) * rng.standard_normal((n, W))
        x = np.empty((n, W)); y = np.empty((n, W))
        x[:, 0] = e1[:, 0]; y[:, 0] = e2[:, 0]          # stationary start: var 1, corr = q exactly
        y[:, 0] = q * e1[:, 0] + np.sqrt(1 - q * q) * rng.standard_normal(n)
        for t in range(1, W):
            x[:, t] = ax * x[:, t - 1] + np.sqrt(1 - ax ** 2) * e1[:, t]; y[:, t] = ay * y[:, t - 1] + np.sqrt(1 - ay ** 2) * e2[:, t]
        X[:, w * W:(w + 1) * W] = np.exp(kappa * zx)[:, None] * x
        Y[:, w * W:(w + 1) * W] = sgn[:, None] * np.exp(kappa * zy)[:, None] * y
    r = budget(X, Y, return_pairs=True); m = {k: v.mean() for k, v in r.items()}; se = {k: v.std() / np.sqrt(n) for k, v in r.items()}
    print(f"kappa {kappa}: run {m['run']:+.5f} wd {m['wd']:+.5f} within {m['within']:+.5f} aq {m['aq']:+.5f} (SE {se['aq']:.5f}) "
          f"[cov part {m['aq_cov']:+.5f}, weight-mismatch part {m['aq_wt']:+.5f}] means {m['means']:+.5f} eps {m['eps']:+.6f}  mean sum(pi) {m['sumpi']:.4f}")
