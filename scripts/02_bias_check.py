"""
02_bias_check.py — finite-sample bias of windowed Gaussian ΦID atoms.

Pre-registered diagnostic (CLAUDE.md, open questions). A 30-TR window leaves
29 lag-1 transitions to fit a 4x4 covariance (10 free parameters), so the
plug-in Gaussian entropies — and therefore every ΦID atom — are biased. The
question that matters for the DMT claim is not "is there bias?" (yes) but
"is the bias the SAME across two conditions whose covariance structure
differs?", because a covariance shift is the hypothesis under test. If the
bias differs, a windowed DMT-vs-PCB synergy difference could be manufactured
by the estimator alone.

Design
------
Simulate a bivariate VAR(1),  z[t+1] = A z[t] + e[t],  e ~ N(0, Q), with
known (A, Q). The stationary lag-1 joint covariance of (x_t, y_t, x_t+1, y_t+1)
is then known in closed form, so every ΦID atom has an ANALYTIC value. The
estimator under test is exactly the FIT_MODE="window" estimator from
01_synergy_timecourse.py: take a W-TR window, call calc_PhiID on it (which
fits the Gaussian on that window alone), and average the local atoms over
the window.

Conditions (parameters fixed here, before any run):
  baseline        — PCB-like: moderate autocorrelation, weak cross-coupling,
                    weak innovation correlation.
  shift_coupling  — stronger cross-coupling in A (temporal structure changes).
  shift_noisecorr — stronger innovation correlation in Q (instantaneous
                    covariance changes; dynamics unchanged).
Both shifts are plausible for a drug that alters connectivity; they load on
different entries of the 4x4 covariance, so they are checked separately.

Window lengths: 30 (primary), 60 (load-bearing robustness), 840 (full-run
global fit, as reference).

Reported per (condition, window, atom):
  analytic value, mean estimate, bias (= mean - analytic) with 95% CI,
  SD of the estimate across windows (the variance term), and the fraction of
  windows in which the MMI double-redundancy min-selection picked an MI whose
  analytic value is NOT the analytic minimum (a discrete source of error the
  CI does not see). Picks between analytically tied MIs — e.g. I(x->y') and
  I(y->x') are identical under the symmetric A, Q used here — are not errors
  and are not counted.
And per (window, atom, shift): the DIFFERENTIAL bias, bias(shift) -
bias(baseline), with 95% CI, next to the true between-condition difference
in the atom — so bias magnitude can be read against effect magnitude.

Analytic atoms are computed by feeding the true differential entropies
through phyid's own downstream functions (_get_coinfo_four_vec etc.), so
the algebra — including the MMI min-selections — is identical by
construction. These are private functions; the phyid version is pinned in
requirements.lock.txt.

Does not touch the empirical data.
"""

import subprocess
import time
from pathlib import Path

import numpy as np
from scipy.linalg import solve_discrete_lyapunov

from phyid.calculate import (
    _get_atoms_four_vec,
    _get_coinfo_four_vec,
    _get_double_redundancy_four_vec,
    _get_redundancy_four_vec,
    calc_PhiID,
)

# ---------------------------------------------------------------- config
SEED = 20261120
TAU = 1
KIND = "gaussian"
REDUNDANCY = "MMI"
ATOMS = ("sts", "rtr")

WINDOWS = (30, 60, 840)        # TRs per window; 840 = full-run reference
N_WINDOWS = 2000               # independent windows per (condition, W)
BURN_IN = 200                  # TRs discarded so each window is stationary

# VAR(1) parameters. A = [[a, c], [c, a]] (symmetric coupling), Q = [[1, q],
# [q, 1]]. Stability requires |a| + |c| < 1. Values chosen to sit in the
# range of preprocessed fMRI at TR = 2 s (lag-1 autocorrelation ~0.3-0.6,
# pairwise correlation ~0.1-0.3); fixed before any run.
CONDITIONS = {
    "baseline":        dict(a=0.50, c=0.10, q=0.20),
    "shift_coupling":  dict(a=0.50, c=0.30, q=0.20),
    "shift_noisecorr": dict(a=0.50, c=0.10, q=0.60),
}
BASELINE = "baseline"

RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)
OUT_CSV = RESULTS / "bias_check.csv"
OUT_DIFF_CSV = RESULTS / "bias_check_differential.csv"

rng = np.random.default_rng(SEED)

# Order of the four-vector inside calc_PhiID: [src_past, trg_past,
# src_future, trg_future] = [x_t, y_t, x_t+tau, y_t+tau].
# Index sets must match _get_entropy_four_vec exactly.
_P1, _P2, _T1, _T2 = 0, 1, 2, 3
_ENTROPY_SETS = {
    "h_p1": [_P1], "h_p2": [_P2], "h_t1": [_T1], "h_t2": [_T2],
    "h_p1p2": [_P1, _P2], "h_t1t2": [_T1, _T2],
    "h_p1t1": [_P1, _T1], "h_p1t2": [_P1, _T2],
    "h_p2t1": [_P2, _T1], "h_p2t2": [_P2, _T2],
    "h_p1p2t1": [_P1, _P2, _T1], "h_p1p2t2": [_P1, _P2, _T2],
    "h_p1t1t2": [_P1, _T1, _T2], "h_p2t1t2": [_P2, _T1, _T2],
    "h_p1p2t1t2": [_P1, _P2, _T1, _T2],
}


# ---------------------------------------------------------------- model
def var1_matrices(a, c, q):
    A = np.array([[a, c], [c, a]])
    Q = np.array([[1.0, q], [q, 1.0]])
    eig = np.max(np.abs(np.linalg.eigvals(A)))
    assert eig < 1, f"VAR(1) unstable: spectral radius {eig:.3f}"
    return A, Q


def joint_lag_cov(A, Q, tau):
    """True covariance of (x_t, y_t, x_t+tau, y_t+tau) at stationarity."""
    S0 = solve_discrete_lyapunov(A, Q)             # S0 = A S0 A' + Q
    Atau = np.linalg.matrix_power(A, tau)
    cross = Atau @ S0                              # Cov(z_t+tau, z_t)
    return np.block([[S0, cross.T], [cross, S0]])


def analytic_atoms(S4, redundancy):
    """ΦID atoms implied by a known 4x4 covariance, via phyid's own algebra.

    Differential entropy of a k-dim Gaussian: 0.5*log((2*pi*e)^k det S).
    Each entropy is passed as a length-1 array so phyid's array code path,
    including the np.mean-based MMI min-selection, runs unchanged.
    """
    h_res = {}
    for name, idx in _ENTROPY_SETS.items():
        S = S4[np.ix_(idx, idx)]
        k = len(idx)
        h = 0.5 * np.log((2 * np.pi * np.e) ** k * np.linalg.det(S))
        h_res[name] = np.array([h])
    I_res = _get_coinfo_four_vec(h_res)
    R_res = _get_redundancy_four_vec(redundancy, I_res)
    calc = {"h_res": h_res, "I_res": I_res, "R_res": R_res}
    calc["rtr"] = _get_double_redundancy_four_vec(redundancy, calc)
    atoms = _get_atoms_four_vec(calc)
    return {k: float(v[0]) for k, v in atoms.items()}, calc


_RTR_MIS = ("I_xta", "I_xtb", "I_yta", "I_ytb")


def rtr_selection(calc_res):
    """Which of the four single-target MIs the MMI double redundancy picked."""
    I = calc_res["I_res"]
    means = [np.mean(I[k]) for k in _RTR_MIS]
    return int(np.argmin(means))


def rtr_wrong_pick(calc_res, true_mis, tol=1e-9):
    """True if the window picked an MI whose ANALYTIC value is not minimal.

    Picking between analytically tied MIs (e.g. I_xtb == I_yta under
    symmetric A, Q) is not an error, so ties are not counted.
    """
    picked = rtr_selection(calc_res)
    return (true_mis[picked] - min(true_mis)) > tol


def simulate(A, Q, n_trs, n_series, rng):
    """(n_series, 2, n_trs) stationary VAR(1) draws, burn-in discarded."""
    L = np.linalg.cholesky(Q)
    total = n_trs + BURN_IN
    z = np.zeros((n_series, 2, total))
    # innovations correlated across the 2 variables at each t: e_t = L w_t
    eps = np.einsum("ij,njt->nit", L, rng.standard_normal((n_series, 2, total)))
    for t in range(1, total):
        z[:, :, t] = np.einsum("ij,nj->ni", A, z[:, :, t - 1]) + eps[:, :, t]
    return z[:, :, BURN_IN:]


# ---------------------------------------------------------------- run
def main():
    t0 = time.time()
    rows = []          # per (condition, window, atom)
    est_store = {}     # (condition, W, atom) -> array of per-window estimates
    true_store = {}    # (condition, atom) -> analytic value
    sel_true = {}      # condition -> analytic rtr selection index

    for cond, p in CONDITIONS.items():
        A, Q = var1_matrices(**p)
        S4 = joint_lag_cov(A, Q, TAU)
        true_atoms, true_calc = analytic_atoms(S4, REDUNDANCY)
        true_mis = [float(true_calc["I_res"][k][0]) for k in _RTR_MIS]
        n_tied = int(np.sum(np.abs(np.array(true_mis) - min(true_mis)) < 1e-9))
        sel_true[cond] = true_mis
        for atom in ATOMS:
            true_store[(cond, atom)] = true_atoms[atom]
        print(f"[{cond}] a={p['a']} c={p['c']} q={p['q']}  "
              f"analytic sts={true_atoms['sts']:.4f} rtr={true_atoms['rtr']:.4f}  "
              f"rtr analytic min = {min(true_mis):.4f} "
              f"({n_tied} of 4 MIs tied at the min)")

        for W in WINDOWS:
            z = simulate(A, Q, W, N_WINDOWS, rng)   # (N_WINDOWS, 2, W)
            est = {atom: np.empty(N_WINDOWS) for atom in ATOMS}
            flips = 0
            for n in range(N_WINDOWS):
                atoms, calc = calc_PhiID(z[n, 0], z[n, 1], tau=TAU,
                                         kind=KIND, redundancy=REDUNDANCY)
                for atom in ATOMS:
                    est[atom][n] = np.mean(atoms[atom])   # window-mean local atom
                flips += rtr_wrong_pick(calc, sel_true[cond])
            flip_frac = flips / N_WINDOWS

            for atom in ATOMS:
                e = est[atom]
                est_store[(cond, W, atom)] = e
                truth = true_store[(cond, atom)]
                bias = e.mean() - truth
                se = e.std(ddof=1) / np.sqrt(N_WINDOWS)
                rows.append(dict(
                    condition=cond, window=W, atom=atom, n=N_WINDOWS,
                    analytic=truth, est_mean=e.mean(), bias=bias,
                    bias_ci_lo=bias - 1.96 * se, bias_ci_hi=bias + 1.96 * se,
                    est_sd=e.std(ddof=1), rtr_selection_flip_frac=flip_frac,
                ))
            print(f"    W={W:3d}  "
                  + "  ".join(
                      f"{atom}: bias={est[atom].mean() - true_store[(cond, atom)]:+.4f} "
                      f"sd={est[atom].std(ddof=1):.4f}" for atom in ATOMS)
                  + f"  rtr-flip={flip_frac:.3f}"
                  + f"  ({time.time() - t0:.0f}s)")

    # ------------------------------------------------ differential bias
    diff_rows = []
    for cond in CONDITIONS:
        if cond == BASELINE:
            continue
        for W in WINDOWS:
            for atom in ATOMS:
                e_s = est_store[(cond, W, atom)]
                e_b = est_store[(BASELINE, W, atom)]
                t_s = true_store[(cond, atom)]
                t_b = true_store[(BASELINE, atom)]
                true_diff = t_s - t_b
                est_diff = e_s.mean() - e_b.mean()
                dbias = est_diff - true_diff
                # windows are independent across conditions -> variances add
                se = np.sqrt(e_s.var(ddof=1) / e_s.size + e_b.var(ddof=1) / e_b.size)
                diff_rows.append(dict(
                    shift=cond, window=W, atom=atom,
                    true_diff=true_diff, est_diff=est_diff,
                    diff_bias=dbias,
                    diff_bias_ci_lo=dbias - 1.96 * se,
                    diff_bias_ci_hi=dbias + 1.96 * se,
                    # bias as a fraction of the true effect it could mimic
                    diff_bias_over_true_diff=(dbias / true_diff
                                              if true_diff != 0 else np.nan),
                ))

    # ------------------------------------------------ provenance + save
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        if subprocess.check_output(
            ["git", "status", "--porcelain", "--", "scripts", "CLAUDE.md"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip():
            sha += "-dirty"
    except (subprocess.CalledProcessError, FileNotFoundError):
        sha = "nogit"
    header = (f"# script=02_bias_check.py tau={TAU} kind={KIND} "
              f"redundancy={REDUNDANCY} n_windows={N_WINDOWS} "
              f"burn_in={BURN_IN} seed={SEED} git={sha}\n")

    def write_csv(path, rows):
        with open(path, "w") as fh:
            fh.write(header)
            keys = list(rows[0].keys())
            fh.write(",".join(keys) + "\n")
            for r in rows:
                fh.write(",".join(
                    f"{r[k]:.6f}" if isinstance(r[k], float) else str(r[k])
                    for k in keys) + "\n")

    write_csv(OUT_CSV, rows)
    write_csv(OUT_DIFF_CSV, diff_rows)

    # ------------------------------------------------ summary
    print("\nBIAS (estimate - analytic), 95% CI, SD across windows")
    print(f"{'condition':16s} {'W':>4s} {'atom':4s} {'analytic':>9s} "
          f"{'bias':>8s} {'[CI]':>18s} {'sd':>8s} {'flip':>6s}")
    for r in rows:
        print(f"{r['condition']:16s} {r['window']:4d} {r['atom']:4s} "
              f"{r['analytic']:9.4f} {r['bias']:+8.4f} "
              f"[{r['bias_ci_lo']:+7.4f},{r['bias_ci_hi']:+7.4f}] "
              f"{r['est_sd']:8.4f} {r['rtr_selection_flip_frac']:6.3f}")

    print("\nDIFFERENTIAL BIAS  bias(shift) - bias(baseline)  vs  true effect")
    print(f"{'shift':16s} {'W':>4s} {'atom':4s} {'true_diff':>9s} "
          f"{'est_diff':>9s} {'diff_bias':>10s} {'[CI]':>18s} {'bias/eff':>9s}")
    for r in diff_rows:
        print(f"{r['shift']:16s} {r['window']:4d} {r['atom']:4s} "
              f"{r['true_diff']:+9.4f} {r['est_diff']:+9.4f} "
              f"{r['diff_bias']:+10.4f} "
              f"[{r['diff_bias_ci_lo']:+7.4f},{r['diff_bias_ci_hi']:+7.4f}] "
              f"{r['diff_bias_over_true_diff']:+9.3f}")

    print(f"\nwrote {OUT_CSV}\nwrote {OUT_DIFF_CSV}")
    print(f"total {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
