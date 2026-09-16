# Is delta_means only "shared" slow variation? Add UNSHARED slow drift (independent per region) to a null-like pair. Synthetic only.
import sys, numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/dmt-phiid/notes")
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify")
import review_v2_residual_null as N
from budget import budget
rng = np.random.default_rng(2024); N.rng = rng
lo, hi = 0.0064, 0.080; n, T = 5000, 840
tt = np.linspace(-1, 1, T)[None, :]
for amp in (0.0, 0.3, 0.6):
    acc = {}
    for b in range(4):
        betas = np.clip(rng.normal(200, 100, n), 5, None); q = np.clip(rng.normal(0, 0.25, n), -0.95, 0.95)
        X, Y = N.gen(n, T, betas, lo, hi, q); X /= X.std(1, keepdims=True); Y /= Y.std(1, keepdims=True)
        # independent (unshared) slow drift: random linear trend + random quadratic, per region
        X = X + amp * (rng.standard_normal((n, 1)) * tt + rng.standard_normal((n, 1)) * (tt ** 2 - 1 / 3))
        Y = Y + amp * (rng.standard_normal((n, 1)) * tt + rng.standard_normal((n, 1)) * (tt ** 2 - 1 / 3))
        r = budget(X, Y, return_pairs=True)
        for k, v in r.items(): acc.setdefault(k, []).append(v)
    m = {k: np.concatenate(v).mean() for k, v in acc.items()}
    print(f"unshared drift amp {amp}: run {m['run']:+.5f} within {m['within']:+.5f} aq {m['aq']:+.5f} means {m['means']:+.5f} eps {m['eps']:+.5f} | a {m['a']:.4f} |q| {m['absq']:.3f}")
