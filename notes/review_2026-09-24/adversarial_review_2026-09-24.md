# Adversarial review of the shortened text (66c6331), 24 Sep 2026

# Referee report on draft_v2.md and its SI (repo at 66c6331)

## Scope and what was checked

I read the main text in full (`manuscript/draft_v2.md`), S1–S5 Text, `supplementary.md` (S1–S18 Tables), `captions_v2.md` and the six figure PNGs. I also read the record entries of 23 Sep and the 22 Sep review and its verification.

I made independent recomputations from committed files only. No file in the repository was modified. My scripts are in `…/scratchpad/verify/review_b27/`: `chk_core.py` (my own 2^14 sign-flip enumeration and interval inversion) and `phiid_cf.py` (my own Gaussian-MMI ΦID via Möbius inversion).

**Numbers.** I found no discrepancy between the main text and the result files at printed precision. The checks covered:
- Table 1 (all 17 rows against `family_atoms_tables.md`).
- Table 2 (every cell, against the pickles and the engine rows of `inference_revision.csv`).
- Table 3 (all 11 rows against B21–B24 outputs).
- The primary, residual and substituted DiDs and their inverted intervals, recomputed from `did_subjects`.
- r₁ DiD and its phase p; placebo shares 0.34/0.40; the |q| conversions; the cross-half r and its Fisher-z intervals; the OLS slopes and intercepts.
- The lag, ΦR, CCS and prewhitening rows of S11, S12, S14 and S15.
- Closed-form constants: 1.2588, 6.0705, −0.1892, −3.09, 1.1711, the sign change at 0.0076–0.008, the coupled-family values 1.2315/1.2155/1.2569/1.3023/1.4111 re-derived by Lyapunov, 32.76, ∂rtr/∂r₁ 0.056, flat-band r₁ 0.8174/0.9699, and the ratios 6.55, 1.89 and 9.75.

The problems are in interpretation, logic, completeness and presentation.

## MAJOR

**M1. The abstract and Author summary claim more than the results support.**
- **(a)** L15: "about 4.7 to 1 per standard deviation across pairs within windows".
  - This is the closed form's derivative ratio applied to within-window SDs (4.66).
  - The windowed estimator's own partial slopes give 1.4 to 1 (5.126×0.0284 vs 0.528×0.1957; S3 L128; Discussion L158). The group-level ratio is 3.3. The abstract quotes only the most favourable figure.
  - Fix: "…about 3–5 to 1 per SD at the closed form's rates (1.4 to 1 at the windowed estimator's own rates)".
- **(b)** L15, L19, L87, L160: "in close to the proportion a generator with the data's spectrum produces".
  - This is never quantified. The data give 5.5 per unit regional r₁ and 5.2 per unit pair-level a; the band-passed generator gives 6.13.
  - The per-subject OLS slope interval [3.41, 5.12] excludes 6.13.
  - The "proportion" is generator-dependent: AR(1) pairs give 3.1.
  - My Fieller 95% interval for mean sts DiD / mean r₁ DiD, from `inference_rows_raw.pkl`, is 5.5 [4.45, 10.5]; the bootstrap gives [4.6, 8.1].
  - Fix: report the ratio with its interval, and write "compatible with the band-passed generator's 6.1 (AR(1) pairs 3.1)".
- **(c)** L15/L87/L160: "share their reliable variance (cross-half r = 0.69, ceiling 0.73)".
  - The disattenuated r is 0.95 [0.62, 0.99]; the lower limit means as little as 38% is shared.
  - Dropping subject 8 lowers the mean cross-half r to 0.49 (ceiling 0.54), computed from `splithalf_subjects.csv`.
  - Fix: "share most of their reliable variance (disattenuated r 0.95, 95% interval 0.62–0.99)". Report leave-one-out results in S3.
- **(d)** L15: "the remainder exceeds what a pure autocorrelation change produces in simulation only weakly (p = 0.11)".
  - It quotes the smallest of three p values (0.108, 0.219, 0.251; L110).
  - Those p values are against calibrations the paper says are "not validated for the residual on this dataset" (L110).
  - "Exceeds" is asserted from p > 0.1, against the policy of L216.
  - "Remainder" is misleading: the substituted fall (0.092) is larger than the observed fall (0.081).
  - Fix: "the observed fall is 0.011 nats smaller than this estimate, against 0.003–0.005 in simulated pure autocorrelation changes; the data do not distinguish the two (exact p 0.11–0.25)…".
- **(e)** L15: "a bivariate first-order autoregressive (AR(1)) pair in closed form".
  - "Bivariate AR(1)" normally means a VAR(1) with cross-coefficients. The family here is two AR(1)s coupled only through the innovation correlation.
  - The closed form covers equal coefficients (and q = 0); the unequal-coefficient statements are numerical on a grid.
  - With lagged coupling the identity sts − (xtx+yty) = rtr fails (S3 L120).
  - Fix: "…of two AR(1) processes coupled only at lag 0 (no lagged interaction)…".
- **(f)** L15 "at the operating point of fMRI region pairs"; L53 "At the operating point of BOLD region pairs".
  - (0.85, 0.25) is this dataset's point: one subject's overlay, TR 2 s, 0.01–0.08 Hz. At TR 0.72 s the ideal r₁ is 0.97 (L168).
  - Fix: "…of region pairs in these data".
- **(g)** L19: "We show that, with the estimator most of these studies use, the synergy value is mostly…".
  - For other studies this is the family's prediction, not something shown (L166: "not evidence about any study").
  - Fix: "We show, on a solvable family and in one fMRI dataset, that…".

**M2. The "refutation" contradicts the paper's own thesis.**
- The text says:
  - L83: "a significant decrease refutes the up-regulation hypothesis".
  - L19: "we report its refutation".
  - L29: "Synergy decreased".
- L158 says the analysis "says nothing about whether synergy in the intended sense is present".
- If MMI-sts is mostly self-prediction, its fall refutes only the operational hypothesis (an increase in whole-brain MMI-sts at W = 60). The rule was also written after the decrease had been seen.
- Fix:
  - L83: "…refutes the hypothesis as operationalised; on the account of Results 1 this bears on MMI-sts, not on synergy in the intended sense".
  - L29: "MMI-sts decreased".
  - Use "MMI-sts" for the measured quantity throughout.

**M3. The residual-rate comparison is contradicted by the paper's own intervals.**
- L110: "the generators give −0.18 to −0.39 … and do not reproduce it". L160: "scales with the autocorrelation change more steeply than in the generators, on either basis".
- The data slope −0.75 [−1.133, −0.374] contains the AR(1) generator's −0.39. The null's −0.37 sits at the edge. Only the band-passed −0.18 lies outside.
- The group-level −0.74 has no interval. From the committed per-subject DiDs (regional-r₁ basis), the ratio of means is −0.79, with Fieller interval [−1.60, −0.08] and bootstrap interval [−1.33, −0.26]. Both contain −0.37 and −0.39.
- An across-subject slope is not the estimand of a within-simulation ratio: the generators apply one Δa to every subject.
- The "holds across split halves (−0.700 and −0.385)" holds on ts_gsr only. On ts_demean the two correlations are −0.598 and −0.052 (`splithalf.log` l. 24).
- Fix:
  - "…the band-passed generator's rate (−0.18) lies outside the data's slope interval; the AR(1) generator's (−0.39) and the null's (−0.37) lie at its edge; at the group level the data do not distinguish among them."
  - Keep "not validated", but ground it in the band-passed comparison and in the generators' lack of between-subject heterogeneity.

**M4. Methods L220 misdescribes the finite-sample null.**
- L220 reads: "The same construction with no change is the finite-sample null of the residual (+0.0054…)".
- The null (S3 L252; `review_v2_residual_null.log`) is a different generator: filters fitted to the placebo and post-DMT ACFs, solved to each run × period cell. It contains the data's autocorrelation change: its own pair-level a DiD is (0.8532−0.8625)−(0.8655−0.8602) = −0.0146. That is the denominator of the −0.37 rate and the value in Table 3's row 5.
- With truly no change the residual DiD would be about 0, not +0.0054.
- Fix: "A third expectation comes from a stationary finite-sample null, a band-passed filter model solved to the data's window-level a and |q| in each run × period cell (and so carrying the data's autocorrelation change, −0.0146): +0.0054 (S3 Text, §6)."

**M5. The pre-registration account is overstated and outcome reporting is selective.**
- **(a)** L176 "Every later computation was entered in the record with its rule and prediction before it was run"; L236 says the same. This is false by the paper's own SI:
  - The finite-sample null (used for p = 0.251 and the −0.37 rate) was "run before any record entry and with no recorded rule" (S3 L252; S5 L7).
  - The manufacture pairs are "a post hoc computation" (S16).
  - The coupled family and the leave-two-out had "no prediction" (S5 L7).
  - The fresh-review checks (p = 0.0001; variance-ratio partialling) had "no pre-recorded rule" (S3 L205, L388).
  - Fix: "Most later computations…; the exceptions (list) are marked post hoc where quoted."
- **(b)** The deviation list (L236) names only the calibration's failures. Other recorded predictions that missed appear nowhere in the paper:
  - B16: r₁ 0.26 left after whitening, "not met as recorded".
  - B16b: in-band share 0.655 against 0.5–0.6.
  - B22: (c) the D DiD; (d) the group-level SDs, the asymmetry slopes and the ts_demean r₁ slope; (e) the unpartialled spin p 0.056.
  - B23: (a4) −24 to −30 δ² against −22; (a5) −1.7/−2.9 against −1.2; (b) the (a1)/(a2) magnitudes; (c) the CCS slope.
  - B24: D.
  - B21 (d) on ts_demean.
  - B19 (b) was logged "met" although |q| carries as much as asymmetry.
  - Two inference deviations are also unlisted. The pre-specified subject-bootstrap interval (record l. 730–732) was replaced by the inverted sign-flip interval. The pre-specified "second null" (phase-randomised, l. 732–744) was demoted to a "stationarity check" (L212; S1 L5).
  - Fix: add an S table of every recorded prediction with its outcome, and add the two inference changes to L236.
- **(c)** L29/L236: "The hypothesis was recorded before any data were analysed". S5 L7 concedes this "rests on document order within the record, not on a commit"; the hypothesis and a 20-region real-data fit share the initial commit.
  - Fix: "The record places the hypothesis before the first data check; git cannot confirm this, since both entered in the initial commit (S5 Text)."

**M6. Results 1 attributes the residual pattern to lagged structure.**
- L57: "the residual columns are the signature of lagged structure the diagonal family lacks (Results 4)".
- The stationary null reproduces about 72% of the W = 60 sts residual level (−0.035 vs −0.049; DMT-pre −0.0353 vs −0.0530). Of it, −0.0348 is the response to the scattered δ_anti (S3 L246).
- The directed RMS (0.0378) is close to 1/√n (0.0345; S3 L215). L110 itself says sampling scatter lowers observed sts.
- The previous draft's qualifying sentence ("almost all of it the sampling scatter of the antisymmetric part") was dropped in the shortening.
- Fix: "…the residual columns are the effect of the windows' cross-lag departures from the AR(1) values; a stationary finite-sample null reproduces about 70% of the sts residual level (S3 Text, §6)."

**M7. The main text is not self-contained: internal labels, undefined symbols, and one symbol for several quantities.**
- **Labels and paths:**
  - Computation codes in the main text: "B22" (L53), "B24" (L116), "B21, B22", "B17b; B24", "B23 (a4), (b)" and similar (L118–132), "B22…B23…B24" (L220), "B21–B24" (L270), "(B23, B24)" (L258). B17, B17b and B21 are never defined.
  - File names and paths: `residual_source.log` (L118) and `notes/…/review_v2_residual_null.log` (L220).
- **Undefined symbols:**
  - c (L55, Table 3); δ and δ_sym (L112, L114).
  - A_other (Table 3 header; defined only at L220); λ and Δa_s (Table 3, L114).
  - "the diagonal family" (L57); "directed/symmetric part of the cross-lag departure" (L116).
  - "manufacture" (L150, used before it is explained); "window-level operating point".
- **r₁ overload:**
  - r₁ means the population coefficient (L39) and the whole-brain mean regional sample r₁ ("Regional r₁ fell", L85; "the paper's r₁ contrast", L118).
  - It also means the regional map (L104), "pair r₁" (L53, L140) — the same quantity as "pair-level a" (L87, L110–118) — and "mean r₁" across group means (L140).
  - The estimators differ: DMT-pre level 0.848 vs 0.863; DiD −0.0146 vs −0.0155. Fig 3a/c draw rates per unit pair-level a on regional-r₁ axes.
- Fix:
  - Define r₁ (population), r̄₁ (mean regional sample lag-1 autocorrelation and its map) and ā (pair-level, from the 4×4 matrix), and use them consistently.
  - Replace every B label with the S table or section it refers to, and move paths to the SI.
  - Define c, δ, δ_sym, δ_anti, A_other, λ and a_s in Results 1 and 4, one sentence each.

**M8. The SI lacks cited content and uses internal process language.**
- The "applicability table (S3 Text)" is cited at L25, L166, L168 and L252, but it is not in S3. S3 L394 points to `notes/partB5_literature_v2.md`, so the nine-study claims cannot be checked from the SI.
- S4 Text (L3) is only a pointer to `supplementary_cobidas.md`, which is keyed to "earlier drafts".
- Internal process labels appear throughout:
  - "Stage B of round 16" (S1 L3, L5; S3 L108, L197, L215, L396); "planning session" and "writer's session" (S18 L1317).
  - "review, section 5" (S3 L203, L388; "the review" is never defined); "the fresh review" (S3 L205, L388).
  - "quoted at (90690f4)" (S17 L380).
- Fix: include Tables A/B as an S table and the updated COBIDAS checklist in S4; replace process labels or define them once in S5.

**M9. The Ethics statement lost its disclosure, and the REC number is missing.**
- L184 reads: "This is a secondary analysis of anonymised released data".
- The round-12 text (35f1c49; still present at 958648f) disclosed that the released ratings table carries subject codes ("an S, a two-digit subject number and two letters"), unused and removed from the tracked files. That sentence was dropped at 106bd33 and is in neither the main text nor the SI. README still says "the paper's Ethics statement states the facts". The codes remain in the public git history (CLAUDE.md).
- "[TK: REC number]" is still open, and the statement does not give the basis for the secondary use.
- Fix:
  - Restore the sentence, and state that the codes persist in the history and in the source release.
  - Confirm with the data authors whether the letters identify anyone; if they do, rewrite the history.
  - Add the REC number and the approval/exemption basis for the secondary use.

**M10. The AI-use statement (L232) overstates validation.**
- The sentence at issue: "the text by independent reviews and citation audits against the full text of every cited work".
- The reviews and audits were done by other sessions of the same AI system (record, 23 Sep 11:31: "two separate Claude instances").
- L290 says Theiler (1992) and Alexander-Bloch (2018) were checked against abstracts only, and Váša (2018) in its Methods/Results only.
- "Closed form against phyid to 10⁻¹⁴": the local series agree only to 1.0×10⁻¹³ (`phiid_fast_validate_local.log`).
- "V.S. … ran every computation on the data" contradicts 90690f4's statement ("It [the AI] … ran the computations of the record's dated entries").
- Fix:
  - Name the model and versions.
  - Replace "independent" with "separate sessions of the same AI system; no human other than V.S. has yet checked the analysis".
  - Add "full texts except the three noted".
  - State who executed which computations.

**M11. Reproducibility: the paper's single end-to-end run has not completed.**
- L270 says `run_all.sh` "regenerates" everything, but six attempts have ended inside step 2 (S5 L23).
- Outputs come from at least ten commits. Some carry `-dirty` (`results/global_fc_*` at 66b570e-dirty, the source of S7 Table; the logdet check at 8554b3d-dirty); others carry `nogit` (the 20-region fit and all deconvolution files).
- The deconvolution results (Results 7, S2) cannot be regenerated from the release: the sandbox is absent and the rsHRF parameters are not stated.
- Fix:
  - Complete the run at the submission commit, and report its verdicts.
  - Archive the code and outputs with a DOI.
  - Give the deconvolution parameters, or label those results as not reproducible from the release.

**M12. Limitations were deleted rather than moved.**
- The 90690f4 Limitations sentence is gone from both the text and the SI. It read: "the AR(1) family does not fit the data beyond lag 1, the coupled family is symmetric, what acts inside the windows… is not identified, and the windowed estimator's finite-sample manufacture is not removed by the diagnostic", with the generators "solved to this dataset's operating point… not on a second dataset".
- This breaks the decision's rule that material only moves.
- The deleted caveats matter: r₂ = 0.513 in the data vs 0.72 for an AR(1) with a = 0.848; L55's "Lagged interaction moves sts non-monotonically" rests on symmetric coupling only.
- Fix: restore the sentence in the Limitations.

**M13. The CCS claims are too strong.**
- Where: L15 "near zero but moves inversely with r₁"; the L138 heading; L140 "its dependence on r₁ is weaker and of the opposite sign, not absent"; L172 "do not treat CCS as free of it".
- The evidence behind them is weak:
  - The group-mean r = −0.64 is across 28 condition × window means and is confounded with the drug time course: CCS-sts rose while r₁ fell.
  - The per-subject r of −0.27 to −0.43 all have Fisher intervals that include 0, at a reliability of 0.30.
  - The family is flat and non-monotone in r₁ (−0.013 per unit).
  - L140's r = −0.011 comes from one subject's one window (S3 L124).
- Fix:
  - Abstract: "Under CCS the synergy atom is near zero (−0.05 nats) and nearly flat in r₁ on the family; in these data it rose while r₁ fell (per-subject r −0.27 to −0.43, intervals including zero)."
  - Retitle Results 6 accordingly and drop "not absent".

**M14. The recommended null (L172) invites the error the paper documents.**
- L172 reads: "Where a null is wanted, preserve… — the AR(1)-substituted matrix…".
- Read literally, this tests observed − substituted against zero. Results 4 shows that difference has a non-zero finite-sample expectation (level −3%; DiD +0.003 to +0.005).
- Fix: "surrogate series simulated from each pair's AR(1)-substituted matrix (or from the two spectra with the measured lag-0 correlation) and passed through the same estimator; the substituted value itself is not a null."

**M15. What does the Methods article deliver?**
- The recommended estimate's residual "cannot be attributed" and its calibration is "not validated".
- The closed form is a direct Möbius inversion.
- Mediano et al. (2021, Fig 5, App. VI) already computed atoms for a coupled AR pair; this is acknowledged only in S3 L120.
- Fix:
  - Acknowledge Mediano 2021 in the L27 novelty sentence.
  - Release the closed form and the substituted estimate as a documented, tested function.
  - Pair it with the simulated null of M14.

## MINOR

1. **PLOS figure order.** Fig 2a (L53) and Fig 2c (L55) are cited before Fig 1 (first cited in Table 1's caption, L59). Fig 6 (L104) is cited before Figs 4 and 5 (L108, L136). Renumber the figures in order of first citation.
2. **PLOS section order.** Currently: SI list (L246) → Figures → Data availability → contributions, funding, interests → References.
   - PLOS wants Acknowledgments → References → SI captions, with figure captions placed after the paragraph of first citation. Merge the captions from `captions_v2.md`.
   - Remove "Manuscript for co-author review; not for citation or distribution." from L270.
   - L258 lumps S1–S18 Tables into one paragraph; give one caption per file.
3. **Supporting-information citations.** S4 Text and S1–S4, S6, S7, S9 and S12 Tables are not cited in the main text. Cite S12 in Results 4 at least.
4. **References.** Faes et al. (2025) is listed but cited only in S3 L396: cite it in the main text or move it to S3's own list. Remove the internal head note (L290) and convert to numbered style.
5. **S5 L3 and S3 L3** say the main text "carries no commit identifier… file path". That is false: a9d9ca4 appears at L270, a path at L220 and a log name at L118.
6. **S5 L7 stale cross-references:**
   - "weighting rule of Methods (Multiplicity)"
   - "collinearity (Results 3)" (it is now in S3 §5)
   - "run-level cross-lag deviation of Results 4" and "the budget of Results 4" (both now in S3 §6)
   - "two of its checks… in Results 4 and 6" (they are now in S3 §6 and §9)
7. **S2 L7:** "does not transfer to TR 0.72 s (Discussion)" — this is now in S3 §10.
8. **S3 L388:** "the within-run variance change that the main text's Results 7 gives as a reason for caution with the CCS global-fit values" — the main text no longer says this.
9. **S3 L388:** "changes the true sts by −0.069 against the observed DiD of −0.081". This mixes Δr₁ −0.010 with −0.0146; review Finding 14's fix was applied to the S13 caption but not here. Compare with the DMT-run change (−0.0485), or rescale.
10. **S3 L205:** "The residual DiD is positive in every variant × estimator combination" — false for the run-level rows of S12, where it equals the observed DiD and is negative. Also "reproducing the DMT-run change (+0.0041 against +0.0077)" is only about half.
11. **S1 L5:** says the sensitivity set 5–14 was "added after the primary result". The record (l. 671–677) fixed it before any windowed run; the error understates the pre-registration.
12. **S3 L155:** "The account rests on… the AR(1)-substituted estimate" contradicts L108 ("not evidence for the account").
13. **S3 L120:** "slope −1.77 nats per unit c" vs −1.74 in the main text (L55) and in S3 L118. Harmonise to −1.74.
14. **S3 L126:** the +0.756 [+0.715, +0.790] interval is not labelled as a percentile interval (the main text labels it).
15. **S3 L254:** "Fig 3c, which showed…" refers to an earlier draft's Fig 3c. Write "the former Fig 3c".
16. **S3 L317:** gives "−0.0063 per 0.001" and "−0.0028" on population-Δa bases, next to the main text's 6.1 and 3.1 on the window-level basis. Keep one basis.
17. **Fig 1.**
    - The annotation "unequal coefficients make it negative" did not carry Finding 12's fix. It turns negative only beyond an asymmetry threshold: 0.008 at (0.85, 0.25), 0.0915 at q = 0.7, none at (0.80, 0.70).
    - The leader line crosses the annotation text.
    - The atom order differs from Table 1, although L59 says "Fig 1 draws the table".
18. **Fig 4c.**
    - The "±1 SD" band around the expectation is effectively invisible: alpha-0.15 grey about 0.003 nats tall; I verified this from pixel values.
    - "Grey band" is used for two different things in the caption.
    - The legend names "partB17b" and overlaps the data.
19. **Fig 3a/c:** the generator lines are per unit pair-level a but drawn on regional-r₁ axes, a 6% scale difference. Rescale them or add a note.
20. **Fig 2.**
    - In panel (a) the contour labels collide with the orange density contours.
    - The main-text caption omits the (0.85, 0) and (0.6, 0.25) curves.
21. **L136:** "the sts level falls (1.1554, 0.1797, 0.0262, 0.0415)" is not monotone. It follows |r_τ|; say so.
22. **L136:** "DMT shifts the regional autocorrelation function" is causal wording; write "relative to placebo".
23. **L142.**
    - The ΦR "interval that excludes changes larger than 0.0112" covers the primary cell only. ts_demean gives +0.0157 [−0.0024, +0.0341], phase p 0.038; the global ts_gsr cell has phase p 0.023. Report these.
    - "CCS-sts rose… in every combination" includes an interval that spans 0; write "was positive".
24. **L146:** "flat-spectrum noise already has r₁ = 0.82" is the wrong bound for the argument. Any in-band signal has r₁ ≥ cos(2π·0.08·2) ≈ 0.54, so state that bound. In the abstract, "cannot remove" → "cannot fully remove".
25. **L89:** "found three of the four… cells proportional" / "less than proportional" is threshold language for an exploratory check, and proportionality is inferred from an interval that includes 0.
26. **L83.**
    - "in all 28 leave-one-out refits" is ambiguous; write "14 per variant".
    - "held… at the global fit": the global fit is the estimate seen before the test was written, so it is not an independent check.
27. **L85/L87.**
    - The |q| DiD (−0.0164) is given with no interval.
    - The same sentence mixes "per 0.001" and "per unit".
    - "Regional r₁ fell" → "whole-brain mean r₁".
28. **L104.**
    - "(Spearman 0.835; cortical spin p < 0.0001)": the spin p belongs to the cortical Spearman 0.771.
    - r = 0.863 includes the 16 subcortical parcels, which have no spin null; the cortex-only Pearson is 0.807.
    - "The pre-defined contrast vanishes" rests on p = 0.90 with no interval. From S3's mean ± SD the t interval is [−0.011, +0.012], which admits about half of the original −0.020.
    - The residual map's network structure (spin p 0.0009) exceeds the original's (0.056); discuss this.
    - Explain why the slope, 3.09 (cortex 2.29), is about half the family's 6.07: MMI takes the less autocorrelated member.
    - rtr's slope of 0.50 is about 9 times the family's 0.056; discuss this too.
29. **L108.**
    - "(Table 3; Fig 4)" for the early/late values, but they are not in Table 3.
    - "with two entries replaced" understates the substitution: the two lag-0 entries are also replaced by their mean (`partB4_diagnostic.py` l. 73–75).
    - The heading omits q, although the estimate uses (a_x, a_y, q).
30. **L112:** "A cross-lag change at fixed (r₁, q)" cites row (a1), which Table 3 labels "at fixed (a, q)". Table 3's "(r₁, q)" row is (a3).
31. **L114:** the conversions come from AR(1) pairs at a = 0.85, whose window-level sts is 0.72; say they are generator-dependent.
32. **L110:** the null's +0.0054 has no Monte-Carlo SE. Table 3 row 5 says "functions" where L110 says "function".
33. **L51:** "For any q" — this was checked numerically on a grid (a 0.80–0.90, q 0.05–0.70); say so. **L55:** "coupling of the same sign as q lowers sts" holds only for c ≲ 0.1.
34. **L166.**
    - "…(Huang et al., 2018), relative to placebo in this dataset, and within a placebo run with time" reads as r₁ falling within the placebo run. It rose. Rewrite: "…; in these data it fell under DMT relative to placebo and rose within the placebo run".
    - The sentence on the applicability table is unreadable (nested dashes).
35. **L162:** "Two limits on reach remain" — the Limitations list more.
36. **L212.**
    - "earlier versions" does not belong in a journal text.
    - State the symmetry assumption behind the sign-flip inversion.
    - Put the t-interval method for the slopes in Methods.
37. **L220:** "at the data's population-level coefficient" is not supported. 0.85 is the data's window-level regional mean; the run-level r₁ is 0.866 and the pair-level a 0.863; the generator's window-level a is about 0.79.
38. **L228.** Give the search engine, terms and inclusion criteria. B23 (d) shows the exposure does not depend on TR, so justify keeping the TR scoping rule.
39. **L236** "the diagnostic's branch rule" and **S10's** "residual diagnostic" use a term the main text never defines. Write "the residual's branch rule".
40. **L192:** "14 independent 60-TR windows" → "non-overlapping, separately fitted". **L204:** "gives the same τ = 1 signature" has an unclear referent.
41. **L29.**
    - "DMT, a state of intensified conscious content" → "a drug producing a state…".
    - "the closed form was derived afterwards, on the same data" → "motivated by the same data".
    - Abbreviations not expanded in the main text: TR, BOLD, HCP, BIC, HRF, MEG and PCB; also CCS (in the Introduction) and "global fit" (in the abstract).
42. **L270.**
    - "Every number… is quoted from the result files" — 37 numbers are derived; say "quoted or derived as stated".
    - "those the script wrote at the commit that carries them" — they were written at 526090d and committed at 66c6331.
43. **S1 L11 and the S2 Table:** "tier", "tier-2" and "claimed tier is 3" are undefined jargon.
44. **Cross-file values:**
    - The deconvolution r₁ is 0.848→0.783 (window) in the main text and S2, but 0.866→0.790 (run-level) in S3 L394; label both.
    - The AR(1) generator's rate appears as 3.08 (main text), 2.8 (S3 §7) and implicitly 3.4.

## TYPOS
- L116: "is about half the directed and half the symmetric part" → "is about half directed and half symmetric".
- L160: "The run-level residual of the level" → "The run-level residual".
- S17 L378: "1.072–1.192" → "1.191" (the maximum is 1.19147).
- S11 L307: 0.8176 vs 0.8174 in S18; use one value.
- L200: S (self-information) and S₄ (matrix) clash; rename the matrix R₄. S3 also overloads C, c and s.
- Figure labels "Figure 1." → "Fig 1." (PLOS).

## Five most important changes
1. Rewrite the abstract and Author summary to the evidence (M1, M2, M13):
   - Give both per-SD ratios.
   - Report the rate ratio with its interval.
   - Give the residual p range with neutral wording.
   - Scope the closed form to lag-0-only coupling.
   - Say the refutation is of MMI-sts only.
   - Soften the CCS claim.
2. Correct the residual inference:
   - Methods' description of the null (M4).
   - The "more steeply / do not reproduce" claims (M3).
   - Results 1's lagged-structure reading (M6).
   - The recommended null (M14).
3. Make the pre-registration account accurate:
   - Drop "every later computation…".
   - Add a complete prediction-outcome table and the two inference deviations.
   - Qualify the hypothesis-timing claim (M5).
4. Make the text self-contained and PLOS-compliant:
   - One notation for r₁ and ā; no B labels or paths; define symbols (M7).
   - Put the applicability table and the COBIDAS checklist into the SI, and remove the internal jargon (M8).
   - Fix figure and section order, and cite S12 (minor items 1–4).
5. Resolve the integrity items before submission:
   - Ethics disclosure and REC number (M9).
   - An honest AI-use statement (M10).
   - A completed end-to-end run with archived code (M11).
   - The deleted limitations (M12).

Files are in `/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify/review_b27/`:
- `chk_core.py`
- `phiid_cf.py`
- `lost_sentences.txt` (sentences of the 90690f4 main text absent from the new text and SI)
- `old_draft.md`
- `fig4c_crop.png`

The repository is unmodified (`git status` clean).
