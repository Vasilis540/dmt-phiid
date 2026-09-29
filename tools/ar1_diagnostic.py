"""
ar1_diagnostic.py — the check the paper recommends, for any pair of time series.

The Gaussian-MMI synergy atom sts of integrated information decomposition (ΦID) depends
mostly on the lag-1 autocorrelation of the two series (Results 1 of the paper). This module
lets a user put that check beside their own synergy values:

    diagnose(x, y)            one window: the sixteen atoms, the pair's lag-1 autocorrelations
                              a_x, a_y, its lag-0 correlation q, and the AR(1)-substituted sts
    diagnose_windows(x, y)    the same in non-overlapping windows fitted separately (the paper's
                              W = 60 estimator uses 60-sample windows)
    diagnose_pairs(X)         every region pair of a (regions × samples) array at once
    closed_form(a, q)         the sixteen atoms of two AR(1) processes with equal coefficients and
                              no lagged interaction, whose innovations are correlated at lag 0
    exchange_rates(a, q)      ∂sts/∂r₁ and ∂sts/∂q on that family

The estimator is the one phyid computes with calc_PhiID(kind="gaussian", redundancy="MMI"):
a Gaussian fitted to [x_t, y_t, x_{t+τ}, y_{t+τ}], plug-in mutual informations (nats), MMI
redundancies (the smaller mutual information; the double redundancy the smallest of the four
single-source, single-target ones) and the Möbius inversion of the ΦID lattice. Its window
means are a function of the 4 × 4 lag correlation matrix alone, which is what this module
evaluates; tests/test_ar1_diagnostic.py checks it against phyid and against the code behind
the paper's numbers (notes/rev_phiid_fast.py).

The AR(1)-substituted estimate keeps the pair's two lag-1 autocorrelations a_x and a_y, sets
its two lag-0 entries to their mean q and replaces its two cross-lag correlations
corr(x_t, y_{t+τ}) and corr(y_t, x_{t+τ}) by a_y q and a_x q: the sts the pair would have if
its lagged structure were that of two AR(1) processes with its measured autocorrelations and
lag-0 correlation. Read the paper before interpreting the residual (observed minus substituted):
it has a non-zero expectation even under a pure change of autocorrelation (Results 4), so it is
not by itself a measure of lagged interaction.

The substituted matrix is a correlation matrix only if |q| < 1 and
(1 − a_x²)(1 − a_y²) > q²(1 − a_x a_y)². Otherwise no pair of AR(1) processes has the measured
a_x, a_y and q (a high |q| with unequal autocorrelations can do it, e.g. two regions sharing a
slow signal under different noise), the estimate does not exist, and sts_ar1, residual and
atoms_ar1 are NaN: average with np.nanmean and report the share of such windows or pairs.
(notes/rev_phiid_fast.py, the code behind the paper's numbers, does the same since the paper's
B26; before it took the logarithm of |det| and returned a value there.)

Inputs must be finite and not constant: a NaN or a constant series gives NaN atoms. The
paper's estimator drops non-finite samples before forming windows
(scripts/01_synergy_timecourse.py), so drop or impute them first.

Units: nats. Requires numpy only.

Example
-------
>>> import numpy as np
>>> from ar1_diagnostic import diagnose, closed_form, atoms_from_corr, ar1_corr
>>> rng = np.random.default_rng(20261120)
>>> # two AR(1) processes with a = 0.85 and no lagged interaction, innovations correlated at lag 0 (q = 0.25)
>>> n, a, q = 200_000, 0.85, 0.25
>>> e = rng.multivariate_normal([0, 0], [[1, q], [q, 1]], size=n)
>>> x, y = np.zeros(n), np.zeros(n)
>>> for t in range(1, n):
...     x[t] = a * x[t - 1] + e[t, 0]; y[t] = a * y[t - 1] + e[t, 1]
>>> d = diagnose(x, y)
>>> round(closed_form(0.85, 0.25)["sts"], 4)
1.2588
>>> abs(d["sts"] - 1.2588) < 0.03, abs(d["residual"]) < 0.01
(True, True)
>>> # no pair of AR(1) processes has a_x = 0.96, a_y = 0.75 and q = 0.87: no substituted atoms
>>> bool(np.isnan(atoms_from_corr(ar1_corr(0.96, 0.75, 0.87))).all())
True
"""
import numpy as np

__all__ = ["ATOMS", "lag_corr", "atoms_from_corr", "ar1_corr", "closed_form", "exchange_rates",
           "diagnose", "diagnose_windows", "diagnose_pairs"]

# atom order as phyid.utils.PhiID_atoms_abbr: first letter the past-side type, last letter the
# future-side type (r redundant, x unique to X, y unique to Y, s synergistic)
ATOMS = ("rtr", "rtx", "rty", "rts", "xtr", "xtx", "xty", "xts",
         "ytr", "ytx", "yty", "yts", "str", "stx", "sty", "sts")

# variable order inside the four-vector: 0 = x_t, 1 = y_t, 2 = x_{t+τ}, 3 = y_{t+τ}
_MI = {  # the nine mutual informations the lattice needs: (A, B)
    "xta": ((0,), (2,)), "xtb": ((0,), (3,)), "yta": ((1,), (2,)), "ytb": ((1,), (3,)),
    "xyta": ((0, 1), (2,)), "xytb": ((0, 1), (3,)), "xtab": ((0,), (2, 3)), "ytab": ((1,), (2, 3)),
    "xytab": ((0, 1), (2, 3)),
}
# rows: the sixteen knowns (double redundancy, six single-target redundancies, nine mutual
# informations); columns: the atoms in ATOMS order; entry 1 if the atom lies below the known
_KNOWNS = ("rtr", "R_xyta", "R_xytb", "R_xytab", "R_abtx", "R_abty", "R_abtxy",
           "xta", "xtb", "yta", "ytb", "xyta", "xytb", "xtab", "ytab", "xytab")
_LATTICE = np.array([
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
], float)
_SOLVE = np.linalg.inv(_LATTICE).T  # atoms = knowns @ _SOLVE


def lag_corr(x, y, tau=1):
    """The 4 × 4 Pearson correlation matrix of [x_t, y_t, x_{t+τ}, y_{t+τ}] over the sample,
    the matrix phyid's Gaussian fit uses (its standardisation and np.cov give the correlation)."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.shape != y.shape or x.ndim != 1:
        raise ValueError("x and y must be 1-D arrays of the same length")
    if not (tau >= 1 and x.size - tau >= 5):
        raise ValueError("tau must be at least 1 and leave at least five lag pairs (a 4 × 4 correlation needs five)")
    return np.corrcoef(np.vstack([x[:-tau], y[:-tau], x[tau:], y[tau:]]))


def _positive_definite(C):
    """(n,) True where the (n, 4, 4) matrix is finite and positive definite (smallest eigenvalue > 0)."""
    ok = np.isfinite(C).all(axis=(1, 2))
    if ok.any():
        ok[ok] = np.linalg.eigvalsh(C[ok]).min(axis=1) > 0
    return ok


def _mutual_informations(C):
    """Plug-in Gaussian mutual informations (nats) of (n, 4, 4) positive-definite correlation matrices."""
    cache = {}
    def ld(idx):
        key = tuple(sorted(idx))
        if key not in cache:
            k = np.array(key)
            cache[key] = np.linalg.slogdet(C[:, k[:, None], k[None, :]])[1]
        return cache[key]
    return {k: 0.5 * (ld(A) + ld(B) - ld(A + B)) for k, (A, B) in _MI.items()}


def atoms_from_corr(C):
    """The sixteen Gaussian-MMI ΦID atoms (nats) of lag correlation matrices.

    C: a 4 × 4 matrix or an (n, 4, 4) stack, variables ordered [x_t, y_t, x_{t+τ}, y_{t+τ}].
    Returns an array of shape (16,) or (n, 16) in the order of ATOMS. For a sample's correlation
    matrix these are phyid's window means; for a process's lag covariance they are its atoms.
    A matrix that is not finite and positive definite is the lag covariance of no process and
    has no atoms: its row is NaN.
    """
    C = np.asarray(C, float)
    single = C.ndim == 2
    if single:
        C = C[None]
    if C.ndim != 3 or C.shape[1:] != (4, 4):
        raise ValueError("C must be a 4 × 4 matrix or an (n, 4, 4) stack")
    ok = _positive_definite(C)
    mi = _mutual_informations(np.where(ok[:, None, None], C, np.eye(4)))   # placeholders where there are no atoms
    def smaller(a, b):  # phyid's redundancy_mmi: a if mean(a) < mean(b) else b
        return np.where(mi[a] < mi[b], mi[a], mi[b])
    four = np.stack([mi["xta"], mi["xtb"], mi["yta"], mi["ytb"]], 1)
    knowns = {
        "rtr": four[np.arange(four.shape[0]), np.argmin(four, 1)],  # first minimum, as phyid
        "R_xyta": smaller("xta", "yta"), "R_xytb": smaller("xtb", "ytb"), "R_xytab": smaller("xtab", "ytab"),
        "R_abtx": smaller("xta", "xtb"), "R_abty": smaller("yta", "ytb"), "R_abtxy": smaller("xyta", "xytb"),
    }
    knowns.update(mi)
    K = np.stack([knowns[k] for k in _KNOWNS], 1)
    A = K @ _SOLVE
    A[~ok] = np.nan
    return A[0] if single else A


def ar1_corr(a_x, a_y, q):
    """Lag-1 correlation matrix of two AR(1) processes with coefficients a_x, a_y whose lag-0
    correlation is q and which have no lagged interaction:
    [[1, q, a_x, a_y q], [q, 1, a_x q, a_y], [a_x, a_x q, 1, q], [a_y q, a_y, q, 1]].
    Scalars give a 4 × 4 matrix; arrays broadcast to an (n, 4, 4) stack. It is a correlation
    matrix only if |q| < 1 and (1 − a_x²)(1 − a_y²) > q²(1 − a_x a_y)²; otherwise no pair of
    AR(1) processes has these a_x, a_y and q, and atoms_from_corr returns NaN for it."""
    a_x, a_y, q = np.broadcast_arrays(np.asarray(a_x, float), np.asarray(a_y, float), np.asarray(q, float))
    scalar = a_x.ndim == 0
    a_x, a_y, q = a_x.ravel(), a_y.ravel(), q.ravel()
    C = np.empty((a_x.size, 4, 4))
    C[:, 0] = np.stack([np.ones_like(q), q, a_x, a_y * q], 1)
    C[:, 1] = np.stack([q, np.ones_like(q), a_x * q, a_y], 1)
    C[:, 2] = np.stack([a_x, a_x * q, np.ones_like(q), q], 1)
    C[:, 3] = np.stack([a_y * q, a_y, q, np.ones_like(q)], 1)
    return C[0] if scalar else C


def closed_form(a, q):
    """The sixteen atoms of two AR(1) processes with equal coefficient a (= r₁), no lagged
    interaction and lag-0 correlation q (Results 1): with S = −½ ln(1 − a²) and
    C = −½ ln(1 − a²q²), rtr = C, xtx = yty = rts = str = S − C, xts = yts = stx = sty = −(S − C),
    sts = 2S − C, and the six cross-prediction atoms 0."""
    a, q = float(a), float(q)
    if not (abs(a) < 1 and abs(q) < 1):
        raise ValueError("need |a| < 1 and |q| < 1")
    S = float(-0.5 * np.log(1 - a * a))
    C = float(-0.5 * np.log(1 - a * a * q * q))
    out = dict.fromkeys(ATOMS, 0.0)
    out.update(rtr=C, xtx=S - C, yty=S - C, rts=S - C, str=S - C,
               xts=-(S - C), yts=-(S - C), stx=-(S - C), sty=-(S - C), sts=2 * S - C)
    return out


def exchange_rates(a, q):
    """∂sts/∂r₁ and ∂sts/∂q on the equal-coefficient family at (a, q), in nats per unit."""
    a, q = float(a), float(q)
    d_a = 2 * a / (1 - a * a) - a * q * q / (1 - a * a * q * q)
    d_q = -a * a * q / (1 - a * a * q * q)
    return {"dsts_dr1": d_a, "dsts_dq": d_q}


def _summary(C, obs, sub):
    i = ATOMS.index("sts")
    a_x, a_y = C[..., 0, 2], C[..., 1, 3]
    q = 0.5 * (C[..., 0, 1] + C[..., 2, 3])
    return {"a_x": a_x, "a_y": a_y, "r1": 0.5 * (a_x + a_y), "q": q,
            "sts": obs[..., i], "sts_ar1": sub[..., i], "residual": obs[..., i] - sub[..., i],
            "atoms": obs, "atoms_ar1": sub}


def diagnose(x, y, tau=1):
    """One fit over the whole sample of x and y (1-D, same length, at least tau + 5 samples).

    Returns a dict: a_x, a_y (lag-τ autocorrelations), r1 (their mean), q (lag-0 correlation, the
    mean of the matrix's two lag-0 entries), sts (observed), sts_ar1 (AR(1)-substituted), residual
    (sts − sts_ar1), atoms and atoms_ar1 (arrays of 16 in ATOMS order). Scalars are floats.
    sts_ar1, residual and atoms_ar1 are NaN where the measured a_x, a_y and q are those of no
    AR(1) pair (see the module's docstring)."""
    C = lag_corr(x, y, tau)
    a_x, a_y = C[0, 2], C[1, 3]
    q = 0.5 * (C[0, 1] + C[2, 3])
    obs = atoms_from_corr(C)
    sub = atoms_from_corr(ar1_corr(a_x, a_y, q))
    out = _summary(C, obs, sub)
    return {k: (float(v) if np.ndim(v) == 0 else v) for k, v in out.items()}


def diagnose_windows(x, y, window=60, tau=1):
    """diagnose() in non-overlapping windows of `window` samples, each fitted separately (lag pairs
    inside the window only); a trailing incomplete window is dropped. Returns a dict of arrays
    with one entry per window (atoms: (n_windows, 16)); NaN entries as in diagnose()."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)
    if x.shape != y.shape or x.ndim != 1:
        raise ValueError("x and y must be 1-D arrays of the same length")
    if int(window) != window or window < tau + 5:
        raise ValueError("window must be a whole number of samples, at least tau + 5")
    window = int(window)
    n = x.size // window
    if n < 1:
        raise ValueError("series shorter than one window")
    Cs = np.stack([lag_corr(x[w * window:(w + 1) * window], y[w * window:(w + 1) * window], tau) for w in range(n)])
    a_x, a_y = Cs[:, 0, 2], Cs[:, 1, 3]
    q = 0.5 * (Cs[:, 0, 1] + Cs[:, 2, 3])
    return _summary(Cs, atoms_from_corr(Cs), atoms_from_corr(ar1_corr(a_x, a_y, q)))


def diagnose_pairs(X, tau=1):
    """Every pair (i < j) of the rows of X (regions × samples), one fit per pair over all samples.
    Returns (pairs, dict of arrays with one entry per pair); NaN entries as in diagnose(). For
    windows, call it on each window."""
    X = np.asarray(X, float)
    if X.ndim != 2 or X.shape[0] < 2 or not (tau >= 1 and X.shape[1] - tau >= 5):
        raise ValueError("X must be (regions × samples) with at least two regions and tau + 5 samples, tau at least 1")
    R, T = X.shape
    P = X[:, :-tau]
    F = X[:, tau:]
    P = (P - P.mean(1, keepdims=True)) / P.std(1, ddof=1, keepdims=True)
    F = (F - F.mean(1, keepdims=True)) / F.std(1, ddof=1, keepdims=True)
    n = P.shape[1]
    pp, ff, pf = P @ P.T / (n - 1), F @ F.T / (n - 1), P @ F.T / (n - 1)
    I, J = np.triu_indices(R, 1)
    C = np.empty((I.size, 4, 4))
    C[:, 0] = np.stack([pp[I, I], pp[I, J], pf[I, I], pf[I, J]], 1)
    C[:, 1] = np.stack([pp[J, I], pp[J, J], pf[J, I], pf[J, J]], 1)
    C[:, 2] = np.stack([pf[I, I], pf[J, I], ff[I, I], ff[I, J]], 1)
    C[:, 3] = np.stack([pf[I, J], pf[J, J], ff[J, I], ff[J, J]], 1)
    a_x, a_y = C[:, 0, 2], C[:, 1, 3]
    q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    return list(zip(I.tolist(), J.tolist())), _summary(C, atoms_from_corr(C), atoms_from_corr(ar1_corr(a_x, a_y, q)))


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser(description="MMI-sts beside its AR(1)-substituted estimate for two series "
                                             "(one number per line in each file).")
    ap.add_argument("x_file")
    ap.add_argument("y_file")
    ap.add_argument("--window", type=int, default=0, help="window length in samples (0 = one fit over the whole series)")
    ap.add_argument("--tau", type=int, default=1)
    args = ap.parse_args()
    xs, ys = np.loadtxt(args.x_file), np.loadtxt(args.y_file)
    if args.window:
        d = diagnose_windows(xs, ys, args.window, args.tau)
        print("window  a_x      a_y      q        sts      sts_ar1  residual")
        for w in range(d["sts"].size):
            print(f"{w + 1:6d}  {d['a_x'][w]:+.4f}  {d['a_y'][w]:+.4f}  {d['q'][w]:+.4f}  "
                  f"{d['sts'][w]:.4f}   {d['sts_ar1'][w]:.4f}   {d['residual'][w]:+.4f}")
        bad = int(np.isnan(d["sts_ar1"]).sum())
        if bad:
            print(f"{bad} of {d['sts'].size} windows: no pair of AR(1) processes has the measured a_x, a_y and q "
                  f"(sts_ar1 NaN); report that share beside the means (np.nanmean)")
    else:
        d = diagnose(xs, ys, args.tau)
        print(f"a_x {d['a_x']:+.4f}  a_y {d['a_y']:+.4f}  q {d['q']:+.4f}  "
              f"sts {d['sts']:.4f}  sts_ar1 {d['sts_ar1']:.4f}  residual {d['residual']:+.4f}  (nats)")
        if np.isnan(d["sts_ar1"]):
            print("no pair of AR(1) processes has the measured a_x, a_y and q: the substituted estimate does not exist")
