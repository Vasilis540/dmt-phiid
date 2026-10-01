"""The conversions of S3 Text §6 (B22's outcome entry) recomputed with the outputs of B26's run, at full precision.

Planning session, 30 Sep 2026; reads committed result files only (no data). Run from the repository root:
    .venv/bin/python notes/review_2026-09-30/checks/conversions_b26.py
Per unit of A_other the residual changes by B23 (b)'s ratio of its two changes (diagnostic_alternatives.csv, part b);
A_other's DiD per subject is B22's (aligned_directed.csv: windows 1-4 against 6-14, DMT minus placebo), with the
inverted sign-flip interval of notes/rev_inference_inverted.py; the band-passed generator's expectation of that DiD
is the mean of B24's 20 W = 60 replicates (bandpassed_expectations.csv); the residual DiD and B17b's condition (i)
expectation are B21's and B17b's (inference_revision.csv; calibration_filtered.csv).
"""
import csv, subprocess, sys
from pathlib import Path
import numpy as np

R = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
P = R / "notes/review_results/partB"
sys.path.insert(0, str(R / "notes"))
from rev_inference_inverted import signflip_inversion  # noqa: E402

sha = subprocess.run(["git", "-C", str(R), "rev-parse", "--short", "HEAD"], capture_output=True,
                     text=True).stdout.strip()
dirty = subprocess.run(["git", "-C", str(R), "status", "--porcelain", "--untracked-files=no"], capture_output=True,
                       text=True).stdout.strip()
print(f"# conversions_b26.py; git={sha}{'-dirty' if dirty else ''}")
for f in ("diagnostic_alternatives.csv", "aligned_directed.csv", "bandpassed_expectations.csv",
          "inference_revision.csv", "calibration_filtered.csv"):
    print(f"#   {f}: {open(P / f, encoding='utf-8').readline().strip()}")


def rows(f):
    with open(P / f, encoding="utf-8") as fh:
        next(fh)
        return list(csv.DictReader(fh))


B23 = rows("diagnostic_alternatives.csv")


def b23(cond, qty):
    h = [r for r in B23 if r["part"] == "b" and r["condition"] == cond and r["quantity"] == qty and r["a"] == "0.85"]
    assert len(h) == 1, (cond, qty, len(h))
    return float(h[0]["value"])


CONV = {}
for key, cond in (("aligned, δ = −0.01·sign(q)", "(a2) δ = −0.01 × sign(q)"),
                  ("aligned, δ = +0.01·sign(q)", "(a2) δ = +0.01 × sign(q)"),
                  ("Δa_s = −0.03", "(a5) Δa_s = −0.03 (against the (a5) base)"),
                  ("λ → 0.9λ", "(a5) λ → 0.9λ (against the (a5) base)")):
    dres, dao = b23(cond, "Δ residual"), b23(cond, "Δ A_other")
    CONV[key] = dres / dao
    print(f"1. B23 (b) {key}: Δ residual {dres:+.8f} / Δ A_other {dao:+.8f} = {CONV[key]:+.4f} per unit of A_other")

E24 = float(np.mean([float(r["A_other_did"]) for r in rows("bandpassed_expectations.csv") if r["estimator"] == "W60"]))
print(f"2. B24's expectation of the A_other DiD (mean of its W = 60 replicates): {E24:+.7f}")

PRE, POST = np.arange(0, 4), np.arange(5, 14)
B22 = rows("aligned_directed.csv")
RES = {}
for var in ("ts_gsr", "ts_demean"):
    x = np.full((14, 2, 14), np.nan)
    for r in B22:
        if r["variant"] == var:
            x[int(r["subject"]) - 1, 0 if r["run"] == "DMT" else 1, int(r["window"]) - 1] = float(r["A_other"])
    ch = np.nanmean(x[:, :, POST], axis=2) - np.nanmean(x[:, :, PRE], axis=2)
    did = ch[:, 0] - ch[:, 1]
    s = signflip_inversion(did)
    raw = (s["mean"], s["lo"], s["hi"])
    net = (s["mean"] - E24, s["lo"] - E24, s["hi"] - E24)
    RES[var] = net
    print(f"3. {var}: A_other DiD {raw[0]:+.6f} [{raw[1]:+.6f}, {raw[2]:+.6f}]; net of B24's expectation "
          f"{net[0]:+.6f} [{net[1]:+.6f}, {net[2]:+.6f}]")
    # S3 Text converts ts_gsr's change net of the expectation and ts_demean's change as it is (B22's outcome entry)
    for lab, v3 in (("net of the expectation", net), ("as it is", raw)):
        quoted = (var == "ts_gsr") == (lab == "net of the expectation")
        for key in ("aligned, δ = −0.01·sign(q)", "Δa_s = −0.03"):
            c = CONV[key]
            v = sorted(c * np.array(v3[1:]))
            print(f"   {lab}, at {c:+.4f} ({key}): residual change {c * v3[0]:+.6f} [{v[0]:+.6f}, {v[1]:+.6f}]"
                  + ("   <- S3 Text §6" if quoted else ""))

inf = rows("inference_revision.csv")
res = [r for r in inf if r["label"] == "diag residual sts ts_gsr W60" and r["set"] == "primary" and r["field"] == "did"]
assert len(res) == 1
RD = float(res[0]["mean"])
E17 = float(np.mean([float(r["res_did"]) for r in rows("calibration_filtered.csv")
                     if r["condition"].startswith("(i)") and r["estimator"] == "W60"]))
EXC = RD - E17
print(f"4. the residual DiD (B21, ts_gsr, W = 60) {RD:+.10f}; B17b's condition (i) expectation (mean of its W = 60 "
      f"replicates) {E17:+.10f}; the excess {EXC:+.10f}")
lo, hi = [], []
for key in ("aligned, δ = −0.01·sign(q)", "Δa_s = −0.03"):
    c = CONV[key]
    net = RES["ts_gsr"]
    v = sorted(c * np.array(net[1:]))
    f = c * net[0] / EXC
    lo.append(v[0] / EXC); hi.append(v[1] / EXC)
    print(f"   ts_gsr at {c:+.4f}: {c * net[0]:+.6f} of the excess, a fraction {f:.4f} "
          f"[{v[0] / EXC:+.4f}, {v[1] / EXC:+.4f}]")
print(f"   the fractions' range over the two conversions: [{min(lo):+.4f}, {max(hi):+.4f}]")
