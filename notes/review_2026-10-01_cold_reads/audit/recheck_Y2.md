# Y2 — the supporting texts' changes and the derived numbers recomputed

HEAD of VT (26156b8) against `checked3`. Verified: what changed in `manuscript/si/S2_Text.md`, `S3_Text.md`,
`S4_Text.md` and `S5_Text.md` (eleven changed paragraphs: 1, 5, 3 and 2); the script
`notes/review_2026-10-01_cold_reads/checks/derived_r24.py` with its output `derived_r24.out`; the dispositions of
X1-1 and X1-10 and points (4) and (5) of the section "The reading of S19 Table's Part B against the whole paper"; the
reasons of the replacements S201, S323, S324, S417, S420, S422 and S507 and what changed in S305, S311 and S314; the
rules on names and labels.

**Result.** No number that the corrections changed or added in the four supporting texts or in the script's output
was found wrong: each agrees with its source at the printed precision, and every new value of `derived_r24.out` was
reproduced by a separate computation. Eight findings: 0 errors, 4 inexact, 4 notes. The inexact ones are a general
sentence of S2 Text, repeated in the main text's list of supporting information, that the clause added to S2 Text
makes untrue of one result; two reasons recorded in the replacements file (S201, whose words the disposition of X1-5
repeats, and S422); and a comparison in the script that is made on sorted lists where its comment says that it is made
cell by cell.

**How checked.** Nothing under VT was changed (`git status` empty at the end). Scratch files are under VW/Y2/: the
word diff of `manuscript/si/` (`si_worddiff.txt`); `tree/`, a copy taken from HEAD with `git archive` of the script
and its output, of `notes/rev_inference_inverted.py` and of the nineteen files that the script reads, in which the
script was run (`derived_r24.run.out`; `audit_open.py` records every file it opens); the recomputations (`own.py`,
`own2.py`, `regional_check.py`, each with its `.out`); the scan of the main text's numbers (`scan_main.py`,
`scan_main.out`, `scan_signed_noint.out`); the comparison of the replacements file with its state at `checked3`
(`json_cmp2.out`). No internet and no subject data: every computation is on committed result files. Paths are
relative to VT and line numbers are those of HEAD. "Review folder" is `notes/review_2026-10-01_cold_reads/`;
"dispositions" is its
`audit/dispositions_revision.md`; "replacements file" is its
`revision/text_replacements_2026-10-01_cold_reads_revision.json`; `derived_r24.py` and `derived_r24.out` are in its
`checks/`; result files named without a folder are in `notes/review_results/partB/`; "the report" of the regional
check is `notes/regional_phir_deconv_2026-09-14.md`.

## Findings

**Y2-1**
- Where: `manuscript/si/S2_Text.md`, the head (line 3): "Every result in this text is post hoc."; the main text's list
  of supporting information (`manuscript/draft_v2.md` line 395): "Every result in it is post hoc". Both unchanged;
  read with the clause that the correction for X1-5 added to S2 Text's third paragraph (line 9): "its prediction was
  missed, the increase being smaller, not larger, inside the Default/Control proxy than outside it (inside minus
  outside −0.0047 [−0.0079, −0.0013], ...".
- Problem: The added clause puts into S2 Text the result of the regional test, of which the same sentence says that
  it had "a prediction recorded before it was run". The paper does not class that computation as post hoc. S19 Table
  has it in Part A, among the predictions recorded before a computation (verdict "missed", one of the 16 missed of the
  67 counted), and not in Part B, the post hoc computations; Methods sets the two against each other ("whether it had
  a recorded prediction or was post hoc"); S5 Text defines a post hoc computation as one "run without a pre-run
  entry"; the record calls the check "the pre-specified regional ΦR check". At `checked3` S2 Text said only that the
  test was carried out and gave no result of it, so that the two sentences held of every result the text gave; with
  the outcome stated they do not hold of this one. What the record's closure entry says of it is something else: that
  no confirmatory claim attaches to any outcome of the regional check, the quantity, the deconvolution and the
  estimator having been chosen after results were seen.
- Evidence: `manuscript/supplementary.md` line 1616 (the row of the regional check, under the heading of Part A, line
  1603; "missed"; "S2 Text") and line 1691 (Part B's heading); the tally of Part A's verdict cells (36 met, 15 partly
  met, 16 missed, the regional row among the 16); `manuscript/draft_v2.md` line 241; `manuscript/si/S5_Text.md` line
  3 (the definition) and line 7 ("a regional test with a prediction recorded in advance");
  `manuscript/analysis_record.md` lines 2388–2389 and 2423–2425; `git show checked3:manuscript/si/S2_Text.md`, line 9.
- Grade: inexact

**Y2-2**
- Where: the replacements file, entry S201 (line 544), `why`: "the outcome is now stated here, with the values of the
  report's first table and of S19 Table's row"; the same words in the dispositions, the paragraph on X1-5 (lines
  2340–2341): "the values of the report's first table and of the row".
- Problem: The values are not in the report's first table. Its first table lists the scripts and its second the
  checks of the validation (section 0). The row that S2 Text quotes is the first row of the third table, that of
  section 1, "The prediction, on the cell it was made for", and the paragraph under that table repeats it. The values
  themselves are right (last section).
- Evidence: the report, lines 9–15 (the table "file | what it does"), lines 25–41 (the table "check | max abs
  difference"), lines 49–58 (the table "comparison | difference [95 % CI], p | positive/14 | n inside / n outside";
  line 51: "-0.0047 [-0.0079, -0.0013], p = 0.0233 | 4 | 37 / 62") and line 64.
- Grade: inexact

**Y2-3**
- Where: the replacements file, entry S422 (line 816), `why`: "S1 Text states the first of the two values and not the
  second (found in a reading of the supporting tables against the paper after a third check of the corrected
  revision)."
- Problem: The remark on item P5 was made in the reading of S19 Table's Part B against the whole paper, in its
  account of the row of the numbers derived on 24 September 2026. That reading is the only one made after the third
  check, and its subject is one part of one table, not the supporting tables. The dispositions give the correction
  under that reading (point (5)), and the reasons of S323 and S324, beside this one in the file, name it as "a
  reading of S19 Table's Part B against the paper" and "the same reading of Part B against the paper". The first half
  of the reason holds: S1 Text states the 0.82 and not the 0.54.
- Evidence: the review folder's `audit/partB_reading.md` line 441 ("One remark on S4 Text: its item P5 (S4 L38) says
  the two values are "stated in Results 7 and S1 Text"; S1 Text (S1 L5) states the 0.82 and not the 0.54.");
  dispositions lines 2511 and 2551–2553; the replacements file lines 800 and 808; `manuscript/si/S1_Text.md` line 5.
- Grade: inexact

**Y2-4**
- Where: `derived_r24.py`, item 6, the block added after the third check: the comment (lines 180–181), "each r
  compared at three decimals with the value that B16c's tables file prints for the cell", and the assertion (line
  198), `assert sorted(mine8) == sorted(printed)`; the line the block prints (`derived_r24.out` line 68): "each equal
  at three decimals to the r that notes/review_results/partB/prewhiten_fixed_tables.md prints".
- Problem: The script compares the two lists after sorting them. It therefore tests whether the eight computed values
  are the eight printed ones, not whether each cell's value is the one printed for that cell: the assertion would pass
  with the values of two cells exchanged. What the output says is true all the same. Compared cell by cell, with the
  order, the variant and the estimator taken from the heading above each printed r, the eight are equal at three
  decimals, and as the two lists stand they are in the same order.
- Evidence: `prewhiten_fixed_tables.md` lines 28, 53, 77, 102, 126, 151, 175 and 200, under the headings of lines 6,
  31, 55, 80, 104, 129, 153 and 178 (+0.445, +0.570, +0.168, +0.014, +0.333, +0.081, +0.157, −0.079); the
  recomputation from the per-subject vectors (VW/Y2/own.out: +0.444867, +0.570232, +0.167986, +0.014304, +0.332750,
  +0.081360, +0.156566, −0.079255, in that order of cells).
- Grade: inexact

**Y2-5**
- Where: `manuscript/si/S5_Text.md` §1 (line 7): "three of its checks are quoted, as review computations, in S3 Text
  §4, §6 and §9".
- Problem: The three are there, each with its log (last section). Of the words "as review computations": §6 and §9
  say of the value they quote that it is "a computation of the review of 17 September 2026"; §4 gives its value with
  the path of the review's log and no such words, so that there the status is to be read from the name of the folder.
  Before the correction the sentence named §6 and §9 only.
- Evidence: `manuscript/si/S3_Text.md` line 128 ("(0 of 36,481;
  `notes/fresh_review_2026-09-17/checks/check_A1_atoms_family.log`)"), line 307 and line 550.
- Grade: note

**Y2-6**
- Where: `manuscript/si/S4_Text.md`, row R1 (line 62), first sentence: "Contrasts of the data are given as mean DiDs
  with inverted sign-flip 95 % intervals and exact p (Tables 2 and 4; Results 2–7; ...".
- Problem: For the record of the places opened; the row's other sentences account for what follows. Of the six
  sections of the range, Results 2, 6 and 7 print DiDs with an inverted interval and an exact p, and Results 4 prints
  two with an interval and no p, as the parenthesis goes on to say. Results 3 prints no DiD: its contrast of the data
  is the regional one, with t intervals, which the row's last sentence gives as an exception. Results 5 prints its
  DiDs with p and without an interval; the intervals are drawn in Fig 6 and printed in S14 Table, as the row's second
  sentence says of the lags.
- Evidence: `manuscript/draft_v2.md` lines 87 and 106 (Results 2), 114 and 116 (Results 3 and Fig 4's caption), 120
  (Results 4), 146 and 148 (Results 5 and Fig 6's caption), 154 (Results 6), 158 and 164–168 (Results 7 and Table 4).
- Grade: note

**Y2-7**
- Where: dispositions, the paragraph on X1-1 (line 2301): "and two had no interval anywhere (the count DiD of the
  replaced volumes; what the AR(1)-substituted estimate carries of the contrast at p = 20)"; the replacements file,
  entry S417 (line 976), `why`: "the two contrasts that had no interval anywhere".
- Problem: True of the paper, and of the inverted interval; not of the repository for the second of the two. The
  run's files held the subject-bootstrap percentile interval of the estimate's DiD at p = 20, as the finding itself
  says ("a committed result file holds one"). For the count DiD no file held an interval.
- Evidence: `notes/review_results/inference_rows_prewhiten_fixed.csv` line 165 (`did` −0.0036993, `did_lo`
  −0.0062745, `did_hi` −0.0012018; the pickle holds the same); the review folder's `audit/recheck_X1.md` lines 38–40
  and 51–52.
- Grade: note

**Y2-8**
- Where: `derived_r24.py`, the docstring, two statements that the difference from `checked3` does not touch: "the
  between-subject SDs of the three readings of the primary contrast from B27's per-subject table" (line 3) and
  "Planning-session computation on the outputs of B27, B28, B29 and B16c as the run wrote them" (line 16).
- Problem: Outside the delta; read because the docstring was to be checked. (i) Item 2 gives the SDs of the
  pre-injection gap, of the post-injection gap and of the DiD (for five sets of quantity, variant and window, the
  primary contrast the first of them). The paper's three readings are the DiD, the post-injection gap and the
  baseline-adjusted contrast; the third is a regression intercept and has no between-subject SD, and the
  pre-injection gap is not one of the three. (ii) The script also reads outputs of B4, B7, B11, B15, B16, B20 and
  B21, the inference rows of the raw series and the regional array of the windowed estimator (items 3, 4, 6, 7, 10 and
  13); the docstring's first paragraph names two of these, B20's table and, since this delta, B15's directed response.
  The clause that the delta added to the docstring is exact (last section).
- Evidence: `derived_r24.py` lines 80–93 and `derived_r24.out` lines 40–45 ("SD pre gap ..., SD post gap ..., SD
  DiD ..."); `manuscript/draft_v2.md` line 89 ("The three readings of the contrast are the DiD, the post-injection
  gap and the baseline-adjusted contrast"); the head lines of `regional_partial.csv` (`partB20_regional_partial.py`),
  of `inference_revision_tables.md` and `splithalf_subjects.csv` (`partB21_inference_revision.py`) and of
  `directed_crosslag.csv` (`partB15_directed_crosslag.py`); the script's comments on items 7 and 10 (lines 201–202
  and 255–261: B11's table, B4's series, the log of B7); `manuscript/si/S3_Text.md` line 480 (B16's inference rows).
- Grade: note

## Checked and found exact

**1. The delta** (`git diff --word-diff checked3 HEAD -- manuscript/si/`: eleven changed paragraphs, every changed
token read; S1 Text unchanged).

- S2 Text, the outcome of the regional check (line 9): "inside minus outside −0.0047 [−0.0079, −0.0013], a percentile
  interval; p = 0.023; positive in 4 of 14". The report's row (line 51) and its paragraph on the outcome (line 64);
  `notes/review_results/regional/regional_phir_deconv_ts_gsr_win60.csv` line 37 (−0.004658, −0.007864, −0.001291,
  p = 0.02331543, "pos=4/14", 37 parcels against 62); S19 Table, Part A (`manuscript/supplementary.md` line 1616):
  the same values, "(percentile)", verdict "missed". The kind of interval: `notes/rev_regional_phir.py` lines 170–173
  and 283 take the 2.5th and 97.5th percentiles of 10,000 subject-bootstrap means. Recomputed from the committed
  per-subject regional atoms (`regional_atoms_deconv_ts_gsr_win60.npy`, the parcels by the names of the DiD map; 24
  Default and 13 Control parcels against the 62 other cortical ones): mean −0.004658, exact sign-flip p = 0.02331543
  (382 of 16,384), positive in 4 of 14; mean DiD inside +0.0156 and outside +0.0203, so that the increase is the
  smaller inside; percentile intervals of three sets of 10,000 draws from another generator [−0.0079, −0.0013],
  [−0.0079, −0.0012] and [−0.0078, −0.0012]; the inverted sign-flip interval of the same difference would be
  [−0.0085, −0.0008], so that
  "a percentile interval" is the right mark in a text whose other intervals are the inverted ones (line 3).
- S3 Text §5 (line 299): "+1.12 ... (p = 0.2166, positive in 7 of 14; inverted sign-flip interval [−0.58, +2.97],
  from the per-window file: `derived_r24.out`, item 14)". `censoring_tables.md`, the "mean" row of table (a):
  "+1.12 (p = 0.2166; 7/14 positive)"; `derived_r24.out` line 102; recomputed from `censoring.csv` in exact
  arithmetic (item 14 below). The main text's Limitations gives the same mean, p and count.
- S3 Text §6 (line 317): "(the interval inverts the sign-flip test on the per-run values of `directed_crosslag.csv`;
  computed on 23 September 2026, and again in `derived_r24.out`, item 13)". The value, "+0.00044 [−0.00061,
  +0.00149], p = 0.38", and that of the RMS of δ_anti, "−0.0005 (p = 0.73)": `derived_r24.out` lines 97–98;
  `directed_crosslag_tables.md` line 12; recomputed (item 13 below). The date: the interval entered S3 Text in the
  commit of 23 September 2026 (526090d), where the parenthesis read "computed in Stage B of round 16". Before HEAD
  the two limits stood in no file but S3 Text: B21's files hold the interval of the mean of the two runs, not of
  their difference (`inference_revision.csv` lines 785–786).
- S3 Text §6 (line 372): "(`notes/review_2026-09-30/checks/conversions_b26.out`)". The file exists and holds the
  conversions the sentence speaks of, each value of the paragraph at the printed precision: −2.4155, −1.7242, −2.7295
  and −40.2218 per unit of A_other (lines 7–10; Δ A_other −0.00009789 and Δ residual +0.00393750 for the fall of the
  weight); on ts_gsr, net of the expectation, −0.000603 [−0.001673, +0.000398], +0.001457 [−0.000962, +0.004041] and
  +0.001646 [−0.001087, +0.004566] (lines 12–14); the excess +0.0088649893, the fractions 0.1643 and 0.1857 and
  their range [−0.1226, +0.5151] (lines 22–25); on ts_demean, as it is, +0.006015 [+0.000629, +0.011438] and
  +0.006797 [+0.000711, +0.012925] (lines 20–21). The record's entry "The matrices that are not positive definite
  (B26): outcome" names the file (line 8305).
- S3 Text §8 (line 544), the eight correlations: "run from −0.079 to +0.570 over the eight cells, the Fisher-z
  interval including zero in seven of them (not at p = 10 on ts_gsr at the global fit, +0.570; ...)". The last column
  of the section's table (lines 535–542), `prewhiten_fixed_tables.md` and `derived_r24.out` lines 69–77 agree cell
  by cell; the one interval that excludes zero is [+0.057, +0.845], of that cell (item 6 below).
- S3 Text §8 (line 544), the estimate: "carries −0.0037 [−0.0066, −0.0008] (p = 0.0145, negative in 12 of 14;
  `derived_r24.out`, item 1)". `prewhiten_fixed_tables.md` line 127 ("predicted -0.0037");
  `notes/review_results/inference_rows_prewhiten_fixed.csv` line 165 (−0.0036993, p = 0.0145263671875, `n_neg` 12);
  `derived_r24.out` line 38; recomputed (item 1 below). Observed, estimate and residual add up per subject (−0.012673
  = −0.003699 − 0.008973). The main text's Results 7 agrees with the two sentences: "the AR(1)-substituted estimate
  carries −0.0037 of it", the whitened series' own r₁ DiD "(−0.0927)", the correlation +0.333, and "the Fisher-z
  interval of neither correlation excludes zero" for +0.495 and +0.333 ([−0.048, +0.812] and [−0.240, +0.734]).
- S3 Text §10 (line 556): "received injections of ketamine and of other agents". The claim record's section on Gatica
  et al. (2024) (the review folder's `claims/claims_2026-10-01.md` lines 181–189): isoflurane; injections of ketamine
  and of five other agents, named; scanning about two hours after anaesthesia; S20 Table's row 4
  (`manuscript/supplementary.md` line 1725) has "3 macaques under isoflurane"; the search note
  (`pubmed_search/psychedelic_phiid_search.md` lines 93–95) words it likewise. The PDF was not opened here.
- S4 Text, item P5 (line 38): Results 7 states both values ("r₁ ≥ cos(2π × 0.08 Hz × 2 s) = 0.54 (flat in-band noise
  has 0.82)", `manuscript/draft_v2.md` line 158); S1 Text states the first only ("r₁ ≈ 0.82 on white noise at TR 2 s",
  line 5; "0.54" does not occur in S1 Text).
- S4 Text, row S6, last clause (line 53): "S19 Table's Part B gives the status of each". Part B has 18 rows at HEAD
  (`manuscript/supplementary.md` lines 1695–1712: the 13 of `checked3` and five added), each giving its
  computation's status in its first or third cell (post hoc; a review's or an audit's; without a pre-run entry, a
  prediction or a recorded rule; written after the numbers were seen). Each place of the main text and of S1, S2, S3
  and S5 Text that calls a computation post hoc or a review's, or says that it had no pre-run entry, no
  pre-specification entry or no pre-recorded rule (found by searching for those words), names a computation that
  has a row there: the review computations of 14 September, the finite-sample null, the sts-matched null, the
  centroid, global functional connectivity, the checks of 17 September, the leave-one-out on the primary DiD, the
  proportionality check, the residual's source, the third review's partial correlations, the whole-brain ΦR items of
  the regional report, and the numbers derived on 24 September (the leave-one-out on the cross-half relation) and
  for this revision (the regional relation on the windowed atoms). The result of Y2-1 is one that such a place
  covers and that Part A holds. The completeness of Part B beyond those places was not read again here.
- S4 Text, row R1 (line 62), first sentence, each place opened. Table 2 and Table 4: DiDs with inverted intervals and
  exact p, as their captions say. Results 4 (line 120): "−0.0924 [−0.1503, −0.0348]" and "+0.0115 [+0.0005, +0.0226]"
  with no p; Table 3's data row (line 130): the residual's only; neither p is in the main text; S17 Table has both
  (`manuscript/supplementary.md` line 628, row 223: 0.0037, inverted [−0.15032, −0.03484]; line 634, row 229: 0.0421,
  [+0.00047, +0.02265]). The data rows of the residual table of S3 Text §6 (lines 325–326): intervals and no p.
  Table 2's baseline-adjusted rows (lines 99 and 102 of the main text): intervals and no p, t intervals by the
  caption. The range "Results 2–7" is Y2-6.
- Row R1, second sentence, each contrast of the list: the main text gives it at no place with an interval, and the
  named place holds the interval. FD-residualised r₁ DiD "(−0.0123)" and the sensitivity variant's "−0.0216" (line
  106): S3 Text §4 (line 161), [−0.0210, −0.0031] and [−0.0331, −0.0102]. Early and late residual DiDs "(+0.0179)"
  and "(+0.0064)" (line 120): S3 Text §6 (line 307), [+0.0086, +0.0272] for the early one (unrounded upper limit
  0.0272476); S17 Table rows 231 and 232 (lines 636–637). W = 30 "(−0.0686, p = 0.0042)" and windows 5–14 "(−0.0733,
  p = 0.0070 ...)" (line 87): S1 Table (lines 17 and 13), [−0.1142, −0.0242] and [−0.1238, −0.0238]. Lags 2, 3 and 5
  (lines 146 and 148; the sts DiDs with p, the lag-τ autocorrelation DiDs as point values): S14 Table (lines
  372–374), intervals of both. The deconvolved contrast "(−0.0782, p = 0.0013; ..." (line 171): S2 Text (line 7),
  [−0.1221, −0.0362]; S17 Table row 151 (line 556). The whitened series' r₁ DiD "(−0.0927)" (line 158): S3 Text §8
  (line 539) and S11 Table (line 298), [−0.1497, −0.0367]. What the estimate carries, "−0.0037" (line 158): S3 Text
  §8 (line 544); S11 Table has no interval of it, as "the first also in S11 Table" says. The count DiD (line 201):
  S3 Text §5 (line 299).
- Row R1, second sentence, completeness. The main text was read from the Abstract to the end of Methods, with every
  decimal number of the file before its list of supporting information listed and marked by whether an interval
  follows it at some place (563 distinct strings; the 291 signed ones that no interval follows read one by one, each
  in its sentence). Every DiD, and every difference between the runs or the periods, of the data that is printed as
  a point value or with its p and has an interval at no place of the main text is in the row's list (the eleven
  kinds above; the lag-τ autocorrelation DiDs of Fig 6's caption under "those at lags 2, 3 and 5") or among its
  exceptions: the 51 DiDs of Table 1, each with its count (the row of TDMI, the sum of the sixteen, taken here with
  the atoms' rows; its residual DiD, +0.0092, is also in the caption); the pair r₁ DiD (−0.0155) and the pair |q| DiD
  (0.0164); the centroid (+0.0023 Hz, p = 0.022). None is outside both. Not counted
  as such contrasts: those quoted with p at one place and given with their interval at another (the gaps and the
  runs' changes of Results 2, in Table 2; the FD DiD of the Discussion, in Table 2; −0.054 and −0.081 of the
  Discussion); single subjects' values (−0.064, +0.024, +0.0935); shares, ratios and slopes; the excesses over the
  three expectations (0.0088, 0.0066, 0.0061), which are the residual DiD less a simulated value; bounds on p
  ("p ≤ 0.008", "0.085 or more"); the regional contrasts of Results 3 and Fig 4; simulated quantities.
- S5 Text §1 (line 7), the three checks of the review of 17 September 2026, each found in
  `notes/fresh_review_2026-09-17/checks/` with its script and at its place of S3 Text: `check_A1_atoms_family.log`,
  part 4 ("191 x 191 = 36481 points; points with |d/dq| > |d/dr1|: 0"), at §4 (line 128);
  `check_C1_residual_vs_null.log`, part (2) (−0.01373, negative in 14/14, the null's −0.00450, p = 0.0001), at §6
  (line 307); `check_C2_variance_ratio.log` (+0.974, and +0.946 with the ratio partialled out), at §9 (line 550).
  The other three checks of that folder (`check_A2_ratio_range`, `check_B1_did_recompute`, `check_I1_fig4_scale`)
  are named at no place of S3 Text. The words "as review computations" are Y2-5.
- S5 Text §5 (line 33), the counts, from the files of the review folder's `audit/`: 63 + 57 + 32 = 152 findings in
  the three audits' files; 33 + 9 + 25 + 10 + 11 + 13 + 17 + 12 + 10 + 17 = 157 in the ten `check_V*.md`;
  5 + 7 + 12 + 14 + 16 + 20 + 12 = 86 in the seven `recheck_W*.md`; 11 + 10 + 13 + 8 = 42 in the four
  `recheck_X*.md`; the last part of the dispositions has 42 paragraphs.

**2. The derived numbers.**

- The difference of the script from `checked3`: the docstring's last clause, the second block of item 1, the second
  block of item 6, items 13 and 14; nothing else. The clause names what the blocks compute: three inverted intervals
  (what the estimate carries of the whitened contrasts, four cells; the directed response's difference between the
  runs; the count DiD) and the Fisher-z intervals of the eight correlations. The script draws no random number.
- Run on the copy from the repository root, the script's output equals the committed `derived_r24.out` from the
  second line to the last (103 lines; the first reads `git=nogit` for `git=8bd189e`). The files of
  `notes/review_results/` and `notes/rev_inference_inverted.py` do not differ between 8bd189e and HEAD.
- The files the script opens (recorded while it ran; it ran on a copy that held no others): two pickles
  (`notes/review_results/inference_rows_prewhiten_fixed.pkl`, `inference_rows_prewhiten.pkl`); eight CSV files
  (`notes/review_results/inference_rows_raw.csv`; `baseline_gap.csv`, `regional_partial.csv`, `matched_slope.csv`,
  `splithalf_subjects.csv`, `regional_sts_r1.csv`, `directed_crosslag.csv`, `censoring.csv`); five tables files
  (`inference_revision_tables.md`, `prewhiten_fixed_tables.md`, `baseline_gap_tables.md`,
  `directed_crosslag_tables.md`, `censoring_tables.md`); three array files
  (`notes/review_results/regional/regional_atoms_raw_ts_gsr_win60.npy`, `diag_series_ts_gsr_W60.npz`,
  `diag_series_ts_demean_W60.npz`); one log (`splithalf.log`). The delta added two of the CSV files and three of the
  tables files. The count "two pickles of per-subject vectors, eight CSV files, five tables files, three array files
  and a log" stands so in S19 Table's Part B (`manuscript/supplementary.md` line 1711), in the record's last entry
  (`manuscript/analysis_record.md` lines 9165–9166) and in the review folder's `README.md` (lines 67–68); the
  additions that the row, the entry and the README name for the third check are those of the script.
- The inversion. `signflip_inversion` (`notes/rev_inference_inverted.py`) takes p(μ) as the share of the 2¹⁴
  assignments with |Σ sᵢ(xᵢ − μ)| ≥ |Σ(xᵢ − μ)| (relative tolerance 10⁻¹²) and the interval as {μ : p(μ) > 0.05}. Two
  inversions were written apart from it. One is exact: above the mean an assignment counts exactly when the mean of
  one of its two sign groups is at least μ, so that the upper limit is the 409th largest of the 16,382 means of the
  proper subsets, and the lower limit the 409th smallest (820 of 16,384 assignments is the smallest count above
  0.05); each limit was confirmed by the direct count just inside and just outside it. The other is a bisection on a
  p function with its own enumeration of the assignments. The three agree within 3 × 10⁻⁸ on the ten vectors below,
  and no limit is nearer than 8 × 10⁻⁷ to a rounding boundary at its printed precision.
- Item 1, the second block, from `did_subjects` of the pickle (mean [interval], exact p, negative of 14):
  ar10 ts_gsr −0.0100 [−0.0198, −0.0009], 0.0289 (474 of 16,384), 9; ar10 ts_demean −0.0044 [−0.0086, −0.0003],
  0.0338 (554), 10; ar20 ts_gsr −0.0037 [−0.0066, −0.0008], 0.0145 (238), 12 (unrounded limits −0.00657954 and
  −0.00082948); ar20 ts_demean −0.0010 [−0.0030, +0.0010], 0.3086 (5,056), 9. Equal to lines 36–39 of the output.
- Item 6, the eight cells: the correlation of the per-subject DiDs of "MMI sts" and "autocorr" and
  tanh(atanh r ± 1.959964/√11): p = 10: +0.445 [−0.112, +0.789]; +0.570 [+0.057, +0.845], the one that excludes
  zero; +0.168 [−0.398, +0.641]; +0.014 [−0.520, +0.541]; p = 20: +0.333 [−0.240, +0.734]; +0.081 [−0.469, +0.587];
  +0.157 [−0.408, +0.634]; −0.079 [−0.585, +0.471] (ts_gsr W = 60, ts_gsr global fit, ts_demean W = 60, ts_demean
  global fit at each order). Equal to lines 69–77 of the output, and each r to the one that
  `prewhiten_fixed_tables.md` prints under the cell's heading (the script's own comparison is Y2-4).
- Item 13, per subject DMT − placebo from `directed_crosslag.csv` (mean [interval], p, negative of 14): ts_gsr,
  `resp_anti_run` +0.00044 [−0.00061, +0.00149], 0.3800 (6,226), 7 (unrounded +0.00044457, −0.00060733, +0.00148800;
  the six-decimal rounding of the file's values cannot move a printed limit); ts_gsr, `rms_anti_run` −0.00052
  [−0.00372, +0.00266], 0.7313, 6; ts_demean −0.00012 [−0.00135, +0.00109], 0.8330, 7, and −0.00258 [−0.00733,
  +0.00195], 0.2714, 8. Equal to lines 97–100 of the output. `directed_crosslag_tables.md` line 12, in its block of
  ts_gsr at the run level, prints the two ts_gsr means and p (−0.00052, 0.7313; +0.00044, 0.3800); line 26 prints
  those of ts_demean, also equal.
- Item 14, per subject from `censoring.csv`, windows 6–14 minus 1–4, DMT minus placebo. `n_above`, in exact
  arithmetic (36 × DiD an integer): mean 47/42 = +1.119, limits −125/216 = −0.5787 and 427/144 = +2.9653, that is
  [−0.58, +2.97]; 3,548 of 16,384 assignments, p = 0.2166; 7 positive, 6 negative, one zero (subject 3). `mean_fd`:
  +0.0143 [−0.0115, +0.0403] (−0.01146694, +0.04025611), p = 0.2452 (4,018), 8 positive. Equal to lines 102–103 of
  the output and to the "mean" row of table (a) of `censoring_tables.md`; the fourteen per-subject values of each
  equal that table's columns. Table 2 of the main text gives the FD DiD as "+0.0143 [−0.0115, +0.0403], p = 0.2452"
  (line 103), and S17 Table's row 765 has [−0.01147, +0.04026] from the unrounded series
  (`inference_revision.csv` line 767: −0.0114654, +0.0402555).

**3. The dispositions.**

- X1-1 (dispositions lines 2298–2310): the four quotations stand word for word, two in S4 Text's row R1 and one each
  in S3 Text §5 and §8; the row lists the four contrasts that the finding names and its sentence is the one quoted;
  the two intervals are inversions of the sign-flip test on committed values (items 14 and 1); item 14 asserts the
  mean, the p and the count of positive subjects against the run's table, and item 1 the mean and the p against the
  run's file, whose sign count it prints beside its own (12 and 12). The words "had no interval anywhere" are Y2-7.
- X1-10 (lines 2367–2371): the quotation stands word for word in row R1; it answers the finding (Results 4 and Table
  3 for the two intervals without p, their p in S17 Table, Results 7 and Table 4 added).
- Point (4) (lines 2544–2549): at `checked3` the interval [−0.00061, +0.00149] stood in no file of the tree but S3
  Text (`git grep`); item 13 holds it and S3 Text §6 names the item; item 6 holds the eight intervals, of which S3 Text
  §8 says that seven include zero and which it names; S3 Text §6 names `conversions_b26.out`, which holds the
  conversions. The Part B reading's report has these as its item 4 of the computations without a row and its
  borderline cases c and f (the review folder's `audit/partB_reading.md` lines 471–475, 496 and 502).
- Point (5) (lines 2551–2553): the quotation stands word for word in item P5; the item at `checked3` read "is stated
  in Results 7 and S1 Text" of both values; S1 Text states the first.

**4. The replacements file.**

- Each of the ten entries: its `old` stands once in the file at 8bd189e and its `new` once in the file at HEAD.
- S201: S19 Table names S2 Text for the regional check (line 1616); the values and the kind of interval as under 1;
  S2 Text's intervals are the inverted ones "except where marked" (line 3). The words "the report's first table" are
  Y2-2.
- S323: the values (+0.00044 [−0.00061, +0.00149], p = 0.3800; −0.00052, p = 0.7313) are those of item 13; the
  finding is in the Part B reading's report (line 471).
- S324: `conversions_b26.out` holds the recomputed conversions; the record's entry on B26's outcome names it (line
  8305).
- S417: the added sentences hold (X1-1 and X1-10 above; `derived_r24.out`, items 14 and 1), but for the words of
  Y2-7.
- S420: the third check found two computations without a row (X1-2); Part B has rows for both and three more, and
  the places that mark a computation as post hoc each have a row (under 1).
- S422: S1 Text states the first value and not the second; where it was found is Y2-3.
- S507: S3 Text §4 quotes the third check with its log, and S19 Table's Part B names it with the other two (line
  1702).
- S305, S311 and S314, compared with the file at `checked3`: the `new` of S305 gained the clause on the count DiD's
  interval; that of S311 the pointer to the eight intervals and the estimate's interval, p and sign count; that of
  S314 "injections" and "and of" for "an injection" and "with". Each is a change verified under 1. The `new` of S502
  changed too, by the clause "and a third by four more, 42 findings", also verified under 1.

**5. The rules.**

- No computation label (B1–B29, B16b, B16c, B17b) in `manuscript/draft_v2.md` before "## Supporting information"
  (line 391).
- No round, stage or bundle name and no reviewer's letter in the main text, S1–S5 Text or `supplementary.md`: "round"
  occurs only in "rounding" and "rounded"; "stage" in a cited work's title and its reported effect and in "the
  data-release stage"; "bundled" of third-party files; "B's" is the statistic B's.
- "Planning session" and "writer's session" occur in S5 Text §5 (line 33) and at no other place of the manuscript
  files.
