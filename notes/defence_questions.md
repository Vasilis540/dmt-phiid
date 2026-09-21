# Defence questions for `manuscript/draft_v2.md`

Rewritten 21 September 2026 (round 14) to the restructured text: twenty-four questions a hostile reviewer or an interviewing professor could ask about the paper as it now stands, ordered from most to least dangerous, each with an answer the first author can give from memory (two to four sentences) and the part of the paper that backs it. Every number is the paper's (its tables, its supporting texts, and the result files under `notes/review_results/`); where a number is still a [TK: B16b] or [TK: B17b] placeholder in the text, the answer says so. The earlier versions of this file (15–20 September) answered the drafts of those dates and are superseded; the record keeps them in git.

---

**1. Your planned directional test was that synergy goes up under DMT. It went down, and now the paper is about the estimator. Isn't this a failed study repackaged?**

The paper says so in its own words: it began as a planned directional test recorded before the primary analysis, the test refuted the hypothesis under the directional-failure rule (whole-brain MMI-sts DiD −0.0809 nats, sign-flip p = 0.0038, 13 of 14 subjects; Results 2, Table 2), and that refutation is the paper's one confirmatory result. What was found afterwards — that the atom is mostly self-prediction and the fall is the size the pairs' autocorrelation change predicts — was derived to account for the refutation, and everything after the confirmatory contrast is labelled exploratory and reported with effect sizes and intervals (Methods, "Confirmatory and exploratory analyses"). The history, commit by commit, is S5 Text.

**2. What does the pre-specification establish, given that the refutation rule was written after a global fit had shown the decrease?**

Ordering, not blindness, and the paper says exactly that (Methods, "Pre-registration and deviations"; S5 Text §1). The hypothesis, the windowed estimator, the window sets, the nulls and the motion rule were recorded before the windowed result existed; the directional-failure rule and the post-set change were written after a 115-region global fit had shown a decrease; every later computation was entered in the record with its rule and prediction before it was run. A reader who wants to weigh that can read the dates.

**3. "Mostly self-prediction" — what exactly is proved, and on what?**

On the bivariate AR(1) family with equal coefficients, the Gaussian-MMI atoms are in closed form: sts = xtx + yty + rtr = 2S − C, the six cross-prediction atoms are zero, the four mirror atoms are −(S − C), and TDMI = 2S depends on r₁ alone (Results 1; Methods, "The closed form"). With unequal coefficients MMI takes the smaller self-information, so at q = 0 sts = 2 min(S_x, S_y) exactly and the excess over xtx + yty turns negative — which is what the data's atom table shows once each pair's measured (a_x, a_y, q) is put into the family (Table 1, Fig 1). The identities are checked numerically to 4 × 10⁻¹⁵; the q = 0 identity to 2 × 10⁻¹⁶ (S3 Text §3).

**4. How much does autocorrelation matter compared with the cross-correlation? The old title said "dominates"; the abstract now gives exchange rates.**

In data units at the operating point of BOLD pairs, (r₁, q) = (0.85, 0.25): 0.01 of r₁ is worth 0.061 nats of sts, 0.1 of |q| is worth 0.019, 0.01 of lagged coupling is worth 0.017 at fixed (r₁, q), and 0.01 of within-pair asymmetry 0.031 (a population rate). Per standard deviation of the data's own variation — 0.0125 for regional r₁, 0.196 for pair |q| — the r₁ rate is 0.076 nats and the |q| rate 0.037, a ratio of 2 to 1 (Results 1). The per-unit ratio of 32 that earlier drafts quoted is not in the paper, because it compares units the data do not vary in equally.

**5. Where does the −0.092 prediction come from, and isn't it circular to predict sts from correlations that sts is computed from?**

The prediction keeps each pair's measured lag-1 autocorrelations and lag-0 correlation and replaces only the two cross-lag correlations by the AR(1) values a_y q and a_x q; predicted sts is the closed-form sts of that matrix, with no free parameter (Methods, "The residual diagnostic"). Everything the atom carries beyond those three numbers — every lagged interaction — is in the cross-lag entries, which the prediction sets to the null values, so the prediction is exactly "what sts would be if the pair had the measured autocorrelations and correlation and no lagged interaction". Its DiD is −0.0924 against −0.0809 observed, and the per-subject correlation of predicted and observed is 0.99 (Results 2, Fig 3b).

**6. The residual DiD is positive in every combination and p = 0.042 against zero. Why is that not evidence of a synergy change beyond autocorrelation?**

Because zero is the wrong reference, and the calibration shows it (Results 4, Table 7). On simulated data with a known pure autocorrelation change of the data's size, the diagnostic returns a positive residual DiD of +0.0049 ± 0.0017 at W = 60 on AR(1) pairs — the sampling scatter of the cross-lag correlations lowers the observed sts below its AR(1) prediction by an amount that grows with a, so a fall in a shrinks the over-prediction — and a test of that residual against zero gives p < 0.05 in 82 % of replicates. A lagged-coupling change of either sign lowers the residual, not raises it. Read against its calibrated expectation (+0.0049 on AR(1) pairs, [TK: B17b] on the band-passed generator, +0.0054 under the finite-sample null), the data's +0.0115 [+0.0021, +0.0211] is within it, so the paper reports no evidence of a change in lagged interaction and does not test the residual against zero anywhere.

**7. You calibrated on AR(1) pairs whose windowed sts level is 0.715 where the data's is 1.155. Why should that calibration transfer?**

That is why the calibration was repeated on a band-passed generator with the data's spectrum and window-level operating point (0.8632, 0.2842), whose W = 60 level is near the data's (1.19 in the smoke test against 1.155; the committed table is [TK: B17b]), and the paper quotes that generator where the two differ (Methods, "The residual diagnostic and its calibration"; S3 Text §7; S10 Table). Both are in the supporting information, with the population closed-form reference beside them.

**8. If the residual is finite-sample, why does it correlate at 0.80 with the CCS-sts change across subjects?**

Both are computed from the same 60-TR windows, so the shared variance can be common signal or common estimation noise, and the split-half test that was meant to tell them apart could not at the reliabilities of the two quantities (residual 0.49, CCS-sts 0.30 on ts_gsr; S3 Text §6). The paper reports the four correlations (+0.80, +0.09, +0.88, +0.68 across the variant × estimator combinations), says that the question is undetermined, and reads the CCS increase mechanically (question 12).

**9. What is the run-level residual of −0.014, and what did you find it to be?**

It is the over-prediction of the whole-run sts level by the AR(1) prediction, negative in 14 of 14 subjects on ts_gsr. Splitting each pair's cross-lag deviations into a symmetric part and a directed (antisymmetric) part, the closed-form response of sts to the directed part alone is −0.0064 and to the symmetric part −0.0071, together −0.0137: about half and half; without global signal regression the two are −0.0085 and +0.0092 and cancel (Results 4). The directed part does not change under DMT (+0.0004, p = 0.38), so it contributes nothing to the residual DiD; what produces the symmetric part inside 2-minute windows is not identified, and the paper says so as an unknown.

**10. The regional synergy map: you say the sensory–association contrast vanishes when r₁ is partialled out. Doesn't that just mean synergy and autocorrelation share a gradient, with no way to say which is which?**

Yes, and the paper says exactly that (Results 3). What it establishes is that on this dataset regional sts follows regional r₁ (r = 0.863 over 115 regions, 14 of 14 subjects), that regional r₁ accounts for three-quarters of the map's variance, and that the sensory − association contrast goes from −0.0202 nats (p = 0.006 per subject) to +0.0007 (p = 0.90) when r₁ is regressed out. Which gradient is the cause cannot be told on these data, nothing here bears on any published map, and the one published test of the exposure (Luppi et al. 2022's autocorrelation-preserving surrogates) argues the other way for that gradient's macroscale associations (Discussion).

**11. Why no spin test on the partialled map?**

Because the two inputs are algebraically linked — the residual map is the sts map minus a linear function of the r₁ map — so a spin test of the residual against r₁ answers no question the partialled contrast does not already answer. The spin p values of the raw regional correlations (Spearman +0.771 on the 99 cortical parcels, p < 0.0001) are in the note to S5 Table.

**12. CCS-sts rose under DMT in every combination, 13 of 14 subjects at the global fit. Why is that not a synergy increase?**

Three reasons the paper gives (Results 6). CCS-sts is exactly −(1 − s) c̄_rej per pair, and the increase is carried by the co-information term: the double co-information of the sign-disagreeing samples shrinks in magnitude (c̄_rej DiD −0.0292, 14 of 14 at the global fit; +0.0174 of the +0.0197), not fewer samples rejected. It is a specification chosen after the results were seen, and its sign is the direction the study originally pre-specified, so under the record's closure entry it cannot be read as a DMT finding. And it is exploratory by the paper's single-confirmatory-test rule.

**13. Which CCS definition did you use, and does it matter?**

The published double-redundancy definition (Mediano et al. 2021, Appendix, Definition 1; 2025, SI Appendix, Definition 2), computed with respect to the fitted Gaussian, which for two Gaussian sources is also Ince's published construction. `phyid` applies a different fifth sign condition; the two masks disagree on 6–7 % of samples, differ by 0.002–0.012 nats in level, and their DMT contrasts correlate at 0.97 per subject, so no qualitative statement depends on the choice (Methods, "Redundancy functions"; S3 Text §2).

**14. Prewhitening is the standard remedy for autocorrelation. Why do you say it does not work?**

Because on band-passed data it cannot whiten: 99.2 % of the series' power lies inside 0.01–0.08 Hz, where ideal flat noise at TR 2 s already has r₁ = 0.82. An AR(p ≤ 5) fit (BIC chose p = 5, the top of the range, for 3,218 of 3,220 region × run series) leaves a residual with r₁ = 0.26; sts on it is 0.22 (from 1.155), its contrast −0.026 (p = 0.14), and the diagnostic still predicts −0.019 of that −0.026 from the residual autocorrelation (Results 7). The AR(1) residual keeps r₁ = 0.75, for an analytic reason: ρ₁(ρ₁² − ρ₂)/(1 − ρ₁²) = 0.75 for the pooled placebo function. The in-band power share of the whitened residual is [TK: B16b].

**15. Then why not deconvolve?**

Tried, post hoc (S2 Text). At TR 2 s deconvolution lowers the window-level r₁ from 0.848 to 0.783 and the sts level from 1.155 to 0.832 and leaves the contrast in place (−0.0782, p = 0.0013): it changes the operating point, not the mechanism. The paper does not claim this transfers to TR 0.72 s, where Luppi et al. (2022) report negligible effects of deconvolution on their maps.

**16. You recommend the global fit but keep W = 60 as primary. Which is it?**

W = 60 is primary because it was pre-specified and the two agree (−0.0809 against −0.0801); the global fit is recommended for a contrast between separately fitted runs or groups on manufacture grounds — between conditions of equal analytic sts the windowed estimator manufactures −9 % to +16 % of the observed contrast at W = 60 and up to +33 % at W = 30, the run-level fit ≤ 2 % in three of four matched pairs (Table 8). The qualification is stated: a pre/post contrast within one run under a single fit is exposed to the within-run variance change, which is why the global-fit contrast is quoted as agreement, not confirmation (Results 7).

**17. Your Table 5 gives six different numbers for "the sts change that autocorrelation produces". Which is the right one?**

Each answers a different question, and the table says which: the mean r₁ change through the slope at one point (−0.087); each pair's own (a_x, a_y, q) at the windowed estimator (−0.0924); the population change under the whole autocorrelation-function change (−0.069) and what W = 60 returns of it (−0.056); a simulated Δa on AR(1) pairs in population, at W = 60 and at the global fit ([TK: B17b] ≈ −0.08, −0.042, −0.068); the same on the band-passed generator ([TK: B17b]); and the observed −0.0809. The spread between them is the windowed estimator's shrinkage (15–45 % of a true difference at W = 60) and the residual, seen from different sides.

**18. Isn't the per-subject correlation of 0.95 between the sts and r₁ contrasts inflated by shared windows?**

Yes, and the paper says so and gives the correction: the cross-half correlation — each subject's sts DiD on the odd windows against the r₁ DiD on the even windows and the reverse — is 0.742 and 0.645, mean 0.694, against a ceiling of 0.729 set by the two quantities' split-half reliabilities, a disattenuated 0.95 (Results 2). The two contrasts share their reliable variance; 0.953 is the full-set value.

**19. Why is the r₁ contrast itself not the headline evidence?**

Because it is the mechanism's input, not its evidence, and the paper gives it no physiological reading. Its DiD is −0.0146 [−0.0251, −0.0052], p = 0.0106, and the placebo run's own r₁ drift carries 0.34 of it (sts: 0.40), so the within-DMT-run change is the drug-only estimate (Results 2). The account rests on the closed form, the per-pair prediction and the regional map, none of which uses that p.

**20. Lag dependence: doesn't a longer lag fix it?**

A longer lag reduces everything, the artefact included: r_τ falls from 0.848 to 0.513, 0.139 and −0.202 at τ = 2, 3, 5, the sts level and its contrast fall with it, and the contrast stays −7 %, −24 % and −16 % of the level at τ = 1, 2, 3 (Results 5, Table 6). No lag moves the pairs to a point where q contributes comparably, because no such point exists on the family at BOLD cross-correlations. The paper does not recommend τ > 1.

**21. Is this MMI-specific?**

The paper does not say so. On Gaussian systems every PID whose redundancy depends only on the source–target marginals reduces to MMI when the target is univariate (Barrett 2015; Kay & Ince 2018), which covers the single-target lattice nodes but not the joint-target nodes or the double redundancy, which are ΦID's own; other Gaussian PIDs could share or not share the property, and only MMI and Gaussian CCS were examined (Discussion, Limitations).

**22. Are you saying the published synergy results are artefacts?**

No, and the paper is explicit: every study in the applicability table receives the same conditional sentence — the sign of r₁ change that would produce its reported effect on the map — and none of them reports regional r₁, so nothing here is evidence about any of them (Discussion; S3 Text §10). The one published test, Luppi et al. (2022)'s autocorrelation-preserving surrogates, argues against the exposure for their macroscale associations; the paper states that as the only such evidence in the table.

**23. N = 14, one dataset, one drug. What is the reach?**

The closed form is exact on the family and holds for any Gaussian-MMI ΦID at lag one; the exchange rates are the family's at the operating point of BOLD pairs, which the published studies' bands and TRs place at r₁ = 0.73–0.97 (S3 Text §10); the DMT contrast is a proof of concept on one dataset at TR 2 s without deconvolution; the calibration is on generators solved to this dataset, not on a second dataset (Discussion, Limitations).

**24. What do you want a reader to do?**

Report r₁ beside sts per condition and subject, with the effective sample size it implies; predict each pair's sts from its measured (a_x, a_y, q) and read the residual against a calibration at the study's own operating point, not against zero; prefer the run-level fit for between-run contrasts; not expect prewhitening to remove the property on band-passed data; use CCS as the comparison whose synergy atom is near zero; and, where a null is wanted, use one that preserves each region's autocorrelation, as Luppi et al. (2022) did (Discussion, Recommendations).
