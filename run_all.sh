#!/usr/bin/env bash
# run_all.sh — regenerate every table and figure from the raw .mat files, in dependency order.
#
# WARNING: this takes HOURS. Measured single-core wall-clock from the run logs in results/:
#   01 global fit                ~530 s per variant  (x2)          ~18 min
#   01 windowed W=60             ~3,030 s per variant (x2)         ~1 h 41 min
#   01 windowed W=30 (control)   ~5,820 s                          ~1 h 37 min
#   01 placebo-fitted (Rob. C)   ~280 s                            ~5 min
#   02 bias check, 20,000 runs   ~7,180 s                          ~2 h
#   02 AR-shift step, 2,000 runs ~100 s                            ~2 min
#   11 regional (per-pair refit) ~540 s per variant (x2)           ~18 min
#   everything else              seconds to a few minutes each
#   TOTAL                        ~6 h single-core (≈ 21,000 s), no GPU, ~2 GB RAM.
# Every script is deterministic (SEED = 20261120) and writes the git SHA of the tree into
# its output header; commit before running so the headers are clean, not "-dirty".
#
# Inputs: external/DMT_NCT/data/*.mat (git submodule; see README.md) and data/*.lut.
# Outputs: results/*.csv, results/*.npy, results/run_*.log, manuscript/figures/*.
# Not regenerated (superseded sanity runs kept for the record): results/synergy_bins_20regions_*,
# results/synergy_bins_115regions-all_ts_gsr_global.*, results/nonstat_n20000/ (aborted 12 Sep run),
# results/tier_check_decay_windows_n2000_18ad8b4.csv (dry run on the 2,000-run tables at commit 18ad8b4).
#
# Usage:  bash run_all.sh            (PYTHON=... to override the interpreter; default .venv/bin/python)
set -euo pipefail
cd "$(dirname "$0")"
PYTHON="${PYTHON:-.venv/bin/python}"
mkdir -p results manuscript/figures
T0=$(date +%s)
step() {  # step <log-name> <script> [args...]
    local log="results/run_$1.log"; shift
    echo "=== $(date '+%F %T')  $*   -> $log"
    "$PYTHON" -u "$@" 2>&1 | tee "$log"
}

# 0. data and method integrity (fails fast if the submodule or phyid is missing)
step 00_verify                      scripts/00_verify.py

# 1. bias characterisation on simulated data (touches no real data); 04 and 05 read its tables
step 02_bias_check_n20000           scripts/02_bias_check.py --n-runs 20000
step nonstat_ar_step                scripts/02_bias_check.py --only-nonstat nonstat_step_ar --out results/nonstat_ar_step --n-runs 2000
step logdet_correction_check        scripts/04_logdet_correction_check.py
step tier_check_decay_windows       scripts/05_tier_check_decay_windows.py --tables-dir results

# 2. whole-brain PhiID atoms on the real data (the slow part)
step 115_global_atoms               scripts/01_synergy_timecourse.py --fit-mode global  --variant ts_gsr
step 115_global_atoms_ts_demean     scripts/01_synergy_timecourse.py --fit-mode global  --variant ts_demean
step primary_b_win60_ts_gsr         scripts/01_synergy_timecourse.py --fit-mode window  --window-trs 60 --variant ts_gsr
step primary_b_win60_ts_demean      scripts/01_synergy_timecourse.py --fit-mode window  --window-trs 60 --variant ts_demean
step primary_b_win30_ts_gsr         scripts/01_synergy_timecourse.py --fit-mode window  --window-trs 30 --variant ts_gsr
step robustness_c_placebo_ts_gsr    scripts/01_synergy_timecourse.py --fit-mode placebo --variant ts_gsr

# 3. inference on the saved atoms
step 06_ts_gsr_win60                scripts/06_primary_b_analysis.py --variant ts_gsr    --window-trs 60
step 06_ts_demean_win60             scripts/06_primary_b_analysis.py --variant ts_demean --window-trs 60
step 06_ts_gsr_win30                scripts/06_primary_b_analysis.py --variant ts_gsr    --window-trs 30
step 07_ts_gsr_win60                scripts/07_windowed_atoms_did.py --variant ts_gsr --window-trs 60
step 08_robustness_c_ts_gsr         scripts/08_robustness_c_analysis.py --variant ts_gsr
step lz_vs_tdmi_ts_gsr              scripts/03_lz_vs_tdmi.py --variant ts_gsr
step lz_vs_tdmi_ts_demean           scripts/03_lz_vs_tdmi.py --variant ts_demean
step 09_ts_gsr                      scripts/09_global_fc_per_bin.py --variant ts_gsr
step 09_ts_demean                   scripts/09_global_fc_per_bin.py --variant ts_demean
step 10_subject_alignment_check     scripts/10_subject_alignment_check.py
step 13_loo_did                     scripts/13_loo_did.py

# 4. exploratory regional analysis (recomputes the per-pair atoms with the global fit)
step 11_ts_gsr                      scripts/11_regional_analysis.py --variant ts_gsr
step 11_ts_demean                   scripts/11_regional_analysis.py --variant ts_demean

# 5. figures, from saved results only
step 12_figures                     scripts/12_figures.py

echo "=== all done in $(( ($(date +%s) - T0) / 60 )) min"
