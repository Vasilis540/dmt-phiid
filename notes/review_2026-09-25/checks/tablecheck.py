"""tablecheck.py — every row of every markdown table in the given files has the number of cells of its header row
(an escaped pipe, \\|, and a pipe inside a code span are content). Usage: python3 tablecheck.py <file> [<file> ...]"""
import re, sys, glob
def cells(l):
    s = re.sub(r"\\\|", "", l)          # escaped pipes are content
    s = re.sub(r"`[^`]*`", "", s)        # pipes inside code spans are content
    return s.count("|")
bad = 0
for f in sys.argv[1:]:
    L = open(f, encoding="utf-8").read().split("\n")
    i = 0
    while i < len(L):
        if L[i].startswith("|") and i + 1 < len(L) and re.match(r"^\|(\s*:?-+:?\s*\|)+\s*$", L[i + 1]):
            n = cells(L[i]); j = i
            while j < len(L) and L[j].startswith("|"):
                if cells(L[j]) != n:
                    bad += 1; print(f"{f}:{j+1}: {cells(L[j])} pipes, header {n}: {L[j][:100]}")
                j += 1
            i = j
        else:
            i += 1
print("rows with a wrong cell count:", bad)
