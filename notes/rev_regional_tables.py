"""
rev_regional_tables.py — markdown tables for notes/regional_phir_deconv_2026-09-14.md, rendered
from notes/review_results/regional/*.csv, inference_rows_w30.csv and the logs; nothing typed by hand.
Provides table_*() functions used by rev_regional_note.py; run directly to print them all.
"""
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

HERE = Path(__file__).resolve().parent
RR = HERE / "review_results"
REG = RR / "regional"
CELLS = [("deconv", "ts_gsr", "win60"), ("deconv", "ts_demean", "win60"), ("deconv", "ts_gsr", "global"), ("deconv", "ts_demean", "global"),
         ("raw", "ts_gsr", "win60"), ("raw", "ts_demean", "win60"), ("raw", "ts_gsr", "global"), ("raw", "ts_demean", "global")]
NETS = ("Vis", "SomMot", "DorsAttn", "SalVentAttn", "Limbic", "Cont", "Default", "Subcortex")


def load(cell):
    series, var, est = cell
    return pd.read_csv(REG / f"regional_phir_{series}_{var}_{est}.csv", comment="#")


def get(d, section, name):
    r = d[(d.section == section) & (d.name == name)]
    if r.empty:
        raise KeyError((section, name))
    return r.iloc[0]


def cell_name(cell):
    series, var, est = cell
    return f"{'deconvolved' if series == 'deconv' else 'raw'} {var} {'W60' if est == 'win60' else 'global'}"


def f4(x):
    return f"{x:+.4f}"


def ci(r):
    return f"{f4(r.value)} [{f4(r.ci_lo)}, {f4(r.ci_hi)}], p = {r.p:.4f}"


def table_prediction(cell=("deconv", "ts_gsr", "win60")):
    d = load(cell)
    L = [f"**{cell_name(cell)}** — per-subject mean ΦR DiD inside minus outside the proxy (positive = larger increase inside)", "",
         "| comparison | difference [95 % CI], p | positive/14 | n inside / n outside |", "|---|---|---|---|"]
    for sec, name, lab in (("workspace_primary_Default+Cont", "workspace_minus_nonworkspace_vs_noncortex_ws", "primary proxy (Default + Control) vs non-workspace cortex"),
                           ("workspace_primary_Default+Cont", "gateway_proxy_minus_nonworkspace_vs_noncortex_ws", "gateway proxy (Default) vs non-workspace cortex"),
                           ("workspace_primary_Default+Cont", "broadcaster_proxy_minus_nonworkspace_vs_noncortex_ws", "broadcaster proxy (Control) vs non-workspace cortex"),
                           ("workspace_primary_Default+Cont", "gateway_proxy_minus_broadcaster_proxy", "gateway proxy minus broadcaster proxy"),
                           ("workspace_primary_Default+Cont", "workspace_minus_nonworkspace_vs_noncortex_ws+subcortex", "primary proxy vs non-workspace cortex + subcortex"),
                           ("workspace_named_subregion", "workspace_minus_nonworkspace_vs_noncortex_ws", "named-subregion proxy vs non-workspace cortex"),
                           ("workspace_named_subregion", "gateway_proxy_minus_nonworkspace_vs_noncortex_ws", "named gateway (21) vs non-workspace cortex"),
                           ("workspace_named_subregion", "broadcaster_proxy_minus_nonworkspace_vs_noncortex_ws", "named broadcaster (Cont_PFCl, 5) vs non-workspace cortex")):
        r = get(d, sec, name)
        pos = re.search(r"pos=(\d+)/14", str(r.note))
        ns = re.search(r"n_ws=(\d+) n_non=(\d+)", str(r.note)) or re.search(r"n=(\d+)", str(r.note)) or re.search(r"n_gw=(\d+) n_bc=(\d+)", str(r.note))
        L.append(f"| {lab} | {ci(r)} | {pos.group(1) if pos else '–'} | {' / '.join(ns.groups()) if ns else '–'} |")
    ws, non = get(d, "workspace_primary_Default+Cont", "workspace_mean_did_vs_noncortex_ws"), get(d, "workspace_primary_Default+Cont", "nonworkspace_mean_did_vs_noncortex_ws")
    dm, pc = get(d, "workspace_primary_Default+Cont", "dmt_change_workspace_minus_nonworkspace_cortex"), get(d, "workspace_primary_Default+Cont", "pcb_change_workspace_minus_nonworkspace_cortex")
    L += ["", f"Mean DiD inside the primary proxy {ci(ws)}; outside {ci(non)}. Composition of the inside-minus-outside difference: DMT-run change {ci(dm)}; placebo-run change {ci(pc)}."]
    return "\n".join(L)


def table_cells():
    L = ["| cell | whole-brain ΦR DiD, p | FDR regions (q = 0.05) | uncorrected p < 0.05 | group-mean DiD > 0 | primary proxy − non-workspace cortex [CI], p (pos/14) | gateway − non | broadcaster − non | named proxy − non | 5-HT2A ρ (spin p) |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for cell in CELLS:
        d = load(cell)
        wb = get(d, "regional_did", "whole_brain_did_mean_over_regions")
        nf, npos, nneg = get(d, "regional_did", "n_regions_fdr_significant"), get(d, "regional_did", "n_fdr_significant_positive"), get(d, "regional_did", "n_fdr_significant_negative")
        nu, ngp = get(d, "regional_did", "n_uncorrected_p_below_0.05"), get(d, "regional_did", "n_groupmean_positive_of_115")
        ws = get(d, "workspace_primary_Default+Cont", "workspace_minus_nonworkspace_vs_noncortex_ws")
        gw = get(d, "workspace_primary_Default+Cont", "gateway_proxy_minus_nonworkspace_vs_noncortex_ws")
        bc = get(d, "workspace_primary_Default+Cont", "broadcaster_proxy_minus_nonworkspace_vs_noncortex_ws")
        nm = get(d, "workspace_named_subregion", "workspace_minus_nonworkspace_vs_noncortex_ws")
        sp = get(d, "spatial_spin_cortical99", "rho_5HT2A")
        pos = re.search(r"pos=(\d+)/14", str(ws.note)).group(1)
        L.append(f"| {cell_name(cell)} | {f4(wb.value)}, {wb.p:.4f} | {int(nf.value)} ({int(npos.value)} +, {int(nneg.value)} −) | {int(nu.value)} | {int(ngp.value)}/115 | "
                 f"{f4(ws.value)} [{f4(ws.ci_lo)}, {f4(ws.ci_hi)}], {ws.p:.4f} ({pos}) | {f4(gw.value)}, {gw.p:.3f} | {f4(bc.value)}, {bc.p:.3f} | {f4(nm.value)}, {nm.p:.3f} | {sp.value:+.3f} ({sp.p:.5f}) |")
    return "\n".join(L)


def table_networks():
    L = ["| cell | " + " | ".join(NETS) + " |", "|---|" + "---|" * len(NETS)]
    for cell in CELLS:
        d = load(cell)
        vals = []
        for n in NETS:
            r = d[(d.section == "network_mean_did") & (d.name.str.startswith(n + "_n"))].iloc[0]
            fdr = re.search(r"fdr_sig=(\d+)", str(r.note)).group(1)
            vals.append(f"{f4(r.value)} ({r.p:.3f}; {fdr})")
        L.append(f"| {cell_name(cell)} | " + " | ".join(vals) + " |")
    return "\n".join(L)


def table_spin():
    maps = ("5HT2A", "5HT1A", "5HT1B", "5HT4", "5HTT")
    L = ["| cell | " + " | ".join(f"{m} ρ (two-sided spin p; BH)" for m in maps) + " | 115-region ρ with 5-HT2A (no null) |", "|---|" + "---|" * (len(maps) + 1)]
    for cell in CELLS:
        d = load(cell)
        vals = []
        for m in maps:
            r = get(d, "spatial_spin_cortical99", f"rho_{m}")
            bh = re.search(r"BH\(5\) sig=(\d)", str(r.note)).group(1)
            vals.append(f"{r.value:+.3f} ({r.p:.5f}; {'sig' if bh == '1' else 'ns'})")
        r115 = get(d, "spatial_descriptive_115", "rho_5HT2A_incl_subcortex_no_p")
        L.append(f"| {cell_name(cell)} | " + " | ".join(vals) + f" | {r115.value:+.3f} |")
    return "\n".join(L)


def table_fdr_regions(cell):
    d = load(cell)
    sub = d[d.section == "regional_did_fdr_regions"]
    if sub.empty:
        return f"{cell_name(cell)}: no region survives BH FDR."
    L = [f"**{cell_name(cell)}** — regions surviving BH FDR q = 0.05 ({len(sub)}), by network", "", "| network | regions (DiD, sign-flip p) |", "|---|---|"]
    netnum = {1: "Vis", 2: "SomMot", 3: "DorsAttn", 4: "SalVentAttn", 5: "Limbic", 6: "Cont", 7: "Default", 8: "Subcortex"}
    groups = {}
    for _, r in sub.iterrows():
        n = int(re.search(r"net=(\d)", str(r.note)).group(1))
        groups.setdefault(netnum[n], []).append(f"{r['name']} ({f4(r.value)}, {r.p:.4f})")
    for n in NETS:
        if n in groups:
            L.append(f"| {n} ({len(groups[n])}) | " + "; ".join(groups[n]) + " |")
    return "\n".join(L)


def table_map_stats():
    L = ["| cell | SD of group-mean DiD across regions | range (min, max) | region with smallest p |", "|---|---|---|---|"]
    for cell in CELLS:
        d = load(cell)
        sd, rg, mp = get(d, "regional_did", "sd_of_groupmean_did_across_regions"), get(d, "regional_did", "range_of_groupmean_did_across_regions"), get(d, "regional_did", "min_uncorrected_p")
        L.append(f"| {cell_name(cell)} | {sd.value:.4f} | {rg.value:.4f} ({rg.note}) | {mp.note} (p = {mp.value:.4f}) |")
    return "\n".join(L)


def validation_table():
    log = (RR / "logs" / "phiid_fast_validate.log").read_text().splitlines()
    L = ["| check | max abs difference |", "|---|---|"]
    for line in log:
        m = re.match(r"\s+\((\d)\) (.*?)\s+max\|diff\| = ([0-9.e+-]+)", line)
        if m:
            L.append(f"| ({m.group(1)}) {m.group(2).strip()} | {m.group(3)} |")
        m2 = re.match(r"\s+max\|diff\| over 200 draws × 16 atoms = ([0-9.e+-]+)", line)
        if m2:
            L.append(f"| (6) 200 random (subject, run, window, pair) draws vs phyid.calc_PhiID, all 16 atoms | {m2.group(1)} |")
    loc = (RR / "logs" / "phiid_fast_validate_local.log").read_text().strip() if (RR / "logs" / "phiid_fast_validate_local.log").exists() else ""
    m3 = re.search(r"max\|diff\| = ([0-9.e+-]+)", loc)
    if m3:
        L.append(f"| (7) TR-local pair-mean atom series vs saved atoms_win60_local / atoms_bins_local (4 runs × 3 windows + 4 global) | {m3.group(1)} |")
    return "\n".join(L)


def _phir_w60():
    sys.path.insert(0, str(HERE))
    from rev_phiid_fast import phir
    out = {}
    for series, base in (("deconv", RR / "deconv"), ("raw", HERE.parent / "results")):
        for var in ("ts_gsr", "ts_demean"):
            A = np.load(base / f"atoms_win60_115regions-all_{var}_window.npy")
            out[(series, var)] = phir(A)
    return out


def table_subjects():
    P = _phir_w60()
    PRE, POST = np.arange(0, 4), np.arange(5, 14)
    L = ["| subject | " + " | ".join(f"{s} {v}: DMT Δ / PCB Δ / DiD" for s, v in (("deconv", "ts_gsr"), ("deconv", "ts_demean"), ("raw", "ts_gsr"), ("raw", "ts_demean"))) + " |",
         "|---|---|---|---|---|"]
    stats = {}
    for key, X in P.items():
        ch = X[:, :, POST].mean(2) - X[:, :, PRE].mean(2)
        stats[key] = (ch, ch[:, 0] - ch[:, 1])
    for i in range(14):
        cells = []
        for key in (("deconv", "ts_gsr"), ("deconv", "ts_demean"), ("raw", "ts_gsr"), ("raw", "ts_demean")):
            ch, d = stats[key]
            cells.append(f"{ch[i, 0]:+.4f} / {ch[i, 1]:+.4f} / **{d[i]:+.4f}**")
        L.append(f"| {i + 1} | " + " | ".join(cells) + " |")
    cells = []
    for key in (("deconv", "ts_gsr"), ("deconv", "ts_demean"), ("raw", "ts_gsr"), ("raw", "ts_demean")):
        ch, d = stats[key]
        cells.append(f"{ch[:, 0].mean():+.4f} ({int((ch[:, 0] > 0).sum())} rise) / {ch[:, 1].mean():+.4f} ({int((ch[:, 1] < 0).sum())} fall) / **{d.mean():+.4f}** ({int((d > 0).sum())} pos; median {np.median(d):+.4f})")
    L.append("| mean (count/14) | " + " | ".join(cells) + " |")
    return "\n".join(L)


def table_windows():
    P = _phir_w60()
    L = ["| series | run | " + " | ".join(f"w{w}" for w in range(1, 15)) + " | pre 1–4 | 5 | 6–9 | 10–14 |", "|---|---|" + "---|" * 18]
    for key in (("deconv", "ts_gsr"), ("deconv", "ts_demean"), ("raw", "ts_gsr"), ("raw", "ts_demean")):
        X = P[key]
        for c, cn in enumerate(("DMT", "PCB")):
            m, se = X[:, c].mean(0), X[:, c].std(0, ddof=1) / np.sqrt(14)
            L.append(f"| {key[0]} {key[1]} | {cn} | " + " | ".join(f"{a:.4f} ({b:.4f})" for a, b in zip(m, se)) +
                     f" | {m[:4].mean():.4f} | {m[4]:.4f} | {m[5:9].mean():.4f} | {m[9:].mean():.4f} |")
    return "\n".join(L)


if __name__ == "__main__":
    print(validation_table(), "\n")
    print(table_prediction(), "\n")
    print(table_cells(), "\n")
    print(table_networks(), "\n")
    print(table_spin(), "\n")
    print(table_map_stats(), "\n")
    for cell in CELLS[:2]:
        print(table_fdr_regions(cell), "\n")
