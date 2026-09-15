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
#   TOTAL, sections 0–5          ~6 h single-core (≈ 21,000 s), no GPU, ~2 GB RAM.
#   section 6 (review + Part B)  about an hour more (partB6 ≈ 15 min, partB2 ≈ 10 min, the matched
#                                null and the residual null a few minutes each; see each script's docstring)
# Every script is deterministic (SEED = 20261120) and writes the git SHA of the tree into
# its output header; commit before running so the headers are clean, not "-dirty".
#
# Inputs: external/DMT_NCT/data/*.mat (a plain clone of singlesp/DMT_NCT, git-ignored; see README.md) and data/*.lut.
# Outputs: results/*.csv, results/*.npy, results/run_*.log, manuscript/figures/*, and (section 6)
# notes/review_results/** — tables, logs, inference rows and atom arrays of the review and Part B computations.
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

# 0. data and method integrity (fails fast if the data clone or phyid is missing)
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

# 5. post-hoc proportionality check and the draft.md figures, from saved results only
step 14_proportionality             scripts/14_proportionality.py
step 12_figures                     scripts/12_figures.py

# 6. the review computations of 14 Sep 2026 and the Part B analyses of 14–15 Sep (notes/), in
#    dependency order, then the draft_v2.md figures. Added 15 Sep 2026: every script below was run
#    individually as recorded in notes/ and manuscript/analysis_record.md; this section has not yet
#    been executed end-to-end as one run. Scripts that write their own log under notes/review_results/
#    are run with nrun; the others are tee'd to notes/review_results/<path>.log under the names the
#    committed logs carry. The HRF-deconvolution items (review section 3, the closed ΦR exploration,
#    Supplement S2) need the sandbox described in notes/rev_deconv.py — the deconvolved .mat merged
#    under notes/review_results/deconv/ and scripts/01 rerun on it there — and are skipped unless it
#    is present.
nstep() {  # nstep <log path under notes/review_results, without .log> <script> [args...]
    local log="notes/review_results/$1.log"; shift
    echo "=== $(date '+%F %T')  $*   -> $log"
    "$PYTHON" -u "$@" 2>&1 | tee "$log"
}
nrun() {   # nrun <script> [args...]   (the script writes its own log and tables under notes/review_results/)
    echo "=== $(date '+%F %T')  $*"
    "$PYTHON" -u "$@"
}
mkdir -p notes/review_results/logs notes/review_results/partB
nstep logs/phiid_fast_validate      notes/rev_phiid_fast_validate.py
nstep logs/rev_run_raw              notes/rev_run.py raw
nstep logs/rev_extra                notes/rev_extra.py
nstep logs/sts_matched_null_F1      notes/rev_sts_matched_null.py f1
nstep logs/sts_matched_null_F2      notes/rev_sts_matched_null.py f2
nstep logs/sts_matched_null_F3      notes/rev_sts_matched_null.py f3
nstep logs/review_checks            notes/review_checks.py
DECONV_MAT="notes/review_results/deconv/DMT_clean_mni_continuous_fullPreprocsch116.mat"
if [ -f "$DECONV_MAT" ]; then
    nstep logs/rev_run_deconv       notes/rev_run.py deconv
    nstep logs/rev_phir_items       notes/rev_phir_items.py
    for s in deconv raw; do for v in ts_gsr ts_demean; do for e in win60 global; do
        nstep "logs/regional_${s}_${v}_${e}" notes/rev_regional_phir.py --series "$s" --variant "$v" --estimator "$e"
    done; done; done
    nrun notes/rev_regional_note.py
else
    echo "=== skipping the HRF-deconvolution items: $DECONV_MAT not present (see notes/rev_deconv.py)"
fi
nrun notes/rev_assemble.py
nstep partB/scope_map_run           notes/partB1_scope_map.py
nstep partB/overlay_points_run      notes/partB1_overlay_points.py
nrun notes/partB2_ccs_verify.py
nrun notes/partB2_ccs_run.py
nrun notes/partB3_lag.py
nrun notes/partB4_diagnostic.py
nrun notes/partB4_residual_source.py
nrun notes/partB5_family_checks.py
nrun notes/partB6_ccs_definition.py
nrun notes/partB7_splithalf.py
nstep partB/coupling_map_run        notes/partB8_coupling_map.py
nstep logs/review_v2_residual_null  notes/review_v2_residual_null.py
nrun notes/partB9_leave_two_out.py
nstep partB/crosslag_deviation_run  notes/partB10_crosslag_deviation.py
nstep partB/regional_sts_r1_run     notes/partB11_regional_sts_r1.py
step 15_figures_v2                  scripts/15_figures_v2.py

echo "=== all done in $(( ($(date +%s) - T0) / 60 )) min"
