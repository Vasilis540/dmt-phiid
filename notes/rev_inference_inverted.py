"""
rev_inference_inverted.py — the 95 % interval that goes with the paper's exact sign-flip test, obtained by inverting it.
Pre-run entry: manuscript/analysis_record.md, "Inverted sign-flip intervals, the residual against its calibrated
expectations, the per-subject regressions and the correlation intervals (B21): pre-run entry, 23 Sep 2026" (round 16).
Imported by notes/partB21_inference_revision.py and notes/partB22_aligned_directed.py. notes/rev_inference.py is not
changed: the outputs of the final run rest on it.

For a per-subject vector x (N = 14) and a candidate mean μ, p(μ) is the share of the 2^14 sign assignments s with
|Σ sᵢ(xᵢ − μ)| ≥ |Σ(xᵢ − μ)|, the comparison made with a relative tolerance of 1e-12; the interval is {μ : p(μ) > α}.
The assignments are enumerated in rev_inference's order (itertools.product((−1, 1), repeat=14)). With A_s = Σ sᵢxᵢ and
B_s = Σ sᵢ, the statistic of assignment s at μ is A_s − B_sμ, and the observed one is that of the all-plus assignment
(the last row), so the two all-equal assignments tie exactly. Every assignment's acceptance set is an interval that
contains the mean (the defining quadratic in μ is concave, since |B_s| < (1 − 1e-12)·N unless the signs are all equal),
so p cannot rise as μ moves away from the mean; the 2,001-point grid over [min x, max x] checks that numerically and
the number of grid violations is returned. On each side the bound is bracketed between the outermost grid point with
p > α and its outward neighbour and bisected until the bracket is shorter than 1e-7; the bracket's midpoint is
returned. Outside [min x, max x] every xᵢ − μ has one sign and p = 2/2^N, so the interval lies inside that range.
"""
from itertools import product

import numpy as np

_SIGNS = {}


def signflip_inversion(x, mu0=0.0, alpha=0.05, n_grid=2001, tol=1e-7, rel_tol=1e-12):
    """Exact sign-flip test of the mean against mu0 and the interval that inverts the test.

    Returns a dict: mean, n, n_neg (values < 0), p_mu0 (p at mu0), p_zero (p at 0), lo, hi (the bounds of
    {μ : p(μ) > alpha}, each to within tol/2), grid_violations (grid points at which p rises away from the mean), and
    pfun (p as a function of μ, for further evaluations)."""
    x = np.asarray(x, float)
    assert x.ndim == 1 and np.all(np.isfinite(x)), "a finite one-dimensional vector is required"
    n = x.size
    if n not in _SIGNS:
        _SIGNS[n] = np.array(list(product((-1, 1), repeat=n)), dtype=float)
    S = _SIGNS[n]
    A = S @ x                          # Σ sᵢ xᵢ per assignment
    B = S.sum(1)                       # Σ sᵢ per assignment
    a_obs, b_obs = A[-1], B[-1]        # the all-plus assignment: the observed statistic

    def pfun(mu):
        mu = np.atleast_1d(np.asarray(mu, float))
        out = np.empty(mu.size)
        for k0 in range(0, mu.size, 256):
            m = mu[k0:k0 + 256]
            t = np.abs(A[:, None] - B[:, None] * m[None, :])
            obs = np.abs(a_obs - b_obs * m) * (1.0 - rel_tol)
            out[k0:k0 + 256] = np.mean(t >= obs[None, :], axis=0)
        return out

    mean = float(x.mean())
    grid = np.linspace(x.min(), x.max(), n_grid)
    pg = pfun(grid)
    up = grid >= mean
    # p must be non-increasing as μ rises above the mean and non-decreasing as μ rises towards it from below
    viol = int(np.sum(np.diff(pg[up]) > 0) + np.sum(np.diff(pg[~up]) < 0))

    def bound(side):
        if side > 0:
            idx = np.where(up & (pg > alpha))[0]
            inner = grid[idx.max()] if idx.size else mean
            nxt = grid[idx.max() + 1] if idx.size and idx.max() + 1 < grid.size else x.max()
        else:
            idx = np.where(~up & (pg > alpha))[0]
            inner = grid[idx.min()] if idx.size else mean
            nxt = grid[idx.min() - 1] if idx.size and idx.min() - 1 >= 0 else x.min()
        a_in, a_out = inner, nxt                 # p(a_in) > alpha (or the mean), p(a_out) ≤ alpha
        while abs(a_out - a_in) >= tol:
            mid = 0.5 * (a_in + a_out)
            if pfun(mid)[0] > alpha:
                a_in = mid
            else:
                a_out = mid
        return 0.5 * (a_in + a_out)

    return dict(mean=mean, n=n, n_neg=int(np.sum(x < 0)), p_mu0=float(pfun(mu0)[0]), p_zero=float(pfun(0.0)[0]),
                lo=float(bound(-1)), hi=float(bound(+1)), grid_violations=viol, pfun=pfun)
