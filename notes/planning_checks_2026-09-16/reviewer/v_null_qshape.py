# Sensitivity of the null's sign-weighted run-level terms to the SHAPE of the q distribution at similar mean |q_hat|
# (the commission fixes q ~ N(0, sigma_q) in every configuration). Synthetic only; generator imported unmodified.
import sys, numpy as np
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/dmt-phiid/notes")
sys.path.insert(0, "/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify")
import review_v2_residual_null as N
from budget import budget, fmt
N.rng = np.random.default_rng(777); rng = N.rng
lo, hi, beta0 = 0.0064, 0.080, 200.0
shapes = {
    "q = 0 (all)": lambda n: np.zeros(n),
    "N(0, 0.22)": lambda n: rng.normal(0, 0.22, n),
    "N(0, 0.30)": lambda n: rng.normal(0, 0.30, n),
    "|q|=0.19 fixed, random sign": lambda n: 0.19 * rng.choice([-1, 1], n),
    "Laplace scale 0.18": lambda n: rng.laplace(0, 0.18, n),
    "mix 30% q=0, 70% N(0,0.30)": lambda n: np.where(rng.random(n) < 0.3, 0.0, rng.normal(0, 0.30, n)),
}
for name, draw in shapes.items():
    acc = {}
    for b in range(6):
        nb = 5000
        betas = np.clip(rng.normal(beta0, 0.5 * beta0, nb), 5, None); q = np.clip(draw(nb), -0.95, 0.95)
        X, Y = N.gen(nb, 840, betas, lo, hi, q)
        r = budget(X, Y, return_pairs=True)
        for k, v in r.items(): acc.setdefault(k, []).append(v)
    acc = {k: np.concatenate(v) for k, v in acc.items()}
    aq = acc["absq"]
    print(f"{name:30s} run {acc['run'].mean():+.5f} (SE {acc['run'].std()/np.sqrt(aq.size):.5f})  within {acc['within'].mean():+.5f}  d60 {acc['d60'].mean():+.5f}  "
          f"mean|q^| {aq.mean():.3f}  frac|q^|<.05 {np.mean(aq < .05):.3f}  <.10 {np.mean(aq < .10):.3f}  a {acc['a'].mean():.4f}")
