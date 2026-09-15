"""
rev_regional_note.py — fill the markers of notes/regional_phir_deconv_2026-09-14.src.md from the CSVs
(rev_regional_tables.py, rev_tables.py) and write regional_phir_deconv_2026-09-14.md.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rev_regional_tables as t
import rev_tables as rt

HERE = Path(__file__).resolve().parent
SRC = HERE / "regional_phir_deconv_2026-09-14.src.md"
DST = HERE / "regional_phir_deconv_2026-09-14.md"
text = SRC.read_text()
fill = {
    "{{VALIDATION}}": t.validation_table(),
    "{{PREDICTION}}": t.table_prediction(),
    "{{CELLS}}": t.table_cells(),
    "{{NETWORKS}}": t.table_networks(),
    "{{SPIN}}": t.table_spin(),
    "{{MAPSTATS}}": t.table_map_stats(),
    "{{FDR_GSR}}": t.table_fdr_regions(("deconv", "ts_gsr", "win60")),
    "{{FDR_DEMEAN}}": t.table_fdr_regions(("deconv", "ts_demean", "win60")),
    "{{SUBJECTS}}": t.table_subjects(),
    "{{WINDOWS}}": t.table_windows(),
}
for k, v in fill.items():
    assert text.count(k) == 1, k
    text = text.replace(k, v)
text = re.sub(r"\{\{TABLE: ([^}]+)\}\}", lambda m: rt.table(m.group(1).strip()).rstrip(), text)
DST.write_text(text)
print(f"wrote {DST} ({len(text.splitlines())} lines); unfilled markers: {re.findall(r'\{\{[^}]+\}\}', text)}")
