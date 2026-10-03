# W5 — the dispositions file

Part: `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md` at HEAD (eed9271), against `checked`
(9caa60b), the ten reports `audit/check_V*.md` and the files the dispositions name. "Dispositions" below is that file;
its line numbers, and all others, are those of HEAD. Nothing under VT was changed (`git status --short --ignored` is
empty at the end). Scripts and their outputs are in VW/W5/.

Result: 16 findings: 2 errors, 7 inexact, 7 notes. No quotation of the last part is missing from the files; every
finding of the ten reports has its one paragraph; the counts of the introduction hold.

## Findings

**W5-1** — error
- Where: dispositions, last part, VT2-10 (lines 1352–1354): "Kept. The bullet is part of the file's dated history and
  records what was written that day. The paper's files and the file's account of this revision have "p < 1/10,000"."
- Problem: CLAUDE.md has the phrase nowhere. Its account of this revision (the paragraph under "Current state", line
  19; the bullet "Round 24 (bundle 35B; …", lines 430–451; the bullet on the subject codes, line 56) does not give
  the spin p. The only statement of that p in the file is the bullet that is kept, "spin p < 0.0001" (line 71). The
  first half of the sentence holds: the paper's files have "p < 1/10,000". The reason given for keeping the bullet
  (dated history) is not touched.
- Evidence: the string "1/10" occurs in no line of `CLAUDE.md`; "10,000" occurs once (line 330, "under 10,000
  words"); "spin" with a p occurs at line 71 only. `manuscript/draft_v2.md` line 114, `manuscript/si/S3_Text.md` line
  130 and `manuscript/supplementary.md` lines 101 and 1623 have the phrase.
- Grade: error.

**W5-2** — error (in `checks/numbers_update.out`, the file that the dispositions of VR-9, VB-8 and VE-4 describe)
- Where: `numbers_update.out`, lines 13–14: "64 cross-references by number in the running text and the captions
  (Results, Fig, Table, Eq., Example, Definition, pages)". Dispositions, VR-9 (lines 1223–1225): "The file counts each
  kind apart"; VB-8 (line 1645): "The counts are those of the build's pass over every number token of the text."
- Problem: The covered main text has 74 cross-references by number that carry no row, the captions' own heads apart,
  not 64. The file's other counts hold (95 citation years; 13 day numbers and 11 years of the dates; the 10 numbers of
  the captions' heads; the DOI; 9 number tokens in the headings). With 64 the list accounts for 194 of the 204 number
  tokens that have no row (the leading digits of two commit identifiers apart), so that what VB-8 found (191 of 203)
  is true again of ten tokens. Ten is the number of the figure references that carry a panel letter (Fig 1a three
  times, Fig 1c, Fig 3a, 3b, 3c, Fig 4a, 4b, 4c), which the file does not say that it leaves out, and also the number
  of the captions' heads, which the file now counts apart and which the earlier 73 did not hold (VR-9, VE-4, VB-8).
  Rows do sit on tokens that a letter follows ("2S", "50th"), so that such tokens are tokens of the table.
- Evidence: VW/W5/place4.py (output place4.out) places each of the 1,381 rows on a number token by its context (1,592 tokens
  in the title, the text from the Abstract to the end of Data and code availability and the list of supporting
  information, headings and code spans apart). Tokens without a row: 95 citation years, 13 day numbers, 11 years of
  dates, 74 cross-references (Results 29; Table 17; Fig, Fig. and Figure 17; Eq. 5; Eqs. 2; Definition 3; Example 1),
  the 10 caption heads, the DOI, the leading digits of 77af7aa and 13e7299, and the five "10" of powers of ten, which
  belong to rows. Four further cross-reference numbers carry a label row (rows 37–40; with row 1233, a citation year,
  the "5 label rows" of the head note). Run on `checked`, the same script gives 73, the count the file had then, which
  three of the ten sessions recounted: check_VR.md, VR-9 ("83 cross-reference tokens = 73 + 10 caption labels");
  check_VE.md, VE-4 ("73 cross-references, the DOI, the ten caption labels"); check_VB.md, VB-8 ("Results 28, Table
  17, Fig/Fig./Figure 17, Eq./Eqs. 7, Definition 3, Example 1"). The text has since gained one, "(Results 4; S13
  Table)" in Results 2 (draft line 108).
- Grade: error.

**W5-3** — inexact
- Where: dispositions, last part, first sentence (lines 964–965): "After the corrections above were made, ten further
  sessions of the AI system, started by the planning session on 2 October 2026, each checked one part of the corrected
  revision against the files".
- Problem: Not all the corrections above. The dispositions of C26–C32 and the point "S20 Table's rows 2, 5 and 8" are
  not in the file at `checked`, and the corrections they state for C27, C28, C30, C31 and C32 and for that point are
  not in the tree that the ten sessions read (9caa60b): they enter between `checked` and HEAD. None of the ten reports
  covers them (check_VC.md is of "the citation dispositions (C01–C25)").
- Evidence: the file at `checked` ends its third part at C25 and has four points. `git diff checked HEAD`:
  `draft_v2.md` line 154 ("(2023), as we read it,") and line 187 ("S3 Text §10;"); `pubmed_search/screening.md` lines
  8–11, 21 and 27–29; `pubmed_search/psychedelic_phiid_search.md` lines 64–73 and 89–94; `S3_Text.md` line 556 (the
  sentence on ketamine); `supplementary.md` line 1721 ("(sevoflurane, propofol or ketamine; p. 3; p. 35)",
  "(pp. 4–5)") and line 1669 ("as we read their Methods"); the `why` of U17.5 and LT07.5.
- Grade: inexact.

**W5-4** — inexact
- Where: dispositions, "Found while the findings were settled" (line 1761): "One thing that no session raised was
  corrected with them."
- Problem: More than one. Between `checked` and HEAD two further changes answer no finding of a session and are named
  in no disposition: (a) "Legare" becomes "Légaré" in the entry of Luppi et al. (2025) among the references cited only
  in S20 Table (VN-11 raised "Menon, D." alone, and its disposition names that alone); (b) the heading of S3 Text §3's
  paragraph on the transfer entropies, "(1–2 October 2026)", becomes "(written for the revision of 1–2 October
  2026)". Two more changes go beyond the dispositions that lie nearest: the source lines of S11 and S18 Tables no
  longer put "1–2 Oct 2026" after the pre-run entry and its outcome together, where VO-4's disposition names three
  places of S3 Text; and row B27 (a) of S19 Table gains "Table 2;", where VS-9's names B17b, B27 (b) and B27 (c).
- Evidence: the replacements U22 (new at HEAD; `why`: "The preprint prints the author's name as Antoine Légaré."),
  S317 (its `new` changed, its `why` unchanged and silent on the heading), U02, U05 and U06 (their `new` changed);
  `supplementary.md` lines 1742, 256, 1590 and 1671; `S3_Text.md` line 124; check_VN.md lines 68–71. Neither
  "Legare", "Légaré" nor "written for the revision" occurs in the ten reports or in the dispositions.
- Grade: inexact.

**W5-5** — inexact
- Where: dispositions, first part, R32 (lines 243–246): "The paragraph is rewritten in three lists: the statements
  now in the supporting information or in a table, each pointed to from the main text".
- Problem: The record's paragraph "The length and the tables" now has four lists. The correction of VE-8 divided the
  last: "Sentences retired by a rule or a finding, not for length: …" and "Two sentences retired for length: …". R32
  was not changed with it and still names three, the third as "the sentences retired by a rule or a finding".
- Evidence: record lines 9381, 9393, 9396 and 9400; dispositions, VE-8 (lines 1111–1115).
- Grade: inexact.

**W5-6** — inexact
- Where: dispositions, VR-14 (lines 1246–1248): "The three say that the study was found by the search of 1 October
  2026 and read in full on that date, and that the row was added in the revision of 1–2 October 2026".
- Problem: True of S20 Table's head note and of S3 Text §10. The literature file's title, the first of the three
  places that the disposition names, has the last statement only: "with row 10 added in the revision of 1–2 October
  2026". That the study was read in full on that date is in the file's paragraph on the search, and that the search
  found it is in row 10 itself.
- Evidence: `notes/partB5_literature_v2.md` lines 1, 7 and 22; `supplementary.md` line 1711; `S3_Text.md` line 556.
- Grade: inexact.

**W5-7** — inexact
- Where: dispositions, VR-5 (lines 1207–1208): "CLAUDE.md: "their PDF files are identical once the two date fields,
  the cross-reference table and the `startxref` offset are masked"; the disposition of R56 quotes it."
- Problem: R56 does not quote the sentence. Its one quotation is the title "Remaining work"; it gives the condition
  without quotation marks and in another form: "their PDF files identical once the two date fields, the
  cross-reference table and the `startxref` offset are masked". The quotation itself is word for word in CLAUDE.md,
  and what R56 says of CLAUDE.md is true.
- Evidence: dispositions lines 386–389; `CLAUDE.md` lines 457–458.
- Grade: inexact.

**W5-8** — inexact (VO-6; not one of the three reports of item 2 of the task, met in reading the quotations)
- Where: dispositions, VO-6 (lines 1035–1037): "from `baseline_gap.csv`, which `derived_r24.py` now recomputes and
  compares with the pre-run entry's values (item 12 of its output; S19 Table's Part B has the row)".
- Problem: The script recomputes the nine values and prints them. It holds no value of the pre-run entry and compares
  nothing. The printed values do equal the pre-run entry's (0.79; 0.0887 and 0.0485; +0.0949, −0.1121 and −0.0172;
  −0.2795 and +0.0914; +0.0005), which is the reader's comparison. The record's own sentence says only "from
  `baseline_gap.csv` (`notes/review_2026-10-01_cold_reads/checks/derived_r24.out`, item 12)".
- Evidence: `checks/derived_r24.py` lines 303–321 (item 12: its one assertion is on the 14 subjects of the selection;
  no expected value); `derived_r24.out` lines 78–79; record lines 8608–8622 (the pre-run entry's values) and
  8904–8906. The nine values were also recomputed from `baseline_gap.csv` (VW/W5/recompute.py).
- Grade: inexact.

**W5-9** — inexact
- Where: dispositions, first part, R25 (lines 195–197): "Row 5's two cells on HRF deconvolution say what was read,
  the article with its Extended Data and its Reporting Summary, and that the Supplementary Methods were not"; VN-3
  (line 1451): "and the row's last cell likewise"; R38 (lines 276–277): "say only that the Supplementary Methods the
  study defers to were not read (row 5)".
- Problem: Row 5 has two cells on HRF deconvolution. The preprocessing cell says both things. The last cell says what
  was read and nothing of the Supplementary Methods: "HRF deconvolution is not mentioned in the PDF read (the
  article, its Extended Data and its Reporting Summary)". R25's sentence therefore holds of one of the two cells and
  VN-3's "likewise" of the first half only; the reasons recorded with the two replacements of the last cell say that
  it "carries the qualification of its preprocessing cell", the Supplementary Methods included. R38, unchanged since
  `checked`, still says that row 5's cell says "only" that the Supplementary Methods were not read; since the
  correction of VN-3 the cell also says what was read. R38's point, that the cells carry no request, holds.
- Evidence: `supplementary.md` line 1721, fifth and tenth cells (the same ten cells in
  `notes/partB5_literature_v2.md` line 17); the `why` of U17b.1 and LT07b.1.
- Grade: inexact.

**W5-10** — note
- Where: dispositions, VR-17 (lines 1257–1258): "the only one-sided cross-reference among the headings. Corrected. The
  heading reads "R33 — minor (also T38)"."; the headings of C26, C29 and C31 (lines 880, 904, 917).
- Problem: R33's heading is corrected. At HEAD four cross-references among the headings are one-sided, all brought by
  the dispositions added after the checks: C26 names T51, C29 names R12 and T29, C31 names R25, and the headings of
  T51 ("T51 — minor"), R12 ("(also T29 (iv))"), T29 ("(also R12)") and R25 ("(also T45)") do not name them.
- Evidence: parse of the 152 headings; dispositions lines 112, 192, 548 and 652.
- Grade: note.

**W5-11** — note
- Where: dispositions, VS-11 (lines 1595–1596): "Corrected. Both: "confirmed on ts_gsr, the variant the script reads
  for this check"."; VR-12 points to it.
- Problem: S19 Table's row B29 (d) has the words as quoted. S3 Text §5 has them with ts_gsr as a code span:
  "confirmed on `ts_gsr`, the variant the script reads for this check". Other quotations of the file carry the code
  marks of their source (VR-10, VE-23, VB-31).
- Evidence: `supplementary.md` line 1682; `S3_Text.md` line 299.
- Grade: note.

**W5-12** — note
- Where: dispositions, VR-4 (lines 1202–1203): "the disposition of R48 gives condition (1) in the record's words".
- Problem: Nearly. R48's condition (1) differs from the record's sentence in four places: "differs in six" for
  "differs from it in six", "the header" for "its header", "the text commit's" for "this commit's", "the main text's"
  for "the main text's caption". The content is the same.
- Evidence: dispositions lines 335–338; record lines 9475–9478.
- Grade: note.

**W5-13** — note
- Where: dispositions, VT2-13 (lines 1367–1368): "gives each with its page, read again in the PDF: "persistent
  synergy", "persistent redundancy", "Gaussian MMI solver" and "246 x 246" (p. 3)".
- Problem: S20 Table's row 10 has the third phrase as "the Gaussian MMI solver", with the article inside the quotation
  marks; the claim record, which says that it gives the words of the row that stand in quotation marks, gives
  "Gaussian MMI solver". Whether the article is the work's cannot be told from the tree.
- Evidence: `supplementary.md` line 1726; `claims/claims_2026-10-01.md` lines 87–91.
- Grade: note.

**W5-14** — note
- Where: dispositions, the list of the reports (lines 978–979): "`check_VT2.md` (VT2-1 to VT2-17): … 17 findings (1
  error, 7 inexact, 9 notes)"; line 990: "graded by the sessions as 11 errors, 69 inexact statements and 77 notes".
- Problem: The counts are those of the grades that the seventeen findings carry, which is how the other nine reports
  count too. The report's own opening sentence counts otherwise: "1 wrong number in the record's last entry, 8
  inexactnesses … and 8 notes". By the reports' own summaries the totals would be 70 and 76.
- Evidence: check_VT2.md line 3, against its headings (inexact: VT2-1, 2, 3, 5, 6, 8, 9; notes: VT2-7 and 10–17).
- Grade: note.

**W5-15** — note
- Where: dispositions, the description of the eleven errors (lines 992–996): "one wrong number in the record's entry on
  the revision" and "the reasons recorded with four replacements (VB-4, VB-5, VB-6)".
- Problem: The description holds of what it names. VB-2, one of the eleven, also found its wrong place in the reason
  recorded with a fifth replacement (R205) and in the record's entry itself (the intervals of the two cross-half
  correlations placed in Fig 3b), as VB-2's own disposition says.
- Evidence: check_VB.md lines 16–19; dispositions lines 1612–1618.
- Grade: note.

**W5-16** — note (the figure script; beside R49, VT1-2 and VE-21)
- Where: `scripts/15_figures_v2.py` line 474, the comment on the legend's line: "# the same distance below the taller
  panel"; dispositions, R49 (line 347): "it stays about as far below the taller panel".
- Problem: After the checks "keeps its distance" was changed to "stays about as far" in R49 and in the script's
  revision note, and the record says "about as far", the distance being about 2 % greater (VE-21: "from 0.42 to
  0.4286 of the former panel height"). The comment on the line of code still says "the same distance".
- Evidence: `git diff checked HEAD -- scripts/15_figures_v2.py` (lines 21 and 26 alone change); script line 474;
  record line 9482; check_VE.md, VE-21.
- Grade: note.

## Checked and found exact

**1. The first three parts as changed (item 1).** Each `### <id>` block, the opening paragraphs and each paragraph of
the part on the points were extracted at `checked` and at HEAD and the joined texts compared (VW/W5/blocks.py): at
`checked` 145 dispositions and 4 points, at HEAD 152 and 5. Changed or new are the opening paragraphs; R09, R19, R22,
R25, R26, R33, R34, R35, R48, R49, R56; T03, T12, T18, T19, T25, T37, T46, T58, T61; C04, C14, C17, C21; C26–C32
(new); the points ""The ΦID authors" for Liardi et al. (2025)" and "Murray et al. (2014)", and the new point on S20
Table's rows 2, 5 and 8. Their 64 quotations were found by script and then read at the place named; all stand word
for word, R19's "a scope map" being what README.md had (line 22 at 8bd189e: "a scope map of `sts`"). What each says
of the files, verified, W5-9 apart:
- Opening paragraphs: 57 + 63 + 32 = 152 headings, their grades those of the three reports (1, 12, 30, 14; 3, 18, 31,
  11; 2, 5, 17, 8); 147 "Corrected.", 2 "Stated, not changed." (R46, T25), 3 "The audit's instructions." (R44, R45,
  T53). `findings_citations.md` at HEAD equals the returned second form but for a final newline, its form at
  `checked` equals the returned first form, and its first 25 findings are identical in the two, block by block. The
  first form lists as not checked the statements about the eight works of the second archive (Varley et al. 2024;
  Luppi et al. 2023 and 2026; Zhang et al. 2025; Pope et al. 2025; Murray et al., Raut et al. and Ito et al.). C26
  and C29 were already corrected in the `checked` tree (draft lines 114 and 15 do not change for them).
- R09: every number token of the covered text has a row or is of a kind the head note names (VW/W5/place4.py), five
  label rows sitting on such tokens as the head note says; `numbers_update.out` lists 264 deleted rows (161 + 64 + 7
  + 28 + 4 by class) and 24 rows carried by a fallback (20 + 4); the unsigned 0.0112 and the "20" of Methods
  (Literature search) are among the deleted; two rows of 0.05 in Methods (Inference) and two of 1 in Methods
  (Remedies).
- R19: draft lines 191, 441 and 397; S3 Text line 128; S5 Text line 7; README.md lines 22–23; the note of numbers row
  103; the record's disposition of A's m8 (lines 9216–9221).
- R22: draft line 237; S3 Text line 260; `derived_r24.out` line 69; record lines 8941–8943 (the paragraph on the sts
  rows), 8970–8972 (item (v)) and 9289–9292. Recomputed from `baseline_gap.csv`: 4.262661 with all 14, 4.139204
  without subject 14, 4.534629 without subject 8.
- R25, C31: record lines 9332–9333; the `why` of U17.5 and LT07.5 name C's M4. R26: S2 Text line 9; draft line 87;
  record lines 8957–8960. R33: S5 Text line 9, and the heading (line 248). R34: S1 Text line 5. R35:
  supplementary.md line 1689 and row B27 (d), line 1674.
- R48: `figures_check.py` read line by line against conditions (1)–(3) as the disposition states them. R49: script
  line 471; the legend's anchor (0.0, −0.25) for (0.0, −0.42). T12: record lines 9479–9482; the script's height
  ratios (0.60 / 0.70 is six-sevenths) and the legend's 6.5 pt against a title of 6.8 pt. R56: every file of the
  review folder is named in its README and every file the README names is in the tree; CLAUDE.md lines 452–458.
- T03: draft line 114; S3 Text line 132; `derived_r24.out` lines 63–67; the record's dispositions of B's MINOR 3 (a)
  (lines 9266–9269) and of A's m9 (9221–9224). T18: draft lines 116 and 241; the record's disposition of B's MINOR 8.
  T19, C04: supplementary.md line 1719, literature file line 15, draft line 25, claim record lines 181–187. T25:
  draft line 124, supplementary.md line 363, S3 Text lines 321 and 337 (+0.0115 / −0.0155 = −0.742). T37: S5 Text
  lines 33 (§5) and 37 (§6); README.md lines 37 and 73; CLAUDE.md lines 19 and 591.
- T46: 19 rows of N = 14 at 8bd189e named line 2 of `results/primary_b_ts_gsr_win60.csv`; at HEAD 34 rows name line
  48 of the record (the 19, the 14 added, and the row of Table 2's caption that the check of the corrections moved).
  All 1,065 rows with a line locator hold their anchor and their held string on the line named, the notation's
  prefixes read as the head note explains them (VW/W5/locators.py).
- T58: draft lines 108, 124, 110 and 245; S3 Text line 395. T61: S3 Text lines 505 and 544; supplementary.md lines
  309 and 331; record lines 9131–9133; the five uses of "artefact" in the manuscript files (draft line 187; S3 Text
  lines 305 and 550; supplementary.md lines 1617 and 1618).
- C14: claim record lines 143–145; the `why` of D05 and S319. C17: claim record lines 21, 33–34, 65–67, 97–98. C21:
  S1 Text line 11; S4 Text line 14. C26: draft line 114; claim record lines 171–179. C27: draft line 154;
  supplementary.md line 1669; claim record lines 150–157. C28: `screening.md` lines 8–11, 21 and 29. C29: draft line
  15. C30: the search note, lines 64–73. C32: S3 Text line 556; supplementary.md line 1721; draft line 187; the search
  note, lines 89–94.
- The points: S3 Text line 558, and the two author lists in the main text's references (lines 331 and 341: four of
  the six are among the seven, the first author of the six is not); the `why` of R301 ("'In the literature'
  dropped"), and the sentence of Results 3 at 8bd189e, which begins with those words; the pages of row 5 (37, 38, 39,
  40; 4–5) as the claim record's item on Luppi et al. (2026) gives them, and the second form's three things under
  "Not checked".
- The other dispositions of the first three parts are unchanged since `checked`. Their 128 quotations were searched
  at HEAD as well: all are found ("Checked and found exact" is a heading of the reports). Their statements were read
  again against the files as they stand after the changes between `checked` and HEAD (word diffs of the main text
  and of S3 Text; the record's entry; the supplementary tables' rows; the `why` fields): beyond W5-5 and W5-9 they
  hold. R08: the four passages of S3 Text (lines 231, 264, 395, 531) name the reviewers by role with "(S5 Text §5)",
  the two of §6 and §8 now giving the statistical reviewer's request and the methods reviewer's part apart. T38
  (iv): the five cells name S5 Text §1 (lines 1619, 1621, 1632, 1642, 1643). T56: the record's list of the note's
  items and CLAUDE.md's are word for word the same. R45: no line of the five new entries exceeds 120 characters.

**2. The introduction of the last part (item 2).** The ten reports, their ranges and their subjects are as listed.
Findings and grades, counted in the reports (VW/W5/grades.py): VO 13 (0, 4, 9); VE 25 (1, 12, 12); VR 17 (2, 9, 6);
VT1 10 (1, 5, 4); VT2 17 (1, 7, 9); VC 9 (0, 7, 2); VN 11 (0, 1, 10); VM 10 (0, 4, 6); VS 12 (0, 7, 5); VB 33 (6, 13,
14); in all 157: 11, 69, 77. The grade in each of the 157 paragraphs equals the report's. The eleven errors are VE-1,
VR-1, VT1-1 and VT2-4 (the 4.54) and VR-2, VB-1 to VB-6; VB-4 and VB-5 concern one replacement each and VB-6 two. Of
the 69 findings graded inexact, 18 concern the main text or the supporting information, and none of them a value of
a result: dates (VO-4, VR-3, VS-1, VS-2), pages (VN-1), pointers (VO-2, VT2-8, VS-3, VS-4) and wordings (VO-1, VR-7,
VT1-6, VM-1, VM-2, VM-8, VS-5, VS-6, VS-7). "Corrected." 142, "Stated." 7 (VO-9, VE-14, VR-16, VT2-6, VS-12, VB-22,
VB-31), "Kept." 8 (VE-22, VE-25, VT2-10, VN-7, VN-8, VN-10, VM-9, VB-33), one verdict in each paragraph; the corrected
dispositions with a second part that is kept are VT1-10, VM-6 and VM-8. For each of the seven "Stated." a text of
the commit says what is kept: the record (VO-9, lines 9029–9033; VE-14, VR-16 and VT2-6, lines 9243–9244; VB-31,
lines 9457–9458), S3 Text §5 (VS-12, line 260) and the row's note (VB-22, row 1338). The record's paragraph on the
audits (lines 9443–9454) gives the same counts.

**3. The dispositions of VR-1 to VR-17, VT1-1 to VT1-10 and VT2-1 to VT2-17 (item 2).** Each was read with its
finding in the report. All 44 describe their finding fairly. The quoted text is at the place named in each, with the
remarks of W5-1, W5-11 and W5-13. Each correction answers its finding, the count of VR-9 (b) apart (W5-2); in
particular:
- VR-1, VT1-1, VT2-4: record line 9292, "(4.263: 4.139 to 4.535)", the values of `derived_r24.out` line 69 and of S3
  Text line 260, and of the recomputation above.
- VR-2: rows 770 and 771 of the numbers table; the residual table of S3 Text §6 holds −0.01243 and −0.01540 (lines
  328, 327); the head note counts the two notes. VR-3: S3 Text lines 231, 264 and 395, and §8's citation (line 531).
  VR-4: record lines 9475–9478; R48. VR-5: CLAUDE.md lines 457–458. VR-6, VT1-5: row 563's note. VR-7, VT1-6: S4
  Text line 76; S5 Text §4 (line 25) does list the files with no header, with `-dirty` and with `nogit`. VR-8:
  `numbers_update.out` (277 + 62 + 3 + 19 + 86 = 447). VR-9: the file's counts of the citation years, the dates, the
  heads and the DOI; line 360 (the "1" of Results 7, to Table 4's caption); lines 327–331 (the four limits, S3 Text
  §5); record line 9386. VR-10, VT1-3: R19 and the record's disposition of A's m8. VR-11, VT2-3: R22. VR-12:
  supplementary.md line 1682. VR-13: line 1689; B27's pre-run entry does record the part (record lines 8643–8644).
  VR-14: S20 Table's head note (line 1711) and S3 Text line 556. VR-15: S5 Text line 25; the heartbeat's last line is
  of 00:32:10 and the last step, begun at 00:01:08 with 2,040 s, ends at 00:35:08, 178 s later
  (`b27/b27_heartbeat.log`, `b27_unit.log`). VR-16, VT2-6: record lines 9243–9244; T61 (iii). VR-17: line 248.
- VT1-2: record lines 9479–9482; the script's revision note (lines 21 and 26). VT1-4: T03's last sentence and the two
  dispositions of the record. VT1-7: S19 Table's head note (line 1601) names both sets and where the main text has
  them. VT1-8: S4 Text line 53. VT1-9: S3 Text lines 321 and 337. VT1-10: supplementary.md line 3; the heading of
  Results 6 is the committed one, and the quoted sentence is the section's second (draft line 152).
- VT2-1: S5 Text lines 33 and 37. VT2-2: README.md line 73; CLAUDE.md lines 591–592 have the same words. VT2-5:
  draft lines 124 and 110. VT2-7: S3 Text line 505 and supplementary.md line 309, the only two places of the levels
  0.2766 and 0.2438. VT2-8: lines 1621, 1637 and 1687. VT2-9: record lines 9490–9493; each of the eight dispositions
  it names assigns an item, and that of C's m4 names the note. VT2-11: record lines 9294–9295; supplementary.md line
  1623. VT2-12: record lines 9312–9314; draft line 257. VT2-13: claim record lines 87–91. VT2-14: the head note's
  last sentence. VT2-15: S3 Text line 266. VT2-16: S3 Text line 395; supplementary.md line 1590. VT2-17: line 1706.
- "As <id>": the disposition named covers the finding in each case (VR-1, VT1-1 → VT2-4; VR-3 → VO-4; VR-4 → VE-5;
  VR-6 → VT1-5; VR-7 → VT1-6; VR-8 → VE-3; VR-9 → VB-2, VB-7, VB-8; VR-10 → VT1-3; VR-11 → VT2-3; VR-12 → VS-11;
  VR-15 → VO-5; VR-16 → VT2-6). "Found also by": so in each case (VR-5/VB-28; VT1-2/VE-21; VT1-3/VR-10; VT1-5/VR-6;
  VT1-6/VR-7; VT1-8/VS-6; VT2-3/VR-11; VT2-4/VT1-1, VE-1, VR-1; VT2-6/VE-14, VR-16; VT2-9/VE-9; VT2-11/VE-12).

**4. Every quotation of the last part (item 3).** The part after "Corrected.", "Stated." or "Kept." of the 157
paragraphs holds 153 quotations (VW/W5/quotes.py, quotes_last.txt). Every one occurs word for word, elisions allowed
for, in a file of the list at HEAD: none could not be found. Each was then read at the place its disposition names:
the record (lines 8875–9500), the main text, S1, S3, S4 and S5 Text, the supplementary tables, the numbers table and
its head note, `numbers_update.out`, the claim record, the two search files, CLAUDE.md, README.md, the folder's
README, the `why` of the replacements and the first three parts. The places hold, with two remarks: VT2-10's phrase
is not in CLAUDE.md (W5-1), and VS-11's is in S3 Text §5 with code marks (W5-11). Phrases that a disposition gives as
earlier or dropped text are where it says: "a scope map" (README.md at 8bd189e), "In the literature" (the `why` of
R301), "no statement removed" (five reasons still say it: I02, R105, R106, R601, M03; those of D01, D04, M07 and R401
now name what is not repeated), "B21 (b) and (c); the reproductions in B23" (S19 Table's head note at 8bd189e).

**5. The reports as committed (item 4).** Each of the ten files equals the session's returned report (the first
verification's `reports/` folder) once the working directory's path is written `$SP`; check_VC.md and check_VT1.md
lack the returned file's last line and the blank line before it, a line of the kind the dispositions say, and nothing
else differs. No path beginning with a temporary or home directory, no drive letter and no "~/" remains; the
directory names outside the tree are `$SP/…` (VB, VC, VE, VR, VS), `VW/…` (VC, VE, VM, VN, VO, VT1, VT2) and two
relative ones in check_VN.md (`b35/newpdf/`, line 71; `b35/finaltest/Downloads/new_papers/`, line 146). The findings
of each file are numbered from 1 without a gap, and each states its grade.

**6. Cross-references (item 5).** The 157 ids of the reports have one paragraph each in the last part, in the
reports' order, none twice and none besides. 26 dispositions say "As …" (29 references) and 17 say "Found also by …"
(24 references); every id named exists and its finding is about the same thing; VE-4's three (VR-9, VB-8, VB-24) and
VM-10's two (VB-20, VB-23) each cover a part. "Found also by" is not given in every disposition that another points
to (VB-2, VB-7 and VB-8 for VR-9; VB-20 and VB-23 for VM-10; VE-13 for VB-10; VO-1 and VO-5 name VS-7 and VR-15 in
parentheses), and the file does not say that it is. The mentions in parentheses (VS-7, VR-15, VS-4, VT2-7, VB-30,
VB-6, VB-7, VB-21 to VB-23, VR-2, VT2-14, VE-4, VE-22, VT1-7; C28, C30, C31) name the finding or disposition meant.

**7. Recomputations made on the way** (committed result files only). From `baseline_gap.csv` (VW/W5/recompute.py):
SDs 0.0887, 0.0485 and 0.0524, r = −0.888, r² = 0.79 and the parts 0.30, 0.35, 0.35 of the DiD's variance (VM-3);
r(sts DiD, r₁ DiD) = +0.953, +0.921, +0.931, +0.846 (VO-13); the residual's slope −0.7533 with its intercept +0.0005,
and the values of subjects 14 and 8 (VO-6). Copies of `wc.py` and `abstract_summary.py` run on the main text: 8,498
and 8,371 words, the output equal to `wc_revision.out`, 29 heading lines; Abstract 300 and Author summary 200 words.
S19 Table's Part A: 81 rows, 36 met, 15 partly met, 16 missed, 14 others, the ten rows of B23 each with a verdict
("Found while the findings were settled"). 1,198 − 264 + 447 = 1,381 rows; the 37 committed rows corrected after the
checks (13 + 5 + 9 + 1 + 5 + 1 + 1 + 2): the thirteen on line 4 of `family_atoms_tables.md`, the five of Table 2's
caption (rows 405–409), the row of "BIC over 1–5" (1333), the row of rsHRF (1338), the bound row of 6.7e-16 (1272)
and the two notes of rows 770 and 771 were read.

**Not verifiable from the tree:** what the dispositions say of the build and of the planning session's own checks
(R09, VT2-14, VE-20, VB-20), of the regeneration of the figures (R49, VE-22), of what was asked of V.S. (VN-5), and
the pages of the cited works, which were compared with the claim record and with check_VN.md and check_VC.md only.
