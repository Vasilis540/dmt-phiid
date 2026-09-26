# Verification of the error-only check of 25 September 2026

The text checked is the repository at ddae618 (the figures of the revision of 25 September 2026, regenerated at
7470eae): `manuscript/draft_v2.md`, `manuscript/figures/captions_v2.md` and the six figures, S1–S5 Text and
`manuscript/supplementary.md` (S1–S20 Table). Two reads were made of it on 25 September 2026, both restricted to
outright errors (the analysis, the interpretation and the wording choices being frozen):

- **the check** (`findings.md`), by a separate session of the AI system under the brief in `BRIEF.md`: text errors (T),
  numbers (N), cross-references (X), contradictions (C) and uncertain items (U), each with its location, a verbatim
  quote, the evidence and a proposed fix;
- **an end-to-end read** by the session that verified the check, of the same files in the same order, with a
  mechanical check of `manuscript/main_text_numbers.csv` (`checks/check_numbers.py`, `checks/check_cells.py`).

Every finding of both was verified here against the committed files; neither read, nor this verification, ran any
analysis on the data. The verdicts: of the check's 41 findings (10 T, 4 N, 10 X, 10 C, 7 U), 40 are confirmed and 1
partly (T5); the read found 24 errors of its own (V1–V24), and 37 more were found in preparing the revision and the
final run of `run_all.sh` (V25–V61), 18 of them (V35–V52) by an audit of the prepared revision by two further
sessions and 7 (V55–V61) by a second audit, of the corrections, by a third (section 3). Section 5 lists what was
judged not to be an error, with the reason. Every confirmed item is applied in the error-only revision (record, "The
error-only revision: the check of 25 September 2026 applied"); section 6 gives the checks run on the revised files.

## 1. The check's findings

| ID | where | verdict | the fix applied |
|---|---|---|---|
| N1 | Fig 2 caption | confirmed: the mirror atoms' residual levels are +0.0389 (yts) to +0.0400 (stx), not +0.0395 to +0.0400 (`family_atoms_tables.md`, lines 17, 21, 23, 24) | "+0.0389 to +0.0400", computed in the figure script as the minimum and maximum over the four mirror atoms |
| N2 | Fig 2 caption | confirmed: the cross-prediction residuals are ±0.0230 to ±0.0231 and the substituted levels ±0.0024 to ±0.0027 (lines 11–19) | both ranges written, computed in the script over the six atoms |
| C1 | Results 6 | confirmed: +6.09 is the central difference of the CCS fits (`diagnostic_alternatives_tables.md`, line 144), where Results 1 and 3 give the family's derivative +6.0705 (`exchange_rates_tables.md`, line 8) | "+6.07" |
| T1 | Introduction, first sentence | confirmed: "Integrated Information Decomposition" against the lower case of the title, abstract and author summary | "Integrated information decomposition" |
| U1 | Fig 6 caption | confirmed as an error: at τ = 5 the autocorrelation contrast is −0.0108, not "near zero", and "negative (τ = 1, 2, 3)" misstates the contrast at τ = 5; what distinguishes τ = 5 is that both intervals include zero (p = 0.5670 and 0.3688, `lag_tables.md`, line 14) | the sentence restated through the intervals and the two exact p values, computed from the pickle in the script, with an assertion that the stated pattern holds |
| X1 | S3 Text, heading | confirmed | "The supporting analyses of the estimator account", as its caption |
| X2 | S3 Text §4 | confirmed: the record has no entry "Part B, item 1"; B1 is pre-specified in `notes/partB_prespec_2026-09-14.md` ("## B1. Scope map (no prediction)") | "(pre-specified as B1, with no prediction, in `notes/partB_prespec_2026-09-14.md`)" |
| X3 | S3 Text §4 | confirmed: the current captions file holds neither ratio minimum; the captions generated at 48ea934 held both (in the repository from 17 to 23 September 2026), and 6.55 is in `notes/partB1_scope_map.md`, item 2 (not item 1, as the check proposed) | "(the scope-map caption of `manuscript/figures/captions_v2.md` as generated at 48ea934; 6.55 also in `notes/partB1_scope_map.md`, item 2)" |
| X4 | S3 Text §3 | confirmed: the main text no longer quotes −1.7402 | "of the table above" |
| C2 | S3 Text §4 | confirmed: derivatives are also quoted at (0.85, 0.6), (0.848, 0.24) and r₁ = 0.97, each with its point named | "used for the derivative values quoted in this paper unless another point is named" (the check's wording would have narrowed the statement to Results 1) |
| C3 | Results 1; S3 Text §6 | confirmed: −0.037 is the null with one filter at one operating point (`review_v2_residual_null.log`, line 7), −0.035 the mean of the null of Methods, solved to each run × period cell (lines 11–14); the observed −0.049 is the mean over all 392 cells (`residual_source.log`, line 4), where Table 1's −0.0530 is one cell (V9) | both places now compare cell with cell: the null's −0.031 to −0.036 against the data's −0.045 to −0.053 in the four run × period cells (`residual_source.log`, line 6); S3 Text adds the percentages and the all-cells mean, and labels the single-filter values as such |
| C4 | S3 Text §6 | confirmed: the null's filter has a fitted lower edge, 0.0064 Hz (placebo function) and 0.0030 Hz (DMT post), not 0.01 Hz (log, lines 2–3) | both edges written |
| C5 | S3 Text §6 | confirmed: c_xy = +c, c_yx = −c is the antisymmetric VAR(1) (`directed_crosslag_tables.md`, line 42) | "antisymmetric" in the three rows |
| C6 | S3 Text §9 | confirmed: the "two further matched pairs" are F1-i and F1-ii of the preceding sentence | rewritten as the first two of those pairs, with U7's ± on the 840-sample value |
| T2 | S3 Text | confirmed: 583 negative numbers written with the ASCII hyphen-minus | replaced by U+2212 by the rule `(?<=[\s|(\[,;/=])-(?=\d)`; the replacement changes those 583 characters and no other |
| U2 | S3 Text §8 | confirmed as an error of labelling: 0.76 is the run-level r₁, 0.75 (Results 7) the W = 60 value (the table above it: +0.7572, +0.7506) | "a run-level r₁ of 0.76 (0.75 at W = 60)" |
| C7 | S4 Text, R1 | confirmed and wider than reported: Table 1 carries sign counts, Table 3's data rows intervals without p, and the text gives the pair r₁ and pair \|q\| DiDs as point values and the regional contrast of Results 3 with t intervals (their per-subject values were not saved) | R1 restated with those exceptions named |
| U3 | S4 Text, R3 | confirmed: Table 3 has no negative-of-14 counts | "in Tables 1 and 2 and in S17 Table" |
| T3 | S1, S4 Text; SI captions; S6 and S19 Table | confirmed | "Lempel–Ziv" (en dash, as "Benjamini–Hochberg") in all nine places |
| T4 | S5 Text §5 | confirmed: the reference-list passage stands twice (the second copy was added in the revision of 25 September) | the second copy deleted |
| X5 | S5 Text §1 | confirmed: "Figure 4" and "Figure 5" are the numbers of the drafts of 15 September (record, correction note of that day) | "Figure 4 of the drafts of that day (now Fig 5) and … their Figure 5 (now Fig 6)" |
| T5 | S5 Text §5; S19 Table | partly confirmed: 'Round 17' is not a full record title; the other quoted titles are the record's headings, which a citation must reproduce verbatim for the entry to be found and which the append-only record cannot reword (V49) | the title completed, "Round 17: the review of 24 September 2026 applied"; the others kept |
| T6 | S1, S3, S5 Text; S8 Table | confirmed | "post hoc" in all six places |
| X6 | S3 Text §6 | confirmed: the directed/symmetric statement moved from Results 4 to this section on 25 September | "(above)" |
| X7 | S3 Text §9 | confirmed: Results 2 cites S8 Table without the cell | the pointer to Results 2 removed |
| U4 | S3 Text §4 | confirmed: the post hoc status is stated in S19 Table, Part B (its first row), not in Methods | "(a post hoc quantity; S19 Table, Part B)" |
| N3 | S11 Table | confirmed: the inverted upper limit is +0.019252 (`inference_revision.csv`, line 549); +0.0192 was the t limit | "+0.0193" |
| X8 | S8 Table note | confirmed | "Results 2 only cites this table, without the rule's labels" |
| C8 | S1 Text; S19 Table | confirmed: −0.0091 is the record's value at the global fit, bins 9–14 against 1–8 (record, lines 1181 and 1227–1229); −0.0078 the W = 60 DiD of Table 1 | both values given with their estimators in both places; the ts_demean row of S19 labelled the same way (its −0.081 is also the global fit's, record, line 1263) |
| C9 | S19 Table, B2 | confirmed: under the published definition the level is −0.048 (Results 6) | "\|level\| ≤ 0.04 nats under `phyid`'s mask, as recorded; ≤ 0.05 under the published definition" |
| C10 | S19 Table | confirmed: four intervals printed without the "percentile" mark the file's convention requires | "(percentile; inverted […])" on the two cross-lag rows, as on row B4, and "(percentile)" on the EEG and regional ΦR rows |
| T7 | supplementary.md | confirmed: 300 negative numbers with the ASCII hyphen-minus (S10, S11, S18 Table) | as T2; 300 characters |
| U5 | S9 Table sources | confirmed: the headers carry d507728 (the regeneration of 20 September, a75d015), not 6b5181a or 9a19b10 | "first computed at 6b5181a (their headers carry d507728, …)"; likewise for 9a19b10 |
| U6 | Results 4 | confirmed: 0.015 is the band-passed generator's window-level fall of pair r₁ (−0.01540); the AR(1) generator's is −0.01243 and the null's −0.0146 | "a fall of 0.012–0.015 in pair r₁" (the check's "in the autocorrelation coefficient" would not fit the band-passed generator, whose change is a filter tilt) |
| X9 | Results 4 | confirmed: A_other and its conversions are in S3 Text §6 and S18 Table, not S9 Table | "(S3 Text; S18 Table)"; S9 Table keeps a main-text citation in Limitations, where the symmetric cross-lag departure it budgets is named |
| X10 | S20 Table | confirmed: Luppi et al. (2025) and Varley et al. (2023) have no reference entry | a reference note for S20 Table, as S4 Text has for Nichols et al. (2017); both records checked against Crossref on 25 September 2026, the two Luppi et al. (2025) quotations against its full text (version 1) |
| T8 | S3 Text §6 | confirmed: "pair a" is the withdrawn notation | "pair r₁" in the three places |
| N4 | Fig 4c | confirmed: +0.0088 is a second rounding of +0.00875; the unrounded value is +0.0087493 | both contrasts printed at the caption's five decimals |
| T9 | Fig 4b | confirmed | the bar labels passed through the script's `um()` |
| T10 | References (phyid) | confirmed: a file path outside Data and code availability | "the commit of the pinned environment" |
| U7 | S16 Table | confirmed: the note's ± convention holds for every column; F1-ii at 840 samples is +0.0006 ± 0.0005 and F3-b +0.0013 ± 0.0013 (`sts_matched_null_F1.log`, `…_F3.log`) | "+1 % ± 1 %" and "+2 % ± 2 %"; S3 Text §9 likewise |

## 2. The read's own findings (V1–V24)

| ID | where | the error | the fix applied |
|---|---|---|---|
| V1 | Results, notation | DiD used before it is expanded | "a difference-in-differences (DiD) is …" |
| V2 | Table 2 | FD not defined | "FD, framewise displacement" in the caption |
| V3 | Fig 1 caption | VAR(1) used before it is expanded (Methods expands it) | "first-order vector autoregressive (VAR(1))" |
| V4 | Results 1; Fig 4 and Table 3 captions | SD, SEM and SE not expanded at first use | expanded at first use |
| V5 | Results 2 | "fell … by −0.0146" (a fall by a negative amount) | "changed … by −0.0146" |
| V6 | Methods; S3 Text; S9, S10, S18 Table | N(μ, σ) written with the standard deviation (N(0.85, 0.0125), N(0, 0.266), N(0, 0.3424), N(6β̄, h·6β̄), N(β̄/5, h·β̄/5); `partB17_calibration.py` and the other scripts draw with the SD) | the variance written: 0.0125², 0.266², 0.3424², (h·6β̄)², (h·β̄/5)² |
| V7 | Fig 1 caption | the overlay's r₁ is pair r₁ (`partB1_overlay_points.py`, line 35: the two lag-1 entries of the 4 × 4 matrix), not "the mean of the two regions' within-window lag-1 autocorrelations" | "r₁ = pair r₁, the mean of the pair's two lag-1 correlations in its window's 4 × 4 matrix" |
| V8 | References (Down et al.) | a bare DOI where every other entry gives the URL | the bioRxiv identifier and the DOI URL |
| V9 | Results 1 | the observed −0.049 is the mean over all cells, beside Table 1's −0.0530 (one cell) | with C3 |
| V10 | `main_text_numbers.csv` | two rows name the wrong cell of their source line (the A_other interval's upper end +0.0004 held −0.00037, should be +0.00041, `aligned_directed_tables.md`, line 12; the band-passed A_other SD 0.0003 held −0.00028, should be 0.00031, `bandpassed_expectations_tables.md`, line 29); the text is right | both rows corrected |
| V11 | S2 Text | "window-level r₁" for whole-brain r₁ | "whole-brain r₁" |
| V12 | S3 Text §6 | the reading of the earlier drafts was about the subject-bootstrap interval, [+0.0021, +0.0211]; the text quoted the inverted one | both intervals given, each named |
| V13 | S3 Text §6 | the plan's wording attributed to `partB4_diagnostic.md`, which restates `partB_prespec_2026-09-14.md`, B4 | both files named |
| V14 | S3 Text §10 | "the pair of values the Discussion quotes": the Discussion quotes 32.8 only | "of which the Discussion quotes the first" |
| V15 | S3 Text §7; S13 Table | "regional r₁" for the whole-brain mean (−0.0146) | "whole-brain r₁" (seven places) |
| V16 | S3 Text §10 | "fell … rtr by −0.0078" | "rtr by 0.0078" |
| V17 | S4 Text | "as they stand in the revision of 25 September 2026", which this revision supersedes | "as they stand in this version" |
| V18 | S5 Text §4 | the four attempts of 16–17 September 2026 at the end-to-end run are not recorded there, though the main text sends the reader there for the earlier attempts | one sentence (record, "The attempts at the end-to-end run of `run_all.sh`, 16–18 September 2026"): three at d51966e, one at 0a25aaa, all inside step 2; two within minutes of the lid being closed, two for causes not recorded; the third attempt's log and its two stationary bias tables, identical in every cell to the versions they replaced, committed in 48ea934 |
| V19 | S5 Text §4; S19 Table | "the commission of 20 September", "the commissioned sign": an internal term | "the task description given to that session on 20 September"; "the sign the pre-run entry stated" |
| V20 | S5 Text §6 | the three commits of 25 September (371ccf5, 7470eae, ddae618) are not listed | listed |
| V21 | S1, S3, S6, S8, S10 Table headings | the headings differ in wording from their captions (beyond the longer form the other headings use) | the headings made to read as the captions |
| V22 | S9 Table source | "definitions in Methods": the main text's Methods no longer define the budget terms; S3 Text §6 does | "definitions in S3 Text, section 6" |
| V23 | S19 Table, B3 | the τ = 5 level is above the τ = 3 level because \|r₅\| exceeds \|r₃\| (0.202, 0.139), not because r₅ is negative | the reason corrected |
| V24 | Figs 2, 5, 6 | subscripts printed literally ("a_x", "\|a_x − a_y\|", "r_τ"); Fig 5c's legend over the data (scheduled before the check) | mathtext subscripts; Fig 5c's legend below its axis and the panel's range cut to the data (−0.04 to 0.06, the equal-scale height rule kept); Fig 2's annotation lowered clear of the legend |

## 3. Found in preparing the revision and the final run (V25–V61)

V25–V34 were found by the session that verified the check, in preparing the revision and the final run. V35–V52
were found by an audit of the revision as prepared (its three commits built on a clone of ddae618), made on 25
September 2026 by two further sessions of the AI system under briefs restricted to errors, one reading every
changed passage of the text with its consequences (items A1–A8 of its report), the other the record entries of the
revision and the comparison scripts of the final run (B1–B10, and a note on what it could not check); each was
verified against the files before it was applied, and A5 is in section 5. V53 was found in verifying V40, and V54
in verifying V50. V55–V61 were found by a second audit, made on 26 September 2026 by a third session under a brief
restricted to errors, of the corrections V35–V54 had led to (its items C1–C7); each was verified before it was
applied.

| ID | where | the error | the fix applied |
|---|---|---|---|
| V25 | the figure and table captions | ts_gsr and ts_demean are used before Methods defines them (no Results paragraph uses them) | defined at first use: the Fig 1 caption ("ts_gsr, the variant with global signal regression") and the Table 2 caption (ts_demean) |
| V26 | S19 Table, Part B | "Methods, The AR(1)-substituted estimate": a partial heading | the full heading |
| V27 | supplementary.md, head note | "percentile" defined as the interval of quantities with no saved per-subject vector, while S19 Table also marks recorded percentile intervals of saved quantities | the definition covers both uses |
| V28 | S1 Text; S5 Text; S13 Table | six record titles in single quotes, thirty in double | double quotes throughout |
| V29 | `scripts/15_figures_v2.py` | its SHA test covered the whole tree; at the final run's last step every regenerated output is a modified tracked file, so the captions would have read `-dirty` | the rule of `notes/rev_git.py` (scripts, `notes/*.py` and the record), as the `notes/` writers use it (V51) |
| V30 | `8_binary_compare.py` | the inference-row pickles are lists of dicts, which it compared by their pickled bytes: a difference of 1e-13 in any float would have been reported as a real difference (the section-6 run of 20 September found CSV differences up to 7.9 × 10⁻¹³) | pickles compared element by element under the 1e-9 rule |
| V31 | record, "B21, outcome" | "the final run's `inference_revision.csv` will differ from 90690f4's only by the `np.float64` wrappers" omits the column `quoted_at`, which B21 computes from the manuscript text in the working tree; recomputed from the revised text it is non-empty in 10 rows (202 at 90690f4) | corrected in the final run's pre-run entry; `9_wrapper_compare.py` checks both B21 files against the expected differences |
| V32 | the pass rule of 21 September | it names the logs and, implicitly, the figures, which neither comparison script reads; and it does not list the differences the regeneration of 15–16 September had already shown (the 84 and 2 rows of the AR-shift condition that the non-stationary bias tables gain, the line added by hand to the subject-alignment report) or the same hand-added line in the report's log, which that regeneration did not compare (V50) | `10_logs_figures_compare.py`, for the logs and every tracked image; the known differences listed in the final run's pre-run entry |
| V33 | S17 Table | its last column is B21's `quoted_at` as committed at 90690f4, which the file regenerated at the final commit will no longer hold | the source note says so |
| V34 | `main_text_numbers.csv` | its header carries a process label ("Round 17") | a dated description |
| V35 | Results 7 (A1) | the 840-sample value of F3-b printed "+2 %" without the ± that U7 gave it in S16 Table (+0.0013 ± 0.0013, `sts_matched_null_F3.log`, line 18), beside the ± of the two W = 60 values | "+2 % ± 2 %", with its row in the numbers CSV (± 0.0013 / 0.0809 = 1.6 %) |
| V36 | S3 Text §9 (A2) | "at τ = 5 both are near zero", the reading U1 corrected in the Fig 6 caption only: the autocorrelation contrast is −0.0108, p = 0.5670 (`lag_tables.md`, line 14) | "the intervals of both include zero", with the autocorrelation contrast and its p |
| V37 | S4 Text, R1 (A3) | the in-band spectral centroid of Results 5, a point value with p whose per-subject values were not saved (its interval in S3 Text §9 a subject-bootstrap percentile interval), is missing from the exceptions that C7's fix lists | named among them |
| V38 | Methods, The closed form (A4) | VAR(1) expanded a second time, after V3's expansion at its first use in the Fig 1 caption | "a stable VAR(1)" |
| V39 | record, the entry of the revision (A6) | "each is a disposition of the verification": three replacements only bring the text's account of the reviews and of the final run up to date (Data and code availability: this review folder and the [TK] of the final run's verdicts; S5 Text §4: the comparisons of the pre-run entry), and one adds to T5's fix S5 Text §5's sentence on this check | the entry says so |
| V40 | Fig 3 (A7) | in (a) the index labels of subjects 13 and 5, and of 7 and 12, printed over each other (each pair's points nearly coincide), and those of 2, 6 and 10 beside another subject's point; in (c) subject 2's label on the lines' crossing and subject 11's beside subject 7's point | those labels placed clear of each other and of the other points (`LABEL_AT` in the script; refined in V57) |
| V41 | Introduction (A8) | ΦR expanded twice, in the Introduction's first and third paragraphs (V58) | "reduced ΦR" in the second |
| V42 | pre-run entry, item 7 (B1) | the two global-fit logs of section 2 were said to differ in their header line, reworded at 8554b3d, and in a line added at 98149a9: the header line prints the same text at the global fit; what 8554b3d reworded that they print is line 25, "samples/bin: min=28 max=30 median=30", which the ts_demean log keeps too (committed at 84ea657 and rewritten at 8554b3d with the output of a run made before that commit's change to the line); and item 5's clause for such lines covered only a script changed after its log was committed | item 7 names line 25 and the added line of both logs; item 5's clause covers a log written before a change of its script |
| V43 | `10_logs_figures_compare.py` (B2) | its elapsed-time mask skipped a time followed by "(" (to spare "0.5 min(S_x, S_y)" and "s=(…)") and so missed "compute finished in 526.9s (2.9 ms/pair)": the six logs of `scripts/01_synergy_timecourse.py` would have been reported as changed | a time followed by "(" and a digit is masked |
| V44 | pre-run entry, item 3 (B3) | `notes/review_results/inference_rows_raw.csv`, written without a SHA by `notes/rev_run.py raw` (section 6, outside the deconvolution branch), is missing from the files that carry none | five files listed |
| V45 | the pass rule; `6_committed_compare.py`, `10_logs_figures_compare.py` (B4) | several outputs print, as internal checks, the difference between two computations of the same quantity, below 1e-13 (`family_atoms_tables.md`, `aligned_directed_tables.md`, `ccs_decomposition_tables.md`, `phiid_fast_validate.log` and the logs of the first three); some compare with binaries that the run regenerates on V.S.'s machine while the committed ones come from another build (`diag_series_*_W60.npz`, 3781e00), and the section-6 run of 20 September found such lines changed in its logs; a rule requiring identical text would block the commit on them | a printed number within 1e-9 of its committed value counts as reproduced, the tolerance of the CSV cells (the sign of a printed zero is a case of it) |
| V46 | `6_committed_compare.py`, `10_logs_figures_compare.py` (B5) | changed lines compared as unordered multisets: a file whose lines were only reordered would have passed, and a change of line endings was invisible | lines compared in order; line endings compared |
| V47 | section 4 of this document (B6) | "its 12 flags are all magnitudes stated as falls or distances": one (0.83) is the range 0.680-0.830 of `derived_r17.out`, line 20, which the script reads as −0.830 | section 4 says so |
| V48 | section 6 of this document (B7) | the script and the replacements that made the revision were named but not in the repository | committed in `revision/` |
| V49 | section 1, T5 (B8) | the disposition cited a decision of 24–25 September 2026 allowing record titles in quotation marks: the record's decision entry of that day states no such rule (it was the planning session's instruction to the revision) | the reason restated from the record's form |
| V50 | pre-run entry, item 6 (e); V32 (B9) | "as it did on 15–16 September" for the subject-alignment log: that regeneration compared the tables and reports, not the logs | the statement confined to the report |
| V51 | pre-run entry, item 3; V29; the figure script's comment (B10) | the SHA rule described as one rule for every writer: the `scripts/` writers test `scripts/` and the record only, and B10–B13 carry their own copy of `notes/rev_git.py`'s test | each described as it is |
| V52 | pre-run entry, item 2 (the audit's note) | the conditions omit two that the second attempt of 22 September had (record, the first-attempt entry of 23 September, "The second attempt"): the lid switch set to `ignore`, and the run executed inside the root unit as V.S.'s user (`runuser -u vilalius`), as the B21–B24 run of 23 September also was (record, "B21, outcome") | both stated, as conditions of the second attempt (V55) |
| V53 | Fig 3b (found in verifying V40) | the annotation's second line ran past the right edge of the axes | set at 7.0 pt, inside the axes |
| V54 | `results/run_10_subject_alignment_check.log` (found in verifying V50) | the committed log has an empty line, its line 86, where the report has the row "sts_gsrglobal_PCB FD_PCB -0.090 +0.008 0.0885 1/14", as since its first commit (cab580b); the script prints each line of the report as it adds it (one function, `say`), so the regenerated log will have the row, and a rule asking a log for identical lines would block on it; the logs of sections 0–5 had never been compared with a regeneration | the pre-run entry states the line (item 6 (e)), and the rule for a log asks for every non-blank committed line, in order, and lists the lines the regenerated log adds (item 6 (h); `10_logs_figures_compare.py`) |
| V55 | pre-run entry, item 2 (C1) | as first corrected, the sentence made the second attempt of 22 September the source of every condition listed, including `shutdown` in the inhibitor's list and the charger, which the entry closing the pre-run entry of 21 September added after that attempt; and it gave the B21–B24 run of 23 September a reboot and a lid-switch setting that the record does not state | each condition attributed to its source: those of the second attempt, with the two added on 23 September, which the B21–B24 run had |
| V56 | `10_logs_figures_compare.py` (C2) | it printed at most eight committed lines not reproduced and eight added lines per log, while its docstring, the pre-run entry, the revision's entry and `CLAUDE.md` say that every such line is listed | every such line printed |
| V57 | Fig 3 (C3) | after V40, some labels were still about as near another subject's point as their own (in (a) "7" to subject 11's and "3" to subject 4's; in (c) "12" to subject 7's), and in (c) "11" and "4" sat on a line | each label placed where its own point is the nearest by a factor of at least 1.4, measured on the drawn figure (the two nearly coincident pairs of (a), 13 and 5 and 7 and 12, labelled on opposite sides), with no label over another label or point, and a light white backing under the digits |
| V58 | V41 (C4) | "in consecutive paragraphs": they are the Introduction's first and third | corrected |
| V59 | this folder's README; `revision/apply_replacements.py`; the revision's entry (C5) | every replacement said to name in `why` the item of the verification it applies: the eleven of `CLAUDE.md` and `README.md` are marked as bookkeeping, and the two minus-sign entries carry a regular expression, not an old string | stated as they are |
| V60 | `6_committed_compare.py`, `10_logs_figures_compare.py` (C6) | three edge cases, none present in the committed outputs: lines aligned on exact values could fail a line whose printed number changed by less than 1e-9 when a line was added beside it; two numbers smaller than 1e-9 but of opposite sign (9e-10 and −9e-10) passed although they differ by more than 1e-9; only the count of CRLF was compared, so a change to a lone CR or a lost final newline passed | lines aligned on numbers rounded to six decimals and every aligned pair checked by the 1e-9 rule; the line-ending style (CRLF, lone CR, lone LF, a final newline) compared |
| V61 | the record entry of the check (C7) | a double space | removed |

## 4. The numbers CSV

`manuscript/main_text_numbers.csv` is rebuilt for the revised text: 1,191 rows (1,183 before), 675 of them data rows
(667). New rows: the null's and the data's residual levels by cell (−0.031, −0.036; −0.045, −0.053, replacing −0.037
and −0.049), the two dimensions of "4 × 4" in the Fig 1 caption, the smaller ends of the two Fig 2 ranges (0.0230,
0.0024), the two ends of "0.012–0.015" (data rows, replacing the design row 0.015), the two exact p of the Fig 6
caption (0.57, 0.37), and the ± of V35 (a derived row); +0.0395 becomes +0.0389 and +6.09 +6.07; the two rows of V10
are corrected; the two label rows of the Data and code availability [TK] that named the comparison scripts are
removed; 58 contexts are set or recomputed from the revised text. `checks/check_numbers.py` finds every source line
and every value at its printed precision (12 flags, read and accepted: 11 magnitudes stated as falls or distances,
e.g. "fell by 0.0164", and one range, 0.680-0.830 in `derived_r17.out`, line 20, which it reads as −0.830; V47),
and `checks/check_cells.py` finds every held string denoting the right cell (0 flags). The numeric tokens of the old and
new text differ exactly by these rows, apart from S-item numbers, paths in code spans and the reference list, which
the file does not index.

## 5. Judged not to be errors

- Methods: "without threshold language" beside Results 6's "no cell's sign-flip p is below 0.05" — a description of
  a result, not a threshold verdict.
- Data and code availability: "8 min wall-clock" for a unit that ran 17:31:41–17:40:33 — the run log's own "all
  done in 8 min".
- Literature search: "every cited work except three" — the main text's reference list; Nichols et al. (2017) is cited
  in S4 Text only, with its own entry there.
- Discussion: ∂sts/∂r₁ = 32.8 at an ideal-band-pass r₁ of 0.97 — exact at 0.97 (0.9699 would give 32.65).
- S1 Text "S1–S8 Tables" against the main text's "S1 Text and S1–S7 Tables" — S8 Table belongs to the original
  analysis's supplement and is cited separately in Results 2.
- "COBIDAS checklist: S4 Text" — the checklist's name, expanded in S4 Text.
- Printed "−0.0000" in S10 Table and elsewhere — the source files' own rounding of small negative numbers.
- S3 Table's "q = 0.05" — the FDR level, labelled in its heading.
- S2 Table's note that the sign is negative in every cell, beside the FD row — the FD row is FD's own correlation.
- S3 Text §6 "(W = 60)" beside the global-fit correlations — the sentence names both estimators.
- S3 Text §9 "from +0.97 on the series as printed to three decimals, 0.977 unrounded" — intelligible as written.
- S4 Table's Jaccard indices 0.323 and 0.571 — cortical-only (20/62, 32/56), as its note gives.
- Table 3's row label "(Δa = −0.015)" for the band-passed generator, whose change is a filter tilt solved to a
  window-level fall of 0.0154 — the label names the calibration's condition (i), which S10 Table defines.
- ts_gsr and ts_demean glossed in the Fig 1 and Table 2 captions (V25) and described again in Methods, Dataset (the
  audit, A5) — labels of the two data variants, not abbreviations of terms; Methods is where the variants are defined
  and their roles, primary and sensitivity, assigned.
- S5 Text §4 citing the final run's pre-run entry, which the third commit of this revision appends (the audit, A6) —
  the text is read at the final commit, where the entry stands.
- Candidates of the read dropped on checking: Results 6's "+0.742" (`ccs_pub_tables.md`, line 33); the ratio 4.7
  (4.66, `aligned_directed_tables.md`, line 27); S1 Text's "S3 Text, section 6" for the bias check; S4 Text's
  locations of the VAR(1) bias check, the sts-matched null and the effective sample size; S4 Text's 932 quantities.

## 6. Checks of the revised files (the mock application of 25–26 September 2026)

The revision was applied to a clean clone of ddae618 by `revision/apply_replacements.py` from the 131 verbatim
replacements of `revision/text_replacements_2026-09-25.json` (26 in `draft_v2.md`, 4 in S1, 1 in S2, 27 in S3, 3 in
S4 and 10 in S5 Text, 36 in `supplementary.md`, 24 in the figure script; 142 entries with the 11 of `CLAUDE.md` and
`README.md`), each required to occur the stated number of times, and the results were checked:

- the minus-sign replacement changes exactly 583 characters of S3 Text and 300 of `supplementary.md`, each from
  "-" to "−", and no manuscript file keeps a hyphen-minus before a digit after a space, bracket, bar, comma,
  semicolon, slash, equals sign or colon;
- every table row of every manuscript file has its table's number of cells (`checks/tablecheck.py`);
- Introduction through Methods: 6,984 words with headings, 6,864 without (`checks/wc.py`; 6,972 before); the
  abstract and the author summary are unchanged;
- the figure script, run at the text commit, writes captions equal to the six captions of the text without their
  Source sentences, and a header naming that commit without `-dirty`; the PNG of Fig 1 is byte-identical and its PDF
  differs only in the creation date; Figs 2–6 change as listed in V24, V40, V53, T9 and N4;
- the numbers CSV as in section 4;
- the four comparison scripts of the final run were run on a simulated run at the third commit: every git= SHA of a
  regenerated output rewritten to that commit; B21's two files regenerated with B21's own code from the committed
  values; the 84 and 2 AR-shift rows added; the alignment report's hand-added line removed and its log written as the
  script prints it (the report's lines, so with the row that the committed log's line 86 lacks); the two global-fit
  logs' line 25 reworded and the local-atoms line added; every elapsed time of the logs changed; the float-noise
  values of seven files changed below 1e-13; the absolute paths changed; 1e-13 added to the floats of a pickle, an
  npz and a CSV without SHA; the six figures regenerated (Fig 3's PNG then differs in 55 pixels by at most 1 of 255,
  the trace of the 1e-13 in its input); the six new files created. They gave the verdicts the pre-run entry states.
  `6_committed_compare.py`: every CSV within 1e-9 except B21's (item 6 (a)); the two non-stationary tables 84 and 2
  rows longer, all `nonstat_step_ar`, no old row changed; 22 text files changed only on git= lines and 3 also in
  printed numbers within 1e-9; B21's tables file and the alignment report with other changes (items 6 (b) and (e));
  no line endings changed; every header SHA the third commit's, and one CSV without SHA; six untracked files.
  `9_wrapper_compare.py`: PASS (`quoted_at` non-empty in 10 rows and changed in 198; table (a) 195 rows, pickle rows
  76 → 1). `8_binary_compare.py`: noise only (with the scope map's grid, which the planning session's environment
  recomputed within 8.9e-13 of the committed one). `10_logs_figures_compare.py`: 52 of 55 logs reproduced every
  committed line; the other three failed to reproduce exactly the lines of items 6 (e) and 7 and added exactly the
  lines those items state; the images identical, identical apart from their dates, or differing by anti-aliasing
  only.
- negative tests, each on a copy of that simulated tree, were each reported: a CSV cell changed by 1e-6; a CSV row
  deleted; two lines of a table swapped; a table converted to CRLF line endings; a table without its final newline;
  a printed p changed in its fourth decimal; a float-noise value raised to 2e-9, and one raised from 0 to 1.1e-9; a
  `-dirty` header; in B21's files a `quoted_at` cell, a mean changed by 1e-6, a table (a) cell and the count; a
  pickle string; an npz value changed by 1e-6 and another set to NaN; a log line deleted; a log number; two log
  lines swapped; a traceback appended to a log (listed as an added line); a log's float-noise value raised to 3e-9;
  a log rewritten with lone CR line endings; 100 pixels of a figure. Two changes the rule allows were reported only as
  it intends: a blank line removed from a log, not at all; a line added beside a table number changed by 5e-12, as
  an added line only.
