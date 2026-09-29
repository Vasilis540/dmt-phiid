"""b26_changes.py — every change that a run makes to the committed outputs: the listing that rule (i) of B26's pre-run
entry (manuscript/analysis_record.md, "The matrices that are not positive definite (B26): pre-run entry") reads, one
change at a time (every changed line and cell in full; each changed array by its number of changed entries, its largest
change and its first 2,000 entries; each image by its differing pixels).

Usage (from the repository root, pinned environment, on the working tree the run left, before anything is added,
restored or committed):
    .venv/bin/python notes/review_2026-09-28/checks/b26_changes.py [REF]          (the committed outputs at REF, default HEAD)
    .venv/bin/python notes/review_2026-09-28/checks/b26_changes.py --dirs OLD NEW  (the output files of two trees, e.g. two
                                                                                    runs on the same synthetic series)
The files: every file under results/, notes/review_results/ and manuscript/figures/, and
notes/review_computations_2026-09-14.md (which rev_assemble.py, a step of run_all.sh's section 6, rewrites), that
differs from REF (git status), or, with --dirs, that differs between the two trees. For each:
- a text file (.md, .log, .txt, .tex): the committed and the regenerated lines are paired (blank lines set aside; first
  on their form with every number rounded to six decimals; inside a changed stretch, by similarity if a line was
  inserted or deleted there, otherwise on their form without the numbers and, where that differs too, by similarity;
  a stretch of more than 250,000 line pairs is aligned on the form first, and a part of it still that large, with sides
  of unequal length, is listed with every line alone)
  and every pair that does not agree is printed in full, with its line numbers in both files, as is every line
  without a counterpart. Two lines agree if they are identical once the parts that legitimately change between runs are masked,
  as in notes/planning_checks_2026-09-16/reproduction_checks/10_logs_figures_compare.py (git SHAs, dates and clock
  times, elapsed times, absolute paths, the count of B21's quoted intervals), and every number in both is replaced by a
  placeholder, each pair of numbers within 1e-9 (so that a printed zero may change its sign);
- a CSV (.csv): every cell that differs beyond 1e-9 (NaN equal to NaN; text cells by equality), with its line in the
  file, its row's text cells as a label, and its column (a row with more fields than the header, written without
  quoting, has its first fields joined); a CSV whose header or number of rows changed is listed as a text file;
- a binary (.npy, .npz, .pkl): every array or value, reached by its key, index or column, whose entries differ beyond
  1e-9 or whose NaN pattern or shape differs, with the number of such entries, the largest difference over the entries
  finite in both, how many of them are a change of NaN or infinity and how many entries become NaN, and the index and
  the committed and regenerated values of each (those changes first; the first 2,000 per array; the files themselves
  are in the evidence);
- an image: a PNG pixel by pixel (the number of differing pixels, the largest channel difference, 0–255); a PDF byte
  for byte once its /CreationDate and /ModDate are removed.
New and deleted files are named. Nothing is written or changed; the listing goes to standard output.
"""
import csv
import difflib
import io
import pickle
import re
import subprocess
import sys
from pathlib import Path

import numpy as np

OUTPUT_DIRS = ("results/", "notes/review_results/", "manuscript/figures/")
OUTPUT_FILES = ("notes/review_computations_2026-09-14.md",)
TEXT = (".md", ".log", ".txt", ".tex")
BIN = (".npy", ".npz", ".pkl")
CAP = 2000
TOL = 1e-9
csv.field_size_limit(sys.maxsize)
MASKS = [
    (re.compile(r"\bgit[= ][0-9a-f]{7,40}(?:-dirty)?"), "git=SHA"),
    (re.compile(r"\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?"), "DATETIME"),
    (re.compile(r"\b\d{1,2}:\d{2}:\d{2}(?:\.\d+)?\b"), "TIME"),
    (re.compile(r"\b\d+(?:\.\d+)?\s?(?:ms/pair|ms|s|sec|secs|seconds|min|minutes|h)\b(?!\s*=)(?!\s*\((?!\d))"), "DUR"),
    (re.compile(r"(?:/home|/root|/tmp|/Users|/mnt|/media)/\S*"), "PATH"),
    (re.compile(r"; \d+ of them matched to an interval quoted in"), "; N of them matched to an interval quoted in"),
]
NUM = re.compile(r"(?<![\w.])[-+−]?(?:\d+\.\d*|\.\d+|\d+)(?:[eE][-+−]?\d+)?(?!\w)(?!\.\d)")


# ------------------------------------------------------------------ text
def mask(line):
    for pat, rep in MASKS:
        line = pat.sub(rep, line)
    return line


def split(line):
    nums = []

    def rep(m):
        nums.append(float(m.group(0).replace("−", "-")))
        return "\0"
    return NUM.sub(rep, line), nums


def agree(a, b):
    (sa, na), (sb, nb) = split(mask(a)), split(mask(b))
    return sa == sb and all(abs(x - y) <= TOL for x, y in zip(na, nb))


def canon(line):
    s, nums = split(mask(line))
    it = iter(f"{round(x, 6) + 0.0:.6f}" for x in nums)
    return re.sub("\0", lambda m: next(it), s)


def skeleton(line):
    return split(mask(line))[0]


def similarity(a, b):
    """the share of the shorter line that the longer one holds, in order (difflib's matching characters over the shorter
    length), so that a line that gained or lost a clause stays paired with what it was; 0 when the matched characters
    are under 0.3 of the longer line, so that a short line is not taken for a part of a long one"""
    m = sum(k.size for k in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks())
    return m / max(1, min(len(a), len(b))) if m >= 0.3 * max(len(a), len(b)) else 0.0


def similar_pairs(aa, bs):
    """aa and bs ([(line number, line)]) paired in order so that the summed similarity of the pairs is largest (a pair
    needs a similarity of at least 0.6; two lines of the same form, their numbers masked, score 1 more); [(ia, a, ib,
    b)] with None on the side of a line left alone"""
    ka, kb = [skeleton(a) for _, a in aa], [skeleton(b) for _, b in bs]
    R = [[similarity(a, b) + (ka[x] == kb[y]) for y, (_, b) in enumerate(bs)] for x, (_, a) in enumerate(aa)]
    S = [[0.0] * (len(bs) + 1) for _ in range(len(aa) + 1)]
    for x in range(len(aa) - 1, -1, -1):
        for y in range(len(bs) - 1, -1, -1):
            S[x][y] = max(S[x + 1][y], S[x][y + 1], R[x][y] + S[x + 1][y + 1] if R[x][y] >= 0.6 else -1.0)
    out, x, y = [], 0, 0
    while x < len(aa) or y < len(bs):
        if x < len(aa) and y < len(bs) and R[x][y] >= 0.6 and S[x][y] == R[x][y] + S[x + 1][y + 1]:
            out.append((aa[x][0], aa[x][1], bs[y][0], bs[y][1]))
            x, y = x + 1, y + 1
        elif x < len(aa) and (y == len(bs) or S[x][y] == S[x + 1][y]):
            out.append((aa[x][0], aa[x][1], None, None))
            x += 1
        else:
            out.append((None, None, bs[y][0], bs[y][1]))
            y += 1
    return out


SMALL = 250_000                                          # the largest stretch (lines × lines) paired by similarity


def text_changes(old, new):
    """[(committed line number or None, committed line or None, regenerated line number or None, regenerated line or
    None)] for the paired lines that do not agree and the lines without a counterpart; blank lines set aside. Lines are
    paired on their form with the numbers rounded to six decimals. A stretch where that fails is paired by similarity if
    its two sides differ in length (a line inserted or deleted among changed lines); otherwise on the lines' form
    without the numbers, lines of the same form by position and the others by similarity, so that an inserted or
    deleted line is reported alone. A stretch of more than SMALL line pairs is aligned on the lines' form first; a part
    of it that is still that large, with sides of unequal length, is listed with every line alone."""
    A = [(i + 1, l) for i, l in enumerate(old) if l.strip()]
    B = [(i + 1, l) for i, l in enumerate(new) if l.strip()]
    out = []
    keep = lambda pairs: [q for q in pairs if q[0] is None or q[2] is None or not agree(q[1], q[3])]
    sm = difflib.SequenceMatcher(None, [canon(l) for _, l in A], [canon(l) for _, l in B], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        a_, b_ = A[i1:i2], B[j1:j2]
        if tag == "equal":
            out += keep([(ia, a, ib, b) for (ia, a), (ib, b) in zip(a_, b_)])
            continue
        if a_ and b_ and len(a_) != len(b_) and len(a_) * len(b_) <= SMALL:
            out += keep(similar_pairs(a_, b_))
            continue
        sm2 = difflib.SequenceMatcher(None, [skeleton(l) for _, l in a_], [skeleton(l) for _, l in b_], autojunk=False)
        for tag2, k1, k2, m1, m2 in sm2.get_opcodes():
            aa, bs = a_[k1:k2], b_[m1:m2]
            if tag2 == "equal" or (tag2 == "replace" and len(aa) == len(bs) and len(aa) * len(bs) > SMALL):
                out += keep([(ia, a, ib, b) for (ia, a), (ib, b) in zip(aa, bs)])
            elif tag2 == "replace" and len(aa) * len(bs) <= SMALL:
                out += keep(similar_pairs(aa, bs))
            else:
                out += [(ia, a, None, None) for ia, a in aa] + [(None, None, ib, b) for ib, b in bs]
    return out


# ------------------------------------------------------------------ CSV
def csv_rows(text, with_lines=False):
    """the rows, a row with more fields than the header having its first fields joined (a CSV written without quoting,
    whose first column holds commas, as partB17_calibration.py's and partB17b_calibration_filtered.py's conditions);
    with with_lines, each row with its line number in the file"""
    lines = [(i + 1, l) for i, l in enumerate(text.splitlines()) if not l.startswith("#")]
    rows = [(i, r) for (i, _), r in zip(lines, csv.reader(l for _, l in lines))] if lines else []
    if rows:
        n = len(rows[0][1])
        rows = [rows[0]] + [(i, [",".join(r[:len(r) - n + 1])] + r[len(r) - n + 1:] if len(r) > n else r) for i, r in rows[1:]]
    return rows if with_lines else [r for _, r in rows]


def num(x):
    try:
        return float(x)
    except ValueError:
        return None


def csv_changes(old, new):
    """[(line in the regenerated file, row label, column, committed, regenerated)] for the cells that differ beyond 1e-9
    (NaN equal to NaN), or None if the header or the number of rows changed."""
    A, B = csv_rows(old, True), csv_rows(new, True)
    if not A or not B or A[0][1] != B[0][1] or len(A) != len(B):
        return None
    hdr, out = A[0][1], []
    for (_, ra), (lb, rb) in zip(A[1:], B[1:]):
        label = " · ".join(c for c in ra if num(c) is None)
        for h, x, y in zip(hdr, ra, rb):
            fx, fy = num(x), num(y)
            if fx is not None and fy is not None:
                if not (fx == fy or abs(fx - fy) <= TOL or (fx != fx and fy != fy)):
                    out.append((lb, label, h, x, y))
            elif x != y:
                out.append((lb, label, h, x, y))
    return out


# ------------------------------------------------------------------ binaries
def leaves(obj, path=""):
    """(path, value) of every array or scalar in a loaded binary: dicts by key, lists and tuples by index, DataFrames and
    Series by column and index, NpzFile by key."""
    try:
        import pandas as pd
    except ImportError:                                   # pragma: no cover
        pd = None
    if pd is not None and isinstance(obj, pd.DataFrame):
        for c in obj.columns:
            yield from leaves(obj[c], f"{path}[{c!r}]")
        return
    if pd is not None and isinstance(obj, pd.Series):
        vals = obj.to_numpy()
        if vals.dtype.kind in "fcbiu":
            yield path, vals
        else:
            for i, v in zip(obj.index, vals):
                yield from leaves(v, f"{path}[{i!r}]")
        return
    if isinstance(obj, dict):
        for k in obj:
            yield from leaves(obj[k], f"{path}[{k!r}]")
        return
    if isinstance(obj, (list, tuple)):
        for i, v in enumerate(obj):
            yield from leaves(v, f"{path}[{i}]")
        return
    yield path, obj


def load(name, data):
    if name.endswith(".npy"):
        return {"": np.load(io.BytesIO(data), allow_pickle=False)}
    if name.endswith(".npz"):
        z = np.load(io.BytesIO(data), allow_pickle=False)
        return {k: z[k] for k in z.files}
    return {"": pickle.loads(data)}


def value_changes(a, b):
    """None if a and b agree; else (number of differing entries, of how many, largest difference over the entries finite
    in both, [(index, a, b)]), or (kind, description) for a change of shape, type or structure."""
    if isinstance(a, np.ndarray) or isinstance(b, np.ndarray):
        a, b = np.asarray(a), np.asarray(b)
        if a.shape != b.shape:
            return ("shape", f"{a.shape} → {b.shape}")
        if a.dtype.kind in "fciub" and b.dtype.kind in "fciub":
            ct = complex if "c" in a.dtype.kind + b.dtype.kind else float
            fa, fb = a.astype(ct), b.astype(ct)
            with np.errstate(all="ignore"):
                na, nb = np.isnan(fa), np.isnan(fb)
                both_fin = np.isfinite(fa) & np.isfinite(fb)
                d = np.where(both_fin, np.abs(fa - fb), 0.0)
                pat = (na != nb) | (~both_fin & ~(na & nb) & (fa != fb))     # a NaN or an infinity on one side only, or changed
                bad = pat | (d > TOL)
            if not bad.any():
                return None
            idx = np.concatenate([np.argwhere(pat), np.argwhere(bad & ~pat)])[:CAP]      # the changes of pattern first
            return (int(bad.sum()), a.size, float(d.max()), [(tuple(int(i) for i in ix), fa[tuple(ix)], fb[tuple(ix)]) for ix in idx],
                    int(pat.sum()), int((~na & nb).sum()))
        bad = a != b
        if not np.any(bad):
            return None
        idx = np.argwhere(np.atleast_1d(bad))[:CAP]
        return (int(np.sum(bad)), a.size, float("nan"), [(tuple(int(i) for i in ix), np.atleast_1d(a)[tuple(ix)], np.atleast_1d(b)[tuple(ix)]) for ix in idx])
    if isinstance(a, (float, np.floating)) and isinstance(b, (float, np.floating)):
        if (a != a and b != b) or a == b or (np.isfinite(a) and np.isfinite(b) and abs(a - b) <= TOL):
            return None
        fin = bool(np.isfinite(a) and np.isfinite(b))
        return (1, 1, abs(a - b) if fin else 0.0, [((), a, b)], int(not fin), int(a == a and b != b))
    if type(a) is not type(b) and not (isinstance(a, (int, np.integer)) and isinstance(b, (int, np.integer))):
        return ("type", f"{type(a).__name__} → {type(b).__name__}")
    if a != b:
        return (1, 1, float("nan"), [((), a, b)])
    return None


def bin_changes(name, old, new):
    """[(array path, change)] for a binary file's arrays and values that differ; change as value_changes gives it."""
    A, B = load(name, old), load(name, new)
    out = []
    if set(A) != set(B):
        out.append(("(keys)", ("keys", f"{sorted(A)} → {sorted(B)}")))
    for k in sorted(set(A) & set(B)):
        la, lb = list(leaves(A[k], k)), list(leaves(B[k], k))
        if [p for p, _ in la] != [p for p, _ in lb]:
            out.append((k or "(object)", ("structure", f"{len(la)} → {len(lb)} leaves")))
            continue
        for (p, a), (_, b) in zip(la, lb):
            c = value_changes(a, b)
            if c is not None:
                out.append((p or "(value)", c))
    return out


# ------------------------------------------------------------------ images
def png_changes(old, new):
    try:
        from PIL import Image
    except ImportError:                                   # pragma: no cover
        return "differs (bytes); Pillow not available for a pixel comparison"
    a = np.asarray(Image.open(io.BytesIO(old)).convert("RGBA"), dtype=int)
    b = np.asarray(Image.open(io.BytesIO(new)).convert("RGBA"), dtype=int)
    if a.shape != b.shape:
        return f"size {a.shape[1]}×{a.shape[0]} → {b.shape[1]}×{b.shape[0]}"
    d = np.abs(a - b).max(axis=2)
    n = int((d > 0).sum())
    return "the same pixels" if n == 0 else f"{n:,} of {d.size:,} pixels differ, largest channel difference {int(d.max())}"


def pdf_changes(old, new):
    strip = lambda s: re.sub(rb"/(CreationDate|ModDate) *\(D:[^)]*\)", b"", s)
    return "the same once /CreationDate and /ModDate are removed" if strip(old) == strip(new) else "differs (bytes; see its PNG)"


# ------------------------------------------------------------------ the listing
def py(x):
    """a NumPy scalar as the Python scalar it holds (printed by its repr, all its digits)"""
    return x.item() if isinstance(x, np.generic) else x


def is_output(p):
    return p.startswith(OUTPUT_DIRS) or p in OUTPUT_FILES


def listing(name, old, new):
    """The lines of the listing for one file, given its committed and regenerated bytes (None if absent)."""
    if old is None:
        return [f"## {name}: new file"]
    if new is None:
        return [f"## {name}: deleted"]
    if old == new:
        return []
    if name.endswith(".csv"):
        c = csv_changes(old.decode("utf-8"), new.decode("utf-8"))
        if c is not None:
            if not c:
                return [f"## {name}: the bytes differ; every cell agrees (within 1e-9)"]
            L = [f"## {name}: {len(c):,} cell(s) differ (line in the file, its row's text cells, column: committed → regenerated)"]
            return L + [f"- l. {k} ({lab}), {h}: {x} → {y}" for k, lab, h, x, y in c]
    if name.endswith(TEXT + (".csv",)):
        c = text_changes(old.decode("utf-8").split("\n"), new.decode("utf-8").split("\n"))
        if not c:
            return [f"## {name}: the bytes differ; every line agrees (masks as in 10_logs_figures_compare.py; numbers within 1e-9)"]
        L = [f"## {name}: {len(c):,} line(s) differ (committed l., then regenerated l.)"]
        for ia, a, ib, b in c:
            L.append(f"- l. {ia if ia else '—'} → l. {ib if ib else '—'}")
            L.append(f"  − {a if a is not None else '(none)'}")
            L.append(f"  + {b if b is not None else '(none)'}")
        return L
    if name.endswith(BIN):
        c = bin_changes(name, old, new)
        if not c:
            return [f"## {name}: the bytes differ; every array and value agrees (within 1e-9, NaN patterns equal)"]
        L = [f"## {name}: {len(c):,} array(s) or value(s) differ"]
        for p, ch in c:
            if isinstance(ch[0], str):
                L.append(f"- {p}: {ch[0]} {ch[1]}")
                continue
            n, size, dmax, items = ch[:4]
            npat, nnan = ch[4:6] if len(ch) > 4 else (0, 0)
            L.append(f"- {p}: {n:,} of {size:,} entries differ, largest difference over the entries finite in both {dmax:.3g}"
                     + (f"; {npat:,} of them a change of NaN or infinity ({nnan:,} become NaN), listed first" if npat else "")
                     + (f" (the first {CAP:,} listed)" if n > CAP else "") + ":")
            L += [f"  - {ix}: {py(x)!r} → {py(y)!r}" for ix, x, y in items]
        return L
    if name.endswith(".png"):
        return [f"## {name}: {png_changes(old, new)}"]
    if name.endswith(".pdf"):
        return [f"## {name}: {pdf_changes(old, new)}"]
    return [f"## {name}: differs (bytes)"]


def main(argv):
    if argv[:1] == ["--dirs"]:
        O, N = Path(argv[1]), Path(argv[2])
        names = sorted({p.relative_to(O).as_posix() for p in O.rglob("*") if p.is_file()} |
                       {p.relative_to(N).as_posix() for p in N.rglob("*") if p.is_file()})
        names = [n for n in names if is_output(n) and "/.git/" not in f"/{n}"]
        head = f"# b26_changes.py: {O} → {N}"
        get = lambda n: ((O / n).read_bytes() if (O / n).exists() else None, (N / n).read_bytes() if (N / n).exists() else None)
    else:
        ref = argv[0] if argv else "HEAD"
        sha = subprocess.run(["git", "rev-parse", "--short=7", ref], capture_output=True, text=True, check=True).stdout.strip()
        st = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all", "--no-renames", "--", *OUTPUT_DIRS, *OUTPUT_FILES],
                            capture_output=True, text=True, check=True).stdout.splitlines()
        if ref != "HEAD":
            st += [f" M {p}" for p in subprocess.run(["git", "diff", "--name-only", ref, "HEAD", "--", *OUTPUT_DIRS, *OUTPUT_FILES],
                                                      capture_output=True, text=True, check=True).stdout.splitlines()]
        names = sorted({l[3:].strip('"') for l in st})
        head = f"# b26_changes.py: {ref} ({sha}) → the working tree"

        def get(n):
            p = subprocess.run(["git", "show", f"{ref}:{n}"], capture_output=True)
            return (p.stdout if p.returncode == 0 else None, Path(n).read_bytes() if Path(n).exists() else None)
    print(head + "; text: masks of 10_logs_figures_compare.py, numbers within 1e-9; CSV cells and binary entries within "
          "1e-9, NaN equal to NaN")
    n_changed = n_new = n_del = n_agree = 0
    for n in names:
        old, new = get(n)
        L = listing(n, old, new)
        if not L:
            continue
        agrees = L[0][len(f"## {n}: "):].startswith(("the bytes differ; every", "the same "))
        n_new += old is None
        n_del += new is None
        n_agree += old is not None and new is not None and agrees
        n_changed += old is not None and new is not None and not agrees
        print("\n" + "\n".join(L))
    print(f"\n# {len(names)} file(s) examined: {n_changed} with changes listed above, {n_agree} whose bytes differ but whose "
          f"content agrees, {n_new} new, {n_del} deleted; the others byte for byte the same")


if __name__ == "__main__":
    main(sys.argv[1:])
