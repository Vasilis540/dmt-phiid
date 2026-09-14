# Gaussian-MMI integrated information decomposition reports lag-1 autocorrelation change as synergy change: an analytic account, a residual diagnostic, and a demonstration on DMT fMRI

*Alternative title:* **The synergy atom of Gaussian-MMI ΦID on autocorrelated BOLD is mostly within-region self-prediction: analysis and a diagnostic**

Vasilis Sampalis¹, Christopher Timmermann² [TK], [TK further co-authors nominated by C.T.]

¹ Independent researcher, Athens, Greece. ² [TK affiliation]

Correspondence: sampalisvasilis@gmail.com

**Status: draft v2, not for circulation. It supersedes `manuscript/draft.md`, which is kept as a record. Every number is quoted from `results/*.csv`, from `manuscript/analysis_record.md`, or from the review and Part B result files under `notes/review_results/` (source named at first use); [TK] marks a value that no file holds.**

---

## Abstract

**Background.** Integrated Information Decomposition (ΦID) with the minimum-mutual-information (MMI) redundancy function underlies most reports of synergistic information in fMRI. What its synergy atom (sts) measures on strongly autocorrelated BOLD has not been established analytically.

**Methods.** We derive the sixteen Gaussian-MMI atoms in closed form for a bivariate AR(1) pair with lag-1 autocorrelation r₁ and innovation correlation q, map sts and its partial derivatives over (r₁, q), and compare with the common-change-in-surprisal (CCS) redundancy function after verifying its implementation independently. Both were applied to an open within-subject fMRI dataset (14 volunteers, intravenous DMT and placebo, TR = 2 s) in a pre/post difference-in-differences (DiD) with exact sign-flip, bootstrap, phase-randomised and motion controls. A residual diagnostic predicts each region pair's sts from its measured lag-1 autocorrelations and lag-0 correlation alone and tests the remainder. The study began as a pre-specified test of synergy up-regulation under DMT; the reframing is described.

**Results.** On the AR(1) family sts = −ln(1 − r₁²) + ½ ln(1 − r₁²q²): it equals the two within-region self-prediction atoms xtx + yty at q = 0, exceeds them by rtr elsewhere, and is balanced by four negative atoms; |∂sts/∂r₁| exceeds |∂sts/∂q| at every grid point except r₁ = 0, by a factor of 32 at the data's operating point. Under CCS the sts level is −0.0387 nats against +1.1554 under MMI and does not track r₁. Under DMT whole-brain MMI-sts fell (DiD −0.0809 [−0.1261, −0.0377], sign-flip p = 0.0038) and so did mean lag-1 autocorrelation (−0.0146 [−0.0251, −0.0052], p = 0.0106), the two contrasts correlating at r = 0.953 across subjects. The AR(1) prediction from measured (a_x, a_y, q) reproduced the sts level to 4.3 % and the per-subject DiD at r = 0.989, over-predicting the group DiD by 14 %; the residual (+0.0115 [+0.0021, +0.0211], p = 0.042) is exploratory and unresolved. CCS-sts and ΦR did not carry the autocorrelation contrast; at lag 5, where DMT no longer changed r_τ, the sts contrast was null.

**Conclusions.** On autocorrelated fMRI a between-state contrast on Gaussian-MMI sts reports lag-1 autocorrelation change as synergy change whenever the manipulation changes autocorrelation. The DMT dataset demonstrates this; the diagnostic separates the components. Reporting r₁ beside sts, running the diagnostic, and considering CCS or longer lags are recommended.

---

## Introduction

Integrated Information Decomposition (ΦID; Mediano et al., 2021, 2025) extends partial information decomposition (Williams & Beer, 2010) to the time-delayed mutual information (TDMI) between the past and the future of two variables, splitting it into sixteen atoms that describe how each kind of information in the past (redundant, unique to either source, synergistic) becomes each kind in the future. In fMRI the atom that has drawn most attention is synergy-to-synergy, sts, read as the information that only the joint past of two regions carries about their joint future. On resting-state BOLD it separates a redundancy-dominated sensory core from synergy-dominated association cortex (Luppi et al., 2022); regions ranked by synergy form a "synergistic workspace" whose integrated information is reduced under propofol and in disorders of consciousness (Luppi et al., 2024); and group differences in the synergy and redundancy atoms have been reported in Alzheimer's disease, schizophrenia and neurodevelopmental conditions (Down et al., 2026; Nago et al., 2026; Dong et al., 2025). Almost all of this work uses the Gaussian estimator with the MMI redundancy function (Barrett, 2015) at a lag of one TR, on BOLD series whose lag-1 autocorrelation is high because of haemodynamic smoothing and band-pass filtering.

What sts indexes in that regime is assumed rather than derived. Under a Gaussian model every atom is a share of lag-1 predictability, and MMI assigns redundancy by taking the smaller of two mutual informations. Varley (2024) showed on discrete toy systems and one human fMRI subject that MMI cannot distinguish a synergistic pair from two independent autocorrelated processes, and that disintegrating a pair while preserving its autocorrelations can raise its apparent synergy. Not yet available are a closed-form account of how sts depends on the two quantities a pair of BOLD series actually has, its lag-1 autocorrelation and its zero-lag cross-correlation; a statement of where real region pairs sit on that map; a comparison with a redundancy function that does not share the property; and a diagnostic that separates the autocorrelation component of an observed synergy change from the remainder.

This study did not set out to provide these. It was pre-specified as a confirmatory test of whether whole-brain synergy is up-regulated under N,N-dimethyltryptamine (DMT), a state of intensified conscious content, against the workspace account's prediction that synergy indexes conscious level. Synergy decreased. Inspection of the full sixteen-atom table then showed that the decrease was carried by the quantity that carries the level, the pair's within-region self-prediction, and the question became what the estimator measures. The DMT contrast is the demonstration; the original pre-specified analysis and its results are in the supplement.

---

## Methods

### Dataset

Data are the preprocessed Schaefer-116 regional time series released by Singleton et al. (2025) at https://github.com/singlesp/DMT_NCT (Zenodo 10.5281/zenodo.15177511), acquired by Timmermann et al. (2023): fourteen subjects, each with a DMT run and a placebo (PCB) run of 840 TRs at TR = 2 s, intravenous injection at TR 240 (20 mg DMT fumarate over 30 s, 3 T, preprocessing as described by Timmermann et al., 2023 and Singleton et al., 2025); six of twenty participants were excluded by the source authors for head movement (Singleton et al., 2025). The analysed run is the continuous resting-state session; the intensity ratings supplied with the data (0–10, once per 30 TRs, 28 bins) were collected in a second, later session of the same day (Timmermann et al., 2023; Singleton et al., 2025; review, section 0.3.1) and enter no result reported here. The 28 bins of 30 TRs are kept as the global fit's averaging unit. Framewise displacement (FD) per TR is supplied. Two preprocessing variants were analysed: with global signal regression (`ts_gsr`, primary) and demeaned without it (`ts_demean`, sensitivity). The released series are band-limited to 0.01–0.08 Hz, which alone imposes r₁ ≈ 0.82 on white noise at TR = 2 s (`notes/review_computations_2026-09-14.md`, sections 1 and 3). One TR (subject index 2, PCB, TR 839) is non-finite in every region and was dropped.

The parcellation is Schaefer-100 (7-network order; Schaefer et al., 2018; Yeo et al., 2011) plus 16 subcortical parcels. Region 20 (0-based; `LH_DorsAttn_Post_6`) is constant across all 840 TRs of the DMT run of subject 8 in every variant including the raw series; the data authors confirmed that this parcel was a mean-filled replacement, poorly documented at the time (P. Singleton, personal communication, 14 September 2026). It was dropped for all subjects and both conditions before any result was computed, leaving 115 regions and 6,555 pairs, so that every within-subject contrast is over the same pair set. The release carries no licence file; the data are used under a collaborative agreement with the data collectors and the derivative authors, confirmed by email in September 2026. The subject ordering shared by the time series and FD files was verified at one subject (record, "Subject alignment across files").

### Estimator

ΦID atoms were computed with `phyid` (Imperial-MIND-lab, commit 6c5f2e9; Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1), `calc_PhiID(kind='gaussian', tau=1)` with `redundancy='MMI'` or `'CCS'`: a Gaussian model of the four-vector (x_t, y_t, x_{t+1}, y_{t+1}), sixteen local atoms per time point, in nats; whole-brain values are means over the 6,555 pairs. **Windowed (W = 60)**: each run cut into 14 non-overlapping 60-TR windows, each an independent fit on that window's samples alone; W = 30 (28 windows) as a second windowed estimator. **Global fit**: one Gaussian fitted to the full run, local atoms averaged into the 28 rating bins. The analytic work used a closed-form implementation of the same estimator (`notes/rev_phiid_fast.py`): the time mean of phyid's local Gaussian mutual information equals the plug-in log-determinant mutual information and the lattice inversion is linear, so window-mean atoms are closed-form functions of the window's 4 × 4 correlation matrix; it reproduces phyid's window means and global-fit bin means to ≤ 2.1 × 10⁻¹⁴ and its TR-local series to ≤ 1.1 × 10⁻¹³ on every saved output (`notes/review_results/logs/phiid_fast_validate.log`, `phiid_fast_validate_local.log`).

### The two redundancy functions and the CCS verification

Under MMI (Barrett, 2015) each single-target redundancy is the smaller of the two single-source mutual informations and the double redundancy rtr is the smallest of the four single-source, single-target mutual informations. Under CCS (Ince, 2017) redundancy is local co-information at the samples where the constituent local mutual informations and the co-information share a sign, and zero elsewhere. The `phyid` CCS could not be checked against the MATLAB reference it pins (pmediano/PhiID, commit a633cc1), which implements MMI only (`notes/partB2_ccs.md`), so we established what the code computes: its double redundancy is a double co-information D, retained where five local signs (the four single-source, single-target mutual informations and D itself) agree and zero elsewhere, and on the lattice D ≡ rtr − sts (deviation ≤ 3 × 10⁻¹⁵), so CCS-sts is 0 at sign-agreeing samples and −D elsewhere. An independent Gaussian implementation of Ince's construction agreed with `phyid` to 2.1 × 10⁻¹³ on 200 random draws of the real data, and a 56-sample binary hand case agreed to 3 × 10⁻¹⁵ (`notes/review_results/partB/ccs_verify.log`). The published definition of the double-redundancy step (Mediano et al., 2025) could not be retrieved during this work; the verification is against Ince's definition and the code's own algebra.

### Closed-form atoms of a bivariate AR(1) pair

Let x_t = a x_{t−1} + ε_t and y_t = a y_{t−1} + η_t be unit-variance stationary AR(1) processes with corr(ε_t, η_t) = q, so that corr(x_t, y_t) = q, corr(x_t, x_{t+1}) = a and corr(x_t, y_{t+1}) = aq; the correlation matrix of (x_t, y_t, x_{t+1}, y_{t+1}) is S₄ = [[1, q, a, aq], [q, 1, aq, a], [a, aq, 1, q], [aq, a, q, 1]], and every Gaussian mutual information is half the log-ratio of block determinants. Write S = −½ ln(1 − a²) and C = −½ ln(1 − a²q²). Then I(x_t; x_{t+1}) = I(y_t; y_{t+1}) = S and I(x_t; y_{t+1}) = I(y_t; x_{t+1}) = C; the (x_t, x_{t+1}, y_{t+1}) block has determinant (1 − a²)(1 − q²), so I(x_t; x_{t+1}, y_{t+1}) = S and likewise I(x_t, y_t; x_{t+1}) = S; and det S₄ = (1 − q²)²(1 − a²)², the conditional covariance of the future given the past being the innovation covariance, so TDMI = 2S, independent of q. MMI sets the four single-source, single-target redundancies to C, the two joint-target ones to S, and rtr = C. Inverting the lattice by the Möbius inversion of Mediano et al. (2021), under which atoms are not constrained to be non-negative: rtx = rty = xtr = ytr = xty = ytx = 0; xtx = yty = rts = str = S − C; xts = yts = stx = sty = −(S − C); and

sts = 2S − C = −ln(1 − a²) + ½ ln(1 − a²q²).

Hence sts − (xtx + yty) = C = rtr, exact at q = 0 and growing with |q|; rtr + sts = TDMI; ΦR = TDMI − I(x;x′) − I(y;y′) + rtr = C = rtr; and ∂sts/∂a = 2a/(1 − a²) − aq²/(1 − a²q²), ∂sts/∂q = −a²q/(1 − a²q²). The family has the Markov property corr(y_t, x_{t+1}) = corr(y_t, x_t) corr(x_t, x_{t+1}): the other region carries no information about a region's future beyond the region's own past, every cross-prediction atom is zero, and the pair's entire TDMI is self-prediction, of which MMI assigns all but the cross-lag mutual information C to sts. The identities were checked numerically to 4 × 10⁻¹⁵ over 2,000 seeded draws of (a, q) (`notes/review_results/partB/family_checks.log`). For unequal coefficients a_x ≠ a_y the same pipeline evaluates the matrix with cross-lag entries a_y q and a_x q numerically; there ΦR − rtr is not zero.

### The scope map

sts, xtx + yty, ∂sts/∂r₁ and ∂sts/∂q were evaluated on r₁ ∈ [0, 0.95] × q ∈ [−0.6, 0.6] (step 0.01; central differences, h = 0.001), on |q| ≤ 0.95, and on r ∈ [−0.95, 0.95]² for the lag analysis; a cell is r₁-dominated where |∂sts/∂r₁| > |∂sts/∂q|, q-dominated where the reverse holds, flat where both are below 10⁻³. Every pair of subject 1 was placed on the map (r₁ = mean of the two regions' within-window lag-1 autocorrelations, q = the pair's within-window lag-0 correlation) for both variants, both runs, windows 1–4 and 6 (`notes/partB1_scope_map.md`).

### The DMT contrast

Per subject the statistic is (post − pre) on DMT minus (post − pre) on PCB (DiD) for the whole-brain mean of a quantity. Pre-injection windows are 1–4 (bins 1–8); the primary post set is windows 6–14 (bins 11–28), window 5 (bins 9–10) being excluded before any windowed result because both arms show an injection response at bins 8–10 (record, "Pre-registered analysis choices", decay windows fixed 13 September 2026); the sensitivity set is windows 5–14, the early and late sets 6–9 and 10–14. Inference: exact sign-flip permutation over the 14 subjects (16,384 assignments, two-sided); mean DiD with a subject-bootstrap 95 % CI (10,000 draws); a temporal null in which the TR-resolution whole-brain local series is phase-randomised per subject and condition (1,000 surrogates; Prichard & Theiler, 1994) and re-averaged into the same windows; and motion control, in which window-mean values are regressed on window-mean FD within each subject and condition (OLS over the 14 windows) and the DiD recomputed on the residuals, "survives" meaning same sign with a bootstrap CI excluding zero. Two trend corrections were added after the primary result: (a) the placebo run's linear trend subtracted from both runs, (b) a shared slope fitted to both. The same engine (`notes/rev_inference.py`) was applied to every quantity: MMI-sts and CCS-sts, the other atoms, ΦR (= TDMI − I(X;X′) − I(Y;Y′) + rtr), the mean regional lag-1 autocorrelation (each region standardised within the window, the local product z_t z_{t+1} averaged over regions, whose window mean is the sample r₁ averaged over the 115 regions), the diagnostic's predicted and residual sts, and the lag variants. Seed 20261120 throughout; no multiplicity correction, since one whole-brain statistic per quantity, variant and window set is reported and none is selected among.

### The residual diagnostic

For every pair, subject, run and window, the measured 4 × 4 correlation matrix gives the observed sts. The prediction keeps the pair's measured lag-1 autocorrelations a_x, a_y and lag-0 correlation q and replaces the two cross-lag correlations by a_y q and a_x q, the AR(1) structure; predicted sts is the closed-form sts of that matrix, the residual is observed minus predicted, averaged over pairs, and the engine is run on the observed, predicted and residual series. The prediction recorded before the run (`notes/partB_prespec_2026-09-14.md`) was a residual DiD near zero; a residual DiD both significant and uncorrelated with r₁ was to be reported as exploratory evidence of an autocorrelation-independent component. Because the τ = 1 atoms depend only on lag-0 and lag-1 correlations, the diagnostic depends on the AR(1) assumption only through the cross-lag substitution.

### Bias simulations, the matched null, lag variants and deconvolution

Finite-sample bias of the windowed estimator was characterised before any windowed result on simulated VAR(1) processes with analytic ground truth (`02_bias_check.py`, 2,000 replicate windows per cell): the estimated between-condition sts difference had the true sign in every cell, with 52–77 % of the true difference absorbed at W = 30 and 15–45 % at W = 60, which is why W = 60 became the primary window with W = 30 as a positive control (record, "Pre-registered analysis choices"); the real regional autocorrelation function decays faster than either simulated family (pooled placebo ACF, lags 1–6: 0.868, 0.539, 0.172, −0.085, −0.174, −0.145), so no simulated shrinkage figure is applied to the real contrast. An sts-matched null (`notes/rev_sts_matched_null.py`) asked whether a covariance change at equal analytic sts can manufacture a difference, in three families (the record's asymmetric VAR(1); a VAR(1) at a = 0.87; Gaussian processes with the data's own placebo and post-DMT autocorrelation functions) with the second condition's parameters solved so that the analytic sts is unchanged, estimated over 4,000 independent windows at W = 30, 60 and 840. The decomposition was repeated with the lag-τ four-vector (x_t, y_t, x_{t+τ}, y_{t+τ}) for τ = 2, 3, 5 on `ts_gsr`, windowed and global, with the lag-τ autocorrelation contrast built in the same way; the prediction recorded beforehand was that r_τ falls with τ and the artefact weakens. As a sensitivity analysis the regional series were deconvolved with rsHRF 1.7.0 (Wu et al., 2013) and the pipeline rerun unchanged (review, section 3).

### Literature search for the applicability table

Published fMRI ΦID studies reporting Gaussian-MMI synergy on BOLD at TR ≈ 1–3 s were identified by web search on 14 September 2026 and their accessible Methods read for the quantity reported, preprocessing, parcellation, redundancy function, lag and any treatment of autocorrelation, with no critique of any paper by pre-specification. The search record, the table and the sources that could not be read are in the Supplement (S3; `notes/partB5_literature.md`).

### History of the study

The analysis was pre-specified in a git-tracked record (`manuscript/analysis_record.md`, initial commit 44cec4f, 12 September 2026) as a confirmatory test of the prediction that whole-brain synergy is up-regulated under DMT and tracks subjective intensity, with a directional-failure rule under which a significant decrease would be reported as a refutation. The windowed test, its window sets, nulls and motion rule were fixed before the windowed result existed (commits e16ebba to e46df8a), but the direction and approximate size of the effect were already known from the global fit, whose per-subject DiDs correlate at 0.95 with the windowed ones, and the hypothesis was committed alongside a real-data sanity run that showed the decrease; the windowed test fixed the estimator, windows, nulls and motion handling in advance of that computation only. The decrease was recorded (cb1b2cf); the intensity-tracking claim was void under its controls. An adversarial review (14 September 2026) and inspection of all sixteen atoms established that the decrease was carried by the self-prediction atoms and reproduced by the lag-1 autocorrelation contrast, and the study was reframed; an exploration of ΦR, including HRF deconvolution and a regional test with a prediction recorded in advance, was closed by a dated entry recording why its positive whole-brain result supports no claim (record, "Closure entry", commit b4f98a8). The present analyses were pre-specified on 14 September 2026 with predictions recorded before computation (commit 477cccc) and committed one by one; the original analysis and its full results are in the supplement.

---

## Results

### 1. The sixteen atoms under MMI and CCS

Table 1 gives every atom's whole-brain mean in the DMT pre-injection windows and its primary DiD under both redundancy functions (`ts_gsr`, W = 60; `notes/review_results/partB/ccs_tables.md`). Under MMI the table has the structure the closed form predicts: sts (+1.1554 nats) is within 8 % of xtx + yty, rts and str are each about half of it, and four large negative atoms (permitted by the lattice's Möbius inversion, Mediano et al., 2021) almost entirely offset the "synergy block" sts + rts + str; under DMT the four negative atoms rose while the block fell, so the block's net change is a small fraction of the change in TDMI. Under CCS the self-prediction atoms and their DiDs are almost unchanged, the four negative atoms and rts, str are near zero, and sts is negative and 3 % of the MMI value in magnitude; sts ≈ xtx + yty holds under MMI only, on both variants and both estimators.

**Table 1. Whole-brain mean atoms, DMT pre-injection windows 1–4, and primary DiD (windows 6–14 minus 1–4, DMT minus placebo), `ts_gsr`, W = 60, nats; DiD as mean (subjects negative of 14). Sources: `notes/review_results/partB/ccs_tables.md`; MMI negative counts from `notes/review_results/partB/lag_tables.md` (τ = 1).**

| atom | MMI level | MMI DiD | CCS level | CCS DiD |
|---|---|---|---|---|
| rtr | +0.0388 | −0.0078 (10) | +0.0916 | −0.0124 (10) |
| rtx | +0.0258 | −0.0012 (9) | +0.0008 | +0.0007 (5) |
| rty | +0.0254 | −0.0012 (9) | +0.0001 | +0.0011 (4) |
| rts | +0.5669 | −0.0407 (12) | −0.0038 | −0.0008 (10) |
| xtr | +0.0254 | −0.0012 (9) | +0.0005 | +0.0008 (4) |
| xtx | +0.6273 | −0.0523 (12) | +0.6245 | −0.0515 (12) |
| xty | −0.0254 | +0.0012 (5) | −0.0279 | +0.0016 (6) |
| xts | −0.5352 | +0.0399 (2) | +0.0633 | −0.0026 (9) |
| ytr | +0.0258 | −0.0012 (9) | +0.0004 | +0.0010 (4) |
| ytx | −0.0258 | +0.0012 (5) | −0.0281 | +0.0018 (7) |
| yty | +0.6125 | −0.0396 (13) | +0.6105 | −0.0394 (12) |
| yts | −0.5358 | +0.0404 (2) | +0.0622 | −0.0020 (10) |
| str | +0.5667 | −0.0408 (12) | −0.0039 | −0.0008 (10) |
| stx | −0.5350 | +0.0401 (2) | +0.0634 | −0.0027 (9) |
| sty | −0.5357 | +0.0403 (2) | +0.0623 | −0.0021 (9) |
| sts | +1.1554 | −0.0809 (13) | −0.0387 | +0.0036 (4) |
| TDMI (Σ 16) | +1.4772 | −0.1037 | +1.4772 | −0.1037 |

### 2. The scope map, where real pairs sit, and what DMT changes

On the AR(1) family sts is even in q, decreasing in |q| and steeply increasing in r₁: at q = 0 it is 0.041 (r₁ = 0.2), 0.446 (0.6), 1.022 (0.8), 1.282 (0.85), 1.661 (0.9), 2.328 (0.95), and at r₁ = 0.85 it falls from 1.282 to 1.131 as |q| goes from 0 to 0.6 (`notes/review_results/partB/scope_map_tables.md`). |∂sts/∂r₁| exceeds |∂sts/∂q| at every grid point except the line r₁ = 0: there is no q-dominated region on the requested grid, on |q| ≤ 0.95 (0 of 18,336 cells) or on r ∈ [−0.95, 0.95]² (0 of 36,481). At the operating point (0.85, 0.25) used for all derivative values quoted in this paper the derivatives are 6.07 and −0.19 nats per unit (ratio 32); at (0.85, 0.6) they are 5.71 and −0.59 (10); the grid minimum of the ratio is 6.55 at (0.61, ±0.6). Real pairs sit in the steep part: for subject 1 (both variants, both runs, windows 1–4 and 6) 100 % of the 6,555 pairs fall in the r₁-dominated region in all 20 cells, with pair r₁ medians 0.816–0.867 and median |q| 0.22–0.41; the lag-1 autocorrelation of ideal band-passed white noise at the band-pass and TR settings of the published studies whose settings are stated is 0.78–0.93 (`notes/partB5_literature.md`, Table B; `notes/review_results/partB/family_checks.log`), so those datasets sit in the same region.

DMT changes r₁. The whole-brain mean lag-1 autocorrelation fell relative to placebo: DiD −0.0146 [−0.0251, −0.0052], sign-flip p = 0.0106, negative in 12 of 14, phase-randomised p = 0.0729, FD-residualised −0.0123 [−0.0199, −0.0041], p = 0.0135 (`ts_gsr`); −0.0216 [−0.0319, −0.0116], p = 0.0017, phase p = 0.0390 (`ts_demean`) (`notes/review_results/inference_rows_raw.csv`). Projected through the map at the pairs' own point (r₁, |q|) = (0.848, 0.24), where ∂sts/∂r₁ = 5.99, the `ts_gsr` change maps to −0.087 nats against an observed sts DiD of −0.081. DMT's effect on q is small on the map's scale: mean pair |q| moved from 0.284 to 0.266 on DMT against 0.284 to 0.282 on placebo (DiD −0.0164, negative in 10 of 14; `ts_gsr` W = 60, post-hoc supplement, exploratory; `notes/review_results/partB/residual_source.log`), on `ts_demean` the signed mean pairwise correlation rose (DiD +0.052638 [+0.007337, +0.097622], p = 0.0470; `results/global_fc_did_ts_demean.csv`), and a change of 0.01 in |q| moves sts by 0.002 at the pairs' point.

### 3. The DMT contrast on MMI-sts, its robustness, and the autocorrelation contrast

Table 2 gives the primary step contrast (`results/primary_b_ts_gsr_win60.csv`, `results/primary_b_ts_demean_win60.csv`). Whole-brain MMI-sts fell on the DMT run and rose on the placebo run: DiD −0.0809 nats [−0.1261, −0.0377], sign-flip p = 0.0038, phase-randomised p = 0.0020, negative in 13 of 14 subjects, −7.0 % of the pre-injection DMT mean, surviving FD residualisation; without global signal regression −0.1031 [−0.1558, −0.0522], p = 0.0026. The contrast held at W = 30 (−0.0686 [−0.1084, −0.0293], p = 0.0042; `results/primary_b_ts_gsr_win30.csv`), at the global fit (−0.0801 [−0.1303, −0.0310], p = 0.0071; `results/global_fc_did_ts_gsr.csv`), and, in checks added after the primary result (post-hoc), in the early and late sets (−0.1029, p = 0.0009; −0.0633, p = 0.0337, the placebo rise carrying 0.69 of the late DiD), under both trend corrections (−0.0890, p = 0.0021; −0.0995, p = 0.0007; review, section 4), and in all 28 leave-one-out refits (`results/loo_did_win60.csv`). The pre-specified direction was an increase; under the directional-failure rule this is a refutation of the up-regulation hypothesis. In a post-hoc check with its rule recorded before it was run, sts fell in proportion to TDMI: the ratio sts / TDMI did not change (DiD +0.0005 [−0.0081, +0.0083], p = 0.91; `results/proportionality.csv`).

**Table 2. Primary step contrast, whole-brain mean MMI-sts, W = 60, windows 6–14 vs 1–4 (nats; N = 14; sign-flip p two-sided; subject-bootstrap 95 % CI). Source: `results/primary_b_*_win60.csv`.**

| | ts_gsr | ts_demean |
|---|---|---|
| Pre-injection DMT / PCB mean | 1.1554 / 1.1378 | 1.1004 / 1.0819 |
| DMT post − pre | −0.0485 [−0.0819, −0.0113], p = 0.0267 | −0.0633 [−0.1088, −0.0123], p = 0.0333 |
| PCB post − pre | +0.0324 [+0.0053, +0.0606], p = 0.0425 | +0.0398 [+0.0089, +0.0692], p = 0.0306 |
| DiD raw | −0.0809 [−0.1261, −0.0377], p = 0.0038; phase p = 0.0020; 13/14 negative | −0.1031 [−0.1558, −0.0522], p = 0.0026; phase p = 0.0010; 12/14 negative |
| FD DiD | +0.0143 [−0.0070, +0.0365], p = 0.2452 | same |
| DiD FD-residualised | −0.0649 [−0.0966, −0.0289], p = 0.0048; 13/14 | −0.0824 [−0.1224, −0.0372], p = 0.0048; 13/14 |

The sts contrast and the autocorrelation contrast are the same contrast twice. Per subject the MMI-sts DiD and the lag-1 autocorrelation DiD correlate at Pearson r = 0.953 (Spearman 0.903) on `ts_gsr` and 0.96 (0.93) on `ts_demean`; across the 28 condition × window group means the two series correlate at 0.977 and 0.938 (review, section 1; `notes/review_results/partB/ccs_tables.md`). The autocorrelation contrast has the sts contrast's structure in every respect examined: the placebo run's own r₁ rises across the session and carries 0.34 of the DiD (sts: 0.40), the early set is larger (−0.0213, p = 0.0006) than the late (−0.0093, p = 0.1615), and both survive the trend corrections.

CCS-sts does not carry the autocorrelation contrast (Table 4). Its DiD is 4–31 % of MMI's in magnitude and positive in every cell (exploratory); per subject it is uncorrelated with the autocorrelation contrast in every cell (r = −0.439, −0.253, −0.390, −0.207; all p ≥ 0.117), whereas the CCS xtx + yty DiD is (r = 0.955, 0.961, 0.932, 0.911); across the 28 group means CCS-sts correlates with mean r₁ at −0.433 against +0.977 for MMI-sts, and per pair within a window at −0.011 and +0.003 against +0.742 and +0.697 (subject 1, DMT window 6 and placebo window 2; `notes/review_results/partB/ccs_tables.md`). The sign of the CCS-sts change is exploratory and no interpretation is attached to it. ΦR, the quantity of the workspace account, did not change on the primary estimator and variant (+0.0007 [−0.0078, +0.0100], p = 0.8971, phase p = 0.8372, every window set and trend correction null); in no cell was the primary-set sign-flip p below 0.05, and the three cells with phase p below 0.05 disagree in sign across variants (review, section 2).

**Table 4. Primary DiD of CCS-sts and of ΦR by cell (nats; sign-flip p; phase-randomised p; subjects negative of 14). The CCS-sts contrast is reported as exploratory. Sources: `notes/review_results/inference_rows_ccs.csv`, `inference_rows_raw.csv`.**

| cell | CCS-sts DiD [CI], p, phase p, neg/14 | r(CCS-sts DiD, autocorrelation DiD) | ΦR DiD [CI], p, phase p, neg/14 |
|---|---|---|---|
| ts_gsr W60 | +0.0036 [−0.0001, +0.0072], 0.084, 0.016, 4 | −0.439 | +0.0007 [−0.0078, +0.0100], 0.8971, 0.8372, 8 |
| ts_gsr global | +0.0210 [+0.0154, +0.0270], 0.0001, 0.0010, 0 | −0.253 | −0.0062 [−0.0127, +0.0003], 0.0953, 0.0230, 9 |
| ts_demean W60 | +0.0134 [+0.0056, +0.0221], 0.0052, 0.0030, 3 | −0.390 | +0.0157 [+0.0010, +0.0326], 0.0853, 0.0380, 4 |
| ts_demean global | +0.0321 [+0.0216, +0.0431], 0.0001, 0.0010, 0 | −0.207 | +0.0180 [−0.0002, +0.0380], 0.1177, 0.0190, 5 |

### 4. The residual diagnostic

Table 3 summarises the diagnostic (`notes/review_results/partB/diag_tables.md`, `notes/review_results/inference_rows_diag.csv`). The prediction from each pair's measured (a_x, a_y, q) alone reproduces the observed sts level to within 4.3 % at W = 60 and more closely at the run level, over-predicting, with a residual SD a fifth of the observed sts's across the 392 cells; the symmetric-coefficient prediction over-predicts by 16 %. The predicted DiD has the observed sign in every cell, over-shoots it by 14–29 %, and tracks it per subject (Table 3).

The residual DiD (exploratory throughout this paragraph) is positive in every cell, with a CI excluding zero and both nulls below 0.05 in all four windowed cells (Table 3), survives FD residualisation, and is concentrated in the early set. Neither recorded outcome obtained as worded: the residual DiD is not near zero by this study's conventions, and it is not uncorrelated with r₁ (Table 3: the subjects whose r₁ fell more show the larger over-prediction), so the pre-specified signature of an autocorrelation-independent component is not met and the residual is reported as exploratory and unresolved. A post-hoc supplement (`ts_gsr` W = 60 only; `notes/review_results/partB/residual_source.log`) locates the whole residual in the diagnostic's single model assumption, corr(x_t, y_{t+1}) = a_y q: the measured cross-lag correlations scatter about a_y q with no mean offset, the residual is more negative where pair a and |q| are higher, and the positive residual DiD is that over-prediction shrinking as a and |q| fall under DMT (exploratory).

**Table 3. The residual diagnostic: sts predicted from measured (a_x, a_y, q) per pair, nats. The residual rows are exploratory; the W = 30 rows are an addition beyond the pre-specified plan. Source: `notes/review_results/partB/diag_tables.md`.**

| cell | observed level | predicted | residual (% of observed) | observed DiD | predicted DiD [CI], p | residual DiD [CI], sign-flip p, phase p, negative/14 | r(predicted DiD, observed DiD) | r(residual DiD, autocorrelation DiD) |
|---|---|---|---|---|---|---|---|---|
| ts_gsr W60 | 1.1377 | 1.1865 | −0.0489 (−4.3 %) | −0.0809 | −0.0924 [−0.1444, −0.0414], 0.0037 | +0.0115 [+0.0021, +0.0211], 0.042, 0.019, 4 | +0.989 | −0.780 |
| ts_gsr W30 | 1.0082 | 1.1062 | −0.0980 (−9.7 %) | −0.0686 | −0.0869 [−0.1368, −0.0373], 0.0046 | +0.0182 [+0.0066, +0.0299], 0.014, 0.0040, 2 | +0.987 | −0.825 |
| ts_demean W60 | 1.0802 | 1.1181 | −0.0378 (−3.5 %) | −0.1031 | −0.1213 [−0.1776, −0.0631], 0.0022 | +0.0182 [+0.0089, +0.0277], 0.0040, 0.018, 2 | +0.990 | −0.597 |
| ts_demean W30 | 0.9636 | 1.0471 | −0.0835 (−8.7 %) | −0.0877 | −0.1136 [−0.1648, −0.0596], 0.0021 | +0.0259 [+0.0135, +0.0383], 0.0020, 0.0090, 3 | +0.981 | −0.604 |
| ts_gsr global (run-level) | 1.2883 | 1.3021 | −0.0137 (−1.1 %) | −0.0801 | constant within run | = observed by construction | — | — |
| ts_demean global | 1.2205 | 1.2197 | +0.0008 (+0.1 %) | −0.1035 | constant within run | = observed by construction | — | — |

### 5. Lag dependence

Table 5 gives the lag variants (`ts_gsr`, W = 60; `notes/review_results/partB/lag_tables.md`). As predicted, r_τ falls with τ and the artefact weakens: the sts contrast is significant on both nulls at both estimators wherever the lag-τ autocorrelation contrast is (τ = 1, 2, 3) and null where it is not (τ = 5), and per subject it tracks the lag-τ autocorrelation contrast at every lag, with the sign reversed at τ = 5 because r₅ is negative and every AR(1) atom is even in the autocorrelation. No lag moves the pairs into a region where q contributes comparably, because no such region exists on the family; the pairs are r-dominated at every τ (100, 100, 97.7, 99.5 %, the remainder flat at r_τ ≈ 0).

**Table 5. Lag dependence, `ts_gsr`, W = 60 (nats; DMT pre-injection means; primary DiD with sign-flip p). Source: `notes/review_results/partB/lag_tables.md`.**

| τ | mean r_τ | sts level | sts DiD [CI], p | lag-τ autocorrelation DiD, p | r(sts DiD, r_τ DiD) per subject |
|---|---|---|---|---|---|
| 1 | 0.848 | 1.1554 | −0.0809 [−0.1261, −0.0377], 0.0038 | −0.0146, 0.0106 | +0.953 |
| 2 | 0.513 | 0.1797 | −0.0429 [−0.0654, −0.0204], 0.0037 | −0.0468, 0.0090 | +0.970 |
| 3 | 0.139 | 0.0262 | −0.0043 [−0.0063, −0.0022], 0.0018 | −0.0681, 0.0132 | +0.626 |
| 5 | −0.202 | 0.0415 | −0.0024 [−0.0073, +0.0022], 0.3688 | −0.0108, 0.5670 | −0.832 |

### 6. Estimator manufacture and the case for the global fit

Where an sts-matched pair of conditions can be built (equal analytic sts, different covariance), the windowed estimator manufactures a difference at W = 60 of −9 %, +16 %, +7 % ± 8 % and −8 % ± 6 % of the real DiD in the four matched pairs, of either sign, and at W = 30 up to +33 %; at the full run length it is ≤ 2 % except in one family (+29 %) (review, section 5). A matched pair in which r₁ falls by the observed amount could not be built at data-like autocorrelation, because the analytic sts is a steep function of r₁ (≈ +0.07 nats per +0.01 near 0.87) and a weak function of q; the observed autocorrelation-function change alone, at fixed q, changes the true sts by −0.069 against the observed DiD of −0.081, and the W = 60 estimator returns −0.056 of it. The windowed whole-brain sts sits 0.1531 nats below the global fit in the DMT pre-injection windows (1.1554 against 1.3085); the diagnostic decomposes that gap into the lower within-window parameters, which the prediction from the window's own (a_x, a_y, q) captures, and a residual of −0.0489 against −0.0137 at the run level. For a between-state contrast that does not need time resolution within a run, the global fit gave the same contrast (−0.0801 against −0.0809), a run-level residual of 1.1 % and manufactured differences of ≤ 2 % at 840 samples in three of the four matched families (+29 % in the fourth); its per-bin values are local atoms under a single run-level covariance, not per-bin decompositions.

---

## Discussion

### What the finding is and is not

On the bivariate AR(1) family the Gaussian-MMI synergy atom is self-prediction plus rtr, balanced by four negative atoms (Mediano et al., 2021) that have no counterpart under CCS, and its dependence on r₁ dominates its dependence on q everywhere the map was evaluated. This is a property of the estimator, sensitive to both r₁ and q, and it says nothing about whether synergy in the intended sense is present in the brain. What follows for a between-state contrast is narrow and exact: when the manipulation changes r₁, the MMI-sts contrast reports that change, scaled by ∂sts/∂r₁, whether or not anything the word "synergy" is meant to capture has changed. DMT changed r₁ and barely moved q on the map's scale, and is the demonstration, not the finding. The residual is the one part of the DMT result that the account does not reduce to autocorrelation; it did not meet the criterion fixed in advance for an autocorrelation-independent component, it is exploratory and unresolved, and nothing further is claimed for it.

### MMI-specificity, and what CCS costs

The property is MMI-specific under the rule recorded before the CCS computation. The cost of CCS is what the construction makes explicit: its double redundancy is a masked double co-information, so CCS-sts is −D averaged over the samples where five local signs disagree, it takes negative values, and its double-redundancy step has no published text we could check. Whether its small positive DMT change means anything is a question these data do not answer (exploratory). CCS is not offered as the corrected estimator, only as the one that does not carry the autocorrelation contrast.

### A distinction for applicability

Two uses of MMI-sts should be distinguished. A between-state contrast within subjects, as here, is exposed whenever the state changes r₁; BOLD autocorrelation changes with anaesthetic depth and in disorders of consciousness (Huang et al., 2018), and under DMT as this dataset shows. A spatial map of synergy across regions is exposed through regional differences in r₁: the map predicts higher sts where r₁ is higher, with rtr almost unmoved, so a regional autocorrelation gradient would produce a synergy-minus-redundancy gradient of the same spatial form. Whether that is what any published map shows depends on that dataset's regional r₁, which none of the studies we could read reports; we apply the distinction to no specific published result. Two limits on reach follow from the identities of Methods: a change in q moves synergy and redundancy oppositely by equal amounts while a change in r₁ leaves rtr almost untouched, so a pattern of synergy and redundancy moving in opposite directions is not the r₁ signature; and ΦR = rtr on the symmetric family, so the r₁-dominance result for sts does not carry over to ΦR. Among the studies reporting synergy on BOLD that we could read (Supplement S3), none addressed autocorrelation, Varley (2024) being the study whose subject it is.

### Recommendations

Report the mean lag-1 autocorrelation beside sts, per condition and subject, and its contrast beside the sts contrast; if the two are collinear across subjects the sts result adds nothing to the autocorrelation result. Run the residual diagnostic: predict each pair's sts from its measured (a_x, a_y, q), test the residual with the same inference as the observed contrast, and state the cross-lag assumption. Consider CCS, with the costs above. Consider τ > 1, with its signal cost: a longer lag reduces the artefact by reducing everything, and at no lag do the pairs leave the r₁-dominated region (Results 5). Consider HRF deconvolution with its own risks: here it left the sts contrast and its collinearity with the autocorrelation contrast in place and created artefacts in ΦR absent on the raw series (post-hoc, exploratory; Supplement S2).

### Limitations

One dataset, one drug, one parcellation, N = 14; effect sizes are reported with CIs and the demonstration is a proof of concept. The AR(1) family does not fit the data beyond lag 1; the map's q-axis and the diagnostic's cross-lag substitution are AR(1) statements, and the residual they leave is unresolved (exploratory). There is no ground truth for synergy in these data: the analysis establishes what the estimator responds to, not what the brain does. Two redundancy functions were examined, both Gaussian and continuous; the discrete CCS on binarised data used elsewhere was not. The windowed estimator's finite-sample manufacture is not removed by the diagnostic. The pre-specification history is as stated in Methods: the confirmatory test was of a different hypothesis, its direction was known from the global fit before the windowed rules were written, and the present analyses were pre-specified on the day they were run; the git record establishes ordering, not blindness.

---

## Supplement (pointer)

S1. The original pre-specified analysis and its results: the up-regulation hypothesis, the directional-failure rule, the windowed test, the intensity-tracking criterion with its controls and the void verdict, the redundancy prediction, the exploratory regional analysis, the EEG Lempel-Ziv check, robustness across estimators, and the commit-by-commit audit trail (`manuscript/draft.md`, kept as a record; `manuscript/supplementary.md`, Tables S1–S8; `manuscript/prespecification_summary.md`).

S2. The ΦR exploration (every result in it exploratory) and why it was closed: ΦR with full inference on the raw series; HRF deconvolution and its effect on every quantity; the deconvolved whole-brain ΦR increase and the regional test against a prediction recorded before it was run; the reasons the increase supports no claim (a pre-injection baseline gap in the direction that creates it and a placebo-run decline present within the pre-injection windows, both absent on the raw series; estimator disagreement; a 56–64 % placebo share); and the closure entry (`manuscript/analysis_record.md`; `notes/review_computations_2026-09-14.md`; `notes/regional_phir_deconv_2026-09-14.md`).

S3. The full applicability table with its search record and blocked sources (`notes/partB5_literature.md`); the scope-map tables and figure, the CCS verification log, the lag tables, the diagnostic tables and the matched-null tables (`notes/review_results/partB/`).

---

## Data and code availability

Time series, ratings, framewise displacement and the EEG regressor are from https://github.com/singlesp/DMT_NCT (Singleton et al., 2025; Zenodo 10.5281/zenodo.15177511; upstream commit 77af7aa), cloned into `external/DMT_NCT/` and not redistributed. Analysis code, the pinned environment (`requirements.lock.txt`), every results table with the git SHA that produced it, the pre-specification record, the review and Part B notes with their result files, and the closed-form implementation are at https://github.com/Vasilis540/dmt-phiid. Seed 20261120 throughout.

## Author contributions (CRediT)

V.S.: conceptualisation, methodology, software, formal analysis, investigation, data curation (secondary), writing — original draft, writing — review and editing, visualisation, project administration. C.T.: resources (data acquisition), writing — review and editing [TK]. [TK: further contributors nominated by C.T.; P. Singleton: resources (data release) [TK]].

## Conflicts of interest

V.S. is preparing an application for a PhD position in the Cognition and Consciousness Imaging Group, Division of Anaesthesia, University of Cambridge, whose members authored Luppi et al. (2022, 2024), the studies whose estimator this paper analyses; this work was produced in part as evidence of competence for that application. C.T. is a co-author of Timmermann et al. (2023), the source of the data, and of Singleton et al. (2025) [TK: confirm]. No other conflicts are declared [TK].

## AI-use statement

Analysis code, verification scripts, the adversarial review, the Part B computations and the manuscript drafts were produced with the assistance of an AI system (Claude, Anthropic; model Claude Fable 5.1) working under the direction of V.S., in sessions whose outputs are committed to the repository with the session identified in the commit trailers. Every number in this paper was checked against its source file by an independent verification pass before commit. V.S. takes responsibility for the analysis, the text and the claims [TK: journal-specific wording].

---

## References

[TK: author lists, volumes and page ranges to be verified against each DOI before submission; entries marked † were read only through the accessible web pages listed in `notes/partB5_literature.md`.]

Barrett, A. B. (2015). Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems. *Physical Review E*, 91, 052802. https://doi.org/10.1103/PhysRevE.91.052802

Dong, [TK initials], et al. (2025). Dynamic synergy network analysis reveals stage-specific regional dysfunction in Alzheimer's disease. *Brain Sciences*, 15(6), 636. https://doi.org/10.3390/brainsci15060636 †

Down, K. J. A., Huntley, J., Mediano, P. A. M., & Bor, D. (2026). Synergistic and redundant information dynamics are modulated by Alzheimer's disease and cognitive impairment. *bioRxiv*, 10.64898/2026.02.18.706630 [TK: journal version, PubMed 41757079]. †

Gatica, M., Atkinson-Clement, C., Mediano, P. A. M., Alkhawashki, M., Ross, J., Sallet, J., & Kaiser, M. (2024). Transcranial ultrasound stimulation effect in the redundant and synergistic networks consistent across macaques. *Network Neuroscience*, 8(4), 1032–[TK]. †

Huang, Z., Liu, X., Mashour, G. A., & Hudetz, A. G. (2018). Timescales of intrinsic BOLD signal dynamics and functional connectivity in pharmacologic and neuropathologic states of unconsciousness. *Journal of Neuroscience*, 38(9), 2304–2317. https://doi.org/10.1523/JNEUROSCI.2545-17.2018

Ince, R. A. A. (2017). Measuring multivariate redundant information with pointwise common change in surprisal. *Entropy*, 19(7), 318. https://doi.org/10.3390/e19070318

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Holland, N., Fryer, T. D., O'Brien, J. T., Rowe, J. B., Menon, D. K., Bor, D., & Stamatakis, E. A. (2022). A synergistic core for human brain evolution and cognition. *Nature Neuroscience*, 25, 771–782. https://doi.org/10.1038/s41593-022-01070-0

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Allanson, J., Pickard, J. D., Carhart-Harris, R. L., Williams, G. B., Craig, M. M., Finoia, P., Owen, A. M., Naci, L., Menon, D. K., Bor, D., & Stamatakis, E. A. (2024). A synergistic workspace for human consciousness revealed by Integrated Information Decomposition. *eLife*, 12, RP88173. https://doi.org/10.7554/eLife.88173.4

Mediano, P. A. M., Rosas, F. E., Luppi, A. I., Carhart-Harris, R. L., Bor, D., Seth, A. K., & Barrett, A. B. (2021). Towards an extended taxonomy of information dynamics via Integrated Information Decomposition. *arXiv*, 2109.13186.

Mediano, P. A. M., Rosas, F. E., Luppi, A. I., et al. (2025). Toward a unified taxonomy of information dynamics via Integrated Information Decomposition. *Proceedings of the National Academy of Sciences*, [TK volume], e2423297122. https://doi.org/10.1073/pnas.2423297122 [TK: not accessible during this work]

Nago, [TK initials], et al. (2026). Synergistic and redundant information dynamics exhibit dissociable alterations across schizophrenia and neurodevelopmental conditions. *Brain Informatics*, 13, 25. https://doi.org/10.1186/s40708-026-00312-2 †

Prichard, D., & Theiler, J. (1994). Generating surrogate data for time series with several simultaneously measured variables. *Physical Review Letters*, 73, 951–954. https://doi.org/10.1103/PhysRevLett.73.951

Schaefer, A., Kong, R., Gordon, E. M., Laumann, T. O., Zuo, X.-N., Holmes, A. J., Eickhoff, S. B., & Yeo, B. T. T. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28, 3095–3114. https://doi.org/10.1093/cercor/bhx179

Singleton, S. P., Timmermann, C., Luppi, A. I., Eckernäs, E., Roseman, L., Carhart-Harris, R. L., & Kuceyeski, A. (2025). Network control energy reductions under DMT relate to serotonin receptors, signal diversity, and subjective experience. *Communications Biology*, 8, 631. https://doi.org/10.1038/s42003-025-08078-9

Timmermann, C., Roseman, L., Haridas, S., Rosas, F. E., Luan, L., Kettner, H., Martell, J., Erritzoe, D., Tagliazucchi, E., Pallavicini, C., Girn, M., Alamia, A., Leech, R., Nutt, D. J., & Carhart-Harris, R. L. (2023). Human brain effects of DMT assessed via EEG-fMRI. *Proceedings of the National Academy of Sciences*, 120, e2218949120. https://doi.org/10.1073/pnas.2218949120

Varley, T. F. (2024). Considering dynamical synergy and integrated information; the unusual case of minimum mutual information. *arXiv*, 2407.16601. Preprint, not peer reviewed.

Williams, P. L., & Beer, R. D. (2010). Nonnegative decomposition of multivariate information. *arXiv*, 1004.2515.

Wu, G.-R., Liao, W., Stramaglia, S., Ding, J.-R., Chen, H., & Marinazzo, D. (2013). A blind deconvolution approach to recover effective connectivity brain networks from resting state fMRI data. *Medical Image Analysis*, 17, 365–374. https://doi.org/10.1016/j.media.2013.01.003

Yeo, B. T. T., Krienen, F. M., Sepulcre, J., Sabuncu, M. R., Lashkari, D., Hollinshead, M., Roffman, J. L., Smoller, J. W., Zöllei, L., Polimeni, J. R., Fischl, B., Liu, H., & Buckner, R. L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. *Journal of Neurophysiology*, 106, 1125–1165. https://doi.org/10.1152/jn.00338.2011
