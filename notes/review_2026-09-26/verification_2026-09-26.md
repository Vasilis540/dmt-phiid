# Verification of the error-only read of 26 September 2026

The text read is the repository at c25a310 with the pending edits of the outputs commit of the final run of
`run_all.sh` applied (their facts of the run taken from a simulated run, which the brief told the checkers not to
report). It was read on 26 September 2026, while the final run was in progress, by four separate sessions of the AI
system, A–C under one brief and D under a brief of its own (`BRIEF.md`), each restricted to outright errors — text
(T), numbers (N), cross-references (X), contradictions (C) and uncertain items (U):

- **A**: `manuscript/draft_v2.md` in full, `manuscript/figures/captions_v2.md` and the six figures (`findings_A.md`);
- **B**: S1–S5 Text (`findings_B.md`);
- **C**: `manuscript/supplementary.md`, S1–S20 Table (`findings_C.md`);
- **D**: the typeset PDFs of the paper and of its supporting information, for layout only (`findings_D.md`).

The four could not write their reports to files (the environment refuses report files from subagents); each gave its
report as its final message, and the four files here hold those reports as given, apart from the changes the README
lists. Every finding was verified here against the committed files by the planning session, and two further sessions
audited the prepared corrections in turn (section 5). No analysis was run on the data: the checks read committed
result files, and the one computation, of the coupled family's closed form at c = ±0.02 (B-N1), uses
`notes/rev_phiid_fast.py` on population matrices.

Counts: A 8 (T 2, X 2, C 1, U 3), B 28 (T 4, N 3, X 6, C 3, U 12), C 13 (T 1, N 4, X 3, C 2, U 3): 49 text findings,
45 distinct (A-T2, B-T1 and C-T1 are one; A-X1 and B-U11 are one; A-T1 and B-U12 are one). Of the 45, 42 are confirmed
and 3 are judged not to be errors (section 6). The verification found five more (V1–V5, section 4), and the audits of
the prepared corrections four more (V6–V9, section 5). D found 20 layout faults (section 7), all of them faults of the
typesetting, which is outside the repository. None of the confirmed findings changes a result, a conclusion, or a data
value of the main text's tables, and no data value of the main text's numbers table
(`manuscript/main_text_numbers.csv`) changed.

The corrections are applied in the commit after the outputs commit, by the verbatim replacements C01–C73 of
`revision/text_replacements_2026-09-26.json` (the column "fix" below names them), with the numbers table's contexts
and one added row and the record's entry ("The error-only read of 26 September 2026 and its corrections"). One
confirmed finding, B-U4, concerned the pending text of the outputs commit itself; it was corrected in that text
before the commit (section 2).

## 1. Checker A: the main text, the captions and the figures

| ID | where | verdict | fix |
|---|---|---|---|
| X1 (= B-U11) | References, Tarchi et al. (2026) | confirmed: the deconvolution statement ("standard SPM methods") is in S20 Table (row 9 of Table A; Table B, item 4); S3 Text names the study only in a list | C01: "see S20 Table" |
| C1 | Results 4, second paragraph | confirmed: the finite-sample null is solved to the data's window-level pair r₁ and \|q\| in each run × period cell (Methods; `review_v2_residual_null.log`, lines 11–14), so its change is not "applied to the DMT run only" (its DMT-run change alone is −0.0093, its placebo-run change +0.0053) | C02: the null's clause separated from the generators' conditions: "…on AR(1) pairs; on a finite-sample null solved to the data's pair r₁ in each run and period it is +0.0054 (Methods). The data's residual DiD is not distinguished from these three…" (the checker's "on the two generators" would have left the null inside the sentence's description) |
| U1 | Methods, The AR(1)-substituted estimate; Results 4 | confirmed as an imprecision: the null's own DiD of pair r₁ is −0.0146 (`derived_r17.out`, item 6) against the data's −0.0155 (`residual_source.log`, line 10) | C03: "carries approximately the data's fall of pair r₁ (its own DiD −0.0146)"; Results 4 no longer says "carries" (C02) |
| U2 | Data and code availability | confirmed: no `notes/` output carries `-dirty`; the 14 `-dirty` files and one of the five `nogit` files are under `results/`; and the sentence, like S5 Text §4's "Every result file names the commit", passes over the files that carry no commit (V1) | C04: "The result tables and reports name the producing commit in their headers (…); S5 Text lists the files of the last two kinds and those that carry none." |
| U3 | Figs 2a, 4c, 6a | not an error (section 6) | — |
| T1 (= B-U12) | S5 Text §5 | not an error (section 6) | — |
| T2 (= B-T1, C-T1) | S5 Text §3 and §5 (four places); S13 Table note | confirmed: "Round 14", "Stage B of round 16" and "Round 17" are process labels, quoted from the record's headings. The verification of 25 September kept the verbatim titles (T5, V49) so that the entries could be found; a citation by date, time and what the entry records finds them as surely, as S5 Text §4 already cites "the correction entry of 23 September 2026, 15:36 UTC". Several entries share two of these times (five at 23 September 21:40 UTC, two at 25 September 16:34 UTC), so the time alone would not do | C34, C37, C38, C39, C62: "the decision entry of 23 September 2026, 21:40 UTC" (three places), the name S5 Text §4 and §6 already give it; "the restructuring's entry, 21 September 2026, 15:12 UTC"; "the entry applying them, 25 September 2026, 16:34 UTC" |
| X2 | S3 Text §4 | confirmed: Results 6 quotes −0.011 only; −0.018 is `ccs_pub_tables.md`, line 34 | C15: "(`ccs_pub_tables.md`; section 5; the first in main text, Results 6)" |

## 2. Checker B: S1–S5 Text

| ID | where | verdict | fix |
|---|---|---|---|
| T1 | S5 Text | = A-T2 | as A-T2 |
| T2 | S3 Text §6 | confirmed: the residual is the sum of the two responses (−0.0064 + −0.0071 = −0.0137), not half of each part; the 24 September review's fix ("L116") was accepted then and not applied when the sentence moved from the main text to S3 Text on 25 September | C20: "is about half directed and half symmetric (above)", as S19 Table words it |
| T3 | S3 Text §6, §7 | confirmed: a bare "a" for a measured or realised pair lag-1 correlation, which the paper's notation calls pair r₁ ("pair-level a" is withdrawn); the same use is in S9 and S10 Tables (V2). Kept: "a" as the AR(1) or VAR(1) coefficient of a model (the family, the AR(1) generator, "(a, q)"), and the log lines S3 Text §6 quotes verbatim ("window a 0.8629, …", lines 276–280), which keep the file's labels by S3 Text's convention | C17, C18, C19, C21, C22: "pair r₁" in the five places |
| T4 | S5 Text §4 | confirmed: the clone held the data files (`*.mat`; the record's entry on the review of 24 September and its verification: "copies of the data files"), so the files were moved | C36: "the files were moved" |
| N1 | S3 Text §3 | confirmed: the closed form at c = +0.02 gives sts − (xtx + yty) = +0.004498 and rtr = 0.027480 (recomputed here), which round to +0.004 and 0.027; +0.005 and 0.028 are second roundings of the table's +0.0045 and 0.0275 | C14: both pairs at the table's four decimals, "+0.0045 while rtr = 0.0275" and "+0.0586 against rtr = 0.0191" |
| N2 | S3 Text §7 | confirmed: from the 50 replicates of `partB/calibration.csv` (the condition field, which holds commas, parsed from the right) the ratios are −17.04, −23.57, −22.22 and −24.63; from the printed table −17.4, −23.7, −22.3, −24.6 | C25: "−17, −24, −22 and −25" |
| N3 | S3 Text §7 | confirmed: the mean δ_sym DiD at Δc = −0.02 is −0.01494898 | C24: "−0.0149" |
| X1 | S1 Text | confirmed: S5 Text says nothing about the codes; the record's entry "Git history and the participant codes" (15 September 2026) does | C07: that entry cited |
| X2 | S2 Text | confirmed: `rev_extra.log` as regenerated at d507728 (a75d015) reads "deconvolution outputs not present" in section (g); the values are in its version at 9318997 (run-level r₁ 0.7899, in-band share 0.991, ts_gsr) and in the review computations of 14 September, section 3 (0.866 → 0.790 and 0.856 → 0.776; 99.1 %) | C08: the values stated with both sources, and that the log's regenerations without the sandbox do not hold them |
| X3 | S3 Text §10 | confirmed: S2 Text gave 0.848 → 0.783 (W = 60), not the run-level 0.866 → 0.790 | resolved by C08, after which S2 Text states 0.866 → 0.790 |
| X4 | S3 Text §10 | confirmed: `partB/family_checks.log`, line 13, holds the derivatives at (0.97, 0.25) (sts +32.774, rtr +0.064) | C26 |
| X5 | S3 Text §2 | confirmed: a pointer left from the main text's former Methods subsection; the DiD is defined at the opening of the main text's Results | C12: "(DiD; main text, Results)" |
| X6 | S5 Text §2 | confirmed: Results 6 gives one reason; S3 Text §5 gives two reasons and a rule | C33: "for the reasons S3 Text §5 gives (main text, Results 6)" |
| C1 | S3 Text §1, §2 | confirmed: the prewhitened CCS values use `phyid`'s mask (S3 Text §8; main text, Redundancy functions) | C11, C13: the exception stated in both places (C13 with the comparison values of V8) |
| C2 | S3 Text §7 | confirmed: condition (i) of the band-passed generator solves β̄_post to a window-level mean pair r₁ of 0.8482 ("unlike B17's population Δa", B17b pre-run entry); its population change is the Δr₁ = −0.01629 the paragraph gives | C23: "for a window-level fall of 0.015 in pair r₁"; see V3 for Table 3 |
| C3 | S5 Text §1 | confirmed: `notes/partB_prespec_2026-09-14.md` entered git once, in 477cccc (14 September, 12:50:51 UTC), before the first computation's commit (6c8c64e, 12:55:28) | C32: "committed together, in one commit (477cccc), before any of them was run" |
| U1 | S3 Text, opening | confirmed: B1–B13 take their numbers from their scripts (`notes/partB1_*.py` to `partB13_*.py`); the record never writes B1, B3 or B12, and its headings name B6–B13 by topic ("Part B, items 6–8", the leave-two-out, the run-level cross-lag deviation and regional test, the cross-lag budget); B1–B5 were planned in `notes/partB_prespec_2026-09-14.md`, with their outcomes in `notes/partB1_scope_map.md` to `partB5_literature.md` | C09; the paragraph's opening statement of the record's entries, V6 (C63); the same statement in S19 Table's source note, C73 |
| U2 | S5 Text §6 | confirmed: nine commits the supporting information names are not in the list (e01c836, 8554b3d, ac1fdc0, f3b435d, 66b570e, 4f7437b, dbf2311, 9a19b10, 0a25aaa; a633cc1 is PhiID's, outside this repository, and goes with the external commits, V9) | C40: a sentence naming them, with their dates; and the outputs commit named (V5) |
| U3 | S3 Text §4 | confirmed: the two grid counts had no named source (`notes/partB1_scope_map.md`, item 2; `notes/fresh_review_2026-09-17/checks/check_A1_atoms_family.log`, line 66) | C16 |
| U4 | S5 Text §4 (the pending sentence of the outputs commit) | confirmed: the four clauses did not follow the four comparisons of the pre-run entry (`6_committed_compare`, `9_wrapper_compare`, `8_binary_compare`, `10_logs_figures_compare`) | corrected in the outputs commit's own text before that commit: one clause per comparison, in the entry's order, each with the differences fixed for it (V4) |
| U5 | S4 Text, opening | confirmed as an ambiguity: "OHBM 2016" reads as a citation with no entry | C27: "(COBIDAS, released in 2016; summarised in Nichols et al., 2017, …)" |
| U6 | S4 Text, Sh5 | confirmed: S1 Text describes the codes' form and does not state them | C29: "described" |
| U7 | S4 Text, S8 | confirmed: S1 Text names "the pinned commit" without its hash | C28: "(S5 Text §6; main text, References)" |
| U8 | S5 Text, opening | confirmed: the entry "Git history and the participant codes, 15 Sep 2026" is dated to the day | C31 |
| U9 | S3 Text §6 | not an error (section 6) | — |
| U10 | S5 Text and S3 Text, openings | confirmed: the main text's reference list carries phyid's pinned commit | C10, C30: "and the reference list" |
| U11 | References | = A-X1 | as A-X1 |
| U12 | S5 Text §5 | = A-T1 | — |

## 3. Checker C: S1–S20 Table

| ID | where | verdict | fix |
|---|---|---|---|
| N1 | S2 Table, W = 30 | confirmed: −0.40748931 (`results/primary_b_ts_gsr_win30.csv`, line 76) | C42: "−0.407" |
| N2 | S9 Table; S17 Table rows 841–842 | confirmed: the inverted limits are −4.998 × 10⁻⁶, −4.538 × 10⁻⁶ and −6.82 × 10⁻⁷ (`inference_revision.csv`, rows 841, 842, 881), so the ε interval excludes zero (p = 0.0479); the committed percentile lower limits of rows 841–842 are "−0.00000" (`crosslag_budget_tables.md`, line 17) | C44–C48: "−0.00000" in the five places. B21's reading of intervals is unchanged: a zero of either sign rounds to the same value |
| N3 | S19 Table, Part A | confirmed: the prediction for the 20,000-run repeat and the expected tier entered git at 18ad8b4, 12 September 2026, 21:43 EEST (`git log -S`) | C57, C58: "(18ad8b4, 12 Sep 2026)" |
| N4 | S17 Table, source | confirmed: of the 36 engine rows, 24 are Table 2 and S1 Table quantities and 12 S3 Text's; each block of four holds the DMT change, the placebo change, the FD DiD and the FD-residualised DiD | C53 |
| X1 | S16 Table, source | confirmed: the sts-matched null is section 5 of `notes/review_computations_2026-09-14.md`; section 5 of the review of 14 September is on internal inconsistencies | C52 |
| X2 | S17 Table, last column and note | confirmed: B21 matched quoted intervals by their printed values; δ_wd equals δ_run on rows 839 and 868 and δ_means on the placebo run is equal on the two variants (rows 843, 873), so those rows carry the other quantity's lines; of the 39 "changes" rows the column marks ten (73, 379, 667, 752, 770, 865, 868, 874, 885, 888), nine of them quoted, as the record's B21 outcome lists | C55: the note says so; the column, a copy of B21's record, is kept |
| X3 | S19 Table, Part B | confirmed: Table 3 carries the pair r₁ DiD, not the pair \|q\| DiD | C61 |
| C1 | S19 Table, B16b | confirmed: 0.76 is the run-level r₁ (+0.7572), 0.75 the W = 60 value (+0.7506; S11 Table), as S3 Text §8 labels them | C59: "run-level r₁ 0.76" |
| C2 | S19 Table, B21 (d) | confirmed: subject-bootstrap percentile intervals of a ratio without a per-subject vector, unmarked, against the head note's rule | C60: "(percentile)" twice |
| T1 | S13 Table note | = A-T2 | C62 |
| U1 | S2 Table note | confirmed: three differences of correlations are positive (+0.0667, +0.0052, +0.1065) and control (b)'s FD correlations are positive; every ρ_S of sts is negative | C41: "Every ρ_S of sts is negative, against the pre-specified positive direction." |
| U2 | S17 Table, source and header | confirmed as an ambiguity: the text at 90690f4 is that of 0b8d1a4 (21 September; `git diff 0b8d1a4 90690f4 -- manuscript/` holds only the record), while S8 Table's "main text of 23 September 2026" is the shortened text (526090d) | C54, C56: "the drafts of 21–22 September (the text at 90690f4)" in the source and "the drafts of 21–22 September (file:line at 90690f4)" in the header |
| U3 | S13 Table | made consistent: the same quantities as S10 Table's −0.0422 and −0.0675 (unrounded −0.042180 and −0.067523, so the three-decimal values were right) | C51 |

## 4. Found in verifying (V1–V5)

| ID | where | the error | fix |
|---|---|---|---|
| V1 | S5 Text §4, opening; Data and code availability | "Every result file names the commit at which it was produced" does not hold for five CSV files that carry no header by design (their readers read them without a comment line; the final run's pre-run entry, item 3), for the files `run_all.sh` writes only with the deconvolution sandbox present (`inference_rows_deconv.csv`, `inference_rows_w30.csv`, the sixteen regional ΦR tables and the report `notes/regional_phir_deconv_2026-09-14.md`, the last added by the audit, U1), and for logs whose scripts print no commit; the tables and reports otherwise all carry one (`git=`, or "at git" in the two captions files) | C35 (S5 Text), C04 (Data and code availability) |
| V2 | S9 Table (twice), S10 Table | a bare "a" for the data's run-level pair r₁ and for the band-passed generator's realised window-level pair r₁, as B-T3 | C43, C49, C50 |
| V3 | Table 3, rows 3 and 4 | the label "pure autocorrelation change (Δa = −0.015)" covers both generators, but the band-passed generator's change is a window-level target of pair r₁ reached by a filter tilt (B17b pre-run entry; the verification of 25 September, U6, on the same point in Results 4), and only the AR(1) generator's is a population change of a | C05, C06: "(window-level fall of 0.015 in pair r₁), band-passed generator" (the audit's wording, U5) and "the same (population Δa = −0.015), AR(1) pairs"; in the numbers table the band-passed row's number is 0.015, sourced to the generator's target (`calibration_filtered_tables.md`, line 4: 0.8632 → 0.8482), and a row is added for the AR(1) row's −0.015 (`calibration_tables.md`, line 8) |
| V4 | S5 Text §4 (the outputs commit's own text) | its statement of the headers the run wrote gave "five carry no SHA by design" without naming them, beside the opening sentence of V1 | corrected in the outputs commit's text before that commit: the five named; the build of that commit checks every regenerated table's and report's header |
| V5 | S5 Text §6 | the outputs commit, which could not name itself, can now be named | C40: its identifier and date, and the corrections as the commit that follows |

## 5. The audits of the prepared corrections (V6–V9)

Before the corrections were delivered, a further session of the AI system audited them (the first audit): the
replacements applied to the tree of the outputs commit, the numbers table, this folder and the record's entry. It
rebuilt the corrected tree from the replacements byte for byte, found the numbers table's checks and B21's `quoted_at`
as section 8 states them, and found no numeric error. Its findings, each checked here and applied:

| ID | the finding | applied |
|---|---|---|
| C1 | C09 left S3 Text's opening sentence saying that the record holds the pre-run and outcome entries of every computation | V6 |
| X1 | S5 Text §6 names this read (C40), but §5 does not describe it and Data and code availability's list of review folders omits its folder | C68, C67, as the revision of 25 September did for its own check (its V39) |
| X2 | "the entry of the revision of 23 September 2026, 21:40 UTC" and "the entry of that revision, 25 September 2026, 16:34 UTC" are ambiguous: five entries share the first time and two the second | C34, C38, C62: "the decision entry of 23 September 2026, 21:40 UTC"; C39: "the entry applying them, 25 September 2026, 16:34 UTC" |
| N1 | "several entries share each of those times": one entry has 21 September 15:12 UTC | "two of those times" (the record's entry; section 1, T2) |
| N2 | earlier entries of the record give −0.408, −0.0150 (twice), −24 and "the file was moved" | the record's entry lists them as superseded (its item 7) |
| N3 | section 2, X4, cited line 12 of `family_checks.log`; the derivatives are on line 13 | corrected |
| C2 | "under one brief": D had a brief of its own; and this verification understated what the README lists as changed in the findings files | the README, this verification and the record's entry corrected |
| T1 | the file layout of `CLAUDE.md` does not list `review_2026-09-26/` | B09 |
| U1 | the report `notes/regional_phir_deconv_2026-09-14.md`, written only with the deconvolution sandbox, carries no commit and is not among C35's exceptions | added to C35 (V1) |
| U2 | S5 Text §6 lists the external commits of the data and of `phyid` but not a633cc1, which S3 Text §2 names | V9 |
| U3 | a bare "a" for a measured lag-1 correlation in four places | V7; the fourth, the row "\|a_x − a_y\| at fixed mean 0.85" of S3 Text §3's table, is copied from `partB/exchange_rates_tables.md` and keeps the file's label |
| U4 | "every other CCS value in the paper uses the published definition" (Methods), and S3 Text §2's statement of the same, beside S17 Table's rows under `phyid`'s mask | V8 |
| U5 | Table 3's new label "window-level pair r₁ −0.015" names no change, where the next row's reads "population Δa = −0.015" | C05: "(window-level fall of 0.015 in pair r₁)" (V3) |

| ID | where | the error | fix |
|---|---|---|---|
| V6 | S3 Text, opening | "the record holds the pre-run entry (rule and prediction) and the outcome entry of every computation": B1–B5 were planned and reported in `notes/` files (B-U1), the post hoc computations of the reviews have no pre-run entry (S19 Table, Part B), and not every pre-run entry records a rule and a prediction (B8 neither; the record's correction note of 15 September 2026, 10:05 UTC) | C63: "holds the pre-run entry and the outcome entry of every numbered computation from B6 on" |
| V7 | main text, Results 4; S3 Text §6; S19 Table, B14 | "grows with a and \|q\|", "windows that differ in a, q or variance", "the window-level scatter of a": a bare "a" for the pairs' or the regions' measured lag-1 correlation, as B-T3 | C65: "pair r₁"; C64: "r₁"; C71: "regional r₁" |
| V8 | main text, Methods; S3 Text §2; S5 Text §1; S17 Table | the statements that every other CCS value is under the published definition pass over `phyid`'s values given beside the published ones for comparison (S3 Text §1 and §6; S19 Table, B2: "\|level\| ≤ 0.04 nats under `phyid`'s mask, as recorded") and S17 Table's rows under `phyid`'s mask ("CCS sts", "CCS rtr", "CCS xtx+yty", the prewhitened series' rows and the decomposition rows marked "(code mask)"; `notes/partB2_ccs_run.py`, `partB16_prewhiten.py`, `partB18_ccs_decomposition.py`); S5 Text §1 reports the 14 September review's CCS decomposition, made with `phyid`'s mask (`notes/adversarial_review_2026-09-14.md`, item 5 and section 4.1), without saying so; and S3 Text §2 placed every `phyid` value in `ccs_pub_tables.md`, where the decomposition's are in `ccs_decomposition_tables.md` | C66 and C13: the exception stated, and the two files; C70: S17 Table's source says which rows use which mask; C72: S5 Text §1 names the mask |
| V9 | S5 Text §6 | the list of every commit identifier the text rests on gives the external commits of the data and of `phyid`, but not that of the MATLAB reference `phyid` pins, pmediano/PhiID at a633cc1 (S3 Text §2) | C69 |

A second audit, of the corrections as revised above, rebuilt the corrected tree from the replacements byte for byte
and found: the exceptions of V8 left out S19 Table's B2 row, which gives a value under `phyid`'s mask, and S5 Text
§1's report of the 14 September review's CCS decomposition, made with that mask without saying so, and S3 Text §2
placed every `phyid` value in `ccs_pub_tables.md` (all three added to V8); S19 Table's source note still called the
labels B1–B24 the record's (B-U1; C73); the numbers table's head note described the recomputed contexts inexactly, and
one row's recomputed context was one character longer than the table's window (both corrected); section 3 above quoted
C56 as C54 (corrected); and "no value changed", beside a label whose "−0.015" became "fall of 0.015", is made "no data
value changed" here, in the record's entry and in `CLAUDE.md`.

## 6. Judged not to be errors

- **A-U3 (figure annotations).** Figs 2a, 4c and 6a print their values at fewer digits than the captions, as figure
  annotations do for legibility, and every one is the caption's value correctly rounded: 8.146 → 8.15, 16.933 →
  16.93, 0.2240 → 0.22, 0.3089 → 0.31, +0.953 → +0.95, +0.970 → +0.97, +0.626 → +0.63, −0.832 → −0.83, −0.0844 →
  −0.084, −0.1003 → −0.100. N4 of 25 September was a second rounding (+0.0088 for +0.0087493), which this is not.
- **A-T1 and B-U12 (S5 Text §5, "the record's entries call them the writer's session and the planning session").**
  The sentence names the record's labels once in order to replace them, in the paper, by dated descriptions; it is
  the key to which the rule on process labels itself points (S5 Text §5), and a reader of the record needs it.
- **B-U9 ("four specification changes (windowed sts → sixteen atoms → CCS → diagnostic residual)").** The wording is
  the pre-registered rule's (record, "Part B, items 6–8: pre-run entry", 15 September 2026), which S3 Text restates;
  the count runs from the original whole-brain global fit, the first specification, so that the windowed estimator
  is the first of the four changes.

## 7. The layout check (D)

D found 20 faults in the preview PDFs (main.pdf 6, SI.pdf 14). All are faults of the typesetting (pandoc and XeLaTeX,
outside the repository), none of the manuscript files, and all are addressed there before the PDFs are typeset from
the final commit:

| ID | fault | in the typesetting |
|---|---|---|
| M1, M2 | a table caption separated from its table | the main text's tables set as floats with their captions; in the supporting information, a caption, heading or label kept with its table's first rows |
| M3 | Figs 1, 3 and 4, drawn 804–1,025 pt wide, printed at 45–58 %, their lettering at 3–5 pt | the three set on landscape pages at up to 69–89 % |
| M4, M5 | a heading with one line under it; a last page with one line | widow and orphan lines refused |
| M6 | a URL letter-spaced in the justified reference list | the reference list set ragged right |
| S1–S4 | row 1 of S20 Table A taller than a page, 39 lines lost below it, with a blank page, a stranded heading and a doubled header as consequences | a table with a row taller than a page is set as one block per row |
| S5–S8 | headings and table labels stranded at the foot of a page | kept with what follows |
| S9, S10 | a page holding one table row | a table's first row kept with the second and its last with the one before it, unless those rows are very tall |
| S11 | "file:line" linked as a URI | the colon escaped |
| S12, S13 | underscores read as emphasis; subscripts on accented, non-ASCII or bracketed bases printed raw | the subscript rule extended to those bases; every other underscore made literal |
| S14 | the macron of β̄ displaced | β̄ set with a centred accent |

Re-checks of the PDFs typeset after these changes found further faults of the typesetting (a figure apart from its
caption, a heading apart from the table it heads, a table's last row alone on a page, gaps before tables kept whole or
where the room kept for a table was overestimated, a table's header printed twice where a page began with it, a run of
"(n)" lines renumbered as a list, the macron of β̄ touching the row above), corrected there before the PDFs are
typeset from the final commit (the figures and the main text's tables set as floats with their captions, a heading
kept with the headings and table after it, a different and closer test of the room left on a page, hard line breaks, a
strut), and one of the prepared text: in C35, `<SHA>` stood outside a code span, where pandoc reads it as a tag and
drops it (now in code, as `git=<SHA>` is).

The figures themselves (M3) also exceed PLOS Computational Biology's dimensions (width 789–2,250 pixels at 300 dpi,
height at most 2,625 pixels; lettering 8–12 pt in Arial, Times or Symbol; TIFF or EPS): every figure is wider than
7.5 inches except Fig 5, which is taller than 8.75 inches. They are redrawn to those dimensions at submission, by a
change of `scripts/15_figures_v2.py` recorded with its own entry, from the same result files.

## 8. The corrections and their checks

The 73 replacements change the main text in nine places (C01–C06 and C65–C67: the reference note, Results 4 twice,
Methods twice, Data and code availability twice, Table 3's two labels) and the supporting information in 64 (S1 Text
1, S2 Text 1, S3 Text 20, S4 Text 3, S5 Text 14, `supplementary.md` 25). Checked on the corrected tree:

- no line added or removed in any manuscript file;
- the intervals B21 reads (its pattern, the values rounded as it rounds them, and their files and lines) are the same
  as in the outputs commit, so the column `quoted_at` that the final run regenerated from the text of c25a310 holds
  for this text as well; recomputed from the corrected text, it equals the committed column in every row;
- `manuscript/main_text_numbers.csv`: the contexts of the 26 rows whose context the edits reached recomputed, one
  row added (Table 3's population change on AR(1) pairs), the band-passed row's number made 0.015 and sourced to the
  generator's target; 1,193 rows; `notes/review_2026-09-25/checks/check_numbers.py` prints "rows 1193, data rows 676, flagged 12", the twelve
  sign-wording rows of `check_numbers.out`, and `check_cells.py` "flagged 0";
- `tablecheck.py` on the seven manuscript files: 0 rows with a wrong cell count;
- no process label left in the manuscript files outside S5 Text §5's key;
- Introduction through Methods: 6,997 words with headings (6,984 before), within the 7,000 of the decision entry of 23
  September 2026.
