"""Independent mechanical check of manuscript/main_text_numbers.csv (planning session, 25 Sep 2026).
For every 'data' row: the source file exists; its locator line holds the stated string; the printed number
equals that value at the printed precision (sign-aware, % and ± handled); the row's context is in the text."""
import csv, re, sys, math
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
R = Path(sys.argv[1])
text = (R / "manuscript/draft_v2.md").read_text(encoding="utf-8")
textn = re.sub(r"\s*\n\s*", " ", text)
import unicodedata
lines = [l for l in open(R / "manuscript/main_text_numbers.csv", encoding="utf-8") if not l.startswith("#")]
rows = list(csv.DictReader(lines))
def num(s):
    s = s.strip().replace("−", "-").replace("+", "").replace("±", "").replace(",", "").replace("%", "").strip()
    try: return Decimal(s)
    except Exception: return None
bad = []
nd = 0
for i, r in enumerate(rows, 2):
    ctx = r["context"]
    if ctx and ctx.strip() and ctx.strip()[:60] not in text and ctx.strip()[:60] not in textn:
        # context may be cut mid-token; try a middle chunk
        mid = ctx.strip()[10:50]
        if mid not in text and mid not in textn:
            bad.append((i, r["number"], "CONTEXT NOT IN TEXT", ctx[:80]))
    if r["category"] != "data": continue
    nd += 1
    src = R / r["source_file"]
    if not src.exists():
        bad.append((i, r["number"], "NO SOURCE FILE", r["source_file"])); continue
    m = re.match(r"line (\d+); the line holds (.+?); anchor: (.*)$", r["locator"])
    if not m:
        bad.append((i, r["number"], "LOCATOR FORMAT", r["locator"][:100])); continue
    ln, held, anchor = int(m.group(1)), m.group(2).strip(), m.group(3)
    sl = src.read_text(encoding="utf-8", errors="replace").split("\n")
    if ln < 1 or ln > len(sl):
        bad.append((i, r["number"], "LINE OUT OF RANGE", f"{r['source_file']}:{ln}")); continue
    line = sl[ln - 1]
    if held not in line:
        bad.append((i, r["number"], "HELD STRING NOT ON LINE", f"{r['source_file']}:{ln} held={held!r} line={line[:120]!r}")); continue
    p, v = num(r["number"]), num(held)
    if p is None or v is None: continue
    # printed decimals
    s = r["number"].replace("−", "-").replace("+", "").replace("%", "").replace(",", "").strip()
    dec = len(s.split(".")[1]) if "." in s else 0
    q = Decimal(1).scaleb(-dec)
    ok = False
    for mode in (ROUND_HALF_UP, ROUND_HALF_EVEN):
        for vv in (v, -v, abs(v)):
            if abs(vv.quantize(q, rounding=mode)) == abs(p) or vv.quantize(q, rounding=mode) == p:
                ok = True
    if not ok:
        # percent conversions or ratios
        if abs(v * 100).quantize(q, rounding=ROUND_HALF_UP) == abs(p): ok = True
    if not ok:
        bad.append((i, r["number"], "VALUE MISMATCH", f"held={held} printed={r['number']} dec={dec} {r['source_file']}:{ln} note={r['note'][:80]}"))
    elif (p < 0) != (v < 0) and p != 0 and v != 0 and not r["number"].strip().startswith(("±",)):
        # sign differs: may be legitimate ("fell by 0.0164" printed positive)
        bad.append((i, r["number"], "SIGN DIFFERS (check wording)", f"held={held} printed={r['number']} {r['source_file']}:{ln} ctx={ctx[:90]!r}"))
print(f"rows {len(rows)}, data rows {nd}, flagged {len(bad)}")
for b in bad: print(*b, sep=" | ")
