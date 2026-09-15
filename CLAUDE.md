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

## Current state (15 Sep 2026)

**Analysis complete. The paper is `manuscript/draft_v2.md` (revised 15 Sep after the second and third adversarial reviews); `manuscript/draft.md` is the superseded first draft, kept as a record. Figures `fig1_v2`–`fig4_v2` built by `scripts/15_figures_v2.py`.**

- Primary result (Primary B, windowed W = 60 estimator, ts_gsr, replicated
  on ts_demean): whole-brain synergy **decreases** under DMT, DiD negative
  and significant on both nulls, survives motion control. **This refutes
  the pre-specified directional hypothesis** and is reported as a
  refutation, never reframed. Tier-2 intensity tracking is **void** under
  the pre-specified controls; the claimed tier is **3** (step contrast +
  methods contribution).
- The two adversarial reviews of 14 and 15 Sep and the Part B analyses
  (dated entries in the record; `notes/partB_prespec_2026-09-14.md`)
  reframed the paper as an account of the estimator: the sts decrease is
  reproduced by the lag-1 autocorrelation change (per-subject r = 0.95),
  with a residual not accounted for by a stationary finite-sample null and
  a CCS-sts increase that stays exploratory (record, "Closure entry" and
  "Correction note, 15 Sep 2026"). The third review's findings and the
  changes made in response are in the correction note.
- Data reuse: agreed with the data collectors and the derivative authors by
  email in September 2026, with attribution [TK: attach the written
  confirmation]. Subject order across files verified at one subject
  (record, "Subject alignment across files"); author confirmation still
  requested.
- Remaining work: the [TK] items in `draft_v2.md` (affiliations, co-authors,
  reference details, journal wording); delete `manuscript/draft_v2-1.md`,
  an earlier variant with a different author list and abstract.

## Post-hoc checks (NOT pre-specified; recorded here, not in the record)

Specified after the primary result, labelled post-hoc wherever reported,
reported regardless of outcome. They decide nothing. Full numbers in the
named CSVs.

- **Leave-one-out on the primary DiD (14 Sep 2026; `13_loo_did.py` at
  17dbfcb, `results/loo_did_win60.csv`).** Raw W = 60 primary DiD, each
  subject dropped in turn. LOO mean range ts_gsr −0.0944 to −0.0656,
  ts_demean −0.1182 to −0.0871; **no LOO CI includes zero (0 of 28)**,
  p ≤ 0.0076 throughout. Subject 14 (only positive DiD) is the most
  influential: dropping it strengthens the effect. Dropping subject 8
  (largest magnitude): ts_gsr −0.0656 [−0.1013, −0.0271], p = 0.0076;
  ts_demean −0.0871 [−0.1310, −0.0408], p = 0.0051. No single subject
  carries the result. One sentence in the draft's Results.
- **Proportionality of the synergy decrease (14 Sep 2026; rule recorded
  at dbf2311 BEFORE the run; `14_proportionality.py`,
  `results/proportionality.csv`).** Ratio sts / TDMI (Σ 16 atoms) per
  subject, condition, window/bin; DiD of the ratio in the primary form.
  **Rule (fixed before running):** ratio-DiD CI includes zero →
  proportional, no evidence of a selective synergy effect; significantly
  negative → more than proportional; positive → less. The directional
  refutation stands under all three outcomes (sign, not selectivity).
  **Outcome:**

  | cell | ratio DiD [CI], p | verdict | (i) baseline share | (ii) share of TDMI DiD |
  |---|---|---|---|---|
  | W = 60, ts_gsr | +0.0005 [−0.0081, +0.0083], 0.91 | proportional | 0.782 | 0.780 [0.653, 0.936] |
  | W = 60, ts_demean | −0.0095 [−0.0235, +0.0049], 0.22 | proportional | 0.767 | 0.870 [0.691, 1.006] |
  | global, ts_gsr | **+0.0204 [+0.0048, +0.0340], 0.025** | **less than proportional** | 0.908 | 0.658 [0.486, 0.817] |
  | global, ts_demean | +0.0071 [−0.0167, +0.0292], 0.56 | proportional | 0.897 | 0.787 [0.500, 1.013] |

  Under the primary estimator (W = 60) on both variants, synergy falls in
  proportion to total predictable information: sts is ~78 % of TDMI at
  baseline and carries ~78–87 % of the TDMI drop. The global fit on
  ts_gsr is the one cell with a significant ratio DiD, positive, i.e.
  sts falls *less* than proportionally there (DMT post − pre +0.0167,
  p = 0.018; PCB −0.0037), not replicated on ts_demean. **No cell shows
  a more-than-proportional (selective) synergy reduction.** The
  windowed and global estimators put sts at different shares of TDMI
  (0.78 vs 0.90) because the per-window bias falls on sts and the
  self-transfer atoms differently. In the draft (Results, Discussion, Table S8).

## The record: `manuscript/analysis_record.md`

**`manuscript/analysis_record.md` is the full pre-specification and results
record.** It was the project `CLAUDE.md` until 14 Sep 2026, when it was
moved with `git mv` (byte-identical; `git log --follow` carries its
history). Every decision, prediction and rule in it was committed before the
result it governs existed; `manuscript/prespecification_summary.md` lists
them by SHA. **Never retroactively edit, reorganise or condense it.**
Corrections and new entries are appended, dated, with the original left in
place. Read the relevant section before touching a script or result.

## Repository layout

```
CLAUDE.md                        this file: orientation and standing rules
manuscript/analysis_record.md    pre-specification + results record (append-only)
manuscript/prespecification_summary.md  decisions by commit, changed-later audit
manuscript/draft_v2.md           the paper (15 Sep 2026)
manuscript/draft.md              superseded first draft, kept as a record
manuscript/supplementary.md      supplementary tables, values quoted from results/
manuscript/figures/              fig1_v2–fig4_v2 (pdf/png) + captions_v2.md, from 15_figures_v2.py;
                                 the draft.md figures + captions.md (12_figures.py) kept in place
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
  12_figures.py                  draft.md figures, regenerable from results/
  13_loo_did.py                  POST-HOC: leave-one-subject-out on the primary DiD
  14_proportionality.py          POST-HOC: sts / TDMI ratio DiD, four cells, rule in the docstring
  15_figures_v2.py               draft_v2.md figures, from results/ and notes/review_results/
notes/                           adversarial reviews, review computations (rev_*.py, review_*.py),
                                 Part B plans/notes/scripts (partB*.md, partB*.py); outputs under
                                 notes/review_results/ (tables, logs, inference rows, atom arrays)
results/                         every table/array with script + git SHA in its header;
                                 run_*.log are the run logs; nonstat_*/ are bias-check sub-runs
data/                            Schaefer-100 parcel LUT only (all fMRI data is in external/)
external/DMT_NCT/                git clone of singlesp/DMT_NCT (git-ignored, not a submodule): data + original MATLAB
requirements.lock.txt            pinned environment (.venv/bin/python)
```

Data facts are in the record ("Data", "Region exclusion"); do not
re-derive them. Key ones: 14 subjects × 2 conditions, **index 0 = DMT,
1 = placebo**; (116 regions, 840 TRs), TR 2 s; 28 ratings = 30 TRs per
bin; **region 20 (0-based) dropped everywhere → 115 regions, 6,555
pairs**; subject index 2 PCB TR 839 is NaN.

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
- `phyid` is not on PyPI; `requirements.lock.txt` pins its git commit.
- Commit scripts before running them for a reportable result so the
  output header carries a clean SHA; record the SHA with the result.
- `results/` is never hand-edited; the record and manuscript quote it
  verbatim. `run_all.sh` regenerates everything (≈ 6 h for the original
  analysis; about an hour more for the review and Part B section).

## Open questions

At the end of the record ("Open questions"), with the later dated entries
("Closure entry", "Part B, items 6–8", "Correction note, 15 Sep 2026")
after it. The data reuse terms were confirmed by email in September 2026
(README, "Licence"; the written confirmation is still to be attached);
author confirmation of the subject order is still requested.
