#!/usr/bin/env python3
"""apply_replacements.py — apply the verbatim replacements of the error-only revision of 25 September 2026.

Usage, from anywhere:
    python3 apply_replacements.py <repository root> text_replacements_2026-09-25.json

Every entry of the JSON list names a file, an exact old string, its replacement, the number of times the old string
must occur when the entry is applied (entries apply in list order, each to the text the earlier ones left) and, in
"why", the item of notes/review_2026-09-25/verification_2026-09-25.md it applies ("bookkeeping" for the entries of
CLAUDE.md and README.md). Entries whose "op" is "minus" replace the ASCII hyphen-minus of a negative number by the
minus sign U+2212 in one file, with the regular expression given in the entry, and must make exactly "count"
replacements. Files are read and written as they are, line endings included. Nothing is written unless every entry
matches its count: the script changes all files or none. It prints one line per entry and, at the end, the sha256 of
every file it wrote.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

root, spec = Path(sys.argv[1]), json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
texts, bad = {}, []
for e in spec:
    f = e["file"]
    if f not in texts:
        with open(root / f, encoding="utf-8", newline="") as fh:
            texts[f] = fh.read()
    t = texts[f]
    if e.get("op") == "minus":
        new, n = re.subn(e["regex"], "−", t)
        status = "ok" if n == e["count"] else f"MISMATCH: {n} replacements, expected {e['count']}"
        texts[f] = new
    else:
        n = t.count(e["old"])
        status = "ok" if n == e["count"] else f"MISMATCH: old occurs {n} times, expected {e['count']}"
        if n == e["count"]:
            texts[f] = t.replace(e["old"], e["new"])
    print(f"{e['id']:<7} {f:<42} {status}")
    if status != "ok":
        bad.append(e["id"])
if bad:
    sys.exit(f"\nNOTHING WRITTEN: {len(bad)} entries did not match ({', '.join(bad)}).")
for f, t in texts.items():
    with open(root / f, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)
print(f"\nall {len(spec)} entries applied; files written:")
for f in sorted(texts):
    print(f"  {hashlib.sha256((root / f).read_bytes()).hexdigest()}  {f}")
