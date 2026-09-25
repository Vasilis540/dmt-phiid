# S4 Text. The COBIDAS reporting checklist for MRI, filled for this secondary analysis

Supporting information for the paper "The Gaussian-MMI synergy atom of integrated information decomposition is mostly self-prediction". The items follow the OHBM Committee on Best Practices in Data Analysis and Sharing report for MRI (COBIDAS, OHBM 2016; summarised in Nichols et al., 2017, *Nature Neuroscience* 20, 299–303), sections D (experimental design), A (acquisition), P (preprocessing), S (statistical modelling and inference), R (results) and Sh (data sharing); the item wording is paraphrased from the report's checklist, and the numbering is the report's section order, not its exact item numbers. This paper is a secondary analysis of pseudonymised, parcellated, preprocessed regional time series released by the data authors (Singleton et al., 2025; acquired by Timmermann et al., 2023): no data were collected and no image was processed here, so every acquisition and image-preprocessing item is answered by pointing to the data authors' reports, and "not applicable" below always means "not done in this study; reported by the data authors where the item applies to their acquisition". Status codes: **reported** (with the location in the main text or the supporting information), **not applicable** (with the reason), **not reported** (with what is missing). Locations name the sections of the main text (Results 1–7 and the subsections of Materials and methods) and the supporting files as they stand in the revision of 25 September 2026.

## D. Experimental design

| Item | Status | Where / what |
|---|---|---|
| D1 Number of subjects analysed | reported | Methods, Dataset: fourteen subjects, each with a DMT run and a placebo run; N = 14 in every inference. |
| D2 Sample size determination | not applicable | Secondary analysis of a released dataset; the sample is the 14 subjects the data authors retained. No power analysis was possible or performed; Limitations states "One dataset, one drug, one parcellation, N = 14". |
| D3 Sampling frame and recruitment | not applicable | Reported by Timmermann et al. (2023). |
| D4 Inclusion and exclusion criteria | not applicable (recruitment); reported (analysis) | Recruitment criteria: Timmermann et al. (2023). Exclusions at the data-release stage: Methods, Dataset — "six of twenty excluded for head movement by Singleton et al., 2025". No subject was excluded by this study. |
| D5 Demographics (age, sex, handedness) | not reported | Not stated in this paper for the 14 analysed subjects; the derivatives carry no demographic fields. Timmermann et al. (2023) report the demographics of the 20 recruited participants. |
| D6 Task / paradigm specification | reported | Methods, Dataset and S1 Text: continuous task-free session of 840 TRs, intravenous injection at TR 240 (20 mg DMT fumarate over 30 s); placebo run of the same form; intensity ratings (once per 30 TRs) collected in a later session of the same day and used in no main-text result. Instructions to participants (eyes closed or open) are not restated here: Timmermann et al. (2023). |
| D7 Design timing and event structure | reported | Methods, Inference: pre-injection windows 1–4, post windows 6–14 (primary), window 5 excluded; W = 60 TRs (2 min) per window; the rating bins of 30 TRs are in S1 Text. |
| D8 Number of runs and run order | reported | Methods, Dataset: one DMT run and one placebo run per subject (order and blinding as in Timmermann et al., 2023, not restated; S1 Text gives the counterbalancing). |
| D9 Behavioural performance | not applicable | No behavioural task; the subjective intensity ratings are described (S1 Text; S2 Table) and enter no main-text result. |

## A. Acquisition

| Item | Status | Where / what |
|---|---|---|
| A1 Subject preparation (head restraint, mock scanning, instructions) | not applicable | Timmermann et al. (2023). |
| A2 MRI system (vendor, model, field strength, coil) | not applicable; partly reported | S1 Text gives the field strength (3 T) and Methods, Dataset the TR (2 s), as stated by the data authors; vendor, model and coil: Timmermann et al. (2023). |
| A3 Pulse sequence and parameters (TE, flip angle, FOV, matrix, voxel size, slices, acceleration, phase encoding, number of volumes) | not applicable; partly reported | Number of volumes (840) and TR (2 s): Methods, Dataset. All other parameters: Timmermann et al. (2023). |
| A4 Structural acquisition | not applicable | Timmermann et al. (2023). |
| A5 Physiological recording (cardiac, respiratory) and EEG | not applicable | Simultaneous EEG was recorded by the source study (Timmermann et al., 2023); an HRF-convolved EEG Lempel–Ziv regressor is released with the data and is used only in the original pre-specified analysis (S1 Text, S6 Table), not in the main text. |
| A6 Preliminary quality control (motion, incidental findings) | not applicable; partly reported | Exclusion of six subjects for head movement by the data authors: Methods, Dataset. Framewise displacement per TR is released with the data and used for motion control here (Methods, Inference). |

## P. Preprocessing (image processing was done by the data authors; the items below describe the released derivatives as used here)

| Item | Status | Where / what |
|---|---|---|
| P1 Preprocessing software and versions | not applicable | Timmermann et al. (2023); Singleton et al. (2025). Not restated. |
| P2 Distortion, slice-timing and motion correction | not applicable | Timmermann et al. (2023); Singleton et al. (2025). |
| P3 Intra- and inter-subject registration, template | not applicable | Timmermann et al. (2023); Singleton et al. (2025). The parcellation is applied in MNI space by the data authors. |
| P4 Spatial smoothing | not applicable | Timmermann et al. (2023); Singleton et al. (2025). |
| P5 Temporal filtering | reported | Methods, Dataset: the released series are band-limited to 0.01–0.08 Hz; the consequence for lag-1 autocorrelation (r₁ ≈ 0.82 for white noise at TR = 2 s, and r₁ ≥ 0.54 for any series confined to the band) is stated in Results 7 and S1 Text. |
| P6 Nuisance regression and denoising (motion parameters, CompCor, scrubbing, global signal) | reported for what varies here; otherwise not applicable | Two released variants are analysed and named at every result: with global signal regression (`ts_gsr`, primary) and demeaned without it (`ts_demean`, sensitivity) — Methods, Dataset. The remaining denoising steps are the data authors' (Timmermann et al., 2023; Singleton et al., 2025). HRF deconvolution (rsHRF 1.7.0) was applied here only as a post hoc exploration (Methods, Remedies; S2 Text, which gives its parameters). |
| P7 Parcellation / atlas | reported | Methods, Dataset: Schaefer-100 parcels plus 16 subcortical ones; one region, mean-filled for one subject and confirmed as such by the data authors, dropped for all subjects and both conditions (S1 Text names it), leaving 115 regions and 6,555 pairs. |
| P8 Data quality checks on the derivatives | reported | S1 Text: one non-finite TR dropped; subject alignment across files checked (record, "Subject alignment across files"); `scripts/00_verify.py` checks shapes and finiteness before every run. |
| P9 Motion quantification and handling | reported | Methods, Inference: window-mean framewise displacement regressed out within each subject and condition and the DiD recomputed on the residuals (S1 Text); the FD DiD itself and the FD-residualised DiD are reported (Table 2). |

## S. Statistical modelling and inference

| Item | Status | Where / what |
|---|---|---|
| S1 Dependent variables and estimator | reported | Methods, Estimator and Redundancy functions: Gaussian ΦID atoms (`phyid`, commit pinned), MMI and CCS redundancy, whole-brain pair means; windowed (W = 60, W = 30) and global-fit estimators; the second implementation of the estimator and its validation. |
| S2 Model of temporal autocorrelation | reported | The estimator's dependence on lag-1 autocorrelation is the subject of the paper (Methods, The closed form; Results 1–5); the effective sample size per window (about 18) is stated in Methods, Estimator, with its derivation in S3 Text §4. |
| S3 First-level (within-subject) model | reported | Methods, The primary contrast and the exploratory analyses; the per-subject difference-in-differences, (post − pre) on DMT minus (post − pre) on placebo, on window means, is defined at the head of Results. |
| S4 Second-level (group) model and inference | reported | Methods, Inference: exact sign-flip permutation over 14 subjects (16,384 assignments, two-sided); the inverted sign-flip interval (the pre-specified subject-bootstrap interval is in S17 Table); phase-randomised temporal null (1,000 surrogates; S1 Text); motion control. |
| S5 Multiple-comparison handling | reported | Methods, The primary contrast and the exploratory analyses: no correction; every quantity but the primary contrast is exploratory and reported without threshold language; the rows of S17 Table (932 quantities); no weighting rule (withdrawn; S5 Text §2). Exploratory regional FDR (BH) is in S1 Text (S3 Table). |
| S6 Pre-specification and deviations | reported | Methods, Pre-registration and deviations; S5 Text; record `manuscript/analysis_record.md`; `manuscript/prespecification_summary.md`; S19 Table lists every recorded prediction with its outcome and the post hoc computations the paper quotes; every post hoc or review computation is labelled at first mention. |
| S7 Functional-connectivity / network definition | reported | Methods, Estimator: nodes are the 115 parcels, "edges" are the 6,555 region pairs, quantities are whole-brain pair means of ΦID atoms; Results 1 states the per-pair operating point. |
| S8 Software and versions | reported | S1 Text (software versions): Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.1, `phyid` at commit 6c5f2e9d…, `requirements.lock.txt`; seed 20261120 throughout (Methods, Inference). |
| S9 Simulations and null models | reported | Methods, The AR(1)-substituted estimate and its calibration; S1 Text; S3 Text: VAR(1) bias check (2,000 replicate windows per cell; S1 Text; S3 Text §6), the calibration on both generators (S10 Table), the finite-sample null (a review computation; S3 Text §6), the sts-matched null (S3 Text §6; S16 Table), the coupled family (S3 Text §3); each with its provenance. |

## R. Results reporting

| Item | Status | Where / what |
|---|---|---|
| R1 Effect sizes with uncertainty | reported | Every contrast is given as a mean DiD with an inverted sign-flip 95 % interval and exact p (Tables 1–3; Results 2–6). |
| R2 Direction and magnitude relative to baseline | reported | Results 2: −7.0 % of the pre-injection DMT mean; Table 2 pre-injection means. |
| R3 Per-subject data | reported | Fig 3 (per-subject DiDs), negative-of-14 counts in every table, leave-one-out (Results 2; `results/loo_did_win60.csv`), leave-two-out (S3 Text §5) and leave-one-out on the cross-half relation (S3 Text §5). |
| R4 Figures with stated uncertainty | reported | Captions (in the main text; `manuscript/figures/captions_v2.md`) state what each band and whisker is (inverted sign-flip intervals; within-subject SEM) and which panels carry no uncertainty. |
| R5 Null and negative results | reported | Results 6 (ΦR null), Results 4, Results 5, S1 Text (void tier-2 verdict); S19 Table (every recorded prediction with its outcome, the misses included). |
| R6 Regional / spatial results | reported (exploratory) | S1 Text, S3–S5 Tables, with spin tests for cortical maps; labelled exploratory; Results 3 and S3 Text §4 for the regional sts–r₁ map. |
| R7 Limitations | reported | Discussion, Limitations. |

## Sh. Data and code sharing

| Item | Status | Where / what |
|---|---|---|
| Sh1 Raw data availability | not applicable | Raw images were not used and are not held; the data authors' release (https://github.com/singlesp/DMT_NCT; Zenodo 10.5281/zenodo.15177511) is cited in Methods, Dataset and Data and code availability. |
| Sh2 Derived data used | reported | Data and code availability: the released derivatives are cloned into `external/` and not redistributed; reuse terms confirmed by the data collectors and derivative authors. |
| Sh3 Analysis code | reported | Data and code availability: https://github.com/Vasilis540/dmt-phiid, pinned environment, every result table with its git SHA, `run_all.sh`. |
| Sh4 Results files and materials | reported | Every S table names its source file; `results/` and `notes/review_results/` are in the repository; `manuscript/main_text_numbers.csv` gives the source of every number of the main text. |
| Sh5 Ethics and consent for sharing | reported | Ethics statement (main text; S1 Text): approval of the original study, secondary analysis of pseudonymised derivatives; the subject codes of the released ratings table are stated (S1 Text); no new data, no participant contacted. |
| Sh6 Pre-registration / analysis plan | reported | `manuscript/analysis_record.md` (git-tracked, append-only) and `manuscript/prespecification_summary.md`; Methods, Pre-registration and deviations; S19 Table; the record establishes "ordering, not blindness". |

## Items not reported in this paper, collected

D5 demographics of the 14 analysed subjects (available for the 20 recruited in Timmermann et al., 2023; not carried by the derivatives); the participant instructions for the resting-state session (Timmermann et al., 2023); every acquisition parameter beyond field strength, TR and the number of volumes (Timmermann et al., 2023); every image-preprocessing step beyond the band-pass, the global-signal variants and the parcellation (Timmermann et al., 2023; Singleton et al., 2025). None of these was available to, or altered by, this analysis.

## Reference

Nichols, T. E., Das, S., Eickhoff, S. B., Evans, A. C., Glatard, T., Hanke, M., Kriegeskorte, N., Milham, M. P., Poldrack, R. A., Poline, J.-B., Proal, E., Thirion, B., Van Essen, D. C., White, T., & Yeo, B. T. T. (2017). Best practices in data analysis and sharing in neuroimaging using MRI. *Nature Neuroscience*, 20(3), 299–303. https://doi.org/10.1038/nn.4500 (bibliographic record checked against Crossref on 24 September 2026; not read in full)
