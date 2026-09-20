"""
partB19_exchange_rates.py — B19: (a) exchange rates at the operating point in data units; (b) the within-window
regression of pair sts on (mean r₁, |q|, |a_x − a_y|); (c) the cross-half correlation of the sts and r₁ DiDs;
(d) BCa versions of the bootstrap intervals the main text reports.
Pre-run entry: manuscript/analysis_record.md, "Exchange rates, the within-window regression, the cross-half
correlation and BCa intervals (B19): pre-run entry, 20 Sep 2026" (specification, predictions and rules as in
notes/review_2026-09-20/plan_to_submission_2026-09-20.md, §5).

(a) Closed form (rev_phiid_fast.atoms_from_corr, ar1_corr; the symmetric VAR(1) of partB8 for the coupling c, Γ₀ from
    the discrete Lyapunov equation; two conventions for c: partB8's matched view, in which a and the innovation
    correlation are re-solved so that the measured r₁ and q stay at the operating point, and a held with q held) at
    (r₁, q) = (0.85, 0.25): central differences with h = 1e-4; sts per 0.01 of r₁, per 0.1 of
    |q|, per 0.01 of c; and per SD of the data's own variation: regional r₁ SD (from regional_sts_r1.csv), pair |q|
    SD (from scope_map_overlay_points.npz, pre_w1to4_q), window-level a scatter 0.03 (the verification of 20 Sep);
    the identity at q = 0 with unequal coefficients (sts = 2 min(S_x, S_y), rtr = 0) at four (a_x, a_y) pairs. No
    external data.
(b) Needs the .mat: within each W = 60 window of every subject and run (both variants), the per-pair sts, mean r₁ =
    (a_x + a_y)/2, |q| and |a_x − a_y| recomputed exactly as partB4_diagnostic.py builds them; OLS of sts on the three
    (standardised within the window); mean R² and mean standardised coefficients over the 392 windows (window 5
    included; it is a descriptive regression), beside r² for r₁ alone and R² of the full AR(1) prediction.
(c) Needs the .mat for the autocorrelation series only: the odd/even half DiDs of partB7 (odd = pre {1, 3}, post
    {7, 9, 11, 13}; even = pre {2, 4}, post {6, 8, 10, 12, 14}) from diag_series_<variant>_W60.npz (observed sts) and
    rev_series.autocorr_series (window mode; r₁); r(sts_odd, r₁_even), r(sts_even, r₁_odd), their mean, the split-half
    reliabilities of both, and the disattenuated value mean / √(rel_sts × rel_r₁). partB7 does not save the halves.
(d) No external data: for the DiDs the main text quotes whose per-subject values are committed (inference_rows_raw,
    _diag, _ccs_pub and _lag .pkl; the primary sts DiD of Table 2 from results/atoms_win60_115regions-all_<variant>_
    window.npy), the committed percentile interval, the percentile interval recomputed (10,000 draws, seed 20261120),
    and the BCa interval (Efron: z₀ from the share of bootstrap means below the estimate, acceleration from the
    jackknife of the mean); the point estimate and the sign-flip p are unchanged by construction. Both interval
    types tabulated where they differ by more than 10 % of the width.
Parts (b) and (c) are skipped, and say so, when the .mat is absent. Seed 20261120.
Outputs (notes/review_results/partB/): exchange_rates_tables.md, bca_intervals.csv, exchange_rates_run.log via
run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB19_exchange_rates.py   (seconds without the .mat; the
diagnostic's time with it)
"""
import pickle
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
from scipy.linalg import solve_discrete_lyapunov
from scipy.optimize import brentq, least_squares
from scipy.stats import norm, pearsonr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
RR = REPO / "notes" / "review_results"
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
REGIONS = np.array([r for r in range(116) if r != 20])
IX = {n: i for i, n in enumerate(ATOMS)}
S = IX["sts"]
SEED = 20261120
N_BOOT = 10000
H = 1e-4
R1, Q0 = 0.85, 0.25
SIGNS = np.array(list(product((-1, 1), repeat=14)))
PRE, POST = np.arange(0, 4), np.arange(5, 14)
HALVES = {"odd": (np.array([0, 2]), np.array([6, 8, 10, 12])), "even": (np.array([1, 3]), np.array([5, 7, 9, 11, 13]))}
t0 = time.time()
lines = ["# Exchange rates in data units, the within-window regression, the cross-half correlation and BCa intervals (partB19_exchange_rates.py)", f"git={SHA}", ""]


def sts_of(ax, ay, q):
    return atoms_from_corr(ar1_corr(ax, ay, q))[0, S]


def coupled_corr4(a, c, qe):
    A = np.array([[a, c], [c, a]]); Qm = np.array([[1.0, qe], [qe, 1.0]])
    S0 = solve_discrete_lyapunov(A, Qm); S1 = A @ S0
    C = np.block([[S0, S1.T], [S1, S0]]); d = np.sqrt(np.diag(C))
    return C / np.outer(d, d)


def coupled_sts_at_q(a, c, q_target):
    """sts of the symmetric VAR(1) at coupling c with a held and the innovation correlation re-solved so that the lag-0 correlation is q_target."""
    qe = brentq(lambda e: coupled_corr4(a, c, e)[0, 1] - q_target, -0.999, 0.999)
    return atoms_from_corr(coupled_corr4(a, c, qe))[0, S]


def coupled_sts_matched(c, r1_target, q_target):
    """sts at coupling c in partB8's matched view: a and the innovation correlation re-solved so that the pair's measured r₁ and q stay at the targets."""
    def f(p):
        C = coupled_corr4(p[0], c, p[1]); return [C[0, 2] - r1_target, C[0, 1] - q_target]
    lim = 0.995 - abs(c)
    sol = least_squares(f, [min(r1_target, lim - 0.01), q_target], bounds=([0.0, -0.995], [lim, 0.995]), xtol=1e-12, ftol=1e-12)
    assert np.abs(sol.fun).max() < 1e-8, (c, sol.fun)
    return atoms_from_corr(coupled_corr4(sol.x[0], c, sol.x[1]))[0, S]


# ---------------------------------------------------------------- (a) exchange rates
d_r1 = (sts_of(R1 + H, R1 + H, Q0) - sts_of(R1 - H, R1 - H, Q0)) / (2 * H)
d_q = (sts_of(R1, R1, Q0 + H) - sts_of(R1, R1, Q0 - H)) / (2 * H)
d_c = (coupled_sts_at_q(R1, H, Q0) - coupled_sts_at_q(R1, -H, Q0)) / (2 * H)           # a held at 0.85, q held at 0.25
d_c_m = (coupled_sts_matched(H, R1, Q0) - coupled_sts_matched(-H, R1, Q0)) / (2 * H)      # partB8's matched view: measured r₁ and q held at (0.85, 0.25)
d_asym = (sts_of(R1 + H, R1 - H, Q0) - sts_of(R1, R1, Q0)) / (2 * H)   # per unit of a_x − a_y at fixed mean; one-sided at 0 (sts falls with |a_x − a_y| either way)
reg = np.genfromtxt(OUT / "regional_sts_r1.csv", delimiter=",", names=True, dtype=None, encoding="utf-8")
sd_r1_reg = float(np.std(reg["r1_windowed"], ddof=1))
qpool = np.load(OUT / "scope_map_overlay_points.npz")["pre_w1to4_q"]; qpool = qpool[np.isfinite(qpool)]
sd_abs_q = float(np.std(np.abs(qpool), ddof=1)); sd_q = float(np.std(qpool, ddof=1))
lines += ["## (a) Exchange rates at the operating point (r₁, q) = (0.85, 0.25), closed form, central differences h = 1e-4", "",
          "| input | ∂sts/∂input (nats per unit) | sts change per step in data units | per SD of the data's variation |", "|---|---|---|---|",
          f"| r₁ (both members) | {d_r1:+.4f} | {0.01 * d_r1:+.4f} per 0.01 of r₁ | {sd_r1_reg * d_r1:+.4f} per regional SD {sd_r1_reg:.4f} (regional_sts_r1.csv); {0.03 * d_r1:+.4f} per window-level scatter 0.03 |",
          f"| q (lag-0 correlation) | {d_q:+.4f} | {0.1 * d_q:+.4f} per 0.1 of \\|q\\| | {sd_abs_q * d_q:+.4f} per SD of pair \\|q\\| {sd_abs_q:.4f} (SD of q {sd_q:.4f}; scope_map_overlay_points.npz) |",
          f"| c (symmetric VAR(1) coupling), measured r₁ and q held at (0.85, 0.25) — partB8's matched view, the coupling map's convention | {d_c_m:+.4f} | {0.01 * d_c_m:+.4f} per 0.01 of c | — (no data value of c) |",
          f"| c (symmetric VAR(1) coupling), a held at 0.85 and q at 0.25 (r₁ then moves with c) | {d_c:+.4f} | {0.01 * d_c:+.4f} per 0.01 of c | — |",
          f"| \\|a_x − a_y\\| at fixed mean 0.85 (one-sided at 0) | {d_asym:+.4f} | {0.01 * d_asym:+.4f} per 0.01 of \\|a_x − a_y\\| | {0.03 * d_asym:+.4f} per 0.03 (the window-level scatter of one member's a; see the next line) |", ""]
asym_tab = [(0.0, sts_of(R1, R1, Q0))] + [(d, sts_of(R1 + d / 2, R1 - d / 2, Q0)) for d in (0.01, 0.02, 0.03, 0.05, 0.10)]
lines.append("sts against the within-pair asymmetry a_x − a_y at fixed mean 0.85 and q = 0.25: " + "; ".join(f"{d:.2f} → {v:.4f}" for d, v in asym_tab) +
             " (the response is first-order in the asymmetry because MMI takes the minimum of the two self-informations: sts ≈ 2 min(S_x, S_y) − C).")
ratio_per_unit = abs(d_r1 / d_q); ratio_per_sd = abs(sd_r1_reg * d_r1) / abs(sd_abs_q * d_q)
lines += [f"Ratio |∂sts/∂r₁| / |∂sts/∂q| per unit: {ratio_per_unit:.1f}; per SD of the data's variation (regional r₁ SD against pair |q| SD): {ratio_per_sd:.2f}; with the window-level scatter of a (0.03) in place of the regional SD: {abs(0.03 * d_r1) / abs(sd_abs_q * d_q):.2f}.",
          f"Coupled family check: sts at c = 0 through the Lyapunov construction {coupled_sts_at_q(R1, 0.0, Q0):.6f} against the diagonal closed form {sts_of(R1, R1, Q0):.6f}.", ""]
lines += ["Identity at q = 0 with unequal coefficients (sts = 2 min(S_x, S_y), rtr = 0):"]
for ax, ay in ((0.83, 0.87), (0.85, 0.85), (0.80, 0.90), (0.95, 0.60)):
    A = atoms_from_corr(ar1_corr(ax, ay, 0.0))[0]
    Sx, Sy = -0.5 * np.log(1 - ax ** 2), -0.5 * np.log(1 - ay ** 2)
    lines.append(f"  (a_x, a_y) = ({ax}, {ay}): sts {A[S]:.6f}, 2 min(S_x, S_y) {2 * min(Sx, Sy):.6f}, difference {A[S] - 2 * min(Sx, Sy):.1e}; rtr {A[IX['rtr']]:.1e}.")
lines.append("")

# ---------------------------------------------------------------- (b) within-window regression, (c) cross-half correlation
if MAT.exists():
    import scipy.io as sio
    from rev_series import autocorr_series
    ts = sio.loadmat(MAT)
    lines += ["## (b) Within-window regression of pair sts on (mean r₁, |q|, |a_x − a_y|), W = 60, all 392 windows per variant", "",
              "| variant | mean R² (3 regressors) | mean r² (r₁ alone) | mean R² of the full AR(1) prediction | mean standardised coefficients (r₁, \\|q\\|, \\|a_x − a_y\\|) |", "|---|---|---|---|---|"]
    r1_win = {}
    for var in ("ts_gsr", "ts_demean"):
        R2 = []; r2 = []; R2f = []; B = []
        for s in range(14):
            for c in range(2):
                X = np.asarray(ts[var][s, c], float)[REGIONS]
                kept = np.where(np.all(np.isfinite(X), axis=0))[0]
                for w in range(14):
                    in_w = kept[(kept >= w * 60) & (kept < (w + 1) * 60)]
                    if in_w.size <= 5:
                        continue
                    pp = PairPhiID(X[:, in_w])
                    y = pp.atoms_mean()[:, S]
                    ax, ay = pp.C[:, 0, 2], pp.C[:, 1, 3]; q = 0.5 * (pp.C[:, 0, 1] + pp.C[:, 2, 3])
                    pred = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
                    F = np.c_[0.5 * (ax + ay), np.abs(q), np.abs(ax - ay)]
                    Z = (F - F.mean(0)) / F.std(0, ddof=1); yz = (y - y.mean()) / y.std(ddof=1)
                    Xd = np.c_[np.ones(y.size), Z]
                    beta, *_ = np.linalg.lstsq(Xd, yz, rcond=None)
                    fit = Xd @ beta
                    R2.append(1 - np.sum((yz - fit) ** 2) / np.sum(yz ** 2)); B.append(beta[1:])
                    r2.append(pearsonr(y, F[:, 0])[0] ** 2); R2f.append(pearsonr(y, pred)[0] ** 2)
            print(f"   (b) {var}: subject {s + 1}/14 done ({time.time() - t0:.0f}s)", flush=True)
        B = np.array(B)
        lines.append(f"| {var} | {np.mean(R2):.3f} (min {np.min(R2):.3f}, max {np.max(R2):.3f}) | {np.mean(r2):.3f} | {np.mean(R2f):.3f} | {np.mean(B[:, 0]):+.3f}, {np.mean(B[:, 1]):+.3f}, {np.mean(B[:, 2]):+.3f} |")
        r1_win[var] = autocorr_series(ts[var], 60, "window")[0]
    lines += ["", "Prediction recorded (b): R² close to 0.80 with |a_x − a_y| carrying the difference between 0.55 and 0.80.", ""]
    lines += ["## (c) Cross-half correlation of the MMI-sts DiD and the r₁ DiD (halves of partB7; per-subject half DiDs recomputed)", "",
              "| variant | r(sts_odd, r₁_even) | r(sts_even, r₁_odd) | mean | rel(sts) odd/even | rel(r₁) odd/even | ceiling √(rel × rel) | disattenuated mean / ceiling | full-set r |", "|---|---|---|---|---|---|---|---|---|"]
    for var in ("ts_gsr", "ts_demean"):
        obs = np.load(OUT / f"diag_series_{var}_W60.npz")["obs"]; ac = r1_win[var]

        def hd(x, pre, post):
            ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2); return ch[:, 0] - ch[:, 1]
        d = {h: (hd(obs, *HALVES[h]), hd(ac, *HALVES[h])) for h in HALVES}
        x1 = pearsonr(d["odd"][0], d["even"][1])[0]; x2 = pearsonr(d["even"][0], d["odd"][1])[0]
        rel_s = pearsonr(d["odd"][0], d["even"][0])[0]; rel_a = pearsonr(d["odd"][1], d["even"][1])[0]
        ceil = float(np.sqrt(max(rel_s, 0) * max(rel_a, 0)))
        full = pearsonr(hd(obs, PRE, POST), hd(ac, PRE, POST))[0]
        lines.append(f"| {var} | {x1:+.3f} | {x2:+.3f} | {0.5 * (x1 + x2):+.3f} | {rel_s:+.3f} | {rel_a:+.3f} | {ceil:.3f} | {0.5 * (x1 + x2) / ceil if ceil > 0 else float('nan'):+.2f} | {full:+.3f} |")
    lines += ["", "Prediction recorded (c): below 0.953 and near the ceiling 0.729 (√(0.717 × 0.741), the split-half reliabilities of splithalf_tables.md).", ""]
else:
    lines += ["## (b) and (c): skipped — external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat is not present in this checkout; both parts need it (the per-pair window values and the r₁ window series are not saved by partB4 or partB7).", ""]

# ---------------------------------------------------------------- (d) BCa intervals
def bca(v, r, n_boot=N_BOOT):
    v = np.asarray(v, float); n = v.size; est = v.mean()
    draws = v[r.integers(0, n, (n_boot, n))].mean(1)
    pct = np.percentile(draws, [2.5, 97.5])
    z0 = norm.ppf(np.clip(np.mean(draws < est), 1e-6, 1 - 1e-6))
    jack = np.array([np.delete(v, i).mean() for i in range(n)]); jm = jack.mean()
    num = np.sum((jm - jack) ** 3); den = 6 * np.sum((jm - jack) ** 2) ** 1.5
    a = num / den if den > 0 else 0.0
    def adj(alpha):
        z = norm.ppf(alpha); return norm.cdf(z0 + (z0 + z) / (1 - a * (z0 + z)))
    lo, hi = np.percentile(draws, [100 * adj(0.025), 100 * adj(0.975)])
    return pct, (lo, hi), z0, a


def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


items = []      # (name, per-subject values, committed lo, committed hi)
for fname, labels in (("inference_rows_raw.pkl", ["sts ts_gsr W60", "sts ts_demean W60", "sts ts_gsr global-bins", "sts ts_demean global-bins", "autocorr ts_gsr W60", "autocorr ts_demean W60", "autocorr ts_gsr run-standardised bins", "PhiR ts_gsr W60"]),
                       ("inference_rows_diag.pkl", ["diag observed sts ts_gsr W60", "diag predicted sts ts_gsr W60", "diag residual sts ts_gsr W60", "diag residual sts ts_demean W60", "diag residual sts ts_gsr W30"]),
                       ("inference_rows_ccs_pub.pkl", ["CCSpub sts ts_gsr W60", "CCSpub sts ts_gsr global-bins", "CCSpub sts ts_demean W60", "CCSpub sts ts_demean global-bins"]),
                       ("inference_rows_lag.pkl", ["sts tau1 ts_gsr W60", "sts tau2 ts_gsr W60", "sts tau3 ts_gsr W60", "sts tau5 ts_gsr W60", "autocorr lag1 ts_gsr W60", "autocorr lag2 ts_gsr W60", "autocorr lag3 ts_gsr W60", "autocorr lag5 ts_gsr W60"])):
    rows = pickle.load(open(RR / fname, "rb"))
    for lab in labels:
        for st in ("primary", "early", "late") if lab.startswith("diag residual sts ts_gsr W60") else ("primary",):
            r = [x for x in rows if x["label"] == lab and x["set"] == st]
            if r:
                items.append((f"{lab} [{st}]", r[0]["did_subjects"], r[0]["did_lo"], r[0]["did_hi"]))
for var in ("ts_gsr", "ts_demean"):
    A = np.load(REPO / "results" / f"atoms_win60_115regions-all_{var}_window.npy")[..., S]
    d = (A[:, 0, POST].mean(1) - A[:, 0, PRE].mean(1)) - (A[:, 1, POST].mean(1) - A[:, 1, PRE].mean(1))
    items.append((f"Table 2 primary sts DiD {var} W60 (from results/atoms_win60)", d, np.nan, np.nan))
lines += ["## (d) BCa intervals beside the percentile intervals, per-subject DiDs (N = 14), 10,000 draws, seed 20261120", "",
          "| quantity | DiD | sign-flip p | committed percentile CI | percentile CI recomputed | BCa CI | z₀ | a | width ratio BCa/percentile | differ by > 10 % of width |", "|---|---|---|---|---|---|---|---|---|---|"]
csv = ["quantity,did,signflip_p,committed_lo,committed_hi,pct_lo,pct_hi,bca_lo,bca_hi,z0,accel,differs_gt_10pct"]
for name, v, clo, chi in items:
    v = np.asarray(v, float)
    pct, (lo, hi), z0, a = bca(v, np.random.default_rng(SEED))
    width = pct[1] - pct[0]
    differs = (abs(lo - pct[0]) > 0.1 * width) or (abs(hi - pct[1]) > 0.1 * width)
    ccell = "—" if np.isnan(clo) else f"[{clo:+.4f}, {chi:+.4f}]"
    lines.append(f"| {name} | {v.mean():+.4f} | {signflip_p(v):.4f} | {ccell} | [{pct[0]:+.4f}, {pct[1]:+.4f}] | [{lo:+.4f}, {hi:+.4f}] | {z0:+.3f} | {a:+.3f} | {(hi - lo) / width:.2f} | {'yes' if differs else 'no'} |")
    csv.append(f"{name},{v.mean():.6f},{signflip_p(v):.4f},{clo:.6f},{chi:.6f},{pct[0]:.6f},{pct[1]:.6f},{lo:.6f},{hi:.6f},{z0:.4f},{a:.4f},{int(differs)}")
lines += ["", "Rule recorded (d): point estimates and sign-flip p values unchanged (they do not depend on the interval); both interval types tabulated where they differ by more than 10 % of the interval width. Prediction: BCa intervals wider at N = 14. "
          "The committed percentile interval was drawn in the writing script's own generator order; the recomputed one uses a fresh generator (seed 20261120) per quantity, so the two percentile intervals differ by Monte-Carlo error only."]
(OUT / "bca_intervals.csv").write_text(f"# partB19_exchange_rates.py; BCa and percentile intervals of the per-subject DiDs; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "exchange_rates_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"done ({time.time() - t0:.0f}s)")
