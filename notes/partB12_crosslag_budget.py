"""
partB12_crosslag_budget.py — the exact budget of the run-level sign(q)-weighted cross-lag deviation on the data
(16 Sep 2026; pre-run entry "The cross-lag budget: pre-run entry, 16 Sep 2026" in manuscript/analysis_record.md,
rules (a)–(f) recorded there before this ran). Definitions and the shared function: notes/rev_crosslag_budget.py.

Per subject and run, both variants: the run-level matrices of every pair (all kept TRs, as partB10), the run-level
matrices after removing each region's mean within each W = 60 window, the window matrices (kept TRs in
[60w, 60(w + 1)), as partB10 section A and partB4_diagnostic build them; every window checked against the saved
diagnostic's xcorr_dev) and the window SDs (ddof = 0); the per-pair weight s = sign of the pair's run-level q in that
run. budget_terms() then gives δ_run, δ_wd, δ_means, δ_within, δ_pool, ε, δ_60 and the window-sign value per pair;
this script averages them over pairs per run and aggregates as partB10 (per subject the mean of the two runs; grand
mean with subject-bootstrap 95 % CI, 10,000 draws, seed 20261120, one set of draws per variant shared with partB13;
exact sign-flip p; count positive; per run type). Checks: δ_run and the window-sign value per run must reproduce
partB10's crosslag_deviation.csv columns signq_weighted_mean_deviation and w60_signq_weighted_mean_deviation; the
identity δ_run = δ_within + δ_pool + δ_means + ε must hold to machine precision.

Printed before the data are loaded: (1) the general form of the shared-slow-component deviation on population
matrices, d(x→y) = q (1 − λ_y)(a_s − a_n), with equal and unequal loadings; (2) the τ = 1 equivalence for the worked
example λ = 0.25, a_s = 0.95, a_n = 0.80: the VAR(1) with A = Γ₁Γ₀⁻¹ that has the same lag-0/lag-1 structure
(coefficient 0.83, coupling 0.03, innovation correlation ≈ 0.093; d = c(1 − q²)), so that every τ = 1 quantity of the
paper coincides for the two.

Outputs: notes/review_results/partB/crosslag_budget_tables.md, crosslag_budget.csv (one row per subject × run ×
variant), crosslag_budget_run.log (via run_all.sh's nstep, or stdout).
Run from the repository root: .venv/bin/python notes/partB12_crosslag_budget.py   (about two minutes)
"""
import subprocess
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import scipy.io as sio

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ATOMS
from rev_crosslag_budget import budget_terms, aggregate, boot_idx_variants, fmt_agg, TERMS, SEED, N_BOOT

REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
OUT = REPO / "notes" / "review_results" / "partB"
OUT.mkdir(parents=True, exist_ok=True)
REGIONS = np.array([r for r in range(116) if r != 20])
CONDITIONS = ("DMT", "PCB")
W = 60
N_WIN = 840 // W

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=REPO).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "notes/*.py", "manuscript/analysis_record.md"],
                               text=True, cwd=REPO).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"


# ------------------------------------------------------------------------------------------ population checks
def common_component_C(lam_x, lam_y, a_s, a_n, loading=+1.0):
    """Population 4 × 4 correlation matrix of [x_t, y_t, x_(t+1), y_(t+1)] for x = √λ_x s + √(1 − λ_x) n_x,
    y = ±√λ_y s + √(1 − λ_y) n_y, with s of lag-1 autocorrelation a_s and independent regional parts of lag-1
    autocorrelation a_n (unit variances)."""
    q = loading * np.sqrt(lam_x * lam_y)
    a_x = lam_x * a_s + (1 - lam_x) * a_n
    a_y = lam_y * a_s + (1 - lam_y) * a_n
    cross = loading * np.sqrt(lam_x * lam_y) * a_s                 # corr(x_t, y_(t+1)) = corr(y_t, x_(t+1))
    return np.array([[1, q, a_x, cross], [q, 1, cross, a_y], [a_x, cross, 1, q], [cross, a_y, q, 1]], float)


def var1_from_lag01(C):
    """The VAR(1) with the lag-0/lag-1 structure of a 4 × 4 matrix of [x_t, y_t, x_(t+1), y_(t+1)]:
    Γ₀ = C[:2, :2], Γ₁ = C[2:, :2] (rows x_(t+1), y_(t+1); columns x_t, y_t), A = Γ₁ Γ₀⁻¹, Σ = Γ₀ − A Γ₀ Aᵀ."""
    G0 = C[:2, :2]
    G1 = C[2:, :2]
    A = G1 @ np.linalg.inv(G0)
    Sigma = G0 - A @ G0 @ A.T
    return A, Sigma


check_lines = ["Population checks (no data):"]
for lam_x, lam_y, a_s, a_n, loading in ((0.25, 0.25, 0.95, 0.80, +1), (0.25, 0.25, 0.95, 0.80, -1), (0.30, 0.20, 0.95, 0.80, +1), (0.10, 0.40, 0.90, 0.85, -1)):
    Cp = common_component_C(lam_x, lam_y, a_s, a_n, loading)
    q_p = 0.5 * (Cp[0, 1] + Cp[2, 3])
    d_xy = Cp[0, 3] - Cp[1, 3] * q_p
    d_yx = Cp[1, 2] - Cp[0, 2] * q_p
    f_xy = q_p * (1 - lam_y) * (a_s - a_n)
    f_yx = q_p * (1 - lam_x) * (a_s - a_n)
    assert abs(d_xy - f_xy) < 1e-14 and abs(d_yx - f_yx) < 1e-14
    check_lines.append(f"  shared slow component λ_x = {lam_x}, λ_y = {lam_y}, a_s = {a_s}, a_n = {a_n}, loading {loading:+d}: q = {q_p:+.4f}, "
                       f"a_x = {Cp[0, 2]:.4f}, a_y = {Cp[1, 3]:.4f}, cross-lag {Cp[0, 3]:+.5f}; d(x→y) = {d_xy:+.6f} = q(1 − λ_y)(a_s − a_n) = {f_xy:+.6f}; "
                       f"d(y→x) = {d_yx:+.6f} = q(1 − λ_x)(a_s − a_n) = {f_yx:+.6f}")
Cw = common_component_C(0.25, 0.25, 0.95, 0.80, +1)
A, Sigma = var1_from_lag01(Cw)
q_eps = Sigma[0, 1] / np.sqrt(Sigma[0, 0] * Sigma[1, 1])
c_coup, a_coef, q_w = A[0, 1], A[0, 0], Cw[0, 1]
d_w = Cw[0, 3] - Cw[1, 3] * q_w
# the VAR(1)'s own stationary lag-0/lag-1 structure reproduces the matrix (Lyapunov: Γ₀ = A Γ₀ Aᵀ + Σ, Γ₁ = A Γ₀)
G0 = Cw[:2, :2]
assert np.allclose(A @ G0 @ A.T + Sigma, G0) and np.allclose(A @ G0, Cw[2:, :2])
atoms_common = atoms_from_corr(Cw[None])[0]
check_lines.append(f"  τ = 1 equivalence, worked example λ = 0.25, a_s = 0.95, a_n = 0.80: a = {Cw[0, 2]:.4f}, q = {q_w:.4f}, cross-lag {Cw[0, 3]:.4f}, d = {d_w:+.6f}; "
                   f"A = Γ₁Γ₀⁻¹ = [[{A[0, 0]:.4f}, {A[0, 1]:.4f}], [{A[1, 0]:.4f}, {A[1, 1]:.4f}]], innovation correlation q_ε = {q_eps:.4f}, "
                   f"c(1 − q²) = {c_coup * (1 - q_w ** 2):+.6f}; the VAR(1) with this A and Σ has the same Γ₀ and Γ₁ (Lyapunov check passed), so the same 4 × 4 matrix and "
                   f"the same sixteen τ = 1 atoms (sts = {atoms_common[ATOMS.index('sts')]:.5f}, rtr = {atoms_common[ATOMS.index('rtr')]:.5f}).")

t0 = time.time()
lines = [f"# The cross-lag budget on the data (partB12_crosslag_budget.py; git={sha}; seed={SEED})", "",
         "Per subject and run, over the 6,555 pairs: δ_run = s·d at the run level (s = sign of the run-level q; d = mean of the two directions of "
         "corr(x_t, y_(t+1)) − a_y q), δ_wd = the same after removing each region's mean within each W = 60 window, δ_means = δ_run − δ_wd, "
         "δ_within = s·Σ_w π_w d_w, δ_pool = s·Σ_w π_w (a_(y,w) − ā_y) q_w, ε = δ_wd − δ_within − δ_pool (definitions and weights: "
         "notes/rev_crosslag_budget.py); beside them δ_60 = s·mean_w d_w and partB10's window-sign value mean_w sign(q_w) d_w. Mean over "
         "pairs per run; per subject the mean of the two runs; grand mean with subject-bootstrap 95 % CI (10,000 draws, seed 20261120, one "
         "set of draws per variant), exact sign-flip p, count positive; per run type. Rules recorded before the run: analysis_record.md, "
         "\"The cross-lag budget: pre-run entry, 16 Sep 2026\"; the null-corrected budget and the reading under those rules are in "
         "crosslag_budget_null_tables.md (partB13).", ""] + check_lines + [""]
print("\n".join(lines), flush=True)

ts = sio.loadmat(MAT)
b10 = pd.read_csv(OUT / "crosslag_deviation.csv")
idx = boot_idx_variants()
rows = []
per_run_terms = {}
for var in ("ts_gsr", "ts_demean"):
    dg = np.load(OUT / f"diag_series_{var}_W60.npz")
    T = {k: np.full((14, 2), np.nan) for k in TERMS + ("a", "absq", "sumpi", "frac_qneg", "frac_absq05", "frac_absq10")}
    max_ident = 0.0
    n_checked = 0
    for s_i, c in product(range(14), range(2)):
        X = np.asarray(ts[var][s_i, c], float)[REGIONS]
        kept = np.where(np.all(np.isfinite(X), axis=0))[0]
        pp = PairPhiID(X[:, kept])
        I, J = pp.I, pp.J
        C_run = pp.C
        s = np.sign(0.5 * (C_run[:, 0, 1] + C_run[:, 2, 3]))
        Xwd = X.copy()
        C_win, sd_win, n_win = [], [], []
        for w in range(N_WIN):
            in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
            assert in_w.size > 5
            n_win.append(in_w.size)
            Xwd[:, in_w] = X[:, in_w] - X[:, in_w].mean(1, keepdims=True)
            pw = PairPhiID(X[:, in_w])
            Cw_ = pw.C
            ax, ay = Cw_[:, 0, 2], Cw_[:, 1, 3]
            q = 0.5 * (Cw_[:, 0, 1] + Cw_[:, 2, 3])
            dev = np.r_[Cw_[:, 0, 3] - ay * q, Cw_[:, 1, 2] - ax * q]
            assert abs(np.abs(dev).mean() - dg["xcorr_dev"][s_i, c, w]) < 1e-10, (var, s_i, c, w)
            n_checked += 1
            C_win.append(Cw_)
            sdw = X[:, in_w].std(1)                                    # ddof = 0
            sd_win.append(np.stack([sdw[I], sdw[J]], 1))
        C_win = np.stack(C_win, 1)
        sd_win = np.stack(sd_win, 1)
        n_win = np.array(n_win)
        C_wd = PairPhiID(Xwd[:, kept]).C
        o = budget_terms(C_run, C_wd, C_win, sd_win, n_win, s)
        max_ident = max(max_ident, np.abs(o["run"] - (o["within"] + o["pool"] + o["means"] + o["eps"])).max())
        for k in TERMS + ("a", "absq", "sumpi"):
            T[k][s_i, c] = o[k].mean()
        T["frac_qneg"][s_i, c] = (o["q"] < 0).mean()
        T["frac_absq05"][s_i, c] = (o["absq"] < 0.05).mean()
        T["frac_absq10"][s_i, c] = (o["absq"] < 0.10).mean()
        # reproduction of partB10's per-run values
        r10 = b10[(b10.variant == var) & (b10.subject == s_i + 1) & (b10.condition == CONDITIONS[c])].iloc[0]
        assert abs(T["run"][s_i, c] - r10.signq_weighted_mean_deviation) < 1e-12, (var, s_i, c, T["run"][s_i, c], r10.signq_weighted_mean_deviation)
        assert abs(T["d60_winsign"][s_i, c] - r10.w60_signq_weighted_mean_deviation) < 1e-12
        rows.append(dict(variant=var, subject=s_i + 1, condition=CONDITIONS[c], n_trs=int(kept.size), n_trs_last_window=int(n_win[-1]),
                         **{("delta_" + k if k in TERMS else k): T[k][s_i, c] for k in T}))
        print(f"   {var} subject {s_i + 1} {CONDITIONS[c]}: run {T['run'][s_i, c]:+.5f} within {T['within'][s_i, c]:+.5f} pool {T['pool'][s_i, c]:+.5f} "
              f"means {T['means'][s_i, c]:+.5f} eps {T['eps'][s_i, c]:+.6f} d60 {T['d60'][s_i, c]:+.5f} winsign {T['d60_winsign'][s_i, c]:+.5f} ({time.time() - t0:.0f} s)", flush=True)
    per_run_terms[var] = T
    lines.append(f"## {var} ({n_checked} windows checked against diag_series xcorr_dev; max |δ_run − (δ_within + δ_pool + δ_means + ε)| over pairs and runs {max_ident:.1e}; "
                 f"δ_run and the window-sign value reproduce partB10's per-run values to 1e-12)")
    lines.append("")
    lines.append(f"Run-level mean pair a {T['a'].mean():.4f} (DMT {T['a'][:, 0].mean():.4f}, PCB {T['a'][:, 1].mean():.4f}); mean |q̂| {T['absq'].mean():.4f} "
                 f"(DMT {T['absq'][:, 0].mean():.4f}, PCB {T['absq'][:, 1].mean():.4f}); fraction of pairs with q̂ < 0 {T['frac_qneg'].mean():.3f}, "
                 f"|q̂| < 0.05 {T['frac_absq05'].mean():.3f}, |q̂| < 0.10 {T['frac_absq10'].mean():.3f}; mean Σ_w π_w {T['sumpi'].mean():.4f}.")
    for k in TERMS:
        r = aggregate(T[k], idx[var])
        lines.append(fmt_agg("δ_" + k if k not in ("d60", "d60_winsign") else ("δ_60 (run-level sign)" if k == "d60" else "window-sign value (partB10)"), r))
    r_run = aggregate(T["run"], idx[var])
    lines.append("Shares of δ_run (grand means): " + ", ".join(f"δ_{k} {aggregate(T[k], idx[var])['grand'] / r_run['grand']:+.3f}" for k in ("within", "pool", "means", "eps")))
    lines.append("Per-subject δ_run (mean of the two runs): " + np.array2string(r_run["per_subj"], precision=5, floatmode="fixed", max_line_width=250))
    for k in ("within", "pool", "means"):
        lines.append(f"Per-subject δ_{k}: " + np.array2string(aggregate(T[k], idx[var])["per_subj"], precision=5, floatmode="fixed", max_line_width=250))
    lines.append("")
    print("\n".join(lines[-14:]), flush=True)

print(f"done in {time.time() - t0:.0f} s")
pd.DataFrame(rows).to_csv(OUT / "crosslag_budget.csv", index=False)
(OUT / "crosslag_budget_tables.md").write_text("\n".join(lines) + "\n")
print(f"wrote {OUT / 'crosslag_budget_tables.md'} and crosslag_budget.csv")
