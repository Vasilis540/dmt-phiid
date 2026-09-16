"""
audit_bundle15.py — arithmetic behind items (i)–(iv) of the round-7 correction note (planning session, 16 Sep 2026).
Inputs are numbers printed in notes/review_results/partB/crosslag_deviation_tables.md at 9a19b10 (bundle 15) and in
the reviewer logs of this folder (v_null_qshape.log, v_null_periodic.log). No data were touched.
"""
import numpy as np

# --- bundle 15, crosslag_deviation_tables.md (ts_gsr) ---
run, run_dmt, run_pcb = 0.00340, 0.00381, 0.00299            # sign(q)-weighted, run level; grand mean, DMT run, placebo run
w60, w60_dmt, w60_pcb = 0.00611, 0.00615, 0.00608            # section A, W = 60, each window's own sign of q
null840 = 0.00025                                            # section B, homogeneous filter, W = 840 (mean |q̂| 0.222)
null60_h = 0.00348                                           # section B, homogeneous filter, W = 60
cells = dict(DMT_pre=0.00344, DMT_post=0.00311, PCB_pre=0.00325, PCB_post=0.00356)   # section B, four cells, W = 60
null60_cells = np.mean(list(cells.values()))
data_absq = 0.1945                                           # run-level mean pair |q|, ts_gsr

print(f"(ii) near-zero threshold fixed at 10:23: 0.1 x {run} = {0.1 * run:.5f}; null W=840 share F = {null840 / run:.3f}")
# reviewer generator (placebo fit, heterogeneity 0.5, T = 840): run-level sign(q)-weighted mean by q distribution
pts = {"N(0,0.22)  v_null_qshape": (0.183, 0.00039), "N(0,0.25)  v_null_periodic": (0.20452, 0.00033), "N(0,0.30)  v_null_qshape": (0.244, 0.00033)}
x = np.array([v[0] for v in pts.values()]); y = np.array([v[1] for v in pts.values()])
at = np.interp(data_absq, x, y)
print(f"(ii) Gaussian-q points (mean |q^|, delta_run): {pts}")
print(f"(ii) interpolated at the data's mean |q^| {data_absq}: {at:+.5f}, F = {at / run:.3f}")
print(f"(ii) Laplace 0.18 (mean |q^| 0.187): +0.00053, F = {0.00053 / run:.3f}; 30 % at q = 0 (mean |q^| 0.187): +0.00071, F = {0.00071 / run:.3f}")

print(f"(iv) writer's net ratios, net W60 over raw run: {(w60 - null60_h) / run:.3f} (homogeneous), {(w60 - null60_cells) / run:.3f} (cells)")
print(f"(iv) net over net: {(w60 - null60_h) / (run - null840):.3f}, {(w60 - null60_cells) / (run - null840):.3f}")

# (iii) run type. Null counterpart of each run's W = 60 mean: 4 pre windows at the pre cell, 10 post windows at the post cell.
null_dmt_run = (4 * cells["DMT_pre"] + 10 * cells["DMT_post"]) / 14
null_pcb_run = (4 * cells["PCB_pre"] + 10 * cells["PCB_post"]) / 14
d_run = run_dmt - run_pcb
d_w60_raw = w60_dmt - w60_pcb
d_w60_net = d_w60_raw - (null_dmt_run - null_pcb_run)
print(f"(iii) run-type difference DMT - PCB: run level {d_run:+.5f}; W60 raw {d_w60_raw:+.5f}; null cells' run-type difference {null_dmt_run - null_pcb_run:+.5f}; W60 net {d_w60_net:+.5f}")
gap_lo, gap_hi = d_run - d_w60_net, d_run - d_w60_raw
print(f"(iii) gap run level minus W60: {gap_lo:+.5f} (net) to {gap_hi:+.5f} (raw); share of the DMT run-level value {gap_lo / run_dmt:.2f}-{gap_hi / run_dmt:.2f}")
