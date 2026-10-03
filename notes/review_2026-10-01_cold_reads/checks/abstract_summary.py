"""abstract_summary.py — the word counts of the Abstract and the Author summary of the given draft (whitespace tokens),
against the limits of 300 and 200 words. Usage: python3 abstract_summary.py manuscript/draft_v2.md"""
import sys
t = open(sys.argv[1], encoding="utf-8").read()
ab = t.split("## Abstract\n\n")[1].split("\n\n")[0]
su = t.split("## Author summary\n\n")[1].split("\n\n")[0]
print(f"abstract {len(ab.split())} words (limit 300); author summary {len(su.split())} words (limit 200)")
