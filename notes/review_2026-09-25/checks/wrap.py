"""Write reading copies of the manuscript files: each original line prefixed with its line number,
long lines split at spaces into continuation lines marked [N+], so no line exceeds ~900 characters."""
import sys, pathlib
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
files = ["draft_v2.md", "figures/captions_v2.md", "si/S1_Text.md", "si/S2_Text.md", "si/S3_Text.md",
         "si/S4_Text.md", "si/S5_Text.md", "supplementary.md"]
for f in files:
    lines = (src / f).read_text(encoding="utf-8").split("\n")
    res = []
    for i, l in enumerate(lines, 1):
        if len(l) <= 900:
            res.append(f"[{i}] {l}"); continue
        words, cur, first = l.split(" "), "", True
        for w in words:
            if cur and len(cur) + 1 + len(w) > 850:
                res.append(f"[{i}{'' if first else '+'}] {cur}"); first = False; cur = w
            else:
                cur = w if not cur else cur + " " + w
        res.append(f"[{i}{'' if first else '+'}] {cur}")
    (out / f.replace("/", "__")).write_text("\n".join(res) + "\n", encoding="utf-8")
    print(f, len(lines), "->", len(res))
