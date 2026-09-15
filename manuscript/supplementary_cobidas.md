# Supplementary reporting checklist (COBIDAS) for `manuscript/draft_v2.md`

Companion to `manuscript/draft_v2.md` (Supplement S4). The items follow the OHBM Committee on Best Practices in Data Analysis and Sharing report for MRI (COBIDAS, OHBM 2016; summarised in Nichols et al., 2017, *Nature Neuroscience* 20, 299–303), sections D (experimental design), A (acquisition), P (preprocessing), S (statistical modelling and inference), R (results) and Sh (data sharing); the item wording is paraphrased from the report's checklist, and the numbering is the report's section order, not its exact item numbers. This paper is a secondary analysis of anonymised, parcellated, preprocessed regional time series released by the data authors (Singleton et al., 2025; acquired by Timmermann et al., 2023): no data were collected and no image was processed here, so every acquisition and image-preprocessing item is answered by pointing to the data authors' reports, and "not applicable" below always means "not done in this study; reported by the data authors where the item applies to their acquisition". Status codes: **reported** (with the location in `draft_v2.md`), **not applicable** (with the reason), **not reported** (with what is missing).

## D. Experimental design

| Item | Status | Where / what |
|---|---|---|
| D1 Number of subjects analysed | reported | Methods, Dataset: fourteen subjects, each with a DMT run and a placebo run; N = 14 in every inference. |
| D2 Sample size determination | not applicable | Secondary analysis of a released dataset; the sample is the 14 subjects the data authors retained. No power analysis was possible or performed; Limitations states "One dataset, one drug, one parcellation, N = 14". |
| D3 Sampling frame and recruitment | not applicable | Reported by Timmermann et al. (2023). |
| D4 Inclusion and exclusion criteria | not applicable (recruitment); reported (analysis) | Recruitment criteria: Timmermann et al. (2023). Exclusions at the data-release stage: Methods, Dataset — "six of twenty participants were excluded by the source authors for head movement (Singleton et al., 2025)". No subject was excluded by this study. |
| D5 Demographics (age, sex, handedness) | not reported | Not stated in this paper for the 14 analysed subjects; the derivatives carry no demographic fields. Timmermann et al. (2023) report the demographics of the 20 recruited participants. |
| D6 Task / paradigm specification | reported | Methods, Dataset: continuous resting-state session of 840 TRs, intravenous injection at TR 240 (20 mg DMT fumarate over 30 s); placebo run of the same form; intensity ratings (0–10, once per 30 TRs) collected in a second, later session and used in no main-text result. Instructions to participants (eyes closed or open) are not restated here: Timmermann et al. (2023). |
| D7 Design timing and event structure | reported | Methods, The DMT contrast: pre-injection windows 1–4, post windows 6–14 (primary), window 5 excluded; W = 60 TRs (2 min) per window; rating bins of 30 TRs. |
| D8 Number of runs and run order | reported | Methods, Dataset: one DMT run and one placebo run per subject (order and blinding as in Timmermann et al., 2023, not restated). |
| D9 Behavioural performance | not applicable | No behavioural task; the subjective intensity ratings are described (Methods, Dataset; Supplement S1, Table S2) and enter no main-text result. |

## A. Acquisition

| Item | Status | Where / what |
|---|---|---|
| A1 Subject preparation (head restraint, mock scanning, instructions) | not applicable | Timmermann et al. (2023). |
| A2 MRI system (vendor, model, field strength, coil) | not applicable; partly reported | Methods, Dataset gives the field strength (3 T) and TR (2 s) as stated by the data authors; vendor, model and coil: Timmermann et al. (2023). |
| A3 Pulse sequence and parameters (TE, flip angle, FOV, matrix, voxel size, slices, acceleration, phase encoding, number of volumes) | not applicable; partly reported | Number of volumes (840) and TR (2 s): Methods, Dataset. All other parameters: Timmermann et al. (2023). |
| A4 Structural acquisition | not applicable | Timmermann et al. (2023). |
| A5 Physiological recording (cardiac, respiratory) and EEG | not applicable | Simultaneous EEG was recorded by the source study (Timmermann et al., 2023); an HRF-convolved EEG Lempel–Ziv regressor is released with the data and is used only in the original pre-specified analysis (Supplement S1, Table S6), not in the main text. |
| A6 Preliminary quality control (motion, incidental findings) | not applicable; partly reported | Exclusion of six subjects for head movement by the data authors: Methods, Dataset. Framewise displacement per TR is released with the data and used for motion control here (Methods, The DMT contrast). |

## P. Preprocessing (image processing was done by the data authors; the items below describe the released derivatives as used here)

| Item | Status | Where / what |
|---|---|---|
| P1 Preprocessing software and versions | not applicable | Timmermann et al. (2023); Singleton et al. (2025). Not restated. |
| P2 Distortion, slice-timing and motion correction | not applicable | Timmermann et al. (2023); Singleton et al. (2025). |
| P3 Intra- and inter-subject registration, template | not applicable | Timmermann et al. (2023); Singleton et al. (2025). The parcellation is applied in MNI space by the data authors. |
| P4 Spatial smoothing | not applicable | Timmermann et al. (2023); Singleton et al. (2025). |
| P5 Temporal filtering | reported | Methods, Dataset: the released series are band-limited to 0.01–0.08 Hz; the consequence for lag-1 autocorrelation (r₁ ≈ 0.82 for white noise at TR = 2 s) is stated. |
| P6 Nuisance regression and denoising (motion parameters, CompCor, scrubbing, global signal) | reported for what varies here; otherwise not applicable | Two released variants are analysed and named at every result: with global signal regression (`ts_gsr`, primary) and demeaned without it (`ts_demean`, sensitivity) — Methods, Dataset. The remaining denoising steps are the data authors' (Timmermann et al., 2023; Singleton et al., 2025). HRF deconvolution (rsHRF 1.7.0) was applied here only as a post-hoc exploration (Methods; Supplement S2). |
| P7 Parcellation / atlas | reported | Methods, Dataset: Schaefer-100 (7-network order) plus 16 subcortical parcels; region 20 dropped for all subjects and both conditions (mean-filled parcel confirmed by the data authors), leaving 115 regions and 6,555 pairs. |
| P8 Data quality checks on the derivatives | reported | Methods, Dataset: one non-finite TR (subject index 2, PCB, TR 839) dropped; subject alignment across files checked (record, "Subject alignment across files"); `scripts/00_verify.py` checks shapes and finiteness before every run. |
| P9 Motion quantification and handling | reported | Methods, The DMT contrast: window-mean FD regressed out within each subject and condition, DiD recomputed on the residuals, "survives" defined; the FD DiD itself is reported (Table 2). |

## S. Statistical modelling and inference

| Item | Status | Where / what |
|---|---|---|
| S1 Dependent variables and estimator | reported | Methods, Estimator and The two redundancy functions: Gaussian ΦID atoms (`phyid`, commit pinned), MMI and CCS redundancy, whole-brain pair means; windowed (W = 60, W = 30) and global-fit estimators; the closed-form implementation and its validation. |
| S2 Model of temporal autocorrelation | reported | The estimator's dependence on lag-1 autocorrelation is the subject of the paper (Methods, Closed-form atoms; Results 2–5); the effective sample size per window (≈ 20) is stated in Methods, Estimator and in the Abstract. |
| S3 First-level (within-subject) model | reported | Methods, The DMT contrast: per-subject difference-in-differences, (post − pre)_DMT − (post − pre)_PCB, on window means. |
| S4 Second-level (group) model and inference | reported | Methods, The DMT contrast: exact sign-flip permutation over 14 subjects (16,384 assignments, two-sided); subject-bootstrap 95 % CI (10,000 draws); phase-randomised temporal null (1,000 surrogates); motion control. |
| S5 Multiple-comparison handling | reported | Methods, Multiplicity: no correction; the count of inference rows (474), the weighting rule (p ≤ 0.005 on both nulls across variants), and the treatment of p between 0.01 and 0.06. Exploratory regional FDR (BH) is in Supplement S1 (Table S3). |
| S6 Pre-specification and deviations | reported | Methods, History of the study; record `manuscript/analysis_record.md`; `manuscript/prespecification_summary.md`; every post-hoc or review computation is labelled at first mention. |
| S7 Functional-connectivity / network definition | reported | Methods, Estimator: nodes are the 115 parcels, "edges" are the 6,555 region pairs, quantities are whole-brain pair means of ΦID atoms; Results 2 states the per-pair operating point. |
| S8 Software and versions | reported | Methods, Estimator: Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.1, `phyid` at commit 6c5f2e9d…, `requirements.lock.txt`; seed 20261120 throughout. |
| S9 Simulations and null models | reported | Methods, The residual diagnostic and Bias simulations: VAR(1) bias check (2,000 replicate windows per cell), sts-matched null, finite-sample null (a review computation), coupled family; each with its provenance. |

## R. Results reporting

| Item | Status | Where / what |
|---|---|---|
| R1 Effect sizes with uncertainty | reported | Every contrast is given as a mean DiD with a bootstrap 95 % CI and exact p (Tables 2–6; Results 3–5). |
| R2 Direction and magnitude relative to baseline | reported | Results 3: −7.0 % of the pre-injection DMT mean; Table 2 pre-injection means. |
| R3 Per-subject data | reported | Figure 3 (per-subject DiDs), subjects negative-of-14 counts in every table, leave-one-out (Results 3; `results/loo_did_win60.csv`) and leave-two-out (Results 3; Figure 3a). |
| R4 Figures with stated uncertainty | reported | Captions (`manuscript/figures/captions_v2.md`) state what each band and whisker is (bootstrap CI; within-subject SEM) and which panels carry no uncertainty. |
| R5 Null and negative results | reported | Results 3 (ΦR null), Results 4 (residual outcome outside both pre-specified branches; split-half undetermined), Results 5 (τ = 5 null), Supplement S1 (void tier-2 verdict). |
| R6 Regional / spatial results | reported (exploratory) | Supplement S1, Tables S3–S5, with spin tests for cortical maps; labelled exploratory. |
| R7 Limitations | reported | Discussion, Limitations. |

## Sh. Data and code sharing

| Item | Status | Where / what |
|---|---|---|
| Sh1 Raw data availability | not applicable | Raw images were not used and are not held; the data authors' release (https://github.com/singlesp/DMT_NCT; Zenodo 10.5281/zenodo.15177511) is cited in Methods, Dataset and Data and code availability. |
| Sh2 Derived data used | reported | Data and code availability: the released derivatives are cloned into `external/` and not redistributed; reuse terms confirmed by the data collectors and derivative authors (Methods, Dataset). |
| Sh3 Analysis code | reported | Data and code availability: https://github.com/Vasilis540/dmt-phiid, pinned environment, every result table with its git SHA, `run_all.sh`. |
| Sh4 Results files and materials | reported | Every table's source file is named in its caption; `results/` and `notes/review_results/` are in the repository. |
| Sh5 Ethics and consent for sharing | reported | Ethics statement (main text): approval of the original study, secondary analysis of anonymised derivatives, no new data, no participant identifiable. |
| Sh6 Pre-registration / analysis plan | reported | `manuscript/analysis_record.md` (git-tracked, append-only) and `manuscript/prespecification_summary.md`; Methods, History states what each entry establishes ("ordering, not blindness"). |

## Items not reported in this paper, collected

D5 demographics of the 14 analysed subjects (available for the 20 recruited in Timmermann et al., 2023; not carried by the derivatives); the participant instructions for the resting-state session (Timmermann et al., 2023); every acquisition parameter beyond field strength, TR and the number of volumes (Timmermann et al., 2023); every image-preprocessing step beyond the band-pass, the global-signal variants and the parcellation (Timmermann et al., 2023; Singleton et al., 2025). None of these was available to, or altered by, this analysis.
