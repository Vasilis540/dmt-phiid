"""The closed form of Results 1 and the numbers the paper quotes from it, checked against the
lattice solve of tools/ar1_diagnostic.py. No data needed."""
import numpy as np
import pytest

from ar1_diagnostic import ATOMS, atoms_from_corr, ar1_corr, closed_form, exchange_rates

GRID = [(a, q) for a in (0.1, 0.3, 0.6, 0.8, 0.85, 0.9, 0.95, 0.99) for q in (-0.7, -0.25, 0.0, 0.25, 0.5, 0.7)]
IDX = {k: i for i, k in enumerate(ATOMS)}


def S_C(a, q):
    return -0.5 * np.log(1 - a * a), -0.5 * np.log(1 - a * a * q * q)


@pytest.mark.parametrize("a,q", GRID)
def test_atoms_equal_the_closed_form(a, q):
    solved = atoms_from_corr(ar1_corr(a, a, q))
    cf = closed_form(a, q)
    assert np.allclose(solved, [cf[k] for k in ATOMS], atol=1e-12, rtol=0)


@pytest.mark.parametrize("a,q", GRID)
def test_identities(a, q):
    A = atoms_from_corr(ar1_corr(a, a, q))
    S, C = S_C(a, q)
    g = lambda k: A[IDX[k]]
    assert abs(g("sts") - (g("xtx") + g("yty")) - g("rtr")) < 1e-12        # sts − (xtx + yty) = rtr
    assert abs(g("rtr") + g("sts") - 2 * S) < 1e-12                      # rtr + sts = TDMI = 2S
    assert abs(A.sum() - 2 * S) < 1e-12                                  # TDMI depends on r1 alone
    assert abs(g("str") + g("stx") + g("sty") + g("sts") - S) < 1e-12    # the four-atom synergy = S
    for k in ("xts", "yts", "stx", "sty"):                                # the four mirror atoms
        assert g(k) <= 1e-15
    phi_r = A.sum() - (g("rtr") + g("rtx") + g("xtr") + g("xtx")) - (g("rtr") + g("rty") + g("ytr") + g("yty")) + g("rtr")
    assert abs(phi_r - g("rtr")) < 1e-12                                  # ΦR = rtr on the family


def test_operating_point_numbers():
    cf = closed_form(0.85, 0.25)
    assert round(cf["sts"], 4) == 1.2588                                 # Fig 1 caption, c = 0
    r = exchange_rates(0.85, 0.25)
    assert round(r["dsts_dr1"], 2) == 6.07                               # Results 1
    assert round(r["dsts_dq"], 2) == -0.19
    # finite differences of the lattice solve agree with the analytic rates
    h = 1e-6
    f = lambda a, q: atoms_from_corr(ar1_corr(a, a, q))[IDX["sts"]]
    assert abs((f(0.85 + h, 0.25) - f(0.85 - h, 0.25)) / (2 * h) - r["dsts_dr1"]) < 1e-5
    assert abs((f(0.85, 0.25 + h) - f(0.85, 0.25 - h)) / (2 * h) - r["dsts_dq"]) < 1e-5


def test_unequal_coefficients():
    # q = 0: sts = 2 min(S_x, S_y) and rtr = 0 (Results 1)
    for ax, ay in ((0.8, 0.9), (0.85, 0.86), (0.6, 0.95)):
        A = atoms_from_corr(ar1_corr(ax, ay, 0.0))
        Sx, Sy = -0.5 * np.log(1 - ax * ax), -0.5 * np.log(1 - ay * ay)
        assert abs(A[IDX["sts"]] - 2 * min(Sx, Sy)) < 1e-12
        assert abs(A[IDX["rtr"]]) < 1e-12
    # at (0.85, 0.25) the excess sts − (xtx + yty) changes sign at an asymmetry of about 0.008
    # (S18 Table's first negative value on its 0.0005 grid is at 0.0080; the crossing is at 0.0076)
    excess = lambda d: (lambda A: A[IDX["sts"]] - A[IDX["xtx"]] - A[IDX["yty"]])(atoms_from_corr(ar1_corr(0.85 + d / 2, 0.85 - d / 2, 0.25)))
    assert excess(0.0075) > 0 > excess(0.008)
    # 0.01 of within-pair asymmetry moves sts by 0.031 (rate at zero asymmetry, mean held at 0.85)
    sts = lambda d: atoms_from_corr(ar1_corr(0.85 + d / 2, 0.85 - d / 2, 0.25))[IDX["sts"]]
    assert round(0.01 * (sts(0.0) - sts(1e-6)) / 1e-6, 3) == 0.031
