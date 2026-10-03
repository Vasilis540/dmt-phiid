"""Derived numbers for the revision that answers the cold reads of 1 October 2026, computed from committed result files
only (no subject data): the inverted sign-flip intervals of B16c's contrasts from its committed per-subject vectors,
the between-subject SDs of the pre-injection gap, the post-injection gap and the DiD from B27's per-subject table, the
regional slope of rtr on r₁ from B20's table, the squares and shares the text quotes, and, added after the audits of
the prepared revision (2 October 2026), the generators' mean residual DiDs from B28's replicates, the Fisher-z
intervals the text reads to two decimals or by whether they hold zero, the regional relation with the windowed
estimator's own regional atoms, the leave-one-out of the sts DiD's slope on the r₁ DiD, and, added after the checks of
the corrected revision, the parts of the sts DiD's between-subject variance, the residual's cross-half correlations
with r₁ from the committed per-subject series, with their intervals, means and ceilings, the recomputation of every
cell of B27's table (a) from its six-decimal per-subject file, and values that B27's pre-run entry lists as known,
compared with the entry's, and, added after a third check, the inverted intervals of three quantities that the text
gave without one or without a committed source (what the AR(1)-substituted estimate carries of the whitened contrasts;
the difference between the runs in B15's directed response; the DiD of B29's count of replaced volumes) and the
Fisher-z intervals of all eight whitened correlations at p = 10 and 20.

Planning-session computation on committed outputs: those of B27, B28, B29 and B16c as the run wrote them and, for some
items, earlier ones (of B4, B7, B11, B15, B16, B20 and B21, the inference rows of the raw series and the regional
atoms of the windowed estimator). Run from the repository root:
    python notes/review_2026-10-01_cold_reads/checks/derived_r24.py
The text and the record quote the numbers printed here as derived from the named files, and the output's header names
the commit whose files were read; no random draw is made.
"""
import csv
import pickle
import re
import subprocess
import sys
from itertools import product
from pathlib import Path

import numpy as np
from scipy import stats

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
sys.path.insert(0, str(R / "notes"))
from rev_inference_inverted import signflip_inversion  # noqa: E402

RR = R / "notes/review_results"
try:
    sha = subprocess.run(["git", "-C", str(R), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "nogit"
    dirty = subprocess.run(["git", "-C", str(R), "status", "--porcelain", "--untracked-files=no"], capture_output=True, text=True).stdout.strip()
    sha += "-dirty" if dirty else ""
except Exception:
    sha = "nogit"
print(f"# derived_r24.py; git={sha}")

# 1. B16c: the inverted sign-flip interval of each primary-set contrast (the text's interval for a mean over subjects;
#    the CSV's did_lo/did_hi are the subject-bootstrap percentile interval of rev_inference.Engine)
rows = pickle.load(open(RR / "inference_rows_prewhiten_fixed.pkl", "rb"))
print("1. B16c, inverted sign-flip 95 % intervals (notes/review_results/inference_rows_prewhiten_fixed.pkl, field "
      "did_subjects, primary set); mean [lo, hi], exact p, negative/14")
for tag in ("ar10", "ar20"):
    for var in ("ts_gsr", "ts_demean"):
        for est in ("W60", "global-bins"):
            for q in ("MMI sts", "CCS sts", "MMI xtx+yty", "autocorr"):
                label = f"prewhiten_fixed {tag} {q} {var} {est}"
                d = [r for r in rows if r["label"] == label and r["set"] == "primary"]
                assert len(d) == 1, label
                x = np.asarray(d[0]["did_subjects"], float)
                inv = signflip_inversion(x)
                assert inv["grid_violations"] == 0, label
                assert abs(inv["mean"] - float(d[0]["did"])) < 1e-9, label
                print(f"   {label}: {inv['mean']:+.4f} [{inv['lo']:+.4f}, {inv['hi']:+.4f}], p = {inv['p_zero']:.4f}, "
                      f"{inv['n_neg']}/14 (CSV did_p {float(d[0]['did_p']):.4f}, n_neg {int(d[0]['n_neg'])})")
#    and the AR(1)-substituted estimate on the whitened series at W = 60 (the diagnostic's substituted sts; the label
#    calls it "predicted"), whose contrast at p = 20 the main text gives as a point value
print("   the AR(1)-substituted estimate on the whitened series, W = 60 (label 'diag predicted sts'): mean [lo, hi], "
      "exact p, negative/14")
for tag in ("ar10", "ar20"):
    for var in ("ts_gsr", "ts_demean"):
        label = f"prewhiten_fixed {tag} diag predicted sts {var} W60"
        d = [r for r in rows if r["label"] == label and r["set"] == "primary"]
        assert len(d) == 1, label
        x = np.asarray(d[0]["did_subjects"], float)
        inv = signflip_inversion(x)
        assert inv["grid_violations"] == 0, label
        assert abs(inv["mean"] - float(d[0]["did"])) < 1e-9 and abs(inv["p_zero"] - float(d[0]["did_p"])) < 5e-5, label
        print(f"   {label}: {inv['mean']:+.4f} [{inv['lo']:+.4f}, {inv['hi']:+.4f}], p = {inv['p_zero']:.4f}, "
              f"{inv['n_neg']}/14 (CSV did_p {float(d[0]['did_p']):.4f}, n_neg {int(d[0]['n_neg'])})")

# 2. B27: between-subject SDs of the pre gap, the post gap and the DiD, and the square of r(DiD, pre gap)
print("2. B27, between-subject SDs (ddof 1) from notes/review_results/partB/baseline_gap.csv, and r(DiD, pre gap)²")
with open(RR / "partB" / "baseline_gap.csv", encoding="utf-8") as fh:
    bg = list(csv.DictReader([l for l in fh if not l.startswith("#")]))
for q, var, W in (("sts", "ts_gsr", "60"), ("sts", "ts_demean", "60"), ("sts", "ts_gsr", "30"), ("r1", "ts_gsr", "60"), ("residual", "ts_gsr", "60")):
    sel = [r for r in bg if r["quantity"] == q and r["variant"] == var and r["W"] == W]
    assert len(sel) == 14, (q, var, W, len(sel))
    pre = np.array([float(r["pre_gap"]) for r in sel]); post = np.array([float(r["post_gap"]) for r in sel]); did = np.array([float(r["did"]) for r in sel])
    assert np.allclose(did, post - pre, atol=1e-6)
    r_dp = np.corrcoef(did, pre)[0, 1]
    print(f"   {q} {var} W{W}: SD pre gap {pre.std(ddof=1):.4f}, SD post gap {post.std(ddof=1):.4f}, SD DiD {did.std(ddof=1):.4f}; "
          f"r(DiD, pre gap) {r_dp:+.3f}, r² {r_dp ** 2:.2f}; subject with the largest DiD {int(np.argmax(did)) + 1} ({did.max():+.4f}), "
          f"its pre gap {pre[np.argmax(did)]:+.4f}, its post gap {post[np.argmax(did)]:+.4f}; positive DiDs {int((did > 0).sum())}; "
          f"most negative pre gap subject {int(np.argmin(pre)) + 1} ({pre.min():+.4f})")

# 3. B20: the regional slope of rtr on windowed regional r₁, beside sts's (115 regions)
print("3. B20, OLS slopes across the 115 regions on r1_windowed (notes/review_results/partB/regional_partial.csv)")
with open(RR / "partB" / "regional_partial.csv", encoding="utf-8") as fh:
    rp = list(csv.DictReader([l for l in fh if not l.startswith("#")]))
assert len(rp) == 115, len(rp)
r1 = np.array([float(r["r1_windowed"]) for r in rp]); sts = np.array([float(r["sts"]) for r in rp]); rtr = np.array([float(r["rtr"]) for r in rp])
assert np.allclose(sts - rtr, [float(r["sts_minus_rtr"]) for r in rp], atol=1e-6)
for name, y in (("sts", sts), ("rtr", rtr)):
    b = np.polyfit(r1, y, 1)[0]
    print(f"   {name} on r₁: slope {b:+.4f} nats per unit r₁ (r = {np.corrcoef(r1, y)[0, 1]:+.3f}, SD of the map {y.std(ddof=1):.4f})")
b_sts, b_rtr = np.polyfit(r1, sts, 1)[0], np.polyfit(r1, rtr, 1)[0]
print(f"   ratio rtr slope / sts slope: {b_rtr / b_sts:.3f} (sts slope / rtr slope {b_sts / b_rtr:.1f})")

# 4. Squares and shares the text quotes
print("4. Squares and shares quoted in the text")
# the lower limit of the disattenuated ratio's interval (partB/inference_revision_tables.md, (d), ts_gsr)
dis = None
for l in (RR / "partB" / "inference_revision_tables.md").read_text(encoding="utf-8").split("\n"):
    if l.startswith("| ts_gsr | +"):
        dis = [c.strip() for c in l.split("|")]
assert dis is not None
lo = float(dis[9].strip("[]").split(",")[0])
print(f"   disattenuated ratio's interval, lower limit {lo:+.3f} (inference_revision_tables.md (d)); its square {lo ** 2:.2f} = the share of "
      f"reliable variance at the limit, {100 * lo ** 2:.0f} %")
# FD residualisation: the share of each contrast it removes (inference_rows_raw.csv, primary set)
with open(RR / "inference_rows_raw.csv", encoding="utf-8") as fh:
    ir = {(r["label"], r["set"]): r for r in csv.DictReader([l for l in fh if not l.startswith("#")])}
for lab in ("sts ts_gsr W60", "autocorr ts_gsr W60"):
    r = ir[(lab, "primary")]
    d, rd = float(r["did"]), float(r["resid_did"])
    print(f"   {lab}: DiD {d:+.4f}, FD-residualised {rd:+.4f}; removed {(d - rd) / d:.3f} of the DiD")
print("   (the data's residual DiD, +0.0115, against the expectations +0.0027, +0.0049 and +0.0054: excesses "
      f"{0.0115 - 0.0027:+.4f}, {0.0115 - 0.0049:+.4f}, {0.0115 - 0.0054:+.4f}; B27's table (c) prints them from the unrounded values)")

# 5. B28: the mean residual DiD of each condition from the replicates (the tables file prints it at four decimals), and
#    the step-minus-ramp differences. The CSV's condition label holds a comma and is not quoted, so each data row has
#    eleven fields under ten column names: the first two fields are the label.
print("5. B28, mean residual DiD per condition over the replicates (notes/review_results/partB/matched_slope.csv, column "
      "res_did; the label is the row's first two fields) and the step-minus-ramp differences")
with open(RR / "partB" / "matched_slope.csv", encoding="utf-8") as fh:
    ms = [l.rstrip("\n") for l in fh if not l.startswith("#")]
mh = ms[0].split(",")
assert mh[0] == "condition" and len(mh) == 10, mh
acc = {}
for l in ms[1:]:
    f = l.split(",")
    assert len(f) == 11, l
    acc.setdefault(f[0] + "," + f[1], []).append(float(f[1 + mh.index("res_did")]))
CONDS = ("(i) band-passed, step", "(ii) band-passed, ramp", "(iii) AR(1), step", "(iv) AR(1), ramp")
assert tuple(acc) == CONDS and all(len(v) == len(acc[CONDS[0]]) for v in acc.values()), {k: len(v) for k, v in acc.items()}
mres = {k: float(np.mean(v)) for k, v in acc.items()}
for k in CONDS:
    print(f"   {k}: mean residual DiD {mres[k]:+.6f} over {len(acc[k])} replicates")
for name, a, b in (("band-passed", CONDS[0], CONDS[1]), ("AR(1)", CONDS[2], CONDS[3])):
    d = mres[a] - mres[b]
    print(f"   {name}, step minus ramp: {d:+.6f} ({abs(d):.4f} at four decimals)")

# 6. Fisher-z 95 % intervals, tanh(atanh r ± 1.959964/√11), as B21 (d) computes them
def fisher(r, n=14):
    h = 1.959964 / np.sqrt(n - 3)
    return float(np.tanh(np.arctanh(r) - h)), float(np.tanh(np.arctanh(r) + h))

print("6. Fisher-z 95 % intervals at N = 14 (B21 (d)'s formula)")
with open(RR / "partB" / "splithalf_subjects.csv", encoding="utf-8") as fh:
    sh = [r for r in csv.DictReader([l for l in fh if not l.startswith("#")]) if r["variant"] == "ts_gsr"]
assert len(sh) == 14
so, se_, ro, re_ = (np.array([float(r[k]) for r in sh]) for k in ("sts_odd", "sts_even", "r1_odd", "r1_even"))
x1, x2 = np.corrcoef(so, re_)[0, 1], np.corrcoef(se_, ro)[0, 1]
mx = 0.5 * (x1 + x2)
lo_, hi_ = fisher(mx)
print(f"   mean cross-half correlation of the sts and r₁ DiDs, ts_gsr (splithalf_subjects.csv): r {mx:+.6f} "
      f"({x1:+.6f} and {x2:+.6f}), interval [{lo_:+.6f}, {hi_:+.6f}]")
rows16 = pickle.load(open(RR / "inference_rows_prewhiten.pkl", "rb"))

def vec(rr, label):
    d = [r for r in rr if r["label"] == label and r["set"] == "primary"]
    assert len(d) == 1, label
    return np.asarray(d[0]["did_subjects"], float)

for name, rr, pre, tag in (("p = 1", rows16, "prewhiten", "ar1"), ("p ≤ 5 (BIC)", rows16, "prewhiten", "arp"),
                           ("p = 10", rows, "prewhiten_fixed", "ar10"), ("p = 20", rows, "prewhiten_fixed", "ar20")):
    r = float(np.corrcoef(vec(rr, f"{pre} {tag} MMI sts ts_gsr W60"), vec(rr, f"{pre} {tag} autocorr ts_gsr W60"))[0, 1])
    lo_, hi_ = fisher(r)
    print(f"   r(MMI-sts DiD, whitened r₁ DiD), ts_gsr W60, {name}: r {r:+.6f}, interval [{lo_:+.6f}, {hi_:+.6f}]; "
          f"{'includes' if lo_ <= 0 <= hi_ else 'excludes'} zero")
#    the eight cells at p = 10 and 20 (2 orders × 2 variants × 2 estimators), each r compared at three decimals with
#    the value that B16c's tables file prints under the cell's heading ("## ar10 ts_gsr W60: ...")
ft = (RR / "partB" / "prewhiten_fixed_tables.md").read_text(encoding="utf-8")
printed = {m.group(1, 2, 3): m.group(4) for m in re.finditer(
    r"^## (ar10|ar20) (ts_gsr|ts_demean) (W60|global-bins):.*?per subject r\(MMI sts DiD, whitened autocorrelation "
    r"DiD\) = ([+-]\d\.\d{3})", ft, flags=re.M | re.S)}
assert len(printed) == 8, printed
print("   the eight cells at p = 10 and 20, r(MMI-sts DiD, whitened r₁ DiD) from the per-subject vectors, each equal at "
      "three decimals to the r that notes/review_results/partB/prewhiten_fixed_tables.md prints under the cell's "
      "heading:")
mine8, n_incl = [], 0
for tag, pn in (("ar10", "p = 10"), ("ar20", "p = 20")):
    for var in ("ts_gsr", "ts_demean"):
        for est, en in (("W60", "W60"), ("global-bins", "global fit")):
            r = float(np.corrcoef(vec(rows, f"prewhiten_fixed {tag} MMI sts {var} {est}"),
                                  vec(rows, f"prewhiten_fixed {tag} autocorr {var} {est}"))[0, 1])
            lo_, hi_ = fisher(r)
            incl = lo_ <= 0 <= hi_
            n_incl += incl
            mine8.append(f"{r:+.3f}")
            assert mine8[-1] == printed[(tag, var, est)], (tag, var, est, mine8[-1], printed[(tag, var, est)])
            print(f"   {pn}, {var}, {en}: r {r:+.3f}, interval [{lo_:+.3f}, {hi_:+.3f}]; {'includes' if incl else 'excludes'} zero")
assert len(mine8) == 8
print(f"   intervals that include zero: {n_incl} of 8; smallest r {min(mine8, key=float)}, largest {max(mine8, key=float)}")

# 7. The regional relation on one estimator: the windowed estimator's own regional atoms (saved by the regional ΦR
#    analysis, notes/rev_regional_phir.py) against the same windowed regional r₁ (B11's table)
print("7. Regional sts of the windowed estimator (notes/review_results/regional/regional_atoms_raw_ts_gsr_win60.npy: "
      "subjects × runs × windows × regions × atoms; placebo run, windows 1–4, mean over subjects and windows) against "
      "regional r₁ (notes/review_results/partB/regional_sts_r1.csv, r1_windowed)")
A = np.load(RR / "regional" / "regional_atoms_raw_ts_gsr_win60.npy")
assert A.shape == (14, 2, 14, 115, 16) and not np.isnan(A).any(), A.shape
print(f"   check: the array's whole-brain sts, windows 1–4, is {A[:, 0, 0:4, :, 15].mean():.4f} on the DMT run and "
      f"{A[:, 1, 0:4, :, 15].mean():.4f} on the placebo run (Table 2: 1.1554 and 1.1378)")
with open(RR / "partB" / "regional_sts_r1.csv", encoding="utf-8") as fh:
    rs = list(csv.DictReader([l for l in fh if not l.startswith("#")]))
assert len(rs) == 115
r1w = np.array([float(r["r1_windowed"]) for r in rs]); cort = np.array([r["cortical"] == "True" for r in rs])
stsg = np.array([float(r["sts_pcb_pre"]) for r in rs])
assert int(cort.sum()) == 99
stsw = A[:, 1, 0:4, :, 15].mean(axis=(0, 1)); rtrw = A[:, 1, 0:4, :, 0].mean(axis=(0, 1))

def rank(v):
    o = np.argsort(v); r = np.empty(len(v)); r[o] = np.arange(len(v)); return r

for name, y in (("windowed sts", stsw), ("global-fit sts (the map of Results 3)", stsg), ("windowed rtr", rtrw)):
    b = np.polyfit(r1w, y, 1)[0]
    print(f"   {name} on r₁, 115 regions: r {np.corrcoef(r1w, y)[0, 1]:+.3f}, Spearman {np.corrcoef(rank(r1w), rank(y))[0, 1]:+.3f}, "
          f"slope {b:+.4f} nats per unit r₁; 99 cortical parcels: r {np.corrcoef(r1w[cort], y[cort])[0, 1]:+.3f}")

# 8. The leave-one-out of the sts DiD's slope on the r₁ DiD (the slope of Results 2; B27's per-subject table)
print("8. The OLS slope of the sts DiD on the whole-brain r₁ DiD across the 14 subjects, ts_gsr W60 (baseline_gap.csv), "
      "with each subject left out")

def did_of(q):
    sel = [r for r in bg if r["quantity"] == q and r["variant"] == "ts_gsr" and r["W"] == "60"]
    assert len(sel) == 14
    return np.array([float(r["did"]) for r in sel])

ys, xs = did_of("sts"), did_of("r1")
loo = [float(np.polyfit(np.delete(xs, i), np.delete(ys, i), 1)[0]) for i in range(14)]
print(f"   all 14 subjects: slope {np.polyfit(xs, ys, 1)[0]:+.3f}; one subject left out: {min(loo):+.3f} (without subject "
      f"{int(np.argmin(loo)) + 1}) to {max(loo):+.3f} (without subject {int(np.argmax(loo)) + 1})")

# 9. The parts of the sts DiD's between-subject variance: DiD = post gap − pre gap, so
#    Var(DiD) = Var(post gap) + Var(pre gap) − 2 Cov(post gap, pre gap)
print("9. The between-subject variance of the sts DiD by its parts, ts_gsr W60 (baseline_gap.csv): DiD = post gap − pre gap, "
      "Var(DiD) = Var(post gap) + Var(pre gap) − 2 Cov(post gap, pre gap)")
sel = [r for r in bg if r["quantity"] == "sts" and r["variant"] == "ts_gsr" and r["W"] == "60"]
assert len(sel) == 14
pre = np.array([float(r["pre_gap"]) for r in sel]); post = np.array([float(r["post_gap"]) for r in sel]); did = post - pre
v_did, v_post, v_pre = did.var(ddof=1), post.var(ddof=1), pre.var(ddof=1)
cov = float(np.cov(post, pre, ddof=1)[0, 1])
assert abs(v_did - (v_post + v_pre - 2 * cov)) < 1e-12
print(f"   shares of Var(DiD): post gap {v_post / v_did:.2f}, pre gap {v_pre / v_did:.2f}, −2 Cov {(-2 * cov) / v_did:.2f} "
      f"(the pre gap's and the covariance's together {1 - v_post / v_did:.2f}; the post gap's and the covariance's together "
      f"{1 - v_pre / v_did:.2f}); "
      f"r(pre gap, post gap) {np.corrcoef(pre, post)[0, 1]:+.3f}; r(DiD, post gap) {np.corrcoef(did, post)[0, 1]:+.3f}")

# 10. The cross-half correlations of the residual DiD with the r₁ DiD, which the main text quotes, from the committed
#     per-subject series: the residual's window series of B4 (diag_series_<variant>_W60.npz, key res), halved as the
#     split-half test halves it (partB7_splithalf.py: odd, windows 1 and 3 before and 7, 9, 11 and 13 after the
#     injection; even, windows 2 and 4 before and 6, 8, 10, 12 and 14 after), and the r₁ half DiDs of
#     splithalf_subjects.csv; their Fisher-z intervals, their mean, and the ceiling that the two split-half
#     reliabilities set. Each correlation, reliability and p is compared, at three decimals, with the value that the
#     split-half test's log prints (splithalf.log, B7).
print("10. The cross-half correlations of the residual DiD with the r₁ DiD, from the committed per-subject series "
      "(notes/review_results/partB/diag_series_<variant>_W60.npz, key res, with the halves of the split-half test; "
      "splithalf_subjects.csv, r1_odd and r1_even), with Fisher-z 95 % intervals at N = 14, their mean and the ceiling "
      "√(rel(residual DiD) × rel(r₁ DiD)); each correlation, reliability and p equals, at three decimals, the value that "
      "the split-half test's log prints (splithalf.log)")
HALF = {"odd": (np.array([0, 2]), np.array([6, 8, 10, 12])), "even": (np.array([1, 3]), np.array([5, 7, 9, 11, 13]))}


def half_did(x, h):
    pre_, post_ = HALF[h]
    ch = x[:, :, post_].mean(2) - x[:, :, pre_].mean(2)
    return ch[:, 0] - ch[:, 1]


var, logv = None, {}
for l in (RR / "partB" / "splithalf.log").read_text(encoding="utf-8").split("\n"):
    m = re.match(r"# (ts_gsr|ts_demean), W = 60", l)
    if m:
        var = m.group(1)
    m = re.match(r"split-half reliability \(odd vs even\) — residual DiD: ([+-]\d\.\d{3}) \(p = (\d\.\d{3});.*?"
                 r"autocorrelation DiD: ([+-]\d\.\d{3}) \(p = (\d\.\d{3});", l)
    if m:
        logv.setdefault(var, {})["rel"] = m.groups()
    m = re.search(r"cross r\(res_odd, ac_even\) = ([+-]\d\.\d{3}) .*?r\(res_even, ac_odd\) = ([+-]\d\.\d{3}) ", l)
    if m and l.startswith("context"):
        logv.setdefault(var, {})["cross"] = m.groups()
assert set(logv) == {"ts_gsr", "ts_demean"} and all(set(v) == {"rel", "cross"} for v in logv.values()), logv
with open(RR / "partB" / "splithalf_subjects.csv", encoding="utf-8") as fh:
    sh_all = list(csv.DictReader([l for l in fh if not l.startswith("#")]))
for v in ("ts_gsr", "ts_demean"):
    rows_v = [r for r in sh_all if r["variant"] == v]
    assert len(rows_v) == 14 and [int(r["subject"]) for r in rows_v] == list(range(1, 15))
    r1o, r1e = (np.array([float(r[k]) for r in rows_v]) for k in ("r1_odd", "r1_even"))
    z = np.load(RR / "partB" / f"diag_series_{v}_W60.npz")
    res_, obs_ = z["res"], z["obs"]
    assert res_.shape == (14, 2, 14) and np.isfinite(res_).all()
    # the file's sts halves are the halves of the observed series: the two files halve the windows alike
    for h, k in (("odd", "sts_odd"), ("even", "sts_even")):
        assert np.abs(half_did(obs_, h) - np.array([float(r[k]) for r in rows_v])).max() < 1e-9, (v, h)
    reo, ree = half_did(res_, "odd"), half_did(res_, "even")
    c1, c2 = float(np.corrcoef(reo, r1e)[0, 1]), float(np.corrcoef(ree, r1o)[0, 1])
    (rel_res, p_res), (rel_r1, p_r1) = stats.pearsonr(reo, ree), stats.pearsonr(r1o, r1e)
    mine = (f"{rel_res:+.3f}", f"{p_res:.3f}", f"{rel_r1:+.3f}", f"{p_r1:.3f}")
    assert mine == logv[v]["rel"] and (f"{c1:+.3f}", f"{c2:+.3f}") == logv[v]["cross"], (v, mine, logv[v], c1, c2)
    f1, f2 = fisher(c1), fisher(c2)
    mean, ceil = 0.5 * (c1 + c2), float(np.sqrt(rel_res * rel_r1))
    big = max(abs(c1), abs(c2))
    print(f"   {v}: r(res_odd, r₁_even) {c1:+.3f} [{f1[0]:+.3f}, {f1[1]:+.3f}], r(res_even, r₁_odd) {c2:+.3f} [{f2[0]:+.3f}, {f2[1]:+.3f}]; "
          f"mean {mean:+.4f}; reliabilities {rel_res:.3f} (residual DiD; p = {p_res:.3f}) and {rel_r1:.3f} (r₁ DiD; p = {p_r1:.3f}), "
          f"ceiling {ceil:.3f}; |mean| / ceiling {abs(mean) / ceil:.2f}; the larger of the two correlations, {big:.3f} in size, is "
          f"{'above' if big > ceil else 'below'} the ceiling")

# 11. Every cell of B27's table (a) recomputed from the six-decimal per-subject file with the run's own formulas
#     (partB27_baseline_gap.py: tint, signflip_p, ols) and compared, as printed, with the run's table
print("11. B27's table (a) recomputed from the six-decimal per-subject file (baseline_gap.csv: pre_gap, post_gap, did) with "
      "the run's formulas, each cell compared as printed with notes/review_results/partB/baseline_gap_tables.md")
SIGNS = np.array(list(product((-1, 1), repeat=14)))


def sf_count(v):
    v = np.asarray(v, float)
    return int((np.abs((SIGNS * v).mean(1)) >= abs(v.mean()) - 1e-12).sum())


def tint(v):
    r = signflip_inversion(np.asarray(v, float))
    assert r["grid_violations"] == 0
    return r["mean"], r["lo"], r["hi"]


def ols12(x, y):
    X = np.c_[np.ones(x.size), x]; b = np.linalg.lstsq(X, y, rcond=None)[0]; e = y - X @ b
    cv = (e ** 2).sum() / (x.size - 2) * np.linalg.inv(X.T @ X); t = stats.t.ppf(0.975, x.size - 2)
    return b[1], t * np.sqrt(cv[1, 1]), b[0], t * np.sqrt(cv[0, 0])


tab = {}
for l in (RR / "partB" / "baseline_gap_tables.md").read_text(encoding="utf-8").split("\n"):
    c = [x.strip() for x in l.split("|")]
    if len(c) == 15 and c[1] in ("sts", "r1", "substituted", "residual"):
        tab[(c[1], c[2], c[3])] = c[4:14]
assert len(tab) == 12, len(tab)
ncell, differ = 0, []
for (q, var, W), cells in tab.items():
    sel = [r for r in bg if r["quantity"] == q and r["variant"] == var and r["W"] == W]
    assert len(sel) == 14
    g = np.array([float(r["pre_gap"]) for r in sel]); pg = np.array([float(r["post_gap"]) for r in sel]); dd = np.array([float(r["did"]) for r in sel])
    (m, lo, hi), (mp, plo, phi), (md, dlo, dhi) = tint(g), tint(pg), tint(dd)
    sl, sl_h, ic, ic_h = ols12(g, pg)
    mine = [f"{m:+.4f} [{lo:+.4f}, {hi:+.4f}]", f"{sf_count(g) / 16384:.4f}; {int((g > 0).sum())}/14", f"{mp:+.4f} [{plo:+.4f}, {phi:+.4f}]",
            f"{sf_count(pg) / 16384:.4f}; {int((pg < 0).sum())}/14", f"{md:+.4f} [{dlo:+.4f}, {dhi:+.4f}]", f"{sf_count(dd) / 16384:.4f}",
            f"{ic:+.4f} [{ic - ic_h:+.4f}, {ic + ic_h:+.4f}]", f"{sl:+.3f} [{sl - sl_h:+.3f}, {sl + sl_h:+.3f}]",
            f"{np.corrcoef(dd, g)[0, 1]:+.3f}", f"{np.corrcoef(dd, pg)[0, 1]:+.3f}"]
    for k, (a_, b_) in enumerate(zip(cells, mine)):
        ncell += 1
        if a_ != b_:
            differ.append(((q, var, W), k, a_, b_, g))
print(f"   cells compared {ncell} (12 rows × 10 cells); recomputed as printed {ncell - len(differ)}; not {len(differ)}")
assert len(differ) == 1 and differ[0][0] == ("r1", "ts_demean", "60") and differ[0][1] == 1, [d[:4] for d in differ]
(_, _, a_, b_, g) = differ[0]
cnt = sf_count(g)
run_p = a_.split(";")[0]
fits = [c for c in range(0, 16385, 2) if f"{c / 16384:.4f}" == run_p]
assert len(fits) == 1 and cnt % 2 == 0, fits
# The file gives each value to six decimals, so each is within 0.5 × 10⁻⁶ of the run's. For an assignment of signs, the
# difference between its absolute mean and the observed absolute mean is −2/14 times the sum of the values of one of
# its two sign groups (the flipped ones if its mean has the observed sign, the others if not), so that the rounding
# moves it by at most k/14 × 10⁻⁶, k the number of values in that group. In units of 10⁻⁶ (integers):
xi = np.rint(g * 1e6).astype(int)
assert np.abs(g * 1e6 - xi).max() < 1e-4 and xi.sum() > 0
tot = int(xi.sum())
m_int = SIGNS @ xi
k_flip = (SIGNS == -1).sum(1)
same = m_int >= 0
d_units = np.where(same, m_int - tot, -m_int - tot)        # 14 × 10⁶ × (|mean of the assignment| − |observed mean|)
k_grp = np.where(same, k_flip, 14 - k_flip)
assert int((d_units >= 0).sum()) == cnt
others = k_grp > 0                                          # not the observed assignment or its mirror
within = others & (np.abs(d_units) <= k_grp)
in_cnt, out_cnt = within & (d_units >= 0), within & (d_units < 0)
assert in_cnt.sum() % 2 == 0 and out_cnt.sum() % 2 == 0
pairs_in = sorted({(int(d), int(k)) for d, k in zip(d_units[in_cnt], k_grp[in_cnt])})
assert int(in_cnt.sum()) == 2 * len(pairs_in), pairs_in    # each margin belongs to one assignment and its mirror
lo_cnt, hi_cnt = cnt - int(in_cnt.sum()), cnt + int(out_cnt.sum())
assert lo_cnt <= fits[0] <= hi_cnt and (cnt - fits[0]) % 2 == 0
desc = "; ".join(f"margin {d / 14:.2f} × 10⁻⁶ against a bound of {k / 14:.2f} × 10⁻⁶" for d, k in pairs_in)
print(f"   the cell that differs: the exact p of the pre gap of r1, ts_demean, W = 60: {run_p} in the run's table, "
      f"{cnt / 16384:.4f} from the file ({cnt} of 16384 sign assignments); the even count that prints the run's value is "
      f"{fits[0]}; the file's rounding can move the difference between an assignment's absolute mean and the observed one "
      f"by at most k/14 × 10⁻⁶ (k of the fourteen values enter it): {len(pairs_in)} assignments and their mirrors are "
      f"counted from the file with a margin within that bound ({desc}), and {int(out_cnt.sum()) // 2} left uncounted lie "
      f"within it, so that the unrounded values give between {lo_cnt} and {hi_cnt}; the run's {fits[0]} is {(cnt - fits[0]) // 2} "
      f"such pair fewer than the file's")

# 12. Values that B27's pre-run entry lists as known before the run (its item (i)), recomputed from the per-subject
#     file and compared with the values as the entry prints them: those that the run's tables file does not print
#     (r², the two SDs, the values of subjects 14 and 8, the regression's intercept), with the regression's slope and
#     r, which it prints in its table (c), and the ratio of means, which B28's tables file prints
print("12. Values that B27's pre-run entry lists as known (record, 'What is known before the run', item (i)), recomputed "
      "from baseline_gap.csv (ts_gsr, W = 60) and compared with the entry's: r², the SDs, the values of subjects 14 and 8 and "
      "the intercept, which baseline_gap_tables.md does not print; the slope and r, which it prints; the ratio of means, "
      "which matched_slope_tables.md prints")


def col(q, name):
    sel = [r for r in bg if r["quantity"] == q and r["variant"] == "ts_gsr" and r["W"] == "60"]
    assert len(sel) == 14 and [int(r["subject"]) for r in sel] == list(range(1, 15))
    return np.array([float(r[name]) for r in sel])


s_did, s_pre, s_post = col("sts", "did"), col("sts", "pre_gap"), col("sts", "post_gap")
r1_did, res_did = col("r1", "did"), col("residual", "did")
X = np.c_[np.ones(14), r1_did]
b0, b1 = np.linalg.lstsq(X, res_did, rcond=None)[0]
mine12 = [f"{np.corrcoef(s_did, s_pre)[0, 1] ** 2:.2f}", f"{s_did.std(ddof=1):.4f}", f"{s_post.std(ddof=1):.4f}", f"{s_did[13]:+.4f}",
          f"{s_pre[13]:+.4f}", f"{s_post[13]:+.4f}", f"{s_did[7]:+.4f}", f"{s_pre[7]:+.4f}", f"{b1:+.3f}", f"{b0:+.4f}",
          f"{np.corrcoef(r1_did, res_did)[0, 1]:+.3f}", f"{res_did.mean() / r1_did.mean():+.3f}"]
# the values as the pre-run entry prints them (its minus signs written here as hyphens)
ENTRY12 = ["0.79", "0.0887", "0.0485", "+0.0949", "-0.1121", "-0.0172", "-0.2795", "+0.0914", "-0.753", "+0.0005", "-0.780", "-0.788"]
equal12 = sum(a == b for a, b in zip(mine12, ENTRY12))
print(f"   sts: r(DiD, pre gap)² {mine12[0]}; SD of the DiD {mine12[1]}, of the post gap {mine12[2]}; subject 14: DiD {mine12[3]}, "
      f"pre gap {mine12[4]}, post gap {mine12[5]}; subject 8: DiD {mine12[6]}, pre gap {mine12[7]}; the residual DiD on the r₁ DiD: "
      f"slope {mine12[8]}, intercept {mine12[9]}, r {mine12[10]}; ratio of the means of the residual DiD and the r₁ DiD {mine12[11]}")
print(f"   compared with the entry's values as printed there: {equal12} of {len(ENTRY12)} equal")

# 13. B15: the difference between the runs (DMT − placebo) in the run-level directed response and in the RMS of δ_anti,
#     per subject, from the per-run values of directed_crosslag.csv, with the interval that inverts the sign-flip test
#     (S3 Text §6 quotes the first; the tables file prints the two means and their p)
print("13. B15, the DMT − placebo difference of the run-level directed response (resp_anti_run) and of the RMS of δ_anti "
      "(rms_anti_run), per subject, from notes/review_results/partB/directed_crosslag.csv: mean [lo, hi] (inverted "
      "sign-flip 95 % interval), exact p")
with open(RR / "partB" / "directed_crosslag.csv", encoding="utf-8") as fh:
    dc = list(csv.DictReader([l for l in fh if not l.startswith("#")]))
dtab = (RR / "partB" / "directed_crosslag_tables.md").read_text(encoding="utf-8")
m13 = re.search(r"DMT − placebo of the run-level RMS of δ_anti: ([+-]\d\.\d{5}), sign-flip p = (\d\.\d{4}); of the directed "
                r"response: ([+-]\d\.\d{5}), p = (\d\.\d{4})\.", dtab)
assert m13, "the tables file's line on the difference between the runs"
for var in ("ts_gsr", "ts_demean"):
    for colname, what in (("resp_anti_run", "directed response"), ("rms_anti_run", "RMS of δ_anti")):
        diff = []
        for s in range(1, 15):
            a = {r["run"]: float(r[colname]) for r in dc if r["variant"] == var and int(r["subject"]) == s}
            assert set(a) == {"DMT", "PCB"}, (var, s, a)
            diff.append(a["DMT"] - a["PCB"])
        inv = signflip_inversion(np.asarray(diff, float))
        assert inv["grid_violations"] == 0
        if var == "ts_gsr":      # the first ts_gsr block of the tables file prints these two means and p
            want = (m13.group(3), m13.group(4)) if colname == "resp_anti_run" else (m13.group(1), m13.group(2))
            assert (f"{inv['mean']:+.5f}", f"{inv['p_zero']:.4f}") == want, (colname, inv["mean"], inv["p_zero"], want)
        print(f"   {var}, {what}: {inv['mean']:+.5f} [{inv['lo']:+.5f}, {inv['hi']:+.5f}], p = {inv['p_zero']:.4f}, "
              f"{inv['n_neg']}/14 negative")

# 14. B29: the DiD of the count of replaced volumes per window and of the mean framewise displacement, per subject,
#     from the per-window file censoring.csv (post windows 6–14 minus pre windows 1–4, DMT minus placebo), with the
#     interval that inverts the sign-flip test; the means, the p and the counts of positive subjects are those of the
#     run's table (a), and the mean-FD DiD's interval is Table 2's
print("14. B29, the DiD of the count of TRs above the threshold per window (n_above) and of the mean framewise "
      "displacement (mean_fd), per subject, from notes/review_results/partB/censoring.csv: mean [lo, hi] (inverted "
      "sign-flip 95 % interval), exact p, positive/14")
with open(RR / "partB" / "censoring.csv", encoding="utf-8") as fh:
    cz = list(csv.DictReader([l for l in fh if not l.startswith("#")]))
ctab = (RR / "partB" / "censoring_tables.md").read_text(encoding="utf-8")
m14 = re.search(r"\| mean \|.*\| ([+-]\d+\.\d{2}) \(p = (\d\.\d{4}); (\d+)/14 positive\) \| ([+-]\d\.\d{4}) \(p = (\d\.\d{4}); (\d+)/14 positive\) \|", ctab)
assert m14, "the mean row of the run's table (a)"
for colname, what, fmt, want in (("n_above", "count per window", "{:+.2f}", m14.group(1, 2, 3)), ("mean_fd", "mean framewise displacement", "{:+.4f}", m14.group(4, 5, 6))):
    dd = []
    for s in range(1, 15):
        ch = {}
        for run in ("DMT", "PCB"):
            w = {int(r["window"]): float(r[colname]) for r in cz if int(r["subject"]) == s and r["run"] == run}
            assert sorted(w) == list(range(1, 15)), (s, run)
            ch[run] = np.mean([w[k] for k in range(6, 15)]) - np.mean([w[k] for k in range(1, 5)])
        dd.append(ch["DMT"] - ch["PCB"])
    dd = np.asarray(dd, float)
    inv = signflip_inversion(dd)
    assert inv["grid_violations"] == 0
    got = (fmt.format(inv["mean"]), f"{inv['p_zero']:.4f}", str(int((dd > 0).sum())))
    assert got == tuple(want), (colname, got, want)
    print(f"   {what}: {fmt.format(inv['mean'])} [{fmt.format(inv['lo'])}, {fmt.format(inv['hi'])}], p = {inv['p_zero']:.4f}, "
          f"{int((dd > 0).sum())}/14 positive (the run's table (a): {want[0]}, p = {want[1]}, {want[2]}/14 positive)")
