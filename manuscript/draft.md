# Whole-brain synergistic information decreases under DMT: a pre-specified test of two accounts of synergy and conscious level

Vasilis Sampalis¹, [TK]

¹ Independent researcher, Athens, Greece

Correspondence: sampalisvasilis@gmail.com

**Status: draft, not for circulation. Every number is quoted from `results/*.csv` or the project record; [TK] marks a value not yet in a file.**

---

## Abstract

**Background.** Integrated Information Decomposition (ΦID) splits the information a pair of brain regions carries forward in time into redundant, unique and synergistic parts. Luppi et al. (2024) found that synergy-ranked regions form a "synergistic workspace" whose integrated information collapses under propofol and in disorders of consciousness. If synergy indexes conscious level, it should rise in an intensely conscious state such as the DMT experience. The entropic-brain account and the Lempel-Ziv literature predict instead that psychedelic dynamics become less predictable, which under a Gaussian ΦID model means less time-delayed information of every kind, synergy included.

**Methods.** We applied time-resolved ΦID (Gaussian, minimum-mutual-information redundancy, lag one TR) to an open within-subject fMRI dataset of 14 volunteers scanned under intravenous DMT and placebo with intensity ratings every 60 s. Whole-brain mean synergy was estimated in 60-TR windows, model refit per window. The primary pre-/post-injection difference-in-differences (DiD), its motion handling, an intensity-tracking criterion with time-in-scanner and motion controls, and a directional-failure rule were fixed in a git-tracked record before any windowed result existed. The pre-specified direction was an increase.

**Results.** Synergy decreased: DiD −0.0809 nats [95 % CI −0.1261, −0.0377], sign-flip p = 0.0038, phase-randomised p = 0.0020, negative in 13 of 14 subjects. It survived framewise-displacement residualisation and replicated without global signal regression (−0.1031 [−0.1558, −0.0522], p = 0.0026). Total time-delayed mutual information fell with it. The intensity-tracking claim was void under its pre-specified controls. Exploratory regional analysis found the decrease in 114 of 115 regions, with no concentration in a network proxy of the synergistic workspace and no receptor-map correlation surviving correction.

**Conclusions.** In a state of heightened conscious content, whole-brain synergy falls uniformly across cortex. The result favours the predictability account over synergy as a monotone index of conscious level, and dissociates the DMT state from the workspace-concentrated collapse reported under anaesthesia.

---

## Introduction

Integrated Information Decomposition (ΦID; Mediano et al., 2021) extends partial information decomposition (Williams & Beer, 2010) to the time-delayed mutual information (TDMI) between the past and future of two variables. TDMI is split into sixteen atoms, each describing how one kind of information in the past (redundant, unique to either source, or synergistic) becomes one kind of information in the future. The atom that has drawn most attention is synergy-to-synergy (sts): information that only the joint past of two regions carries about their joint future. Applied to resting fMRI, ΦID separates a redundancy-dominated core from a synergy-dominated set of association regions (Luppi et al., 2022), and Luppi et al. (2024) showed that the regions ranked highest for synergy form a "synergistic global workspace" whose integrated information is reduced under propofol anaesthesia and in patients with disorders of consciousness. The natural reading of that result is that synergy is a marker of conscious level: less synergy, less consciousness.

That reading makes a prediction in the opposite direction for a state in which conscious content is intensified rather than lost. N,N-dimethyltryptamine (DMT) given intravenously produces, within about two minutes, an immersive experience of very high subjective intensity that decays over roughly twenty minutes (Timmermann et al., 2023). If synergy tracks conscious level, whole-brain synergy should rise under DMT and follow the intensity time course. A second body of work predicts the reverse. The entropic-brain account (Carhart-Harris et al., 2014) holds that psychedelics increase the entropy of spontaneous brain activity, and the most replicated electrophysiological finding under psychedelics is increased Lempel-Ziv complexity of the signal, including under DMT (Schartner et al., 2017; Timmermann et al., 2019). Under a Gaussian ΦID model every atom is a share of lag-one predictability. Less predictable dynamics mean less TDMI, and since sts is the largest atom at the whole-brain mean in these data, they mean less synergy. The two accounts therefore make opposite directional predictions for the same quantity in the same state.

Nobody has applied time-resolved ΦID to a psychedelic fMRI dataset. The nearest work is a static partial information decomposition of MEG under LSD, psilocybin and ketamine (Liardi et al., 2024), which is neither fMRI, nor DMT, nor time-resolved, nor coupled to a continuous intensity measure. The dataset of Timmermann et al. (2023), released with Singleton et al. (2025), permits the adjudication: fourteen volunteers scanned under DMT and placebo in a within-subject design, with intensity rated every minute throughout, so a synergy time course can be set against a subjective one in the same subject. We pre-specified the workspace prediction (synergy increases) together with a rule for how a significant decrease would be reported, and we found the decrease.

---

## Methods

### Dataset

Data are the preprocessed Schaefer-116 timeseries released by Singleton et al. (2025) at https://github.com/singlesp/DMT_NCT (Zenodo 10.5281/zenodo.15177511), originally acquired by Timmermann et al. (2023). Fourteen subjects each have a DMT run and a placebo (PCB) run of 840 TRs at TR = 2 s (28 min), with intravenous injection at TR 240 (the end of minute 8). Timmermann et al. (2023) report twenty participants given 20 mg DMT fumarate in 10 mL saline injected intravenously over 30 s, scanned at 3 T (Siemens Magnetom Verio) with TR = 2000 ms; preprocessing is as described there and by Singleton et al. (2025). Singleton et al. state that six of the twenty were excluded for excessive head movement during the DMT scans, leaving 14, and the ratings file carries 14 subject codes (S02WT, S03CT, S06JB, S07MN, S10RM, S11AE, S12AP, S13HK, S15LP, S17CS, S18CS, S19SG, S23LPJ, S25MM). Subjective intensity was rated on a 0–10 scale 28 times per run, once per 30 TRs, so each rating bin is exactly 60 s. The mean DMT curve is ≈ 0 for bins 1–8, rises to 8.5 at bin 9, peaks at 9.3 at bin 10 and decays to ≈ 0.4 by bin 28; placebo ratings are flat at ≈ 0. Framewise displacement (FD) per TR and an HRF-convolved EEG Lempel-Ziv complexity regressor per TR are supplied with the data. Two preprocessing variants were analysed: with global signal regression (`ts_gsr`, primary) and demeaned without it (`ts_demean`, sensitivity). One TR (subject index 2, PCB, TR 839) is non-finite in every region and was dropped.

The release carries no licence file; reuse terms are being confirmed with the authors [TK]. The subject ordering shared by the timeseries, FD, ratings and EEG files is not carried by any array. We verified it for timeseries–FD at one subject (a co-located data defect) and for timeseries–EEG statistically (matched-pairing test, p = 0.008), and it is plausible but unverified for the ratings (see Limitations).

### Parcellation and region exclusion

The parcellation is Schaefer-100 (7-network order; Schaefer et al., 2018; Yeo et al., 2011) plus 16 subcortical parcels. Region 20 (0-based; `LH_DorsAttn_Post_6`) is exactly constant across all 840 TRs of one subject's DMT run in every variant including the raw timeseries, so the defect is upstream. It was dropped for all subjects and both conditions before any result was computed, leaving 115 regions and 6,555 pairs, so that every within-subject contrast is over the same pair set. Neither source paper mentions the parcel.

### Estimator

ΦID atoms were computed with the `phyid` package (Imperial-MIND-lab, commit 6c5f2e9; Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1) using `calc_PhiID(kind='gaussian', redundancy='MMI', tau=1)`: a Gaussian model of the four-vector (x_t, y_t, x_{t+1}, y_{t+1}), minimum-mutual-information redundancy (Barrett, 2015), lag one TR. The function returns sixteen local atoms per timepoint. Whole-brain synergy is the mean of the sts atom over the 6,555 pairs; the other atoms and their sum (TDMI) are kept from the same computation. Every atom value in this paper is in nats.

Three fitting modes were used. **Robustness A (global fit)**: one Gaussian fitted to the full run, local atoms averaged into the 28 rating bins. The global fit fits one covariance to the whole run and returns local values under that single model, so by construction it cannot detect a change in the joint distribution; it was retained as a descriptive baseline. **Primary B (windowed)**: the run cut into non-overlapping 60-TR windows (14 per run), each an independent `calc_PhiID` call on that window's samples alone, with covariance, mean and MMI selections all refit per window. Each window spans two rating bins. **Robustness C (placebo-fitted)**: per subject and pair, the Gaussian fitted on the first half of the placebo run (TRs 0–419) and local atoms evaluated under that fixed model on the held-out placebo half (TRs 420–839) and on the full DMT run, so both evaluations are out-of-sample. The fixed-model code path reproduces `calc_PhiID` to 1e-13 when fit and evaluation data coincide.

### Pre-specification and audit trail

The analysis plan is pre-specified but not externally pre-registered. Every analysis choice, prediction and decision rule was written into the repository record (`manuscript/analysis_record.md`; the file lived at `CLAUDE.md` until 14 Sep 2026, when it was moved with `git mv`, byte-identical and with its history following it) and committed before the result it governs existed, and the commit history is the audit trail. The initial commit (44cec4f, 12 Sep 2026) fixed the hypothesis, the estimator and its settings, the seed (20261120), the window length and the methodological rules. Commit e16ebba fixed the region-20 exclusion and the design of the bias check; 18ad8b4 fixed the window-length decision tree, the non-stationary simulation, its tracking criteria and the tracking controls; 33f0b33 fixed the directional-failure rule and the redundancy prediction; febf599 executed the decision tree's check, fixed the real-data decay windows, the tier-disagreement rule and the W = 30 positive control; b7e4595 fixed the step-contrast test and the motion handling; e46df8a fixed the tracking threshold correction while the first windowed real-data run was in progress and unread; the result was recorded at cb1b2cf. Each results table carries the git SHA of the code that produced it.

The pre-specified direction was an increase in whole-brain synergy under DMT. The directional-failure rule, fixed before any Primary B result, states that a significant decrease refutes the stated hypothesis and is reported as a refutation, not reframed as a confirmation of "synergy changes under DMT".

### Bias characterisation and the choice of window length

Gaussian entropy estimates carry finite-sample bias, and a windowed ΦID estimate is a difference of such estimates. Before any windowed result on real data, the estimator was characterised on simulated VAR(1) processes with analytic ground truth (`02_bias_check.py`; 2,000 replicate windows per cell, repeated at 20,000 for the tracking verdict). Window length was fixed in advance at 30 TRs (one rating bin, the window Singleton et al. used on this dataset) with a decision tree for moving to 60 TRs. In stationary simulations the estimated between-condition sts difference had the true sign in every cell but a smaller magnitude, with 52–77 % of the true difference absorbed at W = 30 and 15–45 % at W = 60. An analytic log-det bias correction was derived, predicted to change the differential bias by exactly zero, implemented, and confirmed to do so (max change 1e-6, the tables' rounding). The pre-specified criterion for W = 30 therefore failed and W = 60 became the primary window, with W = 30 retained as a positive control expected to give the same sign and a smaller magnitude.

A non-stationary simulation with a regime switch at TR 240 and an intensity-shaped decay tested whether pooled synergy could resolve adjacent windows (tier 1) or the full decay (tier 2). At W = 60 and the effective pooling estimated for these data (see below), tier 2 passed cleanly (sign-corrected Spearman R = 0.964–0.990 across cells) while tier 1 was marginal, and tier 2 was assigned by the pre-specified escalation rule. The global fit landed on the analytic value of the mixture covariance to within 0.0003 in the step conditions: it smears a change rather than tracking it.

A later diagnostic showed that no simulated family matches the real dependence structure: the real regional autocorrelation function falls to 0.16 by lag 3 and is negative from lag 5, with a crude integrated autocorrelation time of ≈ 2.8 against 3.3 and 14.4 for the two simulated AR(1) families. The simulated per-window bias is therefore 3–4 times the real windowed-versus-global gap. Consequently no simulated shrinkage figure is quoted as the cost of the primary result. What the real data bound directly is the per-window level bias (whole-brain sts under the windowed estimator sits 0.15 nats below the global fit at W = 60, common to both conditions) and the agreement between the two window lengths (below).

### Effective sample size

The whole-brain mean pools 6,555 non-independent pairs. For the simulation the effective number of independent components per subject was taken as the participation ratio of the eigenvalues of each subject's placebo-run 115 × 115 correlation matrix: 14.3 for `ts_gsr` (SD 2.3) and 10.8 for `ts_demean` (SD 3.0). The deciding pooling was M = 14 × C(14.3, 2) = 1,338 independent pair-windows, with M = 742 as a required sensitivity and M = 151 (one unit per component rather than per pair) reported but not deciding. Both deciding values are upper bounds.

### Window sets and onset contamination

Pre-injection windows are 1–4 (bins 1–8). The post-injection primary set is windows 6–14 (bins 11–28), the sensitivity set windows 5–14 (bins 9–28). Window 5 (bins 9–10) was excluded from the primary set, before any windowed result, on evidence from the global fit that bins 8–10 carry an injection response present in both arms: on the no-GSR data placebo redundancy (rtr) rises at bins 8–9 (0.042, 0.049 against a 0.028 baseline), the same bins in which DMT rtr peaks; placebo sts on `ts_gsr` dips at bin 10 alone (1.232 against a 1.23–1.35 range); and, computed later, mean pairwise correlation on `ts_demean` jumps in placebo at bins 8–9 (0.278, 0.336 against ≈ 0.15). Window-mean FD on DMT is 0.203 at window 5 against 0.117–0.132 pre-injection. Any contrast that includes bins 8–10 mixes a drug effect with an injection event.

### Primary test: step contrast

Per subject, the statistic is (post − pre) on DMT minus (post − pre) on PCB for whole-brain mean sts from the windowed estimator (DiD). Inference: exact sign-flip permutation across the 14 subjects (all 16,384 assignments, two-sided); effect size as mean DiD with a subject-bootstrap 95 % CI (10,000 draws) in nats and as a share of the pre-injection DMT mean; and a second, temporal null under which the TR-resolution whole-brain mean local sts series is phase-randomised per subject and condition (1,000 surrogates; Prichard & Theiler, 1994), re-averaged into the same windows and the DiD recomputed. Both preprocessing variants and both window sets are reported together; no correction is applied because there is one whole-brain statistic per variant and window set and none is selected among.

### Motion handling

Window-mean FD is reported per condition and window, and the FD DiD is computed in the same form as the synergy DiD. Within each subject and condition, window-mean sts was regressed on window-mean FD across all 14 windows (OLS, intercept, one slope per subject × condition) and the DiD recomputed on the residuals. "Survives motion control" was defined as the residualised DiD having the same sign as the raw DiD with a bootstrap CI excluding zero. A 14-window within-subject regression is crude and can over-remove where FD and drug share a time course, which they do at onset; this is one reason the primary post set starts at window 6.

### Intensity tracking and its controls

The tracking analysis asks whether synergy follows intensity across the decay phase (the tier-2 claim; tier 1, adjacent-window resolution, was not attempted on real data). The thresholded statistic is the Spearman correlation ρ_S between the 14-subject mean sts series over the decay windows and the group-mean intensity template f, with |ρ_S| ≥ 0.80 as the threshold validated by simulation. Alongside it, the per-subject mean ρ_S against each subject's own ratings (primary) and against f (sensitivity) is tested for existence against the phase-randomised null and is not thresholded. A tier-2 claim requires: the group-mean-series threshold pass; the per-subject mean significant in the same direction; control (a), that the same statistic on the placebo run, which correlates synergy with time in scanner alone, is exceeded by DMT with a within-subject difference whose bootstrap CI excludes zero and with placebo below half of DMT; and control (b), that all of the above also hold on FD-residualised synergy (regression over the decay windows). Tracking is assessed on |ρ_S|; the sign is reported separately against the pre-specified positive direction. A voided claim is reported at tier 3, the step contrast plus the methods contribution.

### Secondary and robustness analyses

The remaining fifteen atoms and TDMI were tested with the same DiD, sign-flip test and bootstrap, under both estimators on identical bin sets (`07_windowed_atoms_did.py`). A redundancy prediction was fixed before rtr was inspected: under a redundancy-dominance reading of an sts decrease, rtr should rise with a mirrored time course. Robustness C contrasts are (i) the within-DMT step and (ii) DMT minus PCB on the matched out-of-sample bins 15–28. Mean pairwise Pearson correlation per bin (`09_global_fc_per_bin.py`) was computed on the same pairs for comparison with Timmermann et al. (2023). The EEG Lempel-Ziv regressor was correlated with bin-mean TDMI per subject (Spearman, 28 bins), tested against a phase-randomised surrogate of the LZ series, with the prediction, recorded before computation, of a negative correlation on the DMT run.

### Exploratory regional analysis

Specified after the primary result and labelled exploratory throughout. Per-region synergy is the mean sts over the 114 pairs containing that region, from the global fit, per bin, subject and condition. Per-region DiD (post bins 11–28 minus pre bins 1–8) was tested by exact sign-flip and corrected by Benjamini–Hochberg FDR at q = 0.05 across 115 regions. The group-mean DiD map was correlated with 5-HT2A, 5-HT1A, 5-HT1B, 5-HT4 and 5-HTT density maps [TK: PET atlas source for `5HTvecs_sch116.mat`] on the 99 cortical parcels using the 10,000 spherical rotations supplied with the source repository (Váša et al., 2018; Alexander-Bloch et al., 2018), two-sided, BH-corrected across the five maps; subcortex has no spin null and is reported descriptively. The Luppi et al. workspace, published only as a figure on a different parcellation, was proxied at the network level as Yeo Default ∪ Control (37 cortical parcels; gateway proxy = Default, broadcaster proxy = Control), with a named-subregion proxy (26 parcels) as sensitivity. The statistic is each subject's mean regional DiD inside minus outside the proxy, sign-flip tested. The proxy is fixed by atlas labels and involves no selection on the tested effect.

---

## Results

### Whole-brain synergy decreases after DMT

Table 1 gives the primary step contrast. On `ts_gsr` at W = 60, whole-brain sts fell after injection on the DMT run and rose on the placebo run, giving a DiD of −0.0809 nats [−0.1261, −0.0377], sign-flip p = 0.0038, phase-randomised p = 0.0020, negative in 13 of 14 subjects. The FD DiD in the same form was not significant, and the FD-residualised DiD kept its sign with a CI excluding zero, so the effect survives motion control under the pre-specified definition. Without global signal regression the contrast replicated (−0.1031 [−0.1558, −0.0522], p = 0.0026), and the sensitivity windows 5–14 give the same result on both variants (Supplementary Table S1). The pre-specified direction was positive; under the directional-failure rule this is a refutation of the up-regulation hypothesis. A post-hoc leave-one-out check, not pre-specified, refit the primary DiD with each subject dropped in turn: the mean ranged from −0.0944 to −0.0656 on ts_gsr and from −0.1182 to −0.0871 on ts_demean, all 28 refits kept a bootstrap CI excluding zero, and dropping subject 8, the largest single contributor (per-subject DiD −0.280 on ts_gsr, −0.311 on ts_demean), gave −0.0656 [−0.1013, −0.0271], p = 0.0076 on ts_gsr and −0.0871 [−0.1310, −0.0408], p = 0.0051 on ts_demean (`results/loo_did_win60.csv`).

**Table 1. Primary step contrast, whole-brain mean sts, W = 60, windows 6–14 vs 1–4 (nats; N = 14; sign-flip p two-sided; subject-bootstrap 95 % CI).**

| | ts_gsr | ts_demean |
|---|---|---|
| Pre-injection DMT / PCB mean | 1.1554 / 1.1378 | 1.1004 / 1.0819 |
| DMT post − pre | −0.0485 [−0.0819, −0.0113], p = 0.0267 | −0.0633 [−0.1088, −0.0123], p = 0.0333 |
| PCB post − pre | +0.0324 [+0.0053, +0.0606], p = 0.0425 | +0.0398 [+0.0089, +0.0692], p = 0.0306 |
| DiD raw | −0.0809 [−0.1261, −0.0377], p = 0.0038; phase-randomised p = 0.0020; 13/14 negative; −7.0 % of baseline | −0.1031 [−0.1558, −0.0522], p = 0.0026; phase-randomised p = 0.0010; 12/14 negative; −9.4 % |
| FD DiD | +0.0143 [−0.0070, +0.0365], p = 0.2452 | same (FD is variant-independent) |
| DiD FD-residualised | −0.0649 [−0.0966, −0.0289], p = 0.0048; 13/14 | −0.0824 [−0.1224, −0.0372], p = 0.0048; 13/14 |

The placebo rise is a finding of the windowed estimator that the global fit did not show (global-fit placebo change over bins 9–14: −0.005). On the primary windows roughly 40 % of the DiD is the placebo rise rather than the DMT fall, which is why the within-condition changes are reported separately.

### A loss of total predictable information, not a redistribution

Table 2 gives the same DiD for redundancy (rtr), TDMI and the largest remaining atoms under both estimators. Every entry is negative: TDMI fell, sts carried the largest share, the within-region self-transfer atoms xtx and yty most of the rest, and no atom of consequence rose. The pre-specified redundancy prediction failed on `ts_gsr`: rtr fell with sts (positive DiD in 4 of 14 subjects) and co-varied with it across bins (r = 0.66) rather than mirroring it. On `ts_demean` the group-mean rtr DiD was +0.0137 but positive in only 7 of 14 subjects, peaked at the injection bin 9 rather than the intensity peak, and coincided with a placebo rtr bump at bins 8–9. The redundancy-dominance interpretation is not supported on either variant.

**Table 2. Atom decomposition of the primary DiD, ts_gsr (nats; windowed: windows 6–14 vs 1–4 at W = 60; global fit: bins 11–28 vs 1–8).**

| atom | windowed DiD [CI], p, negative/14 | global-fit DiD [CI], p, negative/14 |
|---|---|---|
| sts | −0.0809 [−0.1253, −0.0365], 0.0038, 13 | −0.0801 [−0.1302, −0.0310], 0.0071, 12 |
| rtr | −0.0078 [−0.0135, −0.0016], 0.0312, 10 | −0.0060 [−0.0131, +0.0014], 0.1378, 10 |
| TDMI (Σ16) | −0.1037 [−0.1600, −0.0479], 0.0034, 12 | −0.1216 [−0.1917, −0.0526], 0.0051, 13 |
| xtx | −0.0523 [−0.0839, −0.0221], 0.0065, 12 | −0.0544 [−0.0885, −0.0216], 0.0081, 12 |
| yty | −0.0396 [−0.0673, −0.0130], 0.0131, 13 | −0.0431 [−0.0767, −0.0128], 0.0137, 13 |
| rts | −0.0407 [−0.0645, −0.0178], 0.0051, 12 | −0.0396 [−0.0661, −0.0141], 0.0090, 12 |

Pre-injection DMT levels, windowed / global: sts 1.1554 / 1.3085, rtr 0.0388 / 0.0248, TDMI 1.4772 / 1.4421.

### Intensity tracking: significant, negative, and void under its controls

On the primary decay windows (6–14, DMT run, `ts_gsr`) the group-mean sts series correlated with the intensity template at ρ_S = −0.9833 (p = 0.0020), passing the |ρ| ≥ 0.80 threshold with the sign opposite to the pre-specified direction, and the per-subject mean against each subject's own ratings was −0.4826 [−0.6291, −0.3362], p = 0.0010. Control (a) cleared on the raw data. Control (b) voided the claim: window-mean FD on DMT itself correlates with the template (+0.4060 [+0.1774, +0.6000]), and after FD residualisation the within-subject difference from placebo was −0.2071 [−0.4345, +0.0345], a CI including zero. The tier-2 claim is void on the primary windows for both the own-ratings and the template versions, void on the sensitivity windows on the raw data already, and void on `ts_demean` (Supplementary Table S2). The void reflects attenuation by residualisation plus a placebo trend with time in scanner, which is what the controls were built to detect; it stands as written. The tier assigned to the primary empirical claim is tier 3: the step contrast plus the methods contribution.

### Exploratory regional analysis: a uniform decrease

*Every result in this subsection is exploratory.* The regional DiD map was negative in 114 of 115 regions on both variants (exploratory); the mean over regions equals the whole-brain pair-mean DiD to 2.22e-15. Seven regions survived FDR on `ts_gsr` and 19 on `ts_demean`, all negative and all cortical, four common to both (exploratory; Supplementary Table S3). The exploratory workspace comparison found no concentration of the decrease in the network proxy of the synergistic workspace: workspace minus non-workspace mean regional DiD was −0.0095 [−0.0230, +0.0050], p = 0.216, on `ts_gsr` and −0.0050 [−0.0225, +0.0120], p = 0.590, on `ts_demean`, with both sets falling individually by similar amounts and the same picture under the named-subregion, subcortex-inclusive, gateway and broadcaster variants (exploratory; Supplementary Table S4). The exploratory receptor-map test was null: nothing survived BH correction across the five maps on either variant, and the 5-HT2A cortical spin-test ρ_S was −0.160 (p = 0.116) on `ts_gsr` and −0.055 (p = 0.677) on `ts_demean` (exploratory; Supplementary Table S5).

### Mean pairwise correlation rises while synergy falls

On `ts_demean`, mean Pearson r over the same 6,555 pairs rose under DMT (DiD +0.0526 [+0.0073, +0.0976], p = 0.0470, positive in 10 of 14), replicating the global-connectivity increase of Timmermann et al. (2023), while on the identical bins whole-brain sts fell (−0.1035 [−0.1678, −0.0357], p = 0.0132). On `ts_gsr` the mean correlation is pinned near zero by construction and the comparison is uninformative. Zero-lag correlation and lag-one predictable information move in opposite directions on the same data.

### Cross-modal check against EEG Lempel-Ziv complexity

The prediction recorded before computation, that TDMI anti-correlates with EEG Lempel-Ziv complexity within the DMT run, held on both variants: per-subject Spearman ρ across 28 bins −0.2416 [−0.4011, −0.0765], one-sided p = 0.0020 against the phase-randomised LZ null on `ts_gsr`, nothing on the placebo run (Supplementary Table S6; global functional connectivity per bin set in Table S7). Both series are drug-locked, so the check establishes coherence across modalities, not tracking beyond the drug.

### Robustness

Table 3 collects the contrast across estimators, windows and variants. The W = 30 control gave the same sign at 0.85 of the W = 60 magnitude; the pre-specified inconsistency criterion (opposite sign or larger magnitude) was not met, and the shortfall against the simulated expectation has the cause given in Methods. Robustness C confirms the sign under an independent model; its magnitude is not comparable to the native fit because out-of-sample inflation differs between arms (+0.109 on PCB, +0.052 on DMT).

**Table 3. The DMT-minus-placebo synergy contrast across estimators, windows and variants (nats).**

| analysis | contrast | estimate [CI], p, negative/14 |
|---|---|---|
| Primary B, ts_gsr, W = 60 | DiD, windows 6–14 vs 1–4 | −0.0809 [−0.1261, −0.0377], 0.0038, 13 |
| Primary B, ts_demean, W = 60 | same | −0.1031 [−0.1558, −0.0522], 0.0026, 12 |
| W = 30 positive control, ts_gsr | DiD, bins 11–28 vs 1–8 | −0.0686 [−0.1084, −0.0293], 0.0042, 13 |
| Robustness A (global fit), ts_gsr | DiD, bins 11–28 vs 1–8 | −0.0801 [−0.1303, −0.0310], 0.0071, 12 |
| Robustness A, ts_demean | same | −0.1035 [−0.1678, −0.0357], 0.0132, 11 |
| Robustness C (placebo-fitted), ts_gsr | DMT − PCB, out-of-sample bins 15–28 | −0.1110 [−0.1803, −0.0593], 0.0005, 13 |
| Robustness C | within-DMT step, bins 11–28 vs 1–8 | −0.0508 [−0.1047, +0.0137], 0.1338, 11 |


---

## Discussion

### Synergy and conscious level

The two accounts set out in the Introduction made opposite predictions for the same measured quantity, and the data decided between them. Whole-brain synergistic information fell under DMT by about 7–9 % of baseline, in 12–13 of 14 subjects, on two nulls, two window sets, two preprocessing streams and three estimators, and the fall survived motion residualisation. It was not a redistribution among atoms: total lag-one predictable information fell, and synergy carried the largest share. The result is what the predictability account expects. Under a Gaussian ΦID model the atoms partition TDMI, TDMI is the predictability of the next sample from the current one, and psychedelics make cortical dynamics less predictable, as the Lempel-Ziv literature has repeatedly shown and as the EEG regressor supplied with this dataset shows again here.

What the result says about synergy as an index of conscious level has to be stated at the level of the quantity measured. Luppi et al.'s collapsing quantity is integrated information (ΦR) within a workspace of regions defined by a synergy-rank rule; ours is the whole-brain mean of the sts atom over all pairs. The whole-brain mean of sts is not a monotone index of conscious level: it falls when consciousness is lost under propofol and in disorders of consciousness, on the evidence of Luppi et al., and it falls here when conscious content is intensified. At the whole-brain mean, then, sts is tracking something other than level, and the natural candidate is the temporal predictability of the signal, which both propofol and DMT reduce. Whether workspace ΦR behaves differently under DMT is an open question that these data do not address.

### A spatial dissociation from anaesthesia

The exploratory regional analysis adds a second distinction. Under propofol and in disorders of consciousness the reduction reported by Luppi et al. (2024) is concentrated in workspace gateway regions of the default mode network. Here the decrease was present in 114 of 115 regions and was not larger inside a network proxy of the workspace than outside it, on either variant, with either proxy (exploratory). Read with the proxy's limitations, the two states dissociate spatially: a workspace-concentrated collapse in the one, a spatially uniform reduction in the other (exploratory). The exploratory receptor-map null is consistent with this: a uniform effect has no spatial pattern to correlate with a receptor distribution, and none was found. The comparison cannot go further than that. Luppi et al.'s workspace is a rank rule computed on other subjects at four times the parcel resolution and published as a figure; ours is a Yeo-network stand-in. "Synergy falls under DMT as it does under propofol" is not a licensed sentence, because the quantities, region sets and states all differ.

### Estimator findings

Three methodological findings are independent of the direction of the effect. First, the global Gaussian fit that `phyid` computes natively returns local values under one covariance fitted to the whole run and cannot represent a change in the joint distribution; in simulation it landed on the analytic value of the mixture covariance to within 0.0003, and on real data it missed the placebo-run rise that the windowed estimator found. A time-resolved synergy claim needs a model refit per window. Second, the windowed estimator is biased low by a per-window amount that is large relative to the effect (0.15 nats at W = 60 against a 0.08-nat DiD) but common to both conditions, and the two window lengths agree in sign and to within 15 % in magnitude. Third, a directional prediction on redundancy, fixed before the atom was inspected, failed on the GSR data and held only at the group mean on the no-GSR data, where it was carried by an injection-locked bump present in placebo. Injection itself produces a response in both arms at bins 8–10 that would have contaminated any contrast including them.

### Limitations

N = 14 within-subject. Effect sizes are reported with CIs throughout and the study is a proof of concept. The effective sample size used to set the simulation pooling is an upper bound; at the lower value (M = 151) the simulated full-decay criterion is marginal in some cells, which is one more reason the tracking claim is not made. No simulated family matches the real dependence structure, so the simulations characterise the estimator at longer correlation times than the data have, and no simulated shrinkage figure applies to the primary result. The workspace proxy is a network atlas standing in for a rank rule we did not compute. The subject ordering of the ratings file relative to the timeseries is plausible (it follows the original MATLAB loop and is in ascending subject-code order) but not verified, and it affects the per-subject tracking statistics, which were void in any case, and nothing in the step contrast. All results come from one dataset, one drug and one parcellation; the pre-specification is a git-tracked record, not an external registration, and the record was written over two days, so its ordering, not its duration, is what the audit trail establishes.

### Conclusion

Set against two opposing predictions fixed in advance, whole-brain synergistic information under DMT decreased, in nearly every subject and nearly every region, with total predictable information. Synergy at this scale does not index conscious level; it indexes predictability, and the DMT state reduces it uniformly rather than through the workspace collapse seen when consciousness is lost.

---

## Data and code availability

Timeseries, ratings, framewise displacement and the EEG regressor are from https://github.com/singlesp/DMT_NCT (Singleton et al., 2025; Zenodo 10.5281/zenodo.15177511), included as a submodule. Analysis code, the pinned environment (`requirements.lock.txt`), every results table with the git SHA that produced it, and the full pre-specification record are at https://github.com/Vasilis540/dmt-phiid. Seed 20261120 throughout. Reuse terms for the source data are being confirmed with its authors [TK].

## Author contributions

V.S.: conception, analysis, writing. [TK]

## Acknowledgements

[TK]. We thank the authors of Timmermann et al. (2023) and Singleton et al. (2025) for releasing the data.

---

## References

[TK: author lists, volumes and page ranges below are to be verified against each DOI before submission; only the DOIs recorded in the project file (Luppi 2024, Timmermann 2023, Singleton 2025, Liardi 2024) are taken from the record.]

Alexander-Bloch, A. F., Shou, H., Liu, S., Satterthwaite, T. D., Glahn, D. C., Shinohara, R. T., Vandekar, S. N., & Raznahan, A. (2018). On testing for spatial correspondence between maps of human brain structure or function. *NeuroImage*, 178, 540–551. https://doi.org/10.1016/j.neuroimage.2018.05.070

Barrett, A. B. (2015). Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems. *Physical Review E*, 91, 052802. https://doi.org/10.1103/PhysRevE.91.052802

Benjamini, Y., & Hochberg, Y. (1995). Controlling the false discovery rate: a practical and powerful approach to multiple testing. *Journal of the Royal Statistical Society B*, 57, 289–300.

Burt, J. B., Helmer, M., Shinn, M., Anticevic, A., & Murray, J. D. (2020). Generative modeling of brain maps with spatial autocorrelation. *NeuroImage*, 220, 117038. https://doi.org/10.1016/j.neuroimage.2020.117038

Carhart-Harris, R. L., Leech, R., Hellyer, P. J., Shanahan, M., Feilding, A., Tagliazucchi, E., Chialvo, D. R., & Nutt, D. (2014). The entropic brain: a theory of conscious states informed by neuroimaging research with psychedelic drugs. *Frontiers in Human Neuroscience*, 8, 20. https://doi.org/10.3389/fnhum.2014.00020

Kriegeskorte, N., Simmons, W. K., Bellgowan, P. S. F., & Baker, C. I. (2009). Circular analysis in systems neuroscience: the dangers of double dipping. *Nature Neuroscience*, 12, 535–540. https://doi.org/10.1038/nn.2303

Liardi, A., Rosas, F. E., Carhart-Harris, R. L., Bor, D., & Mediano, P. A. M. (2024). [TK: title]. *arXiv*, 2410.11583. Preprint, not peer reviewed.

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Holland, N., Fryer, T. D., O'Brien, J. T., Rowe, J. B., Menon, D. K., Bor, D., & Stamatakis, E. A. (2022). A synergistic core for human brain evolution and cognition. *Nature Neuroscience*, 25, 771–782. https://doi.org/10.1038/s41593-022-01070-0

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Allanson, J., Pickard, J. D., Carhart-Harris, R. L., Williams, G. B., Craig, M. M., Finoia, P., Owen, A. M., Naci, L., Menon, D. K., Bor, D., & Stamatakis, E. A. (2024). A synergistic workspace for human consciousness revealed by Integrated Information Decomposition. *eLife*, 12, RP88173. https://doi.org/10.7554/eLife.88173.4

Mediano, P. A. M., Rosas, F. E., Luppi, A. I., Carhart-Harris, R. L., Bor, D., Seth, A. K., & Barrett, A. B. (2021). Towards an extended taxonomy of information dynamics via Integrated Information Decomposition. *arXiv*, 2109.13186.

Prichard, D., & Theiler, J. (1994). Generating surrogate data for time series with several simultaneously measured variables. *Physical Review Letters*, 73, 951–954. https://doi.org/10.1103/PhysRevLett.73.951

Schaefer, A., Kong, R., Gordon, E. M., Laumann, T. O., Zuo, X.-N., Holmes, A. J., Eickhoff, S. B., & Yeo, B. T. T. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28, 3095–3114. https://doi.org/10.1093/cercor/bhx179

Schartner, M. M., Carhart-Harris, R. L., Barrett, A. B., Seth, A. K., & Muthukumaraswamy, S. D. (2017). Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*, 7, 46421. https://doi.org/10.1038/srep46421

Singleton, S. P., Timmermann, C., Luppi, A. I., Eckernäs, E., Roseman, L., Carhart-Harris, R. L., & Kuceyeski, A. (2025). Network control energy reductions under DMT relate to serotonin receptors, signal diversity, and subjective experience. *Communications Biology*, 8, 631. https://doi.org/10.1038/s42003-025-08078-9

Timmermann, C., Roseman, L., Schartner, M., Milliere, R., Williams, L. T. J., Erritzoe, D., Muthukumaraswamy, S., Ashton, M., Bendrioua, A., Kaur, O., Turton, S., Nour, M. M., Day, C. M., Leech, R., Nutt, D. J., & Carhart-Harris, R. L. (2019). Neural correlates of the DMT experience assessed with multivariate EEG. *Scientific Reports*, 9, 16324. https://doi.org/10.1038/s41598-019-51974-4

Timmermann, C., Roseman, L., Haridas, S., Rosas, F. E., Luan, L., Kettner, H., Martell, J., Erritzoe, D., Tagliazucchi, E., Pallavicini, C., Girn, M., Alamia, A., Leech, R., Nutt, D. J., & Carhart-Harris, R. L. (2023). Human brain effects of DMT assessed via EEG-fMRI. *Proceedings of the National Academy of Sciences*, 120, e2218949120. https://doi.org/10.1073/pnas.2218949120

Váša, F., Seidlitz, J., Romero-Garcia, R., Whitaker, K. J., Rosenthal, G., Vértes, P. E., Shinn, M., Alexander-Bloch, A., Fonagy, P., Dolan, R. J., Jones, P. B., Goodyer, I. M., the NSPN consortium, Sporns, O., & Bullmore, E. T. (2018). Adolescent tuning of association cortex in human structural brain networks. *Cerebral Cortex*, 28, 281–294. https://doi.org/10.1093/cercor/bhx249

Williams, P. L., & Beer, R. D. (2010). Nonnegative decomposition of multivariate information. *arXiv*, 1004.2515.

Yeo, B. T. T., Krienen, F. M., Sepulcre, J., Sabuncu, M. R., Lashkari, D., Hollinshead, M., Roffman, J. L., Smoller, J. W., Zöllei, L., Polimeni, J. R., Fischl, B., Liu, H., & Buckner, R. L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. *Journal of Neurophysiology*, 106, 1125–1165. https://doi.org/10.1152/jn.00338.2011
