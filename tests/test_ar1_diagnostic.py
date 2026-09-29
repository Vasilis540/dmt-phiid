"""tools/ar1_diagnostic.py against phyid (the implementation the paper uses) and against
notes/rev_phiid_fast.py (the second implementation behind the paper's numbers). No data needed.
Each test draws from its own generator, so a test's data do not depend on which tests run before it."""
import numpy as np
import pytest

import rev_phiid_fast as rev
from phyid import calculate as phyid_calc
from phyid.utils import PhiID_atoms_abbr

from ar1_diagnostic import (ATOMS, atoms_from_corr, ar1_corr, closed_form, diagnose, diagnose_pairs,
                            diagnose_windows, lag_corr)

STS = ATOMS.index("sts")


def rng_for(k):
    return np.random.default_rng([20261120, k])


def ar1_pair(n, a_x, a_y, q, rng):
    """Two AR(1) series with lag-0 correlation q and no lagged interaction (innovation covariance
    chosen so that the stationary variances are 1 and the lag-0 correlation is q)."""
    cov = [[1 - a_x ** 2, q * (1 - a_x * a_y)], [q * (1 - a_x * a_y), 1 - a_y ** 2]]
    assert np.linalg.eigvalsh(cov).min() > 0, "(a_x, a_y, q) not realisable"
    e = rng.multivariate_normal([0, 0], cov, size=n + 200)
    x, y = np.zeros(n + 200), np.zeros(n + 200)
    for t in range(1, n + 200):
        x[t] = a_x * x[t - 1] + e[t, 0]
        y[t] = a_y * y[t - 1] + e[t, 1]
    return x[200:], y[200:]


def random_corr(rng):
    """A random 4 × 4 correlation matrix (positive definite)."""
    B = rng.normal(size=(4, 8))
    S = B @ B.T
    d = np.sqrt(np.diag(S))
    return S / np.outer(d, d)


def test_against_the_papers_second_implementation():
    rng = rng_for(1)
    Cs = np.stack([random_corr(rng) for _ in range(500)])
    assert rev.ATOMS == ATOMS
    assert np.max(np.abs(atoms_from_corr(Cs) - rev.atoms_from_corr(Cs))) < 1e-12
    assert np.allclose(ar1_corr(0.8, 0.9, 0.3), rev.ar1_corr(0.8, 0.9, 0.3)[0])
    # matrices that are not positive definite: NaN in both (the paper's code since its B26)
    M = rev.ar1_corr(np.array([0.96, 0.85]), np.array([0.75, 0.85]), np.array([0.87, 0.25]))
    assert np.isnan(rev.atoms_from_corr(M)[0]).all() and np.isnan(atoms_from_corr(M)[0]).all()
    assert np.max(np.abs(rev.atoms_from_corr(M)[1] - atoms_from_corr(M)[1])) < 1e-12


@pytest.mark.parametrize("n", [60, 840])
def test_against_phyid(n):
    rng = rng_for(2)
    assert tuple(PhiID_atoms_abbr) == ATOMS
    for a_x, a_y, q in ((0.85, 0.85, 0.25), (0.8, 0.9, -0.4), (0.6, 0.9, 0.3)):
        x, y = ar1_pair(n, a_x, a_y, q, rng)
        res, _ = phyid_calc.calc_PhiID(x, y, 1, kind="gaussian", redundancy="MMI")
        phyid_means = np.array([np.mean(res[k]) for k in ATOMS])
        assert np.max(np.abs(diagnose(x, y)["atoms"] - phyid_means)) < 1e-10


def test_substitution_matches_partB4():
    # notes/partB4_diagnostic.py computes the substituted sts per pair as
    # rev.atoms_from_corr(rev.ar1_corr(C[:, 0, 2], C[:, 1, 3], ½(C[:, 0, 1] + C[:, 2, 3])))[:, sts]
    rng = rng_for(3)
    X = np.stack(ar1_pair(300, 0.85, 0.8, 0.3, rng) + ar1_pair(300, 0.9, 0.7, -0.3, rng))
    pairs, d = diagnose_pairs(X)
    pp = rev.PairPhiID(X)
    ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]
    q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
    M = rev.ar1_corr(ax, ay, q)
    p = rev.atoms_from_corr(M)[:, STS]
    pd_ = np.linalg.eigvalsh(M).min(axis=1) > 0
    assert pairs == [tuple(t) for t in pp.pairs]
    assert np.max(np.abs(d["sts"] - pp.atoms_mean()[:, STS])) < 1e-12
    assert np.array_equal(np.isnan(d["sts_ar1"]), ~pd_) and np.array_equal(np.isnan(p), ~pd_)
    assert np.max(np.abs(d["sts_ar1"][pd_] - p[pd_])) < 1e-12
    # the placement of the substituted cross-lags: a_y q for (x_t, y_{t+1}), a_x q for (y_t, x_{t+1})
    x, y = X[0], X[1]
    C = lag_corr(x, y)
    qq = 0.5 * (C[0, 1] + C[2, 3])
    S = ar1_corr(C[0, 2], C[1, 3], qq)
    assert np.isclose(S[0, 3], C[1, 3] * qq) and np.isclose(S[1, 2], C[0, 2] * qq)


def test_nan_exactly_where_no_ar1_pair_exists():
    # (1 − a_x²)(1 − a_y²) > q²(1 − a_x a_y)² is the condition for the substituted matrix to be a correlation matrix
    rng = rng_for(4)
    a_x, a_y = rng.uniform(0.5, 0.99, 20000), rng.uniform(0.5, 0.99, 20000)
    q = rng.uniform(-0.99, 0.99, 20000)
    exists = (1 - a_x ** 2) * (1 - a_y ** 2) > q ** 2 * (1 - a_x * a_y) ** 2
    margin = np.abs((1 - a_x ** 2) * (1 - a_y ** 2) - q ** 2 * (1 - a_x * a_y) ** 2)
    keep = margin > 1e-9                                   # leave out draws within rounding of the boundary
    A = atoms_from_corr(ar1_corr(a_x, a_y, q))
    assert 0 < (~exists).sum() < exists.sum()
    assert np.array_equal(np.isnan(A[keep]).all(axis=1), ~exists[keep])
    assert np.isfinite(A[exists & keep]).all()


def test_shared_slow_signal_gives_nan():
    # a pair sharing one slow signal under unequal noise: a high q with unequal autocorrelations
    rng = rng_for(5)
    n = 840
    s = np.zeros(n + 500)
    for t in range(1, n + 500):
        s[t] = 0.98 * s[t - 1] + np.sqrt(1 - 0.98 ** 2) * rng.normal()
    x = s[500:] + np.sqrt(0.01) * rng.normal(size=n)       # population a_x 0.970, a_y 0.653, q 0.81: no AR(1) pair
    y = s[500:] + np.sqrt(0.50) * rng.normal(size=n)
    d = diagnose(x, y)
    assert np.isfinite(d["sts"]) and np.isnan(d["sts_ar1"]) and np.isnan(d["residual"])
    w = diagnose_windows(x, y, window=60)
    assert np.isfinite(w["sts"]).all()


def test_input_checks():
    rng = rng_for(6)
    x, y = rng.normal(size=6), rng.normal(size=6)
    diagnose(x, y)                                         # six samples: five lag pairs
    with pytest.raises(ValueError):
        diagnose(x[:5], y[:5])                             # four lag pairs: the 4 × 4 matrix is singular
    with pytest.raises(ValueError):
        diagnose(x, y, tau=0)
    with pytest.raises(ValueError):
        diagnose_windows(rng.normal(size=150), rng.normal(size=120), window=60)
    with pytest.raises(ValueError):
        diagnose_windows(rng.normal(size=150), rng.normal(size=150), window=5)
    with pytest.raises(ValueError):
        diagnose_pairs(rng.normal(size=(3, 5)))
    with pytest.raises(ValueError):
        diagnose_pairs(rng.normal(size=(3, 40)), tau=0)
    with pytest.raises(ValueError):
        diagnose_pairs(rng.normal(size=40))


def test_windows_and_pairs_agree_with_single_fits():
    rng = rng_for(7)
    X = np.stack(ar1_pair(840, 0.85, 0.85, 0.25, rng) + ar1_pair(840, 0.7, 0.9, -0.2, rng))
    w = diagnose_windows(X[0], X[1], window=60)
    assert w["sts"].shape == (14,)
    assert np.isclose(w["sts"][3], diagnose(X[0, 180:240], X[1, 180:240])["sts"])
    pairs, d = diagnose_pairs(X)
    k = pairs.index((1, 3))
    assert np.isclose(d["sts"][k], diagnose(X[1], X[3])["sts"])
    assert np.isclose(d["sts_ar1"][k], diagnose(X[1], X[3])["sts_ar1"])


def test_long_ar1_series_sit_on_the_closed_form():
    rng = rng_for(8)
    x, y = ar1_pair(200_000, 0.85, 0.85, 0.25, rng)
    d = diagnose(x, y)
    assert abs(d["sts"] - closed_form(0.85, 0.25)["sts"]) < 0.03
    assert abs(d["residual"]) < 0.01
