# Reproduction check of the single full run of run_all.sh at d51966e, run after its outputs were
# committed: every regenerated .md/.csv/.txt file is compared between the commit before the outputs
# commit (argv[1], default cc59a74, whose outputs are those of d51966e) and the working tree, which
# is the outputs as committed. Prints only what did not reproduce exactly. Run from the repository root.
import collections, difflib, io, re, subprocess, sys
import numpy as np, pandas as pd

OLD = sys.argv[1] if len(sys.argv) > 1 else "cc59a74"
sh = lambda *a: subprocess.run(a, capture_output=True, text=True).stdout
at_old = lambda f: sh("git", "show", OLD + ":" + f)
SHA = re.compile(r"\bgit[= ]([0-9a-f]{7,40}(?:-dirty)?)")
ZERO = re.compile(r"(?:^|(?<=[^\d.]))[-+−](0\.0+)(?=\D|$)")

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
    mx = float(np.nanmax(d)) if d.size else 0.0
    cells = int((d > 1e-9).sum())
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

sha_only, zero_only, changed = [], [], []
for f in txts:
    d = [l for l in difflib.unified_diff(at_old(f).splitlines(), open(f, encoding="utf-8", errors="replace").read().splitlines(),
                                         lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---") and not SHA.search(l)]
    rem = collections.Counter(ZERO.sub(r"\1", l[1:]) for l in d if l[0] == "-")
    add = collections.Counter(ZERO.sub(r"\1", l[1:]) for l in d if l[0] == "+")
    (sha_only if not d else zero_only if rem == add else changed).append((f, d))
print(f"text files changed only on git-SHA lines: {len(sha_only)}; there and in the sign of a printed zero: {len(zero_only)}"
      + (f" ({', '.join(p.split('/')[-1] for p, _ in zero_only)})" if zero_only else ""))
print(f"text files with other changes: {len(changed)}")
for p, d in changed:
    print(f"    {p} ({len(d)} changed lines besides SHA lines)")
    for l in d[:6]: print("       ", l[:170])

heads = collections.Counter()
for f in files:
    first = "\n".join(open(f, encoding="utf-8", errors="replace").read().splitlines()[:3])
    heads.update(set(SHA.findall(first)) or {"no SHA in the first three lines"})
print("SHA in the headers of the regenerated files:", dict(heads))
other = [f for f in sh("git", "diff", "--name-only", OLD).split() if not f.endswith((".csv", ".md", ".txt"))]
print("other files changed by the run, by extension:", dict(collections.Counter(f.rsplit(".", 1)[-1] for f in other)))
unt = [l[3:].strip('"') for l in sh("git", "status", "--porcelain", "--untracked-files=all").splitlines() if l.startswith("??")]
unt = [u for u in unt if u.startswith(("results/", "notes/review_results/", "manuscript/figures/"))]
print(f"untracked files under the output folders: {len(unt)}")
for u in unt: print("   ", u)
