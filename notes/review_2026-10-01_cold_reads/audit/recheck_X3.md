# X3 — the dispositions file (`notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`) at HEAD

Part: the dispositions file as a whole document at HEAD of VT, against `checked2`, the seven reports
`audit/recheck_W1.md` to `recheck_W7.md`, the files the dispositions name, and the four other places that state the
same counts. "Dispositions" below is that file; its line numbers, and all others, are those of HEAD. Paths are relative
to VT; `audit/`, `checks/`, `claims/`, `pubmed_search/` and `revision/` are the folders of
`notes/review_2026-10-01_cold_reads/`. Nothing under VT was changed (`git status --short --ignored` is empty at the
end). Scratch files are under VW/X3/ (the scripts named below, their outputs, and `tree/`, an export of HEAD on which
the programs that write were run). No internet, no subject data.

**Result.** No finding of grade `error`. 13 findings: 5 `inexact` and 8 `note`. Of the 86 paragraphs of the last part,
82 are true of the files at HEAD as written and answer their finding in full; four are not exact as written (W6-13 and
W5-3; W7-3 and W2-4, notes), and the list that one more describes carries a small inexactness of its own (W4-1). Two
paragraphs of the part on the ten checks (VB-16, VC-2) were not carried along with corrections that the second check
brought, so that they now contradict the last part. The counts of the file and of the four other places agree with
the reports and with each other.

## Findings

**X3-1**
- Where: dispositions, last part, W6-13 (lines 2157–2158): "`check_numbers_revision.out` flags ten rows, each an
  unsigned print of a negative value whose direction the wording gives."
- Problem: ten rows are flagged, and each is an unsigned print of a negative held value. For three of the ten the
  wording gives the size and no direction: the Abstract's "0.01 of r₁ moves it by 0.061 nats, 0.1 of the lag-0
  correlation |q| by 0.019" (held −0.0189), Results 1's "and 0.01 of within-pair asymmetry |a_x − a_y| by 0.031" (held
  −0.0309) and Limitations' "only to within 0.053 nats for sts" (held −0.0530). For the other seven the wording does
  give it ("fell by", "exceeds the observed level by", "a fall of", and in Results 1 the derivative "∂sts/∂q = −0.19"
  beside the 0.019). The report that the paragraph answers has "whose direction or size the wording gives".
- Evidence: `checks/check_numbers_revision.out` lines 2, 4 and 11; `manuscript/draft_v2.md` lines 15, 53 and 201;
  `audit/recheck_W6.md` line 272. `check_numbers.py` run on the export of HEAD gives the committed output line for line.
- Grade: inexact

**X3-2**
- Where: dispositions, "The checks of the corrections", first sentence (lines 968–969): "After the corrections above
  were made, apart from those for C26 to C32 and for the point on S20 Table's rows 2, 5 and 8, which came later"; and
  the statement of the finding in W5-3 (lines 2059–2060): "came after the ten checks".
- Problem: not all of C26 to C32. By the file's own paragraphs the correction that C29 points to (R12: the Abstract's
  "most") and the words restored for C26 (T51 (ii)) were made before the report's second form raised them, and they were
  in the tree that the ten sessions read: two of the ten reports verify them. Of C26 only the claim record's item came
  later, and of C29 nothing did. The finding that the sentence answers names the corrections for C27, C28, C30, C31 and
  C32; of C26 to C32 as a whole it says only that their dispositions were not yet in the file. So the amended sentence,
  and the paragraph of W5-3 that restates the finding, do not agree with the opening paragraph and with the paragraphs
  of C26 and C29, which the file marks "Corrected." with corrections made before the ten checks.
- Evidence: dispositions lines 19–21 ("Two of the seven findings of the report's second form (C26, C29) were of things
  already corrected for findings of the other audits"), line 885 ("The words had been restored for T51 (ii) before the
  report's second form raised it") and line 909 ("As R12, corrected before the report's second form raised it");
  `audit/check_VR.md` line 117 ("R12 — verified. Abstract "underlies most fMRI synergy reports we found"");
  `audit/check_VT2.md` line 107 ("T51 verified. The three clauses are restored."); `audit/recheck_W5.md` lines 55–57
  and 217–218; for the item that did come later, `claims/claims_2026-10-01.md` lines 8–10 (the second form "brought
  the items on Luppi et al. (2023) and on Murray et al. (2014)").
- Grade: inexact

**X3-3**
- Where: dispositions, VB-16 (lines 1719–1720): "the names of the review folders (S5 Text §5) and the calibration
  scripts one by one (the sentence now has `notes/partB*.py`)".
- Problem: the paragraph was not changed with the correction for W6-2. The reason recorded with the replacement no
  longer speaks of scripts listed one by one: it has "the calibration scripts, given as a range and two names", which
  is what the committed sentence held. VB-16 still gives the reason the wording that W6-2 found wrong, and the two
  paragraphs of the file now disagree.
- Evidence: `revision/text_replacements_2026-10-01_cold_reads_revision.json`, entry DCA01, `why` (line 448) and `old`
  ("`notes/partB14_*.py`–`partB26_*.py`, `partB16b_*.py`, `partB17b_*.py`"); dispositions, W6-2 (lines 2116–2119).
  "one by one" stands in no other file of the review folder at HEAD, the reports apart.
- Grade: inexact

**X3-4**
- Where: dispositions, VC-2 (lines 1423–1424): "The item says what each place holds: … S3 Text §10 gives the authors and
  ΦID as a possible further generalisation".
- Problem: the paragraph was not changed with the correction for W7-10. The claim record's item now says that S3 Text
  §10 gives "the number of the authors and their relation to the ΦID paper's (four of that paper's seven, with two
  others)", and S3 Text §10 names no author of Liardi et al. (2025). VC-2 still gives the item the statement that W7-10
  found inexact.
- Evidence: `claims/claims_2026-10-01.md` lines 225–228; `manuscript/si/S3_Text.md` line 558 ("Four of the ΦID paper's
  seven authors, with two others, have proposed null-model normalisation"); dispositions, W7-10 (lines 2227–2229).
  "gives the authors" stands in no other file at HEAD, the reports apart.
- Grade: inexact

**X3-5**
- Where: `checks/numbers_update.out` lines 13–16: "to the paper's own sections, tables and figures (25 after "Results",
  17 after "Table" and 14 after "Fig", 10 of these before a panel letter, as in "Fig 1a")"; the disposition of W4-1
  (lines 1991–1993) gives the same grouping.
- Problem: the counts are right (below). One of the 17 numbers after "Table" is not of the paper's own tables: the
  Discussion's "their Table 1" is Table 1 of Luppi et al. (2022). The paper's own are 16, and the items of cited works
  include a table, a kind that the second list ("equations, definitions, an example and figures of cited works") does
  not have.
- Evidence: `manuscript/draft_v2.md` line 193: "the six macroscale associations of their Table 1 on that dataset"; a
  tokenisation of the covered text written for this check, with each of the 1,381 rows placed on its token by its
  context (VW/X3/tokens.py): the 17 tokens after "Table" that have no row, the four heads apart, are Table 1 four
  times, Table 2 six times, Table 3 four times, Table 4 twice, and "their Table 1".
- Grade: inexact

**X3-6**
- Where: dispositions, last part, W7-3 (line 2196): "The heading and the pointer name S3 Text §10 and the search note."
- Problem: the pointer names both. The heading names S3 Text §10 and not the search note.
- Evidence: `claims/claims_2026-10-01.md` line 162 ("## Luppi et al. (2026), Nature Human Behaviour 10, 777 (S20 Table,
  row 5; S3 Text §10)") and lines 173–174.
- Grade: note

**X3-7**
- Where: dispositions, "Found while the findings were settled", (4) (lines 1809–1810): "The source lines of S11 and S18
  Tables put the date after the pre-run entry's title alone, as the three places of S3 Text do for VO-4."
- Problem: true of S18 Table's source line. S11 Table's gives no title: it has "pre-run entry 1 Oct 2026, with its
  outcome entry". The date there stands with the pre-run entry alone, which is the point of the change, but it follows
  no title.
- Evidence: `manuscript/supplementary.md` lines 256 and 1590.
- Grade: note

**X3-8**
- Where: dispositions, VB-31 (lines 1782–1783): ""8,498 words with headings" is the output of `wc.py` …; without the 29
  markers the count is 8,469. Stated. The count stays the one the limit was set in."
- Problem: the two numbers are those of the tree that the check read. Since the corrections for W1-1 and W1-3 the
  output is 8,489 (8,362 without headings, 8,460 without the 29 markers), which the record, CLAUDE.md, README.md and
  `wc_revision.out` have. The paragraph is of something that is kept, and it does not say that the count it quotes has
  changed: "8,498 words with headings" now stands in no file but the reports. It is the one quotation of the earlier
  parts that lost its place between `checked2` and HEAD.
- Evidence: `wc.py` run on the export of HEAD: "total with headings 8489 without 8362", identical to
  `checks/wc_revision.out`; `manuscript/analysis_record.md` lines 9423 and 9488; CLAUDE.md lines 19 and 451; README.md
  line 39.
- Grade: note

**X3-9**
- Where: dispositions, R55 (line 382): "Every replacement has its own id, and the build of the file stops on a repeated
  one."; W5-10 (lines 2085–2086): "the program that writes this file stops on a cross-reference that is not returned".
- Problem: of the kind that W6-19 found. Neither program is in the tree, and neither sentence says that it is the
  planning session's and outside the repository, which is what the correction for W6-19 made the dispositions of VB-8,
  VB-20, VT2-14 and VE-20 say. What can be checked holds: the 287 replacements have 287 ids, and no cross-reference
  among the headings is one-sided.
- Evidence: `git -C VT grep -l` for "text_replacements_2026-10-01_cold_reads_revision" and for "dispositions_revision"
  in `*.py`, `*.sh` and `*.yml`: no file; dispositions, W6-19 (lines 2179–2182).
- Grade: note

**X3-10**
- Where: dispositions, "Points the audit of the citations raised outside its findings", the heading of the last point
  (line 957): "S20 Table's rows 2, 5 and 8, read in full by one of the second checks."
- Problem: "the second checks" here are sessions of the audit of the citations. Since the last part was added the file
  uses "the second check" for the seven sessions W1 to W7, the first time eleven lines below this heading ("which the
  second check covered (below)") and then as the title of its last part. Nothing in the point says which is meant, and
  read with the rest of the file the heading says that one of the seven read the three rows.
- Evidence: `audit/findings_citations.md` line 9 ("Second checks, second round") and line 226 ("One of the second checks
  of the second archive read rows 2, 5 and 8 of S20 Table in full"); dispositions lines 957, 968–969 and 1814.
- Grade: note

**X3-11**
- Where: dispositions, last part, introduction (lines 1836–1837): "Again no value of a result in the main text or in
  the supporting information was found wrong."; the same sentence in the record (lines 9473–9474).
- Problem: the sentence holds by the grades: no finding graded `error` is of such a value. One finding graded `inexact`
  is: W2-1, three limits of the Fisher-z intervals of S3 Text §6, each of which the correction moved by 0.001 (−0.270
  to −0.269, −0.099 to −0.098, −0.566 to −0.567). The introduction of the part on the ten checks says what was found
  inexact in the paper's files ("dates, pages, pointers and wordings"); this one does not, and what it leaves unsaid
  includes values.
- Evidence: dispositions, W2-1 (lines 1876–1883); `git -C VT diff checked2 HEAD -- manuscript/si/S3_Text.md`, line 406;
  record lines 9480–9481 ("three limits of the intervals of the residual's cross-half correlations, now computed from
  the unrounded correlations"); recomputed here from the committed per-subject series: [−0.897, −0.269],
  [−0.857, −0.098], [−0.567, +0.493].
- Grade: note

**X3-12**
- Where: dispositions, C32, the sentence added for the second check (lines 932–933): "Since the second check both name
  a second study of the table, row 4's, whose macaques were given ketamine before a scan under isoflurane (W7-8)."
- Problem: "both" follows a sentence whose two subjects are the Discussion's sentence and the search note. The
  Discussion's sentence names no study of the table. The two places that name the second study are S3 Text §10 and
  the search note, as the paragraph of W7-8 says; read by its grammar the sentence says it of the Discussion.
- Evidence: dispositions lines 931–932 ("The Discussion's sentence points to S3 Text §10 beside Methods, and the search
  note has a paragraph on it."); `manuscript/draft_v2.md` line 187 ("(Methods; S3 Text §10; Liardi et al., 2025, is a
  PID on MEG under LSD, ketamine and psilocybin)"); `manuscript/si/S3_Text.md` line 556;
  `pubmed_search/psychedelic_phiid_search.md` lines 92–95.
- Grade: note

**X3-13**
- Where: dispositions, last part, W2-4 (lines 1897–1898): "The comment names the split-half test's log
  (`splithalf.log`, B7); no printed line named a computation."
- Problem: true of the printed lines of item 10, which is what the finding says ("the item's printed label names the
  file and no computation"). As written it is wider: printed lines of the script's other items named computations then
  and name them now ("1. B16c", "2. B27", "3. B20", "5. B28", "B21 (d)'s formula" in item 6, "11. B27's table (a)",
  and item 12's "B27's pre-run entry").
- Evidence: `checks/derived_r24.out` lines 2, 35, 41, 50, 57, 75 and 78, the same labels in the file at `checked2`;
  `audit/recheck_W2.md` lines 74–75.
- Grade: note

## Checked and found exact

**1. The introduction of the last part.**
- The seven reports, their ranges and their subjects are as listed. Findings and grades recounted in the reports
  (VW/X3/grades.py): W1 5 (0, 4, 1); W2 7 (1, 3, 3); W3 12 (0, 6, 6); W4 14 (1, 5, 8); W5 16 (2, 7, 7); W6 20 (2, 8,
  10); W7 12 (0, 7, 5); in all 86: 6 errors, 40 inexact, 40 notes.
- The six graded errors are W2-4, W4-1, W5-1, W5-2, W6-1 and W6-2, which are the four things described.
- 85 paragraphs have "Corrected." and one "Stated." (W5-14); none has "Kept."; one verdict in each.
- The tree the seven read: `git -C VT log --oneline -3 checked2` gives eed9271 on 8bd189e, and the reports' headers
  name eed9271 and `checked` (9caa60b). The seven files are in `audit/`; none holds an absolute path.

**2. The 86 paragraphs of the last part** (each read with its finding in the report and against HEAD).
- One paragraph for each finding, in the reports' order, none twice and none besides; the grade in each is the
  report's (86 of 86).
- Each statement of a finding is fair to its report. Two say more than their own report does, both truly: W4-2 gives
  the six numbers of W6-9, which it names (W4-2 itself counts four), and W3-8 adds the folder's README, which no report
  named and which did say "arrays" at `checked2`.
- The 97 quotations (37 in the statements of the findings, 60 after the verdict) were extracted by script, searched in
  every tracked text file at HEAD (VW/X3/qsearch.py, wquotes.py) and then read at the place named. All 60 after a
  verdict stand word for word where the paragraph puts them: the main text (lines 87, 160 and 241), S3 Text (line
  556), S4 Text (lines 53 and 62), `supplementary.md` (lines 1590, 1601, 1619, 1647, 1664, 1706, 1711 and 1721), the
  literature file (lines 1, 7 and 17), the record (lines 9036–9037, 9156–9157, 9163–9164, 9183, 9228, 9295–9297,
  9314–9316 and 9417–9419), the numbers table's head note and the note of its 17 rows, `checks/numbers_update.out`
  (lines 334, 341–342, 357–358, 369, 386–387 and 391), `checks/derived_r24.out` (line 80), CLAUDE.md (line 19), the
  folder's README (lines 65–66), the claim record (lines 63, 165, 195, 220 and 226–227), the figure script (line 474),
  the `why` of M06, I03, R201, R205, R403, DCA01, A01 and D04, and, for W5-12, the paragraph of VR-4. The quotation of
  W5-13 is on p. 3 of Gao2026.pdf.
- Each correction answers every part of its finding, X3-1, X3-2, X3-5, X3-6 and X3-13 apart. Read in particular:
  - W1: Methods' parenthesis names no section, and the `why` of M06 names the next subsection of Methods and
    Limitations; the record's disposition of B's MINOR 8 names both places under the quoted words; the four titles of
    VM-8 against the file's and the list's (S1 and S9 without their parentheses, S9 without its time of day; S17 and
    S18 with computation labels); the main text has "bins" and 31 references of the form "S3 Text §n", no time of day
    and no computation label; the four rows of Table 2's caption cite the record's line 1747.
  - W2: item 10 of `derived_r24.py` computes the correlations from `diag_series_<variant>_W60.npz` and
    `splithalf_subjects.csv` and asserts that they, the reliabilities and their p equal the log's; items 11 and 12 as
    described; the twelve values of ENTRY12 are those of the pre-run entry's item (i) (record lines 8608–8628); the
    comment names "splithalf.log, B7"; the script run on the export of HEAD reproduces `derived_r24.out` but for the
    commit in its first line. Recomputed from the committed files with code written for this check: the four cross-half
    correlations (−0.384543, −0.699541, −0.597558, −0.051497) with their eight limits, means, reliabilities, ceilings
    (0.605, 0.392) and ratios (0.90, 0.83), the larger correlation above the ceiling on both variants; 3,068
    assignments counted from the file, the tie (bound 0.64 × 10⁻⁶) and the margin 0.43 × 10⁻⁶ (bound 0.50 × 10⁻⁶), the
    nearest uncounted pair 0.71 × 10⁻⁶ away (bound 0.36 × 10⁻⁶), so 3,064 to 3,068; the twelve values of item 12; the
    SDs 0.0887, 0.0485 and 0.0524 and r² 0.79 and 0.75; the slope 4.263 with 4.139 to 4.535.
  - W3: S19 Table's head note (both lists, Fieller's g); the row of B24's expectations against S3 Text §6 (the
    residual table's last column; the text and the table under the next heading); the 24 rows of Part A that differ
    from `checked2` are the six of the finding, the seventeen that W3-4 lists, and the row of W3-2, each changed as
    described; the Part B row; S18 Table's source line names the three kinds of column that its eleven columns lack
    of the result file's fourteen; S4 Text's rows S6 and R1 (five kinds; S3 Text §4 and §6, S1, S14 and S17 Tables);
    S20 Table's head note, the literature file's title and search paragraph; what `derived_r24.py` reads: two
    pickles, six CSV files, two tables files, three array files and one log.
  - W4: the count of 70 and its parts, by the tokenisation named under X3-5: 25 after "Results", 17 after "Table", 14
    after "Fig" (10 before a panel letter), 7 equations, 3 definitions, 1 example and 3 figures of cited works; also
    95 citation years, 13 day numbers and 11 years of dates; no page number. The six forms in the list, and the six
    numbers at their places (Fig 3's caption, S13 Table's note, S18 Table, Table 3); the record's dispositions of A's
    m8 and w1, of B's MINOR 8 and of C's M1, its item (iii) of "B28, outcome", its list of what `checks/` holds and
    its sentences on the works and on ketamine; the Ethics statement (main text, line 209); the head note's six
    kinds, word for word the record's.
  - W5: CLAUDE.md has "1/10" nowhere and "spin p" at line 71 only; the four headings; the four lists of the record's
    paragraph; R25, R38, VN-3 and the two cells of row 5; VR-4, VR-5, VR-14, VS-11, VT2-13; the opening sentence of
    `check_VT2.md` (8 and 8), the only one of the seventeen reports whose own summary differs from the grades of its
    findings.
  - W6: the 17 rows with the new note (3 committed, 14 added), the five rows that gained "@pct|", the three label
    notes, the held string 0.830, the derivation of the row of 18 % (0.012673 / 0.071895 = 17.6 %; line 135 of
    `inference_rows_prewhiten_fixed.csv`); Fig 3's caption names Table 3 twice and no earlier place does; the
    committed `check_numbers.py` tests the held string of data rows and no anchor.
  - W7: the claim record's head, its items on Liardi et al. (2025), Luppi et al. (2026), Murray et al. (2014), and
    its sections on Gatica et al. (2024) and Down et al. (2026); `screening.md`, row of Pope et al. (2025); S3 Text
    §10 and the search note on the second study.
- The 14 paragraphs "As …" each point to a paragraph that answers their finding too, and each is returned by a
  "Found also by".
- Statements of the file about cited works, read in the PDFs where the page has a text layer (the last part's, and
  for Luppi et al., 2026, those of C32 and of the point on S20 Table's rows): Gao2026.pdf p. 3 (the solver phrase);
  Gatica2024.pdf p. 12 (isoflurane; ketamine at 10 mg/kg with five other agents; scanning about two hours after
  anaesthesia; the journal's p. 1043) and p. 1 (no drug in title, keywords or abstract); Down2026.pdf (25 pages
  labelled 1/55 to 25/55; p. 4, the fMRIPrep output in the supplementary materials; the references from p. 20);
  Luppi2025.pdf p. 1 ("Légaré", "David K. Menon"); Pope2025.pdf, PDF pp. 3, 5 and 6 (named and chosen; section 2.2.2;
  Eq. 7); Murray2014.pdf pp. 1–2 ("primate cortex", "monkeys"; the macaque and the seven areas on p. 2; "motor"
  nowhere); Luppi2026.pdf pp. 3–5 (the three anaesthetics; the three group sizes; 43 mice).

**3. The amended paragraphs of the earlier parts** (`git diff checked2 HEAD`, compared paragraph by paragraph:
VW/X3/blocks.py).
- Changed: the title; the opening paragraph; the headings of R12, R25, T29 and T51; R32, R38, T18, T61, C28, C32; the
  first and the third paragraph of the part on the ten checks; VO-2, VO-6, VE-8, VE-13, VE-20, VE-23, VR-4, VR-5,
  VR-14, VT1-8, VT2-6, VT2-10, VT2-13, VT2-14, VT2-17, VN-1, VN-3, VN-4, VM-1, VM-3, VM-8, VM-10, VS-3, VS-11, VS-12,
  VB-8, VB-20, VB-25, VB-27; "Found while the findings were settled". No other paragraph of the earlier parts differs.
- Every changed sentence was read against the files at HEAD and against the finding it answers, and every quotation
  of these paragraphs is at the place named (VW/X3/aquotes.py). X3-2, X3-7 and X3-12 apart, they hold.
- "Found while the findings were settled": (1) the head note at 8bd189e has "(B21 (b) and (c); the reproductions in
  B23)" and at HEAD says that the ten rows of B23 are counted and names the two sets without a row; (2) "Legare, A."
  at 8bd189e, "Légaré, A." at HEAD (`supplementary.md` line 1742), with "Menon, D. K."; (3) the heading of the
  paragraph (S3 Text line 124), the paragraph being absent at 8bd189e; (4) see X3-7; (5) row B27 (a): "Results 2;
  Table 2; S3 Text §5", and the three cells of VS-9 as quoted.

**4. The whole file** (VW/X3/whole.py, xref.py, allquotes.py, allquotes2.py, allquotes3.py).
- (a) 57 + 63 + 32 = 152 headings, R01–R57, T01–T63 and C01–C32 in order, each with one block and the grade of its
  report (1, 12, 30, 14; 3, 18, 31, 11; 2, 5, 17, 8); 157 paragraphs for the ten checks, in the reports' order, with
  the reports' grades (VO 13: 0, 4, 9; VE 25: 1, 12, 12; VR 17: 2, 9, 6; VT1 10: 1, 5, 4; VT2 17: 1, 7, 9; VC 9: 0, 7,
  2; VN 11: 0, 1, 10; VM 10: 0, 4, 6; VS 12: 0, 7, 5; VB 33: 6, 13, 14; in all 11, 69, 77); 86 for the second check.
- (b) 95 headings carry 110 cross-references; none is one-sided; every "As <id>" of a block is named in its heading.
  Every id mentioned anywhere in the file exists.
- (c) 147 "Corrected.", 2 "Stated, not changed." (R46, T25) and 3 "The audit's instructions." (R44, R45, T53) in the
  first three parts; 142 "Corrected.", 7 "Stated." (VO-9, VE-14, VR-16, VT2-6, VS-12, VB-22, VB-31) and 8 "Kept."
  (VE-22, VE-25, VT2-10, VN-7, VN-8, VN-10, VM-9, VB-33) in the part on the ten checks; the eleven errors as described
  (four of one number; seven on the bookkeeping; four replacements and a fifth for VB-2); 85 and 1 in the last part.
- (d) No line longer than 120 characters, headings apart (the longest has 118); no tab, no trailing space.
- (e) The 571 quotations of the file were searched at HEAD and at `checked2`: of those that follow a verdict in the
  earlier parts none has lost its place, and the one quotation of a statement of a finding that has is VB-31's
  (X3-8). The wordings that the second check corrected in other files were searched in the earlier parts: two remain
  (X3-3, X3-4). No other statement of the file was found to contradict another, X3-2 and X3-10 apart.
- Every change between `checked2` and HEAD in the files that the dispositions describe was mapped to a finding of the
  second check or to its bookkeeping: `supplementary.md` (29 lines), S3 Text (3), S4 Text (2), S5 Text (1), the main
  text (2), the literature file (3), CLAUDE.md (4), README.md (1), the figure script (1), `screening.md` (1), the
  record's five entries (15 paragraphs, five of them the headings' time), `numbers_update.out`, `derived_r24.py`, the
  claim record, the search note, the folder's README, 30 rows of the numbers table, 21 changed `why` and 10 new
  entries of the replacements file. None is left without a paragraph of the last part.

**5. The other places that state the same counts.**
- S5 Text §5 (line 33): three audits, 152 findings; ten further sessions, 157 findings; seven more, 86 findings; the
  file named.
- The record, "The audits of the prepared revision" (lines 9429–9485): 63 (3, 18, 31, 11), 57 (1, 12, 30, 14), 32 (2,
  5, 17, 8); 25 findings and eight works for the first form and seven findings added, as the dispositions' opening
  paragraph has them (the first form itself is not in VT); 152 with 147, 2 and 3; ten sessions whose
  parts sum to ten (1 + 1 + 4 + 1 + 1 + 1 + 1), 157 findings with 11, 69 and 77, 142, 7 and 8; seven sessions with the
  seven parts of the reports, 86 findings with 6, 40 and 40, the four things, 64, 74 and 70, 85 and 1; `check_*.md`
  and `recheck_W1.md` to `recheck_W7.md`. Its list of the corrections in the paper's files agrees with the diff.
- CLAUDE.md, the bullet on round 24 (lines 430–451): three sessions, then "twice (ten sessions, then seven)"; 70
  findings of the reads; 1,381 rows; 8,489 words.
- The folder's README, the bullet on `audit/` (lines 78–87): the three reports with `te_filter_check.py`, the ten
  `check_V*.md` named one by one, `recheck_W1.md` to `recheck_W7.md`, `dispositions_revision.md`, and `findings.md`
  and `dispositions.md` of the earlier commit: each file is in the folder, and the folder holds no other report.

**Not verifiable from the tree.** What the file says of the planning session's preparation, packaging and checks (R01,
R08, R09, R55, VE-20, VB-8, VB-20, VT2-14, W5-10); that the reports are as the sessions returned them; the first form
of the report on the citations (its 25 findings and its list of eight works), which is not in VT: the second form
speaks of "the eight PDFs of the second archive" and of "the six works then asked of V.S."
(`audit/findings_citations.md` lines 5 and 11), and its C01–C25 are unchanged between `checked2` and HEAD; that V.S.
was asked for the complete file of Down et al. (VN-5). Not redone here: the reading of every "reported at" cell of
S19 Table's
Part A against the main text (W3-4), beyond the 24 changed cells and five places opened in the main text (the
disattenuated value in the Abstract, the Discussion and Fig 3's caption; the mean-FD DiD in the Discussion;
Limitations' sentence on the coupling change; g in Methods, Inference); and pages 33–41 of Luppi2026.pdf, which have
no text layer.
