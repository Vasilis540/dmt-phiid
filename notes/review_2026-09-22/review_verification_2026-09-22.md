# Verification and disposition of the review and citation pass of 22 September 2026

Planning session, 22–23 Sep 2026. Text checked: `manuscript/draft_v2.md`, S1–S5 Text and `manuscript/supplementary.md` at 0b8d1a4. Each finding of `adversarial_review.md` was checked against the committed files and the git history. Mathematical claims were recomputed with `notes/rev_phiid_fast.py`, the closed form validated against `phyid`. Every item of `citation_pass.md` marked below as spot-checked was read against the full text in the planning session's folder of PDFs. Nothing was run on the time series.

**Verdicts.**

- **confirmed**: the check reproduces the claim.
- **partly**: the direction holds, but a number, the scope or a wording does not.
- **judgement**: a matter of presentation or policy, with no fact to check.
- **declined**: not accepted, with the reason given.

**Dispositions.**

- **R16A**: a record entry or committed file in round 16, Part A.
- **B21–B24**: new computations under pre-run entries, specified in `prompt_round16.md`.
- **R16B**: the text revision, whose exact wording comes in the Stage B prompt after B21–B24 have run.

## A correction to the planning session's own earlier work

The direction argument is withdrawn. Its claim was that a coupling change applied independently of sign(q) lowers the residual and cannot raise it, so that the residual's rise "is in the direction no coupling change produces". It entered in round 14's follow-up (item B2) and was carried into Results 4 and the Discussion by 24c. Round 15 (item A.2) put it into the abstract as "a residual that a coupling change of either sign would have lowered".

The argument was a generalisation from B17's construction. That construction adds a VAR(1) cross-coefficient with the innovations held, so it moves each pair's lag-0 correlation and autocorrelation along with the coupling. At fixed (r₁, q) the response has the opposite sign; the checks are under Finding 1 below.

Two dispositions of 20 September are also revised:

- Item 13 gave the DMT run's own change as "the drug-only estimate", which is wrong (Finding 16).
- Item 21 chose BCa intervals. BCa corrects bias and skew, not the narrowness of percentile intervals at N = 14. The interval consistent with the paper's exact test is the inverted sign-flip interval (Finding 13).

## The twenty findings

**1. The residual's response to coupling depends on the generator — confirmed.** Population checks, closed form:

Population residual change at a = 0.85, averaged over q = +0.25 and −0.25. The perturbation is δ in the first row and c in the other two; each value is the same for either sign.

| construction | ±0.01 | ±0.02 | ±0.03 |
|---|---|---|---|
| δ added to both cross-lag entries at fixed (a, q) | +0.00227 | +0.00919 | +0.02110 |
| B17's construction (VAR(1), a and the innovation correlation held at their c = 0 values) | −0.00228 | −0.00919 | −0.02091 |
| the coupled family of Results 1 (a and the innovation correlation re-solved, so r₁ and q are held) | +0.00200 | +0.00806 | +0.01846 |

The shared-slow-component model was also checked: x = √λ s + √(1−λ) n_x, y = √λ s + √(1−λ) n_y, λ = 0.25, a_n = 0.84, a_s falling from 0.90 to 0.87.

- r₁ falls from 0.8550 to 0.8475.
- The aligned departure falls from +0.01125 to +0.00562.
- The population residual rises from −0.0186 to −0.0096, a change of +0.0090, or −1.2 per unit of Δr₁.

The review's W = 60 simulation reproduces Table 7's AR(1) rows. Disposition: R16A (correction entry); B23 and B24; R16B (the argument withdrawn from the abstract, Results 4, the Discussion and S3; the residual stated as unable to discriminate on these data).

**2. The "bound" uses a superseded statistic — confirmed.**

- `partB15_directed_crosslag.py` (l. 121) weights by each window's own sign(q).
- S9 Table marks those values superseded.
- `directed_crosslag_tables.md` gives the ts_demean DiD as −0.00390 [−0.00633, −0.00137], p = 0.0128.
- No result file holds a DiD of a selection-free version.

Disposition: B22, then R16B ("bounds" deleted; both variants reported).

**3. The calibration does not reproduce the data's residual–Δr₁ relation — confirmed.**

- The per-subject slope is −0.753 [−1.133, −0.374] (t) with intercept +0.0005 on ts_gsr, and −0.568 [−1.048, −0.088] on ts_demean.
- Exact sign-flip p of the residual DiD against +0.0027, +0.0049 and +0.0054: 0.108, 0.219 and 0.251.

One correction to the review: the cross-half value it quotes (−0.70) is the larger of two. `splithalf.log` gives r(res_even, r₁_odd) = −0.700 and r(res_odd, r₁_even) = −0.385, a mean of −0.54, against a ceiling of √(0.494 × 0.741) = 0.605. The relation holds across halves; the review overstated it by quoting one value.

Disposition: B21, then R16B.

**4. Failed calibration predictions are missing from the deviation list — confirmed** against the record:

- B17's pre-run entry predicted "(ii) residual ≈ −1.77 Δc … (first order)", and its outcome entry calls this "wrong in form".
- B17b's (ii) prediction was "residual negative for either sign of Δc"; it was not met (no response).
- B17b's (i) prediction missed low, and was recorded as a miss.
- The departure from B17b's rule is recorded in its outcome entry.

None of these is in the main text's deviation list. The AR(1) generator's W = 60 level is 0.715 against the data's 1.155. Disposition: R16B.

**5. The "prediction" is the same estimator on the same matrices — confirmed.**

- The per-subject regression of the sts DiD on the r₁ DiD has slope +4.263 [+3.408, +5.117] and intercept −0.0184 [−0.0390, +0.0021], p = 0.074 (ts_demean: +4.922 and +0.0031).
- Counterpoint: the slope is attenuated by measurement error in the r₁ DiD. Its full-set reliability is 0.851 (Spearman–Brown from the split-half 0.741), so the "a fifth does not scale" reading is partly attenuation, and the corrected slope is about 5.0.

Disposition: B21; R16B ("AR(1)-substituted estimate"; "no free parameter", "predicted in sign and size" and r = 0.99-as-validation deleted).

**6. "Confirmatory" misstates the history — confirmed** from git:

- 44cec4f (12 Sep 10:29) holds the hypothesis together with `results/synergy_bins_20regions_ts_gsr_global.csv` (header `git=nogit`). Its DiD by the later pre/post definition is −0.0994, negative in 12 of 14.
- 33f0b33 (13 Sep 10:40) holds the 115-region global fit ("The direction is a DECREASE") and the directional-failure rule.
- b7e4595 (13 Sep 11:36) holds the step-contrast test ("The step contrast had no test on record").
- cb1b2cf (13:15) holds the primary result.

`prespecification_summary.md` does not mention the 20-region file. Disposition: R16B ("primary", with the history in the abstract, Introduction, Results 2 and Methods; "obtains" deleted).

**7. "2 to 1 per SD" is not like-for-like — confirmed.** On `scope_map_overlay_points.npz` (subject 1, windows 1–4, 52,440 pair-windows):

- The pair-window SD is 0.0290 for r₁ and 0.1957 for |q|.
- The closed-form per-SD ratio is then 4.75.
- OLS gives +5.483 per unit r₁ and −0.472 per unit |q|; the standardised coefficients are 0.733 and −0.427.

Disposition: B22 (d), then R16B.

**8. CCS "does not follow autocorrelation" — partly.** The group-level r = −0.639 and the per-subject values −0.420 to −0.297 are in the committed files and in the text itself.

The review's "a mild filter reverses the sign" holds in one of four cells after AR(1) whitening:

| cell | CCS-sts DiD after AR(1) whitening |
|---|---|
| ts_gsr, W = 60 | −0.0057, p = 0.0065 |
| ts_gsr, global fit | +0.0134 |
| ts_demean, W = 60 | +0.0035 |
| ts_demean, global fit | +0.0204 |

After AR(p) whitening all four point estimates are negative; one is significant (ts_gsr W = 60, −0.0135, p = 0.016).

**New, not in the review:** every prewhitened CCS value (S11 Table, Results 7) was computed with phyid's mask (`partB16_prewhiten.py` l. 14, 127, 134). Methods says every CCS value in the paper is under the published definition.

Disposition: B23 (d); R16B (the pattern stated; the decomposition described as an identity that locates the change; the whitened values labelled by mask; the recommendation withdrawn).

**9. Remedies and recommendations — confirmed** from the committed logs:

- F1 analytic sts is 0.0942.
- F2-ii at 840 samples gives +0.0236 ± 0.0023, which is +29 %.
- At W = 60, F2-ii gives +7 % ± 8 % and F3-b gives −8 % ± 6 %.
- BIC chose p = 5 in 3,218 of 3,220 series.
- The whitened per-subject r is +0.495.

Disposition: R16B (the estimator preference withdrawn; the prewhitening statement narrowed to the band-limit argument; the recommended null changed to one that keeps the pair's lag-0 correlation).

**10. Regional grouping — confirmed** (`regional_partial_tables.md`).

- rtr's slope on r₁ is 3.0887 − 2.5906 = 0.498 per unit.
- Network r₁ means: SomMot 0.8493, Default 0.8484, Vis 0.8403 (the lowest).

Disposition: B22 (e), then R16B.

**11. "Most exposed dataset" is a units artefact — confirmed.** Two identical-spectrum pairs on 0.008–0.09 Hz, one with a tilt exp(−βf²), at q = 0.25:

| β | Δsts at TR 0.72 s | Δsts at TR 2 s | Δr₁ at TR 0.72 s | Δr₁ at TR 2 s |
|---|---|---|---|---|
| 100 | +0.190 | +0.165 | 0.0053 | 0.0376 |
| 200 | +0.382 | +0.335 | 0.0097 | 0.0689 |
| 400 | +0.738 | +0.658 | 0.0158 | 0.1132 |

Disposition: B23 (e), then R16B.

**12. Unequal-coefficient statements — confirmed.** Grid: mean a 0.80, 0.85 and 0.90 × q 0.05–0.70 × asymmetry 0–0.10.

- str = min(xtx, yty) to 1e-15.
- rts ≥ str.
- sts ≤ xtx + yty + rtr, with equality only at equal coefficients.
- The excess sts − (xtx + yty) starts at +rtr and crosses zero at |a_x − a_y| ≈ 0.008 at (0.85, 0.25), 0.035 at q = 0.5 and 0.09 at q = 0.7.

Disposition: R16B.

**13. Intervals at N = 14 — confirmed.** Inverted sign-flip intervals:

| quantity | inverted sign-flip interval |
|---|---|
| primary sts DiD | [−0.1317, −0.0310] |
| residual DiD | [+0.0005, +0.0226] |
| r₁ DiD | [−0.0261, −0.0037] |
| CCS W = 60 DiD | [−0.0001, +0.0088] |

r₁'s phase-randomised p (0.073) is in S3 §5. Disposition: B21, then R16B.

**14. Table 5 mixes Δr₁ — confirmed** (`sts_matched_null_F3.log`: lag 1 is 0.868 on the placebo ACF against 0.858 on the DMT-post ACF, with q fixed at 0.2). Disposition: B23 (f); R16B (Table 5 to S3 with a Δr₁ column; the caption's comparison deleted).

**15. The "directed component DiD" is not a DiD — confirmed** (`directed_crosslag_tables.md`).

- The value +0.00044, p = 0.38 is the run-level DMT − placebo difference.
- The W = 60 DiD of RMS δ_anti is +0.00631 [+0.00006, +0.01278], p = 0.0829, against B17b (i)'s +0.00641.

Disposition: B22 (c), then R16B.

**16. "Drug-only" — judgement, agreed.** The label came from the 20 September disposition 13. Disposition: R16B.

**17. Literature framing — confirmed** (citation pass C1, A2, A26). Disposition: R16B.

**18. Rates, signs and terms — confirmed** for the sign(q) point. The coupled family is invariant under (c, q) → (−c, −q). So sts at (q = −0.25, c = +0.02) equals sts at (+0.25, −0.02), 1.3023, which is +0.0435 above c = 0. The others are agreed. Disposition: R16B.

**19. Provenance — partly.**

- +0.0054 is in `notes/review_results/logs/review_v2_residual_null.log`.
- The range components (+0.0037, +0.0052, +0.0059, +0.0077) appear only in `notes/fresh_review_2026-09-17/checks/check_C1_residual_vs_null.log`. That file is committed but outside the folders the Data-availability sentence names.
- "≤ 2.1 × 10⁻¹⁴ on every saved window and bin mean" is true as worded. Those means reach 1.24 × 10⁻¹⁴; the log's 2.21 × 10⁻¹⁴ is the per-region comparison, its item 4.

Disposition: R16B.

**20. Length and novelty — judgement.** A restructuring decision for V.S. Disposition: R16B.

## The citation pass

Spot-checked against the full texts in the planning session's folder:

- **A1:** "glycolytic index", and Table 1's six values.
- **A2:** Luppi 2023, p. 12.
- **A3:** Bartlett 1935, p. 2, derives the AR(1) case only. Afyouni et al.'s Eq. 8 carries "Building on work of Bartlett (1946), Quenouille (1947)".
- **A4:** Faes 2025's "is … and is often violated".
- **A8:** recomputed from the ideal band-pass formula. r₁ runs 0.730–0.973 and the derivative ratio at |q| = 0.25 runs 22.3–145.8.
- **A9:** Honari et al., "did not have detrimental effects on the results (Fig. 4)".
- **A13:** Down et al., "many of the other atoms can occasionally take negative values".
- **A15:** Liardi et al., "may entail … Integrated Information Decomposition".
- **A16:** Luppi 2022, macaque TR "2,600 ms".
- **A17:** Luppi 2026 Reporting Summary, "TR = 1250 ms".
- **A20:** "synergistic core".
- **A21:** Luppi 2024, "Subtracting each region's redundancy rank from its synergy rank".
- **A22:** Mediano 2021, "noise correlation (c in the notation of Ref. [19])".
- **A23:** Singleton et al., "Six out of 20"; Timmermann et al., "Four out of 20".

The other items are accepted on the report's page-cited evidence. Disposition of A1–A26: R16B, with the report's proposed wordings unless the rewrite for a finding above replaces the sentence. `notes/partB5_literature_v2.md` row 1 also says "gyrification" (A1) and is corrected with a dated note.
