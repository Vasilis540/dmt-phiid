"""
02_bias_check.py — finite-sample bias of windowed Gaussian ΦID atoms.

Pre-registered diagnostic (manuscript/analysis_record.md, open questions). A 30-TR window leaves
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

Conditions (parameters fixed here, before any run). A = [[a1, c12],
[c21, a2]], Q = [[s1^2, q s1 s2], [q s1 s2, s2^2]].
  Symmetric family (first run, 12 Sep 2026, git e01c836): a1 = a2,
  c12 = c21, s1 = s2.
    baseline        — PCB-like: moderate autocorrelation, weak cross-coupling,
                      weak innovation correlation.
    shift_coupling  — stronger cross-coupling in A (temporal structure changes).
    shift_noisecorr — stronger innovation correlation in Q (instantaneous
                      covariance changes; dynamics unchanged).
  Asymmetric family (added 12 Sep 2026 after the first run and before any
  windowed result on real data): a1 != a2, c12 != c21, s1 != s2. Under the
  symmetric family I(x;y') == I(y;x') and I(x;x') == I(y;y') exactly, so two
  of the four MMI double-redundancy candidates are analytically tied — a
  situation no real region pair is in. A tie makes the min-selection error
  unmeasurable between the tied pair, and the estimator's behaviour at a
  tie need not resemble its behaviour with a small non-zero gap. The same
  two shifts are applied to the asymmetric baseline; the run asserts that
  every asymmetric condition has a unique analytic minimum.
    asym_baseline / asym_shift_coupling / asym_shift_noisecorr
Both shifts are plausible for a drug that alters connectivity; they load on
different entries of the 4x4 covariance, so they are checked separately.
Each shift is compared with the baseline of its own family.

Window lengths: 30 (primary), 60 (load-bearing robustness), 840 (full-run
global fit, as reference).

Non-stationary conditions (pre-registered in manuscript/analysis_record.md, Primary B, revised
12 Sep 2026 before implementation). Every stationary cell above measures
recovery of a CONSTANT true value; the DMT case is a covariance change
partway through the run, which the global fit cannot detect by
construction. Each non-stationary run is a staircase of 28 rating bins x
30 TRs = 840 TRs with one stationary VAR(1) regime per bin:
theta_b = theta_base + f_b (theta_shift - theta_base), theta = c for the
coupling type and theta = q for the noise-correlation type, base =
asym_baseline, shift = asym_shift_<type>.
  nonstat_step_*   f_b = 0 for bins 1-8, 1 for bins 9-28 (switch at TR 240,
                   a window boundary at W = 30 and W = 60).
  nonstat_decay_*  f_b = 0 for bins 1-8, then the 14-subject mean DMT
                   intensity curve normalised to its peak (INTENSITY_SCALE,
                   literals so this script still touches no data file).
Truth per window: at W = 30 the stationary analytic atoms of the bin's
(A_b, Q_b); at W = 60 the analytic atoms of the equal-weight mixture of
the two bins' 4x4 lag covariances; the global fit is read against the
regime values, the sample-weighted mean of the per-bin analytic sts, and
the analytic sts of the 28-bin mixture covariance (its N -> inf limit).
Transients after a regime change are not burned in: they are estimator
error and are reported as such.
Tracking criteria (fixed before the run; manuscript/analysis_record.md, Primary B). The pooled
whole-brain mean is emulated by averaging M replicate runs drawn with
replacement, M = 14 subjects x C(n_eff, 2) with n_eff the participation
ratio of the placebo 115-region correlation matrix: M_DECIDE = (1338, 742)
from ts_gsr (n_eff 14.3, primary stream) and ts_demean (10.8, conservative
sensitivity); a pass is required at both. M_SENS = (151,) is reported only.
  Tier 1, adjacent-pair tracking: S = mean over N_BOOT draws of the
  fraction of adjacent DECAY window pairs (W = 30: windows 10..28; W = 60:
  windows 5..14) whose pooled estimated sts difference has the true sign.
  Chance is 0.5.
  Tier 2, full-decay tracking: R = mean over draws of the Spearman rank
  correlation between the pooled sts per decay window and the intensity
  scale per window, sign-corrected by the Spearman correlation of the
  analytic truth with intensity. Chance is 0.
PASS at a tier requires the statistic >= PASS_THRESHOLD = 0.80 at W = 60
for both decay conditions at both M_DECIDE values. The ordering of
outcomes (tier 1, tier 2, then step contrast + methods) and the reasoning
for 0.80 (raised from an initially proposed 0.75) are in manuscript/analysis_record.md.
Bootstrap caveat (recorded before any verdict): M is drawn with
replacement from N_RUNS = 2000, and M_DECIDE / N_RUNS = 0.67 and 0.37, so
every draw is centred on the same N_RUNS-run sample mean, whose own SE is
sqrt(M / N_RUNS) = 0.82 / 0.61 of the pooled SD. The bootstrap spread is
therefore resampling variability around a fixed centre, not the
variability of fresh pools of M units. Alongside the bootstrap S, the
per-pair correct-sign probability is computed analytically as
Phi(sign(true) * d_hat / SD_pooled) under approximate normality of the
pooled mean, with an interval from d_hat +/- 1.96 SE(d_hat), and
S_analytic = its mean over decay pairs. Where the two differ materially
the analytic value is the one to trust (no resampling noise, no
discretisation at 0/1, the centring assumption explicit). If the
analytic interval of S, or the bootstrap range of R, straddles the
threshold in any deciding cell the verdict is UNDETERMINED and the run is
repeated with --n-runs 20000 before a tier is assigned.

Reported per (condition, window, atom):
  analytic value, mean estimate, bias (= mean - analytic) with 95% CI, SD of
  the estimate across windows (the variance term);
  the same bias with every MMI min-selection forced to its analytic choice
  ("oracle selection": identical fitted entropies, selection decided by the
  true MIs instead of the window's). bias - bias_oracle is the SELECTION
  component of the bias (the discrete min-over-noisy-candidates error); the
  remainder is the entropy-estimation (log-det) component. The analytic
  log-det correction named in the pre-registered decision tree (manuscript/analysis_record.md,
  Primary B) can only address the second, so the split says how much of the
  bias is correctable in principle;
  the fraction of windows in which the rtr min-selection picked an MI whose
  analytic value is NOT the analytic minimum, and the fraction in which ANY
  of the seven MMI min-selections (rtr + six redundancies) did so. Picks
  between analytically tied MIs are not errors and are not counted.
And per (shift, window, atom): the DIFFERENTIAL bias, bias(shift) -
bias(baseline), with 95% CI, next to the true between-condition difference
in the atom — so bias magnitude can be read against effect magnitude — and
the same split into oracle-selection and selection components.

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
from scipy.stats import norm, rankdata

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

# VAR(1) parameters: a = (a1, a2) diagonal of A, c = (c12, c21) off-diagonal
# of A, q = innovation correlation, s = (s1, s2) innovation SDs. Stability
# (spectral radius of A < 1) is asserted. The implied stationary lag-1
# autocorrelations (~0.4-0.7) and pairwise correlations (~0.3-0.7) are
# printed at run time; they sit in the range of preprocessed fMRI at
# TR = 2 s. All values fixed before their first run.
CONDITIONS = {
    # symmetric family — first run 12 Sep 2026 (git e01c836); unchanged
    "baseline":             dict(a=(0.50, 0.50), c=(0.10, 0.10), q=0.20, s=(1.0, 1.0)),
    "shift_coupling":       dict(a=(0.50, 0.50), c=(0.30, 0.30), q=0.20, s=(1.0, 1.0)),
    "shift_noisecorr":      dict(a=(0.50, 0.50), c=(0.10, 0.10), q=0.60, s=(1.0, 1.0)),
    # asymmetric family — added 12 Sep 2026, before any windowed real-data result
    "asym_baseline":        dict(a=(0.55, 0.40), c=(0.15, 0.05), q=0.20, s=(1.0, 1.4)),
    "asym_shift_coupling":  dict(a=(0.55, 0.40), c=(0.35, 0.20), q=0.20, s=(1.0, 1.4)),
    "asym_shift_noisecorr": dict(a=(0.55, 0.40), c=(0.15, 0.05), q=0.60, s=(1.0, 1.4)),
}
# each shift is read against the baseline of its own family
BASELINE_OF = {
    "shift_coupling": "baseline",
    "shift_noisecorr": "baseline",
    "asym_shift_coupling": "asym_baseline",
    "asym_shift_noisecorr": "asym_baseline",
}
# conditions that must have a unique analytic rtr minimum (the point of the
# asymmetric family); the run stops if any of them is tied
MUST_BE_UNTIED = ("asym_baseline", "asym_shift_coupling", "asym_shift_noisecorr")

# AR-shift family — added 13 Sep 2026 AFTER the Primary B ts_gsr W=60 and W=30
# real-data results existed (recorded in manuscript/analysis_record.md), to test the shrinkage
# model on the covariance-change type the real data showed. Kept out of
# CONDITIONS so the stationary tables are unchanged. Parameters fixed before
# the run: a = 0.87 is the measured regional lag-1 autocorrelation on ts_gsr
# (pooled mean 0.867); c and q give pairwise corr(x,y) = 0.197 against the
# measured mean |r| = 0.195; asymmetric so no MMI candidate ties; the shift is
# a -> a - 0.0085 with c, q, s held fixed, chosen so the true sts step
# (~ -0.056) is comparable to the asym coupling step (-0.0562). Implied
# baseline: autocorr (0.877, 0.871), sts 1.384, rtr 0.016, spectral radius
# 0.886 (the 0.75 transient bound does not hold here; see max_radius).
AR_DELTA = 0.0085
AR_CONDITIONS = {
    "ar_baseline": dict(a=(0.87, 0.87), c=(0.025, 0.01), q=0.05, s=(1.0, 1.4)),
    "ar_shift_a":  dict(a=(0.87 - AR_DELTA, 0.87 - AR_DELTA), c=(0.025, 0.01), q=0.05, s=(1.0, 1.4)),
}
ALL_PARAMS = {**CONDITIONS, **AR_CONDITIONS}

# ---- non-stationary conditions (pre-registered; see module docstring) ----
N_BINS, BIN_TRS = 28, 30                  # 28 rating bins x 30 TRs = 840
N_RUNS = 2000                             # replicate 840-TR runs per condition
NONSTAT_WINDOWS = (30, 60)                # windowed estimators; 840 = global
# 14-subject mean DMT intensity per rating bin / its peak (bin 10), bins
# 9..28; from intensity_ratings.mat `dmt_intensity`, computed 12 Sep 2026
# and fixed here as literals. Bins 1-8 are forced to 0 (baseline regime).
INTENSITY_SCALE = np.array(
    [0.0] * 8 +
    [0.9154, 1.0000, 0.9385, 0.8462, 0.7308, 0.6308, 0.5462, 0.4769, 0.4000,
     0.3462, 0.2615, 0.2154, 0.1846, 0.1462, 0.1308, 0.1077, 0.0846, 0.0692,
     0.0769, 0.0462])
STEP_SCALE = np.array([0.0] * 8 + [1.0] * 20)
assert INTENSITY_SCALE.size == N_BINS and STEP_SCALE.size == N_BINS
NONSTAT_CONDITIONS = {
    "nonstat_step_coupling":   dict(shift="asym_shift_coupling",  param="c", f=STEP_SCALE),
    "nonstat_step_noisecorr":  dict(shift="asym_shift_noisecorr", param="q", f=STEP_SCALE),
    "nonstat_decay_coupling":  dict(shift="asym_shift_coupling",  param="c", f=INTENSITY_SCALE),
    "nonstat_decay_noisecorr": dict(shift="asym_shift_noisecorr", param="q", f=INTENSITY_SCALE),
    # AR-shift step (13 Sep 2026): base and radius bound differ from the others
    "nonstat_step_ar":         dict(shift="ar_shift_a", param="a", f=STEP_SCALE,
                                    base="ar_baseline", max_radius=0.90),
}
NONSTAT_BASE = "asym_baseline"
SWITCH_BIN = 8                            # bins 0..7 pre-switch (1-based 1-8)
# adjacent window pairs inside the decay, as (first window index, 0-based)
DECAY_PAIRS = {30: list(range(9, 27)),    # windows 10->11 .. 27->28 (18 pairs)
               60: list(range(4, 13))}    # windows 5->6 .. 13->14 (9 pairs)
# effective independent pair-windows in the pooled whole-brain mean
M_DECIDE = (1338, 742)                    # ts_gsr primary; ts_demean sensitivity; both must pass
M_SENS = (151,)                           # 14 x n_eff (one unit per component); report only
N_BOOT = 2000                             # bootstrap draws of M runs each
PASS_THRESHOLD = 0.80                     # on S (tier 1) and R (tier 2) at W = 60;
                                          # 0.75 first proposed, raised before the run
# decay windows (0-based) for the full-decay Spearman: bins 10..28
DECAY_WINDOWS = {30: list(range(9, 28)), 60: list(range(4, 14))}

RESULTS = Path("results")
RESULTS.mkdir(exist_ok=True)
OUT_CSV = RESULTS / "bias_check.csv"
OUT_DIFF_CSV = RESULTS / "bias_check_differential.csv"
OUT_NS_CSV = RESULTS / "bias_check_nonstat.csv"            # per window
OUT_NS_GLOBAL_CSV = RESULTS / "bias_check_nonstat_global.csv"
OUT_NS_TRACK_CSV = RESULTS / "bias_check_nonstat_tracking.csv"   # per pair
OUT_NS_CRIT_CSV = RESULTS / "bias_check_nonstat_criterion.csv"

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

# The seven MMI min-selections. rtr = argmin over the four single-target
# MIs (double_redundacy_mmi); each redundancy R = min of a pair of MIs
# (redundancy_mmi). Pairs must match _get_redundancy_four_vec exactly.
_RTR_MIS = ("I_xta", "I_xtb", "I_yta", "I_ytb")
_R_PAIRS = {
    "R_xyta": ("I_xta", "I_yta"),
    "R_xytb": ("I_xtb", "I_ytb"),
    "R_xytab": ("I_xtab", "I_ytab"),
    "R_abtx": ("I_xta", "I_xtb"),
    "R_abty": ("I_yta", "I_ytb"),
    "R_abtxy": ("I_xyta", "I_xytb"),
}


# ---------------------------------------------------------------- model
def var1_matrices(a, c, q, s):
    A = np.array([[a[0], c[0]], [c[1], a[1]]])
    Q = np.array([[s[0] ** 2, q * s[0] * s[1]], [q * s[0] * s[1], s[1] ** 2]])
    eig = np.max(np.abs(np.linalg.eigvals(A)))
    assert eig < 1, f"VAR(1) unstable: spectral radius {eig:.3f}"
    return A, Q


def joint_lag_cov(A, Q, tau):
    """True covariance of (x_t, y_t, x_t+tau, y_t+tau) at stationarity.

    Cov(z_t+tau, z_t) = A^tau S0 for an asymmetric A; the block placement
    below was checked against a 2e6-sample simulation of an asymmetric
    condition on 12 Sep 2026 (max abs deviation 6e-3 vs 0.63 for the
    transposed placement), and independently a second time the same day
    against a 4e6-sample asymmetric simulation (max deviation 0.0006 as
    written vs 0.041 transposed).
    """
    S0 = solve_discrete_lyapunov(A, Q)             # S0 = A S0 A' + Q
    Atau = np.linalg.matrix_power(A, tau)
    cross = Atau @ S0                              # Cov(z_t+tau, z_t)
    return np.block([[S0, cross.T], [cross, S0]])


def implied_correlations(S4):
    d = np.sqrt(np.diag(S4))
    C = S4 / np.outer(d, d)
    return dict(auto_x=C[_P1, _T1], auto_y=C[_P2, _T2], xy=C[_P1, _P2],
                x_to_y=C[_P1, _T2], y_to_x=C[_P2, _T1])


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


def _argmin_mean(I_res, keys):
    return keys[int(np.argmin([np.mean(I_res[k]) for k in keys]))]


def selection_flips(calc_res, true_I, tol=1e-9):
    """(rtr_wrong, any_wrong) for one window.

    A selection is wrong if the MI it picked has an ANALYTIC value above the
    analytic minimum of its candidate set. Picking between analytically tied
    candidates (e.g. I_xtb == I_yta under symmetric A, Q) is not an error.
    """
    I = calc_res["I_res"]

    def wrong(keys):
        picked = _argmin_mean(I, keys)
        return (true_I[picked] - min(true_I[k] for k in keys)) > tol

    rtr_wrong = wrong(_RTR_MIS)
    any_wrong = rtr_wrong or any(wrong(pair) for pair in _R_PAIRS.values())
    return rtr_wrong, any_wrong


def oracle_atoms(calc_res, true_I):
    """Atoms from this window's fitted MIs with every MMI min-selection
    forced to the analytically minimal candidate (ties -> first key).

    Isolates the entropy-estimation component of the bias from the
    selection component. Uses phyid's own lattice inversion.
    """
    I = calc_res["I_res"]
    R = {name: I[min(pair, key=lambda k: true_I[k])]
         for name, pair in _R_PAIRS.items()}
    rtr = I[min(_RTR_MIS, key=lambda k: true_I[k])]
    return _get_atoms_four_vec({"I_res": I, "R_res": R, "rtr": rtr})


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


def staircase_params(shift, param, f, base_name=NONSTAT_BASE):
    """Per-bin VAR(1) parameter dicts, theta_b = base + f_b (shift - base)."""
    base, top = ALL_PARAMS[base_name], ALL_PARAMS[shift]
    out = []
    for fb in f:
        p = dict(base)
        if param == "c":
            p["c"] = tuple(b + fb * (t - b) for b, t in zip(base["c"], top["c"]))
        elif param == "q":
            p["q"] = base["q"] + fb * (top["q"] - base["q"])
        elif param == "a":
            p["a"] = tuple(b + fb * (t - b) for b, t in zip(base["a"], top["a"]))
        else:
            raise ValueError(param)
        out.append(p)
    return out


def simulate_staircase(params_per_bin, n_runs, rng):
    """(n_runs, 2, N_BINS*BIN_TRS) draws; burn-in under the bin-1 regime,
    then one regime per bin with NO burn-in after a change (transients are
    part of what is measured)."""
    mats = [var1_matrices(**p) for p in params_per_bin]
    chols = [np.linalg.cholesky(Q) for _, Q in mats]
    total = N_BINS * BIN_TRS + BURN_IN
    z = np.zeros((n_runs, 2, total))
    w = rng.standard_normal((n_runs, 2, total))
    for t in range(1, total):
        b = max(0, (t - BURN_IN) // BIN_TRS)
        A, L = mats[b][0], chols[b]
        z[:, :, t] = (np.einsum("ij,nj->ni", A, z[:, :, t - 1])
                      + np.einsum("ij,nj->ni", L, w[:, :, t]))
    return z[:, :, BURN_IN:]


def _window_truths(S4_bins, W):
    """Analytic atoms per window: bin value at W=30, equal-weight mixture of
    the covered bins' 4x4 lag covariances at larger W."""
    per = W // BIN_TRS
    truths = []
    for w in range(N_BINS // per):
        S = np.mean(S4_bins[w * per:(w + 1) * per], axis=0)
        truths.append(analytic_atoms(S, REDUNDANCY)[0])
    return truths


def _spearman(a, b):
    ra, rb = rankdata(a), rankdata(b)
    return float(np.corrcoef(ra, rb)[0, 1])


def _pooled_tracking(est, true, pairs, dwin, f_win, M, n_boot, rng):
    """est: (n_runs, n_windows) sts estimates; true: (n_windows,) truth;
    pairs: first index of each adjacent decay pair; dwin: decay window
    indices; f_win: intensity scale per window.
    Returns (S per draw, per-pair correct-sign probability, sign-corrected
    Spearman per draw, Spearman of truth vs intensity)."""
    n_runs = est.shape[0]
    true_sign = np.sign(np.array([true[i + 1] - true[i] for i in pairs]))
    assert np.all(true_sign != 0), "a decay pair has zero true difference"
    rho_true = _spearman(np.asarray(true)[dwin], f_win[dwin])
    hits = np.empty((n_boot, len(pairs)), bool)
    rho = np.empty(n_boot)
    for b in range(n_boot):
        pooled = est[rng.integers(0, n_runs, M)].mean(0)
        d = np.array([pooled[i + 1] - pooled[i] for i in pairs])
        hits[b] = np.sign(d) == true_sign
        rho[b] = np.sign(rho_true) * _spearman(pooled[dwin], f_win[dwin])
    # analytic counterpart: pooled mean of M fresh units ~ N(mu, v/M);
    # mu is known only through the n_runs sample mean d_hat, SE sqrt(v/n_runs)
    d_hat = np.array([est[:, i + 1].mean() - est[:, i].mean() for i in pairs])
    v = np.array([est[:, i + 1].var(ddof=1) + est[:, i].var(ddof=1) for i in pairs])
    sd_pooled = np.sqrt(v / M)
    se_dhat = np.sqrt(v / n_runs)
    p_an = norm.cdf(true_sign * d_hat / sd_pooled)
    p_lo = norm.cdf(true_sign * (d_hat - true_sign * 1.96 * se_dhat) / sd_pooled)
    p_hi = norm.cdf(true_sign * (d_hat + true_sign * 1.96 * se_dhat) / sd_pooled)
    analytic = dict(d_hat=d_hat, se_dhat=se_dhat, sd_pooled=sd_pooled,
                    p=p_an, p_lo=p_lo, p_hi=p_hi)
    return hits.mean(1), hits.mean(0), rho, rho_true, analytic


def run_nonstat(rng, t0):
    """Non-stationary staircase conditions; returns four row lists."""
    ns_rows, glob_rows, track_rows, crit_rows = [], [], [], []
    for cond, spec in NONSTAT_CONDITIONS.items():
        params = staircase_params(spec["shift"], spec["param"], spec["f"],
                                  spec.get("base", NONSTAT_BASE))
        S4_bins = []
        for b, p in enumerate(params):
            A, Q = var1_matrices(**p)
            assert np.max(np.abs(np.linalg.eigvals(A))) <= spec.get("max_radius", 0.76), \
                "transient claim in manuscript/analysis_record.md (0.75 bound; AR family uses its own bound)"
            S4 = joint_lag_cov(A, Q, TAU)
            _, calc = analytic_atoms(S4, REDUNDANCY)
            mis = np.array([float(calc["I_res"][k][0]) for k in _RTR_MIS])
            if int(np.sum(np.abs(mis - mis.min()) < 1e-9)) != 1:
                raise RuntimeError(f"{cond} bin {b + 1}: tied analytic rtr minimum")
            S4_bins.append(S4)
        S4_bins = np.array(S4_bins)
        truths = {W: _window_truths(S4_bins, W) for W in NONSTAT_WINDOWS}
        bin_sts = np.array([t["sts"] for t in truths[30]])
        mix_atoms, _ = analytic_atoms(S4_bins.mean(0), REDUNDANCY)
        print(f"[{cond}] true sts per bin: "
              + " ".join(f"{v:.3f}" for v in bin_sts))

        z = simulate_staircase(params, N_RUNS, rng)          # (N_RUNS, 2, 840)
        est = {W: {a: np.empty((N_RUNS, N_BINS * BIN_TRS // W)) for a in ATOMS}
               for W in NONSTAT_WINDOWS}
        est_g = {a: np.empty(N_RUNS) for a in ATOMS}
        for n in range(N_RUNS):
            x, y = z[n, 0], z[n, 1]
            for W in NONSTAT_WINDOWS:
                for w in range(N_BINS * BIN_TRS // W):
                    sl = slice(w * W, (w + 1) * W)
                    atoms, _ = calc_PhiID(x[sl], y[sl], tau=TAU, kind=KIND,
                                          redundancy=REDUNDANCY)
                    for a in ATOMS:
                        est[W][a][n, w] = np.mean(atoms[a])
            atoms, _ = calc_PhiID(x, y, tau=TAU, kind=KIND, redundancy=REDUNDANCY)
            for a in ATOMS:
                est_g[a][n] = np.mean(atoms[a])
        print(f"    simulated + estimated {N_RUNS} runs ({time.time() - t0:.0f}s)")

        # per-window rows and step recovery
        for W in NONSTAT_WINDOWS:
            nw = est[W]["sts"].shape[1]
            per = W // BIN_TRS
            for a in ATOMS:
                e = est[W][a]
                for w in range(nw):
                    tr = truths[W][w][a]
                    se = e[:, w].std(ddof=1) / np.sqrt(N_RUNS)
                    ns_rows.append(dict(
                        condition=cond, window=W, window_index=w + 1, atom=a,
                        bins_covered=f"{w * per + 1}-{(w + 1) * per}",
                        f_first_bin=float(spec["f"][w * per]),
                        analytic=tr, est_mean=e[:, w].mean(),
                        bias=e[:, w].mean() - tr,
                        bias_ci_lo=e[:, w].mean() - tr - 1.96 * se,
                        bias_ci_hi=e[:, w].mean() - tr + 1.96 * se,
                        est_sd=e[:, w].std(ddof=1)))
            pre = SWITCH_BIN // per
            e = est[W]["sts"]
            tr = np.array([t["sts"] for t in truths[W]])
            step_true = tr[pre:].mean() - tr[:pre].mean()
            step_est = e[:, pre:].mean() - e[:, :pre].mean()
            print(f"    W={W:3d} sts pre/post-switch means: true "
                  f"{tr[:pre].mean():.4f}->{tr[pre:].mean():.4f} (Δ {step_true:+.4f})  "
                  f"est {e[:, :pre].mean():.4f}->{e[:, pre:].mean():.4f} "
                  f"(Δ {step_est:+.4f}, {100 * step_est / step_true:.0f}% of true)")

        # global fit vs its reference points
        n_pre, n_post = SWITCH_BIN, N_BINS - SWITCH_BIN
        for a in ATOMS:
            g = est_g[a]
            glob_rows.append(dict(
                condition=cond, atom=a,
                global_est_mean=g.mean(), global_est_sd=g.std(ddof=1),
                global_est_ci_lo=g.mean() - 1.96 * g.std(ddof=1) / np.sqrt(N_RUNS),
                global_est_ci_hi=g.mean() + 1.96 * g.std(ddof=1) / np.sqrt(N_RUNS),
                regime_pre=truths[30][0][a],
                regime_peak=truths[30][int(np.argmax(spec["f"]))][a],
                weighted_mean_of_bin_truths=float(
                    np.mean([t[a] for t in truths[30]])),
                mixture_cov_truth=mix_atoms[a],
                n_pre_bins=n_pre, n_post_bins=n_post))
        print(f"    global fit sts: est {est_g['sts'].mean():.4f}  "
              f"regimes pre {truths[30][0]['sts']:.4f} / peak "
              f"{truths[30][int(np.argmax(spec['f']))]['sts']:.4f}  "
              f"weighted-mean truth {bin_sts.mean():.4f}  "
              f"mixture-cov truth {mix_atoms['sts']:.4f}")

        # tracking criterion: decay conditions only (a step has no decay pairs)
        for W in (NONSTAT_WINDOWS if "decay" in cond else ()):
            pairs = DECAY_PAIRS[W]
            tr = [t["sts"] for t in truths[W]]
            e = est[W]["sts"]
            per = W // BIN_TRS
            f_win = spec["f"].reshape(-1, per).mean(1)   # intensity per window
            for M in M_DECIDE + M_SENS:
                S_draws, p_pair, R_draws, rho_true, an = _pooled_tracking(
                    e, tr, pairs, DECAY_WINDOWS[W], f_win, M, N_BOOT, rng)
                for i, (w0, pc) in enumerate(zip(pairs, p_pair)):
                    d_true = tr[w0 + 1] - tr[w0]
                    track_rows.append(dict(
                        condition=cond, window=W, M=M,
                        pair=f"{w0 + 1}->{w0 + 2}", true_diff=d_true,
                        est_diff_mean=float(an["d_hat"][i]),
                        est_diff_se=float(an["se_dhat"][i]),
                        est_diff_sd_pooled=float(an["sd_pooled"][i]),
                        p_correct_sign_boot=float(pc),
                        p_correct_sign_analytic=float(an["p"][i]),
                        p_analytic_lo=float(an["p_lo"][i]),
                        p_analytic_hi=float(an["p_hi"][i])))
                decides = (M in M_DECIDE) and (W == 60)
                S, R = float(S_draws.mean()), float(R_draws.mean())
                S_an = float(an["p"].mean())
                S_an_lo, S_an_hi = float(an["p_lo"].mean()), float(an["p_hi"].mean())
                R_lo, R_hi = (float(np.percentile(R_draws, 2.5)),
                              float(np.percentile(R_draws, 97.5)))
                # deciding statistic for tier 1 is the analytic S (see docstring)
                undetermined = int(decides and (
                    (S_an_lo < PASS_THRESHOLD <= S_an_hi) or (R_lo < PASS_THRESHOLD <= R_hi)))
                crit_rows.append(dict(
                    condition=cond, window=W, M=M, n_pairs=len(pairs),
                    n_decay_windows=len(DECAY_WINDOWS[W]),
                    S_boot=S, S_boot_lo=float(np.percentile(S_draws, 2.5)),
                    S_boot_hi=float(np.percentile(S_draws, 97.5)),
                    S_analytic=S_an, S_analytic_lo=S_an_lo, S_analytic_hi=S_an_hi,
                    R=R, R_lo=R_lo, R_hi=R_hi,
                    rho_truth_vs_intensity=rho_true,
                    threshold=PASS_THRESHOLD, decides=int(decides),
                    passed_adjacent=int(S_an >= PASS_THRESHOLD),
                    passed_adjacent_boot=int(S >= PASS_THRESHOLD),
                    passed_fulldecay=int(R >= PASS_THRESHOLD),
                    undetermined=undetermined))
                if M in M_DECIDE:
                    print(f"    W={W:3d} M={M:4d}: S_boot={S:.3f} "
                          f"[{np.percentile(S_draws, 2.5):.3f},"
                          f"{np.percentile(S_draws, 97.5):.3f}]  S_analytic={S_an:.3f} "
                          f"[{S_an_lo:.3f},{S_an_hi:.3f}] over {len(pairs)} decay pairs;  "
                          f"R={R:.3f} [{R_lo:.3f},{R_hi:.3f}] over "
                          f"{len(DECAY_WINDOWS[W])} windows (truth rho={rho_true:+.2f})"
                          + (f"  -> adjacent {'PASS' if S_an >= PASS_THRESHOLD else 'FAIL'}, "
                             f"full-decay {'PASS' if R >= PASS_THRESHOLD else 'FAIL'}"
                             + ("  [UNDETERMINED: interval straddles threshold]"
                                if undetermined else "")
                             if decides else ""))
    return ns_rows, glob_rows, track_rows, crit_rows


# ---------------------------------------------------------------- run
def main():
    t0 = time.time()
    rows = []          # per (condition, window, atom)
    est_store = {}     # (condition, W, atom) -> per-window estimates
    orc_store = {}     # (condition, W, atom) -> per-window oracle-selection estimates
    true_store = {}    # (condition, atom) -> analytic value

    for cond, p in CONDITIONS.items():
        A, Q = var1_matrices(**p)
        S4 = joint_lag_cov(A, Q, TAU)
        true_atoms, true_calc = analytic_atoms(S4, REDUNDANCY)
        true_I = {k: float(v[0]) for k, v in true_calc["I_res"].items()}
        true_mis = np.array([true_I[k] for k in _RTR_MIS])
        n_tied = int(np.sum(np.abs(true_mis - true_mis.min()) < 1e-9))
        if cond in MUST_BE_UNTIED and n_tied != 1:
            raise RuntimeError(
                f"{cond}: {n_tied} of 4 single-target MIs tied at the analytic "
                "minimum; the asymmetric family exists to avoid this. Fix the "
                "parameters before running.")
        for atom in ATOMS:
            true_store[(cond, atom)] = true_atoms[atom]
        corr = implied_correlations(S4)
        print(f"[{cond}] a={p['a']} c={p['c']} q={p['q']} s={p['s']}  "
              f"autocorr=({corr['auto_x']:.2f},{corr['auto_y']:.2f}) "
              f"corr(x,y)={corr['xy']:.2f}")
        print(f"    analytic sts={true_atoms['sts']:.4f} rtr={true_atoms['rtr']:.4f}  "
              f"single-target MIs "
              + " ".join(f"{k}={true_I[k]:.4f}" for k in _RTR_MIS)
              + f"  ({n_tied} of 4 tied at the min)")

        for W in WINDOWS:
            z = simulate(A, Q, W, N_WINDOWS, rng)   # (N_WINDOWS, 2, W)
            est = {atom: np.empty(N_WINDOWS) for atom in ATOMS}
            orc = {atom: np.empty(N_WINDOWS) for atom in ATOMS}
            rtr_flips = any_flips = 0
            for n in range(N_WINDOWS):
                atoms, calc = calc_PhiID(z[n, 0], z[n, 1], tau=TAU,
                                         kind=KIND, redundancy=REDUNDANCY)
                o_atoms = oracle_atoms(calc, true_I)
                for atom in ATOMS:
                    est[atom][n] = np.mean(atoms[atom])   # window-mean local atom
                    orc[atom][n] = np.mean(o_atoms[atom])
                r_w, a_w = selection_flips(calc, true_I)
                rtr_flips += r_w
                any_flips += a_w
            rtr_flip_frac = rtr_flips / N_WINDOWS
            any_flip_frac = any_flips / N_WINDOWS

            for atom in ATOMS:
                e, o = est[atom], orc[atom]
                est_store[(cond, W, atom)] = e
                orc_store[(cond, W, atom)] = o
                truth = true_store[(cond, atom)]
                bias = e.mean() - truth
                bias_o = o.mean() - truth
                se = e.std(ddof=1) / np.sqrt(N_WINDOWS)
                rows.append(dict(
                    condition=cond, window=W, atom=atom, n=N_WINDOWS,
                    analytic=truth, est_mean=e.mean(), bias=bias,
                    bias_ci_lo=bias - 1.96 * se, bias_ci_hi=bias + 1.96 * se,
                    est_sd=e.std(ddof=1),
                    bias_oracle_sel=bias_o, sel_bias=bias - bias_o,
                    rtr_selection_flip_frac=rtr_flip_frac,
                    any_selection_flip_frac=any_flip_frac,
                ))
            print(f"    W={W:3d}  "
                  + "  ".join(
                      f"{atom}: bias={est[atom].mean() - true_store[(cond, atom)]:+.4f} "
                      f"(oracle-sel {orc[atom].mean() - true_store[(cond, atom)]:+.4f}) "
                      f"sd={est[atom].std(ddof=1):.4f}" for atom in ATOMS)
                  + f"  flip rtr={rtr_flip_frac:.3f} any={any_flip_frac:.3f}"
                  + f"  ({time.time() - t0:.0f}s)")

    # ------------------------------------------------ differential bias
    diff_rows = []
    for cond, base in BASELINE_OF.items():
        for W in WINDOWS:
            for atom in ATOMS:
                e_s, e_b = est_store[(cond, W, atom)], est_store[(base, W, atom)]
                o_s, o_b = orc_store[(cond, W, atom)], orc_store[(base, W, atom)]
                true_diff = true_store[(cond, atom)] - true_store[(base, atom)]
                est_diff = e_s.mean() - e_b.mean()
                dbias = est_diff - true_diff
                dbias_o = (o_s.mean() - o_b.mean()) - true_diff
                # windows are independent across conditions -> variances add
                se = np.sqrt(e_s.var(ddof=1) / e_s.size + e_b.var(ddof=1) / e_b.size)
                diff_rows.append(dict(
                    shift=cond, baseline=base, window=W, atom=atom,
                    true_diff=true_diff, est_diff=est_diff,
                    diff_bias=dbias,
                    diff_bias_ci_lo=dbias - 1.96 * se,
                    diff_bias_ci_hi=dbias + 1.96 * se,
                    # bias as a fraction of the true effect it could mimic
                    diff_bias_over_true_diff=(dbias / true_diff
                                              if true_diff != 0 else np.nan),
                    diff_bias_oracle_sel=dbias_o,
                    diff_sel_bias=dbias - dbias_o,
                ))

    # ------------------------------------------------ provenance + save
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
        if subprocess.check_output(
            ["git", "status", "--porcelain", "--", "scripts", "manuscript/analysis_record.md"],
            text=True, stderr=subprocess.DEVNULL,
        ).strip():
            sha += "-dirty"
    except (subprocess.CalledProcessError, FileNotFoundError):
        sha = "nogit"
    header = (f"# script=02_bias_check.py tau={TAU} kind={KIND} "
              f"redundancy={REDUNDANCY} n_windows={N_WINDOWS} "
              f"burn_in={BURN_IN} seed={SEED} git={sha} "
              f"n_runs={N_RUNS} n_boot={N_BOOT} m_decide={'/'.join(map(str, M_DECIDE))} "
              f"threshold={PASS_THRESHOLD}\n")

    def write_csv(path, rows):
        if not rows:
            print(f"(nothing to write for {path.name})")
            return
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

    # ------------------------------------------------ non-stationary
    print("\nNON-STATIONARY conditions")
    ns_rows, glob_rows, track_rows, crit_rows = run_nonstat(rng, t0)
    write_csv(OUT_NS_CSV, ns_rows)
    write_csv(OUT_NS_GLOBAL_CSV, glob_rows)
    write_csv(OUT_NS_TRACK_CSV, track_rows)
    write_csv(OUT_NS_CRIT_CSV, crit_rows)

    # ------------------------------------------------ summary
    print("\nBIAS (estimate - analytic), 95% CI, SD across windows; "
          "oracle-sel = bias with MMI selections forced to the analytic "
          "choice; flip = fraction of windows with a wrong rtr / any selection")
    print(f"{'condition':21s} {'W':>4s} {'atom':4s} {'analytic':>9s} "
          f"{'bias':>8s} {'[CI]':>18s} {'sd':>7s} {'oracle':>8s} "
          f"{'flip-rtr':>8s} {'flip-any':>8s}")
    for r in rows:
        print(f"{r['condition']:21s} {r['window']:4d} {r['atom']:4s} "
              f"{r['analytic']:9.4f} {r['bias']:+8.4f} "
              f"[{r['bias_ci_lo']:+7.4f},{r['bias_ci_hi']:+7.4f}] "
              f"{r['est_sd']:7.4f} {r['bias_oracle_sel']:+8.4f} "
              f"{r['rtr_selection_flip_frac']:8.3f} "
              f"{r['any_selection_flip_frac']:8.3f}")

    print("\nDIFFERENTIAL BIAS  bias(shift) - bias(baseline)  vs  true effect")
    print(f"{'shift':21s} {'W':>4s} {'atom':4s} {'true_diff':>9s} "
          f"{'est_diff':>9s} {'diff_bias':>10s} {'[CI]':>18s} {'bias/eff':>9s} "
          f"{'oracle':>8s}")
    for r in diff_rows:
        print(f"{r['shift']:21s} {r['window']:4d} {r['atom']:4s} "
              f"{r['true_diff']:+9.4f} {r['est_diff']:+9.4f} "
              f"{r['diff_bias']:+10.4f} "
              f"[{r['diff_bias_ci_lo']:+7.4f},{r['diff_bias_ci_hi']:+7.4f}] "
              f"{r['diff_bias_over_true_diff']:+9.3f} "
              f"{r['diff_bias_oracle_sel']:+8.4f}")

    print("\nTRACKING CRITERIA  S = mean fraction of correctly signed adjacent "
          "decay pairs;  R = mean sign-corrected Spearman(pooled sts, intensity) "
          "over decay windows;  pooled mean of M runs")
    for r in crit_rows:
        tag = ("DECIDES" if r["decides"] else "report ") + (
            "  adj " + ("PASS" if r["passed_adjacent"] else "FAIL")
            + "  full " + ("PASS" if r["passed_fulldecay"] else "FAIL")
            + ("  UNDETERMINED" if r["undetermined"] else ""))
        print(f"{r['condition']:24s} W={r['window']:3d} M={r['M']:5d} "
              f"S_boot={r['S_boot']:.3f} S_an={r['S_analytic']:.3f} "
              f"[{r['S_analytic_lo']:.3f},{r['S_analytic_hi']:.3f}]  "
              f"R={r['R']:+.3f} [{r['R_lo']:+.3f},{r['R_hi']:+.3f}]  {tag}")
    deciding = [r for r in crit_rows if r["decides"]]
    if deciding:
        adj = all(r["passed_adjacent"] == 1 for r in deciding)
        full = all(r["passed_fulldecay"] == 1 for r in deciding)
        und = any(r["undetermined"] == 1 for r in deciding)
        gap = max(abs(r["S_boot"] - r["S_analytic"]) for r in deciding)
        tier = ("1: adjacent-pair tracking" if adj else
                "2: full-decay tracking" if full else
                "3: step contrast + methods")
        print(f"\nPRE-REGISTERED VERDICT at W=60, M in {M_DECIDE}, "
              f"threshold {PASS_THRESHOLD}, both decay conditions, tier 1 on "
              f"S_analytic: adjacent-pair {'PASS' if adj else 'FAIL'}; "
              f"full-decay {'PASS' if full else 'FAIL'}  -> outcome tier {tier}"
              + ("\nUNDETERMINED: an interval straddles the threshold in a "
                 "deciding cell; repeat with --n-runs 20000 before assigning a tier."
                 if und else "")
              + f"\nmax |S_boot - S_analytic| over deciding cells: {gap:.3f}"
              f"  (N_RUNS={N_RUNS}, M/N_RUNS = "
              + ", ".join(f"{m / N_RUNS:.2f}" for m in M_DECIDE) + ")")

    print(f"\nwrote {OUT_CSV}\nwrote {OUT_DIFF_CSV}\nwrote {OUT_NS_CSV}\n"
          f"wrote {OUT_NS_GLOBAL_CSV}\nwrote {OUT_NS_TRACK_CSV}\n"
          f"wrote {OUT_NS_CRIT_CSV}")
    print(f"total {time.time() - t0:.1f}s")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--quick", action="store_true",
                    help="smoke test: few windows/runs/draws; requires --out")
    ap.add_argument("--out", type=Path, default=None,
                    help="write CSVs here instead of results/ (required with --quick)")
    ap.add_argument("--n-runs", type=int, default=None,
                    help="replicate runs per non-stationary condition "
                         f"(default {N_RUNS}; the pre-registered UNDETERMINED "
                         "rule repeats with 20000)")
    ap.add_argument("--only-nonstat", default=None, choices=sorted(NONSTAT_CONDITIONS),
                    help="run ONE non-stationary condition only, skipping the "
                         "stationary block (requires --out so results/ tables are untouched)")
    args = ap.parse_args()
    if args.only_nonstat is not None:
        if args.out is None or args.out.resolve() == RESULTS.resolve():
            ap.error("--only-nonstat must write outside results/ (pass --out DIR)")
        NONSTAT_CONDITIONS = {args.only_nonstat: NONSTAT_CONDITIONS[args.only_nonstat]}
        CONDITIONS = {}
        BASELINE_OF = {}
    if args.quick:
        if args.out is None or args.out.resolve() == RESULTS.resolve():
            ap.error("--quick must write outside results/ (pass --out DIR)")
        N_WINDOWS, N_RUNS, N_BOOT = 20, 12, 30
    if args.n_runs is not None:
        N_RUNS = args.n_runs
    if args.out is not None:
        RESULTS = args.out
        RESULTS.mkdir(parents=True, exist_ok=True)
        OUT_CSV = RESULTS / OUT_CSV.name
        OUT_DIFF_CSV = RESULTS / OUT_DIFF_CSV.name
        OUT_NS_CSV = RESULTS / OUT_NS_CSV.name
        OUT_NS_GLOBAL_CSV = RESULTS / OUT_NS_GLOBAL_CSV.name
        OUT_NS_TRACK_CSV = RESULTS / OUT_NS_TRACK_CSV.name
        OUT_NS_CRIT_CSV = RESULTS / OUT_NS_CRIT_CSV.name
    main()
