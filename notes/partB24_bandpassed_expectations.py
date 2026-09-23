"""
partB24_bandpassed_expectations.py — B24: the pure-autocorrelation expectations of B22's statistics on the band-passed
generator of B17b (no data).
Pre-run entry: manuscript/analysis_record.md, "The pure-autocorrelation expectations of the new statistics on the
band-passed generator (B24): pre-run entry, 23 Sep 2026" (round 16, Part A).

B17b's generator at its solved parameters, condition (i) only: the smooth band-pass of review_v2_residual_null.py (lo and
hi from fit_filter on the placebo ACF, as B17b) with tilt exp(−βf²), per pair β ~ N(β̄, 0.5β̄) clipped at 5 and q ~ N(0,
σ_q) clipped to ±0.95; β̄, σ_q and β̄_post read from the committed calibration_filtered_tables.md (β̄ and β̄_post were
solved to xtol = 1 there, so the printed precision is finer than the solve's own); N_REP = 20 replicates × 14 subjects ×
2 runs × 840 samples × 300 pairs; one draw of (β, q) per subject shared by the two runs; the placebo run at the pre
parameters, the DMT run filtered at the pre and at the post parameters (β·β̄_post/β̄) and spliced at sample 300.
B17b's functions are copied verbatim (importing partB17b_calibration_filtered.py would run it) and checked against their
source lines at run time: signflip_p and boot_ci (l. 81–88), filtered, draw_noise and draw_params (l. 97–112),
simulate_run (l. 135–150) and B17's deviations, analyse_run, cell and did as B17b carries them (l. 154–186); and
partB15's with_deviation and response (l. 78–92).
Per replicate: B17b's statistics (W = 60, and the global fit with the run-level and the period-level prediction: the
DMT pre-injection level, the DiDs of observed, predicted and residual sts, the residual's exact sign-flip p and bootstrap
CI, the δ_sym and RMS δ_anti DiDs); and at W = 60 B22's statistics: A_same (the sign of the pair's whole-run q̄ in the
same run), A_other (in the same subject's other run), the window-sign statistic, B (the OLS slope of δ_sym on q), D and
Sym (partB15's closed-form responses to δ_anti and to δ_sym alone) and their sum, and the window-level mean pair r₁ — each
as its DMT pre-injection level and its DiD (windows 6–14 minus 1–4, DMT minus placebo); every quantity summarised as mean
± SD over the replicates. Checked first: the W = 60 sts, predicted, residual and RMS δ_anti DiDs each within one of
B17b's replicate SDs of B17b's committed means (calibration_filtered_tables.md); a miss is printed as CHECK FAILED and
the run goes on.
Free choices: those above; seed 20261120, one generator; --n-rep N sets the replicates (a check that the script runs).
Outputs (notes/review_results/partB/): bandpassed_expectations_tables.md, bandpassed_expectations.csv (one row per
replicate and estimator), bandpassed_expectations_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB24_bandpassed_expectations.py   (a few minutes)
"""
import re
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_phiid_fast import PairPhiID, atoms_from_corr, ar1_corr, ATOMS
from review_v2_residual_null import psd_weights, fit_filter, TARGET_ACF
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
OUT = REPO / "notes" / "review_results" / "partB"
S = ATOMS.index("sts")
SEED = 20261120
TR = 2.0
N_PAIRS, N_SUBJ, T, W, N_BOOT = 300, 14, 840, 60, 1000
N_REP = int(sys.argv[sys.argv.index("--n-rep") + 1]) if "--n-rep" in sys.argv else 20
CHANGE_AT = 300
PRE, POST = np.arange(0, 4), np.arange(5, 14)
PRE_B, POST_B = np.arange(0, 8), np.arange(10, 28)
SIGNS = np.array(list(product((-1, 1), repeat=N_SUBJ)))
t0 = time.time()
rng = np.random.default_rng(SEED)
PAIRS = [(2 * k, 2 * k + 1) for k in range(N_PAIRS)]
CHECKS = []
nan = float("nan")


def check(name, diff, tol):
    ok = bool(np.isfinite(diff) and diff <= tol)
    CHECKS.append((name, diff, tol, ok))
    if not ok:
        print(f"   CHECK FAILED: {name}: |difference| {diff:.3g} above {tol:.1g}", flush=True)
    return ok


def verbatim(src_rel, first, last):
    """The block between this file's markers equals lines first–last of src_rel."""
    own = Path(__file__).read_text().split("\n")
    i = next(k for k, l in enumerate(own) if l.startswith(f"# ---- copied verbatim from {src_rel}, l. {first}–{last}"))
    j = next(k for k in range(i + 1, len(own)) if own[k].startswith("# ---- end of the copy"))
    src = (REPO / src_rel).read_text().split("\n")[first - 1:last]
    check(f"the copy of {src_rel} l. {first}–{last} is verbatim", 0.0 if own[i + 1:j] == src else 1.0, 0.0)


# ---------------------------------------------------------------- the generator's parameters, as committed
CFT = (OUT / "calibration_filtered_tables.md").read_text()
BMEAN = float(re.search(r"β̄ = (\d+\.\d+) \(window-level mean a", CFT).group(1))
QSD = float(re.search(r"σ_q = (\d\.\d+) \(mean \|q\|", CFT).group(1))
BMEAN_POST = float(re.search(r"β̄_post = (\d+\.\d+) \(mean a", CFT).group(1))
DELTA = nan                                               # condition (iv)'s asymmetry is not used here
FIT = fit_filter(TARGET_ACF["placebo"])
LO, HI = FIT[2], FIT[3]
m_edges = re.search(r"smooth (\d\.\d+)–(\d\.\d+) Hz band-pass", CFT)
check("the filter edges = those in calibration_filtered_tables.md (printed precision)", max(abs(round(LO, 4) - float(m_edges.group(1))), abs(round(HI, 3) - float(m_edges.group(2)))), 1e-12)
print(f"   generator: β̄ = {BMEAN}, σ_q = {QSD}, β̄_post = {BMEAN_POST}; filter {LO:.4f}–{HI:.3f} Hz", flush=True)


# ---- copied verbatim from notes/partB17b_calibration_filtered.py, l. 81–88 (checked at run time)
def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))


def boot_ci(v):
    draws = v[rng.integers(0, v.size, (N_BOOT, v.size))].mean(1)
    return np.percentile(draws, [2.5, 97.5])
# ---- end of the copy


# ---- copied verbatim from notes/partB17b_calibration_filtered.py, l. 97–112 (checked at run time)
def filtered(e1, e2, betas_x, betas_y, n):
    """Filter the two white noises (n_pairs, n) with per-pair tilts β_x (for x) and β_y (for y); circular, as gen."""
    f = np.fft.rfftfreq(n, d=TR)
    Hx = np.sqrt(psd_weights(f, betas_x, LO, HI)); Hy = np.sqrt(psd_weights(f, betas_y, LO, HI))
    return np.fft.irfft(np.fft.rfft(e1, axis=1) * Hx, n=n, axis=1), np.fft.irfft(np.fft.rfft(e2, axis=1) * Hy, n=n, axis=1)


def draw_noise(n_pairs, n, q):
    e1 = rng.standard_normal((n_pairs, n)); e2 = rng.standard_normal((n_pairs, n))
    return e1, q[:, None] * e1 + np.sqrt(1 - q[:, None] ** 2) * e2


def draw_params(n_pairs, bmean, qsd):
    betas = np.clip(rng.normal(bmean, 0.5 * bmean, n_pairs), 5, None)
    q = np.clip(rng.normal(0, qsd, n_pairs), -0.95, 0.95)
    return betas, q
# ---- end of the copy


# ---- copied verbatim from notes/partB17b_calibration_filtered.py, l. 135–150 (checked at run time)
def simulate_run(betas, q, change, dc, asym):
    """One run of N_PAIRS pairs; returns X (2 N_PAIRS, T): rows (2k, 2k+1) are pair k."""
    e1, e2 = draw_noise(N_PAIRS, T, q)
    d = DELTA if asym else 0.0
    x, y = filtered(e1, e2, np.clip(betas + d, 5, None), np.clip(betas - d, 5, None), T)
    if change:
        bp = betas * (BMEAN_POST / BMEAN)
        xp, yp = filtered(e1, e2, np.clip(bp + d, 5, None), np.clip(bp - d, 5, None), T)
        x = np.concatenate([x[:, :CHANGE_AT], xp[:, CHANGE_AT:]], 1); y = np.concatenate([y[:, :CHANGE_AT], yp[:, CHANGE_AT:]], 1)
    if dc:
        sx, sy = x[:, CHANGE_AT:].std(1, ddof=1), y[:, CHANGE_AT:].std(1, ddof=1)
        xn = x[:, CHANGE_AT:] + dc * y[:, CHANGE_AT - 1:-1]; yn = y[:, CHANGE_AT:] + dc * x[:, CHANGE_AT - 1:-1]
        x = np.concatenate([x[:, :CHANGE_AT], xn * (sx / xn.std(1, ddof=1))[:, None]], 1)
        y = np.concatenate([y[:, :CHANGE_AT], yn * (sy / yn.std(1, ddof=1))[:, None]], 1)
    X = np.empty((2 * N_PAIRS, T)); X[0::2] = x; X[1::2] = y
    return X
# ---- end of the copy


# ---- copied verbatim from notes/partB17b_calibration_filtered.py, l. 154–186 (checked at run time)
def deviations(C):
    ax, ay = C[:, 0, 2], C[:, 1, 3]; q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    d_xy = C[:, 0, 3] - ay * q; d_yx = C[:, 1, 2] - ax * q
    return ax, ay, q, 0.5 * (d_xy + d_yx), 0.5 * (d_xy - d_yx)


def analyse_run(X):
    """Window (14,) and bin (28,) whole-pair means of observed sts, predicted sts, δ_sym, δ_anti."""
    obs_w = np.empty(14); pred_w = np.empty(14); sym_w = np.empty(14); anti_w = np.empty(14)
    for w in range(14):
        pp = PairPhiID(X[:, w * W:(w + 1) * W], pairs=PAIRS)
        ax, ay, q, sym, anti = deviations(pp.C)
        obs_w[w] = pp.atoms_mean()[:, S].mean(); pred_w[w] = atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean()
        sym_w[w] = sym.mean(); anti_w[w] = np.sqrt(np.mean(anti ** 2))
    pp = PairPhiID(X, pairs=PAIRS)
    ax, ay, q, sym, anti = deviations(pp.C)
    obs_b = np.nanmean(pp.atoms_bins(np.arange(pp.n) // 30, 28)[..., S], axis=1)
    pred_b = np.full(28, atoms_from_corr(ar1_corr(ax, ay, q))[:, S].mean())          # the pipeline's run-level prediction, constant across bins
    pred_bp = np.empty(28)                                                            # period-level prediction: (a_x, a_y, q) measured on the pre and on the post samples
    for lo, hi, sl in ((0, CHANGE_AT, slice(0, CHANGE_AT // 30)), (CHANGE_AT, T, slice(CHANGE_AT // 30, 28))):
        pq = PairPhiID(X[:, lo:hi], pairs=PAIRS)
        axp, ayp, qp, _, _ = deviations(pq.C)
        pred_bp[sl] = atoms_from_corr(ar1_corr(axp, ayp, qp))[:, S].mean()
    return obs_w, pred_w, sym_w, anti_w, obs_b, pred_b, pred_bp


def cell(v):
    return '—' if np.isnan(v).all() else f"{np.nanmean(v):+.5f} ± {np.nanstd(v):.5f}"


def did(x, pre, post):
    ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
    return ch[:, 0] - ch[:, 1]
# ---- end of the copy


# ---- copied verbatim from notes/partB15_directed_crosslag.py, l. 78–92 (checked at run time)
def with_deviation(ax, ay, q, d_xy, d_yx):
    """AR(1) matrices with the cross-lag entries corr(x_t, y_{t+1}) = a_y q + d_xy and corr(y_t, x_{t+1}) = a_x q + d_yx."""
    C = ar1_corr(ax, ay, q)
    C[:, 0, 3] = C[:, 3, 0] = ay * q + d_xy
    C[:, 1, 2] = C[:, 2, 1] = ax * q + d_yx
    return C


def response(ax, ay, q, sym, anti):
    """sts responses (per pair): to δ_anti alone, to δ_sym alone, to both; and the AR(1) sts."""
    base = atoms_from_corr(ar1_corr(ax, ay, q))[:, S]
    r_anti = atoms_from_corr(with_deviation(ax, ay, q, anti, -anti))[:, S] - base
    r_sym = atoms_from_corr(with_deviation(ax, ay, q, sym, sym))[:, S] - base
    r_both = atoms_from_corr(with_deviation(ax, ay, q, sym + anti, sym - anti))[:, S] - base
    return base, r_anti, r_sym, r_both
# ---- end of the copy


verbatim("notes/partB17b_calibration_filtered.py", 81, 88)
verbatim("notes/partB17b_calibration_filtered.py", 97, 112)
verbatim("notes/partB17b_calibration_filtered.py", 135, 150)
verbatim("notes/partB17b_calibration_filtered.py", 154, 186)
verbatim("notes/partB15_directed_crosslag.py", 78, 92)


def new_stats(X, qbar_same, qbar_other):
    """B22's per-window statistics on one run's 300 pairs: (14,) each."""
    out = {k: np.empty(14) for k in NEW}
    for w in range(14):
        pp = PairPhiID(X[:, w * W:(w + 1) * W], pairs=PAIRS)
        ax, ay, q, sym, anti = deviations(pp.C)
        base, r_anti, r_sym, r_both = response(ax, ay, q, sym, anti)
        out["A_other"][w] = np.mean(np.sign(qbar_other) * sym); out["A_same"][w] = np.mean(np.sign(qbar_same) * sym)
        out["winsign"][w] = np.mean(np.sign(q) * sym); out["B"][w] = np.polyfit(q, sym, 1)[0]
        out["D"][w] = r_anti.mean(); out["Sym"][w] = r_sym.mean(); out["D_plus_Sym"][w] = (r_anti + r_sym).mean()
        out["r1"][w] = np.mean(0.5 * (ax + ay))
    return out


NEW = ("A_other", "A_same", "winsign", "B", "D", "Sym", "D_plus_Sym", "r1")
NEW_NAMES = {"A_other": "A_other (sign from the other run)", "A_same": "A_same (sign from the same run)", "winsign": "window-sign statistic (selected)",
             "B": "B, slope of δ_sym on q", "D": "D, response to δ_anti alone", "Sym": "Sym, response to δ_sym alone", "D_plus_Sym": "D + Sym",
             "r1": "window-level mean pair r₁"}
ESTS = ("W60", "global (run-level prediction)", "global (period-level prediction)")
acc = {est: {k: [] for k in ("lvl", "sts", "pred", "res", "p", "sym", "anti")} for est in ESTS}
acc_new = {k: {"lvl": [], "did": []} for k in NEW}
sym_minus = []                                            # Sym DiD − (residual DiD − D DiD), per replicate
csv = ["estimator,replicate,sts_level_pre,sts_did,pred_did,res_did,res_p,res_ci_lo,res_ci_hi,sym_did,anti_did," + ",".join(f"{k}_level,{k}_did" for k in NEW)]
for rep in range(N_REP):
    obs_w = np.empty((N_SUBJ, 2, 14)); pred_w = np.empty((N_SUBJ, 2, 14)); sym_w = np.empty((N_SUBJ, 2, 14)); anti_w = np.empty((N_SUBJ, 2, 14))
    obs_b = np.empty((N_SUBJ, 2, 28)); pred_b = np.empty((N_SUBJ, 2, 28)); pred_bp = np.empty((N_SUBJ, 2, 28))
    nw = {k: np.empty((N_SUBJ, 2, 14)) for k in NEW}
    for s in range(N_SUBJ):
        betas, q = draw_params(N_PAIRS, BMEAN, QSD)
        Xs = [simulate_run(betas, q, change=(c == 0), dc=0.0, asym=False) for c in range(2)]
        qbar = []
        for c in range(2):
            obs_w[s, c], pred_w[s, c], sym_w[s, c], anti_w[s, c], obs_b[s, c], pred_b[s, c], pred_bp[s, c] = analyse_run(Xs[c])
            Cr = PairPhiID(Xs[c], pairs=PAIRS).C
            qbar.append(0.5 * (Cr[:, 0, 1] + Cr[:, 2, 3]))
        for c in range(2):
            st = new_stats(Xs[c], qbar[c], qbar[1 - c])
            for k in NEW:
                nw[k][s, c] = st[k]
    row_new = []
    for k in NEW:
        lvl = nw[k][:, 0, PRE].mean(); dd = did(nw[k], PRE, POST).mean()
        acc_new[k]["lvl"].append(lvl); acc_new[k]["did"].append(dd); row_new += [lvl, dd]
    for est, o, p, sy, an, pre, post in (("W60", obs_w, pred_w, sym_w, anti_w, PRE, POST), ("global (run-level prediction)", obs_b, pred_b, None, None, PRE_B, POST_B),
                                         ("global (period-level prediction)", obs_b, pred_bp, None, None, PRE_B, POST_B)):
        d_o, d_p = did(o, pre, post), did(p, pre, post); d_r = d_o - d_p
        pr = signflip_p(d_r); lo, hi = boot_ci(d_r)
        d_s = did(sy, pre, post).mean() if sy is not None else nan; d_a = did(an, pre, post).mean() if an is not None else nan
        lvl = o[:, 0, pre].mean()
        for k, v in (("lvl", lvl), ("sts", d_o.mean()), ("pred", d_p.mean()), ("res", d_r.mean()), ("p", pr), ("sym", d_s), ("anti", d_a)):
            acc[est][k].append(v)
        if est == "W60":
            sym_minus.append(acc_new["Sym"]["did"][-1] - (d_r.mean() - acc_new["D"]["did"][-1]))
        tail = ("," + ",".join(f"{v:.6f}" for v in row_new)) if est == "W60" else "," * (2 * len(NEW))
        csv.append(f"{est},{rep + 1},{lvl:.6f},{d_o.mean():.6f},{d_p.mean():.6f},{d_r.mean():.6f},{pr:.4f},{lo:.6f},{hi:.6f},{d_s:.6f},{d_a:.6f}" + tail)
    print(f"   replicate {rep + 1}/{N_REP} ({time.time() - t0:.0f}s)", flush=True)

# ---------------------------------------------------------------- the check against B17b, and the tables
A = {est: {k: np.array(v) for k, v in acc[est].items()} for est in ESTS}
m17 = re.search(r"\| \(i\) Δa \(post filter\) \| W60 \| [^|]* \| ([+−-]?\d\.\d+) ± (\d\.\d+) \| ([+−-]?\d\.\d+) ± (\d\.\d+) \| ([+−-]?\d\.\d+) ± (\d\.\d+) \|[^|]*\|[^|]*\| ([+−-]?\d\.\d+) ± (\d\.\d+) \|", CFT)
b17b = {}
if m17 is None:
    check("B17b's condition (i) W60 row located in calibration_filtered_tables.md", nan, 0)
else:
    g = [float(x.replace("−", "-")) for x in m17.groups()]
    b17b = {"sts": (g[0], g[1]), "pred": (g[2], g[3]), "res": (g[4], g[5]), "anti": (g[6], g[7])}
    for k, (m, sd) in b17b.items():
        check(f"(i) W60 {k} DiD within one of B17b's replicate SDs of B17b's mean ({m:+.5f} ± {sd:.5f})", abs(A["W60"][k].mean() - m), sd)
lines = ["# The pure-autocorrelation expectations of the new statistics on the band-passed generator (partB24_bandpassed_expectations.py)", f"git={SHA}", "",
         f"B17b's generator at its solved parameters (β̄ = {BMEAN}, σ_q = {QSD}, β̄_post = {BMEAN_POST}, read from calibration_filtered_tables.md; filter {LO:.4f}–{HI:.3f} Hz), condition (i) only: "
         f"{N_REP} replicates × {N_SUBJ} subjects × 2 runs × {T} samples × {N_PAIRS} pairs, the DMT run spliced at sample {CHANGE_AT}. Seed {SEED}. ± is the SD over replicates. "
         "DiD = windows 6–14 minus 1–4 (bins 11–28 minus 1–8), DMT minus placebo; level = the DMT pre-injection mean.", ""]
n_fail = sum(1 for c in CHECKS if not c[3])
lines += [f"Checks: {len(CHECKS)} run, {n_fail} failed" + ("" if n_fail == 0 else " — listed as CHECK FAILED under Checks") + ".", "",
          "## The check against B17b's condition (i), W = 60", "", "| DiD | B24 (mean ± SD) | B17b (committed) | within one of B17b's SDs |", "|---|---|---|---|"]
for k, lab in (("sts", "observed sts"), ("pred", "AR(1)-substituted sts"), ("res", "residual"), ("anti", "RMS δ_anti")):
    if k in b17b:
        lines.append(f"| {lab} | {A['W60'][k].mean():+.5f} ± {A['W60'][k].std():.5f} | {b17b[k][0]:+.5f} ± {b17b[k][1]:.5f} | {'yes' if abs(A['W60'][k].mean() - b17b[k][0]) <= b17b[k][1] else 'no'} |")
lines += ["", "## B17b's statistics, condition (i)", "",
          "| estimator | sts level (pre) | sts DiD | predicted DiD | residual DiD | residual p (mean; share < 0.05) | δ_sym DiD | RMS δ_anti DiD |", "|---|---|---|---|---|---|---|---|"]
for est in ESTS:
    a = A[est]
    lines.append(f"| {est} | {a['lvl'].mean():.4f} | {a['sts'].mean():+.4f} ± {a['sts'].std():.4f} | {a['pred'].mean():+.4f} ± {a['pred'].std():.4f} | {a['res'].mean():+.4f} ± {a['res'].std():.4f} | "
                 f"{a['p'].mean():.3f}; {np.mean(a['p'] < 0.05):.2f} | {cell(a['sym'])} | {cell(a['anti'])} |")
lines += ["", "## B22's statistics under a pure autocorrelation change (W = 60)", "", "| statistic | DMT pre-injection level | DiD |", "|---|---|---|"]
for k in NEW:
    lv, dd = np.array(acc_new[k]["lvl"]), np.array(acc_new[k]["did"])
    lines.append(f"| {NEW_NAMES[k]} | {lv.mean():+.5f} ± {lv.std():.5f} | {dd.mean():+.5f} ± {dd.std():.5f} |")
sm = np.array(sym_minus)
lines += ["", f"Sym's DiD minus (the residual DiD − D's DiD): {sm.mean():+.5f} ± {sm.std():.5f}.", ""]
lines += ["## Checks", ""] + [f"- {'ok' if ok else 'CHECK FAILED'}: {n} (|difference| {d:.3g}, tolerance {t:.1g})" for n, d, t, ok in CHECKS]
lines += ["", "## Prediction and rule (pre-run entry, B24)", "",
          "Prediction: the check passes; the A_other DiD within ±0.0005, the A_same DiD within ±0.001, the B DiD within ±0.003; the D DiD −0.002 to −0.006; Sym's DiD equal to the residual DiD minus D's within 0.001.",
          "Rule: these are the pure-autocorrelation expectations against which B22's DiDs are read."]
(OUT / "bandpassed_expectations.csv").write_text(f"# partB24_bandpassed_expectations.py; one row per estimator × replicate; git={SHA}\n" + "\n".join(csv) + "\n")
(OUT / "bandpassed_expectations_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines))
print(f"   checks: {len(CHECKS)} run, {n_fail} failed")
print(f"done ({time.time() - t0:.0f}s)")
