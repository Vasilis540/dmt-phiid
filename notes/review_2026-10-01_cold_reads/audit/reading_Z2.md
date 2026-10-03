# Z2 — the record, the dispositions file, the bookkeeping files, the numbers table and the replacements

Reading of the last corrections of the prepared revision. Tree: VT at HEAD (9f89c23), against `checked4` (26156b8),
`checked3` (f50c1d3) and 8bd189e. Part: `manuscript/analysis_record.md` (its last five entries),
`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`, `CLAUDE.md`,
`notes/review_2026-10-01_cold_reads/README.md`, `manuscript/main_text_numbers.csv`,
`notes/review_2026-10-01_cold_reads/checks/apply_revision.out` and the replacements file
`notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json` (below: the JSON).
Paths are relative to VT. "The record" is `manuscript/analysis_record.md`; "the dispositions file" is
`audit/dispositions_revision.md`; "the main text" is `manuscript/draft_v2.md`; "the claim record" is
`claims/claims_2026-10-01.md`; `audit/`, `checks/`, `claims/` and `revision/` are the folders of
`notes/review_2026-10-01_cold_reads/`. "CSV line n" is the line of the numbers table at HEAD (line 1 its head note,
line 2 its column names). Line numbers are those of HEAD. Nothing under VT was changed (`git status --short --ignored`
is empty at the end, and no `__pycache__` was written); the scripts that write were run on copies under VW/Z2/, the
scripts that only print were run from copies under VW/Z2/ with VT as their input. No internet, no subject data: every
computation is on committed files.

**Result.** 5 findings: 0 errors, 3 inexact, 2 notes. Apart from them, no number, count, grade, date, locator or
quotation that was changed or added between `checked4` and HEAD in the files of this part disagrees with its source.
The inexact statements are one clause of the record's new passage on the fourth check (the count of scripts that it
implies), one sentence of the disposition of Y1-4 (where the head note's clause had been repeated), and the
parenthesis that the correction for Y1-4 put into S17 Table's source note, which that disposition quotes (the
sentence itself is in a file of another part). Each of the 38 dispositions of the fourth check carries its report's
grade, is true of the files at HEAD with every quotation at the place named, word for word, and answers its finding
in full; each states its finding fairly, Z2-2 apart. The two notes are of paragraphs of the dispositions file that
were amended in answer to the fourth check.

## Findings

**Z2-1**
- Where: the record, the entry on the revision, "The audits of the prepared revision" (lines 9531–9532):
  "`derived_r24.py` compares the eight whitened correlations with B16c's printed values cell by cell, and the parse
  check covers the fifth script that this commit adds."
- Problem: The commit adds four scripts and changes one. The script that the parse check now covers,
  `audit/te_filter_check.py`, is the fifth of the five that the commit adds or changes, and one of the four that it
  adds; as the clause is written it counts five scripts added. The first paragraph of the same entry has the count as
  it is: "the five scripts that this commit adds or changes".
- Evidence: `git -C VT diff --name-status 8bd189e HEAD` lists five `.py` files and no other script:
  `A …/audit/te_filter_check.py`, `A …/checks/abstract_summary.py`, `A …/checks/derived_r24.py`,
  `A …/checks/figures_check.py` and `M scripts/15_figures_v2.py`; the record, lines 9156–9158;
  `checks/scripts_check_revision.out` (five lines, the fifth that of `te_filter_check.py`).
- Grade: inexact

**Z2-2**
- Where: the dispositions file, last part, Y1-4 (lines 2646–2647): "The closing section of the part on the third check
  and the reason recorded with the replacement repeated the clause."
- Problem: The second place is not the reason. The report names "the `new` text of replacement U09h", that is, the
  head note itself as the JSON holds it. At `checked4` the reason (`why`) of U09h says nothing of S17 Table, and no
  reason of the JSON held the clause. In this part "the reason recorded with the replacement" is the `why` elsewhere
  (Y2-2, Y2-3, Y2-7, Y3-10). The rest of the paragraph holds: the three quotations stand at their places, and the
  closing section and the `new` of U09h have the clause as corrected.
- Evidence: `audit/recheck_Y1.md`, lines 134–136; the JSON at `checked4`: "every saved per-subject quantity" occurs in
  the `new` of U09h and in no `old` or `why` of any entry; the `why` of U09h there ends "and its cells completed by
  the rule now stated".
- Grade: inexact

**Z2-3**
- Where: the dispositions file, W4-11 as amended (lines 2059–2060): "The list has "the parse check of the five
  scripts" (four when the second check read it; the check covers the fifth since the fourth check, Y3-1)".
- Problem: The pronoun can be read of two things. Read of the list, which is the subject of the sentence, the clause
  is not so: when the second check read the list it named no parse check at all, which is what W4-11 found; "the
  parse check of the four scripts" came into the list as the correction for that finding, and it was the third check
  that read the list with "four" (X2-7). Read of the check's output, the clause holds: that file had four lines when
  the second check read it, and until the fourth check.
- Evidence: `audit/recheck_W4.md`, W4-11 (lines 178–186: the list as quoted there has no parse check;
  "`scripts_check_revision.out` (4 lines"); `git show checked3:manuscript/analysis_record.md`, line 9156: "the parse
  check of the four scripts"; `audit/recheck_X2.md`, X2-7 (lines 119–120); the paragraph of W4-11 at `checked3` and
  at `checked4`, which has "four" without the parenthesis.
- Grade: note

**Z2-4**
- Where: the dispositions file, the closing section of the part on the third check, point (2) (lines 2545–2551):
  "Eleven cells were completed by that rule: those of … of the coupled family (the reading kept S18 Table there with a
  gloss, … since the fourth check the cell does not name it, by the rule: Y1-9)".
- Problem: With the correction for Y1-9 the count no longer holds of eleven. The reading added no place to the cell of
  the coupled family: it added a gloss to "S18 Table", which the cell named before, and the fourth check's correction
  removed the table. At HEAD the cell is that of `checked3` less a place, which is the case of the leave-one-out's
  cell, set apart in the same paragraph ("no longer names S4 Text, by the rule"). Ten of the eleven cells name more
  places than at `checked3`. The parenthesis itself says what was done to the cell.
- Evidence: the cell at 8bd189e and at `checked3`: "Results 1; Fig 1c; S3 Text §3; S18 Table"; at `checked4`: "…; S18
  Table (the family named in the rows of B23 (a3), whose values those are)"; at HEAD (`manuscript/supplementary.md`,
  line 1700): "Results 1; Fig 1c; S3 Text §3". The second cells of the other ten rows (lines 1695–1699, 1702, 1704,
  1705, 1711 and 1712) compared at `checked3` and at HEAD: each gains places.
- Grade: note

**Z2-5**
- Where: the dispositions file, Y1-4 (lines 2648–2651), the text it gives as the correction of S17 Table's source
  note (`manuscript/supplementary.md`, line 400, a file of another part): "(the per-subject values that the run of 1
  October 2026 saved, those of B27, B29 and B16c, are not among them; their intervals are in S3 Text §5 and §8 and in
  S11 Table)".
- Problem: The quotation stands; the parenthesis that the correction added says more than holds. (i) "their intervals
  are in …": B16c's file holds 264 rows with a per-subject vector, 44 quantities in six window sets. S3 Text §8 and
  S11 Table print inverted intervals for the primary set of the MMI-sts, CCS-sts and whitened-r₁ contrasts of the eight
  cells and for one contrast of the AR(1)-substituted estimate; they give the diagnostic's residual DiD at p = 10 and
  20 as point values with sign counts, and S3 Text §8 itself sends the reader to `derived_r24.out` for the contrast of
  xtx + yty. (ii) "are not among them": the per-subject DiDs that B27's file saves, in its column `did`, are those of
  twelve quantities that S17 Table holds, and the mean-FD DiD that B29's file gives is S17 Table's "fd_did". What the
  table does not hold are the quantities that the run saved for the first time (the gaps, the counts of replaced
  volumes, the contrasts at the fixed orders).
- Evidence: `notes/review_results/inference_rows_prewhiten_fixed.pkl`: 264 rows, 44 labels in 6 sets, each with
  `did_subjects` of length 14, among them "prewhiten_fixed ar10 diag residual sts ts_gsr W60" and "prewhiten_fixed
  ar10 MMI xtx+yty ts_gsr W60"; S3 Text, line 544: "residual DiD −0.0091 (negative in 11/14) and −0.0090 (12/14)" and
  "the contrast of their sum is in `inference_rows_prewhiten_fixed.csv` and in `derived_r24.out`, item 1";
  `manuscript/supplementary.md`, S11 Table: 24 rows "the order fixed" (MMI-sts, CCS-sts and the whitened r₁ in the
  eight cells) and its note (line 331), which has the two residual DiDs without an interval.
  `notes/review_results/partB/baseline_gap.csv`: twelve groups of quantity, variant and window; the mean of `did` in
  each equals, at five decimals, the mean of a row of S17 Table (lines 628, 634, 646, 652, 664, 670, 1030, 1042, 1066,
  1078, 1102 and 1108; −0.08087 at line 1030), and for sts on ts_gsr at W = 60 the fourteen values equal the vector of
  `inference_rows_raw.pkl` within 5 × 10⁻⁷. S17 Table, line 1146 ("fd_did", +0.01435, inverted [−0.01147, +0.04026]),
  against `checks/derived_r24.out`, line 103 (from B29's `censoring.csv`: +0.0143 [-0.0115, +0.0403]).
- Grade: inexact

## Not checkable from the tree

That `recheck_Y1.md` to `recheck_Y4.md` are as the sessions returned them (the folder's README and the dispositions
file; each begins with its heading and none holds an absolute path). The day of the fourth check beyond the date of the
tree that the four read (`checked4` is dated 3 October 2026, 04:10 UTC; `checked3`, 00:46 UTC of the same day). That
26156b8 is not in the public repository. What a session said when it returned its report (the sentence written for
Y3-9; the report of X2 names X3 nowhere, as the sentence says). That each finding was read against the files before
anything was changed. The pages of the cited works' PDFs that the paragraphs of Y4-3 to Y4-5 and of X1-3 give (another
part; they are the pages of `audit/recheck_Y4.md`).

## Checked and found exact

**1. The record.**

- The rules. The file at 8bd189e (814,068 bytes) is a byte prefix of the file at HEAD (890,857 bytes); 709 lines are
  added. No line of the five entries is longer than 120 characters, headings apart (the longest has 120; no tab, no
  trailing space). The five headings carry "3 Oct 2026 05:55 UTC".
- The delta. The text from "## B27, outcome" was extracted at `checked4` and at HEAD, each paragraph's lines joined,
  and compared word by word: 42 paragraphs on each side; beside the time of the five headings three paragraphs differ,
  all of the last entry (its first paragraph; "The revision."; "The audits of the prepared revision"), in 16 spans.
  The four outcome entries are word for word those of `checked4`.
- First paragraph. `checks/scripts_check_revision.out` has five lines, of the five scripts that the parenthesis names,
  in its order; `git -C VT diff --name-status 8bd189e HEAD` (63 files: 47 added, 16 changed) lists those five `.py`
  files and no other script; the five parse. `derived_r24.py` opens two pickles (its lines 49, 168), eight CSV files
  (83, 98, 121, 135, 159 and again 294, 215, 438, 466), five tables files (113, 183, 344, 440, 468), three array files
  (211; 300, for both variants) and one log (282). Run on a copy that held the script, the module it imports and those
  nineteen files alone, it gives `checks/derived_r24.out` line for line from its second line (the first has
  `git=nogit` for `git=8bd189e`).
- "The revision." S2 Text differs from 8bd189e in two sentences (the head, line 3; the outcome of the regional check,
  line 9). In `manuscript/supplementary.md` the parts that differ from 8bd189e are the head note (line 3), one line
  each under S5, S12 and S13 Tables (lines 101, 335, 363), one sentence of S17 Table's source line (line 400), and S11,
  S18, S19 and S20 Tables. The sentence on the macaques agrees with S3 Text §10 (line 556: "received injections of
  ketamine and of other agents"; "scanned awake and under sevoflurane, propofol or ketamine"; "Data under anaesthesia
  are not counted here as psychedelic data") and with the claim record's item on Gatica et al. (lines 186–192).
- The amended sentences on the third check. The 42 findings of `audit/recheck_X1.md` to `recheck_X4.md` were read one
  by one: none is of a value of a result in the main text or in the supporting information (the nearest are pages of
  S20 Table's row 1, X1-3 and X4-1; a singular in S3 Text §10, X4-7; a count in `checks/numbers_update.out`, X2-1 and
  X3-5). S19 Table compared cell by cell at `checked3` and at `checked4`: the last cell of six rows of Part A (lines
  1610, 1622, 1625, 1634, 1636, 1684); in Part B the second cell of twelve rows (lines 1695–1700, 1702–1705, 1711,
  1712) and the third cell of line 1711; five new rows (lines 1706–1710). S3 Text between `checked3` and `checked4`:
  two outputs named in §6 (line 317, `derived_r24.out`, item 13; line 372, `conversions_b26.out`) and one in §8 (line
  544, item 6), beside the two intervals (line 299 in §5; line 544 in §8) and the plural (line 556 in §10); nothing
  else. S5 Text §5 (line 33) named the third check at `checked4`. The part of the dispositions file on the third
  check holds a paragraph for each of the 42 and the section on the reading of Part B.
- The passage on the fourth check. Findings and grades recounted in the four reports: Y1 12 (0, 7, 5), Y2 8 (0, 4,
  4), Y3 11 (0, 4, 7), Y4 7 (0, 2, 5); 38 in all, 0 errors, 17 inexact, 21 notes. The four parts are those of the
  reports' titles; Y1 reads each of the 18 rows of Part B, and Y4 places the 107 page citations of S20 Table's Table A.
  Three things were found by two sessions (Y1-12 and Y3-2; Y3-10 and Y4-7; Y3-11 and Y4-1), each pair one thing, and
  no other two of the 38 are the same thing. None of the 38 is of a value of a result in the main text or in the
  supporting information, and neither the reports' summaries nor their sections "Checked and found exact" have such
  a value wrong. The new values of `derived_r24.out` (the lines that `checked4` has and `checked3` has not: four of
  item 1, the eight cells and the summary line of item 6, four of item 13, two of item 14) are each recomputed in
  `audit/recheck_Y2.md`, section 2, by code written apart from the script, and found equal to the output's lines. 36
  paragraphs of the last part of the dispositions file have "Corrected." and two "Stated." (Y1-1, Y1-2), both of the
  last column of Part A; the head note (`manuscript/supplementary.md`, line 1601) says of that column what the
  record says it says.
- The list of the corrections in the paper's files, against `git -C VT diff --word-diff checked4 HEAD -- manuscript/
  notes/partB5_literature_v2.md`. Every change is an item of the list and every item is in the difference: the main
  text, line 395 (the list of supporting information, S2 Text's entry); S2 Text, line 3; S3 Text, line 128 (§4, which
  runs from line 126 to line 162); S4 Text, line 62 (row R1, "Results 2–7" to "Results 2, 6 and 7"); S5 Text, line 33
  (§5); `manuscript/supplementary.md`, line 400 (S17 Table's source line), line 1601 (the head note: the sentences on
  Part A, the clause on S17 Table, the clause on the predictions), line 1700 (the coupled family, second cell), line
  1707 (the whole-brain ΦR items, first and second cell), line 1711 (the row of `derived_r24.out`, second cell), line
  1722 (S20 Table's row 1) and line 1726 (row 5); the literature file, lines 13 and 17, which are rows 1 and 5 of S20
  Table character for character. No cell of Part A differs. `derived_r24.py`: item 6 reads each printed correlation
  under its cell's heading and asserts the equality cell by cell (its lines 183–201). On "the fifth script that this
  commit adds", Z2-1.
- "The checks" (unchanged since `checked4`), on the files of HEAD: `check_numbers.py` ("rows 1381, data rows 787,
  flagged 10"), `check_cells.py` ("flagged 0"), `tablecheck.py` on the seven manuscript files ("rows with a wrong cell
  count: 0"), `wc.py` ("total with headings 8489 without 8362") and `abstract_summary.py` (300 and 200) give the
  committed outputs of `checks/` byte for byte. The main text has no computation label before "## Supporting
  information" (line 391), and "planning session" and "writer's session" occur among the manuscript files in S5 Text
  line 33 (§5) alone.

**2. The dispositions file, the last part (lines 2579–2831).**

- (a) The opening paragraph and the list. `git -C VT log --oneline -2 checked4` gives 26156b8 on 8bd189e; the reports
  of Y2 and Y3 name 26156b8 and `checked3`. The four reports with their ranges, parts, counts and grades are as
  listed (recounted as under 1).
- (b) The introduction. 38, 0, 17 and 21; three pairs, 35 different things. The two things found complete: the
  statement on the computations without a row is in `audit/recheck_Y1.md` (lines 337–341: "no quoted computation
  without a pre-run entry lacks a row") and that on the contrasts in `audit/recheck_Y2.md` (lines 244–252: "None is
  outside both"). The 17 findings graded inexact were gone through one by one, and each is in the list of what was
  found inexact: the sentence of the head note on Part A (Y1-1, Y1-2), its clause on S17 Table (Y1-4), the file named
  in a new row of Part B (Y1-5), the head of S2 Text with the main text's list (Y2-1), statements of the file (Y1-3,
  Y1-6, Y1-7, Y3-6), statements of the record's entry (Y3-1, Y3-2, Y3-3), two reasons (Y2-2, Y2-3), a pointer and a
  count of the claim record (Y4-2, Y4-1), the comparison on sorted lists (Y2-4); the list names nothing that is not
  among the 17. 36 and 2; for each of the 36 a file of the commit differs from `checked4` as its paragraph says.
- (c) All 38: one paragraph each, in the reports' order, with the report's grade (38 of 38). Three paragraphs "As …"
  (Y3-2, Y4-1, Y4-7), each returned by a "Found also by" (Y1-12, Y3-11, Y3-10) and each pointing to a paragraph that
  answers its finding too. Each statement of a finding was read with the finding in its report and is fair to it, with
  Z2-2 on one sentence of Y1-4. The 54 quotations of the part were extracted by script and searched in every tracked
  text file of HEAD, the lines joined, and then read in place. The 39 that follow a verdict stand word for word where
  the paragraph puts them: `manuscript/supplementary.md`, lines 400, 1601, 1700, 1707, 1711, 1722 and 1726; the
  literature file, lines 13 and 17; S2 Text, line 3; the main text, line 395; S3 Text, line 128; S4 Text, line 62; the
  record, lines 9156–9158, 9193, 9496–9497 (and 9519–9520), 9500–9501, 9504–9505 and 9507; `checks/derived_r24.out`,
  line 68; `checks/derived_r24.py`, lines 3 and 16–18; the claim record, lines 15–17, 169 and 178–180; the `why` of
  S201, S422, S417, LT13.1 and LT13.2; and, where a paragraph quotes the dispositions file itself, the paragraphs of
  R56, W3-8, W3-10, X1-1, X1-5, the introduction of the part on the third check, point (1) and the last paragraph of
  its closing section. Of the 15 in the statements of the findings, nine are earlier forms, each in the report it is
  quoted from and in no other file of HEAD, and six are words that the files still have.
- What the paragraphs say of files, verified apart from the quotations. Y1-1: no cell of Part A differs from
  `checked4`. Y1-4: S17 Table's body has 932 rows (738 "pickle", 36 "engine", 158 "saved"), none with a label of the
  fixed orders ("prewhiten_fixed", "ar10", "ar20") and none of a gap or of the count of replaced volumes;
  `notes/review_results/` holds nine `inference_rows_*.pkl` (1,002 rows), the eight without
  `inference_rows_prewhiten_fixed.pkl` holding 738 (on the parenthesis of the new source note, Z2-5). Y1-5:
  `notes/review_results/logs/rev_phir_items.log` holds the three items (the contrasts at W = 30; "(2) per-subject
  ΦR", line 35; "(3) ΦR by window", line 55), and `inference_rows_w30.csv` (30 rows) the first. Y1-6: the conversion
  is item 3 of the record's entry "The sign(q)-weighted cross-lag deviation: outcome" (lines 3110–3115, "stated
  here, not in a result file"). Y1-7: the three predictions cite −1.77 (`coupling_map_tables.md`, line 16: −1.7711),
  0.953 with the ceiling 0.729, and "the null's 1.18" (`manuscript/supplementary.md`, lines 1632, 1637, 1641); CSV
  lines 439, 446 and 1322 give `inference_rows_raw.csv` as the source of the two phase-randomised p and of 1.155.
  Y1-8: Results 2 (main text, line 87) has "(the scrutiny S2 Text applies to the deconvolved ΦR contrast)". Y1-10:
  `derived_r17.out`, line 42, has 1.41; Results 1 (line 53) and the Discussion (line 181) print 1.4; CSV lines 99 and
  1146. Y1-11: Results 7 (line 158) prints the interval at p = 20 alone, Table 4 (lines 167–168) both. Y2-2: the
  report's first two tables are of the scripts and of the validation; the row "-0.0047 [-0.0079, -0.0013], p =
  0.0233 | 4 | 37 / 62" is in the table of its section 1 (line 51). Y2-4: as under 1. Y2-8: the docstring's list is
  that of the finding. Y3-1: as under 1. Y3-10: the sentence stands in the literature file's line 7. Y4-2: S20
  Table's row 5 has "awake" of three macaques of the DBS dataset and not of the five; S3 Text §10 and the search note
  (line 92) say that the five were scanned awake.
- Each correction answers every part of its finding. Where a finding names more than one place, each has the
  corrected text: the closing section and the `new` of U09h beside the head note for Y1-4; the dispositions of X1-8
  and W3-4 for Y1-3; the head note and point (1) for Y1-7; the main text's list beside the head of S2 Text for Y2-1;
  the disposition of X1-5 beside the `why` of S201 for Y2-2; that of X1-1 beside the `why` of S417 for Y2-7; that of
  X2-7 beside the record for Y3-1; the introduction of the part on the third check beside the record for Y3-5; the
  `why` of LT13.1 and of LT13.2 for Y3-10 and Y4-7; the literature file beside S20 Table for Y4-3 and Y4-4; the
  dispositions of X4-8 and W7-5 beside the claim record for Y4-5.

**3. The amended paragraphs of the earlier parts.**

- `checked4` to HEAD, paragraph by paragraph (493 paragraphs to 539): 23 paragraphs differ before the last part, which
  is new (46 paragraphs). They are the title and the opening paragraph, R56, VE-24, VN-3, W3-4, W3-8, W3-10, W4-11,
  W7-5, the introduction of the part on the third check, X1-1, X1-3, X1-5, X1-8, X1-10, X2-7, X4-2, X4-7, X4-8, and
  points (1) and (2) and the last paragraph of the closing section; no other.
- Every changed sentence was read against the files at HEAD and against the finding of the fourth check that it
  answers (R56: Y3-8; VE-24 and point (1): Y1-4; VN-3: Y4-3; W3-4 and X1-8: Y1-3; W3-8: Y3-7; W3-10: Y3-6; W4-11 and
  X2-7: Y3-1; W7-5 and X4-8: Y4-5; the introduction: Y3-5, Y3-9; X1-1: Y2-7; X1-3: Y4-4; X1-5: Y2-2; X1-10: Y2-6;
  X4-2: Y4-2; X4-7: Y4-6; point (1): Y1-7, Y1-10; point (2): Y1-9; the last paragraph: Y1-6). Each holds, with Z2-3 on
  a parenthesis of W4-11 and Z2-4 on the count of point (2). Every quotation that follows a verdict in these
  paragraphs stands at the place named. In particular: W3-8's counts are those of the script (under 1), and the
  addition to item 6 is what reads the fifth tables file; W3-10's places are those of the row's list (S4 Text, line
  62); X1-8's quotation is the first sentence of the head note's passage on Part A; point (1) quotes the head note's
  sentence on the second column word for word, and the kinds it names are those of `audit/partB_reading.md` (its
  lines 11–16).
- No quotation of the file has lost its place between `checked4` and HEAD but earlier forms quoted as such: of the 588
  quotations of twelve or more characters, ten stood at `checked4` in a file other than the reports and stand at HEAD
  in the reports alone, nine in the statements of the findings of the last part and one in that of X2-7 ("the parse
  check of the four scripts").

**4. The whole file.**

- 152 headings for the three audits, R01–R57, T01–T63 and C01–C32, each once, with the grade of its report (1, 12, 30,
  14; 3, 18, 31, 11; 2, 5, 17, 8); 157 paragraphs for the ten checks (VO 13, VE 25, VR 17, VT1 10, VT2 17, VC 9, VN
  11, VM 10, VS 12, VB 33), 86 for the second, 42 for the third and 38 for the fourth, each finding once, with the
  report's grade (11, 69, 77; 6, 40, 40; 0, 17, 25; 0, 17, 21). The counts and grades of each report as the four
  lists of the file give them are those of the report.
- 147 "Corrected.", 2 "Stated, not changed." (R46, T25) and 3 "The audit's instructions." (R44, R45, T53); 142, 7 and
  8 in the part on the ten checks; 85 and 1 (W5-14); 41 and 1 (X1-8); 36 and 2. In the parts on the second, third and
  fourth checks 14, 8 and 3 paragraphs point to another, each returned by a "Found also by".
- No line longer than 120 characters but the title (133); the longest other line has 118; no tab, no trailing space.
- The record's last entry, S5 Text §5 (line 33: "a fourth by four more, 38 findings"), `CLAUDE.md` (lines 447–450)
  and the folder's README (lines 81–94) give the same numbers of sessions (three; ten, seven, four, four) and of
  findings (152; 157, 86, 42, 38), the same grades and the same names of the report files as the dispositions file.
  No statement of the file was found to contradict another statement of it or of those four places.

**5. The bookkeeping files and the numbers table.**

- `CLAUDE.md`: one sentence changed, "four times (ten sessions, then seven, then four, then four more)", which are
  the numbers of the reports.
- The folder's README: one clause added, on `recheck_Y1.md` to `recheck_Y4.md`, and "the four checks". Its bullet on
  `audit/` names every one of the folder's 33 files (the three reports, `te_filter_check.py`, the ten `check_V*.md`,
  `recheck_W1.md` to `recheck_W7.md`, `recheck_X1.md` to `recheck_X4.md`, `partB_reading.md`, `recheck_Y1.md` to
  `recheck_Y4.md`, `dispositions_revision.md`, `findings.md`, `dispositions.md`), and the folder holds no other.
- The numbers table, `checked4` to HEAD: 1,381 rows on both sides, the same keys in the same order, the head note
  unchanged; three rows differ, each in the line number of its locator alone (CSV lines 1201 and 1230: 69 to 71; 1231:
  57 to 59). The claim record gained two lines in its head; its line 71 holds "frame-wise displacement greater than
  0.4" and its line 59 ""Six out of 20 participants were discarded" for more than 20 % of the". No other row cites the
  claim record.
- All 1,065 line locators of the table at HEAD, in 54 source files, by own code: the anchor is on the named line, the
  prefixes removed (169 rows with "@La-b|", the line within the range; 6 with "@pct|"), and the held string is on the
  line for the 792 data and bound rows. The seven files that rows cite and that differ from `checked4` (the record,
  S2 and S3 Text, `manuscript/supplementary.md`, the literature file, `checks/derived_r24.out`, the claim record) are
  among them.

**6. The replacements.**

- The JSON of HEAD applied to copies of the sixteen files of 8bd189e with
  `notes/review_2026-09-25/revision/apply_replacements.py`: 314 entries, each "ok", 314 different ids; 16 files
  written, which are all the files of 8bd189e that differ at HEAD; 15 are identical with HEAD's and the record differs
  in its five headings alone («ENTRY_TIME», lines 8875, 8976, 9045, 9092, 9150). The output is identical with
  `checks/apply_revision.out` (332 lines); of the 16 sha256 values it prints, 15 are those of the files at HEAD and
  the record's is that of the file with «ENTRY_TIME».
- `checked4` to HEAD: 310 entries to 314; none removed, the order kept, no `old`, `count` or `file` changed. New, 4:
  S202 (S2 Text), S203 (the main text), S325 (S3 Text) and U25 (`manuscript/supplementary.md`), each with count 1.
  Changed, 16: `why` alone in S201, S422 and LT13.2; `new` and `why` in S417, U09h, U09i.4, U17.5, U24.1, LT07.5 and
  LT13.1; `new` alone in S502, U06d, N01, C08, RR03 and REC01, whose six reasons, read again, remain true of the
  changed `new`.
- `checks/apply_revision.out`, `checked4` to HEAD: the four lines of the new entries, "all 314 entries applied" and
  the sha256 of the eleven files that changed; nothing else.
