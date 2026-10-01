# Audit of the correction of Table 3's caption (1 October 2026): findings

*By a separate session of the AI system, read-only, on the prepared revision (a simulated commit on e9a6128 that applies
the replacements as they then stood: 12 entries; the dispositions say what was done with each finding, and the
replacements committed are the 15 of `../revision/text_replacements_2026-10-01.json`). Line numbers are those of the
build audited. Copy for the repository: the paths of the auditing session's scratch files are left out.*

What checks out (not listed below): the correction itself; the revision reproduced byte for byte by applying the JSON
to e9a6128 (all 12 old strings occur exactly once; the six sha256 equal apply.out's); check_numbers.py on the revised
tree identical to checks/check_numbers.out (rows 1197, flagged 12, the same twelve sign rows as in the checks of 25, 26,
28 and 30 September); check_cells "flagged 0"; tablecheck 0; wc.py 6998/6878 on the revised tree and at e9a6128 (the
text of df5c160); the record's diff 26 additions, 0 deletions, at the end, the heading in the established form; the new
lines of the record and of CLAUDE.md at most 120 characters (the CLAUDE.md heading and the state paragraph were already
single long lines); the −2.76 row's context exactly 60 + the number + 40 characters of the new caption and the only
context overlapping the changed span; S5 Text §6's commits right (df5c160 = Round 22 (1 of 2), 1 Oct; e9a6128 = Round 22
(2 of 2), the figures regenerated at df5c160, the PNG files identical there) and the sentence reads correctly; README's
`notes/` row and Data and code availability name the folder; CLAUDE.md's edits consistent (1,197 rows, 6,998 words, the
map's alignment); finding 8 of `notes/review_2026-09-30/audit/findings_T.md` (l. 92–99) and `dispositions.md` item 8 (l.
37) are indeed what led to "(the last two over the residual's pairs)" (B12 of the JSON of 30 September, "B26 rule (ii)";
record l. 8287); no other file says "the last two" or needs the correction (S13 Table's note l. 339, S3 Text §6 l. 243,
Fig 3's captions and captions_v2.md cite the rates without saying which pairs; the dispositions and record of 30
September are historical).

Verification of the correction: the three −0.39 rows (`main_text_numbers.csv` l. 555, 691, 749) cite
`diagnostic_alternatives_tables.md` l. 108, row (i), −0.387, the last column of (b), whose note (l. 102;
`supplementary.md` l. 1415) says it "divides the residual's change by r₁'s over the residual's pairs";
`partB23_diagnostic_alternatives.py` l. 469–471 computes both the residual's change and r₁'s over the pairs whose
residual exists in both conditions, that is, whose substituted (AR(1)) matrices are positive definite in all 14 windows
(the per-pair residual is the 14-window mean; row (i) leaves out 11 → 2,989). −0.18 = +0.00279 / −0.01540 (B24, no
matrix left out) and −0.37 = +0.0054 / −0.0146 (the null at W = 60, none left out) are ratios of displayed values, as
S13 Table's note (l. 339) gives them. So "the AR(1) rate and the last two over the residual's pairs" is exact;
+0.0049 / −0.01243 = −0.3942 → −0.394, so the row-4 remark is arithmetically right.

## Findings

1. **inaccuracy (bookkeeping)** — `manuscript/main_text_numbers.csv`: the caption's new "AR(1)" has no label row. Head
   note (l. 1): "one row per occurrence"; the caption's other five "AR(1)"/"VAR(1)" each have a label row for their "1"
   (l. 706, 721, 727, 737, 750; Fig 3's caption likewise, l. 554, 556), and earlier revisions added rows for new label
   occurrences (head note: "added three label rows", "added 22 rows"). The new sentence "recomputed the context of the
   one row its edit reached" is true but the table is now one occurrence short; the record's "No number changes" stays
   true (a label, not a quantity). Fix: insert after l. 753 a label row for the "1" of that "AR(1)" (the seventh
   occurrence of 1 in the caption, context 60 characters before and 40 after), extend the head note's sentence ("… and
   added the label row of the AR(1) it names"), and change "(1,197 rows)" to 1,198 in CLAUDE.md l. 19 (the round 22
   bullet's 1,197 at l. 398 is historical); optionally say so in the record entry. (Pre-existing, not this revision's:
   "no AR(1) pair" in Data and code availability, draft_v2.md l. 246, also has no row.)

2. **inaccuracy (incomplete description)** — the review folder's README.md l. 18–21: "the figure check … (`figures.out`):
   the captions file differs from the committed one in its header alone." figures.out also reports "fig4_v2_regional.png:
   DIFFERS in 70 pixels, the largest channel difference 1 of 255" (l. 7) and ends "conditions NOT met: send this output to
   the planning session" (l. 14); its own header (l. 1) explains the anti-aliasing and that the PNGs are to be identical
   on V.S.'s machine. The README of 30 September described figures.out neutrally. Fix: describe the PDFs, the five
   identical PNGs, Fig 4's 70 pixels and the verdict line, and that on V.S.'s machine the PNGs are to be identical. Note
   also: figures_check.py's conditions (l. 9–10, 36–39) still admit a Fig 5 caption difference; this round's condition is
   the header alone, so the committer must read the caption lines of figures.out, not only its verdict.

3. **wording (ambiguity)** — the review folder's README.md l. 5–6: "as the writer's session of the revision of 1 October
   2026 remarked in its report". Both the revision committed as df5c160 (1 Oct) and this correction (the README's own
   title: "…, 1 October 2026") are revisions of 1 October 2026. Fix: "the writer's session of the revision committed as
   df5c160".

4. **wording** — `manuscript/analysis_record.md` l. 8471–8472: "The writer's session of round 22 remarked it in the
   report it gave with its bundle, as a remark and not an error, after its commit." (a) "round 22" is a process label;
   the record's entries since 26 Sep describe revisions by date and content, and S5 Text §5 keys only "writer's
   session"/"planning session" (CLAUDE.md l. 19: "the manuscript files carry no process label (round, stage or session
   names), dated descriptions replacing them"). (b) "with its bundle … after its commit" is ambiguous: a report given
   with the bundle precedes the commit. The repository holds no report, so the statement cannot be checked; it does not
   contradict anything in the repository. Fix: "The writer's session of the revision committed as df5c160 noted it in
   the report it gave with that revision's files, as a remark and not an error; the revision was committed as it
   stood."

5. **wording** — `manuscript/analysis_record.md` l. 8476–8477: "No number changes: at its printed precision the AR(1)
   rate also follows from Table 3's row 4, +0.0049 / −0.01243 = −0.394." The colon makes the row-4 ratio the reason no
   number changes; it is not (the correction is wording only), and row 4's columns come from other simulations that
   only happen to round to the same −0.39; the rate's source remains S18 (b) (i). Fix: "No number changes (at its
   printed precision the rate is also what Table 3's own row 4 gives, +0.0049 / −0.01243 = −0.394)."

6. **wording (omission)** — `manuscript/si/S5_Text.md` l. 27 (§5) ends with the audits of the revision of 30 September
   and does not mention the correction of 1 October 2026 or its audit, although Data and code availability
   (draft_v2.md l. 246) now lists `notes/review_2026-10-01/` among the folders of "the adversarial reviews and the
   citation audits" and §5 is where "each review is named by its date" (the revision of 26 Sep added its read there:
   record l. 7585). README.md's state paragraph (l. 31–37) likewise lists every text revision through 29–30 Sep and not
   this one, while CLAUDE.md's state paragraph (l. 19) does. Fix: one sentence in §5 and "and, on 1 Oct 2026, in Table
   3's caption" in README.md's paragraph — or leave both if deliberately limited to checks of the text.

7. **wording (incomplete)** — `manuscript/si/S5_Text.md` l. 31: "df5c160 (1 Oct, B26's outcome entry, the entry on the
   claim-by-claim check of 29–30 September 2026 and the text that reports them)" carries over the old clause; df5c160
   also holds the entries on B25's re-run, on Fig 5's caption/B3's header/run_all.sh (with the figure-script and
   run_all.sh changes) and on the audits, and the review folder (`git show df5c160 --stat`), where comparable items
   (820cacd, 13705b9) list such contents. Fix: append ", with the entries on B25's re-run, on Fig 5's caption and on the
   audits, and the review folder of 30 September".

8. **wording** — record l. 8462 and CLAUDE.md l. 406–407 say "the replacement" (singular) while the JSON holds 12 and
   the review folder's README.md l. 10 says "the 12 verbatim replacements". Fix: "the replacements".

**Verdict:** the correction is right and exact and the revision applies cleanly with every check reproduced; the
findings are one bookkeeping inaccuracy (the missing label row for the new "AR(1)"), one incomplete description
(figures.out in the review folder's README) and wording points — none changes a number, a verdict or the word count.
