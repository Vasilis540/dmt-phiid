"""b26_null_sections.py — the finite-sample null of notes/review_v2_residual_null.py replayed with the corrected code of
B26 (record, "The matrices that are not positive definite (B26): pre-run entry"): the same generator, draws and call
sequence as the null's own run, counting, in each evaluation whose residual the null's log prints, the AR(1)-substituted
matrices that are not positive definite, and printing the residual by B26's rule (1) (the observed mean over all pairs
minus the substituted mean over the pairs where it exists) beside the residual over the pairs where both exist. The
evaluations inside the cells' root searches, which use only the window-level a and |q|, are not counted here (the
wrappers of notes/partB26_positive_definite.py count every evaluation). No data.

Run from the repository root at the commit of B26's pre-run entry:
    .venv/bin/python notes/review_2026-09-28/checks/b26_null_sections.py
"""
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "notes"))
import review_v2_residual_null as N  # noqa: E402  (seeds its generator, 20261120, at import)

fits = {k: N.fit_filter(t) for k, t in N.TARGET_ACF.items()}


def report(label, obs, pred):
    ok = np.isfinite(pred)
    r_all = obs.mean() - np.nanmean(pred)
    r_m = (obs[ok] - pred[ok]).mean()
    print(f"{label}: {pred.size:,} substituted matrices, {int((~ok).sum())} not positive definite; residual by rule (1) "
          f"{r_all:+.6f} ({100 * r_all / obs.mean():+.4f} %); over the pairs where both exist {r_m:+.6f} "
          f"({100 * r_m / obs[ok].mean():+.4f} %)", flush=True)


for W in (30, 60, 840):
    betas = np.clip(N.rng.normal(200, 100, 2000), 5, None); q = np.clip(N.rng.normal(0, 0.27, 2000), -0.95, 0.95)
    X, Y = N.gen(2000, 8400, betas, fits["placebo"][2], fits["placebo"][3], q)
    obs, pred, a, aq = N.residual(N.window_corr(X, Y, W))
    report(f"homogeneous filter, W = {W}", obs, pred)
res = {}
for name, (ta, tq, acf) in N.CELLS.items():
    lo, hi = fits[acf][2], fits[acf][3]
    W, n_pairs, T, bsd = 60, 3000, 3000, 0.5

    def stats(bmean, qsd):
        betas = np.clip(N.rng.normal(bmean, bsd * bmean, n_pairs), 5, None); q = np.clip(N.rng.normal(0, qsd, n_pairs), -0.95, 0.95)
        X, Y = N.gen(n_pairs, T, betas, lo, hi, q)
        return N.residual(N.window_corr(X, Y, W))
    bmean = brentq(lambda b: stats(b, 0.27)[2].mean() - ta, 20, 800, xtol=3)
    qsd = brentq(lambda s: stats(bmean, s)[3].mean() - tq, 0.05, 0.9, xtol=0.005)
    obs, pred, a, aq = stats(bmean, qsd)
    report(f"cell {name} (W = 60)", obs, pred)
    res[name] = obs.mean() - np.nanmean(pred)
print(f"null residual DiD {(res['DMT post'] - res['DMT pre']) - (res['PCB post'] - res['PCB pre']):+.6f}")
