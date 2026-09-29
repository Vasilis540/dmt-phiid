#!/usr/bin/env python3
"""b25_fill.py — the text that reports B25, written from B25's outputs alone. Fixed with B25's pre-run entry, before B25
was run on the family (record, "The binarised estimators on the AR(1) family (B25): pre-run entry"): the verdicts follow
that entry's criteria mechanically and every sentence below is a template whose only free parts are values read from
`notes/review_results/partB/binarised.csv` and the dates and times of the entry, the run and this script's own run.

Usage, from the repository root, after B25 has run at the commit of its pre-run entry (the tree otherwise unchanged):
    python3 notes/review_2026-09-28/revision/b25_fill.py <that commit, short SHA> [--now "D Mon YYYY HH:MM"]
The outcome entry is dated now (UTC); --now gives the time instead, to reproduce a fill made earlier.

It stops, writing nothing, if an output is missing, names another commit or a dirty tree, does not match the sha256 the
tables give for `binarised.csv`, or reports a failed check; if the pre-run entry's time is not filled; or if any
replacement does not find its text exactly once. Otherwise it writes the replacements it applies to
`notes/review_2026-09-28/revision/text_replacements_2026-09-28_b25.json`, applies them with
`notes/review_2026-09-25/revision/apply_replacements.py`, updates `manuscript/main_text_numbers.csv` (the five rows of
the count of predictions and the contexts the edits reach), appends the outcome entry to the record, runs the
repository's checks and prints READY or NOT READY. It reads the verdict criteria from nowhere but this file. It states
no result of the separate session's re-run of B25: the text names that re-run only as still to be made, and the commit
that follows the re-run records its result.
"""
import csv
import difflib
import hashlib
import io
import json
import math
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path.cwd()
A = sys.argv[1]
if not re.fullmatch(r"[0-9a-f]{7}", A):
    sys.exit("NOTHING WRITTEN: the first argument must be the commit's short SHA (7 hexadecimal characters)")
if "--now" in sys.argv:
    NOW = sys.argv[sys.argv.index("--now") + 1]
else:
    g = time.gmtime()
    NOW = f"{g.tm_mday} {time.strftime('%b %Y %H:%M', g)}"
if not re.fullmatch(r"\d{1,2} [A-Z][a-z]{2} \d{4} \d\d:\d\d", NOW):
    sys.exit(f"NOTHING WRITTEN: --now must read like '29 Sep 2026 10:15', not {NOW!r}")
MONTHS = {"Jan": "January", "Feb": "February", "Mar": "March", "Apr": "April", "May": "May", "Jun": "June",
          "Jul": "July", "Aug": "August", "Sep": "September", "Oct": "October", "Nov": "November", "Dec": "December"}


def long_date(d):
    """'29 Sep 2026' → '29 September 2026'."""
    day, mon, year = d.split()
    return f"{day} {MONTHS[mon]} {year}"


OUTD = ROOT / "notes/review_results/partB"
REC, CSVF, D = "manuscript/analysis_record.md", "manuscript/main_text_numbers.csv", "manuscript/draft_v2.md"
SUP, LIT, S3, S5 = "manuscript/supplementary.md", "notes/partB5_literature_v2.md", "manuscript/si/S3_Text.md", "manuscript/si/S5_Text.md"
REVDIR = "notes/review_2026-09-28/revision"
R1 = [0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95]
QS = [0.1, 0.25, 0.5]
TS = [160, 300, 840]
OP = (0.85, 0.25)
SD_R1, SD_Q = 0.0284, 0.1957
STOPS = []


def stop(msg):
    STOPS.append(msg)
    print("STOP:", msg)


def rd(p):
    return open(ROOT / p, encoding="utf-8", newline="").read()


def wr(p, s):
    open(ROOT / p, "w", encoding="utf-8", newline="").write(s)


def m(v, nd=4, sign=False):
    """A number as the paper prints it: the minus sign U+2212, a plus sign where asked."""
    s = f"{v:+.{nd}f}" if sign else f"{v:.{nd}f}"
    return s.replace("-", "−")


# ------------------------------------------------------------------ the pre-run entry and the outputs
mh = re.search(r"^## The binarised estimators on the AR\(1\) family \(B25\): pre-run entry, (\d{1,2} [A-Z][a-z]{2} \d{4}) "
               r"(\d\d:\d\d) UTC \(appended; nothing above edited\)$", rd(REC), re.M)
if not mh:
    sys.exit("NOTHING WRITTEN: the pre-run entry's heading, with its date and time filled, is not in the record")
DATE_A, TIME_A = mh.group(1), mh.group(2)
for f in ("binarised.csv", "binarised_tables.md", "binarised_run.log"):
    if not (OUTD / f).exists():
        sys.exit(f"NOTHING WRITTEN: notes/review_results/partB/{f} is missing")
tables = (OUTD / "binarised_tables.md").read_text(encoding="utf-8")
log = (OUTD / "binarised_run.log").read_text(encoding="utf-8")
csv_text = (OUTD / "binarised.csv").read_text(encoding="utf-8")
TL = tables.split("\n")
if TL[1] != f"git={A}":
    sys.exit(f"NOTHING WRITTEN: binarised_tables.md names {TL[1]!r}, not git={A}")
if log.split("\n")[0] != f"git={A}":
    sys.exit(f"NOTHING WRITTEN: binarised_run.log begins {log.split(chr(10))[0]!r}, not git={A}")
mr = re.fullmatch(r"run (\d{1,2} [A-Z][a-z]{2} \d{4}) (\d\d:\d\d) UTC", TL[2])
if not mr:
    sys.exit(f"NOTHING WRITTEN: binarised_tables.md's third line is {TL[2]!r}, not the time of the run")
RUN_DATE = mr.group(1)
if TL[3] != f"binarised.csv sha256 {hashlib.sha256(csv_text.encode('utf-8')).hexdigest()}":
    sys.exit("NOTHING WRITTEN: binarised.csv does not match the sha256 that binarised_tables.md gives for it")
if csv_text.split("\n")[0] != f"# partB25_binarised.py; git={A}; run {RUN_DATE} {mr.group(2)} UTC":
    sys.exit(f"NOTHING WRITTEN: binarised.csv begins {csv_text.split(chr(10))[0]!r}")
mc = re.search(r"Checks: (\d+), failed (\d+)\.", tables)
if not mc or mc.group(2) != "0":
    sys.exit(f"NOTHING WRITTEN: B25 reports failed checks ({mc.group(0) if mc else 'no count'}); investigate first")
NCHECKS = int(mc.group(1))
WALL = int(re.search(r"Wall-clock (\d+) s\.", tables).group(1))
ENV = re.search(r"python [\d.]+, numpy [\S]+, scipy [\S]+, phyid [^.]+(?:\.[^ .]+)*", tables).group(0).rstrip(".")
V = {}
for row in csv.DictReader(io.StringIO("\n".join(l for l in csv_text.split("\n") if not l.startswith("#")))):
    V[(row["part"], row["quantity"], float(row["r1"]), float(row["q"]), row["T"])] = (float(row["value"]),
                                                                                    float(row["se"]))


def lim(k, r1, q):
    return V[("a", k, r1, q, "inf")][0]


def fin(k, r1, q, T):
    return V[("b", k, r1, q, str(T))]


def rate(k, var, step=""):
    return V[("a", f"d({k})/d{var}{step}", OP[0], OP[1], "inf")][0]


def differentiable(k, var):
    """The script's 1 % rule: the rates at the steps 10⁻⁴ and 10⁻³ agree within 1 % (+ 10⁻⁶)."""
    r, r3 = rate(k, var), rate(k, var, " [step 1e-3]")
    return abs(r - r3) - 0.01 * abs(r) <= 1e-6


def steps(vals):
    return [b - a for a, b in zip(vals[:-1], vals[1:])]


# ------------------------------------------------------------------ the facts and the verdicts (the pre-run entry's criteria)
a_steps = [s for q in QS for k in ("MMI sts", "MMI EC") for s in steps([lim(k, r, q) for r in R1])]
c_steps = [s for T in TS for q in QS for k in ("MMI sts", "MMI EC") for s in steps([fin(k, r, q, T)[0] for r in R1])]
a_up, c_up = sum(s > 0 for s in a_steps), sum(s > 0 for s in c_steps)
dr1, dq = rate("MMI sts", "r1"), rate("MMI sts", "q")
ratio_unit = dr1 / abs(dq) if dq != 0 else math.inf
ratio_sd = dr1 * SD_R1 / (abs(dq) * SD_Q) if dq != 0 else math.inf
VA = "met" if a_up == 42 else ("partly met" if a_up >= 21 else "missed")
VB = ("met" if ratio_sd > 1 else "partly met") if dr1 > 0 else "missed"
VC = "met" if c_up == 126 else ("partly met" if c_up >= 63 else "missed")
if len(a_steps) != 42 or len(c_steps) != 126:
    stop("the grid is not the pre-run entry's")
for k in ("MMI sts",):
    for var in ("r1", "q"):
        if not differentiable(k, var):
            stop(f"the rate d({k})/d{var} differs between the two steps, which the script checks")
# the table's own statement of the facts must agree
fa = re.search(r"that rise in the limit: (\d+) of (\d+)\.", tables)
fc = re.search(r"that rise: (\d+) of (\d+)\.", tables)
if not fa or int(fa.group(1)) != a_up or not fc or int(fc.group(1)) != c_up:
    stop("the facts in binarised_tables.md differ from those recomputed from binarised.csv")


def fmt_ratio(v):
    return "unbounded (∂/∂q = 0)" if math.isinf(v) else m(v, 2)


def desc(k, q, part="a", T=None):
    vals = [lim(k, r, q) for r in R1] if part == "a" else [fin(k, r, q, T)[0] for r in R1]
    st = steps(vals)
    up = sum(s > 0 for s in st)
    if up == 7:
        return "rises with r₁ at every step"
    if up == 0 and all(s < 0 for s in st):
        return "falls with r₁ at every step"
    return f"is not monotone in r₁ (it rises at {up} of the 7 steps)"


def desc_q(k):
    d = [desc(k, q) for q in QS]
    if len(set(d)) == 1:
        return d[0] + " at each q"
    return f"{d[0]} at q = 0.10, {d[1]} at 0.25 and {d[2]} at 0.50"


def rates_of(k, nd=3, against=False):
    """The two rates of k at the operating point, or what the 1 % rule says of them."""
    r1s = f"∂/∂r₁ = {m(rate(k, 'r1'), nd, True)}" if differentiable(k, "r1") else "∂/∂r₁ not differentiable on the 10⁻³ scale"
    qs = f"∂/∂q = {m(rate(k, 'q'), nd, True)}" if differentiable(k, "q") else "∂/∂q not differentiable on the 10⁻³ scale"
    s = f"{r1s} {'against' if against else 'and'} {qs}"
    if not (differentiable(k, "r1") and differentiable(k, "q")):
        s += " (a CCS sign mask changes within 10⁻³ of the point)"
    return s


S_OP = -0.5 * math.log(1 - OP[0] ** 2)
G_STS = 2 * S_OP + 0.5 * math.log(1 - OP[0] ** 2 * OP[1] ** 2)
sop, eop, aop = lim("MMI sts", *OP), lim("MMI EC", *OP), lim("2A", *OP)
bias = [fin("MMI sts", r, q, T)[0] - lim("MMI sts", r, q) for T in TS for q in QS for r in R1]
bias840 = [fin("MMI sts", r, q, 840)[0] - lim("MMI sts", r, q) for q in QS for r in R1]
ccs_op, ccs_code_op, ccsec_op = lim("CCS-pub sts", *OP), lim("CCS-code sts", *OP), lim("CCS EC", *OP)
ince_op = lim("Ince EC", *OP)
ince840 = fin("Ince EC", OP[0], OP[1], 840)
N_MET = {"met": 0, "partly met": 0, "missed": 0}
for v in (VA, VB, VC):
    N_MET[v] += 1
MET, PART, MISS = 25 + N_MET["met"], 14 + N_MET["partly met"], 14 + N_MET["missed"]

# ------------------------------------------------------------------ the texts
d_s, d_e = desc_q("MMI sts"), desc_q("MMI EC")
MMI_DESC = (f"binarised MMI-sts {d_s}, and so does its emergence capacity"
            if d_s == d_e and d_s in ("rises with r₁ at every step at each q", "falls with r₁ at every step at each q")
            else f"binarised MMI-sts {d_s}, and its emergence capacity {d_e}")
if dr1 > 0:
    PER_SD = (f"so that per standard deviation of the pairs' variation within a window (main text, Results 1) the r₁ rate "
              f"is {fmt_ratio(ratio_sd)} times the |q| rate, against 4.7 for the Gaussian atom")
else:
    PER_SD = "so that ∂(MMI-sts)/∂r₁ is not positive there and the per-SD comparison does not arise"
RESULTS = (
    f"In the long-series limit {MMI_DESC}. "
    f"At q = 0.25 MMI-sts goes from {m(lim('MMI sts', 0.6, 0.25))} nats at r₁ = 0.60 to {m(lim('MMI sts', 0.95, 0.25))} "
    f"at 0.95 and is {m(sop)} at the operating point (0.85, 0.25), where the Gaussian atom is {m(G_STS)} and the two "
    f"binarised self-informations, 2A, are {m(aop)}; the emergence capacity there is {m(eop)}, against S = {m(S_OP)} "
    f"for the Gaussian estimator. At the operating point ∂(MMI-sts)/∂r₁ = {m(dr1, 3, True)} and ∂(MMI-sts)/∂q = "
    f"{m(dq, 3, True)} nats per unit, {PER_SD}. At 160, 300 and 840 samples the replicate means of MMI-sts and its "
    f"emergence capacity rise with r₁ at {c_up} of the 126 steps, and the replicate mean of MMI-sts lies between "
    f"{m(min(bias), 4, True)} and {m(max(bias), 4, True)} nats from its limit ({m(min(bias840), 4, True)} to "
    f"{m(max(bias840), 4, True)} at 840 samples). Under CCS, through phyid's discrete path, sts is {m(ccs_op, 4, True)} "
    f"nats at the operating point with the published mask ({m(ccs_code_op, 4, True)} with phyid's) and "
    f"{desc_q('CCS-pub sts')}; the CCS emergence capacity is {m(ccsec_op, 4, True)} there and {desc_q('CCS EC')}. "
    f"Luppi et al. (2023)'s emergence capacity as we read it, Ince's CCS synergy of the two pasts about the joint "
    f"future, is {m(ince_op, 4, True)} nats at the operating point and {desc_q('Ince EC')}, with {rates_of('Ince EC')} "
    f"there; at 840 samples its replicate mean at the operating point is {m(ince840[0], 4, True)} ± {m(ince840[1], 4)}. "
    f"Of the predictions recorded before the run (S19 Table), (a), that binarised MMI-sts and its emergence capacity "
    f"rise with r₁ at every step of the grid in the limit, was {VA}; (b), that at the operating point ∂(MMI-sts)/∂r₁ is "
    f"positive and the r₁ rate exceeds the |q| rate per standard deviation, was {VB}; and (c), that the replicate means "
    f"rise at every step at the three lengths, was {VC}. The CCS quantities carried no prediction.")
TABLE = ["**The long-series limit at q = 0.25** (nats; the other values of q, the finite lengths and the rates are in "
         "`notes/review_results/partB/binarised_tables.md`).", "",
         "| r₁ | MMI-sts | MMI emergence capacity | 2A | CCS-sts (published mask) | CCS emergence capacity | "
         "Luppi et al. (2023)'s emergence capacity | Gaussian-MMI sts |",
         "|---|---|---|---|---|---|---|---|"]
for r in R1:
    g_ = -math.log(1 - r * r) + 0.5 * math.log(1 - r * r * 0.0625)
    TABLE.append(f"| {r:.2f} | {m(lim('MMI sts', r, 0.25))} | {m(lim('MMI EC', r, 0.25))} | {m(lim('2A', r, 0.25))} | "
                 f"{m(lim('CCS-pub sts', r, 0.25), 4, True)} | {m(lim('CCS EC', r, 0.25), 4, True)} | "
                 f"{m(lim('Ince EC', r, 0.25), 4, True)} | {m(g_)} |")
S3_SECTION = "\n".join([
    "## 11. The binarised estimators on the family", "",
    "Two studies in S20 Table use binarised signals: Luppi et al. (2022) replicated their gradient from mean-binarised "
    "signals with the plug-in estimator (their pp. 3, 14), and the primary quantity of Luppi et al. (2023) is the "
    "emergence capacity of Ince's CCS decomposition on mean-binarised signals (their p. 12; S20 Table, row 2). B25 "
    "(`notes/partB25_binarised.py`; "
    "record, \"The binarised estimators on the AR(1) family (B25): pre-run entry\", with its predictions, and \"B25, "
    "outcome\") evaluates on the symmetric AR(1) family phyid's discrete path, which binarises each of x_t, y_t, x_{t+1} "
    "and y_{t+1} at its mean and takes plug-in probabilities, under MMI and under CCS, and Luppi et al. (2023)'s "
    "emergence capacity as we read their Methods: the synergy of the two pasts about the joint future, taken as one "
    "target, in Ince's decomposition, whose redundancy is evaluated on the maximum-entropy distribution that keeps the "
    "three pairwise marginals (Ince, 2017, Definition 2; his toolbox's code read, not run). At finite length each of the "
    "four lagged series is binarised at its own mean, as phyid does, where Luppi et al. binarise each signal once, a "
    "difference of order 1/T. The emergence capacity is str + stx + sty + sts, under MMI the whole-minus-max synergy. "
    "In the long-series limit the binarised probabilities are the orthant probabilities of the Gaussian family, "
    "computed by numerical quadrature to about 10⁻¹³; at 160, 300 and 840 samples, 1,000 replicate pairs per point of "
    "the grid r₁ 0.60–0.95 × q 0.10, 0.25, 0.50. Values in nats (bits × ln 2).", "",
    "Under MMI the lattice fixes the form before any computation. With A = I(x_t; x_{t+1}) of the binarised series, "
    "B = I(x_t; y_{t+1}), F = I(x_t; x_{t+1}, y_{t+1}) and T = I(x_t, y_t; x_{t+1}, y_{t+1}), binarised MMI-sts on the "
    "symmetric family in the long-series limit is T − 2F + 2A − B and its emergence capacity T − F, for 0 < q < 1, where "
    "B < A settles every MMI selection; the Gaussian atoms have F = A and T = 2A, which gives sts = 2S − C and "
    "emergence capacity S (main text, Results 1). At q = 0 binarised MMI-sts is exactly 2A, the two binarised "
    "self-informations, and its emergence capacity A = 1 − H₂(arccos(r₁)/π) bits.", "",
    RESULTS, ""] + TABLE) + "\n"
RATIO_CELL = (f"per-unit ratio {fmt_ratio(ratio_unit)}, per-SD ratio {fmt_ratio(ratio_sd)}" if dr1 > 0 else
              "∂/∂r₁ not positive")
S19_ROWS = [
    f"| B25 (a), binarised MMI in the long-series limit ({DATE_A}, {TIME_A} UTC) | Binarised MMI-sts and its emergence "
    f"capacity rise with r₁ at every step of the grid (r₁ 0.60–0.95 in steps of 0.05; q = 0.10, 0.25, 0.50): 42 steps "
    f"| {a_up} of 42 steps rise; at (0.85, 0.25) MMI-sts {m(sop)} (Gaussian {m(G_STS)}) | {VA} | S3 Text §11 |",
    f"| B25 (b), the rates at the operating point | ∂(MMI-sts)/∂r₁ positive and, per SD of the pairs' variation within "
    f"a window, above \\|∂(MMI-sts)/∂q\\| (a per-unit ratio above 6.89) | ∂/∂r₁ {m(dr1, 3, True)}, ∂/∂q "
    f"{m(dq, 3, True)}: {RATIO_CELL} | {VB} | S3 Text §11 |",
    f"| B25 (c), binarised MMI at 160, 300 and 840 samples | The replicate means of binarised MMI-sts and its emergence "
    f"capacity rise with r₁ at every step, q and length: 126 steps | {c_up} of 126 steps rise; MMI-sts "
    f"{m(min(bias), 4, True)} to {m(max(bias), 4, True)} from its limit | {VC} | S3 Text §11 |",
    f"| B25 (d), the CCS quantities and Luppi et al. (2023)'s emergence capacity | No prediction (descriptive), nor for "
    f"the sign of the finite-sample bias of MMI-sts | At (0.85, 0.25): CCS-sts {m(ccs_op, 4, True)} (published mask), "
    f"CCS emergence capacity {m(ccsec_op, 4, True)}, Luppi et al. (2023)'s {m(ince_op, 4, True)}, its "
    f"{rates_of('Ince EC')} | no prediction | S3 Text §11; S20 Table, row 2 |"]
S20_G = (f" On the symmetric family this estimator, as we read it (Ince's CCS on mean-binarised signals, the joint future "
         f"as one target), gives an emergence capacity of {m(ince_op, 4, True)} nats at (r₁, q) = (0.85, 0.25), which "
         f"{desc_q('Ince EC')}, with {rates_of('Ince EC', against=True)}")


def rr(id_, file, old, new, why):
    return {"id": id_, "file": file, "old": old, "new": new, "count": 1, "why": why}


OLD_COUNT_M = "of 53, 25 were met, 14 partly met, 14 missed and 0 could not be evaluated"
NEW_COUNT_M = f"of 56, {MET} were met, {PART} partly met, {MISS} missed and 0 could not be evaluated"
OLD_S19 = ("\n\nOf 53 recorded predictions, 25 were met, 14 partly met, 14 missed and 0 could not be evaluated. Six further "
           "entries recorded a reading rule or an outcome mapping without predicting which branch would obtain (B2, B6, "
           "B7, the two rules of 16 September 2026, 10:23 UTC, the cross-lag budget) or recorded no prediction (B18);")
NEW_S19 = ("\n" + "\n".join(S19_ROWS) + f"\n\nOf 56 recorded predictions, {MET} were met, {PART} partly met, {MISS} missed "
           "and 0 could not be evaluated. Six further entries recorded a reading rule or an outcome mapping without "
           "predicting which branch would obtain (B2, B6, B7, the two rules of 16 September 2026, 10:23 UTC, the "
           "cross-lag budget) or recorded no prediction (B18), and B25 recorded none for its CCS quantities (row B25 (d));")
S20_OLD = ("Primary quantity is discrete CCS on binarised data: outside the map, which is Gaussian-MMI (the CCS comparison "
           "(S3 Text §2) evaluated Gaussian CCS on continuous data, not this estimator). The Gaussian and the MMI "
           "validations are inside it")
LIT_OLD = ("Primary quantity is discrete CCS on binarised data: outside the map, which is Gaussian-MMI (B2 evaluated "
           "Gaussian CCS on continuous data, not this estimator). The Gaussian and the MMI validations are inside it")
IT = " The Gaussian and the MMI validations are inside it"
S3_TAIL = "while the AR(1)-substituted estimate from each pair's measured (a_x, a_y, q), in which |q| fell too, gives −0.0086 (main text, Table 1).\n"
S5_RUN = "(record, \"The final end-to-end run of `run_all.sh` at the final commit: outcome\")."
S5_COMMIT_OLD = ("the revision that followed the citation crosscheck of 28 September 2026 (its corrections; the licences, the "
                 "citation file, the diagnostic tool, the tests and the continuous-integration workflow; the pre-run entry "
                 "of B25, the binarised estimators on the family; and the correction for the matrices that are not positive "
                 "definite, with the pre-run entry of its run, B26) is the commit that follows, which cannot name its own "
                 "identifier (its parent is d108d66).")
S5_COMMIT_NEW = (f"{A} ({DATE_A.rsplit(' ', 1)[0]}, the revision that followed the citation crosscheck of 28 September 2026: "
                 f"its corrections; the licences, the citation file, the diagnostic tool, the tests and the "
                 f"continuous-integration workflow; the pre-run entry of B25; and the correction for the matrices that are "
                 f"not positive definite, with the pre-run entry of its run, B26; B25 was run at this commit); "
                 f"the outputs of B25, its outcome entry and the text that reports it are the commit that follows, which "
                 f"cannot name its own identifier (its parent is {A}).")
DCA_RUN = ("record, \"The final end-to-end run of `run_all.sh` at the final commit: the difference in the two CCS "
           "agreement-share arrays\"). The HRF-deconvolution items")
R = [
    rr("G01", S3, S3_TAIL, S3_TAIL + "\n" + S3_SECTION, "B25: S3 Text §11"),
    rr("G02", S3, "(B1–B24, B16b, B17b)", "(B1–B25, B16b, B17b)", "B25: the labels"),
    rr("G03", SUP, OLD_S19, NEW_S19, "B25: S19 Table's rows and its count"),
    rr("G04", SUP, "Labels B1–B24, B16b and B17b", "Labels B1–B25, B16b and B17b", "B25: the labels"),
    rr("G05", SUP, S20_OLD, S20_OLD.replace(IT, "") + S20_G + " (S3 Text §11). The Gaussian and the MMI validations are "
       "inside the map", "B25: S20 Table, row 2"),
    rr("G05L", LIT, LIT_OLD, LIT_OLD.replace(IT, "") + S20_G + " (B25). The Gaussian and the MMI validations are inside "
       "the map", "B25: the table S20 Table transcribes, row 2"),
    rr("G06", D, OLD_COUNT_M, NEW_COUNT_M, "B25: the count of predictions (Methods)"),
    rr("G07", D, "is outside the scope, and the main text of Tarchi",
       "is outside the scope (S3 Text evaluates it), and the main text of Tarchi", "B25: the Discussion's pointer"),
    rr("G08", D, "the calibration and remedy computations with their result files (`notes/partB14_*.py`–`partB24_*.py`,",
       "the calibration, remedy and binarised-estimator computations with their result files "
       "(`notes/partB14_*.py`–`partB25_*.py`,", "B25: Data and code availability"),
    rr("G09", D, DCA_RUN,
       DCA_RUN.replace(" The HRF-deconvolution items",
                       f" The computation of the binarised estimators on the family (S3 Text), which uses no data, was "
                       f"added to `run_all.sh` after that run; it was run at {A} in a session of the AI system. The "
                       f"HRF-deconvolution items"),
       "B25: Data and code availability"),
    rr("G10", D, "; manufacture and the lag variants; the literature details behind S20 Table.",
       "; manufacture and the lag variants; the literature details behind S20 Table; the binarised estimators on the "
       "family.", "B25: S3 Text's caption"),
    rr("G11", S5, S5_RUN,
       S5_RUN + f" B25 (S3 Text §11), which uses no data, was run on {long_date(RUN_DATE)} at {A} in a session of the AI "
       f"system ({WALL} s by its own count; {NCHECKS} checks, 0 failed; its three outputs carry `git={A}`, and its tables "
       f"the sha256 of `binarised.csv`); it was added to `run_all.sh` after the final run.",
       "B25: S5 Text §4"),
    rr("G12", S5, S5_COMMIT_OLD, S5_COMMIT_NEW, "B25: S5 Text §6"),
    rr("G13", "CLAUDE.md", "of 53, 25 met, 14 partly met, 14 missed, 0 not evaluable",
       f"of 56, {MET} met, {PART} partly met, {MISS} missed, 0 not evaluable", "bookkeeping"),
    rr("G14", "README.md", "B16b, B17b\nand B21–B24 have been run and their values are in the text,",
       "B16b, B17b,\nB21–B24 and B25 have been run and their values are in the text,", "bookkeeping"),
    rr("G15", "CLAUDE.md", "; next B25's run and outcome, its re-run by a separate session, B26's run on the data, then "
       "the typeset PDF and the note to C.T. and S.P.S.)",
       f"; B25 run at {A} and reported; next its re-run by a separate session, B26's run on the data, then the typeset "
       f"PDF and the note to C.T. and S.P.S.)", "bookkeeping"),
    rr("G16", "CLAUDE.md", "- Remaining work: B25's run at the revision's commit and its outcome (`b25_fill.py`), its "
       "re-run by a separate\n  session,",
       f"- Remaining work: B25's re-run at {A} by a separate session (B25 was run and reported in the commit that\n  "
       f"follows {A}),", "bookkeeping"),
]


# ------------------------------------------------------------------ apply
def apply(spec):
    path = ROOT / REVDIR / "text_replacements_2026-09-28_b25.json"
    path.write_text(json.dumps(spec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    p = subprocess.run([sys.executable, str(ROOT / "notes/review_2026-09-25/revision/apply_replacements.py"), str(ROOT),
                        str(path)], capture_output=True, text=True)
    print(p.stdout[-3000:])
    if p.returncode:
        path.unlink()
        sys.exit("NOTHING WRITTEN by the replacements: " + p.stdout[-500:] + p.stderr[-500:])


if STOPS:
    sys.exit("NOTHING WRITTEN: " + "; ".join(STOPS))
old_main = rd(D)
apply(R)

# ------------------------------------------------------------------ the numbers table
raw = rd(CSVF)
first, rest = raw.split("\n", 1)
rows = list(csv.reader(io.StringIO(rest)))
hdr, body = rows[0], rows[1:]
H = {k: i for i, k in enumerate(hdr)}
flat = lambda s: re.sub(r"\s*\n\s*", " ", s)
ob = [flat(b) for b in re.split(r"\n\s*\n", old_main)]
nb = [flat(b) for b in re.split(r"\n\s*\n", rd(D))]
if len(ob) != len(nb):
    stop("the main text's blocks changed in number")
count_line = next(i for i, l in enumerate(rd(SUP).split("\n"), 1) if l.startswith("Of 56 recorded predictions"))
anchor = next(l for l in rd(SUP).split("\n") if l.startswith("Of 56 recorded predictions")).split(". ")[0]
para = [r for r in body if r[H["section"]] == "Materials and methods / Pre-registration and deviations"]
cnt_rows = [r for r in para if r[H["source_file"]] == SUP]
if [r[H["number"]] for r in cnt_rows] != ["53", "25", "14", "14", "0"]:
    stop(f"the five count rows are not as expected: {[r[H['number']] for r in cnt_rows]}")
kb = [k for k, b in enumerate(nb) if NEW_COUNT_M in b]
if len(kb) != 1 or nb[kb[0]].count(NEW_COUNT_M) != 1:
    stop("the new count sentence is not found once in the main text")
blk = nb[kb[0]]
P0 = blk.find(NEW_COUNT_M)
nums = [(x.group(0), x.start()) for x in re.finditer(r"\d+", NEW_COUNT_M)]
for r, (num, off) in zip(cnt_rows, nums):
    r[H["number"]] = num
    r[H["locator"]] = f"line {count_line}; the line holds {num}; anchor: {anchor}"
    p = P0 + off
    r[H["context"]] = blk[max(0, p - 60):p + len(num) + 40]
seen = {}
for r in para:                                  # occurrences within the paragraph, in reading order
    seen[r[H["number"]]] = seen.get(r[H["number"]], 0) + 1
    r[H["occurrence"]] = str(seen[r[H["number"]]])
changed = [k for k in range(len(ob)) if ob[k] != nb[k]]
nctx = len(cnt_rows)
for k in changed:
    o, n = ob[k], nb[k]
    opc = difflib.SequenceMatcher(None, o, n, autojunk=False).get_opcodes()

    def mp(p):
        for tag, i1, i2, j1, j2 in opc:
            if i1 <= p < i2:
                return j1 + (p - i1) if tag == "equal" else None
        return None
    for r in body:
        c, num = r[H["context"]], r[H["number"]]
        if r in cnt_rows or not c or c not in o or c in n:
            continue
        offs = [x.start() for x in re.finditer(re.escape(num), c)]
        if o.count(c) != 1 or not offs:
            stop(f"row {num!r} ({r[H['paragraph']]}): its context is not found once in its block")
            continue
        off = min(offs, key=lambda x: abs(x - 60))
        p1 = mp(o.find(c) + off)
        if p1 is None or n[p1:p1 + len(num)] != num:
            stop(f"row {num!r} ({r[H['paragraph']]}) not found again after the edit")
            continue
        r[H["context"]] = n[max(0, p1 - off):p1 - off + len(c)]
        nctx += 1
out = io.StringIO()
csv.writer(out, lineterminator="\r\n").writerows([hdr] + body)
first_new = (first + f" The text that reports B25 ({long_date(NOW.rsplit(' ', 1)[0])}) changed the five rows of S19 "
             f"Table's count (56 predictions: {MET} met, {PART} partly met, {MISS} missed) and recomputed the context of "
             f"the rows whose context its edits reached ({nctx}).")
wr(CSVF, first_new + "\n" + out.getvalue())

# ------------------------------------------------------------------ the outcome entry
entry = f"""
## B25, outcome, {NOW} UTC (appended; nothing above edited)

Run in the writer's session at {A}, the commit of the pre-run entry, on {RUN_DATE}, with the command of the script's
docstring ({WALL} s by its own count; {NCHECKS} checks, 0 failed; {ENV}); the three outputs,
`notes/review_results/partB/binarised_tables.md`, `binarised.csv` and `binarised_run.log`, carry `git={A}`, and the
tables give the sha256 of `binarised.csv`, which `notes/review_2026-09-28/revision/b25_fill.py` recomputed. A separate
session re-runs B25 at {A}; the commit that follows its re-run records the result. The text below and every sentence
that reports B25 were written by `b25_fill.py`, fixed with the pre-run entry.

**The facts the predictions read.** (a) {a_up} of the 42 steps rise in the limit: MMI-sts {desc_q('MMI sts')}; its
emergence capacity {desc_q('MMI EC')}. (b) At (0.85, 0.25) ∂(MMI-sts)/∂r₁ = {m(dr1, 4, True)} and ∂(MMI-sts)/∂q =
{m(dq, 4, True)} nats per unit: a per-unit ratio of {fmt_ratio(ratio_unit)} and a per-SD ratio of {fmt_ratio(ratio_sd)}
(the threshold 1, a per-unit ratio of 6.89). (c) {c_up} of the 126 steps of the replicate means rise.

**Verdicts.** (a) {VA}; (b) {VB}; (c) {VC}; (d) no prediction. With them S19 Table counts 56 recorded predictions:
{MET} met, {PART} partly met, {MISS} missed, 0 not evaluable.

**Values the text quotes.** Binarised MMI-sts at (0.85, 0.25) {m(sop)} nats (Gaussian {m(G_STS)}), 2A {m(aop)}, its
emergence capacity {m(eop)} (Gaussian S = {m(S_OP)}); at q = 0.25 MMI-sts {m(lim('MMI sts', 0.6, 0.25))} at r₁ = 0.60
and {m(lim('MMI sts', 0.95, 0.25))} at 0.95; the finite-sample differences of MMI-sts from its limit
{m(min(bias), 4, True)} to {m(max(bias), 4, True)} ({m(min(bias840), 4, True)} to {m(max(bias840), 4, True)} at 840
samples). CCS through phyid's discrete path at (0.85, 0.25): sts {m(ccs_op, 4, True)} (published mask),
{m(ccs_code_op, 4, True)} (phyid's); sts under the published mask {desc_q('CCS-pub sts')}; the emergence capacity
{m(ccsec_op, 4, True)}, which {desc_q('CCS EC')}. Luppi et al. (2023)'s emergence capacity {m(ince_op, 4, True)}, which
{desc_q('Ince EC')}, {rates_of('Ince EC', 4)}; at 840 samples {m(ince840[0], 4, True)} ± {m(ince840[1], 4)}.

**Where it is reported.** S3 Text §11 (new; the limit at q = 0.25 as a table); S19 Table, rows B25 (a)–(d) and its
count; Methods, Pre-registration and deviations (the count); S20 Table row 2 and `notes/partB5_literature_v2.md` (Luppi
et al. 2023's estimator on the family); the Discussion's pointer to S3 Text; S3 Text's caption and the labels B1–B25;
Data and code availability and S5 Text §4 and §6 (the run and the commits); `main_text_numbers.csv` (the count's five
rows; the contexts of {nctx} rows); `CLAUDE.md` and `README.md`. The replacements:
`notes/review_2026-09-28/revision/text_replacements_2026-09-28_b25.json`.
"""
rec = rd(REC)
wr(REC, rec + entry)

# ------------------------------------------------------------------ checks
CH = "notes/review_2026-09-25/checks"
cn = subprocess.run([sys.executable, str(ROOT / CH / "check_numbers.py"), str(ROOT)], capture_output=True, text=True).stdout
cc = subprocess.run([sys.executable, str(ROOT / CH / "check_cells.py"), str(ROOT)], capture_output=True, text=True).stdout
texts = [D, SUP] + [f"manuscript/si/S{i}_Text.md" for i in range(1, 6)]
tc = subprocess.run([sys.executable, str(ROOT / CH / "tablecheck.py")] + texts, capture_output=True, text=True,
                    cwd=str(ROOT)).stdout
wc = subprocess.run([sys.executable, str(ROOT / CH / "wc.py"), str(ROOT / D)], capture_output=True, text=True).stdout
print(cn.splitlines()[0], "|", cc.strip().splitlines()[-1], "|", tc.strip().splitlines()[-1], "|", wc.strip().splitlines()[-1])
if not cn.splitlines()[0].endswith("flagged 12"):
    stop("check_numbers does not flag exactly the twelve known rows")
if cc.strip().splitlines()[-1] != "flagged 0":
    stop("check_cells flags a row")
if not tc.strip().endswith("rows with a wrong cell count: 0"):
    stop("a table row has a wrong cell count")
wtot = int(re.search(r"total with headings (\d+)", wc).group(1))
if wtot > 7000:
    stop(f"Introduction through Methods {wtot} words with headings, above 7,000")
lab = []
for t in texts + ["manuscript/figures/captions_v2.md"]:
    for i, l in enumerate(rd(t).split("\n"), 1):
        for x in re.finditer(r"\b(?:[Rr]ound \d+|[Ss]tage [AB]\b|bundle \d+|[Pp]lanner|writer's (?:session|clone))", l):
            if not (t.endswith("S5_Text.md") and "call them the writer's session and the planning session" in l):
                lab.append(f"{t}:{i}")
if lab:
    stop(f"a process label in the manuscript files: {lab[:3]}")
if re.search(r"\bB\d", rd(D).split("## References")[0]):
    stop("a computation label in the main text")
left = [t for t in texts + [REC, CSVF] if re.search(r"«[^»]*»", rd(t))]
if left:
    stop(f"a placeholder is left in {left}")
print(f"verdicts: (a) {VA}, (b) {VB}, (c) {VC}; counts {MET} / {PART} / {MISS}; Introduction through Methods {wtot} words")
print("READY" if not STOPS else f"NOT READY: {len(STOPS)} stops")
