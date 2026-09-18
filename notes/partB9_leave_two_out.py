"""
partB9_leave_two_out.py — leave-two-out on the per-subject collinearity r(MMI-sts DiD, lag-1 autocorrelation DiD),
ts_gsr, W = 60, primary set (Results 3, Figure 3a). Pre-run entry: manuscript/analysis_record.md, "Leave-two-out on
the sts / autocorrelation collinearity", 15 Sep 2026 11:09 UTC; no prediction.

Every pair of subjects is dropped in turn (C(14, 2) = 91 refits) and the Pearson r over the remaining 12 subjects is
recomputed, with the Spearman ρ alongside. This is a sensitivity of one already-reported correlation to any two
subjects; it carries no inference and changes no verdict. Inputs: notes/review_results/inference_rows_raw.pkl
(field did_subjects of the rows "sts ts_gsr W60" and "autocorr ts_gsr W60", primary set), i.e. the per-subject DiDs
Figure 3a plots. Outputs: notes/review_results/partB/leave_two_out.csv (one row per dropped pair) and
leave_two_out.log (the full-set value, the range, the minimum and maximum with the pairs that give them, the median).
Run from the repository root: .venv/bin/python notes/partB9_leave_two_out.py   (seconds)
"""
import itertools
import pickle
import sys
from pathlib import Path

import numpy as np
from scipy.stats import pearsonr, spearmanr

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rev_git import SHA
print(f"git={SHA}", flush=True)

REPO = Path(__file__).resolve().parents[1]
RR = REPO / "notes" / "review_results"
OUT = RR / "partB"
LOG = []


def log(s=""):
    print(s, flush=True)
    LOG.append(s)


def get(rows, label, st="primary"):
    return np.asarray([r for r in rows if r["label"] == label and r["set"] == st][0]["did_subjects"], float)


rows = pickle.load(open(RR / "inference_rows_raw.pkl", "rb"))
sts, ac = get(rows, "sts ts_gsr W60"), get(rows, "autocorr ts_gsr W60")
n = sts.size
r_all, rho_all = pearsonr(sts, ac)[0], spearmanr(sts, ac)[0]
log(f"git={SHA}")
log("# Leave-two-out on r(MMI-sts DiD, lag-1 autocorrelation DiD), ts_gsr, W = 60, primary set (partB9_leave_two_out.py)")
log(f"full set (N = {n}): Pearson r = {r_all:+.3f}, Spearman ρ = {rho_all:+.3f}")
recs = []
for i, j in itertools.combinations(range(n), 2):
    keep = np.array([k for k in range(n) if k not in (i, j)])
    recs.append((i + 1, j + 1, pearsonr(sts[keep], ac[keep])[0], spearmanr(sts[keep], ac[keep])[0]))
r = np.array([x[2] for x in recs]); rho = np.array([x[3] for x in recs])
imin, imax = int(np.argmin(r)), int(np.argmax(r))
log(f"leave-two-out ({len(recs)} refits, N = {n - 2} each): Pearson r range {r.min():+.3f} to {r.max():+.3f}, median {np.median(r):+.3f}; "
    f"minimum {r[imin]:+.3f} without subjects {recs[imin][0]} and {recs[imin][1]}; maximum {r[imax]:+.3f} without subjects {recs[imax][0]} and {recs[imax][1]}")
log(f"Spearman ρ range {rho.min():+.3f} to {rho.max():+.3f}, median {np.median(rho):+.3f}; minimum without subjects {recs[int(np.argmin(rho))][0]} and {recs[int(np.argmin(rho))][1]}")
log(f"refits with r below 0.90: {int((r < 0.90).sum())} of {len(recs)}; below 0.85: {int((r < 0.85).sum())}")
for s in range(1, n + 1):
    sub = r[[k for k, x in enumerate(recs) if s in (x[0], x[1])]]
    log(f"  pairs containing subject {s:2d}: r range {sub.min():+.3f} to {sub.max():+.3f}")
with open(OUT / "leave_two_out.csv", "w") as f:
    f.write(f"# partB9_leave_two_out.py; ts_gsr W60 primary; per-subject DiDs from inference_rows_raw.pkl; subjects 1-based; git={SHA}\n")
    f.write("drop_a,drop_b,pearson_r,spearman_rho\n")
    for a, b, pr, sr in recs:
        f.write(f"{a},{b},{pr:.6f},{sr:.6f}\n")
(OUT / "leave_two_out.log").write_text("\n".join(LOG) + "\n")
print("wrote", OUT / "leave_two_out.csv", "and", OUT / "leave_two_out.log")
