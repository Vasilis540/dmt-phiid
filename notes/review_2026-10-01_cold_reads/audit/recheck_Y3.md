# Y3 — the record's five new entries, the numbers table, the replacements file, the bookkeeping files and the dispositions file

Fourth verification of the prepared revision. Tree: VT at HEAD (26156b8), against `checked3` (f50c1d3) and 8bd189e.
Part: `manuscript/analysis_record.md` (its last five entries), `manuscript/main_text_numbers.csv`,
`notes/review_2026-10-01_cold_reads/checks/numbers_update.out` and `apply_revision.out`, the replacements file
`notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json` (below: the JSON),
`CLAUDE.md`, `notes/review_2026-10-01_cold_reads/README.md` and
`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`. Paths are relative to VT. "The record" is
`manuscript/analysis_record.md`; "the list" is `checks/numbers_update.out`; "the dispositions file" is
`audit/dispositions_revision.md`; "the main text" is `manuscript/draft_v2.md`; `checks/`, `audit/`, `claims/` and
`revision/` are the folders of `notes/review_2026-10-01_cold_reads/`. "CSV line n" is the line of the numbers table at
HEAD (line 1 the head note, line 2 the column names). Line numbers are those of HEAD. Nothing under VT was changed
(`git status --short` is empty at the end, and no `__pycache__` was written); the scripts that write were run on copies
under VW/Y3/, the scripts that only print were read from copies under VW/Y3/ with VT as their input. No internet, no
subject data: every recomputation is on committed result files.

**Result.** 11 findings: 0 errors, 4 inexact, 7 notes. No number, interval, date, count of findings or of grades,
locator or quotation that was changed or added between `checked3` and HEAD in the files of this part disagrees with
its source. The four inexact statements are three of the record's entry on the revision (what the parse check is said
to cover; one count and one omission in the list of the corrections that the third check brought to the paper's files)
and one amended paragraph of the dispositions file (W3-10). Every disposition of X2-1 to X2-10 and of X3-1 to X3-13
states its finding fairly, carries the report's grade and is true of the files at HEAD, with Y3-1 on the sentence that
the disposition of X2-7 quotes.

## Findings

**Y3-1**
- Where: the record, the revision's entry, first paragraph (lines 9156–9158): "the parse check of the four scripts
  that this commit adds or changes (the figure script, `figures_check.py`, `derived_r24.py` and the counter of the
  Abstract's and the Author summary's words)". The disposition of X2-7 quotes the sentence as the correction (the
  dispositions file, lines 2410–2412).
- Problem: The four named are the four of the parse check, so that the sentence now says which four it means, as X2-7
  asked. The description that came with the correction does not hold: the commit adds or changes five scripts. The
  fifth, `audit/te_filter_check.py`, is added by this commit and is not in the parse check.
- Evidence: `git -C VT diff --name-status 8bd189e HEAD` lists five `.py` files and no `.sh`:
  `M scripts/15_figures_v2.py`, `A notes/review_2026-10-01_cold_reads/audit/te_filter_check.py`,
  `A …/checks/abstract_summary.py`, `A …/checks/derived_r24.py`, `A …/checks/figures_check.py`.
  `checks/scripts_check_revision.out` has four lines, of the first and the last three. (All five parse.)
- Grade: inexact

**Y3-2**
- Where: the record, "The audits of the prepared revision" (lines 9498–9500): "six cells of Part A, twelve of Part B
  and five new rows of Part B, for post hoc computations that the supporting texts quote and that had none".
- Problem: Thirteen cells of S19 Table's Part B differ between `checked3` and HEAD, in twelve rows. Twelve are cells of
  the second column ("where quoted"), the number that the closing section of the dispositions file gives (eleven
  completed and the cell of the leave-one-out, lines 2530–2536). The thirteenth is the third cell ("what it is") of
  the row of the numbers derived for the revision: "six CSV files, two tables files" became "eight CSV files, five
  tables files", and the clause "after the last of those checks, items 13 and 14 and additions to items 1 and 6 (…)"
  was added. The six cells of Part A and the five new rows are right.
- Evidence: S19 Table compared cell by cell at `checked3` and at HEAD (`manuscript/supplementary.md`): Part A, the
  last cell of lines 1610, 1622, 1625, 1634, 1636 and 1684; Part B, the second cell of lines 1695–1700, 1702–1705,
  1711 and 1712, and the third cell of line 1711; new rows at lines 1706–1710. The head lines of the two parts are
  unchanged.
- Grade: inexact

**Y3-3**
- Where: the record, the same paragraph (lines 9503–9506): "in S3 Text, the plural of one sentence of §10, two outputs
  named in §6, and in §5 and §8 the inverted sign-flip intervals of two contrasts that had none".
- Problem: The list is one item short for S3 Text. In §8, "(not at p = 10 on ts_gsr at the global fit, +0.570)"
  became "(… +0.570; the eight intervals are in `derived_r24.out`, item 6)": a third output named, for the Fisher-z
  intervals, which is none of the list's items. The record's next sentence says that the script computes the eight
  intervals and not that S3 Text §8 now names them; the closing section of the dispositions file does say it ("which
  it now names"). Every other change of the supporting texts, of the supplementary tables and of the literature file
  between `checked3` and HEAD is an item of the list, Y3-2 and Y3-4 apart; each item of the list is in the difference.
- Evidence: `git -C VT diff --word-diff checked3 HEAD -- manuscript/ notes/partB5_literature_v2.md`:
  `si/S3_Text.md` line 544 (two changes: the pointer to item 6 and the interval of the estimate's contrast), lines 299,
  317, 372 and 556; the dispositions file, lines 2546–2548.
- Grade: inexact

**Y3-4**
- Where: the record, the same list, which ends "and a sentence of S5 Text §1" (lines 9505–9506).
- Problem: One more place of the paper's files changed between `checked3` and HEAD and is not in the list: S5 Text
  §5's clause on the audits, which now names the third check. For the second check the list ends "S5 Text §5's clause
  on the audits names this check too" (line 9489), the sentence added for X2-5; the list written for the third check
  has the omission that X2-5 found in the earlier one.
- Evidence: `manuscript/si/S5_Text.md` line 33: "a second check by seven more, 86 findings, and a third by four more,
  42 findings" (at `checked3`: "and a second check by seven more, 86 findings"); the dispositions file, X2-5 (lines
  2401–2403).
- Grade: note

**Y3-5**
- Where: the record (lines 9495–9496): "no number, page, count or quotation that the earlier corrections had changed
  or added was found wrong"; the dispositions file, introduction of the last part (lines 2282–2283), the same
  sentence.
- Problem: The sentence holds by the grades (none of the 42 is graded an error) and is what the reports of X1, X2 and
  X4 say of their own parts. Tested against the 42 findings, one thing graded inexact, found by two sessions (X2-1,
  X3-5), is of counts that the correction for W4-1 had written: the list gave 17 references to the paper's own tables
  and 14 to cited works in four kinds, where 16 and 15 in five kinds are so, and the correction changed the numbers
  (17 to 16; a fifth count, 1). The introduction of the last part itself names "a count in
  `checks/numbers_update.out`" among what was found inexact, two sentences after this one. The case is that of X2-10
  and X3-11 for the second check's sentence. No other of the 42 is of a number, page, count or quotation that those
  corrections had changed or added (the pages of S20 Table's row 1, X1-3 and X4-1, are committed text of 8bd189e; the
  two word counts of X3-8 were not changed by them).
- Evidence: `audit/recheck_X2.md`, X2-1 (lines 28–32: "The paper's own tables are referred to by number 16 times, and
  the references to cited works are 15, a table among them, where the sentence gives 14 in four kinds"; "The count of
  17 after "Table" and the total of 70 are right"); `audit/recheck_X3.md`, X3-5 (lines 77–89);
  `git -C VT diff checked3 HEAD -- notes/review_2026-10-01_cold_reads/checks/numbers_update.out`; own count on the
  main text (below): 16 and 1.
- Grade: note

**Y3-6**
- Where: the dispositions file, W3-10 as amended (lines 1987–1991): "with their kinds and their places (S3 Text §4 and
  §6; S1, S14 and S17 Tables). The sentence and its list are as the third check left them".
- Problem: The paragraph quotes the row's sentence in its form at HEAD and gives the places of the earlier form. The
  parenthesis is the one written for the five kinds of the first list ("with the five kinds and their places" at
  `checked3`); the list as the third check left it names four more contrasts, whose places are S2 Text, S3 Text §8
  with S11 Table, and S3 Text §5.
- Evidence: `manuscript/si/S4_Text.md` line 62: "the deconvolved contrast (S2 Text; S17 Table), the whitened series' r₁
  DiD at p = 20 and what the AR(1)-substituted estimate carries of the contrast there (S3 Text §8; the first also in
  S11 Table) and the DiD of the count of replaced volumes (S3 Text §5)", after the five kinds with S3 Text §4 and §6
  and S1, S14 and S17 Tables; `git -C VT diff --word-diff checked3 HEAD` of the paragraph.
- Grade: inexact

**Y3-7**
- Where: the dispositions file, W3-8 as amended (lines 1978–1980): "the counts of the CSV and tables files are those
  after the third check, which added items 13 and 14".
- Problem: Items 13 and 14 account for the two further CSV files and for two of the three further tables files. The
  fifth tables file, `prewhiten_fixed_tables.md`, is read by the addition to item 6 (the eight whitened correlations),
  which came after the third check as well. By the parenthesis alone the tables files would be four. S19 Table's row
  has the whole of it: "items 13 and 14 and additions to items 1 and 6".
- Evidence: `checks/derived_r24.py`: tables files at lines 112 and 339 (the two of `checked3`), 182 (item 6), 435
  (item 13) and 463 (item 14); CSV files at lines 433 (item 13) and 461 (item 14) beside the six of `checked3`;
  `git -C VT diff checked3 HEAD` of the script; `manuscript/supplementary.md` line 1711.
- Grade: note

**Y3-8**
- Where: the dispositions file, R56 (lines 388–389): "The commit holds the files the README names (the three reports,
  `te_filter_check.py`, the reports of the checks and this file)."
- Problem: The statement holds; its parenthesis was not carried along with the folder's README. The README's bullet on
  `audit/` now names one more file of this commit, `partB_reading.md`, "the report of the session that then read S19
  Table's Part B against the whole paper", which is none of the four kinds of the parenthesis: the README, CLAUDE.md
  and the record's first paragraph each set that report beside the reports of the checks, not among them.
- Evidence: `notes/review_2026-10-01_cold_reads/README.md` lines 88–92; `CLAUDE.md` lines 447–448; the record, lines
  9160–9161; the paragraph of R56 is the same at `checked3`. The file is in the commit, and the folder's 29 files are
  all named in the README.
- Grade: note

**Y3-9**
- Where: the dispositions file, introduction of the last part (lines 2283–2285): "two notes of X2 (X2-9, X2-10) that
  session took from the report of X3, which lay in the directory in which the four worked, and verified against the
  files".
- Problem: Nothing in the tree says this. `audit/recheck_X2.md`, which the README gives as the report as its session
  returned it, names the report of X3 nowhere and gives both findings with evidence of its own. The two pairs do agree
  closely (X2-9 and X3-13 list the same seven labels in the same order and the same seven lines of
  `derived_r24.out`; X2-10 and X3-11 give the same three limits and the same recomputed intervals), which fits the
  statement and does not show which session took from which.
- Evidence: `audit/recheck_X2.md`: no occurrence of "X3"; X2-9 (lines 147–158), X2-10 (lines 160–172);
  `audit/recheck_X3.md`, X3-13 (lines 168–177) and X3-11 (lines 142–154).
- Grade: note

**Y3-10**
- Where: the JSON, entries LT13.1 and LT13.2 (file `notes/partB5_literature_v2.md`), `why`: "where the table's head
  note says that a row names what it takes from outside a study's article".
- Problem: The reason is that of U24.1 and U24.2, which change S20 Table, word for word. The file that LT13.1 and
  LT13.2 change has no head note: the sentence is in its paragraph on the search (under "How the literature was
  searched, and what was read"), which the file's title calls "the search paragraph". For these two entries the place
  named is that of another file.
- Evidence: `notes/partB5_literature_v2.md` lines 5–12 (the heading, the paragraph of line 7, "## Table A. Studies"
  and the table's first line); `manuscript/supplementary.md` line 1716; the four `why` are identical.
- Grade: note

**Y3-11**
- Where: `claims/claims_2026-10-01.md`, head (lines 15–16): "and after a third, which made four pointers say which
  place states which part of an item". (Outside the files of this part; seen while the paragraphs of X4-2 to X4-4
  were read against the files.)
- Problem: Between `checked3` and HEAD the pointers of three items were changed, those on Luppi et al. (2026), Gatica
  et al. (2024) and Down et al. (2026), with the heading of the third. The dispositions file has three paragraphs on
  pointers (X4-2, X4-3, X4-4), and the report of X4 three findings. Four is reached only if the heading of the item on
  Down et al. is counted as a pointer, or the two sentences of the pointer on Luppi et al. (2026) as two.
- Evidence: the claim record compared item by item at `checked3` and at HEAD: six items differ (the head; the
  description of the Reporting Summary of Singleton et al.; the item on Luppi et al., 2026, lines 166–179; the pointer
  of Gatica et al., lines 186–189; the heading and the pointer of Down et al., lines 191 and 195–198); the
  dispositions file, lines 2478–2495.
- Grade: note

## Not checkable from the tree

That the reports `recheck_X1.md` to `recheck_X4.md` and `partB_reading.md` are as the sessions returned them, and that
the second was returned as text (the README; the file does begin with its heading, and none of the five holds an
absolute path). What the dispositions of R55 and W5-10 say that the planning session's preparation stops on (what they
are about holds: the 310 entries of the JSON have 310 different ids, and no cross-reference among the 95 headings of
the first three parts is one-sided). The day of the third check beyond the date of the tree that the four read
(`checked3` is dated 3 October 2026, 00:46 UTC). The statement of Y3-9. The pages of the PDFs that the reasons of U11,
U17.1, LT07.1, U24.1, U24.2, LT13.1 and LT13.2 give (another part).

## Checked and found exact

**1. The record.**

- The rules. The file at 8bd189e (814,068 bytes) is a byte prefix of the file at HEAD (888,285 bytes); 686 lines are
  added. No line of the five entries is longer than 120 characters, headings apart (the longest has 120; no tab, no
  trailing space). The five headings carry "3 Oct 2026 04:10 UTC".
- The delta. The text from "## B27, outcome" was extracted at `checked3` and at HEAD, each paragraph's lines joined,
  and compared word by word: 42 paragraphs on each side; beside the time of the five headings, five paragraphs differ,
  all of the last entry (its first paragraph; "The revision."; "The length and the tables"; "The audits of the
  prepared revision"; "The checks"). The four outcome entries are word for word those of `checked3`.
- First paragraph. `checks/scripts_check_revision.out` names the four scripts of the parenthesis (on "that this commit
  adds or changes", Y3-1). `derived_r24.py` opens two pickles (lines 48, 167), eight CSV files (82, 97, 120, 134, 158
  and again 289, 210, 433, 461), five tables files (112, 182, 339, 435, 463), three array files (206; 295, for both
  variants) and one log (277), each a tracked file, and no other; the module it imports,
  `notes/rev_inference_inverted.py`, opens none. `audit/` holds the three audits' reports, the ten `check_V*.md`,
  `recheck_W1.md` to `recheck_W7.md`, `recheck_X1.md` to `recheck_X4.md`, `partB_reading.md` and the dispositions file.
- "The revision." `git -C VT diff --stat 8bd189e HEAD -- manuscript/`: S1 to S5 Text all changed, S2 Text in one line
  and one sentence of it (the outcome of the regional ΦR check). In `supplementary.md` the sections that differ from
  8bd189e are the head note, one line of text each under S5, S12 and S13 Tables (lines 101, 335 and 363), and S11,
  S18, S19 and S20 Tables. The sentence on the macaques agrees with S3 Text §10 (line 556):
  "ketamine[Title/Abstract]" is a term of the string of 2 October 2026; row 5's macaques "scanned awake and under
  sevoflurane, propofol or ketamine"; row 4's, "scanned under isoflurane", "received injections of ketamine and of
  other agents"; "Data under anaesthesia are not counted here as psychedelic data".
- "The length and the tables". The Abstract of 8bd189e has "against 0.003–0.005 in simulated pure autocorrelation
  changes"; the list places the two numbers in Results 4 as 0.0027 and 0.0049 (its lines 310–311), and Results 4 has
  "+0.0027 ± 0.0014" and "+0.0049 ± 0.0017" (main text, line 124).
- "The audits of the prepared revision", the second check. The seven reports hold 5, 7, 12, 14, 16, 20 and 12
  findings, 86 in all, graded 6, 40 and 40. The six errors (W2-4, W4-1, W5-1, W5-2, W6-1, W6-2) are the four things
  named and none is of a value of a result in the paper's files. The 40 findings graded inexact were read one by one:
  W2-1 alone is of such values, three limits of the Fisher-z intervals of S3 Text §6, each moved by 0.001 (−0.270 to
  −0.269, −0.099 to −0.098, −0.566 to −0.567; S3 Text, line 406, has the corrected limits).
- The third check. Findings and grades recounted in the four reports: X1 11 (0, 5, 6), X2 10 (0, 2, 8), X3 13 (0, 5,
  8), X4 8 (0, 5, 3); 42 in all, 0 errors, 17 inexact, 25 notes. The four parts are those of the reports' titles, and
  X1 read all 81 rows of Part A. Eight things were found by two sessions (X1-3 and X4-1; X2-1 and X3-5; X2-2 and
  X3-1; X2-8 and X3-9; X2-9 and X3-13; X2-10 and X3-11; X3-4 and X4-5; X3-6 and X4-6), each pair one thing; no other
  two findings are the same thing. 41 paragraphs of the last part have "Corrected." and one "Stated." (X1-8).
  `git -C VT log --oneline -3 checked3` gives f50c1d3 on 8bd189e, dated 3 October 2026. X1-11 says that the other
  cells of Part B were not read for completeness, and `audit/partB_reading.md` reads the thirteen rows of Part B.
- The list of the corrections in the paper's files, against the difference between `checked3` and HEAD (the main text
  did not change). S19 Table: the head note gains two sentences, on the last column of Part A and on the second column
  of Part B; six cells of Part A; five new rows of Part B, each for a computation quoted in a supporting text (S5 Text
  §1, S2 Text, S3 Text §6, S3 Text §3, S5 Text §4); on the cells of Part B, Y3-2. S20 Table: the head note (line 1716)
  and row 1 (line 1722), which names the Reporting Summary for pp. 36 and 37 and the Extended Data for p. 23; the
  literature file has the same clause (line 7) and the same row (line 13, identical with S20 Table's). S4 Text: rows
  P5, S6 and R1 (lines 38, 53, 62) and no other. S2 Text: line 9. S3 Text: line 556 in §10; lines 317 and 372 in §6
  (`derived_r24.out`, item 13; `notes/review_2026-09-30/checks/conversions_b26.out`, which exists); lines 299 in §5
  and 544 in §8 (on §8's second change, Y3-3). S5 Text: line 7 in §1 (on line 33, Y3-4).
- The two intervals. "+1.12 [−0.58, +2.97]" is line 102 of `checks/derived_r24.out` (item 14) and "−0.0037 [−0.0066,
  −0.0008]" its line 38 (item 1). Recomputed from the committed per-subject values with an inversion of the exact
  sign-flip test written for this check: the count DiD from `censoring.csv` +1.119 [−0.579, +2.965], p = 0.2166,
  positive in 7 of 14; the estimate's DiD at p = 20 from the pickle −0.00370 [−0.00658, −0.00083], p = 0.0145,
  negative in 12 of 14; the directed response's difference from `directed_crosslag.csv` +0.00044 [−0.00061,
  +0.00149], p = 0.3800 (item 13, line 97; S3 Text §6, line 317; the interval stands in no other committed output).
  Items 14, 1, 13 and 6 are the items of the four quantities, in the sentence's order. What each reproduces: item 14
  stops unless the mean, the p and the count of positive subjects equal those of `censoring_tables.md` (line 24);
  item 13 unless the mean and the p equal those of `directed_crosslag_tables.md` (line 12); item 1 unless the mean and
  the p equal the fields of the run's pickle, and prints the run's count of negative subjects beside its own (12 and
  12); item 6 gives the eight correlations that `prewhiten_fixed_tables.md` prints, here compared cell by cell (lines
  28, 53, 77, 102, 126, 151, 175, 200: +0.445, +0.570, +0.168, +0.014, +0.333, +0.081, +0.157, −0.079), seven of the
  eight intervals including zero.
- `derived_r24.py`, run on a copy of the script, of the module and of the nineteen files it reads, gives
  `checks/derived_r24.out` line for line from its second line (the first has `git=nogit` for `git=8bd189e`).
- "The checks". The sentence on the digits that follow a letter states the rule that the head note of the numbers
  table and the list state, and the three agree with the main text (below).

**2. The numbers table.**

- `checked3` to HEAD by (section, paragraph, number, occurrence): 1,381 rows on both sides, the same keys in the same
  order. 17 rows differ, each in the line number of its locator and in nothing else: 14 point into
  `checks/derived_r24.out` (CSV lines 23, 24, 25, 390, 391, 393, 553, 566, 668, 672, 800, 801, 1149, 1175: lines 58
  to 63, 36 to 41, 48 to 53, 46 to 51, 65 to 80, 55 to 60, 56 to 61, 43 to 48) and 3 into the claim record (CSV lines
  1201 and 1230: 67 to 69; 1231: 56 to 57). At HEAD the anchor of each, and the held string of the 14, is on the named
  line. The six other rows that cite `derived_r24.out` cite its lines 3 and 19, which did not move.
- The head note, word by word: one sentence changed, "a group of digits that follows a letter directly (the names of
  the supporting items, S1 Text to S20 Table; "Fig. S4" of a cited work; the user name in the repository's address) is
  not a number token", which is the rule of the list.
- The whole table at HEAD, by own code (VW/Y3/num/): 787 data, 266 design, 262 label, 54 derived, 7 literature and 5
  bound rows. All 1,065 line locators, in 54 source files: the anchor is on the named line, the prefixes removed; the
  line lies in lines a to b for the 169 rows with "@La-b|"; 6 rows carry "@pct|"; the held string is on the line for
  the 792 data and bound rows ("bound on" removed). The 262 label rows have no source and the 54 derived rows a
  derivation.
- The tokens of the covered text (title; Abstract to the end of Data and code availability; the list of supporting
  information), recounted. Each of the 1,381 rows was placed by its context on one digit group of the text (five rows
  in scientific notation on two), on 1,386 of 1,759; no row sits on a group that follows a letter. The 373 without a
  row: 95 citation years; 13 day numbers and 11 years of the dates; 70 cross-references by number: 25 after "Results",
  16 after "Table" of the paper's own, 14 after "Fig" (10 before a panel letter: 1a three times, 1c, 3a, 3b, 3c, 4a,
  4b, 4c), 7 after "Eq." or "Eqs.", 3 after "Definition", 1 after "Example", 3 after "Fig." or "Figure" of cited works
  and 1 "their Table 1" (line 193, in the Discussion); the 10 numbers of the captions' heads; the DOI; 150 groups that
  follow a letter directly: 148 in names S1 Text to S20 Table (76 before "Text", 72 before "Table" or "Tables", "S17
  and S19 Tables" and "S1–S7 Tables" among them), the 4 of "Fig. S4" (line 187) and the 540 of "Vasilis540" (line
  267); the digits of four commit identifiers; 6 groups in code spans; 9 in headings (0 to 7 and the 1 of AR(1)).
  These are the counts of the list (lines 13–22), the changed ones included.
- The list, `checked3` to HEAD: one paragraph changed (lines 13–22) and nothing else.
- The committed outputs still reproduce on the files of HEAD, byte for byte: `check_numbers.py` ("rows 1381, data rows
  787, flagged 10"), `check_cells.py` ("flagged 0"), `tablecheck.py` on the seven manuscript files ("rows with a wrong
  cell count: 0"), `wc.py` ("total with headings 8489 without 8362") and `abstract_summary.py` (300 and 200).

**3. The replacements.**

- The JSON of HEAD applied to copies of the files of 8bd189e with
  `notes/review_2026-09-25/revision/apply_replacements.py`: 310 entries, each "ok", 310 different ids; 16 files
  written, which are all the files of 8bd189e that differ at HEAD; 15 are identical with HEAD's and the record differs
  in its five headings alone («ENTRY_TIME», lines 8875, 8976, 9045, 9092, 9150). The output is identical with
  `checks/apply_revision.out` (328 lines).
- `checked3` to HEAD: 287 entries to 310; none removed, the order kept, no `count` or `file` changed. Changed, 20:
  `new` alone in S305, S311, S314, S502, U06, N01, C08, RR03 and REC01; `new` and `why` in S417, S420, U06d, U08.10,
  U11, U17.1, LT03 and LT07.1; `old`, `new` and `why` in U08.8 and U08.9 (each `old` reaches further into its cell);
  `why` alone in F09b. New, 23: S201, S323, S324, S422, S507, U09g.1 to U09g.5, U09h, U09i.1 to U09i.8, U24.1, U24.2,
  LT13.1 and LT13.2.
- The reasons read against `old`, `new` and the places named. U11 and LT03: the sentence of `new` is that of S20
  Table's head note and of the literature file's search paragraph; at `checked3` row 1 cited pp. 36 and 37 and, for
  the Lausanne-129 parcellation, p. 23 without naming the Reporting Summary or the Extended Data. U17.1 and LT07.1:
  `old` ends with the remark on "DK-66", which `new` drops, and `new` has "(Extended Data Fig. 2, p. 23)". U24.1,
  U24.2, LT13.1, LT13.2: `old` and `new` are the two cells of row 1 as at `checked3` and at HEAD (on the place that
  the reason of the last two names, Y3-10). F09b: the script's height ratios are 0.30 : 0.20 : 0.20 at HEAD
  (`scripts/15_figures_v2.py`, lines 444–446) and 0.30 : 0.20 : 0.10 at 8bd189e; 0.20 / 0.70 is 1.71 times 0.10 /
  0.60; 0.25 × 0.20 / 0.70 = 0.0714 and 0.42 × 0.10 / 0.60 = 0.0700. Read beside these, and consistent with the
  difference of the files: the changed reasons of S417, S420, U06d and U08.8 to U08.10.

**4. The bookkeeping files.**

- `CLAUDE.md`: one sentence changed, "three times (ten sessions, then seven, then four), and one read S19 Table's Part
  B against the whole paper"; ten, seven and four are the numbers of the reports.
- The folder's README. What `derived_r24.py` computes since the third check (the inverted intervals of what the
  estimate carries of the whitened contrasts, of the directed response's difference and of the count DiD; the Fisher-z
  intervals of the eight whitened correlations) is what the additions to items 1 and 6 and items 13 and 14 print; the
  kinds and counts of the files it reads are those of the script. The bullet on `audit/` names every one of the
  folder's 29 files (the three reports, `te_filter_check.py`, the ten `check_V*.md`, `recheck_W1.md` to
  `recheck_W7.md`, `recheck_X1.md` to `recheck_X4.md`, `partB_reading.md`, `dispositions_revision.md`, `findings.md`,
  `dispositions.md`), and the bullet on `checks/` every file of that folder that this commit adds.

**5. The dispositions file, the last part.**

- The introduction: the four reports with their ranges, parts, counts and grades; 42, 0, 17 and 25; eight pairs, 34
  different things; the seventeen graded inexact are those the sentence lists (two rows of S4 Text: X1-1, X1-2; S20
  Table's head note: X1-3, X4-1; the count in the list: X2-1, X3-5; cells of S19 Table: X1-4, X1-5; pointers of the
  claim record: X4-2, X4-3, X4-4; four statements of the file: X3-3, X3-4 and X4-5, X2-2 and X3-1, X3-2); 41 and 1;
  the tree (f50c1d3 on 8bd189e). On two of its sentences, Y3-5 and Y3-9.
- All 42: one paragraph each, in the reports' order; the grade is the report's in each; eight paragraphs "As …", each
  returned by a "Found also by", and each pointing to a paragraph that answers its finding too (for X3-11 the record
  and the introduction of the part on the second check; for X4-1 the three cells of row 1, the Extended Data page
  among them).
- X2-1 to X2-10 and X3-1 to X3-13, each read with its finding in `audit/recheck_X2.md` and `audit/recheck_X3.md` and
  against HEAD. Each statement of a finding is fair to the report. The 16 passages quoted after a verdict were
  extracted by script, searched in every tracked text file and read in place; each stands word for word where the
  paragraph puts it: the list (lines 14–16 and 17–20), the record (lines 9156–9158, 9424, 9477–9478, 9489), the
  `why` of F09b, and the dispositions of W2-4, VB-16, VC-2 (whose words are the claim record's, line 235), W7-3 and
  C32, the first sentence of the part on the ten checks (lines 970–971), the heading of line 959 and "Found while the
  findings were settled", (4). Each correction answers its finding in full, with Y3-1 on X2-7. In particular: the
  disposition of W6-13 names seven rows whose wording gives the direction and three whose text gives a size, which
  are the ten rows of `checks/check_numbers_revision.out` (its rows 534, 725, 727, 756, 771, 772 and, by the
  derivative, 88; rows 10, 91 and 1216); R55 and W5-10 both speak of the planning session's preparation, "which is
  outside the repository"; VB-31 gives 8,489 and 8,460 (8,489 less the 29 markers); S11 Table's source line has
  "pre-run entry 1 Oct 2026" and no title, and S18 Table's the date after the entry's title
  (`manuscript/supplementary.md`, lines 256 and 1590).
- The paragraphs of X1 and X4 and the closing section: the 31 and 2 passages quoted after a verdict stand at the
  places named; the closing section's counts (thirteen rows; eleven cells and one; five rows) agree with the
  difference of S19 Table.

**6. The amended paragraphs of the earlier parts** (`checked3` to HEAD, paragraph by paragraph: 27 paragraphs differ
before the last part, which is new).

- They are the title and the opening paragraph, R55, C32, the heading on S20 Table's rows 2, 5 and 8, the first
  sentence of the part on the ten checks, VE-23, VT1-8, VC-2, VN-1, VB-16, VB-31, "Found while the findings were
  settled", the introduction of the part on the second check, W2-4, W3-3, W3-4, W3-8, W3-10, W3-11, W4-1, W5-3, W5-10,
  W6-13, W7-3, W7-5 and W7-8 (W4-13 points to W3-8). Every changed sentence was read against the files at HEAD and
  against the finding of the third check that it answers, and every quotation after a verdict stands at the place
  named, Y3-6 and Y3-7 apart. In particular: VE-23 and W3-8 quote the kinds and counts as the record, S19 Table's row
  and the README have them; VC-2 and VB-16 give the claim record's item and the reason of DCA01 as they stand; VN-1's
  new sentence holds (the item on Luppi et al., 2026, gives pp. 37, 38, 39 and 21, and the claim record's head gives
  the item to the ten checks); W3-4's list of cells holds of the cells at HEAD, the cell of B22 (a) as described; W7-3
  and W7-5 give the heading, the pointer and the two descriptions of the claim record as they stand (lines 164,
  175–177, 64–65 and 167).
- No quotation of the file that stood in one of the changed files at `checked3` has lost its place at HEAD, the
  earlier forms apart that a paragraph quotes as such ("the complete list is S19 Table's"; "with supplementary
  materials only where a cell names them"; "stays as far below the axis as it was"; "a PDF without a text layer").

**7. The whole file.**

- (a) 152 headings for the three audits, R01–R57, T01–T63 and C01–C32, each once, with the grade of its report (1, 12,
  30, 14; 3, 18, 31, 11; 2, 5, 17, 8); 157 paragraphs for the ten checks (VO 13, VE 25, VR 17, VT1 10, VT2 17, VC 9,
  VN 11, VM 10, VS 12, VB 33), 86 for the second and 42 for the third, each finding once, in the reports' order, with
  the report's grade (11, 69, 77; 6, 40, 40; 0, 17, 25).
- (b) 147 "Corrected.", 2 "Stated, not changed." (R46, T25) and 3 "The audit's instructions." (R44, R45, T53); 142,
  7 and 8 in the part on the ten checks; 85 and 1; 41 and 1. The counts of sessions (three, ten, seven, four) and of
  findings in the introductions are those of the reports.
- (c) No line longer than 120 characters but the title (134), a heading; the longest other line has 118; no tab, no
  trailing space.
- (d) The record's last entry, S5 Text §5 (line 33), `CLAUDE.md` (lines 446–451) and the folder's README give the same
  numbers of sessions and of findings, the same grades and the same names of the report files as the dispositions
  file. No statement of the file was found to contradict another statement of it or of those four places, apart from
  what Y3-5 to Y3-8 report.
