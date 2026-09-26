"""9_wrapper_compare.py — the two outputs of notes/partB21_inference_revision.py (B21) whose regeneration at the final
commit differs from the committed files in ways fixed before the run (record, "The final end-to-end run of
`run_all.sh` at the final commit: pre-run entry", item 6 (a) and (b)).

Usage (from the repository root, pinned environment, on the working tree the run left, before anything is added,
restored or committed):
    .venv/bin/python notes/planning_checks_2026-09-16/reproduction_checks/9_wrapper_compare.py <run commit>

1. notes/review_results/partB/inference_revision.csv. The committed file (git=a9d9ca4) writes a number that NumPy
   returned as a scalar as `np.float64(<value>)`; the writer was changed on 23 September 2026 to write the plain
   value (record, "B21, outcome"). After that wrapper is stripped from the committed text, the two files must have
   the same columns and the same rows in the same order; every numeric cell within 1e-9 with the same empty cells;
   every other cell identical — except `quoted_at`, which B21 computes from the manuscript text in the working tree
   (the script's lines 97–120). That column is checked against the texts at <run commit> instead: recomputed here
   with B21's rule from each row's committed mean and committed percentile interval, it must equal the regenerated
   column in every row.
2. notes/review_results/partB/inference_revision_tables.md. Identical to the committed version apart from the git=
   lines and the parts that follow from `quoted_at`: the count in "(a) Summary" ("N of them matched to an interval
   quoted in ..."), which must equal the number of non-empty `quoted_at` cells of the regenerated CSV, and the table
   "(a) Quantities quoted in the text, ...", whose rows must be exactly those B21 writes from the regenerated CSV:
   every row that is not a pickle row, and the pickle rows with a non-empty `quoted_at`, each formatted as B21 formats
   it. The same formatting is first checked against the committed table and the committed CSV.
Nothing is written or changed. Prints the verdict of each part and PASS only if both hold.
"""
import csv
import io
import math
import re
import subprocess
import sys
from pathlib import Path

REF = sys.argv[1]
CSV_P, MD_P = "notes/review_results/partB/inference_revision.csv", "notes/review_results/partB/inference_revision_tables.md"
TEXT_FILES = ["manuscript/draft_v2.md", "manuscript/supplementary.md"]
SHA = re.compile(r"\bgit[= ]([0-9a-f]{7,40}(?:-dirty)?)")
show = lambda p: subprocess.run(["git", "show", f"{REF}:{p}"], capture_output=True, text=True, check=True).stdout
ok_all = True


def parse_csv(text):
    rows = list(csv.reader(io.StringIO("\n".join(l for l in text.split("\n") if not l.startswith("#")))))
    return rows[0], rows[1:]


def num(s):
    try:
        return float(s)
    except ValueError:
        return None


# ------------------------------------------------------------------------------------------------ 1. the CSV
old_hdr, old = parse_csv(re.sub(r"np\.float64\(([^()]*)\)", r"\1", show(CSV_P)))
new_hdr, new = parse_csv(Path(CSV_P).read_text(encoding="utf-8"))
problems = []
if old_hdr != new_hdr:
    problems.append(f"columns differ: {old_hdr} / {new_hdr}")
if len(old) != len(new):
    problems.append(f"row count {len(old)} committed, {len(new)} regenerated")
C = {c: i for i, c in enumerate(new_hdr)}
worst, changed_q = 0.0, 0
if not problems:
    for k, (o, n) in enumerate(zip(old, new)):
        for c, i in C.items():
            if c == "quoted_at":
                changed_q += o[i] != n[i]
                continue
            a, b = num(o[i]), num(n[i])
            if a is not None and b is not None:
                if math.isnan(a) != math.isnan(b) or (not math.isnan(a) and abs(a - b) > 1e-9):
                    problems.append(f"row {k + 1} ({n[C['label']]} / {n[C['set']]} / {n[C['field']]}) {c}: {o[i]} vs {n[i]}")
                elif not math.isnan(a):
                    worst = max(worst, abs(a - b))
            elif o[i] != n[i]:
                problems.append(f"row {k + 1} ({n[C['label']]} / {n[C['set']]} / {n[C['field']]}) {c}: {o[i]!r} vs {n[i]!r}")

# quoted_at recomputed from the texts at the run commit with B21's rule (partB21_inference_revision.py, lines 97–120)
texts = TEXT_FILES + sorted(p for p in subprocess.run(["git", "ls-tree", "--name-only", REF, "manuscript/si/"],
                                                       capture_output=True, text=True, check=True).stdout.split()
                            if re.fullmatch(r"manuscript/si/S[^/]*_Text\.md", p))
PAT = re.compile(r"([+−-]?\d+\.\d+)\s*\[([+−-]?\d+\.\d+),\s*([+−-]?\d+\.\d+)\]")
QUOTED = {}
for f in texts:
    for i, line in enumerate(show(f).split("\n"), 1):
        for m in PAT.finditer(line):
            nd = len(m.group(1).split(".")[1])
            QUOTED.setdefault((nd,) + tuple(round(float(g.replace("−", "-")), nd) for g in m.groups()), []).append(f"{Path(f).name}:{i}")


def quoted_at(mean, lo, hi):
    if any(v is None or math.isnan(v) or math.isinf(v) for v in (mean, lo, hi)):
        return ""
    locs = []
    for nd in (5, 4, 3):
        locs += QUOTED.get((nd, round(mean, nd), round(lo, nd), round(hi, nd)), [])
    return ";".join(sorted(set(locs)))


q_bad = 0
for k, n in enumerate(new):
    expect = quoted_at(num(n[C["committed_mean"]]), num(n[C["pct_lo"]]), num(n[C["pct_hi"]]))
    if expect != n[C["quoted_at"]]:
        q_bad += 1
        if q_bad <= 5:
            problems.append(f"row {k + 1} quoted_at {n[C['quoted_at']]!r}, expected from the texts at {REF}: {expect!r}")
if q_bad > 5:
    problems.append(f"... {q_bad} rows in all whose quoted_at differs from the texts at {REF}")
n_quoted = sum(1 for n in new if n[C["quoted_at"]])
print(f"1. {CSV_P}: {len(new)} rows, {len(new_hdr)} columns; largest numeric difference {worst:.3g}; "
      f"quoted_at changed in {changed_q} rows, non-empty in {n_quoted} (committed: {sum(1 for o in old if o[C['quoted_at']])}); "
      f"quoted_at rows not matching the texts at {REF}: {q_bad}")
for p in problems[:20]:
    print("   ", p)
print("   verdict:", "PASS" if not problems else "FAIL")
ok_all &= not problems

# ------------------------------------------------------------------------------------------------ 2. the tables file
f5 = lambda v: "—" if v is None or not math.isfinite(v) else f"{v:+.5f}"
ci = lambda lo, hi: "—" if lo is None or hi is None or not (math.isfinite(lo) and math.isfinite(hi)) else f"[{lo:+.5f}, {hi:+.5f}]"


def fmt(r):
    """One row of table (a), as partB21_inference_revision.py writes it (its lines 637–641)."""
    g = lambda c: r[C[c]]
    w = num(g("width_ratio"))
    wtxt = "—" if w is None or not math.isfinite(w) else f"{w:.3f}"
    return (f"| {g('group')} | {g('label')} | {g('set')} / {g('field')} | {f5(num(g('mean')))} | {num(g('p_exact')):.4f} | "
            f"{ci(num(g('pct_lo')), num(g('pct_hi')))} | {ci(num(g('inv_lo')), num(g('inv_hi')))} | {ci(num(g('t_lo')), num(g('t_hi')))} | "
            f"{wtxt} | {g('zero_in_pct') or '—'} / {g('zero_in_inv')} / {g('zero_in_t')} | {g('n_neg')} | {g('quoted_at') or '—'} | {g('check') or '—'} |")


def table_a(rows):
    return [fmt(r) for r in rows if not (r[C["group"]] == "pickle" and not r[C["quoted_at"]])]


def split(md):
    L = md.split("\n")
    s = next(i for i, l in enumerate(L) if l.startswith("## (a) Quantities quoted in the text"))
    a = s + 4                                              # heading, blank line, header row, separator
    b = a
    while b < len(L) and L[b].startswith("| "):
        b += 1
    return L[:a], L[a:b], L[b:]


COUNT = re.compile(r"; (\d+) of them matched to an interval quoted in draft_v2\.md, S1–S5 Text or supplementary\.md\.")
old_md, new_md = show(MD_P), Path(MD_P).read_text(encoding="utf-8")
(oh, ot, of), (nh, nt, nf) = split(old_md), split(new_md)
problems = []
if ot != table_a(old):
    bad = sum(1 for x, y in zip(ot, table_a(old)) if x != y) + abs(len(ot) - len(table_a(old)))
    problems.append(f"this check's formatting does not reproduce the committed table (a) from the committed CSV ({bad} rows)")
if nt != table_a(new):
    bad = sum(1 for x, y in zip(nt, table_a(new)) if x != y) + abs(len(nt) - len(table_a(new)))
    problems.append(f"the regenerated table (a) is not the table B21 writes from the regenerated CSV ({bad} rows)")
mask = lambda lines: [COUNT.sub("; N of them matched ...", SHA.sub("git=SHA", l)) for l in lines]
if mask(oh) != mask(nh) or mask(of) != mask(nf):
    diff = [(x, y) for x, y in zip(mask(oh) + mask(of), mask(nh) + mask(nf)) if x != y]
    problems.append(f"lines outside table (a) differ beyond the git= lines and the count: {len(diff)}"
                    + (f"; the first: {diff[0][0][:100]!r} / {diff[0][1][:100]!r}" if diff else "; line counts differ"))
m_new = [int(m.group(1)) for l in nh for m in [COUNT.search(l)] if m]
if m_new != [n_quoted]:
    problems.append(f"the count in (a) Summary is {m_new}, the regenerated CSV has {n_quoted} non-empty quoted_at cells")
print(f"2. {MD_P}: table (a) {len(ot)} rows committed, {len(nt)} regenerated (pickle rows {sum(1 for l in ot if l.startswith('| pickle |'))} → "
      f"{sum(1 for l in nt if l.startswith('| pickle |'))}); matched count {[int(m.group(1)) for l in oh for m in [COUNT.search(l)] if m]} → {m_new}")
for p in problems:
    print("   ", p)
print("   verdict:", "PASS" if not problems else "FAIL")
ok_all &= not problems
print("9_wrapper_compare:", "PASS" if ok_all else "FAIL")
