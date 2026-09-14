# DMT ΦID Project

Secondary analysis of open DMT fMRI data (Timmermann et al. PNAS 2023;
data from Singleton et al. Commun Biol 2025, `singlesp/DMT_NCT`), applying
Integrated Information Decomposition (ΦID, Gaussian, MMI redundancy, τ = 1)
to test whether whole-brain synergistic information is up-regulated under
DMT and tracks subjective intensity. Produced as evidence of computational
neuroimaging competence for a PhD application to the Cognition and
Consciousness Imaging Group, Division of Anaesthesia, University of
Cambridge (Prof. Emmanuel Stamatakis).

## Deadlines

- **20 Nov 2026** — public preprint + documented repo
- **8 Dec 2026** — Cambridge application (Gates Cambridge / Cambridge Trust)

## Current state (14 Sep 2026)

**Analysis complete. Draft written. Figures built.**

- Primary result (Primary B, windowed W = 60 estimator, ts_gsr, replicated
  on ts_demean): whole-brain synergy **decreases** under DMT, DiD negative
  and significant on both nulls, survives motion control. **This refutes
  the pre-specified directional hypothesis** and is reported as a
  refutation, never reframed. Tier-2 intensity tracking is **void** under
  the pre-specified controls; the claimed tier is **3** (step contrast +
  methods contribution).
- Robustness A (global fit), C (placebo-fitted model), the W = 30 positive
  control, the bias characterisation, the LZ comparison, global FC per
  bin, subject-alignment check and the exploratory regional / receptor /
  workspace analysis are all run and recorded.
- Remaining work is writing, not analysis: finish `manuscript/draft.md`,
  confirm data reuse terms, ask the data authors to confirm subject order
  (see the open questions at the end of the record).

## Post-hoc robustness checks (NOT pre-specified; recorded here, not in the record)

These were specified after the primary result existed and are labelled
post-hoc wherever they are reported. They decide nothing.

- **Leave-one-out on the primary DiD (14 Sep 2026; `scripts/13_loo_did.py`
  at git 17dbfcb, `results/loo_did_win60.csv`, log
  `results/run_13_loo_did.log`).** Raw whole-brain sts DiD, W = 60, primary
  windows 6–14 vs 1–4, each subject dropped in turn (13-subject refits;
  bootstrap CI 10,000 draws, exact sign-flip over 2^13, seed 20261120).
  Motivation: subject 8 carries −0.280 (ts_gsr) / −0.311 (ts_demean)
  against group means of −0.081 / −0.103, and subject 14 is the only
  positive DiD on both variants. The full-sample refit reproduces the
  recorded values (−0.0809, −0.1031). Range of the leave-one-out mean:
  **ts_gsr −0.0944 to −0.0656, ts_demean −0.1182 to −0.0871** (least
  negative when subject 8 is dropped, most negative when subject 14 is
  dropped, on both variants). **No leave-one-out CI includes zero on
  either variant (0 of 28)**; sign-flip p ≤ 0.0076 in every refit.
  **Dropping subject 8: ts_gsr −0.0656 [−0.1013, −0.0271], p = 0.0076,
  negative in 12 of 13; ts_demean −0.0871 [−0.1310, −0.0408], p = 0.0051,
  negative in 11 of 13.** Dropping subject 14: −0.0944 [−0.1374, −0.0574],
  p = 0.0002; −0.1182 [−0.1675, −0.0730], p = 0.0005. The primary result
  does not depend on any single subject. Reported in the draft's Results
  in one sentence.

- **Proportionality of the synergy decrease (specified 14 Sep 2026,
  rule recorded BEFORE the run; `scripts/14_proportionality.py`,
  `results/proportionality.csv`).** Question: does DMT reduce synergy
  selectively or in proportion to the total TDMI reduction? Ratio
  sts / TDMI (TDMI = Σ 16 atoms) per subject, condition and window/bin;
  DiD of the ratio in the primary form (exact sign-flip, subject-bootstrap
  CI); four cells: windowed W = 60 (windows 6–14 vs 1–4) and global fit
  (bins 11–28 vs 1–8), each on ts_gsr and ts_demean. Also (i) sts share
  of TDMI at pre-injection baseline on DMT and (ii) sts share of the TDMI
  DiD, for direct comparison. **Rule:** ratio-DiD CI includes zero →
  synergy falls in proportion to total predictable information, no
  evidence of a selective effect; significantly negative → falls more
  than proportionally; significantly positive → less. **The directional
  refutation of the up-regulation hypothesis stands under all three
  outcomes; it concerns sign, not selectivity.** Outcome: see below once
  run.

## The record: `manuscript/analysis_record.md`

**`manuscript/analysis_record.md` is the full pre-specification and results
record.** It was the project `CLAUDE.md` until 14 Sep 2026, when it was
moved with `git mv` (byte-identical; `git log --follow` carries its
history). Its value is that every decision, prediction and rule in it was
committed before the result it governs existed, and the commit sequence is
the audit trail (`manuscript/prespecification_summary.md` lists the
decisions by SHA).

**It must never be retroactively edited, reorganised or condensed.** New
decisions, results or corrections are appended as new dated entries, never
written into existing ones. If something in it is wrong, append a dated
correction that says so and leaves the original in place. Read the relevant
section of it before touching any script or result.

## Repository layout

```
CLAUDE.md                        this file: orientation and standing rules
manuscript/analysis_record.md    pre-specification + results record (append-only)
manuscript/prespecification_summary.md  decisions by commit, changed-later audit
manuscript/draft.md              the paper
manuscript/supplementary.md      supplementary tables, values quoted from results/
manuscript/figures/              fig1–3 (pdf/png) + captions.md, from 12_figures.py
scripts/                         numbered by execution order, each independently runnable
  00_verify.py                   data + method integrity check; run after any env change
  01_synergy_timecourse.py       all 16 ΦID atoms per pair, whole-brain mean per bin/window
                                 (--fit-mode global|window|placebo, --variant ts_gsr|ts_demean)
  02_bias_check.py               finite-sample bias on simulated VAR(1), stationary + non-stationary
  03_lz_vs_tdmi.py               total TDMI vs EEG Lempel-Ziv regressor
  04_logdet_correction_check.py  decision-tree step 2 (analytic log-det correction)
  05_tier_check_decay_windows.py tier statistics on windows 6–14 from the bias-check tables
  06_primary_b_analysis.py       Primary B inference: step contrast, nulls, motion, tier-2 controls
  07_windowed_atoms_did.py       rtr / total / self-transfer atoms, windowed vs global
  08_robustness_c_analysis.py    Robustness C inference
  09_global_fc_per_bin.py        mean pairwise r per bin, both variants
  10_subject_alignment_check.py  is the subject axis shared across data files?
  11_regional_analysis.py        EXPLORATORY: per-region DiD, spin tests, workspace proxy
  12_figures.py                  manuscript figures, regenerable from results/
results/                         every table/array with script + git SHA in its header;
                                 run_*.log are the run logs; nonstat_*/ are bias-check sub-runs
data/                            Schaefer-100 parcel LUT only (all fMRI data is in external/)
external/DMT_NCT/                git clone of singlesp/DMT_NCT (git-ignored, not a submodule): data + original MATLAB
figs/                            empty; figures live in manuscript/figures/
requirements.lock.txt            pinned environment (.venv/bin/python)
```

Data facts (shapes, indexing, TR, condition axis, defects, region-20
exclusion) are in the record under "Data" and "Region exclusion"; do not
re-derive them. Key ones: `external/DMT_NCT/data/`; 14 subjects × 2
conditions, **index 0 = DMT, 1 = placebo**; (116 regions, 840 TRs), TR 2 s;
28 ratings = 30 TRs per bin; **region 20 (0-based) dropped everywhere →
115 regions, 6,555 pairs**; subject index 2 PCB TR 839 is NaN.

## Standing methodological rules

These govern any new work and are what a Cambridge reviewer will check
first.

1. **Spatial nulls.** Brain-map correlations use spin tests (cortical
   parcels only; subcortex has no spin null and gets a descriptive ρ
   without p) or BrainSMASH. Never naive parametric p-values.
2. **Temporal nulls.** Phase-randomised surrogates for any synergy-vs-
   intensity or synergy-vs-time-course correlation.
3. **No double-dipping.** Never select regions on an effect and re-test
   them on the same data. The FDR-surviving regions from the exploratory
   analysis are not to be selected for any further test.
4. **Motion.** Report FD, residualise, test survival under the definition
   fixed in the record (same sign, bootstrap CI excludes zero).
5. **N = 14.** Effect sizes with CIs, exact sign-flip tests, proof-of-
   concept framing. Never "established".
6. **Preprocessing sensitivity.** Every result on `ts_gsr` (primary) and
   `ts_demean` (sensitivity) at minimum.
7. **FDR** across regions/edges/maps, Benjamini–Hochberg, stated
   explicitly.
8. **Reproducibility.** `SEED = 20261120` everywhere; git SHA in every
   output header (scripts tag `-dirty` if `scripts/` or the record have
   uncommitted changes); every figure regenerable from a single script;
   no manual figure editing.
9. **Directional honesty.** The hypothesis was directional (synergy up).
   The observed decrease is a refutation. Do not reframe it. Tier-2 claims
   stay void; the tier-2 numbers are reported with the void verdict.
10. **Luppi et al. eLife 2024 comparison.** Licensed only as a
    dissociation (workspace-concentrated collapse under propofol/DoC vs a
    spatially uniform DMT decrease), qualified by the network-proxy
    limitation. "Synergy falls under DMT as it does under propofol" is not
    a licensed sentence.
11. **Pre-specify before computing.** Any new analysis gets a dated entry
    appended to the record, with predictions if any, before the first
    number is produced. Exploratory work is labelled exploratory in every
    table and figure and reported regardless of outcome.

## Working conventions

- Python only (`scipy.io.loadmat` for the `.mat` files); no MATLAB.
- `phyid` is not on PyPI: `pip install
  git+https://github.com/Imperial-MIND-lab/integrated-info-decomp.git`.
- Full pairwise run ≈ 9 min single-core per variant and fit mode.
- Commit scripts before running them for a reportable result so the
  output header carries a clean SHA; record the SHA with the result.
- Results written to `results/` and never hand-edited; the record and the
  manuscript quote them verbatim from the named file.

## Open questions

Listed at the end of `manuscript/analysis_record.md`. The two that block
the preprint: reuse licence (no LICENSE in the source repo; cite Singleton
et al. 2025 and Zenodo 10.5281/zenodo.15177511) and author confirmation of
the subject ordering across files.
