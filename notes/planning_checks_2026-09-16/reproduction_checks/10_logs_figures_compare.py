"""10_logs_figures_compare.py — the outputs of a run that 6_committed_compare.py and 8_binary_compare.py do not
read: the tracked logs (.log) under results/ and notes/review_results/, and the images (.png, .pdf) under
manuscript/figures/, results/ and notes/review_results/ (the paper's six figures, the three figures of the first
draft, and the scope map of notes/review_results/partB/), each against its committed version at a reference commit.

Usage (from the repository root, pinned environment, on the working tree the run left, before anything is added,
restored or committed):
    .venv/bin/python notes/planning_checks_2026-09-16/reproduction_checks/10_logs_figures_compare.py <run commit>

Logs: a log is a capture of a step's standard output and error, and the question asked of it is whether the run
reproduced everything the committed log reports. The parts that legitimately change between runs are masked — git
SHAs (with -dirty), dates and clock times, elapsed times and rates ("(172s)", "12.3 s", "4 min", "0.8 ms/pair",
"compute finished in 531.7s (2.9 ms/pair)"), absolute paths, and the count of B21's quoted intervals ("N of them
matched to an interval quoted in ...", which 9_wrapper_compare.py checks) — and blank lines are set aside; then every
committed line must be found, in order, in the regenerated log, where a line is found if a regenerated line agrees
with it: identical once every number in both is replaced by a placeholder, each pair of numbers within 1e-9 (so that
a printed zero may change its sign and a printed float-noise value may change, as in 6_committed_compare.py). Every
committed line not found is printed in full, and so is every regenerated line that matches no committed line (an
added line), for the outcome entry to examine and explain one by one. A change of line endings (CRLF, lone CR, lone
LF, a final newline) is reported.
Figures: a PNG is compared with its committed version byte for byte and, if it differs, pixel by pixel: the
number of differing pixels and the largest channel difference (0–255) are printed, and a difference of at most 2
is reported as "anti-aliasing only" (the trace a sub-1e-9 change of a plotted value leaves: it moves an edge by far
less than a pixel). A PDF is compared byte for byte once its /CreationDate and /ModDate entries are removed; a PDF
that still differs takes the verdict of its PNG, since both are drawn from the same figure: "anti-aliasing" if the
PNG is identical or differs by anti-aliasing only (a coordinate written to the PDF can change in its last digit
without moving a pixel), "differs" otherwise.
Nothing is written or changed.
"""
import collections
import difflib
import io
import re
import subprocess
import sys

REF = sys.argv[1]
git = lambda *a: subprocess.run(["git", *a], capture_output=True, check=True).stdout
MASKS = [
    (re.compile(r"\bgit[= ][0-9a-f]{7,40}(?:-dirty)?"), "git=SHA"),
    (re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?"), "DATETIME"),
    (re.compile(r"\b\d{1,2}:\d{2}:\d{2}(?:\.\d+)?\b"), "TIME"),
    # a number with a unit of time, unless an "=" follows ("s=(0.5, 0.5)") or a "(" that opens a word ("0.5 min(S_x,
    # S_y)", "TR 2 s (this ...)"); "531.7s (2.9 ms/pair)" is masked
    (re.compile(r"\b\d+(?:\.\d+)?\s?(?:ms/pair|ms|s|sec|secs|seconds|min|minutes|h)\b(?!\s*=)(?!\s*\((?!\d))"), "DUR"),
    (re.compile(r"(?:/home|/root|/tmp|/Users|/mnt|/media)/\S*"), "PATH"),
    (re.compile(r"; \d+ of them matched to an interval quoted in"), "; N of them matched to an interval quoted in"),
]
NUM = re.compile(r"(?<![\w.])[-+−]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+−]?\d+)?(?!\w)(?!\.\d)")
TOL = 1e-9


def mask(line):
    for pat, rep in MASKS:
        line = pat.sub(rep, line)
    return line


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


def compare_log(old, new):
    """Blank lines set aside, (the committed lines not reproduced, in order, by the regenerated log; the regenerated
    lines that match no committed line)."""
    return align([l for l in old if l.strip()], [l for l in new if l.strip()])


changed = [l[3:].strip('"') for l in git("status", "--porcelain", "--untracked-files=no").decode().splitlines()
           if l[:2].strip() in ("M", "MM", "AM")]
logs = sorted(p for p in changed if p.endswith(".log") and p.startswith(("results/", "notes/review_results/")))
figs = sorted(p for p in changed if p.startswith(("manuscript/figures/", "results/", "notes/review_results/")) and p.endswith((".png", ".pdf")))

reproduced, missing_any, added_only, eol = 0, [], [], []
for p in logs:
    old_b, new_b = git("show", f"{REF}:{p}"), open(p, "rb").read()
    if eol_style(old_b) != eol_style(new_b):
        eol.append(p)
    old = [mask(l) for l in old_b.decode("utf-8", "replace").splitlines()]
    new = [mask(l) for l in new_b.decode("utf-8", "replace").splitlines()]
    missing, added = compare_log(old, new)
    if missing:
        missing_any.append((p, missing, added))
    else:
        reproduced += 1
        if added:
            added_only.append((p, added))
print(f"logs modified by the run: {len(logs)}; every committed line reproduced: {reproduced}"
      f" ({len(added_only)} of them with added lines); with committed lines not reproduced: {len(missing_any)}")
for p, missing, added in missing_any:
    print(f"    {p}: {len(missing)} committed line(s) not reproduced, {len(added)} line(s) added")
    for a in missing: print(f"        - {a}")
    for b in added: print(f"        + {b}")
for p, added in added_only:
    print(f"    {p}: every committed line reproduced; {len(added)} line(s) added")
    for b in added: print(f"        + {b}")
if eol:
    print(f"logs whose line endings changed: {len(eol)}")
    for p in eol: print(f"    {p}")

DATES = re.compile(rb"/(?:CreationDate|ModDate) \(D:[^)]*\)")
res = {}
for p in sorted(figs, key=lambda q: q.endswith(".pdf")):          # PNGs first: a PDF's verdict refers to its PNG
    old, new = git("show", f"{REF}:{p}"), open(p, "rb").read()
    if p.endswith(".pdf"):
        if DATES.sub(b"", old) == DATES.sub(b"", new):
            res[p] = ("identical", "identical apart from its dates")
        else:
            png = p[:-4] + ".png"
            v = res.get(png, ("identical", "not modified by the run"))
            res[p] = ("anti-aliasing" if v[0] in ("identical", "anti-aliasing") else "differs",
                      f"differs beyond its dates; its PNG: {v[1]}")
        continue
    if old == new:
        res[p] = ("identical", "identical bytes"); continue
    try:
        import numpy as np
        from PIL import Image
        a = np.asarray(Image.open(io.BytesIO(old)).convert("RGBA"), dtype=int)
        b = np.asarray(Image.open(io.BytesIO(new)).convert("RGBA"), dtype=int)
        if a.shape != b.shape:
            res[p] = ("differs", f"size {a.shape} against {b.shape}"); continue
        d = np.abs(a - b)
        n, mx = int((d.max(axis=2) > 0).sum()), int(d.max())
        res[p] = ("anti-aliasing" if mx <= 2 else "differs", f"{n} pixels differ, largest channel difference {mx}"
                  + (" (anti-aliasing only)" if mx <= 2 else ""))
    except Exception as e:  # noqa: BLE001
        res[p] = ("differs", f"not compared: {type(e).__name__}: {e}")
tally = collections.Counter(v[0] for v in res.values())
print(f"images modified by the run: {len(figs)}; " + ", ".join(f"{k}: {v}" for k, v in sorted(tally.items())))
for p in sorted(res):
    if res[p][0] != "identical":
        print(f"    {p}: {res[p][1]}")
differ = [p for p in res if res[p][0] == "differs"]
print("10_logs_figures_compare:", "every committed log line reproduced and every image identical or anti-aliasing only"
      + ("; added log lines listed above" if added_only or any(a for _, _, a in missing_any) else "")
      if not missing_any and not differ and not eol else "committed log lines not reproduced, or images or line endings differing: listed above")
