"""6_committed_compare.py — the .md, .csv and .txt outputs of a run of run_all.sh against their committed versions.

Usage (from the repository root, pinned environment, on the working tree the run left, before anything is added,
restored or committed):
    .venv/bin/python notes/planning_checks_2026-09-16/reproduction_checks/6_committed_compare.py <reference commit>

Every .md, .csv and .txt file that differs between the reference commit and the working tree is compared with its
committed version. CSVs are parsed (comment lines skipped) and compared cell by cell, in order: numbers within 1e-9,
the same empty cells, the same text cells, the same rows and columns. Text files are compared line by line, in order,
after the lines that carry a git SHA are set aside: two lines agree when they are identical once every number in them
is replaced by a placeholder and each pair of numbers differs by at most 1e-9 (so that a printed zero may change its
sign and a printed float-noise value, such as the difference between two computations of the same quantity that some
checks print below 1e-13, may change, as a CSV cell may); every committed line must be reproduced, in order, and no
line added. A change of line endings (CRLF, lone CR, lone LF, a final newline) is reported for every file. Prints what
did not reproduce exactly (for a text file, the counts of committed lines not reproduced and of lines added, and up
to ten of each), the SHAs in the files' first three lines, the other files the run changed, and the untracked files
under the output folders. Nothing is written or changed.

History: written on 16 Sep 2026 for the reproduction check of the run at d51966e; revised on 25 Sep 2026 for the
final run (record, "The final end-to-end run of `run_all.sh` at the final commit: pre-run entry"): the text files,
until then compared as unordered sets of changed lines with only the sign of a printed zero set aside, are compared
in order with the 1e-9 rule for printed numbers, and line endings are compared.
"""
import collections, difflib, io, re, subprocess, sys
import numpy as np, pandas as pd

OLD = sys.argv[1] if len(sys.argv) > 1 else "cc59a74"
sh = lambda *a: subprocess.run(a, capture_output=True, text=True).stdout
at_old = lambda f: sh("git", "show", OLD + ":" + f)
at_old_bytes = lambda f: subprocess.run(["git", "show", OLD + ":" + f], capture_output=True).stdout
SHA = re.compile(r"\bgit[= ]([0-9a-f]{7,40}(?:-dirty)?)")
NUM = re.compile(r"(?<![\w.])[-+−]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+−]?\d+)?(?!\w)(?!\.\d)")
TOL = 1e-9


def split(line):
    """(the line with every number replaced by a NUL placeholder, the numbers)"""
    nums = []

    def rep(m):
        nums.append(float(m.group(0).replace("−", "-")))
        return "\0"
    return NUM.sub(rep, line), nums


def agree(a, b):
    (sa, na), (sb, nb) = split(a), split(b)
    return sa == sb and all(abs(x - y) <= TOL for x, y in zip(na, nb))


def canon(line):
    """The form in which lines are aligned: every number rounded to six decimals. Alignment only pairs lines; whether
    an aligned pair reproduces is decided by agree(), for every pair."""
    s, nums = split(line)
    it = iter(f"{round(x, 6) + 0.0:.6f}" for x in nums)
    return re.sub("\0", lambda m: next(it), s)


def align(old, new):
    """(the committed lines not reproduced, the regenerated lines that match no committed line). The lines are aligned
    in order on their canonical form; an aligned pair counts only if its two lines agree; within a changed block each
    committed line is matched, in order, to the first regenerated line of the block that agrees with it."""
    missing, added = [], []
    sm = difflib.SequenceMatcher(None, [canon(l) for l in old], [canon(l) for l in new], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for a, b in zip(old[i1:i2], new[j1:j2]):
                if not agree(a, b):
                    missing.append(a)
                    added.append(b)
            continue
        b, k = new[j1:j2], 0
        for x in old[i1:i2]:
            m = next((j for j in range(k, len(b)) if agree(x, b[j])), None)
            if m is None:
                missing.append(x)
            else:
                added += b[k:m]
                k = m + 1
        added += b[k:]
    return missing, added


def eol_style(data):
    """Which line endings a file uses (CRLF, a lone CR, a lone LF) and whether it ends with one."""
    return (b"\r\n" in data, re.search(rb"\r(?!\n)", data) is not None, re.search(rb"(?<!\r)\n", data) is not None,
            data.endswith((b"\n", b"\r")))


files = sh("git", "diff", "--name-only", OLD, "--", "*.md", "*.csv", "*.txt").split()
csvs = [f for f in files if f.endswith(".csv")]
txts = [f for f in files if not f.endswith(".csv")]
print(f"compared against {OLD}: {len(files)} files ({len(csvs)} CSV, {len(txts)} text)")


def only_in(a, b):
    m = a.merge(b.drop_duplicates(), how="left", indicator=True)
    return m[m["_merge"] == "left_only"]


exact, noise, real, shape, unread = [], [], [], [], []
for f in csvs:
    try:
        o = pd.read_csv(io.StringIO(at_old(f)), comment="#"); n = pd.read_csv(f, comment="#")
    except Exception as e:
        unread.append(f"{f}: {e}"); continue
    if o.shape != n.shape or list(o.columns) != list(n.columns):
        added, missing = only_in(n, o), only_in(o, n)
        by = {k: int(v) for k, v in added["condition"].value_counts().items()} if "condition" in added else {}
        shape.append(f"{f}: old {o.shape} new {n.shape}; rows in new not in old {len(added)}" + (f" {by}" if by else "")
                     + f"; old rows absent or changed in new {len(missing)}"
                     + ("" if list(o.columns) == list(n.columns) else "; columns differ"))
        continue
    num = o.select_dtypes(include=[np.number]).columns.intersection(n.select_dtypes(include=[np.number]).columns)
    d = (o[num] - n[num]).abs().values
    mx = float(np.nanmax(d)) if d.size and not np.isnan(d).all() else 0.0
    cells = int((d > TOL).sum())
    empty = int((o[num].isna().values != n[num].isna().values).sum())
    tcols = {c: int((o[c].astype(object).where(o[c].notna(), "").astype(str)
                     != n[c].astype(object).where(n[c].notna(), "").astype(str)).sum()) for c in o.columns if c not in num}
    tcols = {c: k for c, k in tcols.items() if k}
    row = f"{f}: max {mx:.3g}, {cells} numbers > 1e-9, {empty} empty-cell changes, text cells {tcols or 0}"
    if cells or empty or tcols: real.append((mx, row))
    elif mx == 0.0: exact.append(f)
    else: noise.append((mx, f))
print(f"CSV identical in every cell: {len(exact)}")
print(f"CSV differing only by less than 1e-9: {len(noise)}" + (f"; largest {max(noise)[0]:.3g} ({max(noise)[1]})" if noise else ""))
print(f"CSV with a real difference: {len(real)}")
for mx, row in sorted(real, reverse=True): print("   ", row)
print(f"CSV whose rows or columns changed: {len(shape)}")
for s in shape: print("   ", s)
if unread:
    print(f"CSV that could not be parsed: {len(unread)}")
    for u in unread: print("   ", u)

sha_only, num_only, changed = [], [], []
for f in txts:
    old = [l for l in at_old(f).splitlines() if not SHA.search(l)]
    new = [l for l in open(f, encoding="utf-8", errors="replace").read().splitlines() if not SHA.search(l)]
    if old == new:
        sha_only.append(f); continue
    missing, added = align(old, new)
    if not missing and not added:
        num_only.append((f, sum(1 for a, b in zip(old, new) if a != b)))
    else:
        changed.append((f, missing, added))
print(f"text files changed only on git-SHA lines: {len(sha_only)}; there and in printed numbers within 1e-9: {len(num_only)}"
      + (f" ({', '.join(p.split('/')[-1] + f': {k} line(s)' for p, k in num_only)})" if num_only else ""))
print(f"text files with other changes: {len(changed)}")
for p, missing, added in changed:
    print(f"    {p} ({len(missing)} committed line(s) not reproduced, {len(added)} line(s) added, besides SHA lines; up to ten of each)")
    for a in missing[:10]: print("        -", a[:170])
    for b in added[:10]: print("        +", b[:170])

eol = [f for f in files if eol_style(at_old_bytes(f)) != eol_style(open(f, "rb").read())]
print(f"files whose line endings changed: {len(eol)}")
for f in eol: print("   ", f)

heads = collections.Counter()
for f in files:
    first = "\n".join(open(f, encoding="utf-8", errors="replace").read().splitlines()[:3])
    heads.update(set(SHA.findall(first)) or {"no SHA in the first three lines"})
print("SHA in the headers of the regenerated files:", dict(heads))
nosha = [f for f in files if not SHA.search("\n".join(open(f, encoding="utf-8", errors="replace").read().splitlines()[:3]))]
for f in nosha: print("    no SHA:", f)
other = [f for f in sh("git", "diff", "--name-only", OLD).split() if not f.endswith((".csv", ".md", ".txt"))]
print("other files changed by the run, by extension:", dict(collections.Counter(f.rsplit(".", 1)[-1] for f in other)))
unt = [l[3:].strip('"') for l in sh("git", "status", "--porcelain", "--untracked-files=all").splitlines() if l.startswith("??")]
unt = [u for u in unt if u.startswith(("results/", "notes/review_results/", "manuscript/figures/"))]
print(f"untracked files under the output folders: {len(unt)}")
for u in unt: print("   ", u)
