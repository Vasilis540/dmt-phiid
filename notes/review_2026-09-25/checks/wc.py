"""Word count of draft_v2.md, Introduction through Methods: whitespace tokens, headings counted;
tables, table captions, display equations, separators excluded. Prints per-section counts."""
import re, sys
p = sys.argv[1]
L = open(p, encoding="utf-8").read().splitlines()
start = next(i for i, l in enumerate(L) if l.strip() == "## Introduction")
end = next(i for i, l in enumerate(L) if l.strip().startswith("## Acknowledg") or l.strip().startswith("## Data and code") or l.strip().startswith("## Author contributions"))
def is_eq(l):
    s = l.strip()
    # display equations: lines without a sentence verb pattern; heuristic list
    return bool(re.match(r"^(rtx = |sts = 2S|sts − \(xtx|S₄ = |R₄ = )", s))
tot = totnh = 0
sec = None; secs = {}
for l in L[start:end]:
    s = l.strip()
    if not s or s == "---" or s.startswith("|") or s.startswith("**Table") or s.startswith("**Fig") or s.startswith("Fig ") and s[4:5].isdigit() and ". " in s[:8] or is_eq(s):
        continue
    n = len(s.split())
    if s.startswith("#"):
        sec = s.lstrip("# ").strip()
        tot += n
        secs.setdefault(sec, [0, 0])[1] += n
        continue
    tot += n; totnh += n
    secs.setdefault(sec, [0, 0])[0] += n
for k, v in secs.items():
    print(f"{v[0]:5d} (+{v[1]} heading)  {k}")
print("total with headings", tot, "without", totnh)
