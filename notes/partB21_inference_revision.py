"""
partB21_inference_revision.py — B21: inverted sign-flip intervals for every quoted mean over subjects, the residual DiD
against its calibrated expectations, the per-subject regressions, and Fisher-z intervals for the correlations.
Pre-run entry: manuscript/analysis_record.md, "Inverted sign-flip intervals, the residual against its calibrated
expectations, the per-subject regressions and the correlation intervals (B21): pre-run entry, 23 Sep 2026" (round 16,
Part A; the specification, predictions and rule of the round-16 commission, restated there).

(a) One row per quantity: its per-subject vector x (N = 14); the exact sign-flip p against 0 and the 95 % interval that
    inverts that test (notes/rev_inference_inverted.py: p(μ) = share of the 2^14 assignments with |Σ sᵢ(xᵢ − μ)| ≥
    |Σ(xᵢ − μ)|, relative tolerance 1e-12; the interval {μ : p(μ) > 0.05}; bounds bisected to 1e-7 after a 2,001-point
    monotonicity grid); the committed percentile interval; the t interval (mean ± t(0.975, 13)·SD/√14); the ratio of the
    inverted to the percentile width; whether zero lies inside each; negative/14; where the text quotes it.
    Groups: "pickle" — every row of every notes/review_results/inference_rows_*.pkl, all sets, from did_subjects;
    "engine" — the per-run post − pre changes, the FD DiD and the FD-residualised DiD recomputed per subject exactly as
    rev_inference.Engine computes them (its window_sets, fd_windows, did and residualise imported), for Table 2 and S1
    Table (MMI-sts W = 60 both variants, W = 30 ts_gsr; primary and sensitivity sets) and for the other per-run and
    FD-residualised values the text quotes (the residual DiD's per-run changes, the FD-residualised CCS-sts and r₁
    DiDs); every recomputation checked against its pickle row (the per-subject DiD and the four means, 1e-12) and, for
    Table 2 and S1 Table, against results/primary_b_*.csv (1e-12);
    "saved" — every other quoted mean over subjects whose per-subject values are committed, or follow from a committed
    per-subject window or bin series by the change or DiD formula of the script that produced them, each mean checked
    against its committed value (1e-12 at full precision, the printed precision otherwise): the run-level residual
    (crosslag_deviation.csv), the directed response to δ_anti (directed_crosslag.csv), the CCS decomposition
    (ccs_decomposition.csv), the cross-lag budget with its null-corrected row (crosslag_budget.csv,
    crosslag_budget_null.csv), the superseded cross-lag statistics of S9 Table (crosslag_deviation.csv), S8 Table
    (scripts/14's ratio from the atom arrays), S7 Table (scripts/09's mean r and sts DiDs from the saved per-bin
    arrays), Robustness C's two quoted contrasts (scripts/08 from the placebo-fitted atoms), and S2 Text's ΦR placebo
    window 4 − window 1 value (raw series). Quantities with no saved per-subject vector are listed, not approximated.
(b) The exact sign-flip p of the primary residual DiD (ts_gsr, W = 60) against +0.0027, +0.0049 and +0.0054.
(c) Per-subject OLS at W = 60, both variants: the sts DiD on the r₁ DiD, the residual DiD on the r₁ DiD; t intervals
    (12 df) and t-test p, subject-bootstrap percentile intervals (10,000 draws, np.random.default_rng(20261120) per
    regression; a resample with zero variance in x skipped and counted), the leave-one-out range; the corrected slope =
    slope / (2r/(1 + r)), r the r₁ DiD's split-half reliability parsed from splithalf_tables.md — model-based: it
    assumes the r₁ DiD's measurement error independent of the y's, which the shared windows do not guarantee.
(d) Fisher-z 95 % intervals, tanh(atanh r ± 1.959964/√11), for the correlations of Tables 3, 4 and 6, the full-set
    r of the sts and r₁ DiDs, the two cross-half correlations and their mean (the mean's interval an approximation), the
    split-half reliabilities; each r recomputed from the committed per-subject vectors, paired as the committed tables
    pair them, and checked at the printed precision. The per-subject half DiDs (partB19's halves: odd = pre {1, 3},
    post {7, 9, 11, 13}; even = pre {2, 4}, post {6, 8, 10, 12, 14}) of observed sts (diag_series) and of r₁
    (rev_series.autocorr_series on the .mat), written to splithalf_subjects.csv; the subject bootstrap (10,000 draws,
    np.random.default_rng(20261120)) of the disattenuated cross-half ratio mean(x1, x2)/√(max(rel_sts, 0) ×
    max(rel_r₁, 0)), all four correlations recomputed per draw; a draw with a zero ceiling or an undefined correlation
    counted and excluded; the full-sample values checked against exchange_rates_tables.md (c).
Free choices: those above; 5-decimal display; a check that fails is printed as CHECK FAILED and counted in the table
header, and the run goes on. Needs external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat (the r₁ series)
and FDlong.mat (the FD rows); stops without them unless --committed-only is given, which skips exactly the rows and
parts that need them and says so (a check mode for a clone without the data; run_all.sh does not use it).
Outputs (notes/review_results/partB/): inference_revision_tables.md, inference_revision.csv (one row per quantity),
splithalf_subjects.csv (one row per variant and subject), inference_revision_run.log via run_all.sh's nstep.
Run from the repository root: .venv/bin/python notes/partB21_inference_revision.py   (minutes)
"""
import csv
import pickle
import re
import sys
import time
import types
from pathlib import Path

import numpy as np
from scipy import stats

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_inference import Engine, window_sets, fd_windows, signflip_p as signflip_p_abs
from rev_inference_inverted import signflip_inversion
from rev_series import autocorr_series, phir_from_atoms
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
RR = REPO / "notes" / "review_results"
OUT = RR / "partB"
RES = REPO / "results"
DATA = REPO / "external" / "DMT_NCT" / "data"
MAT = DATA / "DMT_clean_mni_continuous_fullPreprocsch116.mat"
FDMAT = DATA / "FDlong.mat"
COMMITTED_ONLY = "--committed-only" in sys.argv
if not COMMITTED_ONLY and not (MAT.exists() and FDMAT.exists()):
    sys.exit("partB21: external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat and FDlong.mat are needed "
             "(the r₁ series and the FD rows); --committed-only runs the parts that need neither.")
SEED = 20261120
N_BOOT = 10000
S = 15                                                    # sts in phyid's atom order
T975_13 = stats.t.ppf(0.975, 13)
T975_12 = stats.t.ppf(0.975, 12)
Z975 = 1.959964
EXPECTATIONS = (0.0027, 0.0049, 0.0054)
HALVES = {"odd": (np.array([0, 2]), np.array([6, 8, 10, 12])), "even": (np.array([1, 3]), np.array([5, 7, 9, 11, 13]))}
t0 = time.time()
nan = float("nan")
SKIPPED = []                                              # what --committed-only left out
TS = None
if not COMMITTED_ONLY:
    import scipy.io as sio
    TS = sio.loadmat(MAT)

# ---------------------------------------------------------------- where the text quotes an interval
TEXTS = [REPO / "manuscript" / "draft_v2.md", REPO / "manuscript" / "supplementary.md"] + sorted((REPO / "manuscript" / "si").glob("S*_Text.md"))
PAT = re.compile(r"([+−-]?\d+\.\d+)\s*\[([+−-]?\d+\.\d+),\s*([+−-]?\d+\.\d+)\]")
QUOTED = {}


def _num(s):
    return float(s.replace("−", "-"))


for _f in TEXTS:
    for _i, _line in enumerate(_f.read_text().split("\n"), 1):
        for _m in PAT.finditer(_line):
            _nd = len(_m.group(1).split(".")[1])
            QUOTED.setdefault((_nd,) + tuple(round(_num(g), _nd) for g in _m.groups()), []).append(f"{_f.name}:{_i}")


def quoted_at(mean, lo, hi):
    if not np.all(np.isfinite([mean, lo, hi])):
        return ""
    locs = []
    for nd in (5, 4, 3):
        locs += QUOTED.get((nd, round(mean, nd), round(lo, nd), round(hi, nd)), [])
    return ";".join(sorted(set(locs)))


# ---------------------------------------------------------------- rows and checks
ROWS, CHECKS = [], []


def check(name, diff, tol):
    ok = bool(np.isfinite(diff) and diff <= tol)
    CHECKS.append((name, diff, tol, ok))
    if not ok:
        print(f"   CHECK FAILED: {name}: |difference| {diff:.3g} above {tol:.1g}", flush=True)
    return ok


def yn(lo, hi, v=0.0):
    return "" if not (np.isfinite(lo) and np.isfinite(hi)) else ("yes" if lo <= v <= hi else "no")


def add(group, label, set_, field, source, x, committed=(nan, nan, nan, nan), chk=None, note="", p_tol=1e-9):
    """committed = (mean, percentile lo, percentile hi, p) as committed; chk = (name, |difference|, tolerance); p_tol = the
    precision of the committed p (1e-9 where it is stored in full, 5.1e-5 where it is read from a table printed to four decimals)."""
    x = np.asarray(x, float)
    inv = signflip_inversion(x)
    m, h = inv["mean"], T975_13 * x.std(ddof=1) / np.sqrt(x.size)
    cm, clo, chi, cp = committed
    ok = check(*chk) if chk is not None else None
    wr = (inv["hi"] - inv["lo"]) / (chi - clo) if (np.isfinite(clo) and np.isfinite(chi) and chi > clo) else nan
    ROWS.append(dict(group=group, label=label, set=set_, field=field, source=source,
                     quoted_at=quoted_at(cm, clo, chi), n=x.size, mean=m, committed_mean=cm,
                     check="" if ok is None else ("ok" if ok else "CHECK FAILED"), p_exact=inv["p_zero"], committed_p=cp,
                     pct_lo=clo, pct_hi=chi, inv_lo=inv["lo"], inv_hi=inv["hi"], t_lo=m - h, t_hi=m + h, width_ratio=wr,
                     zero_in_pct=yn(clo, chi), zero_in_inv=yn(inv["lo"], inv["hi"]), zero_in_t=yn(m - h, m + h),
                     n_neg=inv["n_neg"], grid_violations=inv["grid_violations"], note=note, p_tol=p_tol))


def f5(v):
    return "—" if not np.isfinite(v) else f"{v:+.5f}"


def ci(lo, hi):
    return "—" if not (np.isfinite(lo) and np.isfinite(hi)) else f"[{lo:+.5f}, {hi:+.5f}]"


# ---------------------------------------------------------------- (a)(i) every pickle row
PKL = {}
for f in sorted(RR.glob("inference_rows_*.pkl")):
    PKL[f.name] = pickle.load(open(f, "rb"))
    for r in PKL[f.name]:
        x = np.asarray(r["did_subjects"], float)
        add("pickle", r["label"], r["set"], "did", f"notes/review_results/{f.name}", x,
            committed=(r["did"], r.get("did_lo", nan), r.get("did_hi", nan), r.get("did_p", nan)),
            chk=(f"{f.name} {r['label']} [{r['set']}] mean of did_subjects = did", abs(x.mean() - r["did"]), 1e-12))
n_pickle = sum(len(v) for v in PKL.values())
print(f"   (a)(i): {n_pickle} pickle rows ({time.time() - t0:.0f}s)", flush=True)


def prow(fname, label, set_="primary"):
    return [r for r in PKL[fname] if r["label"] == label and r["set"] == set_][0]


def pdid(fname, label, set_="primary"):
    return np.asarray(prow(fname, label, set_)["did_subjects"], float)


# ---------------------------------------------------------------- (a)(ii) Engine's per-run changes and FD rows
def primary_b(path):
    out = {}
    with open(path) as fh:
        rows = list(csv.reader(l for l in fh if not l.startswith("#")))
    for r in rows[1:]:
        out[(r[0], r[1])] = [float(v) if v != "" else nan for v in r[2:6]]            # value, ci_lo, ci_hi, p
    return out


CSV_STAT = {"dmt_change": "DMT post-pre sts", "pcb_change": "PCB post-pre sts", "fd_did": "FD DiD (same form)",
            "resid_did": "DiD FD-residualised (all windows, per subject x condition): mean"}
PFIELDS = {"dmt_change": ("dmt_lo", "dmt_hi", "dmt_p"), "pcb_change": ("pcb_lo", "pcb_hi", "pcb_p"),
           "fd_did": ("fd_lo", "fd_hi", "fd_p"), "resid_did": ("resid_lo", "resid_hi", "resid_p")}
ENGINE_ITEMS = [
    ("inference_rows_raw.pkl", "sts ts_gsr W60", 60, lambda: np.load(RES / "atoms_win60_115regions-all_ts_gsr_window.npy")[..., S],
     ("primary", "sensitivity"), RES / "primary_b_ts_gsr_win60.csv", False, "Table 2, S1 Table"),
    ("inference_rows_raw.pkl", "sts ts_demean W60", 60, lambda: np.load(RES / "atoms_win60_115regions-all_ts_demean_window.npy")[..., S],
     ("primary", "sensitivity"), RES / "primary_b_ts_demean_win60.csv", False, "Table 2, S1 Table"),
    ("inference_rows_raw.pkl", "sts ts_gsr W30", 30, lambda: np.load(RES / "atoms_win30_115regions-all_ts_gsr_window.npy")[..., S],
     ("primary", "sensitivity"), RES / "primary_b_ts_gsr_win30.csv", False, "S1 Table (W = 30)"),
    ("inference_rows_diag.pkl", "diag residual sts ts_gsr W60", 60, lambda: np.load(OUT / "diag_series_ts_gsr_W60.npz")["res"],
     ("primary",), None, False, "S3 Text"),
    ("inference_rows_ccs_pub.pkl", "CCSpub sts ts_gsr W60", 60, lambda: np.load(OUT / "ccs_pub_atoms_win60_ts_gsr.npy")[..., S],
     ("primary",), None, False, "S3 Text"),
    ("inference_rows_raw.pkl", "autocorr ts_gsr W60", 60, lambda: autocorr_series(TS["ts_gsr"], 60, "window")[0],
     ("primary",), None, True, "S3 Text"),
]
for fname, label, W, loader, sets, csv_path, needs_mat, where in ENGINE_ITEMS:
    if needs_mat and COMMITTED_ONLY:
        SKIPPED.append(f"(a)(ii) {label}: the series is recomputed from the .mat")
        continue
    x = loader()
    ws = window_sets(W)
    ns = types.SimpleNamespace(sets=ws)
    PRE = ws["PRE"]
    committed_csv = primary_b(csv_path) if csv_path is not None else None
    for set_ in sets:
        post = ws[set_]
        r = prow(fname, label, set_)
        d = Engine.did(ns, x, post)
        check(f"{label} [{set_}] recomputed per-subject DiD = pickle did_subjects", float(np.max(np.abs(d - np.asarray(r["did_subjects"], float)))), 1e-12)
        fields = {"dmt_change": x[:, 0, post].mean(1) - x[:, 0, PRE].mean(1), "pcb_change": x[:, 1, post].mean(1) - x[:, 1, PRE].mean(1)}
        if COMMITTED_ONLY:
            SKIPPED.append(f"(a)(ii) {label} [{set_}]: FD DiD and FD-residualised DiD (FDlong.mat)")
        else:
            fd = fd_windows(W)
            fields["fd_did"] = Engine.did(ns, fd, post)
            x_res = Engine.residualise(x.reshape(28, -1), fd.reshape(28, -1), np.arange(x.shape[2])).reshape(14, 2, -1)
            fields["resid_did"] = Engine.did(ns, x_res, post)
        for fld, v in fields.items():
            lo_k, hi_k, p_k = PFIELDS[fld]
            cm, clo, chi, cp = r[fld], r[lo_k], r[hi_k], r[p_k]
            if committed_csv is not None:
                sec = f"A.{set_}"
                cv, clo2, chi2, cp2 = committed_csv[(sec, CSV_STAT[fld])]
                check(f"{label} [{set_}] {fld}: pickle value = {csv_path.name}", abs(cm - cv), 1e-12)
                check(f"{label} [{set_}] {fld}: pickle interval = {csv_path.name}", max(abs(clo - clo2), abs(chi - chi2)), 1e-12)
                cm, clo, chi, cp = cv, clo2, chi2, cp2
            add("engine", label, set_, fld, f"recomputed as rev_inference.Engine ({where}); committed: " +
                (f"results/{csv_path.name}" if csv_path is not None else f"notes/review_results/{fname}"), v,
                committed=(cm, clo, chi, cp), chk=(f"{label} [{set_}] {fld} mean = committed", abs(v.mean() - cm), 1e-12))
print(f"   (a)(ii): Engine recomputations done ({time.time() - t0:.0f}s)", flush=True)

# ---------------------------------------------------------------- (a)(iii) other saved per-subject values
RX_CI = r"([+−-]?\d+\.\d+) \[([+−-]?\d+\.\d+), ([+−-]?\d+\.\d+)\]"


def rx(text, pattern, what):
    m = re.search(pattern, text, re.S)
    if m is None:
        check(f"committed value located: {what}", nan, 0)
        return None
    return m


def ci_from(m, k=1):
    return tuple(_num(m.group(k + i)) for i in range(3))


def two_run_mean(rows, var, col):
    """per-subject mean of the DMT and PCB values of column col (rows with variant, subject, condition or run)."""
    out = np.full(14, nan)
    for s in range(14):
        vals = [float(r[col]) for r in rows if r["variant"] == var and int(r["subject"]) == s + 1]
        assert len(vals) == 2, (var, col, s)
        out[s] = np.mean(vals)
    return out


def run_value(rows, var, col, run, key="condition"):
    return np.array([float([r for r in rows if r["variant"] == var and int(r["subject"]) == s + 1 and r[key] == run][0][col]) for s in range(14)])


# (1) the run-level residual (crosslag_deviation.csv; partB10) and the superseded S9 statistics
CLD = list(csv.DictReader(open(OUT / "crosslag_deviation.csv")))
C1LOG = (REPO / "notes" / "fresh_review_2026-09-17" / "checks" / "check_C1_residual_vs_null.log").read_text()
CLDT = (OUT / "crosslag_deviation_tables.md").read_text()
DCT = (OUT / "directed_crosslag_tables.md").read_text()
DCSV = list(csv.DictReader(l for l in open(OUT / "directed_crosslag.csv") if not l.startswith("#")))
for var in ("ts_gsr", "ts_demean"):
    x = two_run_mean(CLD, var, "residual")
    m = rx(C1LOG, var + r": run-level residual mean ([+−-]?\d+\.\d+)\s+95 % CI \[([+−-]?\d+\.\d+), ([+−-]?\d+\.\d+)\]", f"check C1 run-level residual {var}")
    committed = (*ci_from(m), nan) if m else (nan, nan, nan, nan)
    x_d = two_run_mean(DCSV, var, "residual_run")
    check(f"run-level residual {var}: crosslag_deviation.csv against directed_crosslag.csv (six decimals)", float(np.max(np.abs(x - x_d))), 5.1e-7)
    add("saved", f"run-level residual (observed − AR(1)-substituted sts, whole-run matrices) {var}", "run level", "mean of the two runs",
        "notes/review_results/partB/crosslag_deviation.csv; committed interval: notes/fresh_review_2026-09-17/checks/check_C1_residual_vs_null.log",
        x, committed=committed, chk=(f"run-level residual {var} mean = check C1 (5 decimals)", abs(x.mean() - committed[0]), 5.1e-6))
# the superseded cross-lag statistics (S9 Table): signed mean, run-level slope, W = 60 slope
sections = CLDT.split("## A. W = 60")
run_part = {"ts_gsr": sections[0].split("## ts_demean")[0], "ts_demean": sections[0].split("## ts_demean")[1]}
w60_part = {"ts_gsr": sections[1].split("### ts_demean")[0], "ts_demean": sections[1].split("### ts_demean")[1]}
for var in ("ts_gsr", "ts_demean"):
    for col, text, prefix, nd, lab in (
            ("mean_crosslag_deviation", run_part[var], r"\nSigned mean cross-lag deviation:", 5, "signed mean cross-lag deviation, run level (superseded; S9 Table)"),
            ("slope_deviation_on_q", run_part[var], r"\nSlope of the deviation on q across pairs \(OLS, per run\):", 4, "slope of the deviation on q, run level (superseded; S9 Table)"),
            ("w60_slope_deviation_on_q", w60_part[var], r"\nW = 60 slope of the deviation on q across pairs", 4, "slope of the deviation on q, W = 60 (superseded; S9 Table)")):
        x = two_run_mean(CLD, var, col)
        m = rx(text, prefix + r"[^\n]*?grand mean " + RX_CI + r"[^\n]*?exact sign-flip p = (\d\.\d+)", f"{lab} {var}")
        committed = (*ci_from(m), float(m.group(4))) if m else (nan, nan, nan, nan)
        add("saved", f"{lab} {var}", "run level" if "run level" in lab else "W = 60", "grand mean (mean of the two runs)",
            "notes/review_results/partB/crosslag_deviation.csv; committed: crosslag_deviation_tables.md", x, committed=committed,
            chk=(f"{lab} {var} mean = table ({nd} decimals)", abs(x.mean() - committed[0]), 0.51 * 10 ** -nd), p_tol=5.1e-5)

# (2) the directed response to δ_anti (directed_crosslag.csv, six decimals; partB15)
dct_part = {"ts_gsr": DCT.split("## ts_demean, run level")[0], "ts_demean": DCT.split("## ts_demean, run level")[1]}
for var in ("ts_gsr", "ts_demean"):
    x = two_run_mean(DCSV, var, "resp_anti_run")
    m = rx(dct_part[var], r"to δ_anti alone " + RX_CI, f"directed response {var}")
    committed = (*ci_from(m), nan) if m else (nan, nan, nan, nan)
    add("saved", f"closed-form response of sts to δ_anti alone (directed share), run level {var}", "run level", "mean of the two runs",
        "notes/review_results/partB/directed_crosslag.csv (six decimals); committed: directed_crosslag_tables.md", x, committed=committed,
        chk=(f"directed response {var} mean = table (5 decimals; CSV at six)", abs(x.mean() - committed[0]), 1.1e-5),
        note="per-subject values from a CSV written to six decimals")

# (3) the CCS decomposition (ccs_decomposition.csv, six decimals; partB18): DiD = DMT − placebo of each term
CCD = list(csv.DictReader(l for l in open(OUT / "ccs_decomposition.csv") if not l.startswith("#")))
CCDT = (OUT / "ccs_decomposition_tables.md").read_text()
CCD_Q = {"s (selected share)": ("s_post", "s_pre"), "c̄_rej (nats)": ("cbar_post", "cbar_pre"), "CCS-sts (nats)": ("change_sts", None),
         "share term c̄_pre Δs": ("term_share", None), "co-information term −(1 − s_pre) Δc̄": ("term_coinfo", None),
         "interaction Δs Δc̄": ("term_interaction", None)}
for var in ("ts_gsr", "ts_demean"):
    for est in ("W60", "global"):
        block = CCDT.split(f"## {var}, {est}\n")[1].split("\n## ")[0]
        for mask in ("code", "pub"):
            sel = [r for r in CCD if r["variant"] == var and r["estimator"] == est and r["mask"] == mask]
            for qname, (c1, c0) in CCD_Q.items():
                def per_run(run):
                    v = run_value(sel, var, c1, run, key="run")
                    return v - run_value(sel, var, c0, run, key="run") if c0 else v
                x = per_run("DMT") - per_run("PCB")
                m = rx(block, r"\| " + mask + r" \| " + re.escape(qname) + r" \|[^\n]*\| " + RX_CI + r", p = (\d\.\d+), \d+ \|", f"CCS decomposition {var} {est} {mask} {qname}")
                committed = (*ci_from(m), float(m.group(4))) if m else (nan, nan, nan, nan)
                add("saved", f"CCS-sts decomposition: {qname} ({mask} mask) {var} {est}", "primary", "DiD",
                    "notes/review_results/partB/ccs_decomposition.csv (six decimals); committed: ccs_decomposition_tables.md", x,
                    committed=committed, chk=(f"CCS decomposition {var} {est} {mask} {qname} mean = table (5 decimals; CSV at six)", abs(x.mean() - committed[0]), 1.1e-5),
                    note="per-subject values from a CSV written to six decimals: for the small terms the exact p and the interval carry that rounding", p_tol=5.1e-5)

# (4) the cross-lag budget (crosslag_budget.csv; partB12) and its null-corrected row (crosslag_budget_null.csv; partB13)
CLB = list(csv.DictReader(open(OUT / "crosslag_budget.csv")))
CLBT = (OUT / "crosslag_budget_tables.md").read_text()
CLBN = list(csv.DictReader(open(OUT / "crosslag_budget_null.csv")))
BUDGET = (("δ_run", "delta_run", "run"), ("δ_wd", "delta_wd", "wd"), ("δ_means", "delta_means", "means"), ("δ_within", "delta_within", "within"),
          ("δ_pool", "delta_pool", "pool"), ("δ_eps", "delta_eps", "eps"), ("δ_60 (run-level sign)", "delta_d60", "d60"),
          ("window-sign value (partB10)", "delta_d60_winsign", "d60_winsign"))
for var in ("ts_gsr", "ts_demean"):
    block = CLBT.split(f"## {var} (")[1].split("\n## ")[0]
    for lab, col, term in BUDGET:
        m = rx(block, "\n" + re.escape(lab) + r": DMT " + RX_CI + r", PCB " + RX_CI + r"; grand mean " + RX_CI + r"[^\n]*?exact sign-flip p = (\d\.\d+)",
               f"budget {var} {lab}")
        vals = {"grand mean (mean of the two runs)": two_run_mean(CLB, var, col), "DMT run": run_value(CLB, var, col, "DMT"), "placebo run": run_value(CLB, var, col, "PCB")}
        comm = {}
        if m:
            comm = {"DMT run": (*ci_from(m, 1), nan), "placebo run": (*ci_from(m, 4), nan), "grand mean (mean of the two runs)": (*ci_from(m, 7), float(m.group(10)))}
        for which, x in vals.items():
            c = comm.get(which, (nan, nan, nan, nan))
            add("saved", f"cross-lag budget {lab} {var}", which, "S9 Table", "notes/review_results/partB/crosslag_budget.csv; committed: crosslag_budget_tables.md",
                x, committed=c, chk=(f"budget {var} {lab} {which} mean = table (5 decimals)", abs(x.mean() - c[0]), 5.1e-6), p_tol=5.1e-5)
        if var == "ts_gsr":                                                              # the null-corrected primary row (configuration 0)
            nb = [r for r in CLBN if r["configuration"] == "0" and r["run_type"] == "both" and r["term"] == term][0]
            nc = [r for r in CLBN if r["configuration"] == "0" and r["run_type"] == "null-corrected" and r["term"] == term][0]
            x = vals["grand mean (mean of the two runs)"] - float(nb["value"])
            add("saved", f"cross-lag budget {lab} {var}, null-corrected (primary configuration)", "grand mean − null", "S9 Table",
                "crosslag_budget.csv minus the configuration-0 null of crosslag_budget_null.csv (mean over the two run types); committed: crosslag_budget_null.csv",
                x, committed=(float(nc["value"]), float(nc["ci_lo"]), float(nc["ci_hi"]), nan),
                chk=(f"budget {var} {lab} null-corrected mean = crosslag_budget_null.csv", abs(x.mean() - float(nc["value"])), 1e-12),
                note="the inverted interval of the data shifted by the null value")

# (5) S8 Table: scripts/14_proportionality.py's cells, from the atom arrays
PROP = {}
with open(RES / "proportionality.csv") as fh:
    for r in csv.DictReader(l for l in fh if not l.startswith("#")):
        PROP[(r["estimator"], r["variant"], r["statistic"])] = (float(r["value"]), float(r["ci_lo"]) if r["ci_lo"] else nan,
                                                              float(r["ci_hi"]) if r["ci_hi"] else nan, float(r["p"]) if r["p"] else nan)
CELLS14 = (("windowed_W60", "ts_gsr", "atoms_win60_115regions-all_ts_gsr_window.npy", np.arange(0, 4), np.arange(5, 14)),
           ("windowed_W60", "ts_demean", "atoms_win60_115regions-all_ts_demean_window.npy", np.arange(0, 4), np.arange(5, 14)),
           ("global_fit", "ts_gsr", "atoms_bins_115regions-all_ts_gsr_global.npy", np.arange(0, 8), np.arange(10, 28)),
           ("global_fit", "ts_demean", "atoms_bins_115regions-all_ts_demean_global.npy", np.arange(0, 8), np.arange(10, 28)))
for est, var, fname, pre, post in CELLS14:
    A = np.load(RES / fname)
    sts, tdmi = A[..., S], A.sum(axis=3)
    ratio = sts / tdmi

    def did14(x):
        ch = np.nanmean(x[:, :, post], axis=2) - np.nanmean(x[:, :, pre], axis=2)
        return ch[:, 0] - ch[:, 1]
    items = {"ratio sts/TDMI: DiD": did14(ratio),
             "ratio sts/TDMI: DMT post - pre": np.nanmean(ratio[:, 0, post], axis=1) - np.nanmean(ratio[:, 0, pre], axis=1),
             "ratio sts/TDMI: PCB post - pre": np.nanmean(ratio[:, 1, post], axis=1) - np.nanmean(ratio[:, 1, pre], axis=1),
             "(i) sts share of TDMI, pre-injection DMT (subject mean)": np.nanmean(sts[:, 0, pre], axis=1) / np.nanmean(tdmi[:, 0, pre], axis=1),
             "sts share of TDMI, pre-injection PCB (subject mean)": np.nanmean(sts[:, 1, pre], axis=1) / np.nanmean(tdmi[:, 1, pre], axis=1),
             "sts DiD (nats)": did14(sts), "TDMI DiD (nats)": did14(tdmi)}
    for stat_, x in items.items():
        c = PROP[(est, var, stat_)]
        add("saved", f"S8 Table: {stat_} {var} {est}", "primary", "scripts/14", f"results/{fname} as scripts/14_proportionality.py forms it; committed: results/proportionality.csv",
            x, committed=c, chk=(f"S8 {est} {var} {stat_} mean = proportionality.csv", abs(x.mean() - c[0]), 1e-12))

# (6) S7 Table: scripts/09_global_fc_per_bin.py's DiDs, from the saved per-bin arrays
SETS09 = {"primary_bins11-28": np.arange(10, 28), "sensitivity_bins9-28": np.arange(8, 28), "peak_bins9-14": np.arange(8, 14)}
for var in ("ts_gsr", "ts_demean"):
    G = {}
    with open(RES / f"global_fc_did_{var}.csv") as fh:
        for r in csv.DictReader(l for l in fh if not l.startswith("#")):
            if r["name"] == "DiD":
                G[(r["section"], r["quantity"])] = (float(r["value"]), float(r["ci_lo"]), float(r["ci_hi"]), float(r["p_signflip"]))
    fc = np.load(RES / f"global_fc_bins_115regions-all_{var}.npy")
    st = np.load(RES / f"atoms_bins_115regions-all_{var}_global.npy")[..., S]
    for sec, post in SETS09.items():
        for q, arr in (("mean_r", fc), ("sts_global_fit_nats", st)):
            ch = arr[:, :, post].mean(2) - arr[:, :, 0:8].mean(2)
            x = ch[:, 0] - ch[:, 1]
            c = G[(sec, q)]
            add("saved", f"S7 Table: {q} DiD {var} {sec}", sec, "scripts/09", f"results/global_fc_bins_115regions-all_{var}.npy and the global-fit atoms, as scripts/09 forms them; committed: results/global_fc_did_{var}.csv",
                x, committed=c, chk=(f"S7 {var} {sec} {q} mean = global_fc_did CSV (6 decimals)", abs(x.mean() - c[0]), 5.1e-7), p_tol=5.1e-5)

# (7) Robustness C (S1 Text): scripts/08_robustness_c_analysis.py's two quoted contrasts, placebo-fitted atoms
RC = {}
with open(RES / "robustness_c_ts_gsr.csv") as fh:
    for r in csv.DictReader(l for l in fh if not l.startswith("#")):
        RC[(r["estimator"], r["contrast"], r["atom"])] = (float(r["diff_mean"]), float(r["ci_lo"]), float(r["ci_hi"]), float(r["p_signflip"]))
plc = np.load(RES / "atoms_bins_115regions-all_ts_gsr_placebo.npy")[..., S]
for contrast, x in (("(i) within-DMT step, primary (bins 11-28)", plc[:, 0, 10:28].mean(1) - plc[:, 0, 0:8].mean(1)),
                    ("(ii) DMT minus PCB, bins 15-28", plc[:, 0, 14:28].mean(1) - plc[:, 1, 14:28].mean(1))):
    c = RC[("placebo-fitted", contrast, "sts")]
    add("saved", f"Robustness C, placebo-fitted: {contrast} (sts, ts_gsr)", "bins", "scripts/08",
        "results/atoms_bins_115regions-all_ts_gsr_placebo.npy as scripts/08 forms it; committed: results/robustness_c_ts_gsr.csv",
        x, committed=c, chk=(f"Robustness C {contrast} mean = robustness_c_ts_gsr.csv", abs(x.mean() - c[0]), 1e-12))

# (8) S2 Text: ΦR, placebo window 4 − window 1, raw series (phir_baseline_and_slope.log)
PHL = (RR / "logs" / "phir_baseline_and_slope.log").read_text()
for var in ("ts_gsr", "ts_demean"):
    ph = phir_from_atoms(np.load(RES / f"atoms_win60_115regions-all_{var}_window.npy"))
    x = ph[:, 1, 3] - ph[:, 1, 0]
    m = rx(PHL, r"raw\s+" + var + r"\s*:[^\n]*placebo window 4 − window 1 " + RX_CI + r" p = (\d\.\d+)", f"ΦR placebo w4 − w1 {var}")
    c = (*ci_from(m), float(m.group(4))) if m else (nan, nan, nan, nan)
    add("saved", f"ΦR, placebo window 4 − window 1, raw series {var}", "W = 60", "S2 Text",
        "results/atoms_win60 via rev_series.phir_from_atoms; committed: notes/review_results/logs/phir_baseline_and_slope.log", x,
        committed=c, chk=(f"ΦR placebo w4 − w1 {var} mean = log (4 decimals)", abs(x.mean() - c[0]), 5.1e-5), p_tol=5.1e-5)
print(f"   (a)(iii): saved per-subject quantities done ({time.time() - t0:.0f}s)", flush=True)

NOT_SAVED = [
    ("S2 Table and its W = 30 line: the group means of the per-subject Spearman ρ (tier 2; raw and FD-residualised; controls (a) and (b))",
     "scripts/06_primary_b_analysis.py writes the group means only; the ratings are in the data clone"),
    ("S6 Table and S1 Text: the per-subject Spearman ρ of EEG Lempel–Ziv complexity with TDMI, sts and rtr",
     "scripts/03_lz_vs_tdmi.py writes the group means only; the LZ series are in the data clone"),
    ("S4 Table and S1 Text: the per-subject workspace contrasts and set means", "scripts/11_regional_analysis.py writes the group values only"),
    ("Results 3 and S3 Text: the mean per-subject r(regional sts, regional r₁), +0.756 [+0.715, +0.790]",
     "partB11_regional_sts_r1.py writes the mean, minimum and maximum only; the per-subject regional r₁ needs the .mat"),
    ("Results 4: the W = 60 sign(q)-weighted δ_sym DiD (−0.0012 [−0.0029, +0.0006]; ts_demean −0.0039 [−0.0063, −0.0014]); S3 Text: the W = 60 RMS δ_anti DiD (+0.0063 [+0.0001, +0.0128])",
     "partB15 saves each run's mean over all 14 windows, not its pre and post means; B22 recomputes both DiDs with their inverted intervals"),
    ("S2 Text: the deconvolved ΦR values (baseline gap, placebo slope, window 4 − window 1)", "the deconvolution sandbox of notes/rev_deconv.py; not in a clone"),
]

# ---------------------------------------------------------------- (b) the residual DiD against its calibrated expectations
res_x = pdid("inference_rows_diag.pkl", "diag residual sts ts_gsr W60")
B_ROWS = []
for mu0 in EXPECTATIONS:
    inv = signflip_inversion(res_x, mu0=mu0)
    B_ROWS.append((mu0, inv["p_mu0"], signflip_p_abs(res_x - mu0), int(np.sum(res_x - mu0 < 0))))

# ---------------------------------------------------------------- (c) per-subject regressions
SPL = (OUT / "splithalf_tables.md").read_text()


def rel_r1(var):
    block = SPL.split(f"## {var}, W = 60")[1].split("\n## ")[0]
    return float(re.search(r"autocorrelation ([+−-]?\d\.\d+)", block).group(1).replace("−", "-"))


def ols(x, y):
    X = np.c_[np.ones(x.size), x]
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    e = y - X @ beta
    s2 = e @ e / (x.size - 2)
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X)))
    return beta, se


C_ROWS = []
for var in ("ts_gsr", "ts_demean"):
    x = pdid("inference_rows_raw.pkl", f"autocorr {var} W60")
    rel_half = rel_r1(var)
    rel_full = 2 * rel_half / (1 + rel_half)
    for yname, y in (("sts DiD", pdid("inference_rows_raw.pkl", f"sts {var} W60")), ("residual DiD", pdid("inference_rows_diag.pkl", f"diag residual sts {var} W60"))):
        beta, se = ols(x, y)
        tval = beta / se
        pval = 2 * stats.t.sf(np.abs(tval), 12)
        rng = np.random.default_rng(SEED)
        idx = rng.integers(0, 14, (N_BOOT, 14))
        xb, yb = x[idx], y[idx]
        xm, ym = xb.mean(1, keepdims=True), yb.mean(1, keepdims=True)
        sxx = ((xb - xm) ** 2).sum(1)
        ok = sxx > 0
        slope_b = ((xb - xm) * (yb - ym)).sum(1)[ok] / sxx[ok]
        icpt_b = ym[ok, 0] - slope_b * xm[ok, 0]
        loo = np.array([ols(np.delete(x, i), np.delete(y, i))[0] for i in range(14)])
        C_ROWS.append(dict(variant=var, y=yname, slope=beta[1], slope_t=(beta[1] - T975_12 * se[1], beta[1] + T975_12 * se[1]), slope_p=pval[1],
                           slope_boot=tuple(np.percentile(slope_b, [2.5, 97.5])), slope_loo=(loo[:, 1].min(), loo[:, 1].max()),
                           icpt=beta[0], icpt_t=(beta[0] - T975_12 * se[0], beta[0] + T975_12 * se[0]), icpt_p=pval[0],
                           icpt_boot=tuple(np.percentile(icpt_b, [2.5, 97.5])), icpt_loo=(loo[:, 0].min(), loo[:, 0].max()),
                           n_skipped=int((~ok).sum()), rel_half=rel_half, rel_full=rel_full, corrected=beta[1] / rel_full))

# ---------------------------------------------------------------- (d) Fisher-z intervals and the cross-half bootstrap
def fisher(r, n=14):
    z, h = np.arctanh(r), Z975 / np.sqrt(n - 3)
    return float(np.tanh(z - h)), float(np.tanh(z + h))


D_ROWS = []


def dcorr(name, a, b, committed, source):
    r = float(np.corrcoef(a, b)[0, 1])
    lo, hi = fisher(r)
    ok = check(f"(d) {name}: r = committed (3 decimals)", abs(r - committed), 5.1e-4) if np.isfinite(committed) else None
    D_ROWS.append((name, r, committed, lo, hi, source, "" if ok is None else ("ok" if ok else "CHECK FAILED")))


EXR = (OUT / "exchange_rates_tables.md").read_text()
EXC = {}
for var in ("ts_gsr", "ts_demean"):
    cells = [c.strip() for c in re.search(r"\n\| " + var + r" \| ([^\n]*)\|\n", EXR.split("## (c)")[1]).group(1).split("|")]
    EXC[var] = [float(c.replace("−", "-")) for c in cells]            # x1, x2, mean, rel_sts, rel_r1, ceiling, disattenuated, full-set r
DIAGT = (OUT / "diag_tables.md").read_text()
LAGT = (OUT / "lag_tables.md").read_text()
CCSPT = (OUT / "ccs_pub_tables.md").read_text()
for var in ("ts_gsr", "ts_demean"):
    dcorr(f"full-set r(sts DiD, r₁ DiD), {var}, W = 60", pdid("inference_rows_raw.pkl", f"sts {var} W60"), pdid("inference_rows_raw.pkl", f"autocorr {var} W60"),
          EXC[var][7], "exchange_rates_tables.md (c)")
for var in ("ts_gsr", "ts_demean"):
    for W in (60, 30):
        block = DIAGT.split(f"## {var}, W = {W}\n")[1].split("\n## ")[0]
        r_po = float(re.search(r"r\(predicted DiD, observed DiD\) = ([+−-]?\d\.\d+)", block).group(1).replace("−", "-"))
        r_ra = float(re.search(r"r\(residual DiD, autocorrelation contrast\) = ([+−-]?\d\.\d+)", block).group(1).replace("−", "-"))
        ac = pdid("inference_rows_raw.pkl", f"autocorr {var} W60")
        dcorr(f"Table 4: r(AR(1)-substituted DiD, observed DiD), {var}, W = {W}", pdid("inference_rows_diag.pkl", f"diag predicted sts {var} W{W}"),
              pdid("inference_rows_diag.pkl", f"diag observed sts {var} W{W}"), r_po, "diag_tables.md")
        dcorr(f"Table 4: r(residual DiD, r₁ DiD at W = 60), {var}, W = {W}", pdid("inference_rows_diag.pkl", f"diag residual sts {var} W{W}"), ac, r_ra, "diag_tables.md")
for tau in (1, 2, 3, 5):
    cells = [c.strip() for c in re.search(r"\n\| " + str(tau) + r" \| W60 \| ([^\n]*)\|\n", LAGT).group(1).split("|")]
    dcorr(f"Table 6: r(sts DiD, r_τ DiD), τ = {tau}, ts_gsr, W = 60", pdid("inference_rows_lag.pkl", f"sts tau{tau} ts_gsr W60"),
          pdid("inference_rows_lag.pkl", f"autocorr lag{tau} ts_gsr W60"), float(cells[6].replace("−", "-")), "lag_tables.md")
for var in ("ts_gsr", "ts_demean"):
    for est in ("W60", "global-bins"):
        block = CCSPT.split(f"## {var} {est}: ")[1].split("\n## ")[0]
        rc = float(re.search(r"Pearson r = ([+−-]?\d\.\d+)", block).group(1).replace("−", "-"))
        dcorr(f"Table 3: r(CCS-sts DiD, r₁ DiD), {var}, {est}", pdid("inference_rows_ccs_pub.pkl", f"CCSpub sts {var} {est}"),
              pdid("inference_rows_raw.pkl", f"autocorr {var} W60"), rc, "ccs_pub_tables.md")

HALF_ROWS, BOOT_ROWS, SPLIT_CSV = [], [], ["variant,subject,sts_odd,sts_even,r1_odd,r1_even"]
if COMMITTED_ONLY:
    SKIPPED.append("(d) the cross-half and split-half correlations, their bootstrap and splithalf_subjects.csv (the r₁ window series need the .mat)")
else:
    def hd(x, pre, post):
        ch = x[:, :, post].mean(2) - x[:, :, pre].mean(2)
        return ch[:, 0] - ch[:, 1]

    def four(so, se_, ro, re_):
        x1 = np.corrcoef(so, re_)[0, 1]; x2 = np.corrcoef(se_, ro)[0, 1]
        rel_s = np.corrcoef(so, se_)[0, 1]; rel_a = np.corrcoef(ro, re_)[0, 1]
        ceil = np.sqrt(max(rel_s, 0) * max(rel_a, 0))
        return x1, x2, 0.5 * (x1 + x2), rel_s, rel_a, ceil, (0.5 * (x1 + x2) / ceil if ceil > 0 else nan)

    for var in ("ts_gsr", "ts_demean"):
        obs = np.load(OUT / f"diag_series_{var}_W60.npz")["obs"]
        ac = autocorr_series(TS[var], 60, "window")[0]
        so, se_ = hd(obs, *HALVES["odd"]), hd(obs, *HALVES["even"])
        ro, re_ = hd(ac, *HALVES["odd"]), hd(ac, *HALVES["even"])
        for s in range(14):
            SPLIT_CSV.append(f"{var},{s + 1},{so[s]:.10g},{se_[s]:.10g},{ro[s]:.10g},{re_[s]:.10g}")
        x1, x2, mean_x, rel_s, rel_a, ceil, dis = four(so, se_, ro, re_)
        full = float(np.corrcoef(hd(obs, np.arange(0, 4), np.arange(5, 14)), hd(ac, np.arange(0, 4), np.arange(5, 14)))[0, 1])
        for name, v, k, tol in (("x1", x1, 0, 5.1e-4), ("x2", x2, 1, 5.1e-4), ("mean", mean_x, 2, 5.1e-4), ("rel(sts)", rel_s, 3, 5.1e-4),
                                ("rel(r₁)", rel_a, 4, 5.1e-4), ("ceiling", ceil, 5, 5.1e-4), ("disattenuated", dis, 6, 5.1e-3), ("full-set r", full, 7, 5.1e-4)):
            check(f"(d) {var} cross-half {name} = exchange_rates_tables.md (c)", abs(v - EXC[var][k]), tol)
        HALF_ROWS.append((var, x1, x2, mean_x, rel_s, rel_a, ceil, dis))
        for name, r in ((f"cross-half r(sts_odd, r₁_even), {var}", x1), (f"cross-half r(sts_even, r₁_odd), {var}", x2),
                        (f"mean cross-half r, {var} (Fisher-z of the mean: an approximation)", mean_x),
                        (f"split-half reliability of the sts DiD, {var}", rel_s), (f"split-half reliability of the r₁ DiD, {var}", rel_a)):
            lo, hi = fisher(r)
            D_ROWS.append((name, r, nan, lo, hi, "recomputed halves (exchange_rates_tables.md (c) checked above)", ""))
        rng = np.random.default_rng(SEED)
        draws, bad = [], 0
        for _ in range(N_BOOT):
            i = rng.integers(0, 14, 14)
            with np.errstate(invalid="ignore", divide="ignore"):
                v = four(so[i], se_[i], ro[i], re_[i])[6]
            if np.isfinite(v):
                draws.append(v)
            else:
                bad += 1
        BOOT_ROWS.append((var, dis, *np.percentile(draws, [2.5, 97.5]), bad))
    (OUT / "splithalf_subjects.csv").write_text(f"# partB21_inference_revision.py; per-subject half DiDs (partB19's halves), W = 60; git={SHA}\n" + "\n".join(SPLIT_CSV) + "\n")
print(f"   (b)–(d) done ({time.time() - t0:.0f}s)", flush=True)

# ---------------------------------------------------------------- outputs
cols = ["group", "label", "set", "field", "source", "quoted_at", "n", "mean", "committed_mean", "check", "p_exact", "committed_p", "p_tol", "pct_lo", "pct_hi",
        "inv_lo", "inv_hi", "t_lo", "t_hi", "width_ratio", "zero_in_pct", "zero_in_inv", "zero_in_t", "n_neg", "grid_violations", "note"]


def cell(v):
    if isinstance(v, float):
        return "" if not np.isfinite(v) else repr(v)
    return '"' + str(v).replace('"', "'") + '"' if ("," in str(v) or '"' in str(v)) else str(v)


(OUT / "inference_revision.csv").write_text(f"# partB21_inference_revision.py; one row per quantity; git={SHA}\n" + ",".join(cols) + "\n" +
                                            "\n".join(",".join(cell(r[c]) for c in cols) for r in ROWS) + "\n")
n_fail = sum(1 for c in CHECKS if not c[3])
wr = np.array([r["width_ratio"] for r in ROWS if np.isfinite(r["width_ratio"])])
iff_bad = [r for r in ROWS if (r["zero_in_inv"] == "no") != (r["p_exact"] <= 0.05)]
pdiff = [r for r in ROWS if np.isfinite(r["committed_p"]) and abs(r["p_exact"] - r["committed_p"]) > r["p_tol"]]
viol = sum(r["grid_violations"] for r in ROWS)
flips = [r for r in ROWS if r["zero_in_pct"] and r["zero_in_pct"] != r["zero_in_inv"]]
lines = ["# Inverted sign-flip intervals, the residual against its calibrated expectations, the per-subject regressions and the correlation intervals (partB21_inference_revision.py)",
         f"git={SHA}", "",
         "Exploratory (decision D1): effect sizes and intervals; no threshold language. N = 14 subjects; the exact sign-flip test over 2^14 assignments, two-sided; the inverted interval {μ : p(μ) > 0.05} of notes/rev_inference_inverted.py "
         "(relative tolerance 1e-12; bounds bisected to 1e-7 after a 2,001-point monotonicity grid); the t interval mean ± t(0.975, 13)·SD/√14; the percentile interval as committed. Seed 20261120.", "",
         f"Checks: {len(CHECKS)} run, {n_fail} failed" + ("" if n_fail == 0 else " — listed at the foot as CHECK FAILED") + ".",
         ("Mode: --committed-only (a check without the data clone); skipped: " + "; ".join(SKIPPED) + "." if COMMITTED_ONLY else "Mode: full (the .mat and FDlong.mat present)."), ""]
lines += ["## (a) Summary", "",
          f"Quantities: {len(ROWS)} ({sum(r['group'] == 'pickle' for r in ROWS)} pickle rows, {sum(r['group'] == 'engine' for r in ROWS)} Engine recomputations, {sum(r['group'] == 'saved' for r in ROWS)} other saved per-subject quantities); "
          f"{sum(1 for r in ROWS if r['quoted_at'])} of them matched to an interval quoted in draft_v2.md, S1–S5 Text or supplementary.md.",
          f"Width of the inverted interval over the committed percentile interval ({wr.size} quantities with a committed interval): median {np.median(wr):.3f}, "
          f"quartiles {np.percentile(wr, 25):.3f}–{np.percentile(wr, 75):.3f}, range {wr.min():.3f}–{wr.max():.3f}; share with a ratio in 1.05–1.20: {np.mean((wr >= 1.05) & (wr <= 1.20)):.3f}, below 1.05: {np.mean(wr < 1.05):.3f}, above 1.20: {np.mean(wr > 1.20):.3f}." if wr.size else "No committed intervals.",
          f"Zero outside the inverted interval exactly when the exact p ≤ 0.05: {len(ROWS) - len(iff_bad)} of {len(ROWS)} (exceptions: {len(iff_bad)}). Grid points where p rose away from the mean: {viol}.",
          f"Quantities whose zero-inclusion differs between the committed percentile and the inverted interval: {len(flips)}" + (": " + "; ".join(f"{r['label']} [{r['set']}] {r['field']}" for r in flips) if flips else "") + ".",
          f"Exact p against 0 (relative tolerance) differing from the committed p by more than the committed p's precision (1e-9 stored in full; 5.1e-5 read from a four-decimal table): {len(pdiff)}" + (": " + "; ".join(f"{r['label']} [{r['set']}] {r['field']} {r['p_exact']:.6f} vs {r['committed_p']:.6f}" for r in pdiff[:20]) if pdiff else "") + ".", ""]
lines += ["## (a) Quantities quoted in the text, the Engine recomputations and the other saved quantities (every pickle row is in inference_revision.csv)", "",
          "| group | quantity | set / field | mean | exact p | percentile CI (committed) | inverted CI | t CI | width ratio | 0 in pct / inv / t | neg/14 | quoted at | check |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in ROWS:
    if r["group"] == "pickle" and not r["quoted_at"]:
        continue
    wtxt = "—" if not np.isfinite(r["width_ratio"]) else f"{r['width_ratio']:.3f}"
    lines.append(f"| {r['group']} | {r['label']} | {r['set']} / {r['field']} | {f5(r['mean'])} | {r['p_exact']:.4f} | {ci(r['pct_lo'], r['pct_hi'])} | {ci(r['inv_lo'], r['inv_hi'])} | "
                 f"{ci(r['t_lo'], r['t_hi'])} | {wtxt} | {r['zero_in_pct'] or '—'} / {r['zero_in_inv']} / {r['zero_in_t']} | {r['n_neg']} | {r['quoted_at'] or '—'} | {r['check'] or '—'} |")
lines += ["", "## (a) Quantities with no saved per-subject vector (not approximated)", ""]
lines += [f"- {q} — {why}." for q, why in NOT_SAVED]
lines += ["", "Not a mean over subjects, and so outside (a): S8 Table's (ii) ratio of group means (sts share of the TDMI DiD) and every correlation (part (d)).", ""]
lines += ["## (b) The primary residual DiD against its calibrated expectations (ts_gsr, W = 60; per-subject DiD minus the expectation)", "",
          f"Residual DiD {res_x.mean():+.5f}; inverted interval {ci(*[signflip_inversion(res_x)[k] for k in ('lo', 'hi')])}.", "",
          "| expectation | exact p (relative tolerance) | exact p (rev_inference.signflip_p, absolute tolerance) | subjects below the expectation |", "|---|---|---|---|"]
lines += [f"| {mu:+.4f} | {p1:.4f} | {p2:.4f} | {nb}/14 |" for mu, p1, p2, nb in B_ROWS]
lines += ["", "## (c) Per-subject regressions on the r₁ DiD (W = 60, primary windows)", "",
          "| variant | y | slope | t CI (12 df), p | bootstrap CI | leave-one-out range | intercept | t CI, p | bootstrap CI | leave-one-out range | skipped resamples | split-half rel(r₁) → full-set | corrected slope (model-based) |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for c in C_ROWS:
    lines.append(f"| {c['variant']} | {c['y']} | {c['slope']:+.4f} | [{c['slope_t'][0]:+.4f}, {c['slope_t'][1]:+.4f}], {c['slope_p']:.4f} | [{c['slope_boot'][0]:+.4f}, {c['slope_boot'][1]:+.4f}] | "
                 f"{c['slope_loo'][0]:+.4f} to {c['slope_loo'][1]:+.4f} | {c['icpt']:+.5f} | [{c['icpt_t'][0]:+.5f}, {c['icpt_t'][1]:+.5f}], {c['icpt_p']:.4f} | "
                 f"[{c['icpt_boot'][0]:+.5f}, {c['icpt_boot'][1]:+.5f}] | {c['icpt_loo'][0]:+.5f} to {c['icpt_loo'][1]:+.5f} | {c['n_skipped']} | {c['rel_half']:.3f} → {c['rel_full']:.3f} | {c['corrected']:+.3f} |")
lines += ["", "The corrected slope divides by the Spearman–Brown full-set reliability of the r₁ DiD; it assumes that the r₁ DiD's measurement error is independent of the y's, which the shared windows do not guarantee (model-based).", ""]
lines += ["## (d) Fisher-z 95 % intervals (n = 14) and the disattenuated cross-half ratio", "",
          "| correlation | r (recomputed) | committed | Fisher-z 95 % CI | source | check |", "|---|---|---|---|---|---|"]
lines += [f"| {n} | {r:+.3f} | {'—' if not np.isfinite(c) else f'{c:+.3f}'} | [{lo:+.3f}, {hi:+.3f}] | {src} | {chk or '—'} |" for n, r, c, lo, hi, src, chk in D_ROWS]
if HALF_ROWS:
    lines += ["", "| variant | r(sts_odd, r₁_even) | r(sts_even, r₁_odd) | mean | rel(sts) | rel(r₁) | ceiling | disattenuated | bootstrap 95 % CI of the disattenuated ratio | draws excluded |", "|---|---|---|---|---|---|---|---|---|---|"]
    for (var, x1, x2, mx, rs, ra, ce, di), (_, _, blo, bhi, bad) in zip(HALF_ROWS, BOOT_ROWS):
        lines.append(f"| {var} | {x1:+.3f} | {x2:+.3f} | {mx:+.3f} | {rs:+.3f} | {ra:+.3f} | {ce:.3f} | {di:+.3f} | [{blo:+.3f}, {bhi:+.3f}] | {bad} |")
else:
    lines += ["", "The cross-half and split-half correlations and the bootstrap of the disattenuated ratio were not computed (--committed-only)."]
lines += ["", "## Predictions and rule (pre-run entry, B21)", "",
          "Predictions: (a) the inverted intervals wider than the percentile intervals by 5–20 %, and excluding zero exactly when the exact p is below 0.05 (by construction); known values (verification of 22 Sep, Finding 13): the primary sts DiD [−0.1317, −0.0310], "
          "the residual DiD [+0.0005, +0.0226], the r₁ DiD [−0.0261, −0.0037], the CCS-sts DiD at W = 60 on ts_gsr [−0.0001, +0.0088]. (b) Known (Finding 3): 0.108, 0.219, 0.251. (c) Known (Findings 3 and 5): sts on r₁ +4.263 [+3.408, +5.117], intercept −0.0184 [−0.0390, +0.0021] on ts_gsr; "
          "+4.922 and +0.0031 on ts_demean; residual on r₁ −0.753 [−1.133, −0.374], intercept +0.0005 on ts_gsr; −0.568 [−1.048, −0.088] on ts_demean; corrected about 5.0 (0.851) and 5.9 (0.832). "
          "(d) 0.694 → [0.26, 0.90]; 0.953 → [0.85, 0.99]; −0.780 → [−0.93, −0.43]; 0.989 → [0.96, 1.00]; the disattenuated ratio's interval wide, its lower limit below 0.7.",
          "Rule: Stage B reports the inverted interval wherever the text reports a percentile interval of a mean over subjects, and states the method once, in Methods; Fisher-z intervals beside the correlations; "
          "the calibration's replicate SDs keep their form; the p values against the calibrated expectations replace \"inside its interval\"."]
if n_fail:
    lines += ["", "## Failed checks", ""] + [f"- CHECK FAILED: {n}: |difference| {d:.3g} above {t:.1g}" for n, d, t, ok in CHECKS if not ok]
(OUT / "inference_revision_tables.md").write_text("\n".join(lines) + "\n")
print("\n".join(lines[:12]))
print(f"   checks: {len(CHECKS)} run, {n_fail} failed")
print(f"done ({time.time() - t0:.0f}s)")
