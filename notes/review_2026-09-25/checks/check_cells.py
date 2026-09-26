"""Second pass: does the held string denote the right cell? For each data row, find the numeric tokens on the
source line that round to the printed value (with sign when the printed value is signed); flag rows whose held
token is not among them."""
import csv, re, sys
from pathlib import Path
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, InvalidOperation
R = Path(sys.argv[1])
rows = list(csv.DictReader([l for l in open(R / "manuscript/main_text_numbers.csv", encoding="utf-8") if not l.startswith("#")]))
def D(s):
    try: return Decimal(s.replace("−", "-").replace("+", "").replace(",", ""))
    except InvalidOperation: return None
flag = 0
for i, r in enumerate(rows, 2):
    if r["category"] != "data": continue
    m = re.match(r"line (\d+); the line holds (.+?); anchor: (.*)$", r["locator"])
    if not m: continue
    line = (R / r["source_file"]).read_text(encoding="utf-8", errors="replace").split("\n")[int(m.group(1)) - 1]
    held = m.group(2).strip()
    pr = r["number"].strip()
    signed = pr[:1] in "+−-"
    pv = D(pr.replace("%", "").replace("±", ""))
    if pv is None: continue
    s = pr.replace("−", "-").replace("+", "").replace("%", "").replace("±", "").replace(",", "")
    dec = len(s.split(".")[1]) if "." in s else 0
    q = Decimal(1).scaleb(-dec)
    toks = re.findall(r"[-+−]?\d+(?:\.\d+)?(?:e-?\d+)?", line)
    def match(t):
        v = D(t)
        if v is None: return False
        for mode in (ROUND_HALF_UP, ROUND_HALF_EVEN):
            try: rv = v.quantize(q, rounding=mode)
            except InvalidOperation: return False
            if signed and rv == pv: return True
            if not signed and abs(rv) == abs(pv): return True
            if abs(v * 100).quantize(q, rounding=mode) == abs(pv): return True
        return False
    cands = [t for t in toks if match(t)]
    htoks = re.findall(r"[-+−]?\d+(?:\.\d+)?(?:e-?\d+)?", held)
    hok = any(match(t) for t in htoks)
    if not hok:
        flag += 1
        print(f"row {i}: printed {pr} held {held!r} NOT matching (with sign); candidates on line: {cands[:6]} | {r['source_file']}:{m.group(1)} | ctx {r['context'][:70]!r}")
print("flagged", flag)
