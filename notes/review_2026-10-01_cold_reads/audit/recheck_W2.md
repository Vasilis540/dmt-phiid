# W2 — S3 Text and the derived numbers

Scope: `manuscript/si/S3_Text.md` (the 16 places changed between `checked` and HEAD, and §5, §6, §8 read once against
the main text), `notes/review_2026-10-01_cold_reads/checks/derived_r24.py` and `derived_r24.out` (items 9–12 and the
changed docstring), and the twenty dispositions named in the task. HEAD of VT is eed9271. Nothing under VT was changed
(`git status` is empty after the check; no `__pycache__` was written). Scratch: `VW/W2/` (`tree/`, a copy of VT in which
the script was run; `my_b27.py`, `my_splithalf.py`, `my_b28.py`, `my_item1.py`, `my_ties.py`, `my_unrounded.py`, each
with its `.out`; `derived_r24_rerun.out`; `s3_worddiff.txt`). No internet, no subject data: every recomputation is on
committed result files.

**Result in one line.** No number in the changed text of S3 Text or in the new output of `derived_r24.py` disagrees
with the source it names. Seven findings: 1 error (a wrong computation label in a comment of the script), 3 inexact,
3 notes.

## Findings

**W2-1**
- Where: `manuscript/si/S3_Text.md` §6, paragraph "The residual's relation to r₁ across split halves" (line 406):
  "Their Fisher-z 95 % intervals at N = 14 are [−0.760, +0.183] and [−0.897, −0.270] on `ts_gsr`, and [−0.857, −0.099]
  and [−0.566, +0.493] on `ts_demean`". Same limits in `derived_r24.out`, item 10 (lines 73–74).
- Problem: the eight limits are those of the correlations as `splithalf.log` prints them, at three decimals, which the
  paragraph's last parenthesis and the item's label say ("from the log's printed values"). The unrounded correlations
  can be had from committed files, and three of the eight limits then differ in the third decimal:
  r(res_even, r₁_odd) on ts_gsr = −0.699541, interval [−0.897, −0.269] (upper limit −0.26869; printed −0.270);
  r(res_odd, r₁_even) on ts_demean = −0.597558, interval [−0.857, −0.098] (−0.09807; printed −0.099);
  r(res_even, r₁_odd) on ts_demean = −0.051497, interval [−0.567, +0.493] (−0.56660; printed −0.566).
  The fourth is unchanged (−0.384543: [−0.760, +0.183]). Nothing else of the paragraph moves at its printed precision:
  the four correlations, the means (−0.542042 and −0.324528), the reliabilities (0.494017, 0.741495, 0.215687,
  0.712298), the ceilings (0.605236, 0.391961), the ratios (0.895587, 0.827959), and "on each variant one of the two
  excludes zero and the other does not". The main text carries the four correlations only and is not touched.
- Evidence: `VW/W2/my_splithalf.py`: the residual's half DiDs from `notes/review_results/partB/diag_series_<variant>_W60.npz`
  (key `res`; the halves and the DiD of `notes/partB7_splithalf.py`, lines 40–41 and 50–52), the r₁ half DiDs from
  `partB/splithalf_subjects.csv` (`r1_odd`, `r1_even`). The reconstruction reproduces every value the log prints for
  these quantities (lines 4, 12, 16, 24: the two reliabilities, the two within-half and the two cross-half correlations
  of each variant), and the per-window r₁ of `partB/censoring.csv` gives the same four correlations (−0.38458, −0.69962,
  −0.59758, −0.05145). Item 6 of the same script computes the sts–r₁ cross-half correlations from the unrounded
  `splithalf_subjects.csv`, and the Fisher-z intervals that S3 Text has from B21 (d) (§5, line 167; §6, line 307) are
  of unrounded correlations (`notes/partB21_inference_revision.py`, lines 509–521).
- Grade: inexact

**W2-2**
- Where: `derived_r24.py` lines 303–306 and `derived_r24.out` lines 78–79: "12. The values B27's pre-run entry lists as
  known that baseline_gap_tables.md does not print, from baseline_gap.csv (ts_gsr, W = 60)".
- Problem: the label is not exact in two ways. (i) Of the eleven values printed under it, two are printed by
  `baseline_gap_tables.md`: the slope −0.753 and r = −0.780 of the residual DiD on the r₁ DiD; of that regression only
  the intercept +0.0005 is not. (ii) One value that the entry's item (i) lists as known and that file does not print,
  the ratio of means −0.788, is not under the label (it is in B28's tables file, as "B27, outcome" says; from
  `baseline_gap.csv` it is +0.011534 / −0.014646 = −0.7875). The nine values that the record's "B27, outcome" and the
  disposition of VO-6 name as not printed (r², the two SDs, the three of subject 14, the two of subject 8, the
  intercept) are all there and all equal the entry's.
- Evidence: `notes/review_results/partB/baseline_gap_tables.md` line 33: "All 14 subjects: slope -0.753 [-1.133, -0.373],
  r = -0.780"; `manuscript/analysis_record.md` lines 8621–8622 and 8628 (item (i): "intercept +0.0005, r = −0.780", "the
  ratio of means −0.788"); `partB/matched_slope_tables.md` line 6; `VW/W2/my_b27.out` (item 12).
- Grade: inexact

**W2-3**
- Where: `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`, VO-6 (lines 1035–1037): "from
  `baseline_gap.csv`, which `derived_r24.py` now recomputes and compares with the pre-run entry's values (item 12 of its
  output; S19 Table's Part B has the row)".
- Problem: item 12 recomputes and prints; it compares nothing. Its code holds no value of the pre-run entry, no
  assertion and no test of equality (item 11, beside it, does compare each cell with the tables file and counts the
  differences), and its output states no agreement. The comparison is the reader's: the eleven printed values do equal
  those of the entry's item (i), each checked here. The record's sentence ("B27, outcome", lines 8902–8907) does not say
  "compares" and is right as it stands.
- Evidence: `derived_r24.py` lines 303–321; `derived_r24.out` lines 78–79; `manuscript/analysis_record.md` lines
  8608–8628.
- Grade: inexact

**W2-4**
- Where: `derived_r24.py` line 217, the comment that heads item 10: "# 10. The cross-half correlations of the residual
  DiD with the r₁ DiD, which the main text quotes (B19's log): their".
- Problem: `splithalf.log`, which the item reads, is the log of the split-half test, B7, not of B19. B19's outputs are
  `exchange_rates_tables.md`, `bca_intervals.csv` and `exchange_rates_run.log`, and its part (c) is the cross-half
  correlation of the sts and r₁ DiDs, not of the residual. The fault is in a comment only: the item's printed label
  names the file and no computation, and no number depends on it.
- Evidence: `notes/partB7_splithalf.py` lines 20 and 141 (writes `splithalf.log`); `run_all.sh` line 153;
  `notes/partB19_exchange_rates.py` lines 32–33 and 228–229; `S3_Text.md` §6, line 382 ("a split-half test … (`notes/partB7_splithalf.py`)").
- Grade: error

**W2-5**
- Where: `S3_Text.md` §5, "What the tables say" (line 260): "three assignments and their mirrors lying within the file's
  rounding of the observed mean (`derived_r24.out`, item 11)"; `derived_r24.out` line 77: "within 1e-6 (the bound of the
  file's rounding on a difference of two means)"; the same count in the disposition of VS-12.
- Problem: the count is right for the criterion the script states: three pairs of assignments, the observed one apart,
  have an absolute mean within 10⁻⁶ of the observed absolute mean (0, 0.43 × 10⁻⁶ and 0.71 × 10⁻⁶ away). But 10⁻⁶ is
  not the bound that the file's rounding sets here. The two absolute means are built from the same fourteen rounded
  values; their difference is −2/14 of the sum of the values in one of the assignment's two sign groups, and the
  rounding moves it by at most k/14 × 10⁻⁶, k the number of values in that group. By that bound two of the three pairs
  can lie on the other side in the unrounded values, and the third cannot:
  (i) the pair that flips subjects 4, 6, 7, 8 and 10: the other nine values (subjects 1, 2, 3, 5, 9, 11, 12, 13, 14)
  sum to exactly 0 in the file, an exact tie, which the test's "≥" counts (bound 0.64 × 10⁻⁶);
  (ii) the pair 0.43 × 10⁻⁶ above the observed absolute mean (seven values; bound 0.50 × 10⁻⁶);
  (iii) the pair 0.71 × 10⁻⁶ below it (five values; bound 0.36 × 10⁻⁶) is not counted in the file and cannot be counted
  in the unrounded values either.
  This supports the paragraph's account (one pair leaving the 3,068 gives 3,066 and 0.1871, the run's value) and narrows
  its "three" to two. The run's count itself cannot be recomputed from the tree: the unrounded r₁ gaps need the data.
- Evidence: `VW/W2/my_ties.py`, exact integer arithmetic on the fourteen `pre_gap` values of `r1, ts_demean, 60` in
  `baseline_gap.csv` (in units of 10⁻⁶: 4601, −3590, −2004, 16443, −10056, 6760, 14214, 18661, 17335, 19125, 3797,
  25170, −7457, −27796; sum 75203): 3,068 assignments counted; differences of the sums 0, +6 and −10 for the three
  pairs; for every other assignment the difference is 16 or more in size.
- Grade: note

**W2-6**
- Where: `S3_Text.md` §6 (line 406): "so that against what the reliabilities allow the two variants stand alike".
- Problem: the numbers are as given and the two ratios (0.90, 0.83) do follow from them. What the reading rests on is
  the ratio of the means alone: on each variant the larger of the two correlations is itself above the ceiling that the
  means are set against (|−0.700| against 0.605 on ts_gsr; |−0.598| against 0.392 on ts_demean, 1.5 times it), and the
  reliability that makes the ts_demean ceiling, 0.216, has p = 0.459 in the log. The paragraph does not say so; S3 Text
  §5 (line 165) marks a ceiling of the same kind with "(point estimates at N = 14)".
- Evidence: `notes/review_results/partB/splithalf.log` lines 4, 12, 16 ("residual DiD: +0.216 (p = 0.459; ρ +0.143)")
  and 24; `derived_r24.out` lines 73–74; `S3_Text.md` line 165.
- Grade: note

**W2-7**
- Where: `dispositions_revision.md`, VT2-6 (lines 1333–1334): "The sentence of S3 Text §9 is committed text and uses the
  word of the scale of sts, not of the change in r₁; it is kept."
- Problem: the reason for keeping holds: the sentence is committed text (line 420 of the file at 8bd189e) and does not
  use the word of the change in r₁. The gloss "of the scale of sts" is not what the sentence says: its "scale" is the
  variance of the series in a window against the run's (the ratio it speaks of), which, two sentences earlier, "cannot
  enter its atoms". The same gloss stands in the disposition of T61 (iii) (line 724) and in the record's entry on the
  revision (line 9243).
- Evidence: `S3_Text.md` §9, line 550: "No contrast is residualised on the ratio: for the windowed estimator that would
  remove the part of the r₁ change that coincides with the variance change, not an artefact of scale."
- Grade: note

## Checked and found exact

**1. The delta in S3 Text** (`git diff --word-diff checked HEAD`: 16 changed places, 18 lines added, 14 removed; every
one read against its source).

- §3, heading of the transfer-entropy paragraph, "(written for the revision of 1–2 October 2026)": the paragraph is
  absent from the file at 8bd189e; its body is unchanged from `checked`.
- §5, §6, citations of the record (lines 231, 264, 395) and §8 (line 531): the eight titles are the record's headings
  word for word (lines 8575, 8671, 8757, 8816; 8875, 8975, 9042, 9089); the pre-run entries are of 1 Oct 2026 18:50
  UTC; the date now follows the pre-run entry's title alone in the three places of §5 and §6, and §8 cites both entries
  of B16c by title.
- §5 (c), "+0.953 with all 14 subjects and +0.921, +0.931 and +0.846 in these three sets": equal to
  `baseline_gap_tables.md` (c) (line 33 and the three named rows) and recomputed from `baseline_gap.csv`; the whole of
  (c) recomputed (slopes and t intervals, the counts 0/0/11/11 and 1/13/71/63, the ranges of r, SE 0.0051, 0.0155, the
  three excesses, g = 0.611, −0.01465, 0.00530): no difference.
- §5, the parts of the DiD's variance, recomputed with my own code from `baseline_gap.csv` (sts, ts_gsr, W = 60):
  Var(post gap)/Var(DiD) = 0.299728, Var(pre gap)/Var(DiD) = 0.349233, −2 Cov/Var(DiD) = 0.351039 (sum 1); 1 − 0.2997 =
  0.700272; 1 − 0.3492 = 0.650767; r(pre gap, post gap) = −0.542507; r(DiD, post gap) = +0.868073; r(DiD, pre gap) =
  −0.887967 (r² 0.788); SDs 0.088676, 0.048548, 0.052404. These are 0.30, 0.35, 0.35, 0.70, 0.65, −0.543, +0.868,
  −0.888, 0.79, 0.0887, 0.0485, 0.0524, as the text and items 2 and 9 have them. The same from the full-precision
  committed series (`results/atoms_win60_115regions-all_ts_gsr_window.npy`): 0.299727, 0.349232, 0.351041, −0.542511,
  +0.868075, −0.887968, so no printed value rests on the file's rounding. Each sentence says what the numbers give: the
  three parts sum to the whole; "the other 0.70" is the pre-injection gap's variance plus the covariance term; 0.65 is
  the post-injection gap's plus the covariance term; +0.868 against −0.888.
- §5, the note on table (a): all 120 cells (12 rows × 10) recomputed from `baseline_gap.csv` with code of my own (the
  2¹⁴ sign assignments enumerated by bit pattern; the exact p with the run's tolerance and, separately, in exact integer
  arithmetic; the inverted sign-flip interval by bisection of my own p(μ); intercept and slope with t intervals on 12 df
  by the textbook formulas; the two correlations): 119 cells equal the run's table as printed; the one that does not is
  the p of r₁'s pre-injection gap on ts_demean at W = 60, 3,068/16,384 = 0.187256 (0.1873) against the table's 0.1871;
  3,066/16,384 = 0.187134 is the only even count that prints 0.1871 (3,064 prints 0.1870, 3,068 prints 0.1873), and the
  count is even because an assignment and its mirror have the same absolute mean. Three pairs lie within 10⁻⁶ (W2-5).
  For the nine rows of sts, the substituted sts and the residual the counts from the unrounded committed series equal
  those from the file. The paper prints the run's value: S3 Text table (a) (line 242), Table 2 (main text, line 100), "B27,
  outcome" (d). S3 Text's tables (a) (12 × 13 cells) and (b) (3 × 10) equal the run's cell for cell.
- §5, heading of the censoring table (a): `partB29_censoring.py` lines 81–84 (count = TRs above 0.4; share = count over
  the run's finite-FD TRs; mean FD = mean over all the run's TRs). Recomputed from `censoring.csv`: with share =
  count/840 and mean FD = the mean over the run's fourteen windows, all 14 rows and the mean row reproduce (23.6 (0.028),
  0.137; 10.1 (0.012), 0.126; 0.68 / 1.75, 0.75 / 0.70; +1.12, p = 0.2166, 7/14; +0.0143, p = 0.2452, 8/14; subject 8's
  +0.0935 the largest); subject 7's DMT share (0.121) tells 840 from 839. S3 Text's tables (a) (15 × 6) and (b) (2 × 6),
  (c), the four lines of (d) and (e) equal `censoring_tables.md`.
- §5, "(d) … confirmed on `ts_gsr`, the variant the script reads for this check": `partB29_censoring.py` line 123 reads
  `ts["ts_gsr"]` only; the pre-run entry's (d) is the check, not counted (record lines 8800–8801); Methods (Dataset)
  and S19 row B29 (d) say the same.
- §6, the sentence under the residual table: the data row prints "+0.0115" and "pair r₁ −0.0155"; 0.0115/0.0155 =
  0.7419; the pair r₁ DiD is in `partB/residual_source.log` line 10 at four decimals ("primary DiD -0.0155") and in no
  committed array (the `diag_series` files hold no pair a; `crosslag_deviation.csv` holds it per run only); Results 4
  has "(−0.74 per unit of pair r₁, from the printed means)" and S13 Table's note "the printed means: the pair r₁ DiD is
  saved at four decimals". Caption and body of the table are unchanged from `checked`.
- §6, the paragraph that introduces B28: `read_B.md` MAJOR 3 has "The like-for-like comparison is the per-subject OLS
  slope computed inside generator replicates with heterogeneous Δa matched to the data's spread"; `read_A.md` M1 says
  "the per-subject slope comparison is the right test" and names "a within-window non-stationarity control (injection
  ramp in r₁ and variance inside the window …)" as missing; the ramp is conditions (ii) and (iv)
  (`partB28_matched_slope.py` lines 22–28 and 219). "the SD with divisor 100": the script's `.std()` (lines 244–245;
  N_REP = 100); recomputed from `matched_slope.csv` (10 header fields, 11 per row, 100 replicates per condition): the
  table's four rows reproduce with divisor 100 and not with 99 (e.g. 0.091 against 0.092); S3 Text's table equals the
  run's.
- §6, the split-half paragraph, from the log's printed values, with my own code: the four correlations (log lines 12
  and 24: −0.385, −0.700; −0.598, −0.051), their intervals as printed (−0.76028, +0.18295; −0.89731, −0.26952;
  −0.85675, −0.09875; −0.56626, +0.49292), means −0.5425 and −0.3245, reliabilities 0.494, 0.741, 0.216, 0.712 (log
  lines 4 and 16), √(0.494 × 0.741) = 0.60502, √(0.216 × 0.712) = 0.39216, ratios 0.89666 and 0.82746; all equal item
  10. The pointers hold: Results 4 gives the four correlations without a verdict (main text, line 124); the split-half
  test stands above the paragraph; the pre-run entry of the split-half test (record lines 2469–2491) records no
  prediction for these correlations. (The intervals from unrounded values: W2-1.)
- §8, line 505 and line 544, "its levels are means over both runs and all windows": `partB16_prewhiten.py` line 205 and
  `partB16c_prewhiten_fixed.py` line 184 (`np.nanmean(R['obs'])`, `R['pred']`, `R['obs'] - R['pred']`, over the whole
  14 × 2 × 14 array). From the saved arrays (`prewhiten_atoms_arp_ts_gsr_mmi_win60.npy`,
  `prewhiten_fixed_atoms_ar10/ar20_ts_gsr_mmi_win60.npy`): sts over both runs and all windows 0.2766, 0.0861, 0.0705;
  over DMT windows 1–4 0.2202, 0.0866, 0.0719. The CSV rows of the diagnostic give other pre-injection values (e.g. the
  residual at p = 10 and 20: 0.0511, 0.0605), so the quoted levels are not pre-injection means. The values quoted
  (0.2766, 0.2438, +0.0328; −0.0262, −0.0181, −0.0080, 8/14; 0.0861, 0.0296, +0.0564; 0.0705, 0.0080, +0.0624; −0.0091,
  11/14; −0.0090, 12/14; −0.0037) equal `prewhiten_tables.md` line 29 and `prewhiten_fixed_tables.md`.
- §8, the date: B16c ran from 21:01:08 to 21:35:08 UTC on 1 October (`b27/evidence.txt`: 00:01:08 local on 2 October;
  "B27, outcome", lines 8883–8885); S5 Text §4 and the main text (line 267) give 1 October.
- §8, the reviewers: `read_B.md` MINOR 4 ("Compute the atoms there."); `read_A.md` m4 ("Prewhitening is presented
  one-sidedly."). S5 Text §5 names the three cold reads by role.
- §8, (e): `prewhiten_fixed_tables.md` has xtx and yty as two rows in each of its eight atom tables and no entry for
  their sum; it holds the CCS atoms, the global-fit tables and the four diagnostic lines; the eight "MMI xtx+yty" rows
  are in `inference_rows_prewhiten_fixed.csv` and in item 1 (all 32 rows of item 1 recomputed from the pickle with my own
  interval code: no difference; ts_gsr W = 60: −0.0229 [−0.0409, −0.0053], p = 0.0077; −0.0060 [−0.0098, −0.0022], p =
  0.0037). The pre-run entry's (e) is as quoted (record lines 8857–8858).
- §10: the string of the second PubMed search is in S3 Text character for character as in
  `psychedelic_phiid_search.md` (526 characters), the first as in `search_string.txt` (318); the exports hold 2 and 11
  records; ketamine is among the second string's terms; in S20 Table and in the literature file's Table A only row 5
  names ketamine ("sevoflurane, propofol or ketamine"), and the search record has the same account of that study and of
  why the string does not return it. Gao et al. (2026): found by the PubMed search of 1 October 2026 and read in full
  that day, by the reference list, `screening.md`, the literature file and S20 Table's head note; the row "added in the
  revision of 1–2 October 2026" in the literature file's title and in the head note; Methods (Literature search) agrees
  (11 records; 2 records). The clause on the data-driven variant of Liardi et al. (2025) and, in §11, Theorem 1 of
  Rosas et al. (2020) "of order k" agree with the claim record (its lines 197–198 and 115), and nothing in them
  contradicts another place of the paper. Not checked here, as the task leaves them to another session: these
  statements, and those on Luppi et al. (2026), against the works themselves.
- Rules: S3 Text at HEAD carries no round, stage or bundle name, no reviewer's letter (the "B's" of line 372 is the
  statistic B) and no session name; the reviewers are named by role.

**2. `derived_r24.py` and `derived_r24.out`.**

- The diff: the docstring, three imports and items 9–12; items 1–8 and their output are unchanged from `checked`.
- Run in the copy (`VW/W2/tree`, from its root): exit 0, no stderr, 79 lines, identical to the committed
  `derived_r24.out` but for the header (`git=eed9271` against `git=8bd189e`). The result files the script reads are
  unchanged between 8bd189e and HEAD (`git diff --stat 8bd189e HEAD -- notes/review_results results` is empty), so the
  committed header names the commit whose files were read.
- Item 9: reads `baseline_gap.csv` (sts, ts_gsr, 60), DiD = post − pre, variances and covariance with ddof 1; the
  printed line equals my values (above).
- Item 10: the two regular expressions take, per variant, the residual's and the autocorrelation's split-half
  reliabilities and the two "cross" correlations of the "context" line; Fisher z with 1.959964/√11; the two printed
  lines equal my values.
- Item 11: parses the 12 rows of table (a) (10 cells each), recomputes with `signflip_inversion`, the run's count rule
  and the run's OLS, compares as printed; "cells compared 120 …; recomputed as printed 119; not 1", "3068", "3066" and
  "3 assignments and their mirrors" all reproduce with my own code.
- Item 12: each of the eleven printed values equals the value of the pre-run entry's item (i) (record lines
  8608–8628): r² 0.79 (0.788487); SD of the DiD 0.0887 (0.088676), of the post gap 0.0485 (0.048548); subject 14
  +0.0949, −0.1121, −0.0172; subject 8 −0.2795, +0.0914; slope −0.753 (−0.753312), intercept +0.0005 (+0.000502), r
  −0.780 (−0.780243). (Label: W2-2.)
- Docstring: the list of what was added "after the checks of the corrected revision" is items 9–12; no random draw is
  made; the files read are per-subject vectors, one array, CSV files, two tables files and a log, all committed.

**3. The dispositions** (each read against the finding in its `check_V*.md` report and against HEAD).

- VO-2: S3 Text §8 says where the contrast of the sum is, as the disposition has it (line 544); the two contrasts that
  the disposition quotes from the record's entry are item 1's.
- VO-4, VS-1: the three places (lines 231, 264, 395) as the disposition says; §8 cites B16c's two entries by title.
- VO-12, VT2-7: S3 Text §8 says both things (lines 505 and 544); VT2-7's quotation is there word for word.
- VO-13: the quoted clause is in §5 (c) word for word; (c) is carried in prose with every value of the run's (c).
- VT2-6: kept, and the reason holds (the gloss: W2-7).
- VT2-15, VT2-16: the quoted heading (line 266) and "the SD with divisor 100" (line 395) are there and are right.
- VT1-9: the quoted sentence is under the residual table (line 337); the caption is as moved.
- VN-6, VN-9: the quoted texts are in §10 (line 558) and §11 (line 564) word for word; the claim record has both.
- VR-14: S3 Text §10 says found by the search of 1 October, read in full on that date, added in the revision of 1–2
  October; the head note of S20 Table and the literature file say the same.
- VS-2: "computed on 1 October 2026" (line 531), the date of S5 Text §4 and of the main text.
- VS-8: both quoted clauses are in §6 and §8 word for word and agree with the two cold reads.
- VS-11: "confirmed on `ts_gsr`, the variant the script reads for this check" (line 299).
- VS-12: stated as the disposition says, with 3,066, 3,068 and 16,384; item 11 recomputes the 120 cells (the count of
  three: W2-5).
- VM-3: Results 2 leads with the SDs, as quoted (main text, line 87); S3 Text §5 has the parts and "not an
  apportionment".
- VM-5: Results 4 has the quoted sentence word for word (line 124); S3 Text §6 sets the four against their ceilings
  (the intervals: W2-1).
- VO-6: the nine values and the ratio's place are as the disposition says ("compares": W2-3).

**4. S3 Text §5, §6 and §8 against the main text's Results 2, 4 and 7 and Tables 2, 3 and 4.**

- Every decimal number of Table 3 (55 distinct) is in S3 Text §5 or §6 with the same digits. Table 2's gaps, adjusted
  contrasts and DiDs of sts and r₁ on both variants equal table (a) of §5; Table 4's five rows agree with §8 (0.848,
  0.751, 0.263, 0.137, 0.052 against +0.8479, +0.7506, +0.2625 (0.262547 in the CSV), +0.1368, +0.0524; 0.1 %, 0.3 %,
  33.8 %, 51.2 %, 59.7 %; the levels 1.1554, 0.7176, 0.2202, 0.0866, 0.0719, of which §8 has the first two as 1.155 and
  0.718; the DiDs, intervals, p and r that §8 carries).
- Results 2: 0.0887, 0.0485, −0.888, 0.79; −0.0686 (0.0042); −0.0146 [−0.0261, −0.0037], 0.0106; −0.0122, −0.0110,
  +0.0025 (0.4417); −0.844, +0.939, +0.824; 0.953 [0.854, 0.985]; 0.694, [0.258, 0.895], 0.729, 0.95 [0.62, 0.99], 366;
  subject 8 (−0.064, 24, 23.6, +0.0935) and subject 14 (+0.024); 0.486, 0.571, 0.90, 0.92, 0.68–0.83; 4.26.
  Results 4: +0.0115 [+0.0005, +0.0226]; +0.0179, +0.0064; +0.0027 ± 0.0014, +0.0049 ± 0.0017, +0.0054; 0.108, 0.218,
  0.251; 0.0051, 0.0155, 0.0088, 0.0066, 0.0061; −0.18, −0.39, −0.37; −0.75 [−1.13, −0.37]; 0.0001 and 0.0006; −0.79
  (−0.788 in §6) and −0.74; g = 0.61; −0.700, −0.385, −0.598, −0.051. Results 7: −0.0127 [−0.0203, −0.0052], 0.0002, 13
  of 14; 18 % and 7 %; −0.0927; +0.333, +0.495; −0.0037. Limitations and Methods (Dataset): 23.6, 10.1, +1.12 (0.2166, 7
  of 14), −0.107 (+0.037), −0.124 (−0.025); the non-finite TR. Each of these has the same value at the printed precision
  in S3 Text §5, §6 or §8. Two counts of the main text that these sections do not carry, "negative in 12 of 14" (r₁ DiD)
  and "positive in 10 of 14" (residual DiD), agree with item 2 of `derived_r24.out` (2 and 10 positive DiDs).
