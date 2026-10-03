# P1 — S19 Table, Part B: where each post hoc computation is quoted, and the quoted post hoc computations that have no row

Clone: VT at f50c1d3 (clean). Line numbers are those of HEAD.

Abbreviations. MT = VT/manuscript/draft_v2.md; S1 … S5 = VT/manuscript/si/S1_Text.md … S5_Text.md; SUP = VT/manuscript/supplementary.md; CSV = VT/manuscript/main_text_numbers.csv (row numbers are file lines; line 1 is its head note, line 2 its column names); REC = VT/manuscript/analysis_record.md. Part B is SUP L1691–1707; its thirteen rows are SUP L1695–1707.

## Task 1

How a place was decided. Every hit of a search by file name, by value and through CSV was read. The kind of each mention is given in square brackets:

- [V] the place prints a value that the computation's outputs hold;
- [D] it prints a number derived directly from such values (the derivation is the text's or CSV's);
- [N] it names the computation, its script, its log or its file as the source of a statement about its result or method;
- [W] it states the computation's result in words, with no value and no name;
- [H] it names the computation in the study's history or the run inventory, or re-uses one of its parameters, and quotes no result;
- [R] it prints the same number, but the text or CSV gives another computation as its source. An [R] place is not counted as a quote; the source is stated.

"Missing from the cell" is given in three parts: (a) [V], [D] and [N] places, which the proposed cell contains; (b) [W] places; (c) [H] places. (b) and (c) are listed so that they can be added if the table is to name them; Part A names in-words places as "(in words)" (SUP L1632, L1648).

Two things hold for every row. The Supporting information list of the main text (MT L393–441) names several of the computations as contents of the supporting items (S2 Text, S3 Text, S7, S8 and S16 Tables); it is a list of contents, is not one of the places the task names, and is left out below. S17 Table is B21's table of every quantity with a saved per-subject vector: for a post hoc computation whose vectors it holds it prints that computation's mean, committed p and committed percentile interval beside B21's intervals, and its source line names the pickles (SUP L400). It is listed where it does so; Part A's cells name S17 Table only for B21 (a) and B19 (d) (SUP L1646, L1638), not for the other computations whose rows it holds, so whether Part B's cells should name it is a matter of the table's convention.

### The review computations of 14 September 2026 (SUP L1695)

Cell now: "Results 2, 4, 6 and 7; S3 Text §6 (its residual table); Methods, Estimator; S2 Text; S3 Text §4–6".

Outputs identified. VT/notes/review_computations_2026-09-14.md (section 0 at its L20, 1 at L24, 2 at L93, 3 at L145, 4 at L278, 5 at L341, 6 at L376; its scripts at L10–16: rev_inference.py, rev_series.py, rev_run.py, rev_deconv.py, rev_sts_matched_null.py, rev_extra.py, rev_tables.py, rev_assemble.py). VT/notes/review_results/inference_rows_raw.csv and .pkl (84 rows; line 14: "autocorr ts_gsr W60,primary", did −0.014645, did_p 0.0106, n_neg 12, phase_p 0.0729, placebo_share 0.3399; line 8: "PhiR ts_gsr W60,primary", pre_dmt 0.0961, did +0.00066, did_p 0.8971) and inference_rows_deconv.csv and .pkl (72 rows; line 2: autocorr_deconv pre_dmt 0.7833; line 8: sts_deconv pre_dmt 0.8315, did −0.07819, did_p 0.0013). VT/notes/review_results/logs/rev_extra.log (line 3 "Pearson r = +0.953 … Spearman rho = +0.903"; line 13 "+0.977"; line 18 "+0.938"; line 25 "r1 = 0.8176"; line 26 "0.8661 … 0.992"; line 32 "DMT pre 1.277 post 0.889 | PCB pre 0.936 post 1.062"; lines 40, 42, 43 "+0.365", "+0.492 … +0.766", "+0.543 … +0.726"), rev_run_raw.log, rev_run_deconv.log, rev_deconv_*.log.

Quantity by quantity. Section 5 (the sts-matched null) and the spectral centroid (rev_extra.log line 27) have rows of their own and are treated there. The pooled autocorrelation function, which the row's first cell lists, is printed in section 5 and in VT/notes/review_results/logs/sts_matched_null_F3.log line 3 ("placebo lags 1-6 [ 0.868 0.539 0.172 -0.085 -0.174 -0.145]") and is the target at line 2 of the null's log; it is counted in this row because the first cell lists it. Section 0 is the validation of the review's inference engine against the pipeline ("The sts rows in the tables below are therefore the paper's own numbers", review_computations L22): a value that the pipeline's file also holds (the sts DiD, its phase-randomised p, the sts level) is not counted as a quote of the review, even where CSV locates it in the review's file. The per-subject vectors of the two pickles are re-read by B21 (VT/notes/review_results/partB/inference_revision.csv lines 633, 639, 675 and 153 name inference_rows_raw.pkl and inference_rows_deconv.pkl), which adds the inverted interval: a place that prints the r₁ DiD, the ΦR DiD or a deconvolved DiD with B21's interval prints the review's quantity and is counted as [V].

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Abstract | MT L15 | [W] "whole-brain MMI-sts fell relative to placebo (…) with r₁, near a generator's −0.094 for that fall": the fall of r₁, no value | no |
| Author summary | MT L19 | [W] "the signals' autocorrelation fell"; "(synergy rose in one volunteer, autocorrelation in two)": the count 12 of 14, in words | no |
| Introduction | MT L29 | [W] "went with the lag-1 autocorrelation contrast" | no |
| Results 2 | MT L106 | [V] "Whole-brain r₁ (a post hoc quantity) changed relative to placebo by −0.0146 [−0.0261, −0.0037] (p = 0.0106, negative in 12 of 14; −0.0216 without global signal regression)"; "0.073"; "carry 0.34 and 0.40 of the two DiDs". CSV L525–531 (B21's rows of the review's pickle, inference_revision.csv lines 639 and 675), L533, L546–547 (inference_rows_raw.csv lines 14 and 2) | yes |
| Results 2 | MT L108 | [R] "r = 0.953 [0.854, 0.985]": CSV L554–556 give B21 (d) (inference_revision_tables.md line 253) | yes |
| Table 2 (caption) | MT L89 | [H] "The three rows marked r₁ give the two gaps and the baseline-adjusted contrast of whole-brain lag-1 autocorrelation r₁ (dimensionless), whose DiD is in the text": a pointer; the rows' values are B27's | no |
| Table 2 (body) | MT L96 | [R] phase p 0.0020 and 0.0010: CSV L439 and L446 locate them in inference_rows_raw.csv lines 2 and 38, the engine's reproduction of the pipeline's value (S1 L9 gives 0.0020 with `results/primary_b_ts_gsr_win60.csv`) | no |
| Fig 3 (caption) | MT L110 | [V] "the two DiDs differ by 6 % in the data (−0.0155 against −0.0146)" (CSV L608). [R] "r = +0.953, Fisher-z 95 % interval [+0.854, +0.985]" (CSV L617–620: B21 (d)) | no |
| Results 4 | MT L120, L124, L142 | no value of these computations and no name: the r₁ DiD is only the regressor of the slope and the denominator of "−0.79 per unit of whole-brain r₁" (L124), which are B21 (c)'s and the last row's | yes |
| Table 3 (caption) | MT L126 | [V] "(in the data's group means the two DiDs are −0.0146 and −0.0155)" (CSV L814) | no |
| Results 5 | MT L146 | [R] "0.848 at τ = 1" (CSV L928: lag_tables.md, B3) | no |
| Fig 6 (caption) | MT L148 | [R] "(−0.0146, −0.0468, −0.0681, −0.0108)" and "+0.953" (CSV L972 and L968: lag_tables.md, B3) | no |
| Results 6 | MT L152 | [R] "MMI-sts +0.98" (CSV L999: ccs_pub_tables.md, B2) | yes |
| Results 6 | MT L154 | [V] "changed by +0.0007 [−0.0093, +0.0112] (p = 0.90)"; "(0.096)"; "0.085 or more"; "(0.019–0.038)" (CSV L1016–1024) | yes |
| Results 7 | MT L158 | [R] "(flat in-band noise has 0.82)" (CSV L1039: whitened_spectrum_tables.md, B16b) | yes |
| Results 7 | MT L171 | [V] "lowered r₁ from 0.848 to 0.783 and sts from 1.155 to 0.832 and left the contrast in place (−0.0782, p = 0.0013; post hoc" (CSV L1121–1126) | yes |
| Table 4 (caption, body) | MT L160, L164 | [R] "99.2 %" (CSV L1072: B16b); the raw row's "0.848" and "+0.953" (CSV L1077: B16b; L1084: B21 (d)) | no |
| Discussion, What the finding is and is not | MT L183 | [W] "On this dataset MMI-sts fell with r₁ relative to placebo" | no |
| Discussion, The fall of r₁ under DMT | MT L187 | [W] "Why r₁ fell is not identified here, and the fall is not an artefact" | no |
| Limitations | MT L201 | [W] "no deconvolution in the primary analysis"; "Why r₁ fell (…) is not identified" | no |
| Methods, Estimator | MT L217 | [D] "is about 18 in a 60-TR window over six lags of the pooled placebo function (S3 Text)" (CSV L1245: 60 / 3.264, from the placebo function at line 2 of the null's log) | yes |
| Methods, Inference | MT L237 | [R] "(0.61 for the whole-brain r₁ DiD)" (CSV L1302: B27 (c)) | no |
| Methods, The AR(1)-substituted estimate and its calibration | MT L245 | [R] "(1.155)": CSV L1322 locates the sts level in inference_rows_raw.csv line 2; it is the pipeline's value (Table 2) | no |
| Methods, Remedies | MT L249 | [N] "HRF deconvolution used rsHRF 1.7.0 (Wu et al., 2013, 2021; S2 Text)." | no |
| Methods, Pre-registration and deviations | MT L261 | [H] "its plans were written after that review's computations had characterised the phenomenon" | no |
| Data and code availability | MT L267 | [H] "The HRF-deconvolution items need the sandbox described in `notes/rev_deconv.py` and are skipped unless it is present (S2 Text)." | no |
| S1 Text | S1 L5 | [N] "the early and late sets (6–9, 10–14) and two trend corrections were added after the primary result"; "the deconvolution (S2 Text) used rsHRF 1.7.0" | no |
| S1 Text | S1 L21 | [N] "An adversarial review on 14 September 2026, with its own computations, established that the decrease was carried by the self-prediction atoms" | no |
| S2 Text | S2 L3, L5, L7, L9 | [N, V] the file and its section 3 named (L3, L7); "DiD +0.0007 [−0.0093, +0.0112], sign-flip p = 0.8971" (L5); "0.866 → 0.790" (L7); "+0.0178 [+0.0051, +0.0307], p = 0.0099" (L9) | yes |
| S3 Text §4 | S3 L128 | [V] "against a measured 0.866"; "the pooled placebo autocorrelation function (0.868, 0.539, 0.172, −0.085, −0.174, −0.145)" | yes |
| S3 Text §4 | S3 L161 | [V, N] "DiD −0.0146 [−0.0261, −0.0037], sign-flip p = 0.0106, negative in 12 of 14, phase-randomised p = 0.0729"; "(`notes/review_results/inference_rows_raw.csv`)" | yes |
| S3 Text §5 | S3 L165 | [V, N] "0.977 and 0.938 (the review computations of 14 September 2026, `notes/review_computations_2026-09-14.md`, section 1"; "(−0.0213, p = 0.0006) than the late (−0.0093, p = 0.1615)" | yes |
| S3 Text §5 | S3 L197–200 | [V] the rows "autocorr ts_gsr W60 [primary]" (−0.0146, 0.0106, committed interval [−0.0251, −0.0052]) and "PhiR ts_gsr W60 [primary]" (+0.0007, 0.8971, [−0.0078, +0.0100]) | yes |
| S3 Text §5 | S3 L223 | [V, N] "(window variance / run variance 1.28 in the pre-injection windows against 0.89 after; review computations of 14 September, section 6)" | yes |
| S3 Text §6 | S3 L307 | [V, N] "(window variance / run variance 1.28 → 0.89 on DMT, 0.94 → 1.06 on placebo; review computations of 14 September, section 6)" | yes |
| S3 Text §6, its residual table | S3 L325–326 | [V] "−0.01465 [−0.02609, −0.00370]; pair r₁ −0.0155"; "−0.02157 [−0.03314, −0.01020]" | yes |
| S3 Text §6 | S3 L382 | [V] "is fitted to the pooled placebo autocorrelation function" (the function as the null's target) | yes |
| S3 Text §7 | S3 L462 | [V] "and the data's by −0.0155 (whole-brain r₁ −0.0146)" | no |
| S3 Text §8 | S3 L507 | [N] "in-band share = periodogram power at 0.01 ≤ f ≤ 0.08 Hz over the total, as `rev_extra.py` (c) computes it" | no |
| S3 Text §8 | S3 L504, L544 | [R] "(raw series −0.0146)"; "against −0.0146 for the raw series": lines of B16's and B16c's tables (prewhiten_fixed_tables.md line 28) | no |
| S3 Text §9 | S3 L550 | [V, N] "at +0.37 per run on average (review computations of 14 September, section 1)"; "+0.77 and +0.73 on the group-mean series (review computations of 14 September, section 6)" | no |
| S3 Text §10 | S3 L556 | [V] "→ 0.82 against a measured 0.866"; "run-level r₁ 0.866 → 0.790 on ts_gsr"; "the sts contrast unchanged, −0.0782 against −0.0809 at W = 60; S2 Text" | no |
| S4 Text (P6, S2, S8, R1, R5) | S4 L39, L49, L55, L62, L66 | [N] "HRF deconvolution (rsHRF 1.7.0) was applied here only as a post hoc exploration"; "the effective sample size per window (about 18)"; "Results 6 (ΦR null)" | no |
| S5 Text §1 | S5 L7 | [N] "an adversarial review with its own computations (the lag-1 autocorrelation contrast …, ΦR, the trend corrections, …) established that the decrease was carried by the self-prediction atoms" | no |
| S5 Text §2 | S5 L15 | [H] "186 rows are from the 14 September review's files (raw, deconvolved, W = 30)" | no |
| S5 Text §4 | S5 L25 | [H] the run inventory names `notes/review_results/inference_rows_deconv.csv` and `notes/review_results/inference_rows_raw.csv` | no |
| S11 Table | SUP L309 | [V] "for the pooled placebo function (ρ₁ = 0.868, ρ₂ = 0.539)" | no |
| S11 Table | SUP L331 | [V, N] "the raw in-band share is 0.992, ideal flat-spectrum noise on the band at TR 2 s has r₁ = 0.8176 on the 840-sample frequency grid (`rev_extra.log`;" | no |
| S13 Table | SUP L353, L354, L361 | [V] "the whole-brain r₁ change (−0.0146)"; "−0.0146 (whole-brain r₁)" | no |
| S14 Table | SUP L371 | [R] its lag-1 row (−0.0146 [−0.0261, −0.0037], 0.0106; +0.953) is B3's (source line SUP L367: lag_tables.md, inference_rows_lag.csv) | no |
| S15 Table | SUP L378, L382–385 | [N, V] "Source: … `inference_rows_raw.csv`"; the ΦR column, first row "+0.0007 [−0.0093, +0.0112], 0.8971, 0.8372, 8" | no |
| S17 Table | SUP L400; rows 145–216 (L550–621) and 625–708 (L1030–1113) | [N, V] "the 738 rows of the eight `notes/review_results/inference_rows_*.pkl`"; row 637 (L1042): autocorr ts_gsr W60, primary, did, −0.01465, 0.0106, committed interval [−0.02507, −0.00516] | no |
| S18 Table (B28) | SUP L1590 | [H] "its inputs are the committed per-subject whole-brain r₁ DiDs, which set each simulated subject's change" | no |
| S19 Table, Part A | SUP L1616, L1637 | [H] the row "The regional ΦR check after deconvolution"; B19 (c)'s recorded prediction "Below 0.953 and near the ceiling 0.729" | no |
| S20 Table (Table B, items 2 and 4) | SUP L1734, L1738 | [V] "→ 0.82, against a measured 0.866"; "from 0.866 to 0.790 (ts_gsr)"; "(0.924 vs 0.968 at the global fit)"; "(−0.0220 vs −0.0146)" | no |

Missing from the cell:
(a) by value or by name: Fig 3 (caption: the r₁ DiD); Table 3 (caption: the r₁ DiD); Methods, Remedies (the deconvolution's software); S1 Text; S3 Text §7, §8, §9 and §10; S4 Text (P6, S2, S8, R1, R5); S5 Text §1; S11, S13, S15, S17 and S20 Tables.
(b) in words: Abstract; Author summary; Introduction; Discussion (What the finding is and is not; The fall of r₁ under DMT); Limitations.
(c) history, inventory, inputs: Table 2 (caption, a pointer to the text); Methods, Pre-registration and deviations; Data and code availability (`notes/rev_deconv.py`); S5 Text §2 and §4; S18 Table (B28's inputs); S19 Table, Part A (the regional ΦR check; B19 (c)'s recorded 0.953).

Named in the cell but not quoting it: Results 4. Its three paragraphs print no value of these computations and name none of them; the r₁ DiD's value is in Table 3's caption (MT L126), a place of its own. If use as a regressor or denominator is to count, Results 4 stays; otherwise "Table 3 (caption)" takes its place.

Proposed complete cell: Results 2 (the r₁ contrast, its phase-randomised p and the placebo run's share), 6 (ΦR) and 7 (the deconvolution); Fig 3 and Table 3 (captions: the r₁ DiD); Methods, Estimator (the pooled autocorrelation function) and Remedies (the deconvolution); S1 Text; S2 Text; S3 Text §4–10 (§6 with its residual table); S4 Text (P6, S2, S8, R1, R5); S5 Text §1; S11, S13, S15, S17 and S20 Tables. With (b): "Abstract, Author summary, Introduction, Discussion and Limitations (in words)" after Results.

### The finite-sample null of the residual (SUP L1696)

Cell now: "Results 1 and 4; S3 Text §6 (its residual table, row 5); Methods, The AR(1)-substituted estimate and its calibration; S3 Text §6; S9 and S12 Tables" (S3 Text §6 is named twice).

Outputs identified. VT/notes/review_v2_residual_null.py; VT/notes/review_results/logs/review_v2_residual_null.log (line 2: the filter fitted to the placebo function, "lags 1-6 [ 0.872 0.549 0.179 -0.091 -0.196 -0.168]"; lines 6–8: "(-8.51 %)", "(-3.10 %)", "(-0.34 %)" at W = 30, 60, 840; lines 11–14: the four cells, window a 0.8625, 0.8532, 0.8602, 0.8655, residual −0.0353, −0.0313, −0.0350, −0.0364, obs sts 1.1835 in the first; line 16: "null residual change: DMT +0.0041, PCB -0.0013, DiD +0.0054"); VT/notes/adversarial_review_draft_v2_2026-09-15.md, Appendix B. Its generator was simulated again by later computations that have pre-run entries (the entry of 16 September 2026, 10:23 UTC: VT/notes/review_results/partB/crosslag_deviation_tables.md L59, "B. The finite-sample null of notes/review_v2_residual_null.py (addition of 16 Sep 2026)"; the budget's null, partB13; B15; B17b): a place that prints those computations' values names the null and prints none of its own values.

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Abstract | MT L15 | [R] "0.006–0.009 above simulated pure autocorrelation changes"; "(p = 0.11–0.25)": the ends 0.006 and 0.25 are B27 (c)'s and B21 (b)'s values against the null's +0.0054 (CSV L31, L35) | no |
| Results 1 | MT L59 | [W] "a stationary finite-sample null, in which those values hold in population, reproduces most of its level (S3 Text §6)" | yes |
| Fig 3 (caption) | MT L110 | [V] "of the finite-sample null (−0.37: +0.0054 / −0.0146; Methods)" (CSV L641: log line 16) | no |
| Results 4 | MT L124 | [V] "on a finite-sample null solved to the data's pair r₁ in each run and period it is +0.0054 (Methods)" (CSV L780); [D] "−0.37" (CSV L792) | yes |
| Fig 5 (caption) | MT L122 | [V] "the two other expectations, +0.0049 and +0.0054" (CSV L771) | no |
| Table 3 (caption, body) | MT L126, L131–132 | [D] "the three group-level rates of the text (−0.18, −0.39 and −0.37)"; "contain −0.18, −0.39 and −0.37" (CSV L823, L860, L872: +0.0054 / −0.0146) | no |
| Discussion, What the finding is and is not | MT L183 | [R] "the 0.003–0.005 of a simulated pure autocorrelation change (excesses of 0.006–0.009)" (CSV L1156: calibration_tables.md, with the note "the finite-sample null gives +0.0054, NL line 16"; L1157: B27 (c)) | no |
| Methods, The AR(1)-substituted estimate and its calibration | MT L245 | [V] "A third expectation comes from a finite-sample null"; "its +0.0054 is from a single simulation, without a replicate SD (S3 Text)" (CSV L1329) | yes |
| S3 Text §5 | S3 L258 | [D, V] "11 contain −0.37 (the finite-sample null's)"; "(+0.0027, +0.0049, +0.0054)" | no |
| S3 Text §6 | S3 L307 | [V, N] "a residual DiD of +0.0054 against the observed +0.0115"; "−8.5 %, −3.1 % and −0.34 % at W = 30, 60 and 840 … (`notes/review_results/logs/review_v2_residual_null.log`)" | yes |
| S3 Text §6 | S3 L313, L315 | [N] "the finite-sample null described above was simulated as 840-TR runs per run type" (the budget's null; its values are partB13's) | yes |
| S3 Text §6, its residual table | S3 L321, L329 | [V] "Row 5: the finite-sample null, a single simulation (Methods)"; row "finite-sample null with the data's autocorrelation function", +0.0054, 0, −0.0146 | yes |
| S3 Text §6 | S3 L376, L382, L384 | [N, V] "(0) symmetric filter null, as review_v2_residual_null.py"; "the finite-sample null of the residual (`notes/review_v2_residual_null.py`)"; "(lags 1–6 fitted 0.872, 0.549, 0.179, −0.091, −0.196, −0.168)"; "−1.1 % against the null's −0.34 %" | yes |
| S3 Text §7 | S3 L436, L462 | [N, V] "on the generator of `review_v2_residual_null.py`"; "below the AR(1) generator's +0.0049 and the finite-sample null's +0.0054" | no |
| S4 Text (S9) | S4 L56 | [N] "the finite-sample null (a review computation; S3 Text §6)" | no |
| S5 Text §1 | S5 L7 | [H] "The finite-sample null of the residual is that review's own computation, run before any record entry and with no recorded rule" | no |
| S9 Table | SUP L155, L185 | [N] the null named in the table's title and in "the finite-sample null with the same weight, homogeneous filter, +0.00348 at W = 60"; the values are those of the entry of 16 September 2026 and of partB13, not of the null's own log | yes |
| S12 Table | SUP L345 | [V] "+0.0054 (finite-sample null with the data's autocorrelation function; p = 0.251)" | yes |
| S13 Table | SUP L363 | [V, N] "−0.37 under the finite-sample null (+0.0054 for its own −0.0146; `notes/review_results/logs/review_v2_residual_null.log`)" | no |
| S18 Table | SUP L1527 | [H] "filter edges 0.0064–0.080 Hz" (the null's fitted band, in the description of B17b's generator) | no |
| S19 Table, Part A | SUP L1625, L1641, L1642 | [H] "The W = 60 statistic and the finite-sample null (16 Sep 2026, 10:23 UTC)"; "near the null's 1.18"; "near the data's own null, +0.004 to +0.008" (recorded rules and predictions) | no |

Missing from the cell:
(a) by value or by name: Fig 3 (caption); Fig 5 (caption); Table 3 (caption and body: the rate −0.37); S3 Text §5 and §7; S4 Text (S9); S13 Table.
(b) through other computations' values: Abstract and Discussion (the lower end of the excesses and the largest p, which B27 (c) and B21 (b) computed against the null's +0.0054).
(c) history, re-use: S5 Text §1; S18 Table; S19 Table, Part A.

Named in the cell but not quoting it: none. S9 Table names the null and prints values of later simulations of its generator, none from the null's own log; "S3 Text §6" stands twice in the cell.

Proposed complete cell: Results 1 (in words) and 4; Figs 3 and 5 (captions); Table 3 (the rate −0.37); Methods, The AR(1)-substituted estimate and its calibration; S3 Text §5, §6 (with its residual table, row 5) and §7; S4 Text (S9); S9 (by name), S12 and S13 Tables.

### The sts-matched null (SUP L1697)

Cell now: "Results 7; S3 Text §9; S16 Table".

Outputs identified. VT/notes/rev_sts_matched_null.py; VT/notes/review_results/logs/sts_matched_null_F1.log (lines 6–8: −6 %, −9 %, +2 %; lines 13–15: +33 %, +16 %, +1 %; line 4: analytic sts 0.0942), _F2.log (lines 8–10: +6 %, +7 %, +29 %), _F3.log (line 3: the pooled functions, 0.868 and 0.858 at lag 1; lines 16–18: −1 %, −8 %, +2 %; lines 20 and 22: "true difference -0.0688", "estimated difference -0.0557"); section 5 of VT/notes/review_computations_2026-09-14.md (L341).

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Results 7 | MT L173 | [V] "+7 % ± 8 % and −8 % ± 6 % of the observed contrast at W = 60 on the two data-like matched pairs"; "+29 % and +2 % ± 2 % at the 840-sample fit" (CSV L1128–1136: F2 log lines 9–10, F3 log lines 17–18) | yes |
| Limitations | MT L201 | [W] "the substitution does not remove the windowed estimator's manufacture" | no |
| Methods, Remedies | MT L249 | [N] "Manufacture was assessed on four matched pairs of simulated conditions (S16 Table)." | no |
| S3 Text §6 | S3 L305 | [N, V] "The sts-matched null (a post hoc computation; `notes/rev_sts_matched_null.py`)"; "over 4,000 independent windows at W = 30, 60 and 840" | no |
| S3 Text §9 | S3 L550 | [V, N] "−9 % (F1-i), +16 % (F1-ii), +7 % ± 8 % (F2-ii) and −8 % ± 6 % (F3-b)"; "changes the true sts by −0.069"; "the W = 60 estimator returns −0.056 of it" | yes |
| S4 Text (S9) | S4 L56 | [N] "the sts-matched null (S3 Text §6; S16 Table)" | no |
| S5 Text §1 | S5 L7 | [H] named in the list of the review's own computations ("the trend corrections, the sts-matched null, and …") | no |
| S13 Table | SUP L349, L355–356 | [N, V] "(0.868 → 0.858 at q = 0.2; `sts_matched_null_F3.log`)"; rows "true change of sts under the whole autocorrelation-function change at fixed q", −0.069, and "what the W = 60 estimator returns of it", −0.056 | no |
| S16 Table | SUP L389–396 | [V, N] the four matched pairs at W = 30, 60 and 840; "(`notes/rev_sts_matched_null.py`; review computations of 14 September, section 5; a post hoc computation)" | yes |

Missing from the cell:
(a) by value or by name: Methods, Remedies; S3 Text §6; S4 Text (S9); S13 Table.
(b) in words: Limitations.
(c) history: S5 Text §1.

Named in the cell but not quoting it: none.

Proposed complete cell: Results 7; Methods, Remedies; S3 Text §6 (the families and the four matched pairs) and §9; S4 Text (S9); S13 Table (the Gaussian-process rows) and S16 Table.

### The spectral centroid (SUP L1698)

Cell now: "Results 5; S3 Text §9".

Outputs identified. VT/notes/rev_extra.py; VT/notes/review_results/logs/rev_extra.log line 27 ("in-band spectral centroid (Hz): DMT pre 0.0369 post 0.0383 | PCB pre 0.0374 post 0.0364 | DiD +0.00231 Hz [+0.00060, +0.00395] sign-flip p = 0.0217, 12/14 positive") and line 29 (ts_demean); section 1 of the review computations file.

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Results 5 | MT L146 | [V] "(the in-band spectral centroid rises by +0.0023 Hz, p = 0.022; post hoc)" (CSV L951–952: rev_extra.log line 27) | yes |
| Discussion, The fall of r₁ under DMT | MT L187 | [W] "here the regional autocorrelation function decays faster under DMT (Results 5)": rests on the lag contrasts as well | no |
| S3 Text §4 | S3 L128 | [V, N] "the in-band spectral centroid of the released series before injection is 0.0369 Hz on the DMT run and 0.0374 Hz on the placebo run … (`notes/review_results/logs/rev_extra.log`)" | no |
| S3 Text §9 | S3 L552 | [V, N] "a post hoc computation (`rev_extra.py`) — rises accordingly (+0.0023 Hz [+0.0006, +0.0040], p = 0.022, 12 of 14 on `ts_gsr`" | yes |
| S4 Text (R1) | S4 L62 | [N] "the in-band spectral centroid of Results 5 (a point value with p; its interval, in S3 Text, a subject-bootstrap percentile interval)" | no |
| S14 Table (source line) | SUP L367 | [N] "the overlap of the autocorrelation contrasts' intervals and the spectral centroid are in S3 Text, section 9" (a pointer) | no |
| S17 Table (note) | SUP L402 | [N] "the deconvolved ΦR values of S2 Text and the spectral centroid of S3 Text, section 9" (among the quantities that keep a percentile interval) | no |

Missing from the cell:
(a) by value or by name: S3 Text §4 (the pre-injection centroids); S4 Text (R1); S14 Table (a pointer in its source line); S17 Table (its note).
(b) in words: Discussion (The fall of r₁ under DMT).
(c) none.

Named in the cell but not quoting it: none.

Proposed complete cell: Results 5; S3 Text §4 (the pre-injection centroids) and §9; S4 Text (R1); S14 and S17 Tables (by name, in their notes).

### Global functional connectivity per bin (SUP L1699)

Cell now: "S3 Text §4 (the signed mean correlation on ts_demean); S7 Table".

Outputs identified. VT/scripts/09_global_fc_per_bin.py; VT/results/global_fc_did_ts_demean.csv and global_fc_did_ts_gsr.csv, global_fc_bins_115regions-all_<variant>.csv and .npy, VT/results/run_09_<variant>.log; REC L1928 ("Global functional connectivity per bin (`09_global_fc_per_bin.py`, 13 Sep 2026)", "run at 66b570e-dirty").

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| S1 Text | S1 L17 | [N] "(main text, Discussion; S6 Table; global functional connectivity per bin set in S7 Table)" (a pointer) | no |
| S3 Text §4 | S3 L161 | [V, N] "rose from 0.190 to 0.233 on DMT (DiD +0.0526 [+0.0008, +0.1041], p = 0.0470"; "`results/global_fc_did_ts_demean.csv`, a computation with no pre-specification entry" | yes |
| S5 Text §4 | S5 L25 | [H] its four files and two logs among those with `-dirty` headers; "(written by `scripts/09_global_fc_per_bin.py` and `scripts/10_subject_alignment_check.py`" | no |
| S7 Table | SUP L130–140 | [V, N] "Source: `results/global_fc_did_<variant>.csv` (git 66b570e-dirty)"; five rows, e.g. "+0.0526 [+0.0008, +0.1041], 0.0470, 4/10" | yes |
| S17 Table | SUP rows 917–928 (L1322–1333) | [V] "S7 Table: mean_r DiD ts_demean primary_bins11-28", scripts/09, +0.05264, 0.0470, committed interval [+0.00734, +0.09762] (row 923) | no |

Missing from the cell:
(a) by value or by name: S1 Text (a pointer to S7 Table); S17 Table (rows 917–928).
(b) none.
(c) inventory: S5 Text §4.

Named in the cell but not quoting it: none.

Proposed complete cell: S1 Text (S7 Table cited); S3 Text §4 (the signed mean correlation on ts_demean); S7 Table; S17 Table (its rows).

### The coupled family (SUP L1700)

Cell now: "Results 1; Fig 1c; S3 Text §3; S18 Table".

Outputs identified. VT/notes/partB8_coupling_map.py; VT/notes/review_results/partB/coupling_map_tables.md (lines 8–14: sts 1.9216, 1.4111, 1.3023, 1.2588, 1.2315, 1.2155, 1.2569 at c = −0.10 … +0.10; rtr 0.0275 and 0.0191 and the excess +0.0045 and +0.0586 at ±0.02; line 16: "first derivative in c at 0: -1.7711 nats per unit c; second derivative: +40.318"); REC L2429 (pre-run entry of 15 September 2026, 07:30 UTC), L2566 ("B8 outcome (analytic)"), L2572–2573 ("departs from a_y q by ≈ +0.94 c"), L2621 ("B8 was entered with no prediction").

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Abstract | MT L15 | [W] "neither is lagged coupling, which can move it either way" | no |
| Results 1 | MT L57 | [V] "coupling c of the same sign as q lowers sts at each value computed up to +0.10, most at +0.05, and coupling of the opposite sign raises it" (CSV L150–153: coupling_map_tables.md lines 4, 12–14). [R] "−1.74" (CSV L154: exchange_rates_tables.md, B19); "+0.009" (CSV L157: B23 (a3)) | yes |
| Fig 1 (caption, panel c) | MT L55 | [V] "sts is 1.2588 at c = 0, 1.2315 at +0.02, 1.2155 at +0.05 and 1.2569 at +0.10, and 1.3023 and 1.4111 at −0.02 and −0.05" (CSV L138–149) | yes |
| Discussion, What the finding is and is not | MT L181 | [W] "lagged interaction, the thing the atom is meant to capture, can move it either way" | no |
| Limitations | MT L201 | [W] "the coupled family is symmetric" | no |
| S3 Text §3 | S3 L116, L120, L122 | [N, V] "partB8's matched view, the coupling map's convention"; "is −1.7711 per unit c"; "(`notes/partB8_coupling_map.py`, `notes/review_results/partB/coupling_map_tables.md`)"; "sts = 1.2315 and 1.3023 at c = +0.02 and −0.02" | yes |
| S3 Text §6 | S3 L315 | [H] "is the coupled family at coefficient 0.83, c = 0.03, q_ε = 0.093 (section 3)": the family named; the values are the population check of partB12 (S3 L122) | no |
| S4 Text (S9) | S4 L56 | [N] "the coupled family (S3 Text §3); each with its provenance" | no |
| S5 Text §1 | S5 L7 | [H] "the coupled family, entered in the same pre-run entry with no prediction" | no |
| S18 Table | SUP L1363–1370, L1408–1415 | [R] rows "(a3) coupled family, r₁ and q held": B23 (a3)'s residual changes (e.g. +0.00912 at c = +0.02); no value of coupling_map_tables.md (1.2315, 1.3023, 1.2155, 1.4111, −1.7711 are not in S18 Table) and no file of B8 | yes |
| S19 Table, Part A | SUP L1632 | [H] B17 (ii)'s recorded prediction "Residual ≈ −1.77 Δc at the global fit (first order), smaller at W = 60; δ_sym ≈ 0.94 Δc" (B8's slope and departure; REC L4774–4775) | no |

Missing from the cell:
(a) by value or by name: S4 Text (S9).
(b) in words: Abstract; Discussion (What the finding is and is not); Limitations.
(c) history, re-use: S3 Text §6 (the family named in the budget's worked example); S5 Text §1; S19 Table, Part A (B17 (ii)'s recorded prediction).

Named in the cell but not quoting it: S18 Table. Its "(a3) coupled family" rows are B23 (a3)'s (Part A, SUP L1655, gives "Results 1; S18 Table; S3 Text §6 (its residual table)" for B23 (a3)); the "+0.009 … S18 Table" of Results 1 is that computation's, not B8's.

Proposed complete cell: Results 1; Fig 1 (caption, panel c); S3 Text §3; S4 Text (S9). With (b): "Abstract, Discussion and Limitations (in words)". If S18 Table is kept, "(the family's construction in B23 (a3), whose values those rows are)" says what it holds.

### The leave-two-out on the sts / autocorrelation collinearity (SUP L1701)

Cell now: "S3 Text §5".

Outputs identified. VT/notes/partB9_leave_two_out.py; VT/notes/review_results/partB/leave_two_out.log (line 4: "leave-two-out (91 refits, N = 12 each): Pearson r range +0.846 to +0.973, median +0.954; minimum +0.846 without subjects 8 and 14") and leave_two_out.csv; REC L2661 (pre-run entry, 15 September 2026, 11:09 UTC) and L2679 (outcome).

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Table 3 (caption, body) | MT L126, L132 | [R] "the 91 leave-two-out sets"; "data, any two subjects left out": B27 (c)'s refits of the residual's slope, another computation | no |
| S3 Text §5 | S3 L165 | [V, N] "(91 refits) gives r = 0.846 to 0.973 on `ts_gsr`, median 0.954, the minimum without subjects 8 and 14 … (`notes/review_results/partB/leave_two_out.log`)" | yes |
| S3 Text §5 | S3 L258 | [R] "Two left out (91 refits)"; "r −0.930 to −0.465 and +0.846 to +0.973": B27 (c)'s recomputation in its table (c) | yes |
| S4 Text (R3) | S4 L64 | [N] "leave-two-out (S3 Text §5)" | no |
| S5 Text §1 | S5 L7 | [H] "a leave-two-out on the sts / autocorrelation collinearity (S3 Text §5), entered in the record with no prediction before it was run" | no |

Missing from the cell:
(a) by name: S4 Text (R3).
(b) none.
(c) history: S5 Text §1.

Named in the cell but not quoting it: none.

Proposed complete cell: S3 Text §5; S4 Text (R3).

### The checks of the review of 17 September 2026 (SUP L1702)

Cell now: "S3 Text §6 (the run-level residual against the null, p = 0.0001) and §9 (the variance ratio partialled out of the group-mean relation, r = +0.95)".

Outputs identified. VT/notes/fresh_review_2026-09-17/checks/: check_A1_atoms_family.log (line 66: "191 x 191 = 36481 points; points with |d/dq| > |d/dr1|: 0"; lines 63 and 65: ratio minima 6.553 and 1.889), check_A2_ratio_range.log, check_B1_did_recompute.log, check_C1_residual_vs_null.log (line 23: "run-level residual mean -0.01373 95 % CI [-0.01448, -0.01302]"; line 25: "sign-flip p for (observed - null) = 0.0001"; line 29: ts_demean "[-0.00482, +0.00669]"; lines 39–40: ceilings 0.729 and 0.843; lines 58 and 60: 44.2 % and 37.0 %), check_C2_variance_ratio.log (lines 11–12: "+0.974 [paper: +0.977]", "partialling out the variance ratio = +0.946"), check_I1_fig4_scale.log, with their scripts; REC L3944 (entry of 17 September 2026, 17:19 UTC) and its item 2, L3973–3996.

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| S3 Text §4 | S3 L128 | [V, N] "and on r ∈ [−0.95, 0.95]² (0 of 36,481; `notes/fresh_review_2026-09-17/checks/check_A1_atoms_family.log`)" | no |
| S3 Text §4 | S3 L128 | [R] "The ratio's minimum is 6.55 … and 1.9": the text gives the caption file of the figures and `notes/partB1_scope_map.md`, item 2 | no |
| S3 Text §5 | S3 L165 | undecided: "(0.72 and 0.74 for a half, 0.84 and 0.85 at full length by the Spearman–Brown formula)"; "no more than about 0.84". The value is check C1 (3)'s 0.843; the text names no source; REC L3994–3996 gives it as arithmetic on splithalf_tables.md, "(check C1 (3), the same" | no |
| S3 Text §6 | S3 L307 | [V, N] "(−1.1 % against −0.34 %; sign-flip p = 0.0001, a computation of the review of 17 September 2026, `notes/fresh_review_2026-09-17/checks/check_C1_residual_vs_null.log`, with no pre-recorded rule)" | yes |
| S3 Text §6 | S3 L315 | [R] "44 % of the −0.0137 run-level residual at the operating point, 37 % at the pairs' run-level mean point": first stated in the outcome entry of 15 September 2026 (REC L3110–3114); check C1 (4) reproduces it | yes |
| S3 Text §9 | S3 L550 | [V, N] "leaves r = +0.95 (from +0.97 on the series as printed to three decimals, 0.977 unrounded, …; a computation of the review of 17 September 2026, `…/check_C2_variance_ratio.log`)" | yes |
| S5 Text §1 | S5 L7 | [H] "two of its checks are quoted, as review computations, in S3 Text §6 and §9" | no |
| S5 Text §5 | S5 L33 | [H] "the sixth, 17 September, `notes/fresh_review_2026-09-17/`" in the list of reviews | no |
| S12 Table | SUP L343 | [R] "−0.0137 [−0.0146, −0.0129]": B21's inverted interval of the run-level residual | no |
| S17 Table | SUP rows 775–776 (L1180–1181) | [V] the committed percentile intervals "[−0.01448, −0.01302]" and "[−0.00482, +0.00669]" are those of check_C1's log (lines 23 and 29): VT/notes/partB21_inference_revision.py L281, L287 and L291–292 read them from that log | no |

Missing from the cell:
(a) by value or by name: S3 Text §4 (check A1: 0 of 36,481 grid points); S17 Table (rows 775–776: check C1's interval of the run-level residual as the committed interval).
(b) none.
(c) history: S5 Text §1 and §5. S5 Text §1 says that two of its checks are quoted, in S3 Text §6 and §9; with S3 Text §4 there are three.

Undecided: S3 Text §5 (the Spearman–Brown ceilings). The numbers are those of check C1 (3) and of the record's verification of 17 September, which calls them arithmetic on splithalf_tables.md; the text names neither. Whether the place quotes the check cannot be told from the text.

Named in the cell but not quoting it: none.

Proposed complete cell: S3 Text §4 (no grid point of [−0.95, 0.95]² with the |q| derivative the larger: 0 of 36,481), §6 (the run-level residual against the null, p = 0.0001) and §9 (the variance ratio partialled out of the group-mean relation, r = +0.95); S17 Table (rows 775–776, the committed interval of the run-level residual).

### The leave-one-out on the primary DiD (SUP L1703)

Cell now: "Results 2; S4 Text".

Outputs identified. VT/scripts/13_loo_did.py; VT/results/loo_did_win60.csv (28 refits; line 6, ts_gsr with subject 3 dropped: p_signflip 0.007568359375, the largest) and VT/results/run_13_loo_did.log.

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Results 2 | MT L87 | [V] "and, post hoc, in each leave-one-out refit on each variant (p ≤ 0.008)" (CSV L401: a bound on 0.007568, `results/loo_did_win60.csv` line 6) | yes |
| Table 3 (caption, body) | MT L126, L131 | [R] "the 14 leave-one-out" sets; "data, any one subject left out": B27 (c)'s refits of the residual's slope | no |
| S3 Text §5, §6 | S3 L169, L260, L404 | [R] leave-one-out on the cross-half relation (the last row's file), of the sts slope (the next-to-last row's file, item 8) and of the residual slope (B27 (c)): other computations | no |
| S4 Text (R3) | S4 L64 | [N] "leave-one-out (Results 2; `results/loo_did_win60.csv`)" | yes |

Missing from the cell: none.

Named in the cell but not quoting it: none.

Proposed complete cell: Results 2; S4 Text (R3).

### The proportionality check (SUP L1704)

Cell now: "Results 2 (S8 Table cited); S3 Text §9; S8 Table".

Outputs identified. VT/scripts/14_proportionality.py; VT/results/proportionality.csv (header: "POST-HOC analysis specified after the primary result"; its first data row: "windowed_W60,ts_gsr,ratio sts/TDMI: DiD,0.000534…").

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Results 2 | MT L108 | [N] "S8 Table gives a post hoc check of the ratio sts / TDMI" (a pointer) | yes |
| S1 Text | S1 L19 | [N] "the post hoc proportionality check is S8 Table" (a pointer of the same kind) | no |
| S3 Text §9 | S3 L550 | [V] "sts fell less than proportionally to TDMI (S8 Table: +0.0204 [+0.0032, +0.0380], p = 0.025)" | yes |
| S5 Text §1 | S5 L7 | [H] "had dropped one of the four proportionality cells" | no |
| S8 Table | SUP L142–153 | [V, N] "Source: `results/proportionality.csv` (script `14_proportionality.py` at git dbf2311"; four cells and the within-condition changes | yes |
| S17 Table | SUP rows 889–916 (L1294–1321); note L402 | [V] "S8 Table: ratio sts/TDMI: DiD ts_gsr global_fit", scripts/14, +0.02039, 0.0248 (row 903); "S8 Table's share (ii) … (e.g. 0.7797 [0.6531, 0.9362])" | no |

Missing from the cell:
(a) by value or by name: S1 Text (S8 Table cited); S17 Table (rows 889–916 and its note).
(b) none.
(c) history: S5 Text §1.

Named in the cell but not quoting it: none.

Proposed complete cell: Results 2 (S8 Table cited); S1 Text (S8 Table cited); S3 Text §9; S8 Table; S17 Table (its rows).

### The residual's source (SUP L1705)

Cell now: "Results 2 and 4; S3 Text §6 (its residual table: the pair r₁ DiD); S13 Table".

Outputs identified. VT/notes/partB4_residual_source.py; VT/notes/review_results/partB/residual_source.log (line 4: "AR(1) prediction 1.1865 (residual -0.0489); cross-lag substitution only 1.1866 (residual -0.0489); lag-0 substitution only 1.1372 (residual +0.0005)"; line 5: "mean signed +0.00014", "0.0168"; line 6: residual −0.0530, −0.0453, −0.0479, −0.0517 in the four cells; line 10: "pair a: DMT pre +0.8632 post +0.8532; PCB pre +0.8603 post +0.8657; primary DiD -0.0155 (negative in 12/14)"; line 11: "pair |q|: DMT pre +0.2842 post +0.2662; PCB pre +0.2839 post +0.2824; primary DiD -0.0164 (negative in 10/14)"; line 14: "R² 0.744").

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Results 2 | MT L106 | [V] "and pair r₁ by −0.0155"; "Mean pair \|q\| fell by 0.0164 (10 of 14 negative; the count is logged, the per-subject vector not saved)" (CSV L532, L535–536: log lines 10 and 11) | yes |
| Results 2 | MT L108 | [D] "and 5.2 on pair r₁" (CSV L588: 0.0809 / 0.0155) | yes |
| Fig 3 (caption) | MT L110 | [V, D] "(−0.0155 against −0.0146)"; "the data's group means give −0.74 (+0.0115 / −0.0155)" (CSV L606–607, L643, L645) | no |
| Fig 5 (caption) | MT L122 | [V] "exceeds the observed level by 0.049 nats on average" (CSV L757: log line 4) | no |
| Results 4 | MT L124 | [D] "(−0.74 per unit of pair r₁, from the printed means)" (CSV L803) | yes |
| Table 3 (caption) | MT L126 | [V] "(in the data's group means the two DiDs are −0.0146 and −0.0155)" (CSV L815) | no |
| Methods, The AR(1)-substituted estimate and its calibration | MT L245 | [W] "solved to its window-level pair r₁ and \|q\| in each run × period cell": the null's four cells are this log's (S3 L382) | no |
| S3 Text §3 | S3 L122 | [V, N] "(mean \|q_past − q_future\| = 0.0168, `residual_source.log`)" | no |
| S3 Text §4 | S3 L161 | [V, N] "mean pair \|q\| moved from 0.284 to 0.266 on DMT against 0.284 to 0.282 on placebo (DiD −0.0164, negative in 10 of 14; W = 60, post hoc; `…/residual_source.log`)" | no |
| S3 Text §6 | S3 L307 | [V, N] "A post hoc supplement (`ts_gsr` W = 60; `notes/review_results/partB/residual_source.log`)"; "(−0.0489 of −0.0489)"; "+0.0005"; "+0.00014"; "(R² = 0.74" | yes |
| S3 Text §6, its residual table | S3 L321, L325, L337 | [V] "with the pair r₁ DiD beside it for ts_gsr"; "pair r₁ −0.0155"; "+0.0115 / −0.0155 (the pair r₁ DiD is saved at four decimals)" | yes |
| S3 Text §6 | S3 L382 | [N] "equal the four run × period cells of `residual_source.log`" | yes |
| S3 Text §7 | S3 L462 | [V, D] "and the data's by −0.0155"; "against 5.2 in the data (−0.0809 for −0.0155)" | no |
| S3 Text §7 | S3 L436 | [H] the generator's targets "0.8632" and "0.2842" are the log's DMT pre-injection pair a and \|q\| (lines 10 and 11); no source named there | no |
| S4 Text (R1) | S4 L62 | [N] "the pair r₁ and pair \|q\| DiDs (point values)" | no |
| S5 Text §4 | S5 L27 | [H] "the ratio −0.74 per unit of pair r₁, marked as the ratio of the printed means" | no |
| S13 Table | SUP L354, L361, L363 | [V, N] "−0.0155 (pair r₁)"; "The data's pair r₁ change is `residual_source.log`'s (12 of 14 subjects negative)." | yes |
| S18 Table | SUP L1392 | [H] the heading "a = 0.8632" (B23's sensitivity value, the log's DMT pre-injection pair a) | no |

Not counted: the level "−0.0489 (−4.3 %)" of S12 Table (SUP L339; its source line L335 gives diag_tables.md, B4), of S3 Text §1 (S3 L34: "the diagnostic's, diag_tables.md") and the "4.3 %" of Results 4 (MT L120; CSV L726: diag_tables.md) are B4's.

Missing from the cell:
(a) by value or by name: Fig 3 (caption); Fig 5 (caption); Table 3 (caption); S3 Text §3, §4 and §7; S4 Text (R1). In S3 Text §6 the cell's parenthesis names the residual table only; L307 and L382 quote more (the two substitutions applied separately, the signed mean departure, R², the four cells).
(b) in words: Methods, The AR(1)-substituted estimate and its calibration (the cells the null is solved to).
(c) re-use, restatement: S3 Text §7 (the generator's targets); S5 Text §4; S18 Table (a = 0.8632).

Named in the cell but not quoting it: none.

Proposed complete cell: Results 2 (the pair r₁ and |q| DiDs) and 4 (the group-mean rate, −0.74); Figs 3 and 5 and Table 3 (captions); S3 Text §3, §4, §6 (with its residual table) and §7; S4 Text (R1); S13 Table.

### The numbers derived for the revision of 1–2 October 2026 (SUP L1706)

Cell now: "Abstract and Discussion (the mean cross-half correlation at two decimals, in the Abstract with its Fisher-z interval), Results 2 (r² and the SDs of the DiD and of the post-injection gap; the share of reliable variance at the disattenuated interval's lower limit; the FD-residualised r₁ DiD and, in words, the shares of the two contrasts that the FD residualisation removes, a fifth and a sixth), Results 3 (the regional relation on the windowed estimator's own atoms), the Discussion (rtr's slope on regional r₁; the fifth again), Results 4 (the ramp's differences from the step), Results 7 and Table 4 (the inverted intervals of the contrasts at p = 10 and 20; the Fisher-z intervals of the whitened correlations); S3 Text §4, §5, §6 and §8; S11 Table".

Outputs identified. VT/notes/review_2026-10-01_cold_reads/checks/derived_r24.out (80 lines; items 1–12) and derived_r24.py. Lines used: 3 and 19 (item 1: −0.0191 [−0.0285, −0.0098]; −0.0127 [−0.0203, −0.0052]); 36 (item 2: SDs 0.0524, 0.0485, 0.0887, r² 0.79); 43 (item 3: +0.4981); 46–48 (item 4: 38 %; removed 0.197 and 0.163; −0.0123); 55–56 (item 5: +0.000148, +0.000620); 58–62 (item 6: +0.693672 [+0.258078, +0.894889] and the four whitened correlations on ts_gsr at W = 60); 65 (item 7: +0.898, +0.868, +2.3038, +0.850); 69 (item 8: +4.263; +4.139 to +4.535); 71 (item 9: 0.30, 0.35, 0.35, −0.543); 73–74 (item 10); 76–77 (item 11: 119 of 120; 0.1871 and 0.1873).

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Abstract | MT L15 | [V] "(cross-half r 0.69 [0.26, 0.89], disattenuated 0.95)" (CSV L23–25: line 58) | yes |
| Results 2 | MT L87 | [V] "(the DiD's SD 0.0887 against the post-injection gap's 0.0485; r(DiD, pre-injection gap) = −0.888, r² = 0.79)" (CSV L390–393: line 36) | yes |
| Results 2 | MT L106 | [V, D] "removes a fifth of the sts contrast (−0.0649 [−0.1010, −0.0260]) and a sixth of r₁'s (−0.0123)" (CSV L553: line 48) | yes |
| Results 2 | MT L108 | [V] "they share 38 % of their reliable variance" (CSV L566: line 46) | yes |
| Fig 3 (caption) | MT L110 | [R] "mean r = +0.694, Fisher-z interval of the mean [+0.258, +0.895]": at three decimals from B21 (d) (CSV L623–625) | no |
| Results 3 | MT L114 | [V] "r = 0.898 (post hoc; S3 Text §4)"; "2.30 for the windowed atoms" (CSV L668, L672: line 65). [R] "a slope of 0.50 nats per unit": CSV L687 derives it from regional_partial_tables.md | yes |
| Results 4 | MT L124 | [V] "the ramp moves the generators' mean residual DiD by 0.0001 and 0.0006 nats from the step (unrounded means)" (CSV L800–801: lines 55–56) | yes |
| Results 7 | MT L158 | [V, W] "−0.0127 [−0.0203, −0.0052]" (CSV L1048–1049: line 19); "(the Fisher-z interval of neither correlation excludes zero)" | yes |
| Table 4 (body) | MT L167–168 | [V] "−0.0191 [−0.0285, −0.0098]"; "−0.0127 [−0.0203, −0.0052]" (CSV L1108–1109, L1117–1118: lines 3 and 19). The Fisher-z intervals are not in Table 4 | yes |
| Discussion, What the finding is and is not | MT L183 | [V] "(cross-half r = 0.69, disattenuated 0.95)" (CSV L1149: line 58) | yes |
| Discussion, The fall of r₁ under DMT | MT L187 | [D] "residualising on it removes a fifth of the sts contrast (Results 2)" | yes |
| Discussion, The literature | MT L191 | [V] "rtr's slope on r₁ is 0.50, still a sixth of sts's 3.09" (CSV L1175: line 43) | yes |
| S3 Text §4 | S3 L132 | [V, N] "+0.898 (Spearman +0.868; +0.850 over the 99 cortical parcels) and the slope +2.30"; "(`…/checks/derived_r24.py`, item 7 of its output `derived_r24.out`)" | yes |
| S3 Text §5 | S3 L260 | [V, N] items 2, 9, 8 and 11 named: "(`derived_r24.out`, item 2)"; "4.139 (without subject 14) to 4.535 (without subject 8)"; "119 recompute as printed" | yes |
| S3 Text §6 | S3 L404, L406 | [V, N] "(the means over the replicates, `derived_r24.out`, item 5"; "[−0.760, +0.183] and [−0.897, −0.269]" with item 10 named | yes |
| S3 Text §8 | S3 L531, L544 | [V, N] "(`…/checks/derived_r24.out`, item 1, from the committed per-subject vectors)"; "[−0.112, +0.789], [−0.240, +0.734], [−0.048, +0.812] and [+0.704, +0.968] (`derived_r24.out`, item 6)" | yes |
| S11 Table | SUP L256 | [N] "whose intervals are the inverted sign-flip intervals computed from its committed per-subject vectors (`…/checks/derived_r24.out`, item 1)" | yes |
| S19 Table, Part A | SUP L1677, L1687 | [V, N] row B28 (c): "the means over the replicates differ by 0.0001 and 0.0006 nats (`derived_r24.out`, item 5)"; row B16c (e): "and in `derived_r24.out`, item 1" | no |

Missing from the cell:
(a) by value or by name: S19 Table, Part A (rows B28 (c) and B16c (e)).
(b) none.
(c) none.

Named in the cell but not quoting it: none. Two remarks on the parentheses: the Fisher-z intervals of the whitened correlations are in Results 7 (in words) and not in Table 4, which holds the inverted intervals only; the slope "0.50" of Results 3 is derived by CSV from B20's table, while the same slope in the Discussion is taken from this file (item 3).

Proposed complete cell: the cell as it stands, with "; S19 Table, Part A (rows B28 (c) and B16c (e))" added at its end.

### The numbers derived on 24 September 2026 (SUP L1707)

Cell now: "Results 2 (the Fieller interval of the sts rate; the leave-one-out cross-half values), Results 3 (the cortex-only correlation; the t intervals of the partialled contrast), Results 4 (the Fieller interval of the residual rate), Results 7 (the band-limit bound), Methods (the null's own pair-r₁ DiD); S3 Text §4–5".

Outputs identified. VT/notes/review_2026-09-24/checks/derived_r17.out (43 lines) and derived_r17.py; VT/notes/review_2026-09-30/checks/derived_r17_b26.out (the same script on B26's outputs). Lines of derived_r17.out: 2 ("+5.522; Fieller 95 % [+4.45, +10.54]"); 3 ("-0.787; Fieller 95 % [-1.60, -0.08]"; −0.788 at line 3 of the second file); 4 (the r₁ DiD by subject, −0.0642 and 0.0242); 5–36 (item 2, the leave-one-out cross-half values; lines 13, 19, 20: 0.486, 0.571, 0.680–0.830); 37–38 (item 3, the t intervals); 39 (item 4: "+0.807 … slope +2.286"); 40 ("cos(2*pi*0.08*2) = 0.5358; flat 0.01-0.08 Hz: r1 = 0.8174"); 41 ("drtr/dr1 = 0.0556"); 42 ("= 1.41"); 43 ("null pair r1 DiD: (0.8532 - 0.8625) - (0.8655 - 0.8602) = -0.0146; level ratios: 0.76 …, 0.67").

| place | line | what is quoted there | in the cell now? |
|---|---|---|---|
| Results 1 | MT L53 | [V] "make the per-SD ratio 1.4" (CSV L99: "derived_r17.out item 5", line 42) | no |
| Results 1 | MT L59 | undecided: "reproduces most of its level": no value; line 43 holds level ratios 0.76 and 0.67, which the wording may rest on; the text names no source | no |
| Results 2 | MT L108 | [V] "subject 8 (the largest fall of r₁, −0.064"; "(the largest rise, +0.024)"; "0.90 or 0.92"; "0.486 or 0.571 (other omissions: 0.68–0.83"; "5.5 nats on whole-brain r₁ (Fieller interval [4.45, 10.54]" (CSV L571–586) | yes |
| Fig 3 (caption) | MT L110 | [V, D] "(−0.37: +0.0054 / −0.0146; Methods)" (CSV L640, L642: line 43) | no |
| Results 3 | MT L114 | [V] "r = 0.807 over the 99 cortical parcels"; "−0.0202 [−0.0342, −0.0062] to +0.0007 [−0.0110, +0.0124]"; "the family's 0.056" (CSV L658, L677–681, L688) | yes |
| Results 4 | MT L124 | [V, D] "−0.79 per unit of whole-brain r₁"; "a Fieller interval of [−1.60, −0.08]" (CSV L802–805: derived_r17_b26.out line 3); "−0.37" (CSV L792) | yes |
| Table 3 (caption, body) | MT L126, L131–132 | [D] "(−0.18, −0.39 and −0.37)" (CSV L823, L860, L872: the null's own pair-r₁ DiD as denominator) | no |
| Results 7 | MT L158 | [V] "= 0.54"; "below 0.54" (CSV L1038, L1040: line 40) | yes |
| Discussion, What the finding is and is not | MT L181 | [R] "1.4-fold in the windowed estimator": CSV L1146 derives it from aligned_directed_tables.md without naming this file | no |
| Methods, The AR(1)-substituted estimate and its calibration | MT L245 | [V] "(its own pair-r₁ DiD −0.0146)" (CSV L1328: line 43) | yes |
| S3 Text §4 | S3 L130, L134 | [V, N] "+0.807 and the slope +2.29 nats per unit r₁ (`notes/review_2026-09-24/checks/derived_r17.out`, item 4)"; "1.4 times its \|q\| rate (5.126 × 0.0284 against 0.528 × 0.1957)" | yes |
| S3 Text §5 | S3 L169–187 | [V, N] "(`…/derived_r17.out`, item 2; a post hoc computation of 24 September 2026, no pre-run entry)" and its table of fourteen omissions | yes |
| S3 Text §5 | S3 L258 | [D] "11 contain −0.37 (the finite-sample null's)" (B27 (c)'s counts against the rate) | yes |
| S3 Text §6, its residual table | S3 L321, L329 | [V, D] "−0.37 (null)"; row 5's autocorrelation change "−0.0146" | no |
| S4 Text (P5, R1, R3) | S4 L38, L62, L64 | [V, N] "r₁ ≥ 0.54 for any series confined to the band"; "the regional contrast of Results 3 (t intervals from the saved mean and SD)"; "leave-one-out on the cross-half relation (S3 Text §5)" | no |
| S13 Table | SUP L363 | [V] "+5.5, that is 0.0055 nats per 0.001, per unit of whole-brain r₁"; "(+0.0054 for its own −0.0146;" | no |
| S18 Table | SUP L1523 | [R] "0.8174 is the continuous-band value of the flat-spectrum r₁": B23 (d)'s table | no |

Missing from the cell:
(a) by value or by name: Results 1 (the per-SD ratio of the windowed estimator, 1.4); Fig 3 (caption: the null's own pair-r₁ DiD); Table 3 (the rate −0.37, whose denominator it is); S3 Text §6 (its residual table, row 5); S4 Text (P5, R1, R3); S13 Table (the sts rate per unit of whole-brain r₁; the null's own pair-r₁ DiD). Inside the named places the parentheses leave out the r₁ DiDs of subjects 8 and 14 (Results 2) and the family's ∂rtr/∂r₁ (Results 3).
(b) none decided; Results 1 (L59, "most of its level") is undecided.
(c) none.

Named in the cell but not quoting it: none. "Methods" stands without its subsection, which is The AR(1)-substituted estimate and its calibration. One remark on S4 Text: its item P5 (S4 L38) says the two values are "stated in Results 7 and S1 Text"; S1 Text (S1 L5) states the 0.82 and not the 0.54.

Proposed complete cell: Results 1 (the windowed estimator's per-SD ratio), Results 2 (the Fieller interval of the sts rate; the r₁ DiDs of subjects 8 and 14; the leave-one-out cross-half values), Results 3 (the cortex-only correlation; the t intervals of the partialled contrast; the family's ∂rtr/∂r₁), Results 4 (the Fieller interval of the residual rate), Results 7 (the band-limit bound); Fig 3 (caption) and Table 3 (the null's own pair-r₁ DiD, in the rate −0.37); Methods, The AR(1)-substituted estimate and its calibration (the null's own pair-r₁ DiD); S3 Text §4–6 (§6: its residual table, row 5); S4 Text (P5, R1, R3); S13 Table.

## Task 2

Read for this task: MT (Abstract to Data and code availability), S1–S5 Text, every source line and note of SUP, Part A and Part B of S19 Table, and every file name the paper gives in a code span (277 distinct names), each classed as pipeline, B-numbered computation with a pre-run entry, check of the pipeline's reproduction, or other. "No row" means that no first cell of SUP L1695–1707 names the computation or its file.

### Computations quoted by the paper, run without a pre-run entry, with no row in Part B

**1. The first review's check script (VT/notes/review_checks.py; log VT/notes/review_results/logs/review_checks.log).**
Where quoted: S5 Text §1, S5 L7: "whose DiD is negative in 12 of 14 subjects (−0.0994 by the later pre/post definition"; "whose per-subject DiDs correlate at 0.95 with the windowed ones"; "a CCS decomposition with phyid's mask on 400 random pairs showing an sts increase in 14 of 14 subjects". S5 Text §4 (S5 L25) names the log in the run inventory.
Source: review_checks.log line 69 ("per-subject r(global-fit DiD, windowed DiD) = 0.954"), line 70 ("DiD -0.0994, negative 12/14, p=0.0156"), lines 83 and 85 ("CCS: sts baseline -0.033; sts DiD +0.0212 (negative 0/14, p=0.0001)"); VT/notes/adversarial_review_2026-09-14.md L106, L108, L137, L228.
No pre-run entry: the script's head (review_checks.py L2–3) calls it "every computation quoted in notes/adversarial_review_2026-09-14.md that is not already in results/*.csv"; REC names it in lists of scripts (REC L3447, L4373, L4394) and in the entry on B26's run (L8206–8208); none is a pre-run entry for it.
Why no row covers it: the first row names `notes/review_computations_2026-09-14.md`, the review's companion file, which holds none of the three (it has no "400" and no "0.0994"); it is covered only if "the review computations of 14 September 2026" is read as every computation of that review.
Proposed row: The first review's check script (`notes/review_checks.py`, 14 September 2026) | S5 Text §1 (the correlation of the global-fit DiDs with the windowed ones; the 20-region fit's DiD and sign count; the CCS check on 400 random pairs) | Computations of the first adversarial review that its companion file does not hold; no pre-run entry. (Or the same three items added to the first row's first cell, and "S5 Text §1" to its second.)

**2. The ΦR baseline gap, the placebo run's slope and its decline within the pre-injection windows (VT/notes/review_results/logs/phir_baseline_and_slope.log).**
Where quoted: S2 Text, S2 L9: "(deconvolved −0.0124, p = 0.014; raw −0.0042, p = 0.28)"; "(deconvolved slope −0.00115 per window, p = 0.025; raw −0.00036, p = 0.43)"; "(−0.0084 [−0.0174, −0.0003], p = 0.039) as well as after deconvolution (−0.0120, p = 0.067) (`phir_baseline_and_slope.log`)"; the log is among the sources at S2 L3. S17 Table rows 931–932 (SUP L1336–1337: "ΦR, placebo window 4 − window 1, raw series ts_gsr", −0.00840, 0.0391) and its note (SUP L402: "the deconvolved ΦR values of S2 Text").
Source: the log's lines 2–5 (line 2: "DMT pre − PCB pre -0.0124 [-0.0210, -0.0042] p = 0.0140"); VT/notes/regional_phir_deconv_2026-09-14.md L220–226.
No pre-run entry: regional_phir_deconv_2026-09-14.md L220: "Not in the recorded plan: these four tests were added after looking at the window series above, and are descriptive." The closure entry (REC L2407–2415) quotes them afterwards.
Why no row covers it: the first row names `notes/review_computations_2026-09-14.md`, which does not hold them; the Part A row of the regional ΦR check (SUP L1616) is the row of a recorded prediction.
Proposed row: The ΦR baseline gap, the placebo run's slope and its decline within the pre-injection windows (`notes/review_results/logs/phir_baseline_and_slope.log`, 14 September 2026) | S2 Text; S17 Table (the raw window 4 − window 1 rows) | Four tests added after the window series of the regional ΦR check had been seen; not in its recorded plan.

**3. The third review's partial correlations (VT/notes/adversarial_review_draft_v2_second_pass_2026-09-15.md, Appendix, computation 4).**
Where quoted: S3 Text §6, S3 L384: "leaves it at partial r = +0.83 and +0.86 under the published CCS definition (computed by the third review from the committed per-subject DiDs"; "`phyid`'s mask gives +0.69 and +0.82)".
Source: that file's L212 ("partial on the autocorrelation DiD +0.831 / +0.855"; "partial +0.688 / +0.820"); recomputed on B26's outputs in VT/notes/review_2026-09-30/checks/partial_b26.out lines 2–3 (+0.831, +0.855; +0.687, +0.820), which REC L8304 reports.
No pre-run entry: the text itself calls it a computation of the third review; S5 L3 defines a computation "by the adversarial reviews of 14–17 September 2026" as post hoc.
Proposed row: The third review's partial correlations of the residual DiD with the CCS-sts DiD (`notes/adversarial_review_draft_v2_second_pass_2026-09-15.md`, Appendix, computation 4, 15 September 2026; recomputed on B26's outputs, `notes/review_2026-09-30/checks/partial_b26.out`) | S3 Text §6 | Computed by the third review from the committed per-subject DiDs; no pre-run entry.

**4. The interval of the directed response's DMT − placebo difference (23 September 2026).**
Where quoted: S3 Text §6, S3 L317: "is +0.00044 [−0.00061, +0.00149], p = 0.38 (the interval inverts the sign-flip test on the per-run values of `directed_crosslag.csv`, computed on 23 September 2026)".
Source: the point value and p are B15's (VT/notes/review_results/partB/directed_crosslag_tables.md line 12: "of the directed response: +0.00044, p = 0.3800"; REC L4964). The interval is in no committed file: a search of VT/notes and VT/manuscript for its two bounds finds S3 L317 only. B21 holds the mean of the two runs, not their difference (SUP rows 783–784, L1188–1189; VT/notes/partB21_inference_revision.py L310–318).
No pre-run entry: none found for this interval; REC has no line with its bounds.
Proposed row: The inverted interval of the directed response's DMT − placebo difference (23 September 2026) | S3 Text §6 | Computed from the per-run values of `directed_crosslag.csv` (B15); no pre-run entry and no output file.

**5. The transfer entropies under an invertible filter (VT/notes/review_2026-10-01_cold_reads/audit/te_filter_check.py).**
Where quoted: S3 Text §3, S3 L124: "with coefficients 0.90 and 0.70 and innovation correlation 0.3, passed through the invertible filter 1 + 0.6L + 0.3L²"; "0 before the filter and 0.0015 and 0.0004 nats after it"; "(a population computation without data, made in the audit of this revision's citations, S5 Text §5: `…/audit/te_filter_check.py`)".
Source: the script (its L1: "evidence for finding C01 of findings_citations.md"; L7: "population values, no data, no random numbers"); it has no committed output file.
No pre-run entry: REC names it at L9237 and L9446 as the audit's check, after the fact.
Proposed row: The lag-1 transfer entropies under an invertible filter (`notes/review_2026-10-01_cold_reads/audit/te_filter_check.py`, 2 October 2026) | S3 Text §3 | A population computation without data, made in the audit of the revision's citations; no pre-run entry.

**6. The values an audit computed on the released series (VT/notes/review_2026-10-01_cold_reads/audit/findings_text.md, findings T07, T10 and T25).**
Where quoted: S5 Text §4, S5 L27: "the mean per-subject regional slope (2.644997, with a mean r² of 0.576258)"; "(−0.015468)", "(−0.014645)", "(+0.011534), with the ratio of the last to the first (−0.7457)"; "(−0.861 [−1.299, −0.422], r = −0.777)"; "The paper uses none of these".
Source: findings_text.md L81–82 (T07), L100 (T10), L189–190 (T25).
No pre-run entry: REC L9455–9456: "The text audit rested three of its findings on the released series, which it fetched outside its clone (its T07, T10 and T25)".
Why it is listed: the head note of S19 Table (SUP L1601) leaves out of Part B "the checks of the pipeline's reproduction, which S5 Text reports"; these values are in S5 Text §4 but are checks of three statements of the text, not of the pipeline's reproduction. The paper prints them and says it uses none.
Proposed row: The values an audit computed on the released series (`notes/review_2026-10-01_cold_reads/audit/findings_text.md`, T07, T10 and T25, 2 October 2026) | S5 Text §4 | Computed outside the clone to check three statements; quoted as the audit's, used by no result.

### Borderline cases

**a. The third review's variations of the finite-sample null (the same Appendix, computation 3).** S3 L307: "which the third review (15 September 2026) varied"; "the range those variations gave is no longer quoted"; S3 L382: "The third review re-ran it (it reproduces) and varied two of its free choices". Named as the source of a statement; no value quoted. It could share the row proposed under 3.

**b. The deconvolved ΦR contrast at W = 30 and the two other whole-brain items of the regional ΦR pre-specification (VT/notes/rev_phir_items.py; VT/notes/review_results/inference_rows_w30.csv).** Quoted in S2 L9 ("a 56–64 % placebo share of the DiD": the 56 % is the W = 30 row, placebo_share 0.5599 at line 2 of the CSV; REC L2418 "64 % at W = 60, 56 % at W = 30"), in S17 Table rows 709–738 (SUP L1114–1143), in S5 L15 ("raw, deconvolved, W = 30") and S5 L25 (the file named). They were entered before they were run, with no prediction: VT/notes/prespec_regional_phir_deconv_2026-09-14.md L23, "Three whole-brain items requested at the same time (no prediction)". Their status is that of the coupled family and the leave-two-out, which Part B lists as "entered with no prediction"; Part A's row (SUP L1616) is the regional prediction only.

**c. The Fisher-z intervals of the eight whitened correlations at p = 10 and 20.** S3 L544: "run from −0.079 to +0.570 over the eight cells, the Fisher-z interval including zero in seven of them (not at p = 10 on ts_gsr at the global fit, +0.570)". derived_r24.out item 6 (lines 61–62) holds two of the eight (ts_gsr, W = 60); the other six correlations are in VT/notes/review_results/partB/prewhiten_fixed_tables.md (lines 53, 77, 102, 151, 175, 200) and their intervals in no output file (an audit's check file, VT/notes/review_2026-10-01_cold_reads/audit/check_VR.md L134, prints the one that excludes zero). The next-to-last row covers the statement in part; the rest is B21 (d)'s formula applied to printed correlations.

**d. The family-scale conversion of the run-level cross-lag departure (44 % and 37 %).** S3 L315 and S9 Table's note, SUP L187: "+0.0034 gives −0.0061 (44 % of the observed −0.0137)"; "−0.0051 (37 %)". Source: the outcome entry of 15 September 2026, 18:18 UTC, item 3, REC L3110–3114: "stated here, not in a result file". The computation it belongs to had a pre-run entry (18:14 UTC); the conversion was added in the outcome entry; check C1 (4) of the review of 17 September reproduces it (its log, lines 58 and 60).

**e. The Spearman–Brown ceilings of S3 Text §5** (S3 L165; see the row of the checks of 17 September in Task 1): arithmetic of the record's entry of 17 September (REC L3994–3996) that check C1 (3) also holds; no source named in the text.

**f. The conversions of A_other, recomputed on B26's outputs (VT/notes/review_2026-09-30/checks/conversions_b26.out).** S3 L372: "The conversions of the B22 outcome entry, recomputed with B23's values as B26 corrected them"; "−2.42", "−1.72", "−2.73", "about −40"; "+0.00146 [−0.00096, +0.00404]"; "0.16–0.19 [−0.12, +0.52]". The values are those of conversions_b26.out lines 7–10, 12–14 and 22–25; the text does not name that file. The conversion was planned in B22's pre-run entry (REC L6061: "converted to residual-DiD equivalents with B23's two aligned conversions"), so it is not post hoc; the recomputation itself is a check output with no entry of its own (REC L8305 reports it).

**g. Values written by the figure script (VT/scripts/15_figures_v2.py; VT/manuscript/figures/captions_v2.md).** Fig 1's caption, MT L55: "median r₁ 0.855, median |q| 0.249" (CSV L117–118: "computed by scripts/15_figures_v2.py from the saved pre-injection pairs of subject 1"); Fig 2's caption, MT L83: "at most 0.00143 in absolute value" (CSV L371); S3 L128: "The ratio's minimum is 6.55 … and 1.9 … (the caption of the map in `manuscript/figures/captions_v2.md` as generated at 48ea934". Summaries, by a plotting script, of the outputs of computations that have entries (B1's overlay, B14's atom table); no entry of their own.

**h. A closed-form share in S8 Table's note.** SUP L153: "sts carries 0.99 of the change in TDMI against a baseline share of 0.98 (closed form, TDMI = 2S and sts = 2S − C; main text, Results 1)". No file is named for the two figures; they follow from the closed form.

**i. The subject-alignment check (VT/scripts/10_subject_alignment_check.py, 13 September 2026).** Named without a value in S1 L5 ("the subject-order check of `scripts/10_subject_alignment_check.py`") and S4 L41 ("subject alignment across files checked"). It was run on the day and at the commit of the global functional connectivity computation, which has a row (REC L1853–1862: "checked 13 Sep 2026", "run at 66b570e-dirty"); REC has no entry on it before that section. It is a check of the data's integrity; no result is quoted from it.

**j. Values that a pre-run entry lists as known before its run.** S19 Table, Part A, row B23 (a1), SUP L1653: "+0.0036 and +0.0037 at ±0.01, +0.0154 and +0.0158 at ±0.02 (values known from the verification of 22 Sep on another pool)". They are values of the check scripts of the review of 22 September (VT/notes/review_2026-09-22/refcheck/; REC L6151–6155: "Already computed on 22 Sep, on other pools or designs, and so known rather than predicted"), quoted as what B23's entry recorded. The head note of S19 Table (SUP L1601) says this of B23, and says of B21 (b) and (c) and of B27's values that their entries list them as known; S3 L231 says the same of B27 ("computed from the committed per-subject values before the run"). The results the paper reports are those of the runs with entries; no row.

**k. The validation of the second implementation** (Methods, Estimator, MT L217: "≤ 1.3 × 10⁻¹⁴", "≤ 2.3 × 10⁻¹⁴", "1.0 × 10⁻¹³"; CSV L1249–1251: VT/notes/review_results/logs/phiid_fast_validate.log and phiid_fast_validate_local.log). Not listed as post hoc: the pre-specification of the regional ΦR check planned it (prespec_regional_phir_deconv_2026-09-14.md L16: "the implementation is validated … before use, and the validation numbers are reported"), and its report gives it (regional_phir_deconv_2026-09-14.md L21–43).

Not listed, as the task sets out: B1–B29, B16b, B16c and B17b where a pre-run entry or the plan of 14 September covers them; the pipeline of `scripts/` and `results/` where the text does not call it post hoc; the checks of the pipeline's reproduction of S5 Text §4 (the runs of run_all.sh, the re-runs by separate sessions, the comparison scripts, `11_ccs_agree_share_check.py`).
