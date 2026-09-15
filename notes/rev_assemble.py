"""
rev_assemble.py — fill notes/review_computations_2026-09-14.src.md's {{TABLE: label}} and
{{DECONV_COMPARISON}} markers from the inference CSVs and write review_computations_2026-09-14.md.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import rev_tables as rt

HERE = Path(__file__).resolve().parent
SRC = HERE / "review_computations_2026-09-14.src.md"
DST = HERE / "review_computations_2026-09-14.md"
df = rt.df

text = SRC.read_text()


def table_or_pending(m):
    label = m.group(1).strip()
    if df[df.label == label].empty:
        return f"**{label}** — (pending: not yet computed)"
    return rt.table(label).rstrip()


text = re.sub(r"\{\{TABLE: ([^}]+)\}\}", table_or_pending, text)


def row(label, s="primary"):
    sub = df[(df.label == label) & (df.set == s)]
    return None if sub.empty else sub.iloc[0]


def cell(r, digits=4):
    if r is None:
        return "pending"
    fm = "{:+." + str(digits) + "f}"
    return f"{fm.format(r.did)} [{fm.format(r.did_lo)}, {fm.format(r.did_hi)}], p = {r.did_p:.4f}, phase p = {r.phase_p:.4f}, {int(r.n_neg)}/14, FD-resid {'survives' if r.survives else 'does not survive'}"


lines = ["| series | raw | deconvolved |", "|---|---|---|"]
for base, var, est in (("sts", "ts_gsr", "W60"), ("sts", "ts_demean", "W60"), ("sts", "ts_gsr", "global-bins"), ("sts", "ts_demean", "global-bins"),
                       ("autocorr", "ts_gsr", "W60"), ("autocorr", "ts_demean", "W60"),
                       ("PhiR", "ts_gsr", "W60"), ("PhiR", "ts_demean", "W60"), ("PhiR", "ts_gsr", "global-bins"), ("PhiR", "ts_demean", "global-bins")):
    lines.append(f"| {base} {var} {est} | {cell(row(f'{base} {var} {est}'))} | {cell(row(f'{base}_deconv {var} {est}'))} |")
text = text.replace("{{DECONV_COMPARISON}}", "\n".join(lines))
DST.write_text(text)
left = re.findall(r"\{\{[^}]+\}\}", text)
print(f"wrote {DST} ({len(text.splitlines())} lines); unfilled markers: {left}")
