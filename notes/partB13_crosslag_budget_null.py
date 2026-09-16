"""
partB13_crosslag_budget_null.py — the cross-lag budget on the finite-sample null, the two controls, and the
null-corrected budget of the data with its reading under the rules recorded before the run (16 Sep 2026; pre-run
entry "The cross-lag budget: pre-run entry, 16 Sep 2026" in manuscript/analysis_record.md). Definitions and the shared
scoring function: notes/rev_crosslag_budget.py; the data terms: partB12_crosslag_budget.py (run first).

Null. The filter family and gen() of notes/review_v2_residual_null.py, imported and not modified: each pair is one
linear filter (band-pass × exp(−β f²), β per pair ~ N(β̄, h β̄), clipped at 5) applied to two white noises with
correlation q drawn per pair, so the population cross-lag correlation is exactly r₁q and every deviation is finite
sampling. gen() draws from that module's generator, which this script sets to np.random.default_rng([20261120, k])
for configuration k before the fresh draws (the solver uses np.random.default_rng([20261120, k, 1000 + t]) for run
type t, re-created at every evaluation: common random numbers, so the solver's objective is a deterministic function
of its parameters). Runs of T = 840 TRs are simulated and cut into the same 14 windows of 60, so each simulated
pair's s comes from its own run-level q̂. Operating points per run type (DMT, placebo); the null value of a term is
the mean over the two run types, as the data's grand mean is, and per run type for rule (e). The solver runs on
4,000 pair-runs; then ≥ 25,000 fresh pair-runs per run type per configuration are drawn in batches of 5,000 (more
until the Monte-Carlo SE of δ_run is ≤ 0.0003, at most 100,000).
Configurations (k). 0, primary: h = 0.5; the DMT-post ACF filter for DMT runs and the placebo ACF filter for placebo
runs (the fits of the null's own fit_filter); q from a zero-mean two-component Gaussian mixture, one component of SD
0.02 with weight w, the other of SD σ₂, with (β̄, w, σ₂) solved so that the null's run-level mean pair a, mean |q̂|
and fraction |q̂| < 0.05 equal the data's for that run type. One at a time: 1, h = 0.25; 2, h = 1.0; 3, the placebo
ACF filter for both run types; 4, q ~ N(0, σ_q) with (β̄, σ_q) solved to the run-level mean a and |q̂|; 5, the mixture
solved to the run type's W = 60 window-level means (a, |q̂|, fraction |q̂| < 0.05 over pair-windows). The targets and
the fractions printed beside every configuration (q̂ < 0, |q̂| < 0.05, |q̂| < 0.10, run level and window level) are
computed from the data (ts_gsr; nothing else is computed from the data here).
Controls, at the primary configuration's parameters, report-only. (i) Common drive: x = √(1 − λ) n_x + √λ s,
y = √(1 − λ) n_y ± √λ s, λ = 0.2, loading sign random per pair; n_x, n_y, s from the same filter family (regional
parts at the solved β̄ with h = 0.5; the shared part at β_s, solved so that its lag-1 autocorrelation is 0.10 above
the regional parts' at β̄, with the same relative heterogeneity), each scaled to unit variance by its filter's
analytic variance. (ii) Pooling: each pair's q and filter change at TR 240, by pair-specific draws: TRs 0–239 at
β₁ ~ N(6 β̄, h·6 β̄) with q₁ from the primary mixture; TRs 240–839 at β₂ ~ N(β̄/5, h·β̄/5) with q₂ = q₁(1 − g),
g ~ U(0.5, 1), the two segments generated as full-length runs and spliced at TR 240.
Null-corrected value of a term: data minus null, same term, same configuration; the null value is fixed in the CIs
(the data interval shifted). The reading applies rules (a)–(f) of the pre-run entry mechanically and prints the branch.

Outputs: notes/review_results/partB/crosslag_budget_null_tables.md, crosslag_budget_null.csv (one row per
configuration × run type × term, value and Monte-Carlo SE), crosslag_budget_null_run.log (via run_all.sh's nstep, or
stdout).
Run from the repository root: .venv/bin/python notes/partB13_crosslag_budget_null.py   (about ten minutes)
        --dry: 50 pair-runs, fixed parameters, no data, no statistic printed (shape and finiteness checks only)
"""
import subprocess
import sys
import time
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import brentq

sys.path.insert(0, str(Path(__file__).resolve().parent))
import review_v2_residual_null as NULL                       # seeds its own generator at import; replaced below
from rev_crosslag_budget import (budget_terms, mats_from_series, c4_series, aggregate, boot_idx_variants, signflip_p,
                                 fmt_agg, TERMS, SEED, N_BOOT)

DRY = "--dry" in sys.argv
REPO = Path(__file__).resolve().parents[1]
MAT = REPO / "external" / "DMT_NCT" / "data" / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
OUT = REPO / "notes" / "review_results" / "partB"
OUT.mkdir(parents=True, exist_ok=True)
REGIONS = np.array([r for r in range(116) if r != 20])
RUN_TYPES = ("DMT", "PCB")
T_RUN, W, NW = 840, 60, 14
N_SOLVE, N_MIN, BATCH, SE_MAX, N_MAX = (4000, 25000, 5000, 0.0003, 100000) if not DRY else (50, 50, 50, 1.0, 50)
TERM_LIST = TERMS
LAM_CD, DA_CD = 0.2, 0.10                                   # control (i)
K1_POOL, K2_POOL, G_LO, G_HI, T_SWITCH = 6.0, 0.2, 0.5, 1.0, 240   # control (ii)
CONFIGS = [
    dict(k=0, name="primary: h = 0.5, DMT-post/placebo ACF, mixture q solved to run-level a, |q̂|, fraction |q̂| < 0.05", het=0.5, acf={"DMT": "DMTpost", "PCB": "placebo"}, qmodel="mixture", level="run"),
    dict(k=1, name="heterogeneity h = 0.25", het=0.25, acf={"DMT": "DMTpost", "PCB": "placebo"}, qmodel="mixture", level="run"),
    dict(k=2, name="heterogeneity h = 1.0", het=1.0, acf={"DMT": "DMTpost", "PCB": "placebo"}, qmodel="mixture", level="run"),
    dict(k=3, name="placebo ACF for both run types", het=0.5, acf={"DMT": "placebo", "PCB": "placebo"}, qmodel="mixture", level="run"),
    dict(k=4, name="q ~ N(0, σ_q) solved to run-level a and |q̂|", het=0.5, acf={"DMT": "DMTpost", "PCB": "placebo"}, qmodel="gaussian", level="run"),
    dict(k=5, name="mixture solved to the W = 60 window-level means", het=0.5, acf={"DMT": "DMTpost", "PCB": "placebo"}, qmodel="mixture", level="window"),
]

try:
    sha = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], text=True, cwd=REPO).strip()
    if subprocess.check_output(["git", "status", "--porcelain", "--", "scripts", "notes/*.py", "manuscript/analysis_record.md"],
                               text=True, cwd=REPO).strip():
        sha += "-dirty"
except Exception:
    sha = "nogit"

FITS = {k: NULL.fit_filter(t) for k, t in NULL.TARGET_ACF.items()}          # (err, beta, lo, hi, acf)
FREQ = np.fft.rfftfreq(T_RUN, d=NULL.TR)


def filter_var(betas, lo, hi):
    """Analytic variance of gen()'s output for white noise of unit variance: (1/T) Σ over the full spectrum of |H|²."""
    w = NULL.psd_weights(FREQ, np.asarray(betas, float), lo, hi)             # (n, T/2 + 1)
    return (w[:, 0] + w[:, -1] + 2 * w[:, 1:-1].sum(1)) / T_RUN


def draw_q(qmodel, params, n, rng):
    if qmodel == "gaussian":
        return np.clip(params["sigq"] * rng.standard_normal(n), -0.95, 0.95)
    u = rng.uniform(size=n)
    z1 = rng.standard_normal(n)
    z2 = rng.standard_normal(n)
    return np.clip(np.where(u < params["w"], 0.02 * z1, params["sig2"] * z2), -0.95, 0.95)


def simulate(n, run_type, cfg, params, rng):
    lo, hi = FITS[cfg["acf"][run_type]][2], FITS[cfg["acf"][run_type]][3]
    betas = np.clip(rng.normal(params["beta"], cfg["het"] * params["beta"], n), 5, None)
    q = draw_q(cfg["qmodel"], params, n, rng)
    NULL.rng = rng
    X, Y = NULL.gen(n, T_RUN, betas, lo, hi, q)
    return X, Y


def level_stats(X, Y, level):
    """mean a, mean |q̂|, fractions, at the run level or over pair-windows."""
    if level == "run":
        C = c4_series(X, Y)
    else:
        n = X.shape[0]
        C = np.concatenate([c4_series(X[:, w * W:(w + 1) * W], Y[:, w * W:(w + 1) * W]) for w in range(NW)], 0)
    a = 0.5 * (C[:, 0, 2] + C[:, 1, 3])
    q = 0.5 * (C[:, 0, 1] + C[:, 2, 3])
    return dict(a=a.mean(), absq=np.abs(q).mean(), fneg=(q < 0).mean(), f05=(np.abs(q) < 0.05).mean(), f10=(np.abs(q) < 0.10).mean())


def solver_rng(k, t):
    return np.random.default_rng([SEED, k, 1000 + t])


def solve(cfg, run_type, t, targets, log):
    """(β̄, q parameters) for one configuration and run type, with common random numbers."""
    k, level = cfg["k"], cfg["level"]
    tg = targets[run_type][level]
    notes = []

    def stats(params):
        X, Y = simulate(N_SOLVE, run_type, cfg, params, solver_rng(k, t))
        return level_stats(X, Y, level)

    base = dict(w=0.2, sig2=0.25, sigq=0.25)
    beta = brentq(lambda b: stats(dict(base, beta=b))["a"] - tg["a"], 5.0, 4000.0, xtol=1.0)
    params = dict(beta=beta)
    if cfg["qmodel"] == "gaussian":
        params["sigq"] = brentq(lambda s_: stats(dict(params, sigq=s_))["absq"] - tg["absq"], 0.01, 0.95, xtol=1e-4)
    else:
        def sig2_for(w_):
            f = lambda s2: stats(dict(params, w=w_, sig2=s2))["absq"] - tg["absq"]
            if f(0.01) >= 0:
                return 0.01
            if f(0.95) <= 0:
                return 0.95
            return brentq(f, 0.01, 0.95, xtol=1e-4)

        def frac_gap(w_):
            return stats(dict(params, w=w_, sig2=sig2_for(w_)))["f05"] - tg["f05"]
        g0, g1 = frac_gap(0.0), frac_gap(0.9)
        if g0 >= 0:
            w_star = 0.0
            notes.append("fraction |q̂| < 0.05 reached or exceeded with no narrow component: w set to 0")
        elif g1 <= 0:
            w_star = 0.9
            notes.append("fraction |q̂| < 0.05 not reached at w = 0.9: w set to 0.9")
        else:
            w_star = brentq(frac_gap, 0.0, 0.9, xtol=0.005)
        params["w"] = w_star
        params["sig2"] = sig2_for(w_star)
    achieved = stats(params)
    log.append(f"   solved {run_type} (k = {k}, targets at the {level} level: a {tg['a']:.4f}, |q̂| {tg['absq']:.4f}, fraction |q̂| < 0.05 {tg['f05']:.3f}): "
               + ", ".join(f"{kk} = {vv:.4f}" for kk, vv in params.items())
               + f"; achieved on the solver batch a {achieved['a']:.4f}, |q̂| {achieved['absq']:.4f}, fraction {achieved['f05']:.3f}"
               + ("; " + "; ".join(notes) if notes else ""))
    return params


def terms_of(X, Y):
    C_run, C_wd, C_win, sd_win, n_win, s = mats_from_series(X, Y, W)
    return budget_terms(C_run, C_wd, C_win, sd_win, n_win, s)


def collect(draw_fn, n_min, se_key="run"):
    """draw batches with draw_fn(n) -> (X, Y) until n ≥ n_min and SE(δ_run) ≤ SE_MAX (at most N_MAX)."""
    acc = {k: [] for k in TERM_LIST + ("a", "absq", "q")}
    n = 0
    while True:
        m = min(BATCH, N_MAX - n)
        X, Y = draw_fn(m)
        o = terms_of(X, Y)
        for k in acc:
            acc[k].append(o[k])
        n += m
        se = np.std(np.concatenate(acc[se_key]), ddof=1) / np.sqrt(n) if n > 1 else np.inf
        if (n >= n_min and se <= SE_MAX) or n >= N_MAX:
            break
    return {k: np.concatenate(v) for k, v in acc.items()}


def summarise(acc):
    n = acc["run"].size
    out = {k: (acc[k].mean(), acc[k].std(ddof=1) / np.sqrt(n)) for k in TERM_LIST}
    q = acc["q"]
    out["desc"] = dict(a=acc["a"].mean(), absq=acc["absq"].mean(), fneg=(q < 0).mean(), f05=(acc["absq"] < 0.05).mean(), f10=(acc["absq"] < 0.10).mean(), n=n)
    return out


def combine(sd, sp):
    """null value of a term: mean over the two run types; SE from both."""
    return {k: (0.5 * (sd[k][0] + sp[k][0]), 0.5 * np.sqrt(sd[k][1] ** 2 + sp[k][1] ** 2)) for k in TERM_LIST}


def fmt_terms(d, digits=5):
    return "  ".join(f"{k} {d[k][0]:+.{digits}f} ± {d[k][1]:.{digits}f}" for k in TERM_LIST)


# ------------------------------------------------------------------------------------------ data targets (ts_gsr)
t0 = time.time()
lines = [f"# The cross-lag budget on the finite-sample null, the controls, and the null-corrected budget of the data (partB13_crosslag_budget_null.py; git={sha}; seed={SEED})", ""]
if DRY:
    targets = {rt: {"run": dict(a=0.866, absq=0.19, fneg=0.54, f05=0.2, f10=0.35), "window": dict(a=0.86, absq=0.28, fneg=0.5, f05=0.12, f10=0.24)} for rt in RUN_TYPES}
else:
    import scipy.io as sio
    from rev_phiid_fast import PairPhiID
    ts = sio.loadmat(MAT)["ts_gsr"]
    targets = {}
    for c, rt in enumerate(RUN_TYPES):
        run_a, run_q, win_a, win_q = [], [], [], []
        for s_i in range(14):
            X = np.asarray(ts[s_i, c], float)[REGIONS]
            kept = np.where(np.all(np.isfinite(X), axis=0))[0]
            C = PairPhiID(X[:, kept]).C
            run_a.append(0.5 * (C[:, 0, 2] + C[:, 1, 3])); run_q.append(0.5 * (C[:, 0, 1] + C[:, 2, 3]))
            for w in range(NW):
                in_w = kept[(kept >= w * W) & (kept < (w + 1) * W)]
                Cw = PairPhiID(X[:, in_w]).C
                win_a.append(0.5 * (Cw[:, 0, 2] + Cw[:, 1, 3])); win_q.append(0.5 * (Cw[:, 0, 1] + Cw[:, 2, 3]))
        tg = {}
        for level, aa, qq in (("run", run_a, run_q), ("window", win_a, win_q)):
            aa, qq = np.concatenate(aa), np.concatenate(qq)
            tg[level] = dict(a=aa.mean(), absq=np.abs(qq).mean(), fneg=(qq < 0).mean(), f05=(np.abs(qq) < 0.05).mean(), f10=(np.abs(qq) < 0.10).mean())
        targets[rt] = tg
    lines.append("Data targets (ts_gsr), computed here: " + "; ".join(
        f"{rt} {level} level: mean a {tg[level]['a']:.4f}, mean |q̂| {tg[level]['absq']:.4f}, fraction q̂ < 0 {tg[level]['fneg']:.3f}, |q̂| < 0.05 {tg[level]['f05']:.3f}, |q̂| < 0.10 {tg[level]['f10']:.3f}"
        for rt, tg in targets.items() for level in ("run", "window")))
    lines.append("")
    print("\n".join(lines), flush=True)
lines.append("Filter fits (the null's own fit_filter): " + "; ".join(f"{k}: β = {b[1]:.0f}, band {b[2]:.4f}–{b[3]:.3f} Hz" for k, b in FITS.items()))
lines.append("")

# ------------------------------------------------------------------------------------------ configurations
null = {}                                                    # k -> {"DMT": summary, "PCB": summary, "both": combined}
params_all = {}
csv_rows = []
for cfg in CONFIGS:
    k = cfg["k"]
    lines.append(f"## Configuration {k}: {cfg['name']}")
    lines.append("")
    params_all[k] = {}
    fresh = np.random.default_rng([SEED, k])
    summ = {}
    for t, rt in enumerate(RUN_TYPES):
        if DRY:
            params = dict(beta=FITS[cfg["acf"][rt]][1], w=0.2, sig2=0.25, sigq=0.25)
        else:
            params = solve(cfg, rt, t, targets, lines)
        params_all[k][rt] = params
        acc = collect(lambda n: simulate(n, rt, cfg, params, fresh), N_MIN)
        summ[rt] = summarise(acc)
        if DRY:
            for kk in TERM_LIST:
                assert np.isfinite(acc[kk]).all() and acc[kk].shape == (N_MIN,)
            continue
        d = summ[rt]["desc"]
        tg = targets[rt]["run"]
        lines.append(f"   {rt} ({d['n']} pair-runs): null run-level mean a {d['a']:.4f} (data {tg['a']:.4f}), mean |q̂| {d['absq']:.4f} (data {tg['absq']:.4f}), fraction q̂ < 0 {d['fneg']:.3f} "
                     f"(data {tg['fneg']:.3f}), |q̂| < 0.05 {d['f05']:.3f} (data {tg['f05']:.3f}), |q̂| < 0.10 {d['f10']:.3f} (data {tg['f10']:.3f})")
        lines.append(f"   {rt} terms (mean ± Monte-Carlo SE): " + fmt_terms(summ[rt]))
        for kk in TERM_LIST:
            csv_rows.append(dict(configuration=k, run_type=rt, term=kk, value=summ[rt][kk][0], se=summ[rt][kk][1], n=d["n"]))
    both = combine(summ["DMT"], summ["PCB"])
    null[k] = dict(DMT=summ["DMT"], PCB=summ["PCB"], both=both)
    if not DRY:
        lines.append("   null value (mean over the two run types): " + fmt_terms(both))
        for kk in TERM_LIST:
            csv_rows.append(dict(configuration=k, run_type="both", term=kk, value=both[kk][0], se=both[kk][1], n=summ["DMT"]["desc"]["n"] + summ["PCB"]["desc"]["n"]))
        lines.append("")
        print("\n".join(lines[-6:]), f"({time.time() - t0:.0f} s)", flush=True)

# ------------------------------------------------------------------------------------------ controls (primary parameters)
ctrl = {}
lines.append("## Controls at the primary configuration's parameters (report-only)")
lines.append("")
for t, rt in enumerate(RUN_TYPES):
    cfg = CONFIGS[0]
    params = params_all[0][rt]
    lo, hi = FITS[cfg["acf"][rt]][2], FITS[cfg["acf"][rt]][3]
    het, bmean = cfg["het"], params["beta"]
    # (i) common drive
    a_n = NULL.acf_of(bmean, lo, hi)[1]
    beta_s = brentq(lambda b: NULL.acf_of(b, lo, hi)[1] - (a_n + DA_CD), bmean, 50000.0)
    a_s = NULL.acf_of(beta_s, lo, hi)[1]
    rng_cd = np.random.default_rng([SEED, 101, t])

    def draw_cd(n):
        betas = np.clip(rng_cd.normal(bmean, het * bmean, n), 5, None)
        betas_s = np.clip(rng_cd.normal(beta_s, het * beta_s, n), 5, None)
        load = rng_cd.choice([-1.0, 1.0], n)
        NULL.rng = rng_cd
        nx, ny = NULL.gen(n, T_RUN, betas, lo, hi, np.zeros(n))
        sh, _ = NULL.gen(n, T_RUN, betas_s, lo, hi, np.zeros(n))
        vn, vs = filter_var(betas, lo, hi), filter_var(betas_s, lo, hi)
        draw_cd.var_ratio = (nx.var(1) / vn).mean(), (sh.var(1) / vs).mean()
        nx, ny, sh = nx / np.sqrt(vn)[:, None], ny / np.sqrt(vn)[:, None], sh / np.sqrt(vs)[:, None]
        X = np.sqrt(1 - LAM_CD) * nx + np.sqrt(LAM_CD) * sh
        Y = np.sqrt(1 - LAM_CD) * ny + np.sqrt(LAM_CD) * load[:, None] * sh
        return X, Y
    acc = collect(draw_cd, N_MIN)
    ctrl[("cd", rt)] = summarise(acc)
    # (ii) pooling
    rng_pl = np.random.default_rng([SEED, 102, t])
    a1_pop, a2_pop = NULL.acf_of(K1_POOL * bmean, lo, hi)[1], NULL.acf_of(K2_POOL * bmean, lo, hi)[1]

    def draw_pl(n):
        b1 = np.clip(rng_pl.normal(K1_POOL * bmean, het * K1_POOL * bmean, n), 5, None)
        b2 = np.clip(rng_pl.normal(K2_POOL * bmean, het * K2_POOL * bmean, n), 5, None)
        q1 = draw_q("mixture", params, n, rng_pl)
        g = rng_pl.uniform(G_LO, G_HI, n)
        q2 = q1 * (1 - g)
        NULL.rng = rng_pl
        X1, Y1 = NULL.gen(n, T_RUN, b1, lo, hi, q1)
        X2, Y2 = NULL.gen(n, T_RUN, b2, lo, hi, q2)
        X = np.concatenate([X1[:, :T_SWITCH], X2[:, T_SWITCH:]], 1)
        Y = np.concatenate([Y1[:, :T_SWITCH], Y2[:, T_SWITCH:]], 1)
        C1, C2 = c4_series(X[:, :T_SWITCH], Y[:, :T_SWITCH]), c4_series(X[:, T_SWITCH:], Y[:, T_SWITCH:])
        draw_pl.seg = ((0.5 * (C1[:, 0, 2] + C1[:, 1, 3])).mean(), np.abs(0.5 * (C1[:, 0, 1] + C1[:, 2, 3])).mean(),
                       (0.5 * (C2[:, 0, 2] + C2[:, 1, 3])).mean(), np.abs(0.5 * (C2[:, 0, 1] + C2[:, 2, 3])).mean())
        return X, Y
    acc2 = collect(draw_pl, N_MIN)
    ctrl[("pool", rt)] = summarise(acc2)
    if DRY:
        for kk in TERM_LIST:
            assert np.isfinite(acc[kk]).all() and np.isfinite(acc2[kk]).all()
        continue
    d1, d2 = ctrl[("cd", rt)], ctrl[("pool", rt)]
    lines.append(f"   (i) common drive, {rt}: λ = {LAM_CD}, regional parts at β̄ = {bmean:.1f} (population lag-1 a_n = {a_n:.4f}), shared part at β_s = {beta_s:.1f} "
                 f"(a_s = {a_s:.4f}); population d = λ(1 − λ)(a_s − a_n) = {LAM_CD * (1 - LAM_CD) * (a_s - a_n):+.5f}; empirical/analytic variance ratios "
                 f"{draw_cd.var_ratio[0]:.4f} (regional), {draw_cd.var_ratio[1]:.4f} (shared); realised run-level mean a {d1['desc']['a']:.4f}, |q̂| {d1['desc']['absq']:.4f}; "
                 f"{d1['desc']['n']} pair-runs")
    lines.append("      terms: " + fmt_terms(d1) + "; shares of δ_run: " + ", ".join(f"{kk} {d1[kk][0] / d1['run'][0]:+.3f}" for kk in ("within", "pool", "means", "eps")))
    lines.append(f"   (ii) pooling, {rt}: TRs 0–239 at β₁ ~ N({K1_POOL} β̄, h·{K1_POOL} β̄) (population lag-1 {a1_pop:.4f}) with q₁ from the primary mixture; TRs 240–839 at "
                 f"β₂ ~ N(β̄/{1 / K2_POOL:.0f}, h·β̄/{1 / K2_POOL:.0f}) (population lag-1 {a2_pop:.4f}) with q₂ = q₁(1 − g), g ~ U({G_LO}, {G_HI}); last batch's segment means: "
                 f"a {draw_pl.seg[0]:.4f}, |q̂| {draw_pl.seg[1]:.4f} before TR 240 and a {draw_pl.seg[2]:.4f}, |q̂| {draw_pl.seg[3]:.4f} after; realised run-level mean a "
                 f"{d2['desc']['a']:.4f}, |q̂| {d2['desc']['absq']:.4f}; {d2['desc']['n']} pair-runs")
    lines.append("      terms: " + fmt_terms(d2) + "; shares of δ_run: " + ", ".join(f"{kk} {d2[kk][0] / d2['run'][0]:+.3f}" for kk in ("within", "pool", "means", "eps"))
                 + f"; δ_pool = {d2['pool'][0] / d2['pool'][1]:.1f} Monte-Carlo SEs")
    for name, dd in (("common drive", d1), ("pooling", d2)):
        for kk in TERM_LIST:
            csv_rows.append(dict(configuration="control " + name, run_type=rt, term=kk, value=dd[kk][0], se=dd[kk][1], n=dd["desc"]["n"]))
    print("\n".join(lines[-4:]), f"({time.time() - t0:.0f} s)", flush=True)
if not DRY:
    for name in ("cd", "pool"):
        both = combine(ctrl[(name, "DMT")], ctrl[(name, "PCB")])
        ctrl[(name, "both")] = both
        lines.append(f"   {'(i) common drive' if name == 'cd' else '(ii) pooling'}, mean over run types: " + fmt_terms(both)
                     + "; shares: " + ", ".join(f"{kk} {both[kk][0] / both['run'][0]:+.3f}" for kk in ("within", "pool", "means", "eps")))
    lines.append("")

if DRY:
    print(f"dry run ok: configurations {len(null)}, controls {len(ctrl)}, shapes and finiteness asserted; no statistic printed ({time.time() - t0:.0f} s)")
    sys.exit(0)

# ------------------------------------------------------------------------------------------ null-corrected budget and reading
lines.append("## Null-corrected budget of the data and the reading under the pre-run entry")
lines.append("")
data = pd.read_csv(OUT / "crosslag_budget.csv")
idx = boot_idx_variants()
per_run = {}
for var in ("ts_gsr", "ts_demean"):
    d = data[data.variant == var]
    per_run[var] = {}
    for kk in TERM_LIST:
        arr = np.full((14, 2), np.nan)
        for _, r in d.iterrows():
            arr[int(r.subject) - 1, RUN_TYPES.index(r.condition)] = r["delta_" + kk]
        per_run[var][kk] = arr
agg = {var: {kk: aggregate(per_run[var][kk], idx[var]) for kk in TERM_LIST} for var in per_run}
G = agg["ts_gsr"]
run_grand = G["run"]["grand"]
lines.append("Data, ts_gsr (from crosslag_budget.csv, partB12; the same bootstrap draws): " + "  ".join(f"δ_{kk} {G[kk]['grand']:+.5f} [{G[kk]['lo']:+.5f}, {G[kk]['hi']:+.5f}]" for kk in TERM_LIST))
lines.append("")

# (a) finite sampling
F = {k: null[k]["both"]["run"][0] / run_grand for k in null}
se2 = {k: 2 * null[k]["both"]["run"][1] for k in null}
if all(abs(null[k]["both"]["run"][0]) <= se2[k] for k in null):
    a_branch = "none"
elif all(null[k]["both"]["run"][0] < -se2[k] for k in null):
    a_branch = "opposing"
elif all(0 < F[k] <= 1 / 3 for k in null):
    a_branch = "a minor part"
elif all(F[k] >= 2 / 3 for k in null):
    a_branch = "most"
else:
    a_branch = "range"
lines.append("(a) Finite sampling. δ_run,null by configuration: " + "; ".join(f"k = {k}: {null[k]['both']['run'][0]:+.5f} ± {null[k]['both']['run'][1]:.5f} (F = {F[k]:.3f})" for k in null)
             + f". Branch: {a_branch}" + ("" if a_branch != "range" else f" — F from {min(F.values()):.3f} to {max(F.values()):.3f}; (b)–(e) are read with it") + ". The 10:32 UTC reading, as recorded: \"near zero (+0.00025, 7.3 % of +0.00340): finite sampling is removed as a source of the signature\".")
lines.append("")

# (b) apportioning
corr = {}
labels = {kk: {} for kk in ("within", "pool", "means")}
shares = {kk: {} for kk in ("within", "pool", "means")}
gate_ok, reversed_all, eps_fail = True, True, []
for k in null:
    nb = null[k]["both"]
    c = {kk: dict(grand=G[kk]["grand"] - nb[kk][0], lo=G[kk]["lo"] - nb[kk][0], hi=G[kk]["hi"] - nb[kk][0]) for kk in TERM_LIST}
    corr[k] = c
    if not c["run"]["lo"] > 0:
        gate_ok = False
    if not c["run"]["hi"] < 0:
        reversed_all = False
    if abs(c["eps"]["grand"]) > c["run"]["grand"] / 10:
        eps_fail.append(k)
    sh = {kk: c[kk]["grand"] / c["run"]["grand"] for kk in ("within", "pool", "means", "eps")}
    for kk in ("within", "pool", "means"):
        shares[kk][k] = sh[kk]
        half = 0.5 * (c[kk]["hi"] - c[kk]["lo"])
        others = [sh[o] for o in ("within", "pool", "means") if o != kk and sh[o] > 0]
        if half > c["run"]["grand"] / 3:
            lab = "undetermined at N = 14"
        elif c[kk]["lo"] <= 0 <= c[kk]["hi"]:
            lab = "absent"
        elif c[kk]["hi"] < 0:
            lab = "opposing"
        elif sh[kk] >= 2 / 3 and all(o < 1 / 3 for o in others):
            lab = "most"
        elif sh[kk] >= 1 / 3:
            lab = "part"
        else:
            lab = "a minor part"
        labels[kk][k] = lab
    lines.append(f"k = {k}, null-corrected: " + "  ".join(f"δ_{kk},c {c[kk]['grand']:+.5f} [{c[kk]['lo']:+.5f}, {c[kk]['hi']:+.5f}]" for kk in ("run", "within", "pool", "means", "eps"))
                 + "; shares " + ", ".join(f"{kk} {sh[kk]:+.3f}" for kk in ("within", "pool", "means", "eps"))
                 + "; labels " + ", ".join(f"{kk}: {labels[kk][k]}" for kk in ("within", "pool", "means")))
    csv_rows += [dict(configuration=k, run_type="null-corrected", term=kk, value=c[kk]["grand"], se=np.nan, n=np.nan, ci_lo=c[kk]["lo"], ci_hi=c[kk]["hi"]) for kk in TERM_LIST]
validity = {"within": ctrl[("pool", "both")]["within"][0] / ctrl[("pool", "both")]["run"][0] >= 1 / 3,
            "pool": ctrl[("cd", "both")]["pool"][0] / ctrl[("cd", "both")]["run"][0] >= 1 / 3,
            "means": ctrl[("cd", "both")]["means"][0] / ctrl[("cd", "both")]["run"][0] >= 1 / 3}
if gate_ok:
    gate_text = "gate passed: the CI of δ_run,c lies above zero in every configuration"
elif reversed_all:
    gate_text = "reversed: the CI of δ_run,c lies below zero in every configuration"
else:
    gate_text = "no positive null-corrected signature to apportion (the CI of δ_run,c does not lie above zero in every configuration)"
eps_text = ("ε check passed in every configuration (|ε_c| ≤ δ_run,c / 10)" if not eps_fail
            else f"ε check failed in configuration(s) {eps_fail}: |ε_c| > δ_run,c / 10 there, so the budget is reported and not read")
final = {}
for kk in ("within", "pool", "means"):
    labs = set(labels[kk].values())
    if len(labs) == 1:
        lab = labs.pop()
        if lab == "most" and validity[kk]:
            lab = f"no \"most\" reading (validity clause: the control puts ≥ 1/3 in δ_{kk}); shares {min(shares[kk].values()):+.3f} to {max(shares[kk].values()):+.3f}"
    else:
        lab = f"no single label across configurations; shares {min(shares[kk].values()):+.3f} to {max(shares[kk].values()):+.3f}"
    final[kk] = lab
read_b = gate_ok and not eps_fail and a_branch != "most"
lines.append(f"(b) Apportioning. {gate_text}; {eps_text}; validity from the controls: control (i) shares pool {ctrl[('cd', 'both')]['pool'][0] / ctrl[('cd', 'both')]['run'][0]:+.3f}, "
             f"means {ctrl[('cd', 'both')]['means'][0] / ctrl[('cd', 'both')]['run'][0]:+.3f}; control (ii) share within {ctrl[('pool', 'both')]['within'][0] / ctrl[('pool', 'both')]['run'][0]:+.3f}. "
             + ("Read: " if read_b else "Reported, not read (see above): ") + "; ".join(f"δ_{kk}: {final[kk]}" for kk in ("within", "pool", "means")) + ".")
lines.append("")
# (c) readings
if read_b:
    if final["within"] == "most":
        c_text = ("δ_within most: the signature is present inside 2-minute windows, where pooling across windows cannot act. The candidates are common slow drive or lagged coupling "
                  "(not separable at τ = 1), non-stationarity faster than 2 minutes, or a within-window finite-sample effect that the null as specified does not reproduce. Pooling is not the principal account.")
    elif final["pool"] == "most":
        c_text = "δ_pool most: pooling is the principal account."
    elif final["means"] == "most":
        c_text = "δ_means most: slow variation or drift beyond 2 minutes."
    else:
        c_text = ("no term is \"most\": each share is stated, with the attribution clause of the pre-run entry (a share of δ_pool or δ_means read as \"part\" or \"a minor part\" "
                  "is not evidence of pooling or drift, except under rule (e)).")
else:
    c_text = "not read."
lines.append(f"(c) Reading: {c_text}")
lines.append("")
# (d)
lines.append(f"(d) δ_60 with the run-level sign, data {G['d60']['grand']:+.5f} [{G['d60']['lo']:+.5f}, {G['d60']['hi']:+.5f}], null (primary) {null[0]['both']['d60'][0]:+.5f} ± {null[0]['both']['d60'][1]:.5f}; "
             f"partB10's window-sign value, data {G['d60_winsign']['grand']:+.5f}, null (primary) {null[0]['both']['d60_winsign'][0]:+.5f} ± {null[0]['both']['d60_winsign'][1]:.5f}. "
             "The 10:32 UTC W = 60 reading, as recorded: \"comparable to the run-level +0.00340 (ratio 1.80, within a factor of two): a stationary mechanism is indicated and pooling is not "
             "distinguished by run length\"; superseded for the reasons of the correction note of 16 Sep 2026 (the window's sign selects on the same samples; the null's W = 60 value was read at "
             "a different q̂ density; the ratio compares two differently biased statistics).")
lines.append("")
# (e) run type
e_lines = []
for k in null:
    diffs = {}
    for kk in ("pool", "within", "means"):
        d_sub = per_run["ts_gsr"][kk][:, 0] - per_run["ts_gsr"][kk][:, 1]
        d_null = null[k]["DMT"][kk][0] - null[k]["PCB"][kk][0]
        dc = d_sub - d_null
        diffs[kk] = (dc.mean(), signflip_p(dc), int((dc > 0).sum()))
    dmt_run_c = G["run"]["dmt"] - null[k]["DMT"]["run"][0]
    pool_dc = diffs["pool"]
    if pool_dc[0] > 0 and pool_dc[1] < 0.05:
        verdict = f"pooling is larger on the DMT run: +{pool_dc[0]:.5f}, {pool_dc[0] / dmt_run_c:.2f} of the DMT-run δ_run,c ({dmt_run_c:+.5f})"
    else:
        verdict = "no run-type difference in pooling detected"
    e_lines.append(f"k = {k}: DMT − placebo per subject, null-corrected: δ_pool,c {pool_dc[0]:+.5f} (sign-flip p = {pool_dc[1]:.4f}, positive in {pool_dc[2]}/14) → {verdict}; "
                   f"δ_within,c {diffs['within'][0]:+.5f} (p = {diffs['within'][1]:.4f}), δ_means,c {diffs['means'][0]:+.5f} (p = {diffs['means'][1]:.4f}) (no rule)")
lines.append("(e) Run type (rule applied at the primary configuration k = 0; the others reported). " + " | ".join(e_lines))
lines.append("")
# (f)
D = agg["ts_demean"]
lines.append("(f) ts_demean, data only (no null; not read): " + "  ".join(f"δ_{kk} {D[kk]['grand']:+.5f} [{D[kk]['lo']:+.5f}, {D[kk]['hi']:+.5f}]" for kk in TERM_LIST))
lines.append("")
print("\n".join(lines[-14:]), flush=True)
print(f"done in {time.time() - t0:.0f} s")
pd.DataFrame(csv_rows).to_csv(OUT / "crosslag_budget_null.csv", index=False)
(OUT / "crosslag_budget_null_tables.md").write_text("\n".join(lines) + "\n")
print(f"wrote {OUT / 'crosslag_budget_null_tables.md'} and crosslag_budget_null.csv")
