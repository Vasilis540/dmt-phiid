"""Derived numbers for the round-17 text, computed from committed result files only (no subject data).

Planning-session check of 24 Sep 2026 on the text at 66c6331. Run from the repository root:
    python notes/review_2026-09-24/checks/derived_r17.py
Every number printed here is quoted in the text as derived from the named file; seed 20261120.
"""
import csv, math, pickle, subprocess, sys
from pathlib import Path
import numpy as np
from scipy import stats

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
RR = R / "notes/review_results"
SEED, NB = 20261120, 10_000
try:
    sha = subprocess.run(["git", "-C", str(R), "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip() or "nogit"
    dirty = subprocess.run(["git", "-C", str(R), "status", "--porcelain", "--untracked-files=no"], capture_output=True, text=True).stdout.strip()
    sha += "-dirty" if dirty else ""
except Exception:
    sha = "nogit"
print(f"# derived_r17.py; git={sha}; seed={SEED}")


def pdid(pkl, label, st="primary"):
    for d in pickle.load(open(RR / pkl, "rb")):
        if d["label"] == label and d["set"] == st:
            return np.asarray(d["did_subjects"], float)
    raise KeyError(label)


def fieller(y, x, level=0.95):
    """CI for mean(y)/mean(x), paired subjects, t on n-1 df."""
    n = y.size
    t = stats.t.ppf(0.5 + level / 2, n - 1)
    my, mx = y.mean(), x.mean()
    syy, sxx, sxy = np.var(y, ddof=1) / n, np.var(x, ddof=1) / n, np.cov(y, x, ddof=1)[0, 1] / n
    a = mx ** 2 - t ** 2 * sxx
    b = -2 * (mx * my - t ** 2 * sxy)
    c = my ** 2 - t ** 2 * syy
    disc = b * b - 4 * a * c
    if a <= 0 or disc < 0:
        return float("nan"), float("nan")
    r1, r2 = (-b - math.sqrt(disc)) / (2 * a), (-b + math.sqrt(disc)) / (2 * a)
    return min(r1, r2), max(r1, r2)


def boot_ratio(y, x):
    rng = np.random.default_rng(SEED)
    idx = rng.integers(0, y.size, (NB, y.size))
    return np.percentile(y[idx].mean(1) / x[idx].mean(1), [2.5, 97.5])


# 1. Rates as ratios of group means per unit of regional r1 (ts_gsr, W = 60)
r1 = pdid("inference_rows_raw.pkl", "autocorr ts_gsr W60")
sts = pdid("inference_rows_raw.pkl", "sts ts_gsr W60")
res = pdid("inference_rows_diag.pkl", "diag residual sts ts_gsr W60")
for name, y in (("sts", sts), ("residual", res)):
    lo, hi = fieller(y, r1)
    blo, bhi = boot_ratio(y, r1)
    print(f"1. {name} DiD / regional r1 DiD (ratio of means): {y.mean() / r1.mean():+.3f}; Fieller 95 % [{lo:+.2f}, {hi:+.2f}]; "
          f"subject bootstrap 95 % [{blo:+.2f}, {bhi:+.2f}] (means {y.mean():+.5f} / {r1.mean():+.5f})")
print(f"   regional r1 DiD by subject: {np.round(r1, 4).tolist()}; largest fall: subject {int(np.argmin(r1)) + 1} ({r1.min():+.4f})")

# 2. Cross-half relation, leave-one-out (splithalf_subjects.csv)
rows = [r for r in (RR / "partB/splithalf_subjects.csv").read_text().splitlines() if not r.startswith("#")]
SP = list(csv.DictReader(rows))


def four(so, se, ro, re_):
    x1, x2 = np.corrcoef(so, re_)[0, 1], np.corrcoef(se, ro)[0, 1]
    rs, ra = np.corrcoef(so, se)[0, 1], np.corrcoef(ro, re_)[0, 1]
    ce = math.sqrt(max(rs, 0) * max(ra, 0))
    return (x1 + x2) / 2, ce, ((x1 + x2) / 2 / ce if ce > 0 else float("nan"))


for var in ("ts_gsr", "ts_demean"):
    v = {k: np.array([float(r[k]) for r in SP if r["variant"] == var]) for k in ("sts_odd", "sts_even", "r1_odd", "r1_even")}
    subj = [int(r["subject"]) for r in SP if r["variant"] == var]
    m, c, d = four(v["sts_odd"], v["sts_even"], v["r1_odd"], v["r1_even"])
    print(f"2. {var} all 14: mean cross-half r {m:.3f}, ceiling {c:.3f}, ratio {d:.3f}")
    out = []
    for i in range(14):
        keep = np.arange(14) != i
        mi, ci, di = four(*(v[k][keep] for k in ("sts_odd", "sts_even", "r1_odd", "r1_even")))
        out.append((subj[i], mi, ci, di))
        print(f"   without subject {subj[i]:2d}: mean cross-half r {mi:.3f}, ceiling {ci:.3f}, ratio {di:.3f}")
    others = [o for o in out if o[0] not in (8, 14)]
    print(f"   {var}: other twelve omissions, mean cross-half r {min(o[1] for o in others):.3f}-{max(o[1] for o in others):.3f}; "
          f"ratio {min(o[3] for o in others):.3f}-{max(o[3] for o in others):.3f}")

# 3. The partialled sensory - association contrast (regional_partial_tables.md, per-subject mean ± SD)
t13 = stats.t.ppf(0.975, 13)
for lab, m, sd in (("before partialling", -0.0202, 0.0243), ("after partialling", 0.0007, 0.0203)):
    h = t13 * sd / math.sqrt(14)
    print(f"3. sensory - association contrast {lab}: {m:+.4f} [{m - h:+.4f}, {m + h:+.4f}] (t interval, 13 df, from mean ± SD)")

# 4. Regional map, cortex only (regional_sts_r1.csv)
reg = list(csv.DictReader((RR / "partB/regional_sts_r1.csv").read_text().splitlines()))
cort = [r for r in reg if r["cortical"] == "True"]
xs = np.array([float(r["r1_windowed"]) for r in cort]); ys = np.array([float(r["sts_pcb_pre"]) for r in cort])
xa = np.array([float(r["r1_windowed"]) for r in reg]); ya = np.array([float(r["sts_pcb_pre"]) for r in reg])
print(f"4. regional sts on regional r1: all {len(reg)} regions Pearson {np.corrcoef(xa, ya)[0, 1]:+.3f}, slope {np.polyfit(xa, ya, 1)[0]:+.3f}; "
      f"cortex ({len(cort)}) Pearson {np.corrcoef(xs, ys)[0, 1]:+.3f}, Spearman {stats.spearmanr(xs, ys)[0]:+.3f}, slope {np.polyfit(xs, ys, 1)[0]:+.3f}")

# 5. Bounds and closed-form constants
a, q = 0.85, 0.25
print(f"5. band-limit bound at TR 2 s: cos(2*pi*0.08*2) = {math.cos(2 * math.pi * 0.08 * 2):.4f}; "
      f"flat 0.01-0.08 Hz: r1 = {(math.sin(2*math.pi*0.08*2) - math.sin(2*math.pi*0.01*2)) / (2*math.pi*2*0.07):.4f}")
print(f"   family at (0.85, 0.25): dsts/dr1 = {2*a/(1-a*a) - a*q*q/(1-a*a*q*q):.4f}; drtr/dr1 = {a*q*q/(1-a*a*q*q):.4f}; "
      f"S'(a) = {a/(1-a*a):.4f}")
print(f"   windowed estimator's own per-SD ratio: (5.126 x 0.0284)/(0.528 x 0.1957) = {5.126*0.0284/(0.528*0.1957):.2f}")

# 6. The finite-sample null's own pair-r1 DiD (review_v2_residual_null.log)
print(f"6. null pair r1 DiD: (0.8532 - 0.8625) - (0.8655 - 0.8602) = {(0.8532-0.8625)-(0.8655-0.8602):+.4f}; "
      f"level ratios: {0.0373/0.0489:.2f} (all cells, W = 60), {0.0353/0.0530:.2f} (DMT pre)")
