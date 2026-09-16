# Does "simulate whole 840-TR runs" with the null's FFT generator (periodic at length T) change the run-level
# statistics relative to 840-TR segments cut from longer series? Synthetic only; imports the generator unmodified.
import sys, numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/dmt-phiid/notes")
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify")
import review_v2_residual_null as N
from budget import budget, fmt
N.rng = np.random.default_rng(12345)
rng = N.rng
fits = {k: N.fit_filter(t) for k, t in N.TARGET_ACF.items()}
print({k: (b[1], round(b[2], 4), round(b[3], 3)) for k, b in fits.items()})
_, beta0, lo, hi, _ = fits["placebo"]

def acc(gen_fn, nb, batches):
    res = {}
    for b in range(batches):
        X, Y = gen_fn(nb)
        r = budget(X, Y, return_pairs=True)
        for k, v in r.items(): res.setdefault(k, []).append(v)
    res = {k: np.concatenate(v) for k, v in res.items()}
    return {k: (v.mean(), v.std() / np.sqrt(v.size)) for k, v in res.items()}, res

def periodic(nb, bmean=beta0, qsd=0.25):
    betas = np.clip(rng.normal(bmean, 0.5 * bmean, nb), 5, None); q = np.clip(rng.normal(0, qsd, nb), -0.95, 0.95)
    return N.gen(nb, 840, betas, lo, hi, q)

def cut(nb, bmean=beta0, qsd=0.25, L=4200):
    betas = np.clip(rng.normal(bmean, 0.5 * bmean, nb), 5, None); q = np.clip(rng.normal(0, qsd, nb), -0.95, 0.95)
    X, Y = N.gen(nb, L, betas, lo, hi, q); o = rng.integers(0, L - 840)
    return X[:, o:o + 840].copy(), Y[:, o:o + 840].copy()

rp, pp = acc(periodic, 5000, 8)
print("periodic T=840 :", fmt(rp))
X, _ = periodic(3); print("  periodic: |sum over run| of one series", np.abs(X.sum(1)).max(), " window-mean sum", np.abs(X.reshape(3, 14, 60).mean(2).sum(1)).max())
rc, pc = acc(cut, 5000, 8)
print("cut from 4200  :", fmt(rc))
for k in ("run", "within", "aq", "means", "eps", "d60", "a", "absq"):
    print(f"  diff periodic - cut, {k}: {rp[k][0] - rc[k][0]:+.5f} (SE {np.hypot(rp[k][1], rc[k][1]):.5f})")
