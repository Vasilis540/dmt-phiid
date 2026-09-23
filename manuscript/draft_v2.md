# The Gaussian-MMI synergy atom of integrated information decomposition is mostly self-prediction: a closed form on the AR(1) family and a within-subject DMT fMRI application

Short title: The MMI synergy atom of ΦID is mostly self-prediction

Vasilis Sampalis¹, Christopher Timmermann² [TK], S. P. Singleton³ [TK], [TK further co-authors nominated by C.T.]

¹ Independent researcher, Athens, Greece. ² [TK affiliation]. ³ [TK affiliation]

Correspondence: sampalisvasilis@gmail.com

---

## Abstract

Integrated information decomposition (ΦID) with the minimum-mutual-information (MMI) redundancy function underlies most fMRI synergy reports. We derive the sixteen Gaussian-MMI atoms of a bivariate first-order autoregressive (AR(1)) pair in closed form. With equal coefficients the synergy atom sts equals the two self-prediction atoms plus the double redundancy, balanced by four negative atoms; with unequal coefficients MMI takes the smaller self-information and sts falls below that sum. sts therefore inherits self-information's dependence on lag-1 autocorrelation r₁: at the operating point of fMRI region pairs, 0.01 of r₁ moves it by 0.061 nats and 0.1 of the lag-0 correlation |q| by 0.019, about 4.7 to 1 per standard deviation across pairs within windows, while lagged coupling moves it non-monotonically, with a sign set by the sign of q. In within-subject fMRI of 14 volunteers given N,N-dimethyltryptamine (DMT) and placebo, the primary contrast, the pre/post difference-in-differences of whole-brain MMI-sts, was planned to test an increase; its statistic was fixed after global fits on the same data had shown a decrease. sts fell (−0.081 nats [−0.132, −0.031], p = 0.004, 13 of 14) with r₁ (−0.015), in close to the proportion a generator with the data's spectrum produces; across subjects the two changes share their reliable variance (cross-half r = 0.69, ceiling 0.73). The regional sts map follows regional r₁ (r = 0.86, 115 regions). Recomputed with AR(1) cross-lags at each pair's measured autocorrelations and lag-0 correlation, sts falls by 0.092; the remainder exceeds what a pure autocorrelation change produces in simulation only weakly (p = 0.11) and cannot be attributed on these data. Under the common-change-in-surprisal (CCS) redundancy function the synergy atom is near zero but moves inversely with r₁, and prewhitening cannot remove the dependence from band-passed data. We recommend reporting r₁ beside sts and each sts contrast beside its AR(1)-substituted estimate.

## Author summary

Functional brain imaging asks how regions carry information together, not only which are active. A widely used measure, from integrated information decomposition, is synergy: information that a pair of regions holds jointly and neither holds alone. Synergy has been reported to differ across the cortex, and integrated information built from it to fall under anaesthesia and in disorders of consciousness. We show that, with the estimator most of these studies use, the synergy value is mostly something simpler: how well each region's signal predicts its own next sample, its lag-1 autocorrelation. We derive this on a solvable mathematical family and examine it in functional MRI from fourteen volunteers scanned under the psychedelic DMT and placebo. Under DMT the measured synergy fell, and so did the autocorrelation of the signals, in close to the proportion a simulation with the data's properties produces; across volunteers the two falls went together. We had set out to test the opposite hypothesis, that DMT raises synergy, and we report its refutation and what we found instead. We recommend that studies report autocorrelation beside synergy and compare each synergy contrast with the estimate our closed form gives from the regions' own autocorrelations.

---

## Introduction

Integrated Information Decomposition (ΦID; Mediano et al., 2021, 2025) extends partial information decomposition (Williams & Beer, 2010) to the time-delayed mutual information (TDMI) of two variables, splitting it into sixteen atoms that map each kind of past information (redundant, unique, synergistic) to each kind of future information. In fMRI most attention has gone to synergy-to-synergy, sts, read as information that only the two regions' joint past carries about their joint future. On resting-state BOLD it separates redundancy-dominated sensory and motor cortex from a synergy-dominated association cortex, the 'synergistic core' (Luppi et al., 2022). Regions where synergy predominates over redundancy, by rank, form a 'synergistic workspace' whose integrated information (ΦR) is reduced under propofol and in disorders of consciousness (Luppi et al., 2024). Of the nine studies read (S3 Text), seven state the MMI redundancy function (Barrett, 2015; Mediano et al., 2021), six of them with a Gaussian estimator; Luppi et al. (2023) use CCS on binarised signals, with Gaussian and MMI validations, and Tarchi et al. (2026) state neither. Where the lag is written it is a single lag, one TR where its value is stated (Luppi et al., 2023, with four TRs as a check; Down et al., 2026), on BOLD series whose lag-1 autocorrelation is high because of haemodynamic smoothing and band-pass filtering.

Barrett (2015) exhibited positive net synergy — hence positive MMI synergy, since MMI redundancy is non-negative — in a dynamical Gaussian example in which a target's own immediate past is one of the sources (his Example 1); the net synergy vanishes when the infinite pasts are the sources, while the MMI synergy stays at ½ ln(1 + α²) (his Eqs. 73 and 79–82). MMI cannot tell a synergistic pair from two independent autocorrelated processes (Varley, 2024, Eq. 12). Closed-form Gaussian decompositions exist for transfer entropy (Faes et al., 2017), for static systems (Barrett, 2015; Kay & Ince, 2018) and for single-target lagged PIDs of MVAR processes with a target's own past among the sources (Barrett, 2015, Sec. V), and Varley (2024) gave the aggregate identity; what none of them gives is an account at the level of the atoms actually reported — which of the sixteen carry the self-information, how sts depends on a pair's lag-1 autocorrelation r₁ and lag-0 correlation q, where real region pairs sit on that dependence, whether CCS shares the property, and how much of an observed sts change the pairs' own autocorrelations carry.

This study did not set out to provide these. It was planned as a directional test of whether whole-brain synergy is up-regulated under N,N-dimethyltryptamine (DMT), a state of intensified conscious content, against the workspace account's prediction that synergy indexes conscious level. The hypothesis was recorded before any data were analysed; the test statistic was fixed after global fits on the same data had already shown a decrease (Methods). Synergy decreased; the decrease was carried by the pairs' self-prediction atoms and went with the lag-1 autocorrelation contrast, and the closed form was derived afterwards, on the same data, to account for it. We give the sixteen atoms of the AR(1) pair in closed form and their exchange rates in data units (Results 1); the DMT contrast beside the autocorrelation contrast (Results 2); the regional map with regional autocorrelation partialled out (Results 3); an estimate that keeps each pair's measured autocorrelations and lag-0 correlation, with what its residual can and cannot show (Results 4); the lag dependence (Results 5); the CCS comparison (Results 6); and prewhitening, deconvolution and the choice of estimator (Results 7). Apart from the primary contrast every analysis is exploratory, and the account itself is post hoc.

---

## Results

Notation: an atom's letters give the kind of past and future information (r redundant, x or y unique to region X or Y, s synergistic); values are in nats; a DiD is (post − pre) on DMT minus (post − pre) on placebo, per subject.

### 1. The sixteen atoms in closed form

Let x and y be unit-variance AR(1) processes with lag-1 autocorrelation a (= r₁) and lag-0 correlation q, so that corr(x_t, y_{t+1}) = aq. With S = −½ ln(1 − a²), the self-information of one process, and C = −½ ln(1 − a²q²), the cross-lag mutual information, the Möbius inversion of the ΦID lattice under MMI gives (Methods)

rtx = rty = xtr = ytr = xty = ytx = 0,   xtx = yty = rts = str = S − C,   xts = yts = stx = sty = −(S − C),   rtr = C,

sts = 2S − C = −ln(1 − a²) + ½ ln(1 − a²q²).

Hence, exactly for all (a, q),

sts − (xtx + yty) = rtr,   rtr + sts = TDMI = 2S,   ΦR = rtr,

with TDMI depending on r₁ alone, and str + stx + sty + sts = S for every q: Varley's (2024) aggregate synergy (his Eq. 3), which at q = 0 is his identity for a disintegrated pair (his Eq. 12). The four mirror atoms, xts, yts, stx and sty, are negative. That MMI-ΦID can produce negative atoms is noted by its authors (Mediano et al., 2025, SI Appendix, Sec. III.A; Luppi et al., 2026); under MMI the redundancy and synergy atoms are guaranteed non-negative while many of the others can take negative values (Down et al., 2026).

With unequal coefficients the MMI minima select the less self-predictive member. At q = 0, sts = 2 min(S_x, S_y) exactly and rtr = 0, so sts lies below xtx + yty = S_x + S_y by |S_x − S_y|. For any q, str equals the smaller self-prediction atom, rts is at least as large, and sts ≤ xtx + yty + rtr, with equality only at equal coefficients; the excess sts − (xtx + yty), which is rtr at equal coefficients, falls with the asymmetry and changes sign at an asymmetry |a_x − a_y| of 0.008 at (0.85, 0.25) (S3 Text). At a mean coefficient of 0.85 and q = 0.25, sts falls from 1.2588 at equal coefficients to 1.1711 at a difference of 0.03.

At the operating point of BOLD region pairs, (r₁, q) = (0.85, 0.25) (Fig 2a), 0.01 of r₁ moves sts by 0.061 nats (∂sts/∂r₁ = +6.07), 0.1 of |q| by 0.019 (∂sts/∂q = −0.19; sts is even in q), and 0.01 of within-pair asymmetry |a_x − a_y| by 0.031. Per standard deviation of the pairs' variation within a window (0.0284 for pair r₁ and 0.196 for |q|; B22), the r₁ rate is 4.7 times the |q| rate; across pairs averaged over subjects and windows it is 3.3 times. Over all 392 windows the regression of pair sts on (r₁, |q|, |a_x − a_y|) has a mean R² of 0.808 against 0.462 for r₁ alone; the windowed estimator's own slope on |q|, −0.53 per unit, is 2.8 times the population rate, consistent with a finite-sample bias that grows with |q|.

Lagged interaction moves sts non-monotonically. On the coupled family (S3 Text), with r₁ and q held at (0.85, 0.25), sts falls from 1.2588 at c = 0 to 1.2155 at c = +0.05, then rises (1.2569 at +0.10), and for negative c rises (1.4111 at −0.05; slope −1.74 per unit at c = 0): at the data's operating point coupling of the same sign as q lowers the atom called synergy, and coupling of the opposite sign raises it (the family is invariant under (c, q) → (−c, −q)) (Fig 2c).

The data's atom table has the family's pattern (Table 1): the excess sts − (xtx + yty) is negative in the data (−0.0844) and in the AR(1)-substituted atoms (−0.1003), the mirror atoms are negative, and every atom moved under DMT as its AR(1)-substituted value did; the residual columns are the signature of lagged structure the diagonal family lacks (Results 4).

**Table 1. The sixteen whole-brain atoms under MMI, observed and AR(1)-substituted (each pair's measured (a_x, a_y, q) put into the AR(1) family; Results 4): DMT pre-injection level (windows 1–4) and DMT contrast (DiD: windows 6–14 minus 1–4, DMT minus placebo; nats, mean over 14 subjects; in brackets the number of subjects with a negative DiD). Primary variant and estimator (ts_gsr, W = 60); the sensitivity variant and the CCS atoms in S3 Text. Residual = observed − AR(1)-substituted. Fig 1 draws the table.**

| atom | observed level | AR(1)-substituted level | residual | observed DiD | AR(1)-substituted DiD | residual DiD |
|---|---|---|---|---|---|---|
| rtr | +0.0388 | +0.0504 | −0.0116 | −0.0078 (10) | −0.0086 (10) | +0.0008 (4) |
| rtx | +0.0258 | +0.0027 | +0.0231 | −0.0012 (9) | −0.0003 (10) | −0.0008 (8) |
| rty | +0.0254 | +0.0024 | +0.0230 | −0.0012 (9) | −0.0000 (10) | −0.0011 (9) |
| rts | +0.5669 | +0.5756 | −0.0087 | −0.0407 (12) | −0.0414 (13) | +0.0008 (4) |
| xtr | +0.0254 | +0.0024 | +0.0230 | −0.0012 (9) | −0.0000 (10) | −0.0011 (9) |
| xtx | +0.6273 | +0.6617 | −0.0345 | −0.0523 (12) | −0.0535 (12) | +0.0012 (5) |
| xty | −0.0254 | −0.0024 | −0.0230 | +0.0012 (5) | +0.0000 (4) | +0.0011 (5) |
| xts | −0.5352 | −0.5747 | +0.0395 | +0.0399 (2) | +0.0413 (2) | −0.0014 (9) |
| ytr | +0.0258 | +0.0027 | +0.0231 | −0.0012 (9) | −0.0003 (10) | −0.0008 (8) |
| ytx | −0.0258 | −0.0027 | −0.0230 | +0.0012 (5) | +0.0003 (4) | +0.0008 (6) |
| yty | +0.6125 | +0.6470 | −0.0345 | −0.0396 (13) | −0.0408 (12) | +0.0012 (5) |
| yts | −0.5358 | −0.5747 | +0.0389 | +0.0404 (2) | +0.0414 (2) | −0.0010 (9) |
| str | +0.5667 | +0.5750 | −0.0082 | −0.0408 (12) | −0.0414 (12) | +0.0006 (5) |
| stx | −0.5350 | −0.5750 | +0.0400 | +0.0401 (2) | +0.0414 (2) | −0.0013 (9) |
| sty | −0.5357 | −0.5750 | +0.0392 | +0.0403 (2) | +0.0414 (2) | −0.0011 (9) |
| sts | +1.1554 | +1.2084 | −0.0530 | −0.0809 (13) | −0.0924 (13) | +0.0115 (4) |
| TDMI (Σ 16) | +1.4772 | +1.4240 | +0.0532 | −0.1037 (12) | −0.1129 (12) | +0.0092 (5) |

### 2. The DMT contrast

Whole-brain MMI-sts fell under DMT, and across subjects its fall went with the fall of lag-1 autocorrelation. The primary contrast of this paper is the pre-specified DiD of whole-brain MMI-sts on the primary variant and estimator (Table 2): −0.0809 nats [−0.1317, −0.0310], exact sign-flip p = 0.0038, negative in 13 of 14 subjects, −7.0 % of the pre-injection DMT mean; −0.0649 [−0.1010, −0.0260] after residualisation on framewise displacement. It was planned as a test of an increase, and under the directional-failure rule a significant decrease refutes the up-regulation hypothesis; but the rule and the test statistic were written after global fits on the same data had shown a decrease (Methods), so the windowed contrast measures, with a second estimator, an effect already seen. The contrast held without global signal regression (−0.1031 [−0.1629, −0.0435], p = 0.0026), at W = 30 (−0.0686, p = 0.0042), in all 28 leave-one-out refits, and at the global fit (−0.0801 [−0.1362, −0.0251], p = 0.0071).

Regional r₁ fell relative to placebo by −0.0146 [−0.0261, −0.0037] (p = 0.0106, negative in 12 of 14; −0.0216 without global signal regression); its phase-randomised p is 0.073 against 0.002 for sts (S3 Text). Mean pair |q| moved by −0.0164, worth +0.003 nats at the population rate and +0.009 at the windowed estimator's own rate. Both runs contribute: the placebo run's r₁ and sts rose across the session and carry 0.34 and 0.40 of the two DiDs, so the DiD is the design's drug estimate under the assumption that the placebo run's drift would have occurred on the DMT run too, and the DMT run's own change (sts −0.0485, p = 0.027; Table 2) contains time in the scanner as well as the drug. The drift's source is not identified here; lower arousal later in a session is one candidate, since BOLD lag-1 autocorrelation rises in sedation (Huang et al., 2018).

Across subjects the two contrasts share their reliable variance (Fig 3a, b). Both are read off the same windows, so their full-set correlation, r = 0.953 [0.854, 0.985], contains shared estimation error; the cross-half correlation, each subject's sts DiD on odd windows against the r₁ DiD on even windows and the reverse, is 0.742 [0.349, 0.913] and 0.645 [0.174, 0.876], mean 0.694 (approximately [0.258, 0.895]), against a ceiling of 0.729: disattenuated, 0.95 [0.62, 0.99] (subject bootstrap; S3 Text). At the group level sts fell by 0.0055 nats per 0.001 fall of regional r₁, and by 5.2 per unit of the pair-level a (the mean of a pair's a_x and a_y), in close to the proportion a generator with the data's spectrum produces (6.1; AR(1) pairs 3.1). Across subjects the sts DiD rises with the r₁ DiD at 4.26 per unit (OLS slope, t interval, 12 df, [3.41, 5.12]; intercept −0.018 [−0.039, +0.002]), a slope attenuated by measurement error (5.0 corrected for reliability, a model-based figure).

A post-hoc check of the ratio sts / TDMI (S8 Table) found three of the four variant × estimator cells proportional; the fourth, the global fit on the primary variant, is less than proportional (+0.0204, p = 0.025), which is not explained here.

**Table 2. The primary contrast: whole-brain mean MMI-sts, W = 60, windows 6–14 minus 1–4 (nats; N = 14; exact sign-flip p, two-sided; inverted sign-flip 95 % interval; the phase-randomised p of Methods as a stationarity check).**

| | ts_gsr (primary) | ts_demean |
|---|---|---|
| Pre-injection DMT / PCB mean | 1.1554 / 1.1378 | 1.1004 / 1.0819 |
| DMT post − pre | −0.0485 [−0.0882, −0.0068], p = 0.0267 | −0.0633 [−0.1175, −0.0066], p = 0.0333 |
| PCB post − pre | +0.0324 [+0.0013, +0.0638], p = 0.0425 | +0.0398 [+0.0051, +0.0743], p = 0.0306 |
| DiD | −0.0809 [−0.1317, −0.0310], p = 0.0038; phase p = 0.0020; 13/14 negative | −0.1031 [−0.1629, −0.0435], p = 0.0026; phase p = 0.0010; 12/14 negative |
| FD DiD | +0.0143 [−0.0115, +0.0403], p = 0.2452 | same |
| DiD, FD-residualised | −0.0649 [−0.1010, −0.0260], p = 0.0048; 13/14 | −0.0824 [−0.1302, −0.0322], p = 0.0048; 13/14 |

### 3. The regional map

On the placebo run before injection, regional MMI-sts (global fit; S3 Text) correlates with regional r₁ at r = 0.863 (Spearman 0.835; cortical spin p < 0.0001) over the 115 regions; per subject +0.756 [+0.715, +0.790] (a subject-bootstrap percentile interval), positive in 14 of 14; regional r₁ accounts for three-quarters of the map's variance (r² = 0.745; Fig 6a). Partialling regional r₁ out of the map (slope +3.09 nats per unit), the pre-defined contrast of sensory (visual, somatomotor) against association cortex (default-mode, frontoparietal control) goes from −0.0202 nats to +0.0037, and per subject from −0.0202 (p = 0.006) to +0.0007 (p = 0.90): the pre-defined contrast vanishes (Fig 6b). It does not remove all network structure: the residual map's network means run from −0.024 (subcortex) to +0.021 (dorsal attention), the somatomotor − default contrast grows from −0.007 to −0.010, and the residual map's eight-class F (8.15) lies in the upper 0.1 % of its spin distribution (p = 0.0009; p = 0.056 for the unpartialled map), with its somatomotor − default and visual − default contrasts at spin p = 0.22 and 0.31 (Fig 6c). rtr follows regional r₁ at r = 0.638, with a slope of 0.50 nats per unit, a sixth of sts's. Regional r₁ is a hierarchical map in the literature — the intrinsic timescale of BOLD lengthens from sensorimotor to association cortex (Raut et al., 2020; Ito et al., 2020; the single-unit precedent is Murray et al., 2014) — but in these data its network means differ little (somatomotor 0.849, default 0.848, visual lowest of the cortical networks at 0.840). Which gradient is the cause cannot be told on these data; none of the maps of the studies in the applicability table reports regional r₁ (Discussion).

### 4. What the pairs' own autocorrelations carry, and what the remainder can show

For each pair, subject, run and window, the AR(1)-substituted estimate is the sts of the 4 × 4 matrix that keeps the pair's measured a_x, a_y and q and sets its two cross-lag correlations to a_y q and a_x q (Methods): the sts the pair would have if its lagged structure were that of two AR(1) processes with its measured autocorrelations and lag-0 correlation. It is the same estimator applied to the same windows with two entries replaced, so its agreement with the observed sts across subjects (r = 0.99) is largely built in and is not evidence for the account; what it measures is how much of a contrast the pairs' own (a_x, a_y, q) carry. It exceeds the observed level by 4.3 % at W = 60 and by 1.1 % at the run level. Its DiD is −0.0924 [−0.1503, −0.0348] against the observed −0.0809; the residual, observed minus estimate, has DiD +0.0115 [+0.0005, +0.0226], positive in 10 of 14, larger in the early post-injection windows (+0.0179) than in the late (+0.0064) (Table 3; Fig 4).

A pure autocorrelation change also produces a positive residual, because the sampling scatter of the cross-lag correlations lowers the observed sts below the estimate by an amount that grows with a and |q|. In simulations with a fall of about 0.015 in r₁ applied to the DMT run only (Methods; S10 Table), the residual DiD is +0.0027 ± 0.0014 on a band-passed generator solved to the data's spectrum and window-level operating point, and +0.0049 ± 0.0017 on AR(1) pairs; a finite-sample null with the data's autocorrelation function gives +0.0054. Against these the data's residual DiD has exact p = 0.108, 0.219 and 0.251: weak evidence of an excess. Across subjects the residual DiD scales with the r₁ DiD at −0.75 per unit (OLS slope, t interval [−1.13, −0.37]; Fig 3c), where the generators give −0.18 to −0.39 per unit of their pair-level a (the mean of a pair's a_x and a_y; −0.74 for the data's group means on that basis), and the relation holds across split halves (−0.700 and −0.385); the generators apply one change to every subject and do not reproduce it, so the calibration is not validated for the residual on this dataset.

What a change in lagged structure does to the residual depends on how the change is made (Table 3). Coupling added as a VAR(1) cross-coefficient with the innovations held, the calibration's construction, also shifts each pair's lag-0 correlation and autocorrelation, and the residual falls for either sign (−0.0048 ± 0.0006 at c = +0.02 and −0.0055 ± 0.0007 at c = −0.02, at W = 60). A cross-lag change at fixed (r₁, q) raises it for either sign (+0.0098 ± 0.0009 and +0.0102 ± 0.0010 at δ = ±0.02), a change aligned with the sign of q moves it at first order (−0.0135 ± 0.0003 at δ = +0.01·sign(q), +0.0185 ± 0.0004 at −0.01·sign(q)), and a weakening of a slow component shared by the two regions, which at τ = 1 cannot be told from lagged coupling (Methods), raises it in proportion to the fall of r₁ (in population −1.70 per unit of r₁ when the shared component's autocorrelation falls and −2.89 when its weight falls; −1.59 and −2.73 per unit of pair-level a at W = 60). The residual's rise is therefore compatible with a pure autocorrelation change that the generators do not represent, with a coupling change at fixed lag-0 structure, and with a weakening of lagged structure aligned with q.

The aligned cross-lag departure — the mean over pairs of δ_sym signed by the pair's lag-0 correlation in the other run, which carries none of the window's own selection — changed by −0.0006 [−0.0017, +0.0004] under DMT relative to placebo, against +0.0000 ± 0.0003 under a pure autocorrelation change on the band-passed generator; at the conversions of Table 3 (an aligned cross-lag change, and a weakening of a shared slow component's autocorrelation) its interval admits changes accounting for between none and about half of the residual's excess over that generator's expectation, so it neither explains the excess nor excludes aligned structure as its source. On the sensitivity variant it fell, −0.0025 [−0.0047, −0.0003], an amount that at the same conversions corresponds to +0.006 to +0.007 of that variant's residual DiD of +0.018. A fall in the weight of a shared component (λ → 0.9λ in Table 3) raises the residual while barely moving the aligned statistic, so that form of change is invisible to it.

At the run level the residual (−0.0137 [−0.0146, −0.0129], negative in 14 of 14) is about half the directed and half the symmetric part of the cross-lag departure (S3 Text). At W = 60 the directed part's response changed by +0.0011 [−0.0033, +0.0052] under DMT relative to placebo, an interval that contains the −0.0010 ± 0.0004 a pure autocorrelation change produces through the sampling scatter of the directed departure (B24), and the symmetric part's by +0.0103 [+0.0014, +0.0194] against +0.0037 ± 0.0009; the residual's DiD sits in its symmetric part.

**Table 3. The residual of the AR(1)-substituted estimate: the data, its expectation under a pure autocorrelation change, and its response to changes in lagged structure (W = 60 unless marked; nats). Data: mean over subjects [inverted sign-flip 95 % interval]. Generators (rows 3 and 4): DiD with the DMT run changed from sample 300; residual, mean ± replicate SD over 50 replicate datasets of 14 subjects × 2 runs × 300 pairs (B24's 20 replicates give +0.0028 ± 0.0012 for the band-passed residual); row 3's autocorrelation change and A_other are B24's, mean ± replicate SD over its 20 replicates; the AR(1) row's autocorrelation change is a simulation of the same design over 3,000 pairs (± SE) and its A_other a whole-run change at a = 0.85. Autocorrelation change: in the data rows the regional lag-1 autocorrelation DiD, the paper's r₁ contrast, with the pair-level a of the window's 4 × 4 matrix beside it for ts_gsr (residual_source.log); in the generator rows the pair-level a, including the null's own (row 5; Methods). Rows 6–11: whole-run changes at a = 0.85 over 3,000 pairs with common random numbers, against the unperturbed pairs (rows 10 and 11 against the shared-component model at its base parameters), ± SE over pairs; population column: closed-form pool means over 20,000 pairs (B23 (a)). Across subjects the data's residual moves by −0.75 per unit of regional r₁ (OLS slope; t interval, 12 df, [−1.13, −0.37]), and its group means by −0.74 per unit of pair-level a; the generators' residual moves by −0.18 (band-passed), −0.39 (AR(1)), −0.37 (null), −1.59 (Δa_s) and −2.73 (λ) per unit of pair-level a. Full results: S18 Table.**

| condition | residual DiD or change, W = 60 | residual, population change | window-level autocorrelation change (see caption) | A_other DiD or change |
|---|---|---|---|---|
| data, ts_gsr (B21, B22) | +0.0115 [+0.0005, +0.0226] | — | −0.01465 [−0.02609, −0.00370]; pair-level a −0.0155 | −0.00059 [−0.00166, +0.00041] |
| data, ts_demean (B21, B22) | +0.0182 [+0.0072, +0.0293] | — | −0.02157 [−0.03314, −0.01020] | −0.00249 [−0.00474, −0.00026] |
| pure autocorrelation change (Δa = −0.015), band-passed generator (B17b; B24) | +0.0027 ± 0.0014 | 0 | −0.01540 ± 0.00035 | +0.00001 ± 0.00031 |
| the same, AR(1) pairs (B17; B23 (e); B23 (b) (i)) | +0.0049 ± 0.0017 | 0 | −0.01243 ± 0.00101 | +0.00001 ± 0.00004 |
| finite-sample null with the data's autocorrelation functions | +0.0054 | 0 | −0.0146 | — |
| coupling with innovations held (B17's construction), c = +0.02 / −0.02 (B23 (a4), (b)) | −0.0048 ± 0.0006 / −0.0055 ± 0.0007 | −0.0081 / −0.0091 | +0.00129 / +0.00134 (± 0.00012) | +0.00387 ± 0.00034 / +0.00405 ± 0.00033 |
| coupling at fixed (r₁, q), c = +0.02 / −0.02 (B23 (a3), (b)) | +0.0068 ± 0.0006 / — | +0.0091 / +0.0081 | −0.00069 ± 0.00004 / — | +0.00014 ± 0.00031 / — |
| cross-lag departure at fixed (a, q), δ = +0.02 / −0.02 (B23 (a1), (b)) | +0.0098 ± 0.0009 / +0.0102 ± 0.0010 | +0.0161 / +0.0148 | −0.00092 / −0.00089 (± 0.00004) | +0.00041 / +0.00059 (± 0.00034) |
| aligned departure, δ = +0.01·sign(q) / −0.01·sign(q) (B23 (a2), (b)) | −0.0135 ± 0.0003 / +0.0185 ± 0.0004 | −0.0225 / +0.0297 | −0.00023 / −0.00021 (± 0.00002) | +0.00782 ± 0.00011 / −0.00748 ± 0.00010 |
| shared slow component, its autocorrelation Δa_s = −0.03 (B23 (a5), (b)) | +0.0102 ± 0.0002 | +0.0139 | −0.00642 ± 0.00010 (population −0.00815) | −0.00371 ± 0.00006 |
| shared slow component, its weight λ → 0.9λ (B23 (a5), (b)) | +0.0039 ± 0.0001 | +0.0047 | −0.00143 ± 0.00003 (population −0.00163) | −0.00010 ± 0.00005 |

### 5. Lag dependence

A longer lag reduces everything, the artefact included (Fig 5; S14 Table). With the lag-τ four-vector, as the mean lag-τ autocorrelation r_τ falls from 0.848 at τ = 1 to 0.513, 0.139 and −0.202 at τ = 2, 3 and 5, the sts level falls (1.1554, 0.1797, 0.0262, 0.0415), and so does the sts contrast (−0.0809, −0.0429, −0.0043, −0.0024; p = 0.0038, 0.0037, 0.0018, 0.37), which per subject tracks the lag-τ autocorrelation contrast (r = 0.95, 0.97, 0.63 and −0.83; at τ = 5 r₅ is negative and every AR(1) atom is even in the autocorrelation); at τ = 3 the tracking is partial, for a reason the data do not give. DMT shifts the regional autocorrelation function towards a faster decay, of which r₁ is the lag-1 summary (the in-band spectral centroid rises by +0.0023 Hz, p = 0.022). No lag moves the pairs to a point where q contributes comparably, and a longer lag is not recommended as a remedy.

### 6. CCS: a near-zero synergy atom that moves inversely with autocorrelation

Under CCS whole-brain sts is −0.048 nats (MMI 1.155). CCS-sts does not track pair r₁ within a window (r = −0.011, where MMI-sts gives +0.742), but across the 28 condition × window group means it moves inversely with mean r₁ (r = −0.64, where MMI-sts gives +0.98), its per-subject DiD correlates negatively with the r₁ DiD in all four variant × estimator cells (r = −0.43 to −0.27, each Fisher-z interval including zero at N = 14, at a split-half reliability of 0.30), and on the symmetric AR(1) family at fixed q it is nearly flat in r₁ (−0.013 nats per unit at (0.85, 0.25), against +6.09 for MMI-sts from the same fits; it falls from r₁ = 0.80 to 0.87 and rises again at 0.90), so the family accounts for little of that inverse relation. In these data its dependence on r₁ is weaker and of the opposite sign, not absent.

CCS-sts rose under DMT in every combination (S15 Table): +0.0044 [−0.0001, +0.0088] at the primary estimator (exact p = 0.056, positive in 11 of 14) and +0.0197 [+0.0133, +0.0261] at the global fit (p = 0.0002, 13 of 14). CCS-sts is exactly −(1 − s) c̄_rej per pair, with s the share of samples whose five local signs agree and c̄_rej the mean double co-information over the rest; the identity locates the change without explaining it: at the global fit the increase sits in the co-information term (+0.0174 [+0.0118, +0.0231] of +0.0197; c̄_rej fell by 0.0292, in 14 of 14 subjects), not in the share. After AR(p) whitening the CCS contrast is negative in all four cells (ts_gsr, W = 60: −0.0135, p = 0.016) and after AR(1) whitening negative in one and positive in three (S11 Table; those values use phyid's mask, Methods). CCS-sts is a specification chosen after the results were seen; its contrast is not read as a DMT finding. ΦR, the quantity of the workspace account, changed by +0.0007 [−0.0093, +0.0112] (p = 0.90), an interval that excludes changes larger than 0.0112 nats in either direction, about 12 % of its pre-injection level (0.096).

### 7. Remedies

Prewhitening cannot remove the dependence from band-passed data. BOLD band-passed to 0.01–0.08 Hz holds 99.2 % of its power in the band, where flat-spectrum noise already has r₁ = 0.82 at TR 2 s, so a whitened series with low r₁ can only be one in which the whitening filter has amplified the stop-band residue. AR(p) residuals (p by BIC in 1–5, at the cap for 3,218 of 3,220 series) keep r₁ = 0.26 and 34 % of their power above the band, against 0.1 % in the raw series (51 % and 60 % at fixed orders 10 and 20; no atoms were computed at those orders); MMI-sts on them is 0.22, its contrast −0.026 [−0.064, +0.011] (p = 0.14), −0.019 of it carried by the AR(1)-substituted estimate; AR(1) residuals keep r₁ = 0.75 and a contrast of −0.062 (p = 0.0006). Prewhitening also has costs: on HCP fMRI a mutual-information test's false-positive rate rose from 42 % to over 88 % after AR(p) prewhitening (Cliff et al., 2021); making a BOLD series entirely uncorrelated may remove neuronal information carried by the haemodynamic response, a concern Honari et al. (2019) raise although their own simulation found no detrimental effect; and band-pass filtering itself reintroduces autocorrelation (Arbabshirani et al., 2014).

HRF deconvolution (S2 Text) lowered r₁ from 0.848 to 0.783 and sts from 1.155 to 0.832 and left the contrast in place (−0.0782, p = 0.0013). At TR 2 s it changes the operating point, not the mechanism.

Neither estimator is free of manufacture at the data's operating point (S16 Table). Between two simulated conditions of equal analytic sts and different covariance, the W = 60 estimator returned +7 % ± 8 % and −8 % ± 6 % of the observed contrast on the two data-like matched pairs, and the 840-sample fit +29 % and +2 %; on two pairs whose analytic sts is 0.094 nats, an order of magnitude below the data's, W = 60 returned −9 % and +16 % and the 840-sample fit +2 % and +1 %. The global fit's pre/post contrast within a run is also exposed to the within-run variance change, and its period-level residual is biased when the pairs are asymmetric (S10 Table). The paper reports both estimators and prefers neither. Null-model normalisation of atoms is a direction the ΦID authors have named (Liardi et al., 2025, for PID on MEG); on the family the dependence it addresses is r₁'s route into sts, since TDMI = 2S depends on r₁ alone.

---

## Discussion

### What the finding is and is not

The analysis says nothing about whether synergy in the intended sense is present in the brain; what it establishes is what the estimator responds to. On the bivariate AR(1) family the Gaussian-MMI synergy atom is the two self-prediction atoms plus the double redundancy, balanced by four negative atoms of the kind the ΦID authors note MMI can produce (Mediano et al., 2025, SI Appendix, Sec. III.A; Luppi et al., 2026), and with unequal coefficients MMI takes the smaller self-information, so that the atom falls below xtx + yty + rtr — the pattern the data's own atom table shows. The atom therefore inherits the dependence of self-information on lag-1 autocorrelation, at rates that can be stated in the data's units: 0.01 of r₁ is worth 0.061 nats of sts and 0.1 of |q| 0.019, and per standard deviation of the pairs' variation within a window r₁ outweighs |q| 4.7-fold in population and 1.4-fold in the windowed estimator's own dependence. Lagged interaction, the thing the atom is meant to capture, moves it non-monotonically and with a sign set by the sign of q. What follows for a contrast between states is narrow and definite: when the compared conditions differ in r₁, the MMI-sts contrast moves with that difference, at a rate that depends on the estimator (S13 Table), whether or not anything the word synergy is meant to capture has changed.

On this dataset sts fell with r₁, the two contrasts share their reliable variance, the group-level falls stand in close to the proportion a generator with the data's spectrum produces, the regional map follows regional r₁, and the AR(1)-substituted estimate carries the contrast. The remainder is weak evidence of an excess over a pure autocorrelation change and scales with the autocorrelation change more steeply than in the generators, on either basis (−0.75 per unit of regional r₁ across subjects, −0.74 per unit of pair-level a at the group level, against −0.18 to −0.39). What it is — lagged interaction, a weakening of slow shared fluctuations, or an autocorrelation change of a shape the generators lack — is not identified; the aligned cross-lag statistic neither explains it nor excludes aligned structure as its source on the primary variant, and falls on the sensitivity variant. The run-level residual of the level is about half directed and half symmetric.

Two limits on reach remain: the closed form is exact on the family but approximates the data, matching the atom table, with each pair's measured coefficients, to within 0.053 nats for sts and 0.04 for the mirror atoms; and the exchange rate for within-pair asymmetry is a population statement that the estimators recover only in part (S10 Table).

### The literature

Two uses of MMI-sts should be distinguished. A contrast between states, between groups, or across a session is exposed wherever the compared conditions differ in r₁: BOLD lag-1 autocorrelation rises in propofol sedation and falls in deep anaesthesia and in disorders of consciousness (Huang et al., 2018), relative to placebo in this dataset, and within a placebo run with time; between-group designs are exposed to any group difference in r₁ from physiology, motion, age or scanner. A spatial map of synergy across regions is exposed through regional differences in r₁: higher r₁ gives higher sts with rtr moving much less (∂rtr/∂r₁ = 0.06 on the family; across regions here a sixth of sts's slope), so a regional autocorrelation gradient produces a synergy-minus-redundancy gradient of the same spatial form. The applicability table (S3 Text), which lists nine empirical studies (Down et al., 2026; Gatica et al., 2024; Luppi et al., 2022, 2023, 2024, 2026; Nago et al., 2026; Tarchi et al., 2026; Zhang et al., 2025), gives every study within the map — the main texts of all nine read in full; the main text of Tarchi et al. (2026) does not state its redundancy function — the same conditional statement, the sign of r₁ change that would produce its reported effect on the map (the primary quantity of Luppi et al., 2023, CCS emergence capacity on binarised signals, is outside it); that statement is what the map predicts, not evidence about any study, since none of them reports regional r₁.

The human (HCP) data of Luppi et al. (2022), at TR 0.72 s, fall outside the TR range the plan fixed for the table, a scoping rule (its macaque dataset, at TR 2.6 s and not deconvolved, falls inside). At its stated 0.008–0.09 Hz band the ideal-band-pass r₁ is 0.97, where ∂sts/∂r₁ = 32.8; but per unit of regional spectral difference the exposure is almost the same at every TR — a given low-frequency tilt (the band's power weighted by exp(−100 f²), f in Hz) changes sts by 0.19 nats at TR 0.72 s and 0.17 at 2 s — so the derivative does not rank datasets, and the exposure is not specific to TR 2 s data. Its phase-randomised surrogates, which on the family give the regional r₁ gradient up to noise, are the table's one test of the exposure (S3 Text). Its correlations with the six macroscale maps of their Table 1 were small (|ρ| ≤ 0.26) and, with one exception (the glycolytic index, a PET measure of aerobic glycolysis: ρ = 0.26, spin p = 0.028), not significant, against 0.22–0.54 for the observed gradient (0.40–0.54 for its four significant associations: cortical expansion, HAR-Brain gene expression, the glycolytic index and receptor diversity). A change in q moves synergy and redundancy oppositely by equal amounts and a change in r₁ moves mainly sts, so on the family synergy and redundancy moving in opposite directions (Down et al., 2026; regionally, Tarchi et al., 2026) is the q signature or a mixture, not the r₁ signature; those are statements about the family, and they are where the table's reading runs against the r₁ mechanism alone, the surrogate test of Luppi et al. (2022) being the one empirical evidence against the exposure. And ΦR = rtr on the symmetric family falls with a fall in either factor, so the result for sts does not carry over to ΦR (Luppi et al., 2024, 2026). Among the studies in the table, none but Luppi et al. (2022) addressed autocorrelation, and Varley (2024) is the study whose subject it is.

### Recommendations

Report the mean lag-1 autocorrelation beside sts, per condition and subject, and its contrast beside the sts contrast, with the effective sample size computed from the autocorrelation function (Afyouni et al., 2019; the AR(1) case is Bartlett, 1935). Report each sts contrast beside its AR(1)-substituted estimate from each pair's measured (a_x, a_y, q); the difference between the two is not a measure of lagged interaction unless a calibration reproduces the study's own relation between that difference and the autocorrelation change. Compare exposure across datasets per unit of spectral difference, not per unit of r₁, since ∂sts/∂r₁ grows without bound as r₁ approaches 1. Do not expect prewhitening to remove the dependence from band-passed data, and do not treat CCS as free of it. Where a null is wanted, preserve each region's autocorrelation and the pair's lag-0 correlation — the AR(1)-substituted matrix, or surrogates generated from the two spectra with the measured lag-0 correlation — rather than the autocorrelation alone: a null that removes every cross-correlation sits at q = 0, where sts is at its maximum for a given r₁, and so tests lag-0 correlation rather than lagged interaction.

### Limitations

One dataset, one drug, one parcellation, N = 14, TR 2 s, no deconvolution in the primary analysis; the DMT contrast is a proof of concept. There is no ground truth for synergy in these data, so the analysis establishes what the estimator responds to, not what the brain does. Two redundancy functions were examined, both Gaussian. On Gaussian systems every PID whose redundancy depends only on the source–target marginals reduces to MMI when the target is univariate (Barrett, 2015; Kay & Ince, 2018), which covers the lattice nodes with a single past or single future variable but not the joint-target nodes or the double redundancy, which are ΦID's own extensions (Mediano et al., 2021), and the multiscale transfer decomposition of Faes et al. (2017) is a different object; so "MMI-specific" is not a licensed phrase, and other Gaussian PIDs could share or not share the property. The primary contrast was planned as a test of a different hypothesis and its statistic was fixed after global fits on the same data had shown a decrease; the account was derived afterwards on the same data; and the calibration's recorded predictions for a coupling change failed, and a reading of the residual built after that failure has been withdrawn (Methods; S5 Text). Every later computation was entered in the record with its rule and prediction before it was run; the git record establishes ordering, not blindness.

---

## Materials and methods

### Ethics statement

The original study was approved by the National Research Ethics Committee London – Brent and the Health Research Authority, with written informed consent from all participants (Timmermann et al., 2023; S1 Text) [TK: the REC reference number, to be obtained from C. Timmermann]. This is a secondary analysis of anonymised released data (Singleton et al., 2025).

### Dataset

Data are the preprocessed regional time series released by Singleton et al. (2025), acquired by Timmermann et al. (2023): fourteen subjects (six of twenty excluded for head movement by Singleton et al., 2025), each with a DMT and a placebo (PCB) run of 840 TRs at TR = 2 s, injection at TR 240 (S1 Text); with global signal regression (ts_gsr, primary) and without it (ts_demean, sensitivity), both band-passed to 0.01–0.08 Hz; Schaefer-100 parcels (Schaefer et al., 2018; Yeo et al., 2011) and 16 subcortical ones (Tian et al., 2020), one region, mean-filled for one subject, dropped for all: 115 regions and 6,555 pairs.

### Estimator

Atoms were computed with phyid (Imperial-MIND-lab, 2026; calc_PhiID, Gaussian, τ = 1) and averaged over pairs, in 14 independent 60-TR windows per run (W = 60; W = 30 as a second) or in one global fit per run, its local atoms averaged into 28 bins. The effective sample size of a correlation between two series that share these autocorrelations is n / (1 + 2 Σ_k ρ_k²), the global form of the effective-degrees-of-freedom estimator reviewed by Afyouni et al. (2019, their Eq. 8; Bartlett, 1935, gave the AR(1) case); over the six lags of the pooled placebo function (0.868, 0.539, 0.172, −0.085, −0.174, −0.145) the denominator is 3.3, so a 60-TR window holds about 18 effective samples. On simulated VAR(1) pairs the windowed estimator absorbed 15–45 % of a true sts difference at W = 60 and 52–77 % at W = 30, which is why W = 60 was pre-specified. A closed-form implementation of the same estimator reproduces phyid to ≤ 1.3 × 10⁻¹⁴ on every saved window and bin mean and to ≤ 2.3 × 10⁻¹⁴ on the regional values.

### Redundancy functions

MMI takes each single-target redundancy as the smaller single-source mutual information (Barrett, 2015) and rtr as the smallest of the four (Mediano et al., 2021, Appendix, Definition 2). CCS (Ince, 2017) takes the double redundancy as the pointwise double co-information at the samples whose marginal and full pointwise mutual informations share a sign (Mediano et al., 2021, Appendix, Definition 1; 2025, SI Appendix, Definition 2); phyid applies a different fifth condition (S3 Text). The prewhitened CCS values of S11 Table were computed with phyid's mask; every other CCS value in the paper uses the published definition.

### The closed form

For unit-variance stationary AR(1) processes the correlation matrix of (x_t, y_t, x_{t+1}, y_{t+1}) is

S₄ = [[1, q, a, aq], [q, 1, aq, a], [a, aq, 1, q], [aq, a, q, 1]];

its block determinants and the Möbius inversion of Mediano et al. (2021), a linear system with no sign constraint, give the atoms of Results 1, checked to 4 × 10⁻¹⁵ (S3 Text). With unequal coefficients the cross-lag entries are a_y q and a_x q; on a grid of mean a 0.80–0.90, q 0.05–0.70 and |a_x − a_y| up to 0.10 the statements of Results 1 hold to 7 × 10⁻¹⁶ (S18 Table). A pair sharing a slow component gives the same τ = 1 signature, and the two are not separable at that lag: any positive-definite stationary 4 × 4 matrix of (x_t, y_t, x_{t+1}, y_{t+1}) is the lag-0/lag-1 structure of a stable VAR(1) (S3 Text).

### Regional maps

The partialled map is the residual of the regional map's regression on regional r₁ (S3 Text). The correlations were spin-tested with 10,000 rotations of the 99 cortical parcels (Alexander-Bloch et al., 2018; rotations of Váša et al., 2018, released with the data; S5 Table), and the residual map's network structure with the same rotations, subcortex fixed (B22).

### Inference

Pre-injection windows are 1–4 (bins 1–8), post windows 6–14 (bins 11–28). Inference: an exact sign-flip permutation over the 14 subjects (16,384 assignments, two-sided), and a 95 % interval obtained by inverting that test — the set of values μ for which the test of a mean of μ has p > 0.05 — so that an interval excludes zero exactly when p < 0.05. The subject-bootstrap percentile intervals of earlier versions were narrower, by a median of 12.5 % and by 7–16 % for 929 of the 932 quantities (S17 Table; the other three had limits printed at five decimals). Correlations across subjects carry Fisher-z intervals. A phase-randomised surrogate (Theiler et al., 1992) checks stationarity; motion control residualised window means on framewise displacement. r₁ is the regions' mean sample lag-1 autocorrelation within a window; ΦR is TDMI − I(X;X′) − I(Y;Y′) + rtr. Seed 20261120.

### The primary contrast and the exploratory analyses

The pre-specified DiD of whole-brain MMI-sts on ts_gsr at W = 60 is the primary contrast. It was planned as a directional test of an increase; its statistic and the directional-failure rule were fixed after global fits on the same data had shown a decrease (Pre-registration and deviations), so it is not a blind confirmation. Every other quantity is exploratory and is reported with its effect size and interval, without threshold language; a p value quoted for an exploratory quantity describes the sample and is not a claim. An earlier weighting rule, adopted at write-up after the results it governed existed, has been withdrawn (S5 Text).

### The AR(1)-substituted estimate and its calibration

The AR(1)-substituted estimate replaces a window's two cross-lag correlations by a_y q and a_x q. The calibration simulates the design (14 subjects × 2 runs × 840 samples × 300 pairs, the DMT run changed from sample 300, 50 replicates) on AR(1) pairs at the data's population-level coefficient (a_x, a_y ~ N(0.85, 0.0125)), whose windowed level (0.715) lies far below the data's (1.155), and a band-passed generator solved to the data's window-level operating point (S3 Text; S10 Table). The same construction with no change is the finite-sample null of the residual (+0.0054; `notes/review_results/logs/review_v2_residual_null.log`). B22 computed the aligned statistic A_other, each pair's δ_sym (the symmetric cross-lag departure) signed by its lag-0 correlation in the other run, so that no window selects its own sign; B23 the residual's response to five constructions of a change in lagged structure; B24 these statistics' pure-autocorrelation expectations on the band-passed generator; each under a rule and prediction recorded beforehand (S18 Table).

### Remedies

Prewhitening replaced each region's series by the residuals of its own AR(p) fit (p by BIC over 1–5, or p = 1; S11 Table). HRF deconvolution used rsHRF 1.7.0 (Wu et al., 2013, 2021; S2 Text). Manufacture was assessed on four matched pairs of simulated conditions (S16 Table).

### Literature search

Published empirical fMRI ΦID studies reporting synergy, redundancy or quantities built on them were identified by web search on 14 September 2026 and their main texts read in full on 20 September for the quantity reported, preprocessing, parcellation, redundancy function, lag and any treatment of autocorrelation; the map's scope is Gaussian-MMI at TR ≈ 1–3 s, and the table marks the studies outside it. The TR range was fixed before the search, a scoping rule that places the human data of Luppi et al. (2022), at TR 0.72 s, outside the set (Discussion).

### Use of AI tools

The analysis code, the verification scripts, the closed-form implementation, the design of the post hoc computations, the adversarial reviews and citation audits, and the drafts of this text were produced with an AI system, Claude (Anthropic), working under the direction of V.S.; the model of each contribution is named in the trailers of the commits that carry it. The system proposed analyses, interpretations and wording. V.S. decided what was pre-specified, run, closed and reported, ran every computation on the data on his own machine, and accepted, revised or rejected each proposal. The outputs were checked in three ways: every number in the text against the result file that holds it (a table of every number with its source accompanies the manuscript); the mathematical claims by independent recomputation, the closed form against phyid to 10⁻¹⁴; and the text by independent reviews and citation audits against the full text of every cited work, including those of 20 and 22 September 2026, whose findings and dispositions are in S5 Text. The authors are responsible for the content.

### Pre-registration and deviations

The analysis was pre-specified in a git-tracked record rather than a registry. The up-regulation hypothesis was recorded before any data were analysed; a 20-region global fit run as a pipeline check was inspected, and showed a decrease, before the initial commit, which carries both; the directional-failure rule and the windowed test statistic were written on the next day after a 115-region global fit had shown a decrease, and the post set was moved from windows 5–14 to 6–14 on evidence from that fit. The windowed estimator, window sets, nulls and motion rule were fixed before any windowed result existed. The estimator account arose from an adversarial review after the primary result; its plans were written after that review's computations had characterised the phenomenon, and every later computation was entered in the record with its rule and prediction before it was run and its outcome appended afterwards. The deviations are: the diagnostic's branch rule, replaced by the calibrated reference; a write-up weighting rule, withdrawn; a split-half rule whose threshold lay above the reliability ceiling; the calibration's first-order prediction for a coupling change, which failed in form, the band-passed repetition's prediction for the same rows, which was not met, and its pure-autocorrelation residual, which missed low; the quotation of the first calibration's coupling rows where the repetition's rule named the repetition; and a reading of the residual's direction built after the first of those failures, since withdrawn. Each is stated where it arises and listed in S5 Text.

---

## Acknowledgments

[TK: acknowledgments, once the author list is settled]

---

## Supporting information

S1 Text. The original pre-specified analysis and its results: the ethics statement's regulatory detail, the dataset and the estimator; the up-regulation hypothesis, the directional-failure rule, the windowed test, the intensity-tracking criterion with its controls and the void verdict, the redundancy prediction, the exploratory regional analysis, the EEG Lempel-Ziv check and robustness across estimators.

S2 Text. The ΦR exploration and HRF deconvolution (every result in it post hoc) and why it was closed.

S3 Text. The supporting tables of the estimator account: the sensitivity variant and the CCS atoms beside Table 1; the CCS definition check; the closed form's checks and the coupled family; the scope map, the within-window regression and the regional maps; the DMT contrast's collinearity, the CCS contrast and its decomposition; the residual's finite-sample null, the cross-lag departure, its budget, the directed and aligned statistics and the split-half test; the calibration on both generators; the prewhitened series' spectrum; manufacture and the lag variants; and the applicability table with its search record.

S4 Text. The COBIDAS reporting checklist for MRI, filled for this secondary analysis.

S5 Text. Provenance and audit trail: the history of the study commit by commit, the multiplicity count and the withdrawn weighting rule, the run inventory with the attempts at the single full run, the reviews and audits, and every commit identifier the text of this paper rests on.

S1–S18 Tables. S1 Table, the step contrast on the sensitivity windows; S2 Table, tier-2 intensity tracking; S3 Table, the exploratory regional DiD; S4 Table, the exploratory workspace comparison; S5 Table, the exploratory receptor-map correlations, with the spin-test p values of the regional sts–r₁ correlations in its note; S6 Table, EEG Lempel-Ziv complexity against the ΦID quantities; S7 Table, global functional connectivity per bin set; S8 Table, the post-hoc proportionality ratio DiD; S9 Table, the cross-lag budget with its null, its controls and the superseded values; S10 Table, the calibration on the AR(1) and the band-passed generator at both estimators; S11 Table, the prewhitening check and the whitened series' spectrum; S12 Table, the residual by variant and estimator; S13 Table, the sts change by estimator, with population and window-level autocorrelation changes; S14 Table, lag dependence; S15 Table, CCS-sts and ΦR by variant and estimator; S16 Table, manufacture; S17 Table, every interval of a mean over subjects by method; S18 Table, the residual's response to changes in lagged structure and its pure-autocorrelation expectations (B23, B24).

---

## Figures

Figure 1. The sixteen atoms under MMI, observed and AR(1)-substituted from each pair's measured (a_x, a_y, q): levels and DiDs (`manuscript/figures/fig1_v2_atoms_observed_substituted.pdf`). Figure 2. The scope map: sts over (r₁, q) with one subject's pre-injection pairs pooled, the excess sts − (xtx + yty), and sts against lagged coupling c at fixed r₁ for q = +0.25 and, mirrored, q = −0.25 (`fig2_v2_scope_map.pdf`). Figure 3. Per-subject DiDs: (a) sts against lag-1 autocorrelation, with the OLS fit and the band-passed generator's rate; (b) the cross-half relation; (c) the residual against lag-1 autocorrelation, with the generators' rates (`fig3_v2_per_subject.pdf`). Figure 4. The AR(1)-substituted estimate by window: observed and AR(1)-substituted sts, the residual, and the DMT − placebo residual difference against its expectation under a pure autocorrelation change, with within-subject bands (within-subject SEM: Cousineau, 2005; Morey, 2008; `fig4_v2_residual_diagnostic.pdf`). Figure 5. Lag dependence (`fig5_v2_lag_dependence.pdf`). Figure 6. Regional sts against regional r₁ by network, the sensory–association contrast before and after partialling r₁ out, and the residual map's network means with their spin test (`fig6_v2_regional.pdf`). Captions are in `manuscript/figures/captions_v2.md`; all six are generated by `scripts/15_figures_v2.py` from the committed result files, and the committed figure files and captions are those the script wrote at the commit that carries them.

---

## Data and code availability

Manuscript for co-author review; not for citation or distribution. Every number in this paper is quoted from the result files of the repository — `results/*.csv`, the record `manuscript/analysis_record.md`, the review and calibration result files under `notes/review_results/`, and, where named in the supporting information, the check logs of the reviews under `notes/` — with [TK] marking a value that no file holds; a table listing every number of the main text with its source file and row accompanies the manuscript (`manuscript/main_text_numbers.csv`). Time series, ratings, framewise displacement and the EEG regressor are from https://github.com/singlesp/DMT_NCT (Singleton et al., 2025; Zenodo 10.5281/zenodo.15177511; upstream commit 77af7aa), cloned into `external/DMT_NCT/` and not redistributed; the release carries no licence file, and the data are used with the written agreement of the data collectors and the derivative authors. Analysis code, the pinned environment (`requirements.lock.txt`), every results table, the pre-specification record, the adversarial reviews and the citation audits (`notes/`, `notes/review_2026-09-20/`, `notes/review_2026-09-22/`), the calibration and remedy computations with their result files (`notes/partB14_*.py`–`partB24_*.py`, `partB16b_*.py`, `partB17b_*.py`; `notes/review_results/partB/`) and the closed-form implementation (`notes/rev_phiid_fast.py`) are at https://github.com/Vasilis540/dmt-phiid. The repository's full history is public. The `notes/` outputs name the producing commit in their headers (`git=<SHA>`; `-dirty` where the tree had uncommitted changes; `nogit` for the deconvolution files written in a sandbox). `run_all.sh` regenerates the original analysis's tables and figures (sections 0–5) and then, in its section 6, every review, calibration and remedy computation in dependency order and `scripts/15_figures_v2.py`. B21–B24 were run at commit a9d9ca4 on V.S.'s machine (8 min wall-clock); B23 and B24, which use no data, were re-run independently and reproduced every reported value, the differences lying at the level of floating-point rounding (10⁻¹⁶). `run_all.sh` is executed as one run at the final commit before submission ([TK: the commit, the date, the wall-clock, and the verdicts of 6_committed_compare and 8_binary_compare]); the earlier attempts are recorded in S5 Text. The HRF-deconvolution items need the sandbox described in `notes/rev_deconv.py` and are skipped unless it is present. Seed 20261120 throughout.

---

## Author contributions (CRediT)

V.S.: conceptualisation, methodology, software, formal analysis, investigation, data curation (secondary), writing — original draft, writing — review and editing, visualisation, project administration. C.T.: resources (data acquisition), writing — review and editing [TK]. S.P.S.: data curation (the released derivative dataset), resources (data release), validation (confirmation of the mean-filled parcel, Methods, Dataset), writing — review and editing [TK]. [TK: further contributors nominated by C.T.]

## Funding

V.S. received no specific funding for this work. [TK: funding statements of C.T. and S.P.S., if any apply to their contributions.]

## Competing interests

V.S. is preparing an application for a PhD position in the Cognition and Consciousness Imaging Group, Division of Anaesthesia, University of Cambridge, whose members authored Luppi et al. (2022, 2024), the studies whose estimator this paper analyses; this work was produced in part as evidence of competence for that application, as the repository's public record states. C.T. is a co-author of Timmermann et al. (2023), the source of the data, and of Singleton et al. (2025); S.P.S. is the first author of Singleton et al. (2025), the source of the released derivatives. No other conflicts are declared [TK].

---

## References

[Every entry except the software was read in full (main article; supplementary materials only where named) on 20 September 2026 from the publisher's or preprint server's PDF, including the SI Appendix of Mediano et al. (2025); Arbabshirani et al. (2014) was read in its NIH author manuscript and Faes et al. (2025) in its arXiv version. The exceptions are seven entries added on 20 September: Cousineau (2005), Morey (2008) and Wu et al. (2021) were read in full on 22 September 2026 from the publishers' open-access pages, Tian et al. (2020) from its bioRxiv preprint (v2), and Váša et al. (2018) in its Methods and Results on the publisher's page; Theiler et al. (1992) and Alexander-Bloch et al. (2018) could not be obtained in full text and were checked against their abstracts and bibliographic records only. Bibliographic details were checked against Crossref, the publisher page or the preprint server on 15, 17 and 20 September 2026. The audits and their record entries are in S5 Text.]

Afyouni, S., Smith, S. M., & Nichols, T. E. (2019). Effective degrees of freedom of the Pearson's correlation coefficient under autocorrelation. *NeuroImage*, 199, 609–625. https://doi.org/10.1016/j.neuroimage.2019.05.011

Alexander-Bloch, A. F., Shou, H., Liu, S., Satterthwaite, T. D., Glahn, D. C., Shinohara, R. T., Vandekar, S. N., & Raznahan, A. (2018). On testing for spatial correspondence between maps of human brain structure and function. *NeuroImage*, 178, 540–551. https://doi.org/10.1016/j.neuroimage.2018.05.070

Arbabshirani, M. R., Damaraju, E., Phlypo, R., Plis, S., Allen, E., Ma, S., Mathalon, D., Preda, A., Vaidya, J. G., Adali, T., & Calhoun, V. D. (2014). Impact of autocorrelation on functional connectivity. *NeuroImage*, 102(Pt 2), 294–308. https://doi.org/10.1016/j.neuroimage.2014.07.045

Barrett, A. B. (2015). Exploration of synergistic and redundant information sharing in static and dynamical Gaussian systems. *Physical Review E*, 91(5), 052802. https://doi.org/10.1103/PhysRevE.91.052802

Bartlett, M. S. (1935). Some aspects of the time-correlation problem in regard to tests of significance. *Journal of the Royal Statistical Society*, 98(3), 536–543. https://doi.org/10.2307/2342284

Cliff, O. M., Novelli, L., Fulcher, B. D., Shine, J. M., & Lizier, J. T. (2021). Assessing the significance of directed and multivariate measures of linear dependence between time series. *Physical Review Research*, 3(1), 013145. https://doi.org/10.1103/PhysRevResearch.3.013145

Cousineau, D. (2005). Confidence intervals in within-subject designs: A simpler solution to Loftus and Masson's method. *Tutorials in Quantitative Methods for Psychology*, 1(1), 42–45. https://doi.org/10.20982/tqmp.01.1.p042

Down, K. J. A., Huntley, J., Mediano, P. A. M., & Bor, D. (2026). Synergistic and redundant information dynamics are modulated by Alzheimer's disease and cognitive impairment. *bioRxiv*, 10.64898/2026.02.18.706630 (preprint; PubMed 41757079, PMC12934565; no journal version found on 15 September 2026).

Faes, L., Marinazzo, D., & Stramaglia, S. (2017). Multiscale information decomposition: Exact computation for multivariate Gaussian processes. *Entropy*, 19(8), 408. https://doi.org/10.3390/e19080408

Faes, L., Sparacino, L., Mijatovic, G., Antonacci, Y., Ricci, L., Marinazzo, D., & Stramaglia, S. (2025). Partial information rate decomposition. *Physical Review Letters*, 135(18), 187401. https://doi.org/10.1103/nrwj-n8lj (arXiv 2502.04550; the quotations in S3 Text are from the arXiv version dated 7 October 2025)

Gatica, M., Atkinson-Clement, C., Mediano, P. A. M., Alkhawashki, M., Ross, J., Sallet, J., & Kaiser, M. (2024). Transcranial ultrasound stimulation effect in the redundant and synergistic networks consistent across macaques. *Network Neuroscience*, 8(4), 1032–1050. https://doi.org/10.1162/netn_a_00388

Honari, H., Choe, A. S., Pekar, J. J., & Lindquist, M. A. (2019). Investigating the impact of autocorrelation on time-varying connectivity. *NeuroImage*, 197, 37–48. https://doi.org/10.1016/j.neuroimage.2019.04.042

Huang, Z., Liu, X., Mashour, G. A., & Hudetz, A. G. (2018). Timescales of intrinsic BOLD signal dynamics and functional connectivity in pharmacologic and neuropathologic states of unconsciousness. *Journal of Neuroscience*, 38(9), 2304–2317. https://doi.org/10.1523/JNEUROSCI.2545-17.2018

Imperial-MIND-lab (2026). phyid: Python package for Integrated Information Decomposition (ΦID) [computer software, BSD-3-Clause]. GitHub repository, https://github.com/Imperial-MIND-lab/integrated-info-decomp, at commit 6c5f2e9d33c985efbdf875d45cb5a2a6a5cdbf44 (merge of pull request #4, 13 March 2026; the commit pinned in `requirements.lock.txt`). The repository asks users to cite Mediano et al. (2025) and Luppi et al. (2022).

Ince, R. A. A. (2017). Measuring multivariate redundant information with pointwise common change in surprisal. *Entropy*, 19(7), 318. https://doi.org/10.3390/e19070318

Ito, T., Hearne, L. J., & Cole, M. W. (2020). A cortical hierarchy of localized and distributed processes revealed via dissociation of task activations, connectivity changes, and intrinsic timescales. *NeuroImage*, 221, 117141. https://doi.org/10.1016/j.neuroimage.2020.117141

Kay, J. W., & Ince, R. A. A. (2018). Exact partial information decompositions for Gaussian systems based on dependency constraints. *Entropy*, 20(4), 240. https://doi.org/10.3390/e20040240

Liardi, A., Rosas, F. E., Carhart-Harris, R. L., Blackburne, G., Bor, D., & Mediano, P. A. M. (2025). Null models for comparing information decomposition across complex systems. *PLOS Computational Biology*, 21(11), e1013629. https://doi.org/10.1371/journal.pcbi.1013629 (arXiv 2410.11583)

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Holland, N., Fryer, T. D., O'Brien, J. T., Rowe, J. B., Menon, D. K., Bor, D., & Stamatakis, E. A. (2022). A synergistic core for human brain evolution and cognition. *Nature Neuroscience*, 25(6), 771–782. https://doi.org/10.1038/s41593-022-01070-0

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Allanson, J., Pickard, J. D., Williams, G. B., Craig, M. M., Finoia, P., Peattie, A. R. D., Coppola, P., Menon, D. K., Bor, D., & Stamatakis, E. A. (2023). Reduced emergent character of neural dynamics in patients with a disrupted connectome. *NeuroImage*, 269, 119926. https://doi.org/10.1016/j.neuroimage.2023.119926 (bioRxiv 2022.06.16.496445)

Luppi, A. I., Mediano, P. A. M., Rosas, F. E., Allanson, J., Pickard, J. D., Carhart-Harris, R. L., Williams, G. B., Craig, M. M., Finoia, P., Owen, A. M., Naci, L., Menon, D. K., Bor, D., & Stamatakis, E. A. (2024). A synergistic workspace for human consciousness revealed by Integrated Information Decomposition. *eLife*, 12, RP88173 (version of record, version 4, 18 July 2024). https://doi.org/10.7554/eLife.88173.4

Luppi, A. I., Uhrig, L., Tasserie, J., Mediano, P. A. M., Rosas, F. E., Singleton, S. P., Gutierrez-Barragan, D., Gini, S., Castro, P., Signorelli, C. M., Golkowski, D., Ranft, A., Ilg, R., Jordan, D., Muta, K., Hata, J., Okano, H., Liu, Z.-Q., Yee, Y., Destexhe, A., Cofre, R., Menon, D. K., Gozzi, A., Jarraya, B., & Stamatakis, E. A. (2026). Convergent transcriptomic and connectomic controllers of information integration and its anaesthetic breakdown across mammalian brains. *Nature Human Behaviour*, 10(4), 777–802. https://doi.org/10.1038/s41562-025-02381-5

Mediano, P. A. M., Rosas, F. E., Luppi, A. I., Carhart-Harris, R. L., Bor, D., Seth, A. K., & Barrett, A. B. (2021). Towards an extended taxonomy of information dynamics via Integrated Information Decomposition. *arXiv*, 2109.13186 (v1; Appendix, Definition 1 is the CCS double-redundancy definition used here).

Mediano, P. A. M., Rosas, F. E., Luppi, A. I., Carhart-Harris, R. L., Bor, D., Seth, A. K., & Barrett, A. B. (2025). Toward a unified taxonomy of information dynamics via Integrated Information Decomposition. *Proceedings of the National Academy of Sciences*, 122(39), e2423297122. https://doi.org/10.1073/pnas.2423297122 (SI Appendix: Definition 1 is MMI, Definition 2 the CCS double-redundancy definition used here; Sec. III.A states that MMI ΦID atoms can be negative; checked 15 and 20 September 2026)

Morey, R. D. (2008). Confidence intervals from normalized data: A correction to Cousineau (2005). *Tutorials in Quantitative Methods for Psychology*, 4(2), 61–64. https://doi.org/10.20982/tqmp.04.2.p061

Murray, J. D., Bernacchia, A., Freedman, D. J., Romo, R., Wallis, J. D., Cai, X., Padoa-Schioppa, C., Pasternak, T., Seo, H., Lee, D., & Wang, X.-J. (2014). A hierarchy of intrinsic timescales across primate cortex. *Nature Neuroscience*, 17(12), 1661–1663. https://doi.org/10.1038/nn.3862

Nago, H., Kojima, H., Yamaguchi, H., & Yamashita, Y. (2026). Synergistic and redundant information dynamics exhibit dissociable alterations across schizophrenia and neurodevelopmental conditions. *Brain Informatics*, 13(1), 25. https://doi.org/10.1186/s40708-026-00312-2

Raut, R. V., Snyder, A. Z., & Raichle, M. E. (2020). Hierarchical dynamics as a macroscopic organizing principle of the human brain. *Proceedings of the National Academy of Sciences*, 117(34), 20890–20897. https://doi.org/10.1073/pnas.2003383117

Schaefer, A., Kong, R., Gordon, E. M., Laumann, T. O., Zuo, X.-N., Holmes, A. J., Eickhoff, S. B., & Yeo, B. T. T. (2018). Local-global parcellation of the human cerebral cortex from intrinsic functional connectivity MRI. *Cerebral Cortex*, 28(9), 3095–3114. https://doi.org/10.1093/cercor/bhx179

Singleton, S. P., Timmermann, C., Luppi, A. I., Eckernäs, E., Roseman, L., Carhart-Harris, R. L., & Kuceyeski, A. (2025). Network control energy reductions under DMT relate to serotonin receptors, signal diversity, and subjective experience. *Communications Biology*, 8(1), 631. https://doi.org/10.1038/s42003-025-08078-9

Tarchi, L., Lasagni, L., Ubaldi, L., Bottacin, J., Lodovici, E., Di Giacomo, A., Zompa, L., Pisano, T., Bianchi, A., D'Incerti, L., Castellini, G., & Ricca, V. (2026). Disrupted emergent properties of the brain in schizophrenia: Insight from Integrated Information Decomposition of resting state fMRI. *Brain and Behavior*, 16(4), e71352. https://doi.org/10.1002/brb3.71352 (read in full on 20 September 2026; a deconvolving study, see S3 Text)

Theiler, J., Eubank, S., Longtin, A., Galdrikian, B., & Farmer, J. D. (1992). Testing for nonlinearity in time series: the method of surrogate data. *Physica D: Nonlinear Phenomena*, 58(1–4), 77–94. https://doi.org/10.1016/0167-2789(92)90102-S

Tian, Y., Margulies, D. S., Breakspear, M., & Zalesky, A. (2020). Topographic organization of the human subcortex unveiled with functional connectivity gradients. *Nature Neuroscience*, 23(11), 1421–1432. https://doi.org/10.1038/s41593-020-00711-6

Timmermann, C., Roseman, L., Haridas, S., Rosas, F. E., Luan, L., Kettner, H., Martell, J., Erritzoe, D., Tagliazucchi, E., Pallavicini, C., Girn, M., Alamia, A., Leech, R., Nutt, D. J., & Carhart-Harris, R. L. (2023). Human brain effects of DMT assessed via EEG-fMRI. *Proceedings of the National Academy of Sciences*, 120(13), e2218949120. https://doi.org/10.1073/pnas.2218949120

Varley, T. F. (2024). Considering dynamical synergy and integrated information; the unusual case of minimum mutual information. *arXiv*, 2407.16601. Preprint, not peer reviewed.

Váša, F., Seidlitz, J., Romero-Garcia, R., Whitaker, K. J., Rosenthal, G., Vértes, P. E., Shinn, M., Alexander-Bloch, A., Fonagy, P., Dolan, R. J., Jones, P. B., Goodyer, I. M., the NSPN consortium, Sporns, O., & Bullmore, E. T. (2018). Adolescent tuning of association cortex in human structural brain networks. *Cerebral Cortex*, 28(1), 281–294. https://doi.org/10.1093/cercor/bhx249

Williams, P. L., & Beer, R. D. (2010). Nonnegative decomposition of multivariate information. *arXiv*, 1004.2515.

Wu, G.-R., Liao, W., Stramaglia, S., Ding, J.-R., Chen, H., & Marinazzo, D. (2013). A blind deconvolution approach to recover effective connectivity brain networks from resting state fMRI data. *Medical Image Analysis*, 17(3), 365–374. https://doi.org/10.1016/j.media.2013.01.003

Wu, G.-R., Colenbier, N., Van Den Bossche, S., Clauw, K., Johri, A., Tandon, M., & Marinazzo, D. (2021). rsHRF: A toolbox for resting-state HRF estimation and deconvolution. *NeuroImage*, 244, 118591. https://doi.org/10.1016/j.neuroimage.2021.118591

Yeo, B. T. T., Krienen, F. M., Sepulcre, J., Sabuncu, M. R., Lashkari, D., Hollinshead, M., Roffman, J. L., Smoller, J. W., Zöllei, L., Polimeni, J. R., Fischl, B., Liu, H., & Buckner, R. L. (2011). The organization of the human cerebral cortex estimated by intrinsic functional connectivity. *Journal of Neurophysiology*, 106(3), 1125–1165. https://doi.org/10.1152/jn.00338.2011

Zhang, X., Han, C., Xia, J., Deng, L., & Dong, J. (2025). Dynamic synergy network analysis reveals stage-specific regional dysfunction in Alzheimer's disease. *Brain Sciences*, 15(6), 636. https://doi.org/10.3390/brainsci15060636
