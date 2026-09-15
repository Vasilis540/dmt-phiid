"""
rev_tables.py — render the inference rows (notes/review_results/inference_rows_{raw,deconv}.csv)
as markdown tables for the results note; every number is taken from the CSV, not retyped.
Usage: .venv/bin/python notes/rev_tables.py [label ...]   (default: every label, raw then deconv)
"""
import sys
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parent / "review_results"
df = pd.concat([pd.read_csv(OUT / f) for f in ("inference_rows_raw.csv", "inference_rows_deconv.csv", "inference_rows_w30.csv") if (OUT / f).exists()], ignore_index=True)
# W = 60: 14 windows, pre 1–4. W = 30 and 30-TR bins: 28 units, pre 1–8 (rev_inference.window_sets; same as 06).
SETS = {"primary": "primary (windows 6–14)", "sensitivity": "sensitivity (5–14)", "early": "early (6–9)", "late": "late (10–14)",
        "trend_a_placebo_line": "trend (a): placebo line", "trend_b_shared_slope": "trend (b): shared slope"}
W30_SETS = {"primary": "primary (windows 11–28)", "sensitivity": "sensitivity (10–28)", "early": "early (11–18)", "late": "late (19–28)",
            "trend_a_placebo_line": "trend (a): placebo line", "trend_b_shared_slope": "trend (b): shared slope"}
BIN_SETS = {"primary": "primary (bins 11–28)", "sensitivity": "sensitivity (10–28)", "early": "early (11–18)", "late": "late (19–28)",
            "trend_a_placebo_line": "trend (a): placebo line", "trend_b_shared_slope": "trend (b): shared slope"}


def f4(x, sign=True):
    return ("{:+.4f}" if sign else "{:.4f}").format(x)


def table(label, digits=4):
    sub = df[df.label == label]
    if sub.empty:
        return f"(no rows for {label})\n"
    names = BIN_SETS if ("bins" in label) else (W30_SETS if "W30" in label else SETS)
    pre = "bins 1–8" if "bins" in label else ("windows 1–8" if "W30" in label else "windows 1–4")
    fm = "{:+." + str(digits) + "f}"
    lines = [f"**{label}** — pre-injection level ({pre}) DMT {sub.pre_dmt.iloc[0]:.4f}, PCB {sub.pre_pcb.iloc[0]:.4f}", "",
             "| window set | DiD [95 % CI] | sign-flip p | neg/14 | phase p | DMT change (p) | PCB change (p) | PCB share | FD-resid DiD [CI], p | survives |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for _, r in sub.iterrows():
        nm = names[r.set]
        if r.set.startswith("trend"):
            lines.append(f"| {nm} | {fm.format(r.did)} [{fm.format(r.did_lo)}, {fm.format(r.did_hi)}] | {r.did_p:.4f} | {int(r.n_neg)} | – | – | – | – | – | – |")
            continue
        ph = f"{r.phase_p:.4f}" if np.isfinite(r.phase_p) else "–"
        lines.append(f"| {nm} | {fm.format(r.did)} [{fm.format(r.did_lo)}, {fm.format(r.did_hi)}] | {r.did_p:.4f} | {int(r.n_neg)} | {ph} | "
                     f"{fm.format(r.dmt_change)} ({r.dmt_p:.3f}) | {fm.format(r.pcb_change)} ({r.pcb_p:.3f}) | {r.placebo_share:.2f} | "
                     f"{fm.format(r.resid_did)} [{fm.format(r.resid_lo)}, {fm.format(r.resid_hi)}], {r.resid_p:.4f} | {'yes' if r.survives else 'no'} |")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    labels = sys.argv[1:] or list(dict.fromkeys(df.label))
    for lab in labels:
        print(table(lab))
