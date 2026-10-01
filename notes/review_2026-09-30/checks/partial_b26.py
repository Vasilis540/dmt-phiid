"""The partial correlations of S3 Text §6 recomputed with the outputs of B26's run (the third review's computation 4).

Planning session, 30 Sep 2026; reads committed result files only (no data). Run from the repository root:
    .venv/bin/python notes/review_2026-09-30/checks/partial_b26.py
Per-subject DiDs (did_subjects, primary set, W = 60) from
notes/review_results/inference_rows_{diag,raw,ccs_pub,ccs}.pkl: the residual DiD, the autocorrelation (r1) DiD, the
MMI-sts DiD and the CCS-sts DiD under the published definition (ccs_pub) and under phyid's mask (ccs). The third review
(notes/adversarial_review_draft_v2_second_pass_2026-09-15.md, Appendix, computation 4) gave, ts_gsr / ts_demean:
r(residual, CCS-sts) +0.799 / +0.875; partial on the autocorrelation DiD +0.831 / +0.855; partial on the MMI-sts DiD
+0.851 / +0.864; with phyid's mask +0.729 / +0.838, partial +0.688 / +0.820; R2 of the residual DiD on the
autocorrelation DiD 0.61 / 0.36, on it and CCS-sts 0.88 / 0.83.
"""
import pickle, subprocess, sys
from pathlib import Path
import numpy as np

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
RR = R / "notes/review_results"
sha = subprocess.run(["git", "-C", str(R), "rev-parse", "--short", "HEAD"], capture_output=True,
                     text=True).stdout.strip()
dirty = subprocess.run(["git", "-C", str(R), "status", "--porcelain", "--untracked-files=no"], capture_output=True,
                       text=True).stdout.strip()
print(f"# partial_b26.py; git={sha}{'-dirty' if dirty else ''}")


def pdid(pkl, label):
    h = [d for d in pickle.load(open(RR / pkl, "rb")) if d["label"] == label and d["set"] == "primary"]
    assert len(h) == 1, (pkl, label, len(h))
    return np.asarray(h[0]["did_subjects"], float)


def resid(y, *xs):
    X = np.column_stack([np.ones(y.size), *xs])
    b, *_ = np.linalg.lstsq(X, y, rcond=None)
    return y - X @ b


def r(a, b):
    return float(np.corrcoef(a, b)[0, 1])


def r2(y, *xs):
    e = resid(y, *xs)
    return 1 - float(e @ e) / float(((y - y.mean()) @ (y - y.mean())))


for var in ("ts_gsr", "ts_demean"):
    y = pdid("inference_rows_diag.pkl", f"diag residual sts {var} W60")
    ac = pdid("inference_rows_raw.pkl", f"autocorr {var} W60")
    mm = pdid("inference_rows_raw.pkl", f"sts {var} W60")
    pub = pdid("inference_rows_ccs_pub.pkl", f"CCSpub sts {var} W60")
    phy = pdid("inference_rows_ccs.pkl", f"CCS sts {var} W60")
    print(f"{var}: r(residual, CCS-sts) {r(y, pub):+.3f}; partial on the autocorrelation DiD "
          f"{r(resid(y, ac), resid(pub, ac)):+.3f}; partial on the MMI-sts DiD {r(resid(y, mm), resid(pub, mm)):+.3f}; "
          f"with phyid's mask {r(y, phy):+.3f}, partial on the autocorrelation DiD "
          f"{r(resid(y, ac), resid(phy, ac)):+.3f}; "
          f"R2 of the residual DiD on the autocorrelation DiD {r2(y, ac):.2f}, on it and CCS-sts {r2(y, ac, pub):.2f}")
