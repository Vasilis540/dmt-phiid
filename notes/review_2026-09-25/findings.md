# Findings: error-only read of the finished paper (repository at ddae618), 25 September 2026

Classes: T text, N numbers, X cross-references, C contradictions, U uncertain. Line numbers are the original line numbers of the repository files. Findings are appended file by file.

## 1. manuscript/draft_v2.md

### N1
- **Location**: manuscript/draft_v2.md, line 83 (Fig 2 caption); the same string is in manuscript/figures/captions_v2.md line 11.
- **Quote**: "the mirror atoms +0.0395 to +0.0400"
- **Problem**: The range of the four mirror atoms' residual levels is misstated: its lower end is +0.0389 (yts), not +0.0395; two of the four values (+0.0389, +0.0392) lie outside the stated range.
- **Evidence**: Table 1 (draft_v2.md lines 72, 76, 78, 79) and its source notes/review_results/partB/family_atoms_tables.md lines 17, 21, 23, 24: residual level xts +0.0395, yts +0.0389, stx +0.0400, sty +0.0392.
- **Fix**: "the mirror atoms +0.0389 to +0.0400" (in draft_v2.md line 83 and in captions_v2.md line 11 / the figure script's caption string). Word count unchanged.

### N2
- **Location**: manuscript/draft_v2.md, line 83 (Fig 2 caption); the same string is in captions_v2.md line 11.
- **Quote**: "the six cross-prediction atoms ±0.0231 where the substituted atoms are ±0.0027"
- **Problem**: At the printed four decimals the single values are wrong for most of the six atoms: four of the six residuals are ±0.0230 (only rtx and ytr are +0.0231), and three of the six substituted values are ±0.0024 (only rtx, ytr, ytx are ±0.0027). The same sentence gives the mirror atoms as a range, so the single value reads as exact.
- **Evidence**: Table 1 lines 66, 67, 69, 71, 73, 74 and family_atoms_tables.md lines 11–19: residuals +0.0231, +0.0230, +0.0230, −0.0230, +0.0231, −0.0230; substituted +0.0027, +0.0024, +0.0024, −0.0024, +0.0027, −0.0027. main_text_numbers.csv rows 361–362 themselves describe these as "±0.0230 to 0.0231" and "±0.0024 to 0.0027".
- **Fix**: "the six cross-prediction atoms ±0.0230 to ±0.0231 where the substituted atoms are ±0.0024 to ±0.0027" (both files). Adds 4 words to the caption.

### C1
- **Location**: manuscript/draft_v2.md, line 146 (Results 6), against line 53 (Results 1).
- **Quote**: "against +6.09 for MMI-sts"
- **Problem**: The slope of MMI-sts in r₁ on the symmetric AR(1) family at (0.85, 0.25) is given as +6.07 in Results 1 ("∂sts/∂r₁ = +6.07") and as +6.09 in Results 6, with no stated reason for the difference (the +6.09 is a central difference of fitted values over r₁ 0.83–0.87, the +6.07 the exact derivative).
- **Evidence**: notes/review_results/partB/diagnostic_alternatives_tables.md line 144: "Central-difference slope of CCS-sts in r₁ at q = 0.25 (0.83 to 0.87): -0.0134 per unit r₁ (MMI-sts from the same fits: +6.0903)"; notes/review_2026-09-24/checks/derived_r17.out: "family at (0.85, 0.25): dsts/dr1 = 6.0705"; lag_tables.md: ∂sts/∂r = +6.071 at +0.85.
- **Fix**: "against +6.09 for MMI-sts, both as central differences over r₁ 0.83–0.87" (keeps the like-for-like pair and states why it differs from 6.07; adds 8 words), or, if the source figure need not be kept, "against +6.07 for MMI-sts" (word count unchanged).

### T1
- **Location**: manuscript/draft_v2.md, line 25 (Introduction, first sentence).
- **Quote**: "Integrated Information Decomposition (ΦID; Mediano"
- **Problem**: The term is capitalised as a proper name here, but written "integrated information decomposition" in the title (line 1), the Abstract (line 15), the Author summary (line 19) and the running title of every S Text; the same sentence writes "partial information decomposition" in lower case. (Capitals in the reference list are the cited works' own titles and are correct.)
- **Evidence**: grep: lower case at draft_v2.md lines 1, 15, 19 and S1–S5 Text line 3; title case only at line 25 in running text.
- **Fix**: "Integrated information decomposition (ΦID; Mediano" (word count unchanged).

### U1
- **Location**: manuscript/draft_v2.md, line 142 (Fig 6 caption); same string in captions_v2.md line 27.
- **Quote**: "Where the lag-τ autocorrelation contrast is negative (τ = 1, 2, 3) the sts contrast is negative, and at τ = 5, where the autocorrelation contrast is near zero, so is the sts"
- **Problem**: The caption's own panel (b) values give a negative lag-τ autocorrelation DiD at τ = 5 too (−0.0108, about three-quarters of the τ = 1 value −0.0146), so "negative (τ = 1, 2, 3)" as the list of negative lags, and "near zero" at τ = 5, contradict the printed numbers. The intended sense is probably "distinguishable from zero" (τ = 5: p = 0.567).
- **Evidence**: draft_v2.md line 142, panel (b): "(−0.0146, −0.0468, −0.0681, −0.0108)"; notes/review_results/partB/lag_tables.md line 14: τ = 5 r_τ DiD "-0.0108, 0.5670" (against p = 0.0106, 0.0090, 0.0132 at τ = 1, 2, 3).
- **Fix** (if confirmed): "Where the lag-τ autocorrelation contrast is distinguishable from zero (τ = 1, 2, 3) the sts contrast is negative, and at τ = 5, where it is not (p = 0.57), neither is the sts" (both files; adds about 3 words).

## 2. manuscript/figures/captions_v2.md

The six caption strings (lines 7, 11, 15, 19, 23 and 27, without their closing Source sentence) were compared character by character with the six captions of draft_v2.md (lines 55, 83, 104, 110, 116, 142): all six are identical. The errors N1, N2 and U1 above are therefore also in captions_v2.md (line 11 for N1 and N2, line 27 for U1) and must be fixed in the figure script's caption strings as well. Every file named in the Source sentences exists in the repository. No further finding.

## 3. The six figures (manuscript/figures/fig1_v2_scope_map.png … fig6_v2_lag_dependence.png)

Panel letters, axis labels, legends and printed values were compared with the captions and the text: Fig 1 (formula, contour levels 0.25/0.5 labelled inline, operating point, the four panel-c curves and their styles, the c-values 1.2588 … 1.4111); Fig 2 (colours, grouping annotations, the −0.084/−0.100 and 0.008 annotation); Fig 3 (r, intervals, OLS and generator rates in all three panels, markers and index labels); Fig 4 (legend counts Vis 17, SomMot 14, DorsAttn 14, SalVentAttn 12, Limbic 5, Cont 13, Default 24, Subcortex 16 = 115, giving the caption's 31 sensory and 37 association parcels; the partialled values; F, spin p and the two contrasts); Fig 5 (y-range, shading, window-5 hatch, injection line, equal nats per unit height in a, b and c, the +0.0027 ± 0.0014 step); Fig 6 (values, whiskers, per-subject r, the r_τ labels +0.85/+0.51/+0.14/−0.20). No error found in Figs 1, 2, 3, 5 and 6 (the Fig 5c legend placement is excluded by the brief). A second pass over the printed numbers of Fig 4, tracing each to the formatting in `scripts/15_figures_v2.py` (read, not run), found two errors: N4 and T9, in section 3 (continued) below. The figure-6 whisker for the τ = 5 autocorrelation DiD includes zero, which is relevant to U1.

## 4a. manuscript/si/S1_Text.md

No error found in the text itself. Checked: the Primary B figures against Table 2 and S17 Table; the W = 30, global-fit and Robustness C figures against S17 Table / S3 Text; the commit identifiers 44cec4f, 33f0b33, e16ebba–e46df8a and 84ea657 against `git log` (dates and subjects match); the record heading "Pre-registered analysis choices" (exists); "S3 Text, section 6" for the bias characterisation (correct); the software versions against `requirements.lock.txt` (NumPy 2.5.3, SciPy 1.18.1, Matplotlib 3.11.1 match). The S2–S7 Table numbers S1 Text quotes are checked in section 5 below.

## 4b. manuscript/si/S2_Text.md

No error found. Checked against `notes/review_results/inference_rows_deconv.csv`, `partB/inference_revision_tables.md` (the inverted intervals of the deconvolved sts, autocorrelation and ΦR DiDs and of the raw ΦR window 4 − window 1 change), `logs/phir_baseline_and_slope.log`, `notes/review_computations_2026-09-14.md` §3 (time to peak 6.08/6.07 s), the `nogit` headers of the four deconvolved atom CSVs, the absence of a commit identifier in the regional files and `inference_rows_deconv.csv`, the parameters in `notes/rev_deconv.py`, and "S3 Text §10" (correct).

## 4c. manuscript/si/S3_Text.md

### X1
- **Location**: manuscript/si/S3_Text.md, line 1, against manuscript/draft_v2.md line 362 (Supporting-information caption).
- **Quote**: "# S3 Text. The supporting tables of the estimator account"
- **Problem**: The S3 Text title differs from its Supporting-information caption, which reads "S3 Text. The supporting analyses of the estimator account." The other four S Text titles match their captions word for word.
- **Evidence**: draft_v2.md line 362: "**S3 Text. The supporting analyses of the estimator account.**"
- **Fix**: "# S3 Text. The supporting analyses of the estimator account" (or change the caption to "tables"; the caption lists analyses, so the file title is the one to change).

### X2
- **Location**: manuscript/si/S3_Text.md, line 124.
- **Quote**: "(record, \"Part B, item 1\")"
- **Problem**: The record (`manuscript/analysis_record.md`) has no entry or heading "Part B, item 1"; its only Part B headings are "Part B, items 6–8: pre-run entry" and "…: outcomes". The scope-map plan is item B1 of `notes/partB_prespec_2026-09-14.md` ("## B1. Scope map (no prediction)"), committed at 477cccc.
- **Evidence**: grep of the record: no "Part B, item 1"; `notes/partB_prespec_2026-09-14.md` line 7.
- **Fix**: "(`notes/partB_prespec_2026-09-14.md`, item B1)".

### X3
- **Location**: manuscript/si/S3_Text.md, line 124.
- **Quote**: "on |q| ≤ 0.95 (`manuscript/figures/captions_v2.md`)"
- **Problem**: The file cited as the source of "The ratio's minimum is 6.55 at (0.61, ±0.6) … and 1.9 at (0.77, ±0.95)" no longer contains either value: the current captions_v2.md (regenerated at 7470eae) has no ratio minimum. The values were in the captions file up to 0b8d1a4.
- **Evidence**: grep of the current captions_v2.md: no "6.55", no "0.77"; `git show 0b8d1a4:manuscript/figures/captions_v2.md` line 11 holds both; `notes/partB1_scope_map.md` line 12 holds 6.55; `notes/adversarial_review_draft_v2_second_pass_2026-09-15.md` line 124 holds "ratio minima 6.55 at (0.61, ±0.6) and 1.89 at (0.77, ±0.95)".
- **Fix**: "on |q| ≤ 0.95 (`notes/partB1_scope_map.md`, item 1; `notes/adversarial_review_draft_v2_second_pass_2026-09-15.md`, the recomputation of 1.89)".

### X4
- **Location**: manuscript/si/S3_Text.md, line 118.
- **Quote**: "against the fine central difference −1.7402 quoted in the main text"
- **Problem**: The main text does not quote −1.7402 (or −1.74) anywhere; Results 1 and the Fig 1 caption give the sts values at c = 0, ±0.02, ±0.05, +0.10 instead.
- **Evidence**: grep of draft_v2.md: no "1.74". The value is in the exchange-rate table directly above (S3 line 114, "-1.7402").
- **Fix**: "against the fine central difference −1.7402 of the table above".

### C2
- **Location**: manuscript/si/S3_Text.md, line 124.
- **Quote**: "used for all derivative values quoted in this paper"
- **Problem**: False as written: the paper also quotes derivatives at other points — in the same S3 section ∂sts/∂r₁ = 5.71 and ∂sts/∂q = −0.59 at (0.85, 0.6) (same sentence), ∂sts/∂r₁ = 5.99 at (0.848, 0.24) (line 155) and ∂sts/∂q ≈ −0.15 to −0.23 at r₁ = 0.84 (line 155); and the main text quotes ∂sts/∂r₁ = 32.8 at r₁ = 0.97 (draft_v2.md line 172).
- **Evidence**: S3_Text.md lines 124 and 155; draft_v2.md line 172.
- **Fix**: "used for the exchange rates of the main text's Results 1".

### C3
- **Location**: manuscript/si/S3_Text.md, line 227, against manuscript/draft_v2.md line 59.
- **Quote** (S3): "it gives a residual level of −0.035 (−3.0 %) against the observed −0.049 (−4.3 %)"; (main text): "reproduces most of its level (−0.037 against −0.049 at W = 60)"
- **Problem**: The finite-sample null's W = 60 residual level, set against the same observed −0.049, is −0.035 in S3 Text and −0.037 in the main text. The two come from different configurations of the null: −0.037 is the homogeneous filter fitted to the placebo function, whereas the null the main text's Methods describe (and whose +0.0054 the paper uses), solved to each run × period cell, gives −0.031 to −0.036 (mean −0.0345). Neither place says which configuration it quotes.
- **Evidence**: notes/review_results/logs/review_v2_residual_null.log line 7 ("W= 60: … residual=-0.0373 (-3.10 %)", homogeneous filter) and lines 11–14 (the four cells: −0.0353, −0.0313, −0.0350, −0.0364); draft_v2.md line 224 (the null "solved to its window-level pair r₁ and |q| in each run × period cell"); main_text_numbers.csv row 164 (the −0.037 sourced from log line 7).
- **Fix**: main text line 59: "(−0.035 against −0.049 at W = 60)" (word count unchanged; matches the null as the Methods define it and S3 Text), or keep −0.037 and write in S3 line 227 "a residual level of −0.035 (−3.0 %; −0.037 with the homogeneous filter of the next sentence)".

### C4
- **Location**: manuscript/si/S3_Text.md, line 282, against line 321 of the same file.
- **Quote**: "The filter (band-pass 0.01–0.08 Hz times exp(−βf²))"
- **Problem**: The same null filter (that of `review_v2_residual_null.py`) is described here as a 0.01–0.08 Hz band-pass, but in line 321 as "a smooth 0.0064–0.080 Hz band-pass with 0.004 Hz cosine edges"; the log shows fitted lower edges of 0.0064 Hz (placebo function) and 0.0030 Hz (DMT-post function).
- **Evidence**: S3 line 321; notes/review_results/logs/review_v2_residual_null.log lines 2–3 ("beta=200 lo=0.0064 hi=0.080"; "beta=100 lo=0.0030 hi=0.080"); `bandpassed_expectations_tables.md` line 4 ("filter 0.0064–0.080 Hz").
- **Fix**: "The filter (a band-pass with a fitted lower edge, 0.0064–0.080 Hz for the placebo function and 0.0030–0.080 Hz for the DMT-post function, times exp(−βf²))".

### C5
- **Location**: manuscript/si/S3_Text.md, lines 278, 279 and 280.
- **Quote**: "(2) symmetric VAR(1), population a = 0.8632, c_xy = +0.02, c_yx = −0.02" (and the same with ±0.04, ±0.06)
- **Problem**: A VAR(1) with c_xy = +c and c_yx = −c is the antisymmetric (directed) coupling, not the "symmetric VAR(1)" that S3 §3 and Fig 1c define (x_{t+1} = a x_t + c y_t + ε, y_{t+1} = a y_t + c x_t + η, one c for both directions). The source file's own summary line calls these rows "antisymmetric VAR(1)".
- **Evidence**: S3 line 120 (definition of the symmetric VAR(1) pair); notes/review_results/partB/directed_crosslag_tables.md line 42: "antisymmetric VAR(1) c = 0.02: -0.07353, c = 0.04: -0.07253, c = 0.06: -0.06842".
- **Fix**: "(2) antisymmetric VAR(1), population a = 0.8632, …" in each of the three rows.

### C6
- **Location**: manuscript/si/S3_Text.md, line 418.
- **Quote**: "On two further matched pairs, whose analytic sts is 0.094 nats"
- **Problem**: The pairs described (the asymmetric VAR(1) pairs, W = 60 −9 % and +16 %) are not further pairs: they are F1-i and F1-ii, already listed in the preceding sentence (−9 % (F1-i), +16 % (F1-ii)). "Further" implies six matched pairs, whereas S3 line 225, S16 Table and the main text's Methods all have four.
- **Evidence**: S3 line 418 first sentence; S16 Table (supplementary.md lines 369–372: four rows, the first two −9 %/+2 % and +16 %/+1 %); draft_v2.md line 228 ("four matched pairs").
- **Fix**: "On the first two of these pairs (F1-i and F1-ii), whose analytic sts is 0.094 nats".

### T2
- **Location**: manuscript/si/S3_Text.md, 153 lines: 13, 15–20, 22–29, 31, 33–34, 49–50, 52, 54, 56–57, 59–60, 66–67, 69, 71, 73–74, 76, 113–116, 133, 138, 140, 142, 144, 150–151, 187–196, 199–202, 206–215, 251–270, 276–280, 299–319, 325–345, 357–359, 373–374, 376, 378–379, 381–387, 389–390, 412 (583 occurrences).
- **Quote** (example, line 13): "| rtr | +0.0444 | +0.0593 | -0.0149 | +0.0005 (8) | +0.0030 (8) | -0.0025 (8) |"
- **Problem**: Negative numbers are written with the ASCII hyphen-minus instead of the minus sign U+2212 used everywhere else (main text, captions, S1, S2, S4, S5 Text have none). In 41 of these lines both signs occur in one row, e.g. line 187 "| -0.0809 | … | [−0.1317, −0.0310] |".
- **Evidence**: regex `(^|[ (\[|;,/:=])-[0-9]`; zero matches in draft_v2.md, captions_v2.md, S1, S2, S4, S5.
- **Fix**: replace "-" by "−" before digits in the listed lines (a mechanical substitution; no value changes).

### U2
- **Location**: manuscript/si/S3_Text.md, line 414, against manuscript/draft_v2.md line 152.
- **Quote**: "The AR(1) residual keeps 99.6 % of its power in band and r₁ = 0.76"
- **Problem**: The main text gives the AR(1) residuals' r₁ as 0.75, S3 as 0.76. Both match the table above (run-level +0.7572, W = 60 +0.7506), but neither sentence says which r₁ it is, so the same quantity reads as two values.
- **Evidence**: S3 line 399: "| ar1 | 0.996 (0.001) | 0.001 (0.000) | 0.003 (0.001) | +0.7572 (0.0055) | +0.7506 (0.0107) | 839.0 |".
- **Fix** (if wanted): "and a run-level r₁ = 0.76".

## 4d. manuscript/si/S4_Text.md

### C7
- **Location**: manuscript/si/S4_Text.md, line 62 (item R1).
- **Quote**: "Every contrast is given as a mean DiD with an inverted sign-flip 95 % interval and exact p (Tables 1–3; Results 2–6)."
- **Problem**: Table 1 gives its 48 DiDs with the count of negative subjects only, with no interval and no p, so the statement is false for one of the three tables it cites (and Table 3's generator rows carry ± replicate SD or SE, not intervals).
- **Evidence**: draft_v2.md lines 63–81 (Table 1: "−0.0809 (13)" etc.); Table 1 caption line 61 ("in brackets the number of subjects with a negative DiD").
- **Fix**: "Every contrast of the data is given as a mean DiD with an inverted sign-flip 95 % interval and exact p (Tables 2 and 3; Results 2–6), except the atom DiDs of Table 1, which carry the number of negative subjects."

### U3
- **Location**: manuscript/si/S4_Text.md, line 64 (item R3).
- **Quote**: "negative-of-14 counts in every table"
- **Problem**: Table 3 carries no negative-of-14 counts (its data rows give intervals only), so "every table" does not hold for the main-text tables; it holds for Tables 1 and 2 and many S Tables.
- **Evidence**: draft_v2.md lines 124–125 (Table 3 data rows).
- **Fix** (if meant literally): "negative-of-14 counts in Tables 1 and 2 and the S Tables".

### T3
- **Location**: manuscript/si/S4_Text.md line 27 and manuscript/supplementary.md line 378, against draft_v2.md lines 358 and 378, S1_Text.md line 17 (twice), supplementary.md lines 113 and 1580 (twice).
- **Quote**: "an HRF-convolved EEG Lempel–Ziv regressor" (S4) and "S6 Table's Lempel–Ziv correlations" (supplementary.md)
- **Problem**: The same name is spelled with an en dash in these two places and with a hyphen ("Lempel-Ziv") in the other seven, including the S6 Table title and its caption in the paper.
- **Evidence**: grep "Lempel.Ziv" over the material.
- **Fix**: "an HRF-convolved EEG Lempel-Ziv regressor" and "S6 Table's Lempel-Ziv correlations" (or en dash everywhere).

No other error found in S4 Text: every section and S-item location it names was checked (S3 Text §3–§6, S5 Text §2, S1 Text, S10/S16/S17/S19 Table, Table 2) and points to what it claims; the quotations of the main text in D2, D4 and Sh6 are verbatim.

## 4e. manuscript/si/S5_Text.md

### T4
- **Location**: manuscript/si/S5_Text.md, line 27 (§5).
- **Quote**: "The reference list was checked as follows. Every entry except the software was read in full (main article; supplementary materials only where named) on 20 September 2026"
- **Problem**: A whole passage is doubled: from "The reference list was checked as follows." to "…on 15, 17 and 20 September 2026." the paragraph repeats, almost word for word, the three sentences that immediately precede it ("The reference list itself was audited in that citation audit (…): every entry except the software was read in full … Theiler et al. (1992) against its bibliographic record only (…). Bibliographic details were checked against Crossref … on 15 September 2026 (…), Tarchi et al. (2026) on 17 September (…) and the entries added on 20 September on that day (audit, §6).").
- **Evidence**: S5_Text.md line 27: "every entry except the software was read in full" occurs twice (case-insensitive), with the same list of seven exceptions both times.
- **Fix**: delete the second copy, i.e. the text from "The reference list was checked as follows." through "the preprint server on 15, 17 and 20 September 2026." inclusive.

### X5
- **Location**: manuscript/si/S5_Text.md, line 7 (§1).
- **Quote**: "to within-subject bands on Figure 4 and to Figure 5"
- **Problem**: These are the figure numbers of the drafts of 15 September, not of this paper: there, Figure 4 was the residual-by-window figure (now Fig 5) and Figure 5 the lag-dependence figure (now Fig 6). In this paper Fig 4 is the regional map, which has no within-subject bands. Elsewhere S5/S3 qualify old numbers ("Table 5 of the drafts of 21–22 September", "the former Fig 3c (of the drafts of 21–23 September 2026)").
- **Evidence**: analysis_record.md, correction note of 15 Sep 2026 10:05 UTC and following entries (record line ≈2677: "Figure 4 bands are now within-subject SEMs; a Figure 5, the lag dependence of Table 5, is added"); draft_v2.md line 110 (Fig 4 = regional map) and line 116 (Fig 5 bands).
- **Fix**: "to within-subject bands on Figure 4 of the drafts of that day (now Fig 5) and to their Figure 5 (now Fig 6)".

### T5 (process labels)
- **Location**: manuscript/si/S5_Text.md line 19 and line 27 (three times); manuscript/supplementary.md line 339.
- **Quote**: S5 line 19: "record, 'Stage B of round 16: the shortened text', 23 September 2026"; S5 line 27: "(record, \"Round 14: the restructuring\")", "(record, \"Stage B of round 16: the shortened text\", 23 September 2026)", "(record, 'Round 17')"; supplementary.md line 339: "(record, 'Stage B of round 16: the shortened text', 23 September 2026)"
- **Problem**: Process labels ("round 14", "Stage B of round 16", "Round 17") appear in manuscript files, which the brief excludes; elsewhere these revisions are given dated descriptions ("the restructuring of 21 September 2026", "the revision of 23 September 2026"). In addition, 'Round 17' is not the title of a record heading (the heading is "Round 17: the review of 24 September 2026 applied (25 Sep 2026)").
- **Evidence**: grep of the material for round/stage; analysis_record.md headings at lines 5297, 6571, 6733.
- **Fix**: cite the entries by date and time, as S3 does for B22: "record, the entry of 21 September 2026, 15:12 UTC, on the restructuring"; "record, the entry of 23 September 2026, 21:40 UTC, on the shortened text" (S5 lines 19 and 27, supplementary.md line 339); "record, the entry of 25 September 2026, 16:34 UTC, on the revision".

No other error found in S5 Text. Checked: every commit identifier of §1, §4 and §6 resolves in `git log` with the stated date/time (EEST/UTC conversions correct; 10:29 − 10:12 = 17 min); the -dirty and nogit inventory of §4 matches the headers of `results/` and `notes/review_results/` exactly (9 + 2 + 3 files; 5 nogit + review_checks.log); the B21–B24 run (8 min 52 s = 172 + 73 + 59 + 227 s; 1,120 checks = 1,025 + 22 + 63 + 10; 13 outputs with `git=a9d9ca4`); the review tallies (44 = 24 + 2 + 16 + 2 + 0; 119 = 87 + 21 + 6 + 1 + 4; 21 = 9 + 8 + 4; 20 = 16 + 2 + 2; 111 = 88 + 6 + 4 + 0 + 13; 15 = 13 + 2; 44 = 38 + 5 + 1); the multiplicity paragraph (474 = 79 × 6 = 186 + 288; 316 = 79 × 4; 158 = 79 × 2); the seven reference exceptions; every record title quoted (all others match a heading).

### T6
- **Location**: manuscript/si/S1_Text.md line 19; S3_Text.md lines 155 and 227; S5_Text.md line 3; supplementary.md lines 142 (S8 Table heading) and 144.
- **Quote**: supplementary.md line 142: "## S8 Table. Post-hoc proportionality: sts / TDMI ratio DiD, four cells"
- **Problem**: "post hoc" is spelled unhyphenated in all 7 occurrences of the main text (including the S8 Table caption "Post hoc proportionality") and in 21 places of the SI, but hyphenated ("post-hoc", "Post-hoc") in these six places, so the S8 Table's own title differs from its caption.
- **Evidence**: grep "[Pp]ost-hoc" over the material.
- **Fix**: "Post hoc" / "post hoc" in the six places (S8 heading: "## S8 Table. Post hoc proportionality: sts / TDMI ratio DiD, four cells").

## 4c (continued). manuscript/si/S3_Text.md: pointers to the main text (found while checking every "main text, …" pointer of the SI)

### X6
- **Location**: manuscript/si/S3_Text.md, line 272.
- **Quote**: "the residual's DiD sits in its symmetric part (main text, Results 4)"
- **Problem**: The main text's Results 4 no longer says this: the directed/symmetric split was moved from Results 4 into this very section of S3 Text on 25 September 2026 (heading at S3 line 239), and draft_v2.md contains no "symmetric part".
- **Evidence**: grep of draft_v2.md for "symmetric part"/"sits in": no match; S3 line 239 heading "(moved from the main text's Results 4 on 25 September 2026)"; the statement itself is at S3 line 245.
- **Fix**: "the residual's DiD sits in its symmetric part (above)".

### X7
- **Location**: manuscript/si/S3_Text.md, line 418.
- **Quote**: "(main text, Results 2; S8 Table: +0.0204 [+0.0032, +0.0380], p = 0.025)"
- **Problem**: Cited as a source for "the global fit on `ts_gsr` is the one cell of four in which sts fell less than proportionally to TDMI", but Results 2 says only "S8 Table gives a post hoc check of the ratio sts / TDMI." (draft_v2.md line 102); it does not state the cell or its value.
- **Evidence**: draft_v2.md line 102; the only other main-text mention of S8 is its caption (line 382).
- **Fix**: "(S8 Table: +0.0204 [+0.0032, +0.0380], p = 0.025)".

### U4
- **Location**: manuscript/si/S3_Text.md, line 155.
- **Quote**: "(a post hoc quantity; main text, Methods)"
- **Problem**: The main text's Methods does not call the whole-brain lag-1 autocorrelation a post hoc quantity (it says only that every quantity but the primary contrast is exploratory, line 220, and that S19 Table lists the post hoc computations, line 240); the post hoc status is stated in S19 Table, Part B (first row).
- **Evidence**: grep "post hoc" in draft_v2.md: lines 29, 102, 236, 240, 360, 404 only (and line 382, the S8 Table caption "Post hoc proportionality").
- **Fix** (if confirmed): "(a post hoc quantity; S19 Table, Part B)".

## 5. manuscript/supplementary.md (S1–S20 Table)

### N3
- **Location**: manuscript/supplementary.md, line 276 (S11 Table).
- **Quote**: "| AR(1) | ts_gsr | global fit | CCS-sts (`phyid`'s mask) | −0.0298 | +0.0134 [+0.0077, +0.0192] | 0.0005 | 1 |"
- **Problem**: The column is the inverted sign-flip interval, whose upper limit is +0.019252 and rounds to +0.0193; the printed +0.0192 is the t interval's upper limit (+0.019220). It is the only S11 interval that does not match its inverted interval.
- **Evidence**: notes/review_results/partB/inference_revision.csv line 549: inv_lo 0.0077421797869445955, inv_hi 0.01925213221907061 (t_hi 0.019219545831741142); S17 Table row (supplementary.md) "[+0.00774, +0.01925]".
- **Fix**: "+0.0134 [+0.0077, +0.0193]".

### X8
- **Location**: manuscript/supplementary.md, line 153 (S8 Table note).
- **Quote**: "from 25 September 2026 Results 2 cites this table and gives the one cell whose interval excludes zero without the rule's labels"
- **Problem**: Results 2 cites S8 Table but does not give any cell: its only sentence on the check is "S8 Table gives a post hoc check of the ratio sts / TDMI." S19 Table, Part B, correctly says "Results 2 (S8 Table cited)".
- **Evidence**: draft_v2.md line 102; supplementary.md line 1646.
- **Fix**: "from 25 September 2026 Results 2 only cites this table, without the rule's labels".

### C8
- **Location**: manuscript/supplementary.md, line 1578 (S19 Table), against manuscript/si/S1_Text.md line 13.
- **Quote** (S19): "rtr fell with sts (DiD −0.0091, positive in 4 of 14; r = 0.66 between the two time courses)"; (S1 Text): "on ts_gsr rtr fell with sts (DiD −0.0078, positive in 4 of 14 subjects)"
- **Problem**: The outcome of the same recorded prediction (the redundancy prediction) is given as −0.0091 in S19 Table and −0.0078 in S1 Text, with no estimator named in either. −0.0091 is the record's value (global fit, peak bins 9–14); −0.0078 is the W = 60 primary DiD of Table 1. S1 Text also attributes its figure to the record (84ea657), which holds −0.0091.
- **Evidence**: analysis_record.md lines 1181 and 1227–1229 ("DiD −0.0091 … positive DiD in only 4 of 14"); draft_v2.md line 65 (Table 1: rtr observed DiD −0.0078 (10)).
- **Fix**: S1 Text: "(DiD −0.0078 at W = 60; −0.0091 at the global fit over bins 9–14 as recorded; positive in 4 of 14 subjects)"; or S19: "(DiD −0.0091 at the global fit over bins 9–14; −0.0078 at W = 60; positive in 4 of 14; …)".

### C9
- **Location**: manuscript/supplementary.md, line 1582 (S19 Table, row B2).
- **Quote**: "CCS-sts small (\|level\| ≤ 0.04 nats)"
- **Problem**: Under the published definition, which the paper uses for every CCS value outside S11 Table, the CCS-sts level is −0.0480 on ts_gsr at W = 60 (main text Results 6: "−0.048 nats"), so |level| ≤ 0.04 is false. The bound holds only for `phyid`'s mask, which the 14 September outcome used.
- **Evidence**: draft_v2.md line 146; ccs_pub_tables.md lines 28, 58, 85, 115 (published levels −0.0480, −0.0358, −0.0378, −0.0386; `phyid` −0.0387, −0.0335, −0.0255, −0.0297); notes/partB2_ccs.md line 28 (the 14 Sep outcome, `phyid`'s mask).
- **Fix**: "CCS-sts small (\|level\| ≤ 0.04 nats under `phyid`'s mask, as recorded; ≤ 0.05 under the published definition)".

### C10
- **Location**: manuscript/supplementary.md, lines 1587 and 1589 (S19 Table), against supplementary.md lines 161 and 187 (S9 Table) and S3_Text.md line 235.
- **Quote**: line 1587: "ts_gsr +0.00009 [+0.00005, +0.00013], p = 0.0004"; line 1589: "+0.00340 [+0.00300, +0.00380], 14 of 14"
- **Problem**: These are the committed subject-bootstrap percentile intervals, printed without the "percentile" mark that the file's header convention (line 3) requires and that row B4 (line 1584) uses; the same quantities carry their inverted intervals elsewhere in the SI: [+0.00004, +0.00014] (S9 Table note, line 187) and [+0.00294, +0.00386] (S9 Table line 161; S3 Text line 235). So one quantity has two intervals with no stated reason.
- **Evidence**: S17 Table rows 777 and 833 (supplementary.md lines 1158 and 1214): percentile [+0.00005, +0.00013] / inverted [+0.00004, +0.00014]; percentile [+0.00300, +0.00380] / inverted [+0.00294, +0.00386].
- **Fix**: "ts_gsr +0.00009 [+0.00004, +0.00014], p = 0.0004" and "+0.00340 [+0.00294, +0.00386], 14 of 14" (or add "(percentile; inverted […])" as in row B4). The same unmarked-percentile issue applies to line 1580 ("ρ_S = −0.242 [−0.401, −0.076]", percentile in S6 Table and S1 Text) and line 1581 ("−0.0047 [−0.0079, −0.0013]", a bootstrap interval from the closure entry); add "(percentile)" there.

### T7
- **Location**: manuscript/supplementary.md, 147 lines: 196–216, 222–242, 248–250, 305, 1328, 1330, 1332–1338, 1340–1342, 1344–1346, 1352–1355, 1357, 1361–1364, 1373, 1375, 1377–1383, 1385–1387, 1389–1391, 1397–1400, 1402, 1406–1409, 1417, 1421–1431, 1440–1454, 1456, 1503–1504, 1510, 1513, 1515, 1520–1521, 1523, 1525–1527, 1536–1537, 1545–1547, 1553–1560, 1562 (300 occurrences; S10, S11, S18 Tables).
- **Quote** (example, line 196): "| (i) Δa = −0.015, Δc = 0 | W60 | 0.7152 | -0.0422 ± 0.0034 | -0.0471 ± 0.0036 | +0.0049 ± 0.0017 | 0.056; 0.82 | +0.00014 ± 0.00065 | +0.00130 ± 0.00050 |"
- **Problem**: As T2: ASCII hyphen-minus used as the minus sign in numbers; the other tables of this file (S1–S9, S12–S17, S19, S20) use U+2212; 27 lines mix both (e.g. line 196: "Δa = −0.015" and "-0.0422").
- **Evidence**: regex `(^|[ (\[|;,/:=])-[0-9]`.
- **Fix**: replace "-" by "−" before digits in the listed lines.

### U5
- **Location**: manuscript/supplementary.md, line 157 (S9 Table source note).
- **Quote**: "both at git 6b5181a, seed 20261120"
- **Problem**: The two cited files now carry `git=d507728` in their headers (they were regenerated in the section-6 verification run of 20 September and committed as a75d015, identical apart from the SHA line); 6b5181a is where the budget was first computed. A reader checking the header finds a different SHA. The same holds for "`crosslag_deviation_tables.md`, sections A and B at git 9a19b10" (line 185; header `git=d507728`).
- **Evidence**: head of notes/review_results/partB/crosslag_budget_tables.md, crosslag_budget_null_tables.md, crosslag_deviation_tables.md: "git=d507728"; `git log` of those files: d51966e, then a75d015.
- **Fix** (if wanted): "first computed at 6b5181a (headers: d507728, the regeneration of 20 September 2026)".

No other error found in supplementary.md. S19 Part A was tallied row by row: 58 rows = 25 met + 13 partly met + 14 missed (52 predictions) + 6 rule/mapping/no-prediction rows, matching the closing sentence (line 1631), the main text (line 240) and CLAUDE.md. All 932 S17 rows were compared programmatically with notes/review_results/partB/inference_revision.csv (mean, exact and committed p, the three intervals, width ratio, zero-inclusion flags, "changes" flags, negative/14): 0 mismatches; 39 "changes" rows as stated.

### U6 (main text, found while checking Table 3 against S18)
- **Location**: manuscript/draft_v2.md, line 118 (Results 4).
- **Quote**: "In simulations with a fall of about 0.015 in pair r₁ applied to the DMT run only"
- **Problem**: 0.015 is the population fall of the coefficient (Δa = −0.015); the window-level fall of pair r₁ (the quantity the paper calls pair r₁) is 0.0154 on the band-passed generator but 0.0124 on AR(1) pairs, and the same paragraph's "−0.39" for AR(1) pairs is computed with 0.0124. "about 0.015" is therefore not right for one of the two generators it covers.
- **Evidence**: Table 3 rows 3–4 (draft_v2.md lines 126–127): "−0.01540 ± 0.00035", "−0.01243 ± 0.00101"; S18 Table (e), line 1504.
- **Fix** (if confirmed): "In simulations with a fall of 0.015 in the autocorrelation coefficient applied to the DMT run only" (word count +1).

## 6. Cross-reference findings from the exhaustive pass over the main text's S-item pointers and the citations

### X9
- **Location**: manuscript/draft_v2.md, line 136 (Results 4).
- **Quote**: "so it neither explains the excess nor excludes aligned structure as its source (S3 Text; S9 Table)"
- **Problem**: S9 Table (the cross-lag budget: data, finite-sample null, controls, superseded values) contains nothing on A_other, its DiD, its band-passed expectation or the conversions this sentence reports. Those are in S3 Text §6 (the B22 table and the conversion paragraph) and S18 Table (B24's expectations, "B22's statistics under a pure autocorrelation change", and B23 (b)'s conversions). This is the main text's only citation of S9 Table.
- **Evidence**: supplementary.md lines 155–194 (S9 Table, no A_other); lines 1549–1560 (S18 Table, A_other +0.00001 ± 0.00031) and lines 1421–1431 (B23 (b) conversions); S3_Text.md lines 247–272.
- **Fix**: "(S3 Text §6; S18 Table)" (word count unchanged). If S9 Table must still be cited somewhere in the main text, that is a separate matter; it is listed in the Supporting-information captions.

### X10
- **Location**: manuscript/supplementary.md, lines 1662 and 1676 (S20 Table, row 5 and Table B item 3); also line 1667 (row 10).
- **Quote**: "The companion preprint on anaesthetised dynamics across the same species (Luppi et al. 2025 bioRxiv, hctsa; Table B item 3)" and "Luppi et al. 2025 bioRxiv 2025.03.22.644729"; line 1667: "(data from Varley et al. 2023 Comm Biol"
- **Problem**: Author–year citations with no reference-list entry: the reference list has Luppi et al. 2022, 2023, 2024 and 2026 but no 2025 work, and Varley only for 2024. Luppi et al. 2025 is used as a source for the direction of the autocorrelation change under anaesthesia ("from the sources read"); S20 Table has no reference list of its own (unlike S4 Text for Nichols et al. 2017).
- **Evidence**: draft_v2.md References (lines 308–314: Luppi 2022, 2023, 2024, 2026; line 340: Varley 2024 only).
- **Fix**: give S20 Table its own short reference note, as S4 Text does for Nichols et al. (2017), with entries for Luppi et al. (2025, bioRxiv 2025.03.22.644729) and Varley et al. (2023, *Communications Biology*); adding them to the main reference list instead would create entries not cited in the main text. (Menesse 2024 and Mediano 2022 on line 1667 are names Varley's note lists, not works this paper cites; they need no entry.)

### T8
- **Location**: manuscript/si/S3_Text.md, line 227 (twice) and line 282.
- **Quote**: line 227: "the residual is more negative where pair a and |q| are higher (R² = 0.74 on pair a, pair |q| and the cross-lag scatter)"; line 282: "so that the window-level mean pair a and |q| equal the four run × period cells"
- **Problem**: "pair a" is the withdrawn pair-level-a notation for what the paper calls pair r₁ (the mean of a pair's two lag-1 correlations in a window); everywhere else the SI and main text write "pair r₁" (e.g. S3 lines 128, 347; Table 3; S13 Table).
- **Evidence**: brief's notation rule; grep "pair a\b": only these three occurrences.
- **Fix**: "where pair r₁ and |q| are higher (R² = 0.74 on pair r₁, pair |q| and the cross-lag scatter)"; "so that the window-level mean pair r₁ and |q| equal the four run × period cells".


## 3 (continued). Figures: second pass over the printed numbers of Fig 4

### N4
- **Location**: manuscript/figures/fig4_v2_regional.png (and the .pdf), panel c, the fourth line of the annotation; the string is made by scripts/15_figures_v2.py line 365.
- **Quote** (figure text): "Vis − Default +0.0088, spin p = 0.31"
- **Problem**: The residual map's visual − default contrast is +0.0087 at four decimals, not +0.0088. The figure takes the table's five-decimal value "+0.00875" and rounds it again to four decimals. Because the binary value of 0.00875 lies just above the tie, Python rounds it up. The caption and S3 Text print +0.00875, which is correct.
- **Evidence**: `notes/review_results/partB/regional_partial.csv` is the input of B22 (e) (heading of aligned_directed_tables.md (e); `notes/partB22_aligned_directed.py` line 295). From the file's values, the network means of `sts_resid_win` give Vis (17 regions) − Default (24 regions) = +0.0087493 exactly, so the correct four-decimal value is +0.0087. SomMot − Default is −0.0096502, so the figure's −0.0097 is right. `aligned_directed_tables.md` line 61 prints "+0.00875". The script parses that string at line 353 (`vd=num(cells[6])`) and prints it with `:+.4f` at line 365, which gives "+0.0088".
- **Fix**: "Vis − Default +0.0087, spin p = 0.31", then re-render Fig 4. Alternatively, print both contrasts at the five decimals of the caption (draft_v2.md line 110: "−0.00965 (spin p 0.2240) and +0.00875 (0.3089)"): "SomMot − Default −0.00965" and "Vis − Default +0.00875". That means changing `:+.4f` to `:+.5f` for `sm` and `vd` in line 365. No text change; no change to the word count.

### T9
- **Location**: manuscript/figures/fig4_v2_regional.png (and the .pdf), panel b, the bar labels; they are made by scripts/15_figures_v2.py line 348.
- **Quote** (figure text): "-0.0202", "-0.0215", "-0.0014"
- **Problem**: The three negative bar labels in panel b use the ASCII hyphen-minus. Every other negative number in the six figures uses the minus sign "−": the axis ticks, the panel c annotation, and Figs 1, 2, 3, 5 and 6.
- **Evidence**: Script line 348 formats the labels as `f"{c[0]:+.4f}"` and `f"{c[1]:+.4f}"` without the script's `um()` helper. The helper's docstring (line 120) reads "Python's formatting writes a hyphen", and lines 364–365 do wrap their text in `um()`. In the PNG, the short dash of "-0.0202" differs visibly from the "−0.005" of the tick labels beside it.
- **Fix**: "−0.0202", "−0.0215", "−0.0014": wrap both f-strings of line 348 in `um()` and re-render Fig 4. No text change.

## 6 (continued). File paths in the main text

### T10
- **Location**: manuscript/draft_v2.md, line 298 (References, the phyid software entry).
- **Quote**: "(merge of pull request #4, 13 March 2026; the commit pinned in `requirements.lock.txt`)"
- **Problem**: This is a repository file path in the main-text file outside the section Data and code availability. The brief lists that as an error. It is the only such path: the other file paths are all in line 246.
- **Evidence**: grep of draft_v2.md for backticked names and file extensions: only lines 246 (Data and code availability) and 298. Line 246 already names the file: "the pinned environment (`requirements.lock.txt`)".
- **Fix**: "(merge of pull request #4, 13 March 2026; the commit of the pinned environment)". This adds 1 word to the reference list and leaves the body's word count unchanged.

## 5 (continued). manuscript/supplementary.md: S16 Table, the ± convention

### U7
- **Location**: manuscript/supplementary.md, lines 370 and 372 (S16 Table), against the table's note at line 365.
- **Quote**: line 370: "| raised noise correlation, autocorrelation re-solved (asymmetric VAR(1)) | +33 % | +16 % | +1 % |"; line 365: "(± is the standard error over those windows where the difference is not distinguishable from zero)"
- **Problem**: The note says a cell carries ± where the difference cannot be told apart from zero. Two 840-sample cells meet that condition but have no ±: F1-ii's +1 % (line 370) and F3-b's +2 % (line 372). Without the ±, a reader takes them as differences that do stand out from zero. The other cells follow the convention. Reported as uncertain: S3 Text line 418 applies the ± convention only to the W = 60 cells, so the note may be meant for W = 30 and 60 only.
- **Evidence**: In `notes/review_results/logs/sts_matched_null_F1.log`, F1-ii at W = 840 is "+0.0006 ± 0.0005 = +1 %", which is 1.2 SE. In `sts_matched_null_F3.log`, F3-b at W = 840 is "+0.0013 ± 0.0013 = +2 %", which is 1.0 SE. The cells without ± are distinguishable: F1-i at W = 840 is +0.0013 ± 0.0006 (2.2 SE), and F2-ii at W = 840 is +0.0236 ± 0.0023. As shares of the real DiD −0.0809, the two missing SEs are 0.6 % and 1.6 %.
- **Fix** (if the note is meant for every column): "+1 % ± 1 %" in line 370 and "+2 % ± 2 %" in line 372. Otherwise, change the note to "(± is the standard error over those windows at W = 30 and 60 where the difference is not distinguishable from zero)".

## Coverage

**Files read in full**, line by line, from the wrapped reading copies. Line numbers in this file are the original line numbers.
- `manuscript/draft_v2.md`: every line, from the title to the Supporting-information captions. This includes Tables 1–3, the six figure captions, the statements and the References.
- `manuscript/figures/captions_v2.md`. Its six caption strings were compared character by character with the paper's captions and are identical.
- `manuscript/si/S1_Text.md`, `S2_Text.md`, `S3_Text.md`, `S4_Text.md` and `S5_Text.md`.
- `manuscript/supplementary.md`:
  - Read line by line: all prose, source notes and tables of S1–S16 Table and S18–S20 Table, and the heading, source paragraph, note and column header of S17 Table.
  - S17 Table's 932 data rows (lines 382–1313) were checked by program, not read by eye. Every numeric cell was compared with `notes/review_results/partB/inference_revision.csv`: 0 mismatches, and 39 "changes" rows, as the note states. The 202 rows that point to a quoting line ("file:line at 90690f4") were checked against those lines at 90690f4: each holds the quoted mean.

**Figures inspected**: all six PNGs:
- `fig1_v2_scope_map`
- `fig2_v2_atoms_observed_substituted`
- `fig3_v2_per_subject`
- `fig4_v2_regional`
- `fig5_v2_residual_diagnostic`
- `fig6_v2_lag_dependence`

For each I compared the panel letters, panel titles, axis labels, legends, annotations and printed values with the captions and the text. For Figs 3 and 4, every printed number was also traced to its string formatting in `scripts/15_figures_v2.py`. The script was read, not run. That trace found N4 and T9. The PDFs were not opened: they come from the same script run as the PNGs.

**SI numbers, and the files they were checked against**
- **S1 Text**:
  - Table 2, S17 Table and S3 Text;
  - `results/primary_b_ts_gsr_win60.csv`, `…_win30.csv` and `primary_b_ts_demean_win60.csv`;
  - `git log` for the commit identifiers and dates;
  - `requirements.lock.txt` for NumPy, SciPy and Matplotlib;
  - the record and the venv for Python 3.12.3.
- **S2 Text**:
  - `notes/review_results/inference_rows_deconv.csv` and `partB/inference_revision_tables.md`;
  - `notes/review_results/logs/phir_baseline_and_slope.log`;
  - `notes/review_computations_2026-09-14.md` §3;
  - the headers of `notes/review_results/deconv/`;
  - the parameters in `notes/rev_deconv.py`.
- **S3 Text**. Rows were compared by program (`rowcheck.py`) as well as by reading. Sources in `notes/review_results/partB/`:
  - `family_atoms_tables.md`, `scope_map_tables.md`, `coupling_map_tables.md`, `exchange_rates_tables.md`;
  - `lag_tables.md`, `directed_crosslag_tables.md`, `diagnostic_alternatives_tables.md` and `.csv`;
  - `aligned_directed_tables.md` (B22, including (e)), `bandpassed_expectations_tables.md`;
  - `calibration_tables.md`, `calibration_filtered_tables.md`;
  - `crosslag_budget_tables.md`, `crosslag_budget_null_tables.md`, `crosslag_deviation_tables.md`;
  - `splithalf_tables.md` and `splithalf_subjects.csv`;
  - `prewhiten_tables.md`, `whitened_spectrum_tables.md`;
  - `regional_partial_tables.md` and `.csv`, `regional_sts_r1_tables.md`;
  - `ccs_pub_tables.md`, `residual_source.log`.

  Other sources:
  - `notes/review_results/logs/review_v2_residual_null.log` and `rev_extra.log`;
  - `notes/review_2026-09-24/checks/derived_r17.out`;
  - `notes/partB1_scope_map.md`, `notes/partB_prespec_2026-09-14.md` and `notes/partB2_ccs.md`;
  - the git history of `captions_v2.md`;
  - the record.
- **S4 Text**: the main text (Tables 1–3; the quotations in D2, D4 and Sh6 are verbatim), S3 Text §3–§6, S5 Text §2, and S10, S16, S17 and S19 Table.
- **S5 Text**:
  - `git log` for every commit identifier, date and time;
  - the `git=`/`-dirty`/`nogit` headers of all files in `results/` and `notes/review_results/`;
  - the B21–B24 run logs for the durations, check counts and output count;
  - the review tallies and the multiplicity arithmetic, recomputed;
  - the seven reference exceptions;
  - the record headings.
- **S1–S20 Table**:
  - S1–S7 Table: `results/primary_b_*.csv`, `regional_analysis_*.csv`, `regional_did_map_*.csv`, `lz_vs_tdmi_ts_gsr.csv`, `global_fc_did_*.csv`, `proportionality.csv` and `synergy_bins_20regions_ts_gsr_global.csv`, and the record.
  - S8 Table: `inference_revision.csv` (the saved ratio rows).
  - S9 Table: the three cross-lag files, by program.
  - S10 Table: the two calibration files, by program.
  - S11 Table (the prewhitening check): `prewhiten_tables.md`, `whitened_spectrum_tables.md` and the inverted intervals in `inference_revision.csv`.
  - S12 Table: `diag_tables.md` (by program) and `inference_revision.csv`.
  - S13 Table: `diagnostic_alternatives_tables.md`, `bandpassed_expectations_tables.md` and the two calibration files.
  - S14 Table: `lag_tables.md`, by program.
  - S15 Table: `inference_revision.csv` (all eight DiD cells) and the B21 (d) Fisher-z rows of `inference_revision_tables.md` (the four correlations).
  - S16 Table: `logs/sts_matched_null_F1.log`, `F2.log` and `F3.log`.
  - S17 Table: as above.
  - S18 Table: `diagnostic_alternatives_tables.md`, `bandpassed_expectations_tables.md` and `aligned_directed_tables.md`, by program.
  - S19 Table: every outcome against the record and the tables it cites. The Part A tally is 58 rows = 25 met + 13 partly met + 14 missed (52 predictions) + 6 rows without a prediction.
  - S20 Table: against the reference list.
- **Quantities that occur in more than one place** (main text, SI, tables, captions, figures): compared while reading, by searching for each recurring value in all material files. This was not an automated cross-index of every number. The main text's own numbers were not re-verified against `main_text_numbers.csv` row by row, as the brief directs. They were checked only where they recur elsewhere or looked wrong on reading.

**Cross-reference classes**

Checked exhaustively:
- The first-citation order of Figs 1–6 and Tables 1–3, and that each caption follows the paragraph of its first citation.
- Every S Table and S Text reference in the main text and the SI:
  - each exists and is listed in the Supporting-information captions;
  - all 25 caption items exist in the SI files;
  - the SI titles were compared with the captions: S3 Text differs (X1). The S Table headings are longer forms of their captions, which is not reported, except S8's spelling (T6).
- Every S Text section (§) reference.
- Every SI pointer to the main text ("main text, Results n / Methods").
- Every record title cited in quotes, against the headings of `analysis_record.md`.
- Every author–year citation in the main text and the SI against the reference list, including years, and every reference entry for a main-text citation.
- Every commit identifier in the SI.
- The main text for computation labels and file paths outside Data and code availability.
- All material files for process labels and "pair a".
- Markdown: cell counts of every table row; balance of brackets, parentheses, quotation marks and emphasis; doubled words.
- Hyphen-minus in numbers, by regex over all material files.
- Spelling variants of recurring terms, by grep: post hoc, Lempel-Ziv, the capitals of ΦID, and r₁/r1.

Checked by sample:
- The section and line locators inside the SI's source notes (for example "section A and B", "(e)", "item 4"). These were checked wherever the number they support was checked, which is most but not all of them.

**Not checked, and why**
- The cited external works. Without web access I could not check their page, table and equation numbers ("their Eq. 5", "his Eqs. 73 and 79–82", "Eq. 12", "Eq. 8", "Appendix, Eq. 5", "Eqs. 4–5 (pp. 19–20)", "Table 1, p. 10"), the quotations from them in S20 Table, or the DOIs and bibliographic details. The paper has no equation references of its own. Within the paper, the external equation numbers are used consistently: Varley 2024 is cited as Eq. 12 in the Introduction, in Results 1 and in S3 Text.
- Anything that needs subject-level data or re-running an analysis, which the brief forbids. Numbers whose committed source holds only the printed precision were checked only at that precision.
- The ASCII text labels in S17 Table's quantity column. They are the CSV's machine labels, for example "bins 15-28" and "post - pre", and were not treated as prose.
