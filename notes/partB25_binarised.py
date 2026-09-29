"""
partB25_binarised.py — B25: the binarised ΦID estimators on the symmetric AR(1) family: MMI and CCS through phyid's
discrete path, and the CCS emergence capacity of Ince's partial information decomposition, in the long-series limit
and at 160, 300 and 840 samples. No data.
Pre-run entry: manuscript/analysis_record.md, "The binarised estimators on the AR(1) family (B25): pre-run entry";
the first run and the correction of one check: "The binarised estimators on the AR(1) family (B25): the first run
and the correction of one check".

The family (Results 1): x, y unit-variance AR(1) processes with coefficient a (= r₁) whose innovations are correlated so
that their lag-0 correlation is q, with no lagged interaction; the lag-1 correlation matrix of (x_t, y_t, x_{t+1},
y_{t+1}) is rev_phiid_fast.ar1_corr(a, a, q).
The estimators. phyid's calc_PhiID(kind="discrete") binarises each of the four series x_t, y_t, x_{t+1}, y_{t+1} at its
own mean (1 above), takes plug-in probabilities of the binary patterns, evaluates local entropies in bits and forms the
nine local mutual informations, the redundancies and the lattice solve of the continuous path: MMI takes each
redundancy as the candidate with the smaller mean (the double redundancy the smallest of the four), CCS as Ince's
pointwise single-target redundancy (rev_phiid_fast._ccs_red) with the double redundancy the double co-information where
the signs agree — under the published mask (partB6's "pub": the four single-source, single-target local mutual
informations and the full one) and under phyid's ("code": the four and the double co-information itself). The emergence
capacity is str + stx + sty + sts, the synergy of the sources x_t, y_t about the joint future (x_{t+1}, y_{t+1});
under MMI it is the whole-minus-max synergy I(x_t, y_t; x_{t+1}, y_{t+1}) − max[I(x_t; ·), I(y_t; ·)] of Luppi et al.
(2024, Eq. 5), under either CCS mask it does not depend on the mask. The emergence capacity of Luppi et al. (2023),
as we read their Methods (p. 12: CCS, Ince's toolbox, the plug-in estimator on mean-binarised signals; the target is
not stated, and the joint future taken as one four-state target is our reading of "emergence capacity"), is computed
as Ince's toolbox computes it (github.com/robince/partial-info-decomp at 3220716, Iccs.m, calc_pi.m and mme2.py, read,
not run): a two-source partial information decomposition of x_t, y_t about S = (x_{t+1}, y_{t+1}), the redundancy
Ince's Iccs evaluated on the maximum-entropy distribution P̂ that keeps the three pairwise marginals P(x_t, S),
P(y_t, S) and P(x_t, y_t) (Ince, 2017, Definition 2; here by iterative proportional fitting from the uniform
distribution, and where that has not converged after 2,000 sweeps, from the uniform distribution on P̂'s support,
the cells that some distribution with those marginals makes positive, found by one linear programme per cell), the
synergy I(x_t, y_t; S) − I(x_t; S) − I(y_t; S) + Iccs with the mutual informations of the distribution itself. At
finite length each of the four lagged series is binarised at its own mean, as phyid does; Luppi et al. binarise each
signal once, which differs by O(1/T). Every value is converted from bits to nats (× ln 2).
(a) The long-series limit. Binarising at the mean is binarising at 0 in the limit, and the plug-in probabilities become
    the probabilities of the sixteen sign patterns of the four-variate Gaussian. They follow by inclusion–exclusion from
    the orthant probabilities of every subset of the four variables: closed forms up to three variables, and for all
    four Plackett's reduction, P₄(R) = 1/16 + ∫₀¹ Σ_{i<j} R_ij φ₂(0, 0; t R_ij) [1/4 + arcsin(ρ_{kl·ij}(t)) / (2π)] dt
    along R(t) = I + t (R − I) (φ₂ the bivariate normal density, ρ_{kl·ij} the partial correlation of the other two
    variables), by scipy.integrate.quad to about 10⁻¹³. Each estimator's local quantities are evaluated on each pattern and averaged
    with the pattern probabilities. Grid: r₁ ∈ {0.60, 0.65, …, 0.95} × q ∈ {0.10, 0.25, 0.50}; at the operating point
    (0.85, 0.25) the rates ∂/∂r₁ (a moved in both processes) and ∂/∂q by central differences with step 10⁻⁴, checked
    against step 10⁻³. Beside each point: 2A = I(x_t; x_{t+1}) + I(y_t; y_{t+1}), the two binarised self-informations,
    and the Gaussian-MMI closed form (sts = 2S − C, emergence capacity S).
(b) Finite length. For each point of the grid and T ∈ {160, 300, 840} samples, 1,000 replicate pairs simulated from a
    stationary start (x_0, y_0 with lag-0 correlation q; x_t = a x_{t−1} + √(1 − a²) w_t with w_t unit-variance and
    correlated q), with common random numbers across the grid (one set of standard-normal draws per T and replicate,
    drawn in the order T, replicate); per replicate phyid's calc_PhiID(x, y, 1, kind="discrete") under MMI and under
    CCS, the published-mask CCS atoms from the same local mutual informations, and Ince's CCS emergence capacity from
    the plug-in pattern frequencies of phyid's binarisation. Replicate means and SEs (SD / √1,000), and the difference
    from the limit.
(c) Checks: the four-variable orthant probability against scipy.stats.multivariate_normal.cdf (Genz) and the
    three-variable closed forms against the same reduction, on every matrix of the grid; the pattern probabilities
    positive, summing to 1, with the closed-form marginals; I(x_t; x_{t+1}) = 1 − H₂(arccos(a)/π) bits; the family's
    symmetries; phyid on ten series of 10⁵ samples at the operating point against the limit (within 4 SE + 2 × 10⁻⁴
    nats) and the rates at the two steps within 1 % (+ 10⁻⁶), for the quantities that are smooth on the family
    (SMOOTH: MMI sts, MMI EC, 2A, TDMI, MMI rtr, whose MMI selections are strict or exact ties there); phyid's local
    CCS atoms equal to their recomputation from its local mutual informations under its own mask within 10⁻¹², sample
    by sample (no sum over the samples enters the comparison), in the ten series and in every replicate; the
    maximum-entropy fits' marginals within 10⁻¹²; the copy of partB6's make_knowns verbatim; and the number of pattern
    values of a quantity whose sign a CCS mask tests (the nine local mutual informations, the six co-informations of the
    single-target redundancies and the double co-information) that are below 10⁻¹² in absolute value (reported: there
    the decision is set by rounding). The four CCS quantities (CCS-pub sts, CCS-code sts, CCS EC, Ince EC) jump wherever
    a sign mask changes, so for them the rates at both steps and the comparison with phyid are reported, not checked; a
    rate whose two steps differ by more than 1 % (+ 10⁻⁶) is reported as not differentiable on the 10⁻³ scale.
The simulations draw from one generator, np.random.default_rng(20261120): first the ten series of the check against
phyid, then the finite-length draws in the order T, replicate (the Genz check seeds its own generator with 20261120
at each call).
--selftest runs only checks that do not evaluate the family: the reductions against Genz on random correlation
matrices, the limit against phyid on two random stable VAR(1) pairs with lagged coupling, the Ince CCS against the
decompositions Ince (2017) publishes (Tables 6, 8–11 and 13) and his toolbox's examples2d_output.txt prints, and the
recomputation of phyid's CCS atoms; it writes nothing under notes/review_results/.
Free choices: those above. A failed check is printed as CHECK FAILED, counted in the table header, and the run goes on.
Outputs (notes/review_results/partB/): binarised_tables.md (its header carries the commit, the UTC time of the run and
the sha256 of binarised.csv), binarised.csv (a first line with the commit and the time, then one row per part,
estimator, quantity, r₁, q and T), binarised_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python -u notes/partB25_binarised.py 2>&1 | tee notes/review_results/partB/binarised_run.log
(its first run took 514 s; the replicates, 24,000 at each of the three lengths, take under 25 ms each on the planning
session's machine (--selftest times one at the longest length), the limit and the checks a few minutes)
"""
import hashlib
import itertools
import platform
import sys
import time
from pathlib import Path

import numpy as np
import scipy
from scipy.integrate import quad
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import linprog
from scipy.signal import lfilter
from scipy.stats import multivariate_normal

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import ATOMS, KNOWNS, _MINV_T, _MI_SETS, _ccs_red, _mmi_choice, _assemble, ar1_corr  # noqa: E402
from rev_git import SHA  # noqa: E402
import phyid  # noqa: E402
from phyid.calculate import calc_PhiID  # noqa: E402
from phyid.utils import _binarize  # noqa: E402

print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
SEED = 20261120
SELFTEST = "--selftest" in sys.argv
R1_GRID = tuple(round(0.60 + 0.05 * k, 2) for k in range(8))
Q_GRID = (0.10, 0.25, 0.50)
T_GRID = (160, 300, 840)
N_REP = 1000
OP = (0.85, 0.25)
H, H_CHECK = 1e-4, 1e-3
SD_R1, SD_Q = 0.0284, 0.1957          # within-window SDs of pair r₁ and |q| (B22 (d), aligned_directed_tables.md)
LN2 = float(np.log(2.0))
IX = {n: i for i, n in enumerate(ATOMS)}
EC_ATOMS = ("str", "stx", "sty", "sts")
PATTERNS = list(itertools.product((0, 1), repeat=4))
SMOOTH = ("MMI sts", "MMI EC", "2A", "TDMI", "MMI rtr")
t0 = time.time()
G0 = time.gmtime()
RUN_UTC = f"{G0.tm_mday} {time.strftime('%b %Y %H:%M', G0)} UTC"
nan = float("nan")
CHECKS, CSV = [], ["part,estimator,quantity,r1,q,T,value,se"]
IPF = {"calls": 0, "support": 0, "err": 0.0}


def check(name, diff, tol):
    ok = bool(np.isfinite(diff) and diff <= tol)
    CHECKS.append((name, float(diff), tol, ok))
    if not ok:
        print(f"   CHECK FAILED: {name}: {diff:.3g} above {tol:.1g}", flush=True)
    return ok


def rec(part, est, quantity, r1, q, T, value, se=nan):
    CSV.append(f'{part},{est},{quantity},{r1},{q},{T},{value:.10g},{se:.6g}')


def verbatim(src_rel, first, last):
    """The block between this file's markers equals lines first–last of src_rel."""
    own = Path(__file__).read_text(encoding="utf-8").split("\n")
    i = next(k for k, l in enumerate(own) if l.startswith(f"# ---- copied verbatim from {src_rel}, l. {first}–{last}"))
    j = next(k for k in range(i + 1, len(own)) if own[k].startswith("# ---- end of the copy"))
    src = (REPO / src_rel).read_text(encoding="utf-8").split("\n")[first - 1:last]
    check(f"the copy of {src_rel} l. {first}–{last} is verbatim", 0.0 if own[i + 1:j] == src else 1.0, 0.0)


# ---- copied verbatim from notes/partB6_ccs_definition.py, l. 51–76
def make_knowns(mask):
    """A drop-in for rev_phiid_fast.ccs_local_knowns with the requested double-redundancy mask."""
    def knowns(mi):
        R = {"R_xyta": _ccs_red(mi["I_xta"], mi["I_yta"], mi["I_xyta"]), "R_xytb": _ccs_red(mi["I_xtb"], mi["I_ytb"], mi["I_xytb"]),
             "R_xytab": _ccs_red(mi["I_xtab"], mi["I_ytab"], mi["I_xytab"]), "R_abtx": _ccs_red(mi["I_xta"], mi["I_xtb"], mi["I_xtab"]),
             "R_abty": _ccs_red(mi["I_yta"], mi["I_ytb"], mi["I_ytab"]), "R_abtxy": _ccs_red(mi["I_xyta"], mi["I_xytb"], mi["I_xytab"])}
        D = (-mi["I_xta"] - mi["I_xtb"] - mi["I_yta"] - mi["I_ytb"] + mi["I_xtab"] + mi["I_ytab"] + mi["I_xyta"] + mi["I_xytb"] - mi["I_xytab"]
             + R["R_xyta"] + R["R_xytb"] - R["R_xytab"] + R["R_abtx"] + R["R_abty"] - R["R_abtxy"])
        s0 = np.sign(mi["I_xta"])
        four = (s0 == np.sign(mi["I_xtb"])) & (s0 == np.sign(mi["I_yta"])) & (s0 == np.sign(mi["I_ytb"]))
        if mask == "code":
            agree = four & (s0 == np.sign(D))
        elif mask == "pub":
            agree = four & (s0 == np.sign(mi["I_xytab"]))
        elif mask == "pub8":
            agree = four & (s0 == np.sign(mi["I_xtab"])) & (s0 == np.sign(mi["I_ytab"])) & (s0 == np.sign(mi["I_xyta"])) & (s0 == np.sign(mi["I_xytb"])) & (s0 == np.sign(mi["I_xytab"]))
        elif mask == "pubD":
            agree = four & (s0 == np.sign(mi["I_xytab"])) & (s0 == np.sign(D))
        else:
            raise ValueError(mask)
        K = np.empty(mi["I_xta"].shape + (16,))
        K[..., 0] = np.where(agree, D, 0.0)
        for c, name in enumerate(KNOWNS[1:], start=1):
            K[..., c] = mi[name] if name in mi else R[name]
        return K, D, agree
    return knowns
# ---- end of the copy


KN_PUB, KN_CODE = make_knowns("pub"), make_knowns("code")


# ------------------------------------------------------------------ orthant and pattern probabilities
def orthant3(R, idx):
    i, j, k = idx
    return 0.125 + (np.arcsin(R[i, j]) + np.arcsin(R[i, k]) + np.arcsin(R[j, k])) / (4 * np.pi)


def _plackett(R, n):
    """P(X > 0) for X ~ N(0, R), R an n × n correlation matrix (n = 3 or 4), by Plackett's reduction along
    R(t) = I + t (R − I)."""
    I = np.eye(n)
    pairs = list(itertools.combinations(range(n), 2))

    def integrand(t):
        Rt = I + t * (R - I)
        s = 0.0
        for i, j in pairs:
            r = Rt[i, j]
            rest = [k for k in range(n) if k not in (i, j)]
            if n == 3:
                cond = 0.5
            else:
                A = Rt[np.ix_(rest, rest)] - Rt[np.ix_(rest, [i, j])] @ np.linalg.solve(Rt[np.ix_([i, j], [i, j])], Rt[np.ix_([i, j], rest)])
                rho = A[0, 1] / np.sqrt(A[0, 0] * A[1, 1])
                cond = 0.25 + np.arcsin(rho) / (2 * np.pi)
            s += R[i, j] / (2 * np.pi * np.sqrt(1.0 - r * r)) * cond
        return s

    val, _ = quad(integrand, 0.0, 1.0, epsabs=1e-15, epsrel=1e-13, limit=200)
    return 2.0 ** -n + val


def genz4(R):
    """P(X > 0) for X ~ N(0, R) by scipy's Genz algorithm (the independent check of the reduction)."""
    return float(multivariate_normal.cdf(np.zeros(4), mean=np.zeros(4), cov=R, maxpts=4_000_000, abseps=1e-10,
                                         releps=1e-10, rng=np.random.default_rng(SEED)))


def pattern_pmf(R):
    """(2, 2, 2, 2) probabilities of the sign patterns of X ~ N(0, R) (1 = positive), by inclusion–exclusion."""
    pS = {(): 1.0}
    for i in range(4):
        pS[(i,)] = 0.5
    for i, j in itertools.combinations(range(4), 2):
        pS[(i, j)] = 0.25 + np.arcsin(R[i, j]) / (2 * np.pi)
    for c in itertools.combinations(range(4), 3):
        pS[c] = orthant3(R, c)
    pS[(0, 1, 2, 3)] = _plackett(R, 4)
    P = np.empty((2, 2, 2, 2))
    for b in PATTERNS:
        pos = tuple(i for i in range(4) if b[i])
        zer = [i for i in range(4) if not b[i]]
        s = 0.0
        for k in range(len(zer) + 1):
            for B in itertools.combinations(zer, k):
                s += (-1) ** k * pS[tuple(sorted(pos + B))]
        P[b] = s
    return P


# ------------------------------------------------------------------ the estimators on a pattern distribution
def local_mis(P):
    """Local mutual informations (bits) on each of the 16 patterns, phyid's definitions, and the pattern weights."""
    w = np.array([P[b] for b in PATTERNS])
    h = {}
    for idx in {A for A, B in _MI_SETS.values()} | {B for A, B in _MI_SETS.values()} | {tuple(sorted(A + B)) for A, B in _MI_SETS.values()}:
        other = tuple(i for i in range(4) if i not in idx)
        M = P.sum(axis=other) if other else P
        with np.errstate(divide="ignore"):
            h[idx] = np.array([-np.log2(M[tuple(b[i] for i in idx)]) for b in PATTERNS])
    mi = {k: h[A] + h[B] - h[tuple(sorted(A + B))] for k, (A, B) in _MI_SETS.items()}
    return mi, w


def atoms_mmi(mi, w):
    """MMI atoms (bits) of the pattern distribution: the lattice solve of the pattern-averaged knowns, the MMI
    selections made on the means (the atoms' means depend on the means alone)."""
    keep = w > 0
    m = {k: np.array([float(np.dot(w[keep], v[keep]))]) for k, v in mi.items()}
    return (_assemble(m, _mmi_choice(m)) @ _MINV_T)[0]


def atoms_ccs(mi, w, kn):
    keep = w > 0
    K, D, agree = kn({k: v[keep] for k, v in mi.items()})
    return (w[keep] @ K) @ _MINV_T, D, agree


def ec(atoms):
    return float(sum(atoms[IX[k]] for k in EC_ATOMS))


def _ipf(P3, Q, tol, it_max):
    m1, m2, m12 = P3.sum(1), P3.sum(0), P3.sum(2)

    def ratio(target, current):
        return np.divide(target, current, out=np.zeros_like(target), where=current > 0)

    err = np.inf
    for it in range(it_max):
        Q *= ratio(m1, Q.sum(1))[:, None, :]
        Q *= ratio(m2, Q.sum(0))[None, :, :]
        Q *= ratio(m12, Q.sum(2))[:, :, None]
        err = max(np.abs(Q.sum(1) - m1).max(), np.abs(Q.sum(0) - m2).max(), np.abs(Q.sum(2) - m12).max())
        if err < tol:
            return Q, it + 1, err
    return Q, it_max, err


def maxent_support(P3):
    """The support of the maximum-entropy distribution with P3's pairwise marginals: the cells that some distribution
    with those marginals makes positive (the maximum of the cell's probability under the marginals, one linear
    programme per cell, above 10⁻¹²)."""
    sh, N = P3.shape, P3.size
    rows, b = [], []
    for keep in ((0, 2), (1, 2), (0, 1)):
        other = ({0, 1, 2} - set(keep)).pop()
        M = P3.sum(other)
        for idx in np.ndindex(M.shape):
            r = np.zeros(sh)
            sl = [slice(None)] * 3
            sl[keep[0]], sl[keep[1]] = idx
            r[tuple(sl)] = 1.0
            rows.append(r.ravel())
            b.append(M[idx])
    A_eq, b_eq = np.array(rows), np.array(b)
    supp = np.zeros(N, bool)
    for c in range(N):
        cost = np.zeros(N)
        cost[c] = -1.0
        res = linprog(cost, A_eq=A_eq, b_eq=b_eq, bounds=[(0, None)] * N, method="highs")
        supp[c] = res.status == 0 and -res.fun > 1e-12
    return supp.reshape(sh)


def ipf_maxent(P3, tol=1e-15):
    """The maximum-entropy distribution on (a1, a2, s) with the pairwise marginals of P3 (Ince, 2017, Definition 2), by
    iterative proportional fitting from the uniform distribution; where 2,000 sweeps do not reach the tolerance (the
    solution then lies on the boundary and plain IPF converges only sublinearly), from the uniform distribution on the
    solution's support. Returns P̂, the sweeps, the largest marginal error, and whether the support was used."""
    Q, it, err = _ipf(P3, np.full(P3.shape, 1.0 / P3.size), tol, 2000)
    used = False
    if err >= tol:
        S = maxent_support(P3)
        Q, it, err = _ipf(P3, S / S.sum(), tol, 100000)
        used = True
    IPF["calls"] += 1
    IPF["support"] += used
    IPF["err"] = max(IPF["err"], float(err))
    return Q, it, err, used


def ince_pid(P3):
    """Ince's two-source PID (bits) of P3[a1, a2, s]: (redundancy Iccs, unique 1, unique 2, synergy), as Iccs.m and
    calc_pi.m compute it (no thresholding, no normalisation): the local terms on the cells where P̂ > 0, kept where
    sign(ds1) = sign(ds2) = sign(dsj) = sign(overlap), weighted by P̂."""
    Ph = ipf_maxent(P3)[0]
    Ps = P3.sum((0, 1))
    Pa1s, Pa2s = P3.sum(1), P3.sum(0)
    Pa1, Pa2 = Pa1s.sum(1), Pa2s.sum(1)
    Pha12 = Ph.sum(2)
    with np.errstate(divide="ignore", invalid="ignore"):
        dsj = np.log2(Ph / (Pha12[:, :, None] * Ps[None, None, :]))
        ds1 = np.log2(Pa1s / (Pa1[:, None] * Ps[None, :]))[:, None, :]
        ds2 = np.log2(Pa2s / (Pa2[:, None] * Ps[None, :]))[None, :, :]
        overlap = ds1 + ds2 - dsj
    valid = (Ph > 0) & (Pa1s[:, None, :] > 0) & (Pa2s[None, :, :] > 0)
    keep = valid & (np.sign(ds1) == np.sign(ds2)) & (np.sign(dsj) == np.sign(ds1)) & (np.sign(overlap) == np.sign(ds1))
    red = float(np.sum(Ph[keep] * overlap[keep]))

    def mi2(Pab):
        pa, pb = Pab.sum(1), Pab.sum(0)
        nz = Pab > 0
        return float(np.sum(Pab[nz] * np.log2(Pab[nz] / np.outer(pa, pb)[nz])))

    i1, i2 = mi2(Pa1s), mi2(Pa2s)
    i12 = mi2(P3.reshape(-1, P3.shape[2]))
    return red, i1 - red, i2 - red, i12 - i1 - i2 + red


def ince_ec(P):
    """Luppi et al. (2023)'s emergence capacity (bits): the Ince-PID synergy of x_t, y_t about S = (x_{t+1}, y_{t+1})."""
    P3 = P.reshape(2, 2, 4)                       # axes: x_t, y_t, S = 2 x_{t+1} + y_{t+1}
    return ince_pid(P3)[3]


def estimators_of_pmf(P):
    """Every reported quantity (nats) of one pattern distribution, and the near-zero sign count of the CCS masks."""
    mi, w = local_mis(P)
    A_m = atoms_mmi(mi, w)
    A_p, D_p, _ = atoms_ccs(mi, w, KN_PUB)
    A_c, _, _ = atoms_ccs(mi, w, KN_CODE)
    keep = w > 0
    m = {k: v[keep] for k, v in mi.items()}
    coi = [m[a] + m[b] - m[c] for a, b, c in (("I_xta", "I_yta", "I_xyta"), ("I_xtb", "I_ytb", "I_xytb"),
                                              ("I_xtab", "I_ytab", "I_xytab"), ("I_xta", "I_xtb", "I_xtab"),
                                              ("I_yta", "I_ytb", "I_ytab"), ("I_xyta", "I_xytb", "I_xytab"))]
    tested = list(m.values()) + coi + [D_p]
    near0 = int(sum(np.sum(np.abs(v) < 1e-12) for v in tested))
    self2 = float(np.dot(w[keep], mi["I_xta"][keep]) + np.dot(w[keep], mi["I_ytb"][keep]))
    tdmi = float(np.dot(w[keep], mi["I_xytab"][keep]))
    out = {"MMI sts": A_m[IX["sts"]], "MMI EC": ec(A_m), "CCS-pub sts": A_p[IX["sts"]], "CCS-code sts": A_c[IX["sts"]],
           "CCS EC": ec(A_p), "Ince EC": ince_ec(P), "2A": self2, "TDMI": tdmi, "MMI rtr": A_m[IX["rtr"]]}
    return {k: float(v) * LN2 for k, v in out.items()}, A_m, A_p, A_c, near0


QUANTS = ("MMI sts", "MMI EC", "CCS-pub sts", "CCS-code sts", "CCS EC", "Ince EC", "2A", "TDMI", "MMI rtr")


# ------------------------------------------------------------------ simulation and phyid
def simulate_family(a, q, Z):
    """x, y of the family from standard-normal draws Z (2, T): stationary start, x_t = a x_{t−1} + √(1 − a²) w_t."""
    L = np.linalg.cholesky(np.array([[1.0, q], [q, 1.0]]))
    W = L @ Z
    b = np.sqrt(1.0 - a * a)
    out = np.empty_like(W)
    for r in range(2):
        out[r], _ = lfilter([b], [1.0, -a], W[r], zi=[(1.0 - b) * W[r, 0]])
    return out[0], out[1]


def phyid_quantities(x, y):
    """The finite-sample estimators (nats) of one pair of series, and the CCS recomputation check: the largest
    difference, over the samples and the sixteen atoms, between phyid's local CCS atoms and the atoms of the local
    knowns recomputed from its local mutual informations under its mask, compared sample by sample, so that no sum
    over the samples enters it."""
    at_m, cr = calc_PhiID(x, y, 1, kind="discrete", redundancy="MMI")
    at_c, _ = calc_PhiID(x, y, 1, kind="discrete", redundancy="CCS")
    I = cr["I_res"]
    mean_m = np.array([np.mean(at_m[k]) for k in ATOMS])
    mean_c = np.array([np.mean(at_c[k]) for k in ATOMS])
    Kp, _, _ = KN_PUB(I)
    Kc, _, _ = KN_CODE(I)
    mean_p = Kp.mean(0) @ _MINV_T
    dev = float(np.max(np.abs(Kc @ _MINV_T - np.stack([at_c[k] for k in ATOMS], axis=-1))))
    Xb = np.c_[_binarize(x[:-1]), _binarize(y[:-1]), _binarize(x[1:]), _binarize(y[1:])]
    counts = np.zeros((2, 2, 2, 2))
    np.add.at(counts, tuple(Xb.T), 1.0)
    P = counts / Xb.shape[0]
    out = {"MMI sts": mean_m[IX["sts"]], "MMI EC": ec(mean_m), "CCS-pub sts": mean_p[IX["sts"]],
           "CCS-code sts": mean_c[IX["sts"]], "CCS EC": ec(mean_p), "Ince EC": ince_ec(P),
           "2A": np.mean(I["I_xta"]) + np.mean(I["I_ytb"]), "TDMI": np.mean(I["I_xytab"]), "MMI rtr": mean_m[IX["rtr"]]}
    return {k: float(v) * LN2 for k, v in out.items()}, dev


def gaussian_family(a, q):
    S = -0.5 * np.log(1 - a * a)
    C = -0.5 * np.log(1 - a * a * q * q)
    return 2 * S - C, S


def long_series_check(label, R4, sim, n_series=10, n=100_000, rng=None, checked=QUANTS):
    """phyid (and the Ince EC) on n_series independent series of n samples against the limit of R4; the quantities
    in `checked` are checks, the others are reported."""
    lim, _, _, _, _ = estimators_of_pmf(pattern_pmf(R4))
    vals = {k: [] for k in QUANTS}
    for s in range(n_series):
        x, y = sim(n, rng)
        v, dev = phyid_quantities(x, y)
        check(f"{label}: phyid's local CCS atoms recomputed from its local MIs, sample by sample (series {s + 1})", dev,
              1e-12)
        for k in QUANTS:
            vals[k].append(v[k])
    lines = []
    for k in QUANTS:
        m, se = np.mean(vals[k]), np.std(vals[k], ddof=1) / np.sqrt(n_series)
        within = abs(m - lim[k]) - 4 * se <= 2e-4
        if k in checked:
            check(f"{label}: {k} of phyid at n = {n:,} within 4 SE + 2e-4 of the limit", abs(m - lim[k]) - 4 * se, 2e-4)
        lines.append(f"| {k} | {lim[k]:+.5f} | {m:+.5f} ± {se:.5f} | {m - lim[k]:+.5f} | "
                     f"{('yes' if within else 'no') + ('' if k in checked else ' (reported, not checked)')} |")
    return lines


# ------------------------------------------------------------------ the self-test (no evaluation of the family)
def random_corr(rng, n):
    B = rng.normal(size=(n, 2 * n))
    S = B @ B.T
    d = np.sqrt(np.diag(S))
    return S / np.outer(d, d)


def random_var1(rng):
    """A random stable VAR(1) pair with lagged coupling: its lag-1 correlation matrix and a simulator."""
    A = rng.normal(0, 0.5, (2, 2))
    A *= 0.9 / max(0.9, np.max(np.abs(np.linalg.eigvals(A))))
    Lr = rng.normal(size=(2, 2))
    Sig = Lr @ Lr.T + 0.2 * np.eye(2)
    G0 = solve_discrete_lyapunov(A, Sig)
    C4 = np.block([[G0, G0 @ A.T], [A @ G0, G0]])
    d = np.sqrt(np.diag(C4))
    R4 = C4 / np.outer(d, d)
    Lc = np.linalg.cholesky(Sig)
    L0 = np.linalg.cholesky(G0)

    def sim(n, rng_):
        z = np.empty((2, n))
        z[:, 0] = L0 @ rng_.standard_normal(2)
        e = Lc @ rng_.standard_normal((2, n))
        for t in range(1, n):
            z[:, t] = A @ z[:, t - 1] + e[:, t]
        return z[0], z[1]
    return R4, sim, A


INCE_EXAMPLES = {   # (x1, x2, s) → probability; the published PID [{1}{2}, {1}, {2}, {12}] and its printed decimals
    "RDN (examples2d_output.txt)": ({(0, 0, 0): .5, (1, 1, 1): .5}, (1, 0, 0, 0), 4),
    "W&B Fig 4A / Ince 2017 Table 8": ({(0, 0, 0): 1 / 3, (0, 1, 1): 1 / 3, (1, 0, 2): 1 / 3}, (0.3900, 0.5283, 0.5283, 0.1383), 4),
    "W&B Fig 4B / Ince 2017 Table 9": ({(0, 0, 0): .25, (0, 1, 1): .25, (1, 1, 1): .25, (1, 0, 2): .25}, (0, 0.5, 1, 0), 4),
    "W&B Fig 4 modified 1 / Ince 2017 Table 10": ({(0, 0, 0): 1 / 6, (0, 1, 1): 1 / 6, (1, 1, 1): 1 / 6, (1, 0, 2): 1 / 6, (1, 1, 0): 1 / 6, (0, 1, 2): 1 / 6}, (0, 0, 0.2516, 0.6667), 4),
    "W&B Fig 4 modified 2 (examples2d_output.txt)": ({(0, 0, 0): .2, (0, 1, 1): .2, (1, 1, 1): .2, (1, 0, 2): .2, (1, 1, 0): .2}, (0, 0.1710, 0.5710, 0.3800), 4),
    "2 bit copy, independent (examples2d_output.txt)": ({(0, 0, 0): .25, (0, 1, 1): .25, (1, 0, 2): .25, (1, 1, 3): .25}, (0, 1, 1, 0), 4),
    "OR / Ince 2017 Table 11": ({(0, 0, 0): .25, (0, 1, 1): .25, (1, 0, 1): .25, (1, 1, 1): .25}, (0.1038, 0.2075, 0.2075, 0.2925), 4),
    "XOR (examples2d_output.txt)": ({(0, 0, 0): .25, (0, 1, 1): .25, (1, 0, 1): .25, (1, 1, 0): .25}, (0, 0, 0, 1), 4),
    "AND / Ince 2017 Table 11": ({(0, 0, 0): .25, (0, 1, 0): .25, (1, 0, 0): .25, (1, 1, 1): .25}, (0.1038, 0.2075, 0.2075, 0.2925), 4),
    "SUM / Ince 2017 Table 13": ({(0, 0, 0): .25, (0, 1, 1): .25, (1, 0, 1): .25, (1, 1, 2): .25}, (0, 0.5, 0.5, 0.5), 4),
    "IMPERFECTRDN (examples2d_output.txt)": ({(0, 0, 0): .4, (0, 1, 0): .1, (1, 1, 1): .5}, (0.7685, 0.2315, -0.1585, 0.1585), 4),
    "Reduced OR / Ince 2017 Table 6": ({(0, 0, 0): .5, (0, 1, 1): .25, (1, 0, 1): .25}, (0, 0.3113, 0.3113, 0.3774), 4),
}


def ince_table(entries):
    sx = max(k[0] for k in entries) + 1
    sy = max(k[1] for k in entries) + 1
    ss = max(k[2] for k in entries) + 1
    P3 = np.zeros((sx, sy, ss))
    for k, v in entries.items():
        P3[k] = v
    return P3


def selftest():
    rng = np.random.default_rng(SEED + 1)
    print("SELF-TEST (no evaluation of the AR(1) family)", flush=True)
    worst3 = worst4 = 0.0
    for _ in range(20):
        R3 = random_corr(rng, 3)
        worst3 = max(worst3, abs(_plackett(R3, 3) - orthant3(R3, (0, 1, 2))))
        R4 = random_corr(rng, 4)
        g = genz4(R4)
        worst4 = max(worst4, abs(_plackett(R4, 4) - g))
    check("three-variable reduction against the closed form, 20 random matrices", worst3, 1e-12)
    check("four-variable reduction against Genz, 20 random matrices", worst4, 1e-6)
    print(f"   reductions: 3-variable max |Δ| {worst3:.2e}; 4-variable against Genz max |Δ| {worst4:.2e}", flush=True)
    for name, (entries, published, dec) in INCE_EXAMPLES.items():
        pid = ince_pid(ince_table(entries))
        d = max(abs(round(v, dec) - p) for v, p in zip(pid, published))
        check(f"Ince CCS PID, {name}", d, 0.5 * 10 ** -dec + 1e-12)
        print(f"   {name}: [{', '.join(f'{v:.4f}' for v in pid)}] against {published}", flush=True)
    for k in range(2):
        R4, sim, A = random_var1(rng)
        print(f"   random VAR(1) {k + 1}: A = {np.round(A, 3).tolist()}", flush=True)
        t1 = time.time()
        lines = long_series_check(f"random VAR(1) {k + 1}", R4, sim, n_series=10, n=100_000, rng=rng)
        print("\n".join(["   | quantity | limit | phyid, 10 × 10⁵ samples | difference | within 4 SE + 2e-4 |"] + ["   " + l for l in lines]), flush=True)
        print(f"   ({time.time() - t1:.0f} s)", flush=True)
    x, y = random_var1(rng)[1](840, rng)
    t1 = time.time()
    for _ in range(20):
        phyid_quantities(x, y)
    print(f"   one replicate at T = 840: {(time.time() - t1) / 20 * 1000:.1f} ms", flush=True)
    check("the maximum-entropy fits' marginals", IPF["err"], 1e-12)
    print(f"   maximum-entropy fits: {IPF['calls']}, from the support {IPF['support']}, largest marginal error "
          f"{IPF['err']:.1e}", flush=True)
    nfail = sum(not c[3] for c in CHECKS)
    print(f"SELF-TEST: {len(CHECKS)} checks, {nfail} failed", flush=True)
    return nfail


if SELFTEST:
    verbatim("notes/partB6_ccs_definition.py", 51, 76)
    sys.exit(1 if selftest() else 0)

# ------------------------------------------------------------------ (a) the long-series limit
print(f"python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}, phyid {phyid.__version__}",
      flush=True)
verbatim("notes/partB6_ccs_definition.py", 51, 76)
LIM, NEAR0 = {}, {}
worst3 = worst4 = 0.0
for q in Q_GRID:
    for r1 in R1_GRID:
        R4 = ar1_corr(r1, r1, q)[0]
        for c in itertools.combinations(range(4), 3):
            worst3 = max(worst3, abs(_plackett(R4[np.ix_(c, c)], 3) - orthant3(R4, c)))
        g = genz4(R4)
        worst4 = max(worst4, abs(_plackett(R4, 4) - g))
        P = pattern_pmf(R4)
        check(f"pattern probabilities positive at ({r1}, {q})", 0.0 if P.min() > 0 else 1.0, 0.0)
        check(f"pattern probabilities sum to 1 at ({r1}, {q})", abs(P.sum() - 1.0), 1e-13)
        m1 = max(abs(P.sum(axis=tuple(j for j in range(4) if j != i))[1] - 0.5) for i in range(4))
        m2 = max(abs(P.sum(axis=tuple(k for k in range(4) if k not in (i, j)))[1, 1] - (0.25 + np.arcsin(R4[i, j]) / (2 * np.pi)))
                 for i, j in itertools.combinations(range(4), 2))
        check(f"pattern marginals at ({r1}, {q})", max(m1, m2), 1e-13)
        vals, A_m, A_p, A_c, near0 = estimators_of_pmf(P)
        p_flip = np.arccos(r1) / np.pi
        H2 = -(p_flip * np.log2(p_flip) + (1 - p_flip) * np.log2(1 - p_flip))
        check(f"I(x_t; x_t+1) = 1 − H2(arccos(a)/π) at ({r1}, {q})", abs(vals["2A"] / 2 / LN2 - (1 - H2)), 1e-12)
        sym = max(abs(A_m[IX["xtx"]] - A_m[IX["yty"]]), abs(A_m[IX["rts"]] - A_m[IX["str"]]), abs(A_m[IX["stx"]] - A_m[IX["sty"]]),
                  abs(A_m[IX["xts"]] - A_m[IX["yts"]]), abs(A_p[IX["xtx"]] - A_p[IX["yty"]]), abs(A_p[IX["rts"]] - A_p[IX["str"]]))
        check(f"the family's symmetries (xtx = yty, rts = str, stx = sty, xts = yts) at ({r1}, {q})", sym, 1e-12)
        LIM[(r1, q)] = vals
        NEAR0[(r1, q)] = near0
        g_sts, g_ec = gaussian_family(r1, q)
        for k, v in vals.items():
            rec("a", k.split()[0], k, r1, q, "inf", v)
        rec("a", "Gaussian-MMI", "sts (closed form)", r1, q, "inf", g_sts)
        rec("a", "Gaussian-MMI", "EC (closed form)", r1, q, "inf", g_ec)
check("three-variable closed forms against the reduction, every grid matrix", worst3, 1e-12)
check("four-variable reduction against Genz, every grid matrix", worst4, 1e-6)
print(f"(a) the limit: 24 points ({time.time() - t0:.0f} s); reductions: 3-variable {worst3:.2e}, 4-variable {worst4:.2e}",
      flush=True)


def lim_at(a, q):
    return estimators_of_pmf(pattern_pmf(ar1_corr(a, a, q)[0]))[0]


RATES = {}
for h in (H, H_CHECK):
    up_a, dn_a = lim_at(OP[0] + h, OP[1]), lim_at(OP[0] - h, OP[1])
    up_q, dn_q = lim_at(OP[0], OP[1] + h), lim_at(OP[0], OP[1] - h)
    RATES[h] = {k: ((up_a[k] - dn_a[k]) / (2 * h), (up_q[k] - dn_q[k]) / (2 * h)) for k in QUANTS}
SMOOTH_RATE = {}
for k in QUANTS:
    for j, lab in ((0, "r1"), (1, "q")):
        r, rc = RATES[H][k][j], RATES[H_CHECK][k][j]
        SMOOTH_RATE[(k, lab)] = abs(r - rc) - 0.01 * abs(r) <= 1e-6
        if k in SMOOTH:
            check(f"rate d({k})/d{lab} at the two steps within 1 % (+ 10⁻⁶)", abs(r - rc) - 0.01 * abs(r), 1e-6)
        rec("a", k.split()[0], f"d({k})/d{lab}", OP[0], OP[1], "inf", r)
        rec("a", k.split()[0], f"d({k})/d{lab} [step 1e-3]", OP[0], OP[1], "inf", rc)
d_r1, d_q = RATES[H]["MMI sts"]
ratio_unit = d_r1 / abs(d_q) if d_q != 0 else float("inf")
ratio_sd = (d_r1 * SD_R1) / (abs(d_q) * SD_Q) if d_q != 0 else float("inf")

# ------------------------------------------------------------------ the check against phyid at the operating point
rng = np.random.default_rng(SEED)
L_OP = long_series_check("operating point (0.85, 0.25)", ar1_corr(OP[0], OP[0], OP[1])[0],
                         lambda n, g: simulate_family(OP[0], OP[1], g.standard_normal((2, n))), n_series=10, n=100_000, rng=rng,
                         checked=SMOOTH)
print(f"    the check against phyid at the operating point ({time.time() - t0:.0f} s)", flush=True)

# ------------------------------------------------------------------ (b) finite length
FIN, DEVMAX = {}, 0.0
for T in T_GRID:
    Z = rng.standard_normal((N_REP, 2, T))
    for q in Q_GRID:
        for r1 in R1_GRID:
            vals = {k: np.empty(N_REP) for k in QUANTS}
            for i in range(N_REP):
                x, y = simulate_family(r1, q, Z[i])
                v, dev = phyid_quantities(x, y)
                DEVMAX = float(np.maximum(DEVMAX, dev))            # np.maximum keeps a NaN, which max() would drop
                for k in QUANTS:
                    vals[k][i] = v[k]
            for k in QUANTS:
                m, se = float(vals[k].mean()), float(vals[k].std(ddof=1) / np.sqrt(N_REP))
                FIN[(r1, q, T, k)] = (m, se)
                rec("b", k.split()[0], k, r1, q, T, m, se)
    print(f"(b) T = {T} done ({time.time() - t0:.0f} s)", flush=True)
check("phyid's local CCS atoms equal their recomputation from its local MIs, sample by sample, every replicate", DEVMAX,
      1e-12)
check("the maximum-entropy fits' marginals", IPF["err"], 1e-12)


# ------------------------------------------------------------------ the facts the pre-run entry's predictions read
def steps(seq):
    return [b - a for a, b in zip(seq[:-1], seq[1:])]


F = {}
lim_steps = [s for q in Q_GRID for k in ("MMI sts", "MMI EC") for s in steps([LIM[(r1, q)][k] for r1 in R1_GRID])]
F["a_rising"] = sum(s > 0 for s in lim_steps)
F["a_total"] = len(lim_steps)
fin_steps = [s for T in T_GRID for q in Q_GRID for k in ("MMI sts", "MMI EC")
             for s in steps([FIN[(r1, q, T, k)][0] for r1 in R1_GRID])]
F["c_rising"] = sum(s > 0 for s in fin_steps)
F["c_total"] = len(fin_steps)
F["b_d_r1"], F["b_d_q"], F["b_ratio_unit"], F["b_ratio_sd"] = d_r1, d_q, ratio_unit, ratio_sd

# ------------------------------------------------------------------ the tables
nfail = sum(not c[3] for c in CHECKS)
CSV_TEXT = "\n".join([f"# partB25_binarised.py; git={SHA}; run {RUN_UTC}"] + CSV) + "\n"
CSV_SHA = hashlib.sha256(CSV_TEXT.encode("utf-8")).hexdigest()
L = [f"# B25: the binarised estimators on the symmetric AR(1) family (partB25_binarised.py)", f"git={SHA}",
     f"run {RUN_UTC}", f"binarised.csv sha256 {CSV_SHA}", "",
     f"Pre-run entry: record, \"The binarised estimators on the AR(1) family (B25): pre-run entry\". "
     f"python {platform.python_version()}, numpy {np.__version__}, scipy {scipy.__version__}, phyid {phyid.__version__}. "
     f"Checks: {len(CHECKS)}, failed {nfail}. Values in nats (bits × ln 2). MMI: phyid's discrete path under MMI; "
     "CCS-pub / CCS-code: phyid's discrete path under CCS with the published / phyid's double-redundancy mask; "
     "CCS EC: str + stx + sty + sts under CCS (either mask); Ince EC: the synergy of x_t, y_t about the joint future in "
     "Ince's PID (Luppi et al., 2023); 2A: I(x_t; x_t+1) + I(y_t; y_t+1) of the binarised series; EC: emergence "
     "capacity, str + stx + sty + sts.", "",
     "## (a) The long-series limit", ""]
for q in Q_GRID:
    L += [f"### q = {q}", "",
          "| r₁ | MMI sts | MMI EC | 2A | CCS-pub sts | CCS-code sts | CCS EC | Ince EC | Gaussian-MMI sts | Gaussian-MMI EC (= S) |",
          "|---|---|---|---|---|---|---|---|---|---|"]
    for r1 in R1_GRID:
        v = LIM[(r1, q)]
        gs, ge = gaussian_family(r1, q)
        L.append(f"| {r1:.2f} | {v['MMI sts']:.5f} | {v['MMI EC']:.5f} | {v['2A']:.5f} | {v['CCS-pub sts']:+.5f} | "
                 f"{v['CCS-code sts']:+.5f} | {v['CCS EC']:+.5f} | {v['Ince EC']:+.5f} | {gs:.5f} | {ge:.5f} |")
    L.append("")
L += ["### Rates at the operating point (0.85, 0.25), nats per unit (central differences, step 10⁻⁴; step 10⁻³ in brackets)", "",
      "A rate marked * differs between the two steps by more than 1 % (+ 10⁻⁶): the quantity is not differentiable there on "
      "the 10⁻³ scale (a CCS sign mask changes within the step).", "",
      "| quantity | ∂/∂r₁ | ∂/∂q |", "|---|---|---|"]
for k in QUANTS:
    (a1, q1), (a3, q3) = RATES[H][k], RATES[H_CHECK][k]
    L.append(f"| {k} | {a1:+.4f} ({a3:+.4f}){'' if SMOOTH_RATE[(k, 'r1')] else ' *'} | "
             f"{q1:+.4f} ({q3:+.4f}){'' if SMOOTH_RATE[(k, 'q')] else ' *'} |")
L += ["", f"MMI sts: ∂/∂r₁ {d_r1:+.4f}, ∂/∂q {d_q:+.4f}; per unit ratio {ratio_unit:.2f}; per SD of the pairs' variation "
      f"within a window (r₁ {SD_R1}, |q| {SD_Q}) {ratio_sd:.2f}.", "",
      f"Patterns at which a quantity a CCS mask tests is below 10⁻¹² in absolute value: "
      f"{sum(NEAR0.values())} over the 24 grid points ({', '.join(f'({k[0]}, {k[1]}): {v}' for k, v in NEAR0.items() if v)}).", "",
      f"Maximum-entropy fits (Ince EC): {IPF['calls']:,}, of which {IPF['support']:,} from the support; largest marginal "
      f"error {IPF['err']:.1e}.", "",
      "### The limit against phyid at the operating point (10 series of 10⁵ samples)", "",
      "| quantity | limit | phyid, mean ± SE | difference | within 4 SE + 2e-4 |", "|---|---|---|---|---|"] + L_OP + [""]
L += ["## (b) Finite length: replicate means ± SE (1,000 replicates) and the difference from the limit", ""]
for T in T_GRID:
    for q in Q_GRID:
        L += [f"### T = {T}, q = {q}", "",
              "| r₁ | MMI sts | − limit | MMI EC | − limit | CCS-pub sts | CCS EC | Ince EC | − limit |",
              "|---|---|---|---|---|---|---|---|---|"]
        for r1 in R1_GRID:
            f = {k: FIN[(r1, q, T, k)] for k in QUANTS}
            lv = LIM[(r1, q)]
            L.append(f"| {r1:.2f} | {f['MMI sts'][0]:.5f} ± {f['MMI sts'][1]:.5f} | {f['MMI sts'][0] - lv['MMI sts']:+.5f} | "
                     f"{f['MMI EC'][0]:.5f} ± {f['MMI EC'][1]:.5f} | {f['MMI EC'][0] - lv['MMI EC']:+.5f} | "
                     f"{f['CCS-pub sts'][0]:+.5f} ± {f['CCS-pub sts'][1]:.5f} | {f['CCS EC'][0]:+.5f} ± {f['CCS EC'][1]:.5f} | "
                     f"{f['Ince EC'][0]:+.5f} ± {f['Ince EC'][1]:.5f} | {f['Ince EC'][0] - lv['Ince EC']:+.5f} |")
        L.append("")
L += ["## The facts the pre-run entry's predictions read", "",
      f"- (a) steps of MMI sts and MMI EC along r₁ (7 per curve, 3 values of q) that rise in the limit: {F['a_rising']} of {F['a_total']}.",
      f"- (b) at (0.85, 0.25): ∂(MMI sts)/∂r₁ = {F['b_d_r1']:+.4f}, ∂(MMI sts)/∂q = {F['b_d_q']:+.4f}; per-unit ratio "
      f"{F['b_ratio_unit']:.2f}; per-SD ratio {F['b_ratio_sd']:.2f}.",
      f"- (c) steps of the replicate means of MMI sts and MMI EC along r₁ (7 per curve, 3 values of q, 3 lengths) that rise: "
      f"{F['c_rising']} of {F['c_total']}.", "",
      "## Checks", "", "| check | largest difference | tolerance | passed |", "|---|---|---|---|"]
L += [f"| {n} | {d:.3g} | {t:.1g} | {'yes' if ok else 'NO'} |" for n, d, t, ok in CHECKS]
L += ["", f"Wall-clock {time.time() - t0:.0f} s."]
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "binarised_tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")
(OUT / "binarised.csv").write_text(CSV_TEXT, encoding="utf-8")
print("\n".join(L[-(len(CHECKS) + 12):]), flush=True)
print(f"checks: {len(CHECKS)}, failed {nfail}; wrote {OUT / 'binarised_tables.md'} and binarised.csv; {time.time() - t0:.0f} s",
      flush=True)
