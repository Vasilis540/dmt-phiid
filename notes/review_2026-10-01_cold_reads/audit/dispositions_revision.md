# What was done about each finding of the three audits of the revision of 1–2 October 2026, and of the four checks of the corrections

The revision that answers the cold reads of 1 October 2026 was audited, as first prepared, by three separate sessions
on 2 October 2026, each on a clone at 8bd189e with the replacements of that preparation applied: one audited the text
(`findings_text.md`, T01–T63), one the record's entries, the rules for the text and the bookkeeping
(`findings_record.md`, R01–R57), one the citations against V.S.'s copies of the cited works (`findings_citations.md`,
C01–C32, with `te_filter_check.py`, the population check its first finding rests on). The report on the citations is
in its second form: the first, of 25 findings, listed as not checked the statements about eight works whose PDFs its
session did not have; V.S. sent them, and the session returned the report with those statements checked and seven
findings added (C26–C32), its first 25 word for word as before. The three files are the reports as the sessions
returned them. This file, written by the planning session, says what was done about each of the 152 findings and, in
its last four parts, about each finding of the sessions that then checked the corrections, ten, then seven, then four
and then four more. The places it names are those of the revision as committed, which is the revision after these
findings; the line numbers in the reports are those of the first preparation, which was not committed.

Each finding was read against the source it cites before anything was changed. 147 were corrected: the text, table,
caption, entry or file was changed as the finding says. 2 describe something that is kept as it is, and the text now
says what it is. 3 concern the audits' own instructions and no file of the commit. No finding was set aside. Where two
or three reports found the same thing, the disposition is written once and the others point to it. Two of the seven
findings of the report's second form (C26, C29) were of things already corrected for findings of the other audits,
since the session audited the first preparation throughout.

The text audit rested three of its findings (T07, T10 and T25) on the released series, which it fetched outside its
clone. The values it computed there are quoted in its report and used nowhere in the paper, which keeps the printed
values of the committed files; S5 Text §4 records the occasion, and the main text's Use of AI tools statement points
there.

## The record and the outcome entries (`findings_record.md`)

### R01 — blocking (also T54, C24)
Finding: A placeholder for the audits' outcome stood in S5 Text §5.
Corrected. S5 Text §5 now states the audits in its place: three audits, of the text, of the record's entries and of
the citations, the number of their findings, where each finding's disposition is (this file), and that further
sessions checked the corrections. The planning session's packaging of the commit stops if the placeholder's marker
remains in any changed or new file other than the audit reports, which quote it.

### R02 — should fix (also T02)
Finding: Results 2 read the intensity-tracking criterion's sign the wrong way round ("met in sign").
Corrected. Results 2, last sentence: the criterion "passed its threshold of |ρ| ≥ 0.80 (Spearman ρ = −0.98) with the
sign opposite to that pre-specified, and was void under its controls (S1 Text; S2 Table)". The record's disposition of
C's m18 says the same.

### R03 — should fix (also T24)
Finding: The ramp's differences from the step (0.0002 and 0.0007) were differences of the table's rounded cells.
Corrected. Results 4 and S3 Text §6 give the differences of the means over the replicates, 0.0001 and 0.0006 nats
(+0.002182 against +0.002034; +0.004851 against +0.004232), which `checks/derived_r24.py` now computes from
`matched_slope.csv` (item 5 of its output). "B28, outcome" (c) gives the four means, the two differences and, beside
them, the differences of the table's rounded cells; S19 Table's row of B28 (c) and the numbers table's two rows
follow.

### R04 — should fix (also T11)
Finding: Fig 5's caption, title and script comment had the scale of panel (c) the wrong way round.
Corrected. The caption (figure script and main text): "drawn at a quarter of the nats per unit height of (a) and (b),
that is, magnified four times (y-range −0.02 to +0.03 nats)". The panel's title: "(magnified: a quarter of the nats
per unit height of a and b)". The script's comment and its revision note say the same, and so does the record's
disposition of C's m9.

### R05 — should fix (also T09)
Finding: S3 Text §5 said that the adjusted contrast lies between the DiD and the post-injection gap.
Corrected. S3 Text §5: the three readings "agree in sign on both variants and at both window lengths, and in every row
of sts, of r₁ and of the AR(1)-substituted sts the adjusted contrast is the smallest of the three in size".

### R06 — should fix (also T04)
Finding: The committed sentence on the refutation was removed from Results 2, and B's MINOR 6 was half answered.
Corrected. Results 2: "It was planned as a test of an increase: the increase failed whatever the two-sided p, and
under the directional-failure rule the significant decrease refutes the hypothesis as operationalised." S1 Text's
pointer to Results 2 holds again, as do CLAUDE.md's and README.md's statements. The record's disposition of B's MINOR
6 and the reason recorded with the replacement (R201) say what the text has.

### R07 — should fix (also T17 (i))
Finding: Data and code availability said that every result table names its commit, without the exceptions.
Corrected. Data and code availability: "the result tables and reports name the producing commit in their headers
(`git=<SHA>`, with `-dirty` where the tree had uncommitted changes and `nogit` for a file written outside a commit; S5
Text §4 lists the files of those two kinds and those that carry no header)".

### R08 — should fix (also T16)
Finding: S3 Text named the reviewers by letter and S5 Text §4 a session, against the record's sentence on process
labels.
Corrected. The four passages of S3 Text name the reviewers by role and point to S5 Text §5 ("The statistical
reviewer's cold read of 1 October 2026 (S5 Text §5) asked for these readings", and the like for the
psychedelic-neuroimaging reviewer and, twice, for the methods and statistical reviewers). S5 Text §4 says "started by
`b27_start.sh`". The record's "The checks" states what holds: no round, stage or bundle name and no reviewer's letter
in the main text and the supporting information, and the sessions named only in S5 Text §5. The planning session's
packaging now tests for the letters and for session names outside §5, which the audit prompt's pattern did not match.

### R09 — should fix (also T46 (ii), (iii))
Finding: Two rows of the numbers table counted nothing and two numbers had lost their rows.
Corrected. The update of the numbers table was redone, and `checks/numbers_update.out` describes it. A row sits on one
number token of the text and is carried from the committed text only where the token at its place is the row's number,
so that a row cannot land on another number's token. The row of the unsigned 0.0112 and the row "20" of the removed
date are deleted; the second 0.05 of Methods (Inference) and the second 1 of Methods (Remedies) have their rows. Every
number token of the covered text has a row, apart from the kinds the head note names (citation years, cross-references
by number, the numbers of the captions' own heads and of the headings, dates, commit identifiers, the Zenodo DOI, code
spans). `numbers_update.out` lists every deleted row with its class and, for a number that is now elsewhere or is no
longer stated, where it is or what became of it, and every row carried to a rewritten sentence otherwise than by the
alignment of the two texts. The planning session checked the result with two checks written apart from the builder
(placement and coverage; each locator's line), which are not part of the commit.

### R10 — should fix (also T21, C03, C12)
Finding: The exclusion of six participants was cited to Timmermann et al. (2023), whose count is four and three more.
Corrected. Methods (Dataset): the replacement of volumes is cited to both works and the Reporting Summary; "six of the
twenty participants were excluded for more than 20 % of such volumes (Singleton et al., 2025)". S1 Text and S4 Text D4
give both counts: Singleton et al.'s six, and Timmermann et al.'s four discarded over the 8 min after the injection
with three more removed, over the 28 min, for their dynamic analysis. The claim record's pointer names those places.
"B29, outcome", item (i), says whose count the six is.

### R11 — should fix (also T15, C06)
Finding: S3 Text §10 said that PubMed's reading of the string is kept, and misplaced the search's files.
Corrected. S3 Text §10: "its 11 records and their screening are in `notes/review_2026-10-01_cold_reads/pubmed_search/`
(`pubmed_search.csv`, `screening.md`; PubMed's own reading of the string, its Search details, was not kept)".

### R12 — should fix (also T29 (iv), C29)
Finding: The Abstract's first sentence made MMI underlie all the reports found.
Corrected. Abstract: "underlies most fMRI synergy reports we found". The record's disposition of C's m7 names the
Abstract with the Introduction, the Discussion and Methods.

### R13 — should fix (also T44, C25 (b))
Finding: The disposition of C's m19 gave 300 words where the check gave 299; CLAUDE.md had 300.
Corrected. The Abstract of the revision as committed has 300 words (`checks/abstract_summary_revision.out`). The
disposition of C's m19 now takes the count from the check's output, as "The checks" does, so the two cannot differ;
CLAUDE.md's count holds.

### R14 — minor (also T08)
Finding: S3 Text §8 gave +0.45 for the correlation +0.44487.
Corrected. S3 Text §8: "+0.445 and +0.333, against +0.495 at p ≤ 5 and +0.899 at p = 1", with their Fisher-z
intervals.

### R15 — minor
Finding: The Abstract and the Discussion gave the detectable difference as 0.016, a second rounding; a row's note said
12 df.
Corrected. The Abstract and the Discussion give 0.0155, as Results 4 and S3 Text §5 do. The numbers table's rows are
data rows on the line of `baseline_gap_tables.md` that holds 0.0155, with the note "the one-sample t test (13 df)".

### R16 — minor (also T07)
Finding: Results 3 gave 2.65 for the per-subject slope the source prints as +2.6450.
Corrected. Results 3: "2.645 per subject", the source's value at three decimals, which needs no decision of the tie;
the record's disposition of A's m9 has the same. The value the text audit computed from the released series (2.644997)
is not used (S5 Text §4).

### R17 — minor
Finding: "B16c, outcome" described 264 rows as those of four quantities, which make 192.
Corrected. "B16c, outcome", "The outputs": "264 inference rows, 44 labels in six sets: the 192 rows of MMI-sts,
CCS-sts, xtx + yty and the autocorrelation in the eight cells, and the 72 rows of the diagnostic's observed, predicted
and residual sts in the four W = 60 cells".

### R18 — minor (also T36)
Finding: S5 Text §4 said that every output of the run carries the commit; twelve of the 29 do.
Corrected. S5 Text §4: "the twelve text outputs (four tables, four CSV files and four logs) carrying `git=13e7299`,
the sixteen arrays and the pickle carrying no header". "B27, outcome" says the same.

### R19 — minor (also T13, C25 (a))
Finding: "Scope map" was said to be retired but stayed in the list of supporting information and elsewhere, and "the
map" had lost its referent in the main text.
Corrected. The main text names the surface where it spoke of the map: "the sts surface of Fig 1a" in the Discussion
("the reported effect on the sts surface of Fig 1a"; "what that surface predicts") and in the entry of S20 Table in
the list of supporting information, and "the sts surface over (r₁, q)" in the entry of S3 Text. S3 Text §4 begins by
saying what the map is and that the plans called it the scope map; S5 Text §1 gives "scope map" as one of the plans'
own names; README.md's account of the paper has "the surface of `sts` over (r₁, q)" where it had "a scope map"; the
one note of the numbers table that had the term is reworded. The record's disposition of A's m8 says where the term
stays: as the plans' name and in file names.

### R20 — minor (also T42)
Finding: The Recommendations did not name "no band-pass" or say that the remedy cannot be tested here, as the rule and
the dispositions said.
Corrected. Recommendations: "whiten before band-pass filtering or do not band-pass, a remedy the released derivatives
cannot test, and report the in-band power share beside any prewhitened atom". "B16c, outcome", item (ii), and the
dispositions of A's m4 and B's MINOR 4 name both places.

### R21 — minor (also T20)
Finding: The disposition of A's w4 described a clause the Abstract did not have.
Corrected. Abstract: "(4.7 to 1 per within-window standard deviation; neither is lagged coupling, which can move it
either way)". The disposition quotes it.

### R22 — minor (also T47)
Finding: Methods stated no assumption of the Fieller interval, and the sts slope had no leave-one-out.
Corrected. Methods (Inference): "ratios of group means Fieller intervals, which assume the two means jointly normal".
The leave-one-out of the slope of the sts DiD on the r₁ DiD (4.263 with all 14; 4.139 to 4.535) is in S3 Text §5, from
`derived_r24.out`, item 8. "B27, outcome" states the assumptions in its item (v) and the leave-one-out in its
paragraph on the sts rows, and the disposition of B's MINOR 9 has both.

### R23 — minor (also T27)
Finding: Fig 4's caption kept "pre-defined", which Results 3 had replaced.
Corrected. Fig 4's caption: "(b) The contrast between sensory cortex ... and association cortex ..., fixed before the
partialled map was computed (Results 3)"; its last sentence has no "pre-defined". The caption is among those the entry
lists as changing (Figs 1, 3, 4, 5 and 6); the disposition of B's W3 names it.

### R24 — minor (also T48)
Finding: Methods and S4 Text P8 did not name the subject and the window of the non-finite TR.
Corrected. Methods (Dataset): "one non-finite TR, the last of subject 3's placebo run, at the end of window 14 (on
ts_gsr the only one; S3 Text §5)"; S4 Text P8 has the same.

### R25 — minor (also T45, C31)
Finding: The disposition of C's M5 (b) counted eight observations; C lists seven, and in two rows the counts stay.
Corrected. The disposition: "the seven observations C lists are removed from S20 Table and the literature file; in
rows 2 and 3 the remark is removed and the two counts stay as the papers give them". Row 5's two cells on HRF
deconvolution say what was read, the article with its Extended Data and its Reporting Summary, and that the
Supplementary Methods were not (the answer to C's M4, which the reason recorded with that replacement now names).

### R26 — minor
Finding: "B27, outcome" said the scrutiny was applied "in the same words"; one word differs.
Corrected. Item (ii) of the entry says that the words are other than S2 Text's, and why: S2 Text speaks of "a
pre-injection baseline gap in the direction that creates it"; for sts, whose post-injection gap is itself negative in
every subject, Results 2 says that the runs' pre-injection gap "lies in the direction that enlarges the DiD".

### R27 — minor
Finding: Table 3 gave the counts of intervals that contain zero, not those that contain the three rates.
Corrected. Table 3's rows 2 and 3: "of 14 intervals, 0 contain zero; 0, 11 and 11 contain −0.18, −0.39 and −0.37" and
"of 91 intervals, 1 contains zero; 13, 71 and 63 contain −0.18, −0.39 and −0.37"; the caption says what they count.
Item (iv) of "B27, outcome" describes the rows.

### R28 — minor
Finding: Limitations gave the correlations on one variant and read the missed prediction as "motion's own mark".
Corrected. Limitations gives the count DiD's correlation with the r₁ DiD and the within-run correlation on both
variants (−0.107 and +0.037; −0.124 and −0.025) and says of the prediction what happened to it: "(the positive
within-run relation it predicts was not found)". The reading is gone; S3 Text §5 says that the tables do not say what
produces the negative sign. Item (ii) of "B29, outcome" says which correlations Limitations states and which are in S3
Text §5, as a departure from the rule.

### R29 — minor (also T49)
Finding: Results 7 and S3 Text §8 said the contrast "tracks" the whitened r₁ at correlations whose intervals include
zero.
Corrected. Results 7 gives the correlations as values (+0.495 at p ≤ 5; +0.333 at p = 20) and says that "the Fisher-z
interval of neither correlation excludes zero". S3 Text §8 gives the four intervals (`derived_r24.out`, item 6) and
says that over the eight cells at p = 10 and 20 the interval includes zero in seven. Item (iii) of "B16c, outcome"
says the same.

### R30 — minor (also T05)
Finding: Table 2's caption called the r₁ rows the last three.
Corrected. Table 2's caption: "The three rows marked r₁ give the two gaps and the baseline-adjusted contrast of
whole-brain lag-1 autocorrelation r₁ (dimensionless), whose DiD is in the text."

### R31 — minor (also T10)
Finding: Table 3's caption gave one regressor for the data and the generators.
Corrected. Table 3's caption: the slope is "of the residual DiD on the r₁ DiD: for the data the whole-brain r₁ DiD,
for the generators the simulated pairs' pair r₁ DiD (in the data's group means the two DiDs are −0.0146 and −0.0155)".
Results 4 points to the caption for the regressors and no longer calls the comparison like-for-like; Fig 3's caption
says "per unit of the simulated pairs' pair r₁ DiD". "B28, outcome" and the disposition of B's MAJOR 3 say the same.
The data's slope on its own pair r₁ DiD, which the text audit computed from the released series, is not quoted (S5
Text §4).

### R32 — minor
Finding: "The length and the tables" listed as moved two statements that also remain in the main text.
Corrected. The paragraph is rewritten in four lists: the statements now in the supporting information or in a table,
each pointed to from the main text (Barrett's reduction is given as kept in a clause of Limitations, the costs of
prewhitening as pointed to with their three citations); what was written for this revision and placed in the
supporting information; the sentences retired by a rule or a finding; and the two retired for length, which a later
correction divided from the third list (VE-8). CLAUDE.md no longer counts eight statements.

### R33 — minor (also T38)
Finding: S5 Text §1 said that Methods names the deviations; it gives their number and two of them.
Corrected. S5 Text §1's heading: "(moved from the main text's Methods in the revision of 1–2 October 2026; Methods now
gives their number and names the first and the last)".

### R34 — minor (also T43)
Finding: S1 Text said that the record's entry on the codes states the question put to the data authors.
Corrected. S1 Text points to the record's entry "Git history and the participant codes" of 15 September 2026, "which
states what the repository's history holds and why it is not rewritten". The disposition of C's M1 says where the
question is.

### R35 — minor
Finding: S19 Table's sentence counted among the parts without a prediction three that had one.
Corrected. S19 Table, after Part A: B27, B28, B29 and B16c "recorded none for one of their parts (the residual's
correlations with the r₁ gaps, noted in row B27 (d), and rows B28 (d), B29 (c) and B16c (e)); three further rows are
readings by the same criteria or checks that their entries say are not counted (B27 (d), B29 (d) and B16c (a))".

### R36 — minor (also T32)
Finding: S3 Text's head note gave the labels as B1–B26.
Corrected. S3 Text's head note: "(B1–B29, B16b, B16c, B17b)".

### R37 — minor (also T52, C05)
Finding: Rosas et al. (2020) was in the reference list without a citation in the main text.
Corrected. Results 6 cites it where it names the emergence capacity: "the binarised CCS emergence capacity (Rosas et
al., 2020) of Luppi et al. (2023)". The claim record's pointer says so.

### R38 — minor (also C22, T56)
Finding: S20 Table's rows 5 and 10 carried requests to S.P.S. and to V.S.
Corrected. The two cells, and those of the literature file, carry no request: row 5's says what was read and that the
Supplementary Methods the study defers to were not, and row 10's that the Supplementary Materials were not obtained.
Obtaining both is an item of the note to C.T. and S.P.S., whose items the record's entry lists.

### R39 — minor (also T46 (i))
Finding: Label rows were deleted or missing against the table's own practice; the head note counted three tables; the
classes could not be recounted.
Corrected. With R09. (1), (2): the update gives a label row to every such token (section signs, formula indices such
as {t+1}, "Rows 2–6", 2S, n − 2), by one convention for the committed and the new sentences. (3): the head note counts
four tables. (4): `numbers_update.out` names no script outside the repository and lists the rows from which its counts
can be recounted.

### R40 — minor (also T41)
Finding: The respiratory and haemodynamic candidates for the fall of r₁ had left the paper.
Corrected. Limitations: "Why r₁ fell (neural, haemodynamic, cardiac, respiratory or motion effects) is not identified
(Discussion)." The disposition of C's M3 says that the respiratory candidate is named without a citation.

### R41 — minor
Finding: CLAUDE.md's bullet on the subject codes still said that the Ethics statement states the facts.
Corrected. The bullet says that since this revision the Ethics statement no longer describes the codes, that whether
the letters identify anyone is a question for the data authors, and that whether the public history is then rewritten
is V.S.'s decision, to be recorded when made.

### R42 — minor
Finding: The folder's README described `screening.md` as it was before the revision.
Corrected. The bullet: "the two that were marked to assess read in full on 1 October 2026 (the file as the revision
that answers the reads left it)".

### R43 — minor
Finding: Eight added statements dated the revision's moves to 1 October 2026.
Corrected. They read "the revision of 1–2 October 2026" (S3 Text §2, §6, §8 and §9; S5 Text §1 and §4; S20 Table's
head note), and in CLAUDE.md "the revision of 1–2 Oct 2026".

### R44 — note (also T53, and the setup paragraph of the citations report)
Finding: The audit prompt's step 4 could not print the line it named.
The audit's instructions. The prompt piped the script's output to `tail -1`, and the script lists the files it wrote
after its summary line. The three sessions went on, rightly: the application was complete and its output equal to
`checks/apply_revision.out`. The writer's prompt for the commit compares the whole output with that file.

### R45 — note
Finding: The prompt's command for the line length counts bytes under mawk.
The audit's instructions. The rule holds in characters (no added line of the record exceeds 120). The planning
session's check counts characters, and the writer's prompt does not use the command.

### R46 — note (also T62 (i))
Finding: `matched_slope.csv` holds an unquoted comma in its first field.
Stated, not changed. The file stays as the run wrote it, being an output of the commit before this one, and the script
that wrote it is not changed in this commit, so that the committed script remains the one that produced the committed
output. "B28, outcome" and S3 Text §6 state the file's form (eleven fields under a header of ten; the first two are
the condition's name), and `derived_r24.py` reads it so.

### R47 — note
Finding: The run's end time is not in the unit's log as such, and the charger's time is that of a heartbeat line.
Corrected. "B27, outcome", "The run": the last step began at 00:01:08 and its log prints 2,040 s, "which puts the end
at 00:35:08 (the unit's log was last written at 00:35:10)". S5 Text §4 gives the same in UTC, and the charger as
"disconnected between its lines of 23:52 and 23:57 local time".

### R48 — note (also T12 (iii))
Finding: `figures_check.py` did not test exactly the conditions that "The figures" stated.
Corrected. The script is rewritten to test them, and the paragraph to state what the script tests. (1)
`captions_v2.md` has the committed file's number of lines and differs in six: the header, which must name the text
commit's short SHA without "-dirty", and the captions of Figs 1, 3, 4, 5 and 6; each of the six captions must hold a
Source sentence and, without it, equal the main text's, and Fig 2's must also be the committed one. (2) The PNG files
of Figs 1, 3 and 5 differ, each within 3 % of the committed width and height; those of Figs 2, 4 and 6 are identical
or have the same size, at most 0.1 % of the pixels different and no channel different by more than 32 of 255. (3) The
PDF files of Figs 1, 3 and 5 differ beyond their dates; those of Figs 2, 4 and 6 are identical once the two date
fields, the cross-reference table and the `startxref` offset are masked.

### R49 — note (also T12 (i))
Finding: The lengthened title of Fig 5c ran past the axes and widened the saved figure.
Corrected. The title is on two lines, the second "(magnified: a quarter of the nats per unit height of a and b)", and
the panel's legend is anchored so that it stays about as far below the taller panel. The planning session regenerated
the figures with the committed and with the revised script in one environment (matplotlib 3.10.9, not the pinned one):
Fig 5's PNG changes by −1.1 % in width and +0.1 % in height, and the sizes of the other five do not change. The
check's 3 % bound on a redrawn figure's size would stop an overrun of the kind found (+20 % in width).

### R50 — note
Finding: The check of the non-finite TR reads ts_gsr only.
Corrected. "B29, outcome" (d): "confirmed on ts_gsr, the variant the script reads for this check". Methods (Dataset):
"(on ts_gsr the only one; S3 Text §5)".

### R51 — note
Finding: Results 2 showed subject 8's count of marked TRs as ordinary and did not give its framewise displacement.
Corrected. Results 2: "24 TRs above the motion threshold, against 23.6 on average, and its framewise-displacement DiD,
+0.0935, is the largest of the fourteen". S3 Text §5 and "B29, outcome" (d) and item (iii) say the same.

### R52 — note (also T40 (ii))
Finding: "Nothing on the placebo run" held for one variant.
Corrected. Discussion: "on the placebo run −0.05, p = 0.22, or −0.09, p = 0.045, without global signal regression". S1
Text gives both.

### R53 — note (also T26)
Finding: The exclusion rule of the disattenuation was worded as the reliability of a half.
Corrected. Results 2: "the 366 in which the split-half reliability of either DiD was not positive left out". Fig 3's
caption: "a ceiling of 0.729 set by the split-half reliabilities of the two DiDs". The disposition of B's MINOR 2 has
the rule in the same words.

### R54 — note (also T63)
Finding: The claim record had no item for Timmermann et al. (2023) on the EEG statement.
Corrected. The claim record has the item (Results, p. 4: decreases of alpha power and increases of signal diversity
under DMT), and its section on Gao et al. (2026) holds the two details of S20 Table's row 10 that it lacked (the
patients' two subgroups; the controls' matching for age, sex and education).

### R55 — note
Finding: Three ids of the replacements file were used twice.
Corrected. Every replacement has its own id; the planning session's preparation of the file, which is outside the
repository, stops on a repeated one.

### R56 — note
Finding: The README named audit files not yet in the tree; CLAUDE.md gave the figures' condition more narrowly than
the record.
Corrected. The commit holds the files the README names (the three reports, `te_filter_check.py`, the reports of the
checks, the report of the reading of S19 Table's Part B and this file). CLAUDE.md's "Remaining work" gives the
conditions as the record does: the PNG files of Figs 2, 4 and 6 identical or differing by anti-aliasing alone, their
PDF files identical once the two date fields, the cross-reference table and the `startxref` offset are masked.

### R57 — note (also T55 (ii))
Finding: The Use of AI tools statement was said to be unchanged; it was reworded.
Corrected. The disposition of C's M2 says that the statement keeps its content in fewer words and what was reworded.
After the audits the statement points to S5 Text §4 for the two occasions on which a session computed on the data, the
second being the text audit's own check of three values on the public release (T07, T10 and T25).

## The text (`findings_text.md`)

### T01 — blocking
Finding: The Discussion joined CCS-sts's rise at the global fit to a correlation of 0.80 that belongs to W = 60.
Corrected. Discussion, "The literature", last sentence: "CCS-sts's rise under DMT (Results 6), whose per-subject
change at W = 60 correlates with the residual's at r = 0.80 (its global-fit change at 0.09; a split-half test left
undetermined whether what they share is signal; S3 Text §6)". The record's disposition of A's m5 gives both
correlations and says at which estimator the rise has p = 0.0002. The numbers table's two rows are on the line of S3
Text §6 that holds +0.799 and +0.094.

### T02 — blocking (also R02)
Corrected. As R02.

### T03 — blocking
Finding: Results 3 said that only the global-fit regional atoms were saved; the windowed ones are committed.
Corrected. The clause is removed. Results 3 gives the relation for the windowed estimator's own regional atoms: "with
the windowed estimator's own regional atoms, on the same windows, r = 0.898 (post hoc; S3 Text §4)" and a slope of
2.30 beside 3.09. S3 Text §4 has a paragraph on it, with the Spearman and cortex-only values and rtr's, which says
that it was computed after this audit pointed to the array, with no prediction recorded and no spin test, and that it
is not a second test of the claim. `derived_r24.py` computes it from committed files (item 7 of its output), where it
also prints, for comparison, the array's whole-brain pre-injection means (Table 2's 1.1554 and 1.1378) and the same
statistics for the global-fit map (the committed +0.863, +0.835 and +3.09). S19 Table's Part B lists it. The
disposition of B's MINOR 3 (a) says that the reason B offered was not so, and that of A's m9 that the windowed atoms
are committed.

### T04 — should fix (also R06)
Corrected. As R06.

### T05 — should fix (also R30)
Corrected. As R30.

### T06 — should fix
Finding: The Abstract gave the interval's upper limit as 0.90; it is 0.894889.
Corrected. Abstract: "cross-half r 0.69 [0.26, 0.89]". `derived_r24.out`, item 6, holds the mean cross-half
correlation and its Fisher-z interval at six decimals (+0.693672 [+0.258078, +0.894889]), and the numbers table's rows
are data rows on that line. Results 2 and Fig 3's caption keep the three-decimal interval.

### T07 — should fix (also R16)
Corrected. As R16.

### T08 — should fix (also R14)
Corrected. As R14.

### T09 — should fix (also R05)
Corrected. As R05.

### T10 — should fix (also R31)
Corrected. As R31.

### T11 — should fix (also R04)
Corrected. As R04.

### T12 — should fix (also R49, R48)
Finding: Fig 5c's title overran the axes; the entry did not name all the script changes; the check did not test the
entry's conditions.
Corrected. (i) As R49. (ii) "The figures" names the height ratios (0.30 : 0.20 : 0.20 for 0.30 : 0.20 : 0.10, which
leaves panels (a) and (b) six-sevenths of their height), the font of the entries of Fig 3c's legend (6.5 pt for 6.8,
its title staying 6.8) and the anchor of Fig 5c's legend. (iii) As R48.

### T13 — should fix (also R19)
Corrected. As R19.

### T14 — should fix
Finding: S1 Text and S4 Text still said that the ratings and the EEG regressor enter no result of the main text.
Corrected. S1 Text: "The intensity ratings supplied with the data enter one statement of the main text, the outcome of
the intensity-tracking criterion (Results 2; below)", and "the main text states the criterion's outcome in one
sentence (Results 2) and uses the ratings for nothing else". S4 Text D6 and D9 say the same of the ratings, and A5
says that the EEG regressor is used in the original pre-specified analysis, "whose result the main text's Discussion
quotes".

### T15 — should fix (also R11)
Corrected. As R11.

### T16 — should fix (also R08)
Corrected. As R08.

### T17 — should fix (also R07)
Finding: Data and code availability dropped the exceptions on the headers and two limits of the sentence on the final
run; some removed details were in no manuscript file.
Corrected. (i) As R07. (ii) The sentence on the final run: "every output it regenerated reproduced its committed
version within the tolerances the record set before the run, apart from the differences the record listed in advance
and from two arrays that no result uses". (iii) S5 Text §4 has a paragraph, "Details that Data and code availability
held until the revision of 1–2 October 2026", with what no other manuscript file held: what the tests and the
continuous-integration workflow compare, the tool's NaN, the figures' file names and when each revision's figures were
written, the rounding of the wall-clock times, and what a matrix that is not positive definite is. The reason recorded
with the replacement says so.

### T18 — should fix
Finding: Methods said that the exploratory p values the text draws on are marked post hoc; several were not, and one
has a recorded prediction.
Corrected. (i) Fig 4's caption: "spin p 0.0009 (below the range predicted for it; S19 Table), and for the unpartialled
map 16.933, spin p 0.0564, two p values that are not comparable (Results 3)". (ii) Results 3 gives the network spin
test as what S19 Table says it is, a recorded prediction whose p fell below its predicted range, and Methods says:
"S19 Table says of each computation whether it had a recorded prediction or was post hoc (the text repeats it for
several)", a sentence that names no computation and no section, since a list in Methods had left some out (the
disposition of B's MINOR 8 in the record lists them). (iii) Results 2 marks the leave-one-out post hoc; Results 6
gives ΦR's p values as values, without a threshold; Results 7 marks the deconvolved contrast post hoc, and S19 Table's
Part B names the HRF deconvolution among the review computations of 14 September 2026, with Results 7 among the places
that quote them.

### T19 — should fix (also C04)
Finding: S20 Table's row 3 kept the "calls ... but writes as" form for Luppi et al. (2024)'s synergy.
Corrected. S20 Table's row 3 and the literature file: "which the study names the persistent synergy (p. 6) and for
which it gives the whole-minus-max formula of its Eq. 5 (p. 20)". The Introduction gives the name and the formula too,
as the four-atom sum of Results 1 (C04), and the claim record has the item.

### T20 — should fix (also R21)
Corrected. As R21.

### T21 — should fix (also R10)
Corrected. As R10.

### T22 — minor
Finding: "Three readings" had two extensions, and the sentence on r₁ supported "agree in sign" with values of opposite
sign.
Corrected. Table 2's caption defines the three readings (the DiD, the post-injection gap and the baseline-adjusted
contrast) and says that the rows marked r₁ give r₁'s two gaps and its adjusted contrast. Results 2: "r₁'s three
readings are negative too (Table 2: the post-injection gap −0.0122, in 13 of 14; the baseline-adjusted contrast
−0.0110), its pre-injection gap +0.0025 (p = 0.4417)".

### T23 — minor
Finding: The simulated step was said to be "at the injection"; it is at sample 300, the start of window 6.
Corrected. Table 3's caption: "applied as a step at sample 300, the start of window 6, or built up over windows 6 and
7 (ramp)". Fig 3's caption: "applied as a step at sample 300, the start of window 6". Methods: "as a step at the start
of window 6 and as a ramp over windows 6 and 7". The figure script's comment says the same.

### T24 — minor (also R03)
Corrected. As R03.

### T25 — minor
Finding: −0.74 per unit of pair r₁ is the ratio of two printed means; from unrounded means it would be −0.75.
Stated, not changed. The value is kept and said to be what it is. Results 4: "(−0.74 per unit of pair r₁, from the
printed means)"; Fig 3's caption gives the two means beside it; S13 Table's note: "the printed means: the pair r₁ DiD
is saved at four decimals". S3 Text §6 says the same of the residual table's caption, which was moved with its "−0.74
per unit of pair r₁" unchanged. The unrounded pair r₁ DiD is in no committed file: the audit computed it from the
released series, and the paper uses no value computed there (S5 Text §4).

### T26 — minor (also R53)
Corrected. As R53.

### T27 — minor (also R23)
Corrected. As R23.

### T28 — minor
Finding: The list of supporting information did not name the new subsections of S3 Text, S5 Text §1's paragraph or S18
Table's new part.
Corrected. The entries name them: for S3 Text the lag-1 transfer entropies, the pre-injection gap with the three
readings of the contrast, the replaced volumes, the residual table, the generators' per-subject slopes, the atoms at
fixed orders and the costs of prewhitening reported in the literature; for S5 Text the deviations from the
pre-specification; for S18 Table the generators' per-subject slopes.

### T29 — minor (also R12, C29)
Finding: Four clauses of the Abstract said more than the Results.
Corrected. (i) "the atom is near zero and, on the family, nearly flat in r₁". (ii), (iii) "prewhitening removes r₁
only at orders leaving mostly stop-band residue, where a smaller contrast remains"; Results 7 says of the contrast at
p ≤ 5 that its interval includes zero and no longer says that no order removes the contrast; Recommendations: "the
prewhitening orders that remove r₁ leave mostly stop-band residue, with a lower level and a smaller contrast". (iv) As
R12.

### T30 — minor (also C07)
Finding: Methods called four records "outside the scope", a word the paragraph defines otherwise.
Corrected. Methods (Literature search): "six of the nine, four that are not ΦID studies and one study added". The
literature file: "four are not empirical fMRI ΦID studies (an O-information study, a local O-information study, a
partial entropy decomposition and a software library; `screening.md` gives each)".

### T31 — minor
Finding: Three pointers of S3 Text led to statements the main text no longer has.
Corrected. S3 Text §10 no longer says that the Discussion quotes 32.8. The sentence of §9 on the within-run variance
change no longer points to Results 7. §10's pointer to the Discussion for the surrogate gradient's correlations holds
again: the Discussion gives them as "surrogate |ρ| ≤ 0.26, one significant" (T51 (iii)).

### T32 — minor (also R36)
Corrected. As R36.

### T33 — minor
Finding: S3 Text §6 wrote the generator's distribution with the standard deviation as its second argument.
Corrected. S3 Text §6: "a_x, a_y ~ N(0.85, 0.0125²)", as §7, S10 Table and Methods have it.

### T34 — minor
Finding: S3 Text §5 called the mean framewise displacement that of the TRs above the threshold.
Corrected. S3 Text §5: "the number of TRs above the threshold, the mean framewise displacement of the window's TRs and
the window's whole-brain r₁".

### T35 — minor
Finding: S3 Text §9 said that the sts level shrinks with r_τ; it rises again at τ = 5.
Corrected. S3 Text §9: "r_τ falls with τ and the sts contrast shrinks at every step; the sts level follows |r_τ| (it
is 0.0262 at τ = 3 and 0.0415 at τ = 5, where r₅ = −0.202)".

### T36 — minor (also R18)
Corrected. As R18.

### T37 — minor
Finding: S5 Text §5 and §6 called the table whose caption was corrected on 1 October "Table 3", now another table.
Corrected. S5 Text §5: "the caption of what was then Table 3 (the residual table, now in S3 Text §6)"; §6: "the
caption of what was then Table 3, now the residual table of S3 Text §6". README.md and CLAUDE.md say "the then Table
3" too.

### T38 — minor (also R33)
Finding: S5 Text §1 and S19 Table did not give what replaced each deviation, as Methods said; five cells of S19 Table
pointed to Methods.
Corrected. (i) S5 Text §1 says which three deviations were replaced and by what, which two were withdrawn, and which
three are departures with nothing put in their place; Methods: "listed in S5 Text §1, with what replaced each where
something did". (ii) S5 Text §1 says what S19 Table holds of them and for which it has no row; Limitations cites "(S19
Table; S5 Text §1)". (iii) As R33. (iv) The five "reported at" cells name S5 Text §1.

### T39 — minor
Finding: Table 4's caption defined r for the whitened series only, and the AR(1) row's correlation was in no
supporting file.
Corrected. Table 4's caption: "r: the per-subject correlation of the sts DiD with the same series' r₁ DiD (the raw
row's from Results 2; S11 Table; S3 Text §8)". S3 Text §8 gives +0.899 at p = 1 with its source file and its interval.

### T40 — minor (also R52)
Finding: The interval of the EEG check was not marked as a percentile interval; "nothing on the placebo run" held for
one variant.
Corrected. (i) Discussion: "percentile interval [−0.40, −0.08]". (ii) As R52.

### T41 — minor (also R40)
Corrected. As R40.

### T42 — minor (also R20)
Corrected. As R20.

### T43 — minor (also R34)
Corrected. As R34.

### T44 — minor (also R13)
Corrected. As R13.

### T45 — minor (also R25)
Corrected. As R25.

### T46 — minor (also R09, R39)
Finding: The numbers table: the head note, a row without an occurrence, numbers without rows, notes and locators that
do not agree with their source lines.
Corrected. (i), (ii), (iii) As R09 and R39; the pages of Cliff et al. are no longer in the main text, and "Rows 2–6"
has its label rows. (iv) The notes say "the one-sample t test (13 df)" and "B23 (a3)", and the spin p of the residual
map is sourced to `aligned_directed_tables.md`. (v), (vi), (vii) The 13 anchors, the held string and the 19 committed
rows of N = 14 are corrected, and the 14 added rows of N = 14 take the corrected line (the 14 is now located on the
record's line that gives the shape of the data). After the update the anchor and the held string of every row with a
line locator are on the line it names.

### T47 — minor (also R22)
Corrected. As R22.

### T48 — minor (also R24)
Corrected. As R24.

### T49 — minor (also R29)
Corrected. As R29.

### T50 — minor
Finding: S4 Text D8 placed in Methods what S1 Text states.
Corrected. S4 Text D8: "Methods, Dataset: one DMT run and one placebo run per subject. S1 Text: two testing days two
weeks apart, a single-blind design with the order counterbalanced, half the participants receiving placebo first".

### T51 — minor (also C26)
Finding: Clauses the condensation removed were neither in the supporting information nor reworded in place.
Corrected. (i) Introduction: "hence positive MMI synergy since MMI redundancy is non-negative" and "single-target
lagged PIDs of multivariate autoregressive processes" are restored. (ii) Results 3: "in macaque single units, from
sensory to prefrontal cortex, Murray et al., 2014" is restored. (iii) Discussion: "the six macroscale associations of
their Table 1 on that dataset (surrogate |ρ| ≤ 0.26, one significant, against 0.22–0.54 observed; S20 Table)". The
reason recorded with the Introduction's replacement now holds.

### T52 — minor (also R37)
Corrected. As R37.

### T53 — note (also R44)
The audit's instructions. As R44.

### T54 — note (also R01)
Corrected. As R01.

### T55 — note (also R57)
Finding: Five dispositions said a little more than the text has, or left a part of their finding unanswered.
Corrected. (i) The disposition of B's MINOR 1 says where each value is (the SE and the three excesses in Results 4;
the range of the excesses beside the detectable difference in the Abstract and the Discussion) and that the
sensitivity is that of a t test; Results 4: "a t test detects". (ii) As R57. (iii) S3 Text §4, S5 Table's note and S19
Table's row give "p < 1/10,000". (iv) The disposition of A's M1 says what of M1 (b) the ramp answers and what is not
computed, and Limitations says of the calibration that its change is "a step or a two-window ramp, not on a second
dataset or the placebo series with a known change written in". (v) The disposition of A's m10 names the sentence of
Table 1's caption on TDMI's residual DiD.

### T56 — note (also R38)
Finding: Dispositions spoke of the note to the co-authors as existing, and CLAUDE.md gave it fewer items.
Corrected. The dispositions say that the note is not yet written and call its contents items of it. The entry ends
with the list of the items, and CLAUDE.md's "Remaining work" has the same list, word for word. S20 Table's two cells
carry no promise (R38).

### T57 — note
Finding: S19 Table's Part B had no row for the numbers derived for this revision, and four "reported at" cells were
out of date.
Corrected. (i) Part B has a row for `derived_r24.out`, with the places that quote its numbers. (ii) The cells: the EEG
Lempel–Ziv prediction ("Discussion; S1 Text; S6 Table"), B25 (a) and (b) ("Results 6; S3 Text §11"), B23 (a3)
("Results 1; S18 Table; S3 Text §6") and B26 ("Table 1; Methods, The AR(1)-substituted estimate and its calibration;
S3 Text §6").

### T58 — note
Finding: "For the same fall" held for one generator; the three rates were called ratios over simulated subjects; 0.786
had lost "at a = 0.85".
Corrected. (i) Results 2: "between the AR(1) pairs' 3.1 and the band-passed generator's 6.1 (Results 4; S13 Table)".
(ii) Results 4 calls the three rates "ratios of means under one change of r₁" and Fig 3's caption "each a ratio of
means under one change of r₁", and S3 Text §6 says over what each is taken (the band-passed generator's simulated
subjects; 3,000 AR(1) pairs against the unperturbed pairs; one simulation of the null). (iii) Methods: "whose pair r₁
in 60-sample windows is 0.786 at a = 0.85 (S18 Table)".

### T59 — note
Finding: The degrees of freedom of Table 3's rows with subjects left out; the divisor of the generators' SDs; "the
subjects' own changes" are rescaled and floored.
Corrected. (i) Table 3's caption: "(n − 2 df: 11 with one subject left out, 10 with two)"; Methods: "t intervals on n
− 2 degrees of freedom (12 for the 14 subjects)". (ii) The caption: "mean ± SD (the script's, with divisor 100)".
(iii) Fig 3's caption: "the data's r₁ DiD, rescaled and floored as Table 3's caption says"; Results 4 points to that
caption.

### T60 — note
Finding: The definition of the AR(1)-substituted estimate pointed in a circle and used a_x and a_y before introducing
them; "global fit" was explained in Methods only.
Corrected. (i) The definition in the Results' opening paragraph points to Methods alone; Table 1's caption, Results 4
and S12 Table's note point to that paragraph. (ii) The paragraph introduces a_x and a_y where it defines pair r₁.
(iii) It defines the global fit ("a global fit one fit over a whole run"), and the Abstract says "whole-run fits".

### T61 — note
Finding: The new subsections stood before §5's own table; two kinds of level were given without distinction;
"artefact" was said to be reserved for nothing.
Corrected. (i) The two new subsections stand at the end of S3 Text §5, after its own table and paragraphs. (ii) S3
Text §8 says that the levels of the diagnostic are means over both runs and all windows, where the levels above them
are DMT pre-injection means, at p ≤ 5 as at p = 10 and 20; S11 Table's note and "B16c, outcome" (e) say it too. (iii)
The disposition of A's w1 says where the word stays: once in the main text, to deny it; quoted as the plan's word in
S3 Text and in S19 Table's rows of B2 and B3; and once more in S3 Text §9, in committed text, which denies that a part
of the r₁ change is one ("not an artefact of scale").

### T62 — note (also R46)
Finding: The form of `matched_slope.csv`; README.md's list of computations stopped at B26.
Corrected. (i) As R46. (ii) README.md: "B16b, B17b, B21–B24, B25, B26, B27–B29 and B16c have been run and their values
are in the text".

### T63 — note (also R54)
Corrected. As R54.

## The citations (`findings_citations.md`)

### C01 — blocking
Finding: Results 7 stated for the lag-1 pair of transfer entropies an invariance that the cited works prove for
Granger causality regressed on the whole past.
Corrected. Results 7 attributes no invariance to the lag-1 pair: "the pair of lag-1 transfer entropies, zero on the
family and at every AR(1)-substituted matrix (on Granger causality under filtering: Barnett & Seth, 2011; Seth et al.,
2013)", as one of two candidates "not computed on these data". S3 Text §3 states the two works' results as results on
Granger causality regressed on the whole past, with the infinite model order of the filtered process, the proviso that
the convolution be an invertible filter, which excludes onset delays, and the pages; it then says that the lag-1 pair
does not share the invariance exactly and gives the audit's example. `te_filter_check.py`, the population check the
audit sent, is committed beside its report. The claim record's two items say where the results are stated and that
Results 7 attributes no invariance to the lag-1 pair; the record's disposition of A's m10 says the same.

### C02 — blocking
Finding: Results 7 described as Liardi et al.'s normalisation a subtraction that is not their method.
Corrected. Results 7: "null-model normalisation (Liardi et al., 2025, for PID), under which each atom is read as its
quantile among random systems of equal total mutual information, a total that on the family depends on r₁ alone". No
subtraction is described, and the candidate is listed as not computed. S3 Text §10 says what the method is (their p.
7) and that what a normalised sts would keep of the dependence on r₁ was not computed, on the family or on these data.
The claim record has the item; the record's disposition of A's m14 says the same.

### C03 — should fix (also R10)
Corrected. As R10.

### C04 — should fix (also T19)
Finding: The Introduction stated as fact one of the two ways in which Luppi et al. (2024) describe their synergy.
Corrected. Introduction: "(Luppi et al., 2024, who name their synergy the persistent synergy and give its formula as
their Eq. 5, the four-atom sum of Results 1)". S20 Table's row 3 gives the name and the formula too, as the
whole-minus-max formula of Eq. 5 (T19), and the claim record has the item with both places of the work.

### C05 — should fix (also R37)
Corrected. As R37.

### C06 — should fix (also R11)
Corrected. As R11. The folder's README says of `search_string.txt` that it holds a statement that PubMed's reading of
the string was not kept.

### C07 — minor (also T30)
Corrected. As T30.

### C08 — minor
Finding: S4 Text D3 cited the screening visit to both source papers; Timmermann et al. (2023) alone report it.
Corrected. S4 Text D3: the population and the exclusion criteria are cited to both works, "and Timmermann et al.
(2023) the screening visit".

### C09 — minor
Finding: Who was blind, and global signal regression as the last step, were cited to both source papers; only
Singleton et al.'s documents state them.
Corrected. S1 Text and S4 Text D8: "participants were blind to the order and the study personnel were not (Singleton
et al., 2025, Methods and Reporting Summary)". S1 Text and S4 Text P6 give global signal regression as the last step
of Singleton et al. (2025) alone. The claim record notes that Timmermann et al.'s list ends at the nuisance regressors
and that they did not perform it in their main analyses.

### C10 — note
Finding: Results 7 listed among prewhitening's costs a concern that Honari et al. raise and their simulation did not
bear out.
Corrected. Results 7 no longer states the clause; it points to S3 Text §8 for "Prewhitening's other reported costs"
with the three citations, and S3 Text §8 gives Honari et al.'s concern with their simulation's result.

### C11 — minor
Finding: After the inserted sentences "Its Table A" read as the search note's.
Corrected. S3 Text §10: "Table A of the literature file lists".

### C12 — minor (also R10)
Finding: The claim record said that two places state Timmermann et al.'s count; neither did.
Corrected. S1 Text and S4 Text D4 now state it (R10), and the claim record's pointer names them and says that the main
text's Dataset paragraph gives the six and cites Singleton et al. (2025) alone.

### C13 — minor
Finding: A quotation of the claim record dropped words without a mark of omission.
Corrected. The claim record quotes the sentence whole: "Values related to head motion (i.e., frame-wise displacement;
FD) were significantly different between DMT and placebo (P = 0.003)".

### C14 — minor
Finding: The quoted sentence of Luppi et al. (2022) is on PDF p. 15, not p. 14.
Corrected. The claim record's item gives PDF p. 15 and notes that the paragraph begins on p. 14; the reasons recorded
with the two replacements say the same.

### C15 — minor
Finding: The claim record's paraphrase of Rosas et al.'s Theorem 1 was not the theorem, and "the measure" is the
work's "a measure".
Corrected. The claim record states the theorem as the work does (a system has a causally emergent feature of order k
if and only if that synergy is positive) and quotes "serves as a measure of the emergence capacity of the system",
noting that the criterion for a given feature is Definition 2, which the paper does not use. S3 Text §11: "a synergy
that then serves as a measure of the system's emergence capacity".

### C16 — minor
Finding: Three pages of the claim record did not hold all that was put at them.
Corrected. (a) Timmermann et al. (2019): the abstract and p. 3 for the rise of signal diversity and the fall of alpha
power, with the note that the relation to the plasma concentration is a result of pp. 4–5, which the paper does not
use. (b) Liardi et al. (2025): MMI on p. 3, the three datasets on p. 9, Fig 4 on p. 10, the comparison with CCS and
the dependency-constraints PID on p. 11, ΦID on p. 14; the search note describes the work in the same way, with those
pages. (c) Gao et al. (2026): the tests at pp. 3–4, and "distance-based (variogram-matching) surrogates".

### C17 — minor
Finding: Four "Stated in ..." pointers of the claim record named places that do not hold all that the item lists.
Corrected. (a) The eye mask and the EEG: "Stated in S4 Text (A1, A5)". (b) The preprocessing: "Stated in S1 Text, in
S4 Text (P1–P4 and P6) and, for the censoring, in the main text's Dataset and Limitations paragraphs and in S3 Text
§5". (c) The Reporting Summary: "Cited in S4 Text at D3, D4, D5, D8, A1–A4, P1–P4 and P6, in S1 Text, in S3 Text §5
and in the main text's Dataset paragraph", with its statement on replication marked as not used by the paper. (d)
Timmermann et al. (2019): the item no longer puts the time course at the pages it cites, and says that the paper does
not use that result.

### C18 — minor
Finding: A quotation from the Reporting Summary held the form's field label inside the quotation marks.
Corrected. The claim record: under the form's heading for volume censoring, "volumes with a frame-wise displacement
greater than 0.4 were replaced with the mean of surrounding volumes".

### C19 — minor
Finding: S3 Text §3 dropped the abstract's "often", cited the equivalence with transfer entropy to the abstracts, and
had "on simulated BOLD" for theory and simulation.
Corrected. S3 Text §3: "in practice inferences often do change after filtering"; the equivalence is cited to p. 406 of
Barnett & Seth and p. 543 of Seth et al.; "in theory and in simulations". The claim record's two items have the same.

### C20 — minor
Finding: Four statements were wider than the five documents.
Corrected. (a) S4 Text P1: "the sources read give no version of these packages as applied to these images". (b) P3:
"the sources read do not state the space in which it was applied". (c) A1 and the closing paragraph give the
eyes-closed condition as the condition and list what participants were instructed among what the sources read do not
state. (d) The Ethics statement: "derivatives released by the data authors (Singleton et al., 2025)", without
"pseudonymised"; the word stays in S1 Text as this paper's description of the released files, and S4 Text Sh5 says
that it is S1 Text's.

### C21 — note
Finding: The documents do not agree on whether a testing day held one substance or both, which bears on a sentence
about the ratings and on what is asked of the data authors.
Corrected. S1 Text ("collected in scan runs other than the analysed ones, in the second scanning session") and S4 Text
D6 ("collected in other scan runs, in the second scanning session") no longer place the ratings on the day of the
analysed runs. Whether a testing day held one substance or both is an item of the note to C.T. and S.P.S., with each
subject's session order. The Reporting Summary's atlas of 232 regions is not taken up: the paper states the release's
100 cortical and 16 subcortical regions, as the Methods of Singleton et al. (2025) and the release itself do.

### C22 — note (also R38)
Corrected. As R38.

### C23 — note
Finding: "The same four-atom sum" had lost its antecedent in the Introduction.
Corrected. The antecedent is in the paragraph before it again: "their Eq. 5, the four-atom sum of Results 1" (C04).

### C24 — note (also R01)
Corrected. As R01.

### C25 — note (also R19, R13)
Corrected. (a) As R19. (b) As R13.

### C26 — minor (also T51 (ii))
Finding: Results 3 had lost "from sensory to prefrontal cortex" for Murray et al. (2014), whose areas include no motor
area.
Corrected. The words had been restored for T51 (ii) before the report's second form raised it: "(Raut et al., 2020;
Ito et al., 2020; in macaque single units, from sensory to prefrontal cortex, Murray et al., 2014)". The claim record
has an item on Murray et al. (the seven areas of its Fig. 1, none of them motor).

### C27 — minor
Finding: Results 6 and S19 Table's row gave the two derivatives as those of Luppi et al. (2023)'s quantity; they are
those of the paper's reading of it.
Corrected. Results 6: "the binarised CCS emergence capacity (Rosas et al., 2020) of Luppi et al. (2023), as we read
it, has ∂/∂r₁ = +0.124 and ∂/∂q = +0.142 (S3 Text §11)". S19 Table's row of B25 (d): "Luppi et al. (2023)'s as we read
their Methods +0.0397". The claim record has an item on what the study's Methods state and do not state.

### C28 — minor
Finding: The screening file quoted, for Pope et al.'s measure, the paper's words on the O-information, gave the page
by the PDF without saying so, and kept two sentences that no longer fitted its table.
Corrected. `screening.md`, the row of Pope et al. (2025), says that the study's measure is the local O-information,
"the form resolved in time of the O-information", and that it is the O-information that the paper calls "a heuristic
measure of redundancy/synergy dominance", with the pages: "(PDF p. 3, the article's p. 2, where the paper also names
the local measure as the one it chooses; the section that derives it begins on PDF p. 5 and its formula is on PDF p.
6)". The file says that a page is the page of the PDF as saved, speaks of "the two that were left on 1 October 2026 to
be assessed from their full texts", and ends: "With Gao et al. (2026), which the string returns, the table now holds
ten."

### C29 — should fix (also R12, T29 (iv))
Finding: The Abstract's first sentence had lost "most".
Corrected. As R12, corrected before the report's second form raised it: "underlies most fMRI synergy reports we
found".

### C30 — minor
Finding: The search note said that a study is returned only if its title or abstract names both kinds of term; its own
second record has its decomposition term in the keywords.
Corrected. The note says that PubMed's Title/Abstract field takes in a record's author keywords as well as its title
and abstract, with the sentence of an NLM training page as a fetch tool returned it on 2 October 2026, and gives the
record of Varley et al. (2024) as the instance; it says again that PubMed's own reading of the string was not kept. "A
study is returned only if these fields name both a decomposition term and a drug".

### C31 — note (also R25)
Finding: The reason recorded with the replacement of S20 Table's cell on HRF deconvolution (row 5) named C's M5 (b);
the change answers C's M4. The record counted eight observations under M5 (b).
Corrected. The reason recorded with the two replacements (the table's and the literature file's) names C's M4 and says
what the cell now states. The record's disposition of M5 (b) counts seven observations (R25).

### C32 — note
Finding: The paper counts ketamine with the psychedelic drugs, and a study of its own S20 Table applies ΦID to fMRI
under ketamine anaesthesia.
Corrected. S3 Text §10 says that ketamine is among the string's drug terms, that row 5's study scanned macaques "awake
and under sevoflurane, propofol or ketamine", that data under anaesthesia "are not counted here as psychedelic data",
and that the string does not return the study. S20 Table's row 5 names the three anaesthetics. The Discussion's
sentence points to S3 Text §10 beside Methods, and the search note has a paragraph on it. Since the second check of
the corrections, S3 Text §10 and the search note both name a second study of the table, row 4's, whose macaques were
given ketamine before a scan under isoflurane (W7-8).

## Points the audit of the citations raised outside its findings

**The Introduction's sentence on Luppi et al. (2022).** Raised under "Not checked", on text the revision had not
changed: the study separates the two kinds of cortex by the difference of each region's synergy and redundancy ranks,
not by synergy alone. Corrected: "On resting-state blood-oxygen-level-dependent (BOLD) signals its regional rank minus
redundancy's separates redundancy-dominated sensory and motor cortex from a synergy-dominated association cortex".

**"The ΦID authors" for Liardi et al. (2025).** Raised in the same place: four of the six authors of Liardi et al.
(2025) are among the seven of the ΦID paper, and the first author of Liardi et al. is not one of the seven. Corrected
in S3 Text §10: "Four of the ΦID paper's seven authors, with two others, have proposed null-model normalisation of PID
atoms".

**Cliff et al. (2021)'s rate.** "Checked and found exact" notes that S3 Text §8 printed 42 % for the work's 41.8 %. S3
Text §8 now has "from 41.8 % to over 88 %", with the pages and the remark that the second rate is stated in their text
and not plotted.

**Murray et al. (2014).** Listed under "Not checked" in the report's first form, because the revision had removed
"from sensory to prefrontal cortex" after "in macaque single units"; its second form raises it as C26. The words are
restored (T51 (ii)), so that the clause on the three works is the committed one, which the check of 29–30 September
2026 covered; "In the literature", at the head of the committed sentence, is dropped, as the reason recorded with the
replacement says.

**S20 Table's rows 2, 5 and 8, read in full within the audit of the citations.** The report's second form lists three
things there, under "Not checked". The total of 43 mice is on PDF p. 5 of Luppi et al. (2026) and the three group
sizes on p. 4: the cell now gives "(pp. 4–5)". Five page ranges of row 5 were wider than the pages that hold the
facts: each is narrowed to those pages (the sessions and the 350 volumes on p. 37 of the PDF, every acquisition
parameter on p. 38, the parcellations and the human and macaque filters on p. 39, the marmoset and mouse band-pass and
the mouse's global-signal statement on p. 40), which one of the checks of the corrections found as well (VN-1). Row
2's quotation, which is the opening of a sentence of the paper and stands in the cell's running text with a small
initial, is left so: the words are the paper's.

## The checks of the corrections

After the corrections above were made, apart from those that the second form of the report on the citations brought
(those for C27, C28, C30, C31 and C32, the claim record's item for C26 and the point on S20 Table's rows 2, 5 and 8),
which came later and which the second check covered (below), ten further sessions of the AI system, started by the
planning session on 2 October 2026, each checked one part of the corrected revision against the files and, where the
part concerns cited works, against the PDFs. They read the corrected revision as a commit made for the purpose on
8bd189e in the planning session's working directory (9caa60b, which is not in the repository), so that the line
numbers in their reports are that tree's. Their reports are beside this file as the sessions returned them, with two
changes: the path of that working directory is written `$SP`, and the closing line of two reports (VC, VT1), a remark
of the session on its own memory, is left out:

- `check_VO.md` (VO-1 to VO-13): the four outcome entries; 13 findings (0 errors, 4 inexact, 9 notes).
- `check_VE.md` (VE-1 to VE-25): the record's entry on the revision; 25 findings (1 error, 12 inexact, 12 notes).
- `check_VR.md` (VR-1 to VR-17): the dispositions of the audit of the record's entries (R01–R57); 17 findings (2
  errors, 9 inexact, 6 notes).
- `check_VT1.md` (VT1-1 to VT1-10): the dispositions of the audit of the text, T01–T31; 10 findings (1 error, 5
  inexact, 4 notes).
- `check_VT2.md` (VT2-1 to VT2-17): the dispositions of the audit of the text, T32–T63; 17 findings (1 error, 7
  inexact, 9 notes).
- `check_VC.md` (VC-1 to VC-9): the dispositions of the audit of the citations (C01–C25) and the claim record; 9
  findings (0 errors, 7 inexact, 2 notes).
- `check_VN.md` (VN-1 to VN-11): the statements about cited works that the audit of the citations had then left
  unchecked; 11 findings (0 errors, 1 inexact, 10 notes).
- `check_VM.md` (VM-1 to VM-10): the main text; 10 findings (0 errors, 4 inexact, 6 notes).
- `check_VS.md` (VS-1 to VS-12): the supporting information and the literature file; 12 findings (0 errors, 7 inexact,
  5 notes).
- `check_VB.md` (VB-1 to VB-33): the numbers table, the replacements file, the bookkeeping files and the checks'
  outputs; 33 findings (6 errors, 13 inexact, 14 notes).

The ten reports hold 157 findings, graded by the sessions as 11 errors, 69 inexact statements and 77 notes. No value
of a result in the main text or in the supporting information was found wrong; what the sessions found inexact there
are dates, pages, pointers and wordings. The eleven graded errors are one wrong number in the record's entry on the
revision, which four of the sessions found (the upper end of a leave-one-out range given as 4.54, a second rounding of
4.535), and seven findings on the bookkeeping: the notes of two rows and the source of one row of the numbers table
(VR-2, VB-3), the places that the list of deleted rows gave for two sets of moved numbers (VB-1, VB-2; VB-2 found its
wrong place in the reason recorded with a fifth replacement and in the record's entry as well), and the reasons
recorded with four replacements (VB-4, VB-5, VB-6). The grades counted are those that the findings carry; the opening
sentence of `check_VT2.md` counts its seventeen as 8 inexact and 8 notes beside the error, where their grades are 7
and 9. Each finding was read against the files before anything was changed. Of the 157, 142 were corrected: a file of
the commit was changed as the finding says; three of these have a second part that is kept, with the reason (VT1-10,
VM-6, VM-8). 7 name something that is kept, and a text of the commit now says what it is. 8 are kept without a change,
each with its reason here. Where several sessions found the same thing, the disposition is written once and the others
point to it.

### VO: the four outcome entries

**VO-1** (inexact). The entry on B28, and with it S18 Table's source line, said that the run read no data but the
subjects' whole-brain r₁ DiDs; the script reads three committed inputs that derive from the data. Corrected. The
entry's first paragraph names the three: the r₁ DiDs (`inference_rows_raw.pkl`), the residual DiDs, for the data's
slope and r (`inference_rows_diag.pkl`), and B17's pool of the data's window-level pair q, from which the AR(1)
conditions draw (`partB/scope_map_overlay_points.npz`, key `pre_w1to4_q`, 52,440 values). S18 Table's source line
names the same three (VS-7).

**VO-2** (inexact). The entry on B16c, S3 Text §8 and S19 Table's row B16c (e) placed the contrast of xtx + yty in the
tables file, which gives xtx and yty as two rows and no contrast of their sum. Corrected. The three places say that
the contrast of the sum is in `inference_rows_prewhiten_fixed.csv` and in `derived_r24.out`, item 1, which gives its
inverted interval too (the entry says so); the entry quotes its two values on ts_gsr at W = 60 (−0.0229 [−0.0409,
−0.0053], p = 0.0077, at p = 10; −0.0060 [−0.0098, −0.0022], p = 0.0037, at p = 20).

**VO-3** (inexact). The entry on B27 said that the audit of the prepared commit restated the predictions. The audit
found that the group means of the r₁ gaps follow from committed rows; the restatement was the answer to it. Corrected.
The entry: "they were restated to the criteria above in answer to that audit's item 3, which found that the group
means of the r₁ gaps follow from committed rows (`audit/dispositions.md`, item 3)".

**VO-4** (inexact). S3 Text §5 and §6 put one date, 1 October 2026, after the titles of a pre-run entry and its
outcome entry together; the outcome entries are of 2 October. Corrected. In the three places (B27, B29, B28) the date
follows the pre-run entry's title alone, and the outcome entry is cited by its title, as S3 Text §8 cites B16c's.
Found also by VS-1 and VR-3.

**VO-5** (note). "The unit ran on battery to its end": the heartbeat's last line is 178 s before the end of the last
step. Corrected. The entry says that the charger was disconnected from the heartbeat's line 4 to its last line
(00:32:10) and that "no line covers the 178 s from that line to the end of the last step"; S5 Text §4 has the same in
a clause (VR-15).

**VO-6** (note). The entry's sentence on the values that the pre-run entry lists as known named fewer rows than that
item holds, and nine of the values are not printed in B27's tables file. Corrected. The sentence now says where each
kind is reproduced: those the tables file prints, in its tables (a), (b) and (c); those it does not print (r² = 0.79,
the SDs 0.0887 and 0.0485, the three values of subject 14, the two of subject 8 and the intercept +0.0005), from
`baseline_gap.csv`, from which `derived_r24.py` recomputes them with the regression's slope and r and the ratio of
means, and compares the twelve with the pre-run entry's values as printed (item 12 of its output: 12 of 12 equal; S19
Table's Part B has the row); the ratio of means, −0.788, is also in B28's tables file. The comparison was added after
the second check: until then the item printed the values and compared nothing (W2-3).

**VO-7** (note). Item (ii) said that Results 2's sentence has one word changed from S2 Text's; the two sentences
differ by more than the one word. Corrected. Item (ii) says that Results 2 applies the scrutiny in other words than S2
Text's, where the rule has "in the same words", and it quotes both phrases.

**VO-8** (note). Two phrases that the entries quoted as the text's ("not distinguished", "not identified") are not the
Abstract's words. Corrected. B27's item (iv) gives the places of "not distinguished" (Results 4, the Discussion) and
the Abstract's own words ("a test detecting 0.0155 does not resolve this"); B28's item (iv) gives the Abstract's "its
source is unidentified" and places "not identified" in Results 4 and the Discussion.

**VO-9** (note). B28's rule kept the three rates "only" as the group-level comparison; in the text they also stand
against the data's per-subject slope, and the entry had dropped "only" without saying so. Stated. The text is kept:
Table 3's rows on the leave-one-out and the leave-two-out count the intervals that contain each rate, which B27's rule
(iv) requires, and Fig 3c draws the three rates on the per-subject panel, as the committed figure did. The entry's
item (i) now says that these two places go beyond the rule's "only".

**VO-10** (note). S18 Table's part on B28 reports the band-passed conditions without naming the subject held at the
generator's floor. Corrected. S18 Table's source line: "on the band-passed generator subject 8 is held at the
generator's floor"; the entry's item (iii) names that line with Table 3's caption and S3 Text §6.

**VO-11** (note). "S18 Table its slope columns": S18 Table's part on B28 has eleven of the fourteen columns, and the
shares of r that S19 Table's row B28 (d) reports are in S3 Text §6 only. Corrected. The entry's item (v) says which
columns S18 Table leaves out (the percentiles of r, the share of replicates with r at or below the data's, the
percentiles of the ratio); S19 Table's row B28 (d) gives "S3 Text §6; S18 Table (the sts DiDs and the coverage)", and
S18 Table's source line says that S3 Text §6 has the table in full (VS-4).

**VO-12** (note). The diagnostic's levels at p = 10 and 20, in the entry on B16c and in S11 Table's note, are means
over both runs and all windows, and stood beside DMT pre-injection levels without the difference being said.
Corrected. The entry, S11 Table's note and S3 Text §8 say that the diagnostic's levels are means over both runs and
all windows, the entry and S3 Text §8 adding that the levels of the cells are DMT pre-injection means; the lines on
the diagnostic at p ≤ 5 say the same (VT2-7).

**VO-13** (note). "S3 Text §5 transcribes the tables": of table (c), the correlations of the sts DiD with the r₁ DiD
in the three named sets were not carried. Corrected. S3 Text §5 (c) now gives them ("+0.953 with all 14 subjects and
+0.921, +0.931 and +0.846 in these three sets"), and the entry's item (vi) says that S3 Text §5 carries (a) and (b)
cell for cell and (c) in prose with every value.

### VE: the record's entry on the revision

**VE-1** (error). The entry gave the leave-one-out range of the sts slope as 4.14 to 4.54 (the upper end is 4.5346).
Corrected. As VT2-4: "(4.263: 4.139 to 4.535)".

**VE-2** (inexact). "33 rows of N = 14" among the corrected locators of committed rows: 19 are committed rows, and 14
are rows the revision adds. Corrected. "13 anchors, 19 rows of N = 14, whose corrected line the 14 added rows of N =
14 take too, and 1 held string"; `numbers_update.out` and the table's head note say the same.

**VE-3** (inexact). "444 added, each with its source and line": the label rows have no source and the derived rows a
derivation in place of a file and a line. Corrected. The entry gives the added rows by category, with what each kind
carries: data rows "with file, line and held string", design and literature rows "with file, line and anchor", derived
rows "with the derivation", label rows, "which have no source". Found also by VR-8 and VB-9.

**VE-4** (inexact). The entry's list of the kinds of number token that have no row left out kinds that the head note
names, and neither named the tokens of the headings and of the captions' own heads. Corrected. The entry lists
"citation years, cross-references by number, the numbers of the captions' own heads and of the headings, dates, commit
identifiers, the Zenodo DOI, code spans", as the head note now does; `numbers_update.out` counts each kind. Found also
by VR-9, VB-8 and VB-24.

**VE-5** (inexact). The entry said that `figures_check.py` tests the conditions as stated; the script also requires
that Fig 2's caption, without its Source sentence, equal the main text's, and that the header's SHA carry no "-dirty".
Corrected. Condition (1) states both: the header must name the commit's short SHA without "-dirty", and "each of the
six captions must hold a Source sentence and, without it, equal the main text's caption, and Fig 2's must also be the
committed one". Found also by VR-4.

**VE-6** (inexact). "`numbers_update.out` lists every deleted row of the numbers table with where its number now is":
for the 28 label rows it gives no place. Corrected. The entry says for which classes the list gives a place (the 161
rows of the former Table 3 and the 64 of numbers taken out of their paragraph), for which it says what became of the
number (7), and that "the 28 deleted label rows ... have no place to give".

**VE-7** (inexact). "The bracketed earlier p values": the committed Results 4 had one bracketed earlier p value and
one bracketed earlier cross-half correlation. Corrected. "the bracketed earlier p value and cross-half correlation of
Results 4"; the disposition of B's W4 says that the correlation was removed with the p value and that B does not name
it.

**VE-8** (inexact). "Sentences retired, each by a rule or a finding and not for length" listed two sentences for which
no rule or finding is named: the Introduction's sentence listing the Results sections and the Author summary's first
sentence. Corrected. The entry separates them: "Two sentences retired for length: the Introduction's sentence listing
the Results sections, which the headings give, and the Author summary's first sentence, merged into its second for the
200-word limit". The reasons recorded with the two replacements say so, that of the Introduction's since the second
check (W6-18).

**VE-9** (inexact). "The dispositions above that name it assign these items to it": several items of the note's list
are assigned by no disposition. Corrected. As VT2-9.

**VE-10** (inexact). The disposition of C's m4 said that the agreement waits for the co-authors; README.md and
CLAUDE.md record it as confirmed by email. Corrected. The disposition: "the agreement exists in writing as two emails
that V.S. holds, from C.T. (13 September 2026) and S.P.S. (14 September 2026), as README.md's paragraph on the licence
records, and the note asks the two whether the sentence may stand; the acknowledgments wait for the co-authors".

**VE-11** (inexact). The disposition of C's M1 did not answer one part of the finding: that the codes in the git
history contradict "not redistributed". Corrected. The disposition says that the remark is answered by the record and
not in the text: the sentence of Data and code availability is about the release's files, which the repository does
not hold, and the record's two entries of 15 September 2026 state that the codes stood in six tracked files until that
day and remain in the history before fa39ef2.

**VE-12** (inexact). The disposition of B's W1 gave S19 Table's row a clause it does not have. Corrected. As VT2-11.

**VE-13** (inexact). Two glosses of `numbers_update.out` did not match their rows: the "10" of 10⁻¹⁶, described as of
the full run, and Cliff et al.'s 42, sent to a place that prints 41.8 %. Corrected. The two lines: for the 10, "10⁻¹⁶,
the level of the differences in a separate session's re-run of the data-free computations of 23 September 2026"; for
the 42, "S3 Text §8, as 41.8 % (the first of the two false-positive rates of Cliff et al., as their text gives it)".
The entry says that the list marks a number that stands at its new place with more decimals, which the list does for
six more numbers since the second check (W4-2).

**VE-14** (note). The disposition of A's w1 left out the second, unquoted use of "artefact" in S3 Text §9. Stated. As
VT2-6.

**VE-15** (note). The disposition of C's w4 placed "within a window" in the Abstract, which has "per within-window
standard deviation". Corrected. The disposition says that the Abstract has "per within-window standard deviation" and
Results 1 "within a window".

**VE-16** (note). Three sub-points of findings were not mentioned in their own dispositions (A's m4 on Cliff et al.'s
numbers; C's m13 on the line "Manuscript for co-author review"; C's M5 (a) on a confirmation with the authors).
Corrected. Each disposition now has its sub-point: A's m4 points to C's m14 for the numbers given from the paper; C's
m13 says that the line stays until submission, when it goes; C's M5 (a) says that a confirmation with those authors
was not sought.

**VE-17** (note). The disposition of C's M5 (a) gave the Introduction a form with "whole-minus-max", which the
Introduction does not have. Corrected. The disposition gives each place its form: the Introduction, "its formula as
its Eq. 5, the four-atom sum of Results 1"; S20 Table's row 3 and the literature file, "the whole-minus-max formula of
its Eq. 5".

**VE-18** (note). The list of statements moved from the main text omitted the Use of AI tools statement's sentence on
the accidental copy of the data and its 28-second test. Corrected. The list has it: "the Use of AI tools statement's
account of the copy of the data that a session held by accident and of the 28-second test run on it (S5 Text §4)".

**VE-19** (note). The entry placed the ideal-band-pass r₁ at TR 0.72 s and the derivative there in S3 Text §10, while
the Discussion pointed to S3 Text §4 at that place. Corrected. The Discussion's sentence points to both sections, "(S3
Text §4, §10)": §10 holds the two values and §4 the statement that the derivative does not rank datasets.

**VE-20** (note). "Condensed in every section": two subsections of Methods are word for word the committed ones.
Corrected. "condensed in every section, before the audits and again after them; two subsections of Methods stand word
for word (Redundancy functions; Regional maps)". The planning session's preparation of the revision tests that these
two and no others are unchanged.

**VE-21** (note). The paragraph on the figures did not name the anchor of Fig 5c's legend, and Fig 3c's legend title
stays at 6.8 pt. Corrected. As VT1-2.

**VE-22** (note). In the session's regeneration, in an environment that is not the pinned one, Fig 5's PNG was 2.22 %
narrower than the committed file, inside the limit of 3 % by 0.78 %. Kept. The limit is tested on V.S.'s machine, in
the pinned environment in which the committed figures were made, where the revised script alone changes Fig 5's width
by about 1 % (VT1's comparison of the two scripts in one environment: −1.10 % in width, +0.11 % in height). A failure
of the condition blocks the figures commit, as the entry says.

**VE-23** (note). "No computation of this commit was run on the data" stood beside the entry's own account of the text
audit's computations on the released series; and `derived_r24.py` reads a tables file as well. Corrected. The first
paragraph: "No computation whose result the paper uses was run on the data for this commit (the text audit computed on
the released series for three of its findings, as the paragraph on the audits below records); `derived_r24.py` reads
committed files only: two pickles of per-subject vectors, eight CSV files, five tables files, three array files and a
log" (the kinds counted since the second check, W4-13; the counts those of the script as it stands after the third).

**VE-24** (note). The sentence on the main changes named S11, S18, S19 and S20 Tables; the notes of three more tables
change. Corrected. "with the notes of S5, S12 and S13 Tables, a clause of S17 Table's source note and the head note of
the supplementary tables" (the clause of S17 Table's source note since the fourth check: Y1-4).

**VE-25** (note). Recorded for coverage: a clause-by-clause comparison of the committed main text with the revised one
found no moved statement missing from the entry's lists beyond VE-18 and VE-19. Kept. Nothing to change.

### VR: the dispositions of the audit of the record's entries (R01–R57)

**VR-1** (error). The correction made for R22 put a wrong number into the record's entry: the leave-one-out range of
the sts slope as 4.14 to 4.54 (the upper end is 4.5346). Corrected. As VT2-4: "(4.263: 4.139 to 4.535)".

**VR-2** (error). The notes of two committed rows of the numbers table (Results 4, the generators' pair r₁ changes)
pointed to Table 3 for values that are now in the residual table of S3 Text §6. Corrected. Both notes read "(the
residual table of S3 Text §6)"; the head note counts them among the corrections made after the checks.

**VR-3** (inexact). S3 Text §5 and §6 put one date after a pre-run entry and its outcome entry. Corrected. As VO-4.

**VR-4** (inexact). The record's paragraph on the figures and the disposition of R48 stated one condition fewer than
`figures_check.py` tests for Fig 2's caption. Corrected. As VE-5; the disposition of R48 gives condition (1) as the
record does, in nearly its words.

**VR-5** (inexact). CLAUDE.md's "Remaining work" gave the condition on the PDF files of Figs 2, 4 and 6 more narrowly
than the record and the script ("once their dates are masked"), and the disposition of R56 said that it gives the
conditions as the record does. Corrected. CLAUDE.md: "their PDF files are identical once the two date fields, the
cross-reference table and the `startxref` offset are masked"; the disposition of R56 gives the same condition. Found
also by VB-28.

**VR-6** (inexact). The note of the numbers table's row for the 366 excluded draws kept the wording that R53 corrected
in the text. Corrected. As VT1-5.

**VR-7** (inexact). S4 Text Sh3 kept the unqualified "every result table with its git SHA" that R07 corrected in Data
and code availability. Corrected. As VT1-6.

**VR-8** (inexact). "444 added, each with its source and line", in the record and in `numbers_update.out`: 103 of the
added rows are label or derived rows, which have no source file and no line. Corrected. As VE-3; `numbers_update.out`
gives the added rows by category with what each kind carries.

**VR-9** (inexact). Four details of `numbers_update.out`'s description of the table: the count of citation years
included the years of the dates; the captions' own numbers were in no count; one deleted row was classed as still in
its paragraph; and the two cross-half correlations' intervals were placed in Fig 3b as well as in S3 Text §5.
Corrected. The file counts each kind apart (95 citation years; the day numbers and the years of the dates; the
cross-references of the running text and the captions; the ten numbers of the captions' own heads; the DOI), and says
that the headings' number tokens have no row. The deleted "1" of Results 7 is listed as moved to Table 4's caption.
The four interval limits are placed in S3 Text §5 alone, and the record's list of moved statements gives "the two
cross-half correlations (S3 Text §5; Fig 3b), their intervals (S3 Text §5)". As VB-2, VB-7 and VB-8.

**VR-10** (inexact). The disposition of R19 gave the list's entry of S3 Text words it does not have, and said that
README.md describes Fig 1 as the surface, which README.md does not name there. Corrected. As VT1-3 for the list's
entries; of README.md the disposition says that its account of the paper has "the surface of `sts` over (r₁, q)" where
it had "a scope map".

**VR-11** (inexact). The disposition of R22 placed the leave-one-out of the sts slope in item (v) of "B27, outcome".
Corrected. As VT2-3.

**VR-12** (note). S19 Table's row B29 (d) and S3 Text §5 gave the check of the non-finite TR as confirmed without the
qualification "on ts_gsr" that R50 put into the outcome entry and Methods. Corrected. As VS-11.

**VR-13** (note). S19 Table's sentence after Part A named B28, B29 and B16c as recording no prediction for one of
their parts; B27's pre-run entry also records such a part, which has no row of its own. Corrected. The sentence: "B27,
B28, B29 and B16c recorded none for one of their parts (the residual's correlations with the r₁ gaps, noted in row B27
(d), and rows B28 (d), B29 (c) and B16c (e))".

**VR-14** (note). Three places dated the addition of S20 Table's row 10 to 1 October 2026 (the literature file's
title, S20 Table's head note, S3 Text §10); the row enters with this revision. Corrected. S20 Table's head note and S3
Text §10 say that the study was found by the search of 1 October 2026 and read in full on that date, and that the row
was added in the revision of 1–2 October 2026. The literature file's title says that row 10 was added in that
revision, and its paragraph on the search that the study was read in full on 1 October 2026 and added as row 10 in the
revision (W3-12, W5-6). S20 Table's head note gives row 10's pages "as the claim record of that revision gives them".

**VR-15** (note). "Running on battery from then to its end", in S5 Text §4 and in "B27, outcome": the heartbeat's last
line is 178 s before the end. Corrected. As VO-5. S5 Text §4: "still disconnected at its last line, 178 s before the
last step's end".

**VR-16** (note). The record's disposition of A's w1 left out the unquoted use of "artefact" in S3 Text §9. Stated. As
VT2-6.

**VR-17** (note). In the dispositions file the heading of R33 lacked "(also T38)", the only one-sided cross-reference
among the headings. Corrected. The heading reads "R33 — minor (also T38)".

### VT1: the dispositions of the audit of the text, T01–T31

**VT1-1** (error). The record's entry gave the leave-one-out range of the sts slope as 4.14 to 4.54 (the upper end is
4.5346). Corrected. As VT2-4: "(4.263: 4.139 to 4.535)".

**VT1-2** (inexact). The record's paragraph on the figures did not name one drawing change that the script makes, the
anchor of Fig 5c's legend. Corrected. The paragraph names it ("its legend's anchor at −0.25 of the panel's height for
−0.42, which keeps the legend about as far below the taller panel") and, of Fig 3c's legend, that its entries are 6.5
pt for 6.8, its title staying 6.8; the script's revision note says the same. Found also by VE-21.

**VT1-3** (inexact). The disposition of R19 and the record's disposition of A's m8 gave "the sts surface of Fig 1a" as
the words of the list's entry of S3 Text, which reads "the sts surface over (r₁, q)". Corrected. Both give each place
its words: "the sts surface of Fig 1a" in the Discussion and in the list's entry of S20 Table; "the sts surface over
(r₁, q)" in its entry of S3 Text. Found also by VR-10.

**VT1-4** (inexact). The disposition of T03 said that two dispositions of the record call the reason B offered not so;
one of them does. Corrected. "The disposition of B's MINOR 3 (a) says that the reason B offered was not so, and that
of A's m9 that the windowed atoms are committed".

**VT1-5** (inexact). The note of the numbers table's row for the 366 excluded draws kept the wording that T26 had
found inexact ("either half's reliability not positive"). Corrected. The note: "B21 (d): draws excluded (those in
which the split-half reliability of the sts DiD or of the r₁ DiD is not positive)". Found also by VR-6.

**VT1-6** (inexact). S4 Text Sh3 kept, unqualified, "every result table with its git SHA", the statement that T17 (i)
had found inexact in Data and code availability. Corrected. Sh3: "the result tables and reports with the producing
commit in their headers (S5 Text §4 lists the files that carry none or a marked one)". Found also by VR-7.

**VT1-7** (note). Methods says that S19 Table gives the status of each computation; two sets of exploratory p values
that the main text quotes have no row there (B27's values known before its run; the residual's exact p against its
three expectations, B21 (b)). Corrected. S19 Table's head note says so and why: "Two sets of values have no row of
their own, because their pre-run entries list them as known before the run and their outcome entries report them as
reproduced, not predicted", naming both sets and where the main text has them.

**VT1-8** (note). S4 Text S6 said that every post hoc or review computation is labelled at first mention, which does
not hold of the main text's first mentions. Corrected. S6: "the supporting texts say of many post hoc or review
computations, where they report them, that they are such, and the main text repeats the status for several (Methods,
The primary contrast and the exploratory analyses); S19 Table's Part B gives the status of each". A first correction
said that the supporting texts label every such computation, which does not hold of every one (W3-3), and a second
that the complete list is S19 Table's, which was two computations short (X1-2). Found also by VS-6.

**VT1-9** (note). The caption of the residual table in S3 Text §6, moved unchanged, has −0.74 per unit of pair r₁
without the marking that the value carries elsewhere. Corrected. The caption stays as moved, and a sentence under the
table says what the value is: "the ratio of the two means that the table's data row prints, +0.0115 / −0.0155 (the
pair r₁ DiD is saved at four decimals)".

**VT1-10** (note). Two phrasings stood unqualified beside corrected ones: the head note of the supplementary tables
did not name S18 Table's new part, and the heading of Results 6 keeps "nearly flat in r₁", to which the Abstract now
adds "on the family". Corrected. The head note: "the results of B21–B24 and of B28 (S18 Table)". The heading is kept:
it is the committed one, and the section's second sentence says on what the flatness is shown ("On the symmetric AR(1)
family at fixed q it is nearly flat in r₁") before it turns to the data.

### VT2: the dispositions of the audit of the text, T32–T63

**VT2-1** (inexact). The disposition of T37 quoted one phrase for S5 Text §5 and §6; the phrase is §5's, and §6 words
it differently. Corrected. The disposition quotes each: §5, "the caption of what was then Table 3 (the residual table,
now in S3 Text §6)"; §6, "the caption of what was then Table 3, now the residual table of S3 Text §6".

**VT2-2** (inexact). README.md's row for `notes/` still called the table whose caption was corrected on 1 October
"Table 3". Corrected. "the correction of the then Table 3's caption with its checks and audit (`review_2026-10-01/`)";
CLAUDE.md's list of the folders has the same words (VB-30).

**VT2-3** (inexact). The disposition of R22 placed the leave-one-out of the sts slope in item (v) of "B27, outcome",
which states the assumptions only. Corrected. The disposition now says that the entry "B27, outcome" states the
assumptions in its item (v) and the leave-one-out in its paragraph on the sts rows. Found also by VR-11.

**VT2-4** (error). The record's entry gave the leave-one-out range of the sts slope as 4.14 to 4.54; the upper end is
4.5346, and 4.54 was a second rounding of the printed 4.535. Corrected. The entry, in its disposition of B's MINOR 9:
"(4.263: 4.139 to 4.535)", the three decimals of S3 Text §5 and of `derived_r24.out`, item 8. Found also by VT1-1,
VE-1 and VR-1.

**VT2-5** (inexact). The disposition of T58 (ii) quoted for Fig 3's caption the words of Results 4. Corrected. It
quotes each: Results 4, "ratios of means under one change of r₁"; Fig 3's caption, "each a ratio of means under one
change of r₁".

**VT2-6** (inexact). The disposition of T61 (iii) and the record's disposition of A's w1 listed where "artefact" stays
and left out a second, unquoted use in S3 Text §9 ("not an artefact of scale"). Stated. The sentence of S3 Text §9 is
committed text. It uses the word to deny it of a part of the change in r₁: residualising a contrast on the ratio of
window variance to run variance would remove the part of the r₁ change that coincides with the variance change, "not
an artefact of scale". The paper therefore nowhere calls the change in r₁ an artefact, and the sentence is kept. The
record's disposition of A's w1 and the disposition of T61 (iii) now name it and say what it says (W2-7, W4-3). Found
also by VE-14 and VR-16.

**VT2-7** (note). The levels of the diagnostic on the series whitened at p ≤ 5 (0.2766, 0.2438, +0.0328) are means
over both runs and all windows; S3 Text §8 and S11 Table said so for p = 10 and 20 only. Corrected. S3 Text §8 and S11
Table's line on that diagnostic: "its levels are means over both runs and all windows, where the table's level,
0.2202, is the DMT pre-injection mean".

**VT2-8** (inexact). Three "reported at" cells of S19 Table's Part A omitted a place where the revision newly reports
the item (B7; B19 (c); B16c (e)). Corrected. B7: "Discussion; S3 Text §6; S5 Text §1 (the deviations)". B19 (c):
"Abstract; Results 2; Discussion; S3 Text §5; Fig 3". B16c (e): "Results 7 (what the AR(1)-substituted estimate
carries of the contrast at p = 20); S11 Table; S3 Text §8".

**VT2-9** (inexact). The record said that the dispositions assign to the note to C.T. and S.P.S. every item of its
list; five of the items are assigned by no disposition. Corrected. The entry's last paragraph names the dispositions
that assign items to the note (A's M2; B's MINOR 7; C's M1, M2, M4, m1, m4 and m17) and the five items "that no
disposition assigns and that are added here". The disposition of C's m4 now names the note. Found also by VE-9.

**VT2-10** (note). A bullet of CLAUDE.md dated 15 September 2026 keeps "spin p < 0.0001". Kept. The bullet is part of
the file's dated history and records what was written that day. The paper's files have "p < 1/10,000"; CLAUDE.md's
account of this revision does not give the spin p (W5-1).

**VT2-11** (note). The record's disposition of B's W1 gave S19 Table's row the clause "no rotation reaching the
observed value", which the row does not have. Corrected. The disposition separates the places: "Results 3, S3 Text §4
and S5 Table's note: p < 1/10,000, no rotation reaching the observed value; S19 Table's row: p < 1/10,000". Found also
by VE-12.

**VT2-12** (note). The record said that the Use of AI tools statement "says the same as before in fewer words"; the
statement now also speaks of a second occasion on which a session computed on the data. Corrected. The disposition of
C's M2: the statement "keeps what it said, in fewer words", and "adds the second occasion on which a session computed
on the data, that of the text audit".

**VT2-13** (note). S20 Table's row 10 (Gao et al., 2026) holds three quoted phrases and three details that the claim
record did not have. Corrected. The claim record's section on Gao et al. (2026) gives each with its page, read again
in the PDF: "persistent synergy", "persistent redundancy", "the Gaussian MMI solver" and "246 x 246" (p. 3), the work
the paper follows, its reference 10, which is Luppi et al. (2022) (p. 3), and the "t-statistic patterns" with r =
0.942 (p. 4).

**VT2-14** (note). 175 rows of the numbers table carry a locator in a notation that the head note did not explain
("@La-b|", "@pct|", "bound on"). Corrected. The head note explains the three: "@La-b|" before an anchor says that the
row's line is one of lines a to b of the file (the rows of a table, with or without its head, or a single line), the
anchor being on the row's line; "@pct|" marks a value that the text prints as a percentage; "bound on" precedes the
value on the line for which the printed bound holds. The planning session's preparation of the table tests the anchor
of each of these rows on its line, as it tests the held string; the committed `check_numbers.py` tests the held string
of the data rows (W6-4, W6-19).

**VT2-15** (note). The heading of table (a) of the censoring tables in S3 Text §5 could be read as giving the mean
framewise displacement of the marked TRs; it is the run's. Corrected. "(a) TRs above the threshold per run (count and
share of the run's 840 TRs), the run's mean framewise displacement over all its TRs, ...".

**VT2-16** (note). The table of B28 in S3 Text §6 and in S18 Table gives "mean ± SD" without the divisor, which Table
3's caption now states. Corrected. Both say "the SD with divisor 100": S3 Text §6 in the paragraph that precedes its
table, S18 Table in its source line.

**VT2-17** (note). The row of `derived_r24.out` in S19 Table's Part B missed one quotation in its glosses (the
Discussion's cross-half r) and placed the regional relation on the windowed atoms in the Discussion as well as in
Results 3. Corrected. The row: "Abstract and Discussion (the mean cross-half correlation at two decimals, in the
Abstract with its Fisher-z interval), ... Results 3 (the regional relation on the windowed estimator's own atoms), the
Discussion (rtr's slope on regional r₁; the fifth again), ...".

### VC: the dispositions of the audit of the citations (C01–C25) and the claim record

**VC-1** (inexact). Three pointers of the claim record (the Reporting Summary's item, an item of Timmermann et al.,
2023, and one of Singleton et al., 2025) left out S3 Text §5, which states the replacement of volumes and cites the
three documents. Corrected. Each of the three pointers names S3 Text §5.

**VC-2** (inexact). The claim record's second item on Liardi et al. (2025) said that S3 Text §10 states that no
application of ΦID to psychedelic data was found, and its details are in neither place it named. Corrected. The item
says what each place holds: the Discussion gives the study as a PID on MEG under the three drugs where it says that no
application was found; S3 Text §10 gives the number of the authors and their relation to the ΦID paper's, and ΦID as a
possible further generalisation (W7-10); the other details stand in the note on the second search and in the
literature file.

**VC-3** (inexact). The disposition of C21 gave one quotation for S1 Text and S4 Text D6; the words are S1 Text's.
Corrected. The disposition quotes each: S1 Text, "collected in scan runs other than the analysed ones, in the second
scanning session"; S4 Text D6, "collected in other scan runs, in the second scanning session".

**VC-4** (inexact). The paragraph on Murray et al. (2014) in the dispositions called the restored sentence of Results
3 "the committed one"; only its clause on the three works is. Corrected. The paragraph says that the clause on the
three works is the committed one and that "In the literature", at the head of the committed sentence, is dropped, as
the reason recorded with the replacement says.

**VC-5** (inexact). The reason recorded with a replacement in S3 Text §10 said that the authors of Liardi et al.
(2025) include four of the seven of Mediano et al. (2021), "not its first author", which reads as untrue of Mediano.
Corrected. The reason: "the six authors of Liardi et al. (2025) include four of the seven authors of Mediano et al.
(2021), Mediano among them; the first author of Liardi et al. is not one of the seven". Found also by VB-26.

**VC-6** (inexact). The claim record's header said that a page is the page of the PDF as saved; for three works the
pages given are the journal's. Corrected. The header: "for Barnett & Seth (2011), Seth et al. (2013) and Strassman &
Qualls (1994) it is the journal's page, which those PDFs print (their first pages are pp. 404, 540 and 85)".

**VC-7** (inexact). The claim record placed the statement of Theorem 1 of Rosas et al. (2020) in S20 Table's row 2,
which only names the work for the quantity. Corrected. "Stated in S3 Text §11; the main text's Results 6 and S20
Table's row 2 cite the work where they name the emergence capacity".

**VC-8** (note). The disposition of C14 said that the reasons recorded with two replacements both note that the
paragraph of Luppi et al. (2022) begins on PDF p. 14; one of them did not. Corrected. Both reasons now have it: "the
paragraph begins on PDF p. 14 and the sentence quoted ... is at the head of p. 15".

**VC-9** (note). Two statements that the revision makes about cited works had no item or no place in the claim record:
the exclusion criteria that S4 Text D3 and D4 cite to both source papers, and the Introduction's clause on Luppi et
al. (2022). Corrected. The claim record has an item on the exclusion criteria (Timmermann et al., 2023, p. 9;
Singleton et al., 2025, p. 8), and its section on Luppi et al. (2022) gives PDF p. 2 for the Introduction's clause.

### VN: the statements about cited works that the audit of the citations had then left unchecked

**VN-1** (inexact). Five page ranges in S20 Table's row 5 (Luppi et al., 2026) ran past, or started before, the pages
that hold the facts. Corrected. Each is narrowed to those pages, in S20 Table and in the literature file: the human
acquisition "(pp. 37–38)", the macaques', the marmosets' and the mice's "(p. 38)", the parcellations "(p. 39; the
region counts also on p. 21)". The second form of the citations audit's report had noted that five page ranges of the
row are wider than the pages that hold the facts, without listing them (the part above on the points it raised outside
its findings). The claim record's item on Luppi et al. (2026), written with these corrections, gives the page of each.

**VN-2** (note). The same row glossed the third human session as "3 vol% (burst suppression)"; the PDF prints "3 vol%
burst-suppression", and the gloss chose one of two readings. Corrected. The cell quotes the PDF's words, "3 vol%
burst-suppression", and keeps what the pages say of the number of sessions and levels (pp. 37, 35 and 3) without a
reading of its own.

**VN-3** (note). The row's cell on HRF deconvolution, "not mentioned in the main text", was narrower than the PDF
supports, and the reason recorded with its two replacements spoke of a removal. Corrected. The cell: "HRF
deconvolution not mentioned in the article, its Extended Data or its Reporting Summary", followed by "(the PDF read,
whose pp. 1–26 are the article, pp. 27–32 the Extended Data and pp. 33–41 the Reporting Summary; the Supplementary
Methods the article defers to were not read)" (the pages of the three parts since the fourth check: Y4-3). The row's
last cell says the same of what was read and, since the second check, of the Supplementary Methods too (W5-9). The
reasons recorded with the two replacements say what the cell now states (VB-6; C31).

**VN-4** (note). The screening file's page for the phrase quoted from Pope et al. (2025), "its p. 3", is the PDF's
third page, which the article numbers 2. Corrected. "(PDF p. 3, the article's p. 2, where the paper also names the
local measure as the one it chooses; the section that derives it begins on PDF p. 5 and its formula is on PDF p. 6)",
and the file says that a page given in it is the page of the PDF as saved. The audit of the citations raised the same
in its second form (C28), with the point that the phrase describes the O-information. The pages of the local measure
are as the second check read them (W7-6).

**VN-5** (note). Not checked: V.S.'s copy of Down et al. (2026) holds pages 1–25 of 55, so that the two negatives of
S20 Table's row 6 (global signal regression, deconvolution) hold for those pages only. Corrected. Row 6, in S20 Table
and in the literature file, says so: "both negatives are of the main text and its references (pp. 1–25 of the
preprint's 55 pages), the supplementary materials, to which the paper refers for its fMRIPrep output (p. 4), not
having been read"; its last cell reads "Within scope as far as the main text states". The planning session has asked
V.S. for the complete file; nothing in the paper waits on it.

**VN-6** (note). Not checked: the S1 Appendix of Liardi et al. (2025) is a separate file. One observation: in the
data-driven variant the null systems are not "otherwise random", the words of S3 Text §10, which are those of the
primary construction. Corrected. S3 Text §10: "(their p. 7; in the data-driven variant of their pp. 20–21 the null
systems keep the coefficient matrix estimated from the data)"; the claim record has the item. The appendix is not
cited for anything.

**VN-7** (note). Not checked: the session had no PDF of Varley et al. (2024), *Network Neuroscience*, which the note
on the second PubMed search describes in three places. Kept. The audit of the citations had the PDF for its second
form and checked the three descriptions against it (`findings_citations.md`, "Checked and found exact", check 4: the
title and the bibliographic line, the preparation and the drug, the three measures, no ΦID). It raised C30 on another
sentence of the note, which is corrected.

**VN-8** (note). "Schaefer-100 parcels (released with Schaefer et al., 2018)": the article names the resolutions of
400 to 1,000 parcels and a public multiresolution release, not a 100-parcel resolution. Kept. The sentence is the
committed one and says what is the case: the 100-parcel resolution is part of the public release that the article
announces (its p. 1), and the repository carries that release's label file
(`data/Schaefer2018_100Parcels_7Networks_order.lut`, under the release's licence).

**VN-9** (note). S3 Text §11's paraphrase of Theorem 1 of Rosas et al. (2020) dropped the theorem's order k.
Corrected. "a system has a causally emergent feature of order k if and only if the k-th-order synergy of its parts
about its future is positive".

**VN-10** (note). S20 Table's row 2, last cell, on the two validations of Luppi et al. (2023): the finding reports the
statement exact and adds where the paper's nearest statement is. Kept. Nothing to change; the cell says that the paper
does not state the combination.

**VN-11** (note). In the references cited only in S20 Table, the entry of Luppi et al. (2025) had "Menon, D." for the
preprint's "David K. Menon". Corrected. "Menon, D. K.", as in the main text's entries.

### VM: the main text

**VM-1** (inexact). Methods listed the places where the text marks a computation as post hoc or as a recorded
prediction; the list left out four. Corrected. The sentence no longer lists them: "(the text repeats it for several)".
A first correction had named the sections there, and the list of sections left out Methods itself (W1-1). The record's
disposition of B's MINOR 8 names the places: the quantities marked post hoc, and those said to rest on a rule or a
prediction recorded beforehand, in Results 3 and Fig 4's caption, the Discussion, Methods and Limitations (W1-2).

**VM-2** (inexact). Results 3: "the interval admits up to half of it"; the interval's lower limit, −0.0110, is 0.54 of
the contrast of −0.0202. Corrected. "the interval admits just over half of it (Fig 4b)".

**VM-3** (note). Results 2 supported "the DiD's between-subject variance is mostly the gap's" with r² = 0.79 first; r²
does not apportion the variance, and only the comparison of the SDs carries "mostly". Corrected. The parenthesis leads
with the SDs: "(the DiD's SD 0.0887 against the post-injection gap's 0.0485; r(DiD, pre-injection gap) = −0.888, r² =
0.79)", each SD with the quantity it is the SD of since the second check (W1-3). S3 Text §5 says in what sense
"mostly" is meant, with the parts of the DiD's variance (the post-injection gap's 0.30, the pre-injection gap's 0.35,
the covariance term's 0.35: `derived_r24.out`, item 9) and that these are not an apportionment.

**VM-4** (note). Results 4 gives the ramp's differences from the step as 0.0001 and 0.0006 nats; Table 3's printed
cells differ by 0.0002 and 0.0007. Corrected. "by 0.0001 and 0.0006 nats from the step (unrounded means)"; "B28,
outcome" (c) gives both pairs of values.

**VM-5** (note). Results 4 said that the residual's per-subject relation holds across split halves on the primary
variant and not on the sensitivity variant; on each variant one of the two cross-half correlations is clearly
negative. Corrected. The sentence gives the four values without a verdict: "the per-subject relation's cross-half
correlations are −0.700 and −0.385 on the primary variant and −0.598 and −0.051 on the sensitivity variant (S3 Text
§6)". S3 Text §6 sets them against their ceilings (`derived_r24.out`, item 10).

**VM-6** (note). Results 2 and Fig 3's caption use "the AR(1) pairs" and "the band-passed generator" before Results 4
introduces them. Corrected. Results 2 points forward: "(Results 4; S13 Table)". Fig 3's caption is kept: it names the
source of each generator's rate where it gives it (S18 Table; Methods).

**VM-7** (note). The Author summary's last sentence named the regions' autocorrelations as the estimate's inputs; the
estimate also uses each pair's lag-0 correlation. Corrected. "the estimate our closed form gives from each pair's
autocorrelations and correlation", within the 200 words.

**VM-8** (inexact). Five titles in the main text's list of supporting information are not word for word those of the
supplementary tables' file (S1, S9, S17, S18 and S20 Tables), and the entry of S5 Text did not name its section 3.
Corrected. S20 Table's title in the file now has the list's words ("the reading of each on the sts surface of Fig
1a"), and the entry of S5 Text names "the decisions of 20 September 2026". The other four are kept. The file's titles
carry what the list's entries leave out: the bins beside the windows (S1), a pointer to S3 Text's section and a time
of day (S9) and computation labels (S17, S18). Times of day and computation labels the main text does not use; bins
and section references it does use, and the list's entries give those two titles without their parentheses. The
contents are the same (W1-4, W3-6).

**VM-9** (note). The committed figure files and `captions_v2.md` are those of the previous revision, so that five
captions and two drawings differ from the main text's. Kept. By design: the figures and captions are regenerated at
the commit of the text and committed in the one that follows, under the conditions that the record's paragraph on the
figures lists and `checks/figures_check.py` tests; S5 Text §6 says in which commit they are.

**VM-10** (inexact). In the numbers table, locators of three groups of rows led to a line that does not hold the
number (rows citing the record's line 189; rows citing line 6 of `family_atoms_tables.md`; one bound row's held
value). Corrected. The rows of the window sets and of N = 14 cite a line that holds them (line 4 of
`family_atoms_tables.md`; the record's line on the window sets, for the four rows of Table 2's caption; the record's
line on the shape of the data), the coverage "95" of the three captions is a label, and the bound row holds 6.7e-16;
the table's head note lists these corrections. As VB-20 and VB-23.

### VS: the supporting information and the literature file

**VS-1** (inexact). S3 Text §5 and §6 put one date, 1 October 2026, after a pre-run entry and its outcome entry (B27,
B29, B28). Corrected. As VO-4: the date follows the pre-run entry's title alone.

**VS-2** (inexact). S3 Text §8 dated the computation at the fixed orders "1–2 October 2026"; the run lies wholly on 1
October in UTC, the date that S5 Text §4 and the main text give. Corrected. "The atoms at fixed orders p = 10 and p =
20 were computed on 1 October 2026".

**VS-3** (inexact). S19 Table's row of B24's expectations named Results 4 among the places that report it; Results 4
no longer carries any of the row's values. Corrected. The cell: "S3 Text §6 (its residual table, last column, and,
under the next heading, the text and the table of the aligned and directed statistics); S18 Table", the places within
S3 Text §6 as the second check found them (W3-2).

**VS-4** (inexact). S19 Table's rows B28 (a) and (d) named places that hold part of what the rows report: the main
text gives the slopes but not the ratios they are compared with, and S18 Table has no column for the shares of r.
Corrected. Row (a): "S3 Text §6; S18 Table (the two slopes also in Table 3 and Fig 3c)". Row (d): "S3 Text §6; S18
Table (the sts DiDs and the coverage)".

**VS-5** (inexact). S4 Text R1 said that the contrasts of the data carry inverted sign-flip intervals and exact p and
listed the exceptions; the two baseline-adjusted contrasts of Table 2 are regression intercepts with t intervals and
no p, and were not among them. Corrected. R1 adds: "the baseline-adjusted contrasts of Table 2 are regression
intercepts, with t intervals and no p".

**VS-6** (inexact). S4 Text S6: "every post hoc or review computation is labelled at first mention" does not hold of
the main text. Corrected. As VT1-8.

**VS-7** (inexact). S18 Table's source line for B28: "No data but the subjects' whole-brain r₁ DiDs"; the script reads
two further committed quantities derived from the data. Corrected. As VO-1: the source line names the r₁ DiDs, the
residual DiDs and the pool of the data's window-level pair q.

**VS-8** (note). S3 Text §6 and §8 said that the cold reads of the methods and the statistical reviewer asked for the
two computations; the statistical reviewer's asked for each, and the methods reviewer's raised the neighbouring point.
Corrected. §6: the statistical reviewer's read asked for the generators' own slope, "and the methods reviewer's, which
called the per-subject slope the right comparison, for a change that builds up inside the windows". §8: the
statistical reviewer's read asked for the atoms at those orders "(the methods reviewer's found prewhitening presented
one-sidedly)".

**VS-9** (note). Three "reported at" cells of S19 Table held in part (B17b; B27 (b); B27 (c)): the main text carries
some of each row's values and not others. Corrected. Each cell says what the place holds. B17b: "S3 Text §7; S10 and
S13 Tables (the main text quotes this sts DiD as B24 reproduced it: the row of B24's check)". B27 (b): "Results 2 and
Table 2 (the adjusted contrast); S3 Text §5". B27 (c): "Results 2 (the post-injection gaps' correlation); S3 Text §5".

**VS-10** (note). S5 Text §4 listed three of the values that the text audit computed on the released series; its
report quotes five more. Corrected. The paragraph lists all eight: the mean per-subject regional slope with its mean
r², the three group means, the ratio of the last to the first, and the slope on the pair r₁ DiD with its interval and
r. None is used in the paper.

**VS-11** (note). S19 Table's row B29 (d) and S3 Text §5 gave the check of the non-finite TR as confirmed without
saying that the script reads ts_gsr for it. Corrected. S19 Table's row: "confirmed on ts_gsr, the variant the script
reads for this check"; S3 Text §5 has the same words, with the variant's name in code type. Found also by VR-12.

**VS-12** (note). One cell of B27's table (a), which S3 Text §5 and Table 2 carry, does not recompute from the
committed per-subject file: the exact p of r₁'s pre-injection gap on ts_demean at W = 60 is 0.1871 in the run's table
and 0.1873 from the six-decimal file. Stated. The paper prints the run's value, which the run computed from the
unrounded values. S3 Text §5 says so under the table, with the counts of sign assignments (3,066 and 3,068 of 16,384)
and the two assignments, with their mirrors, that the file counts by a margin smaller than its rounding can move, the
run's count being one such pair fewer; `derived_r24.py` recomputes all 120 cells of table (a) from the file and
reports the one that differs (item 11 of its output). The note first spoke of three assignments within 10⁻⁶, which is
not the bound that the rounding sets here (W2-5).

### VB: the numbers table, the replacements file, the bookkeeping files and the checks' outputs

**VB-1** (error). `numbers_update.out` placed the data's change of A_other and its interval, taken out of Results 4,
in S3 Text §6 and S18 Table; S18 Table holds the generator's values, not the data's. Corrected. The three lines give
"S3 Text §6". The reason recorded with the replacement says which of the values S18 Table holds (the constructions'
full results and the expectation under a pure autocorrelation change).

**VB-2** (error). The intervals of the two cross-half correlations were placed in Fig 3b as well as in S3 Text §5, in
`numbers_update.out`, in the reason recorded with the replacement of Results 2's paragraph and in the record; Fig 3b
and its caption carry the two correlations only. The same reason placed −0.0944 and 0.0154 in the Discussion, which
has −0.094. Corrected. The list gives "S3 Text §5" for the four limits; the reason says that the two correlations are
in S3 Text §5 and Fig 3b's caption and their intervals in S3 Text §5, and that the Abstract and the Discussion give
the generator's change as −0.094; the record: "the two cross-half correlations (S3 Text §5; Fig 3b), their intervals
(S3 Text §5)".

**VB-3** (error). The numbers table's row for the 10,000 bootstrap draws (Results 2) named a file and a line that do
not hold the setting. Corrected. The row cites `notes/partB21_inference_revision.py`, line 82, anchor "N_BOOT =
10000".

**VB-4** (error). The reason recorded with the Abstract's replacement gave the interval's lower limit as 0.258077; the
file has 0.258078. Corrected. "(`derived_r24.out`, item 6: [0.258078, 0.894889])".

**VB-5** (error). The reason recorded with a replacement in Results 1 placed the pair-averaged response in part (b) of
S18 Table; it is in part (a). Corrected. "from S18 Table's part (a), row (a3), which the residual table of S3 Text §6
also holds".

**VB-6** (error). The reasons recorded with the two replacements of the cell on HRF deconvolution (S20 Table's row 5
and the literature file) named C's M5 (b) and a removal; the change answers C's M4 and narrows a statement. Corrected.
Both reasons name C's M4 and say what the cell now states and what was not read. The audit of the citations raised the
same in its second form (C31).

**VB-7** (inexact). `numbers_update.out` classed two deleted rows as "re-created" in their paragraph whose quantity is
no longer there (the 14 of the leave-one-out refits in Results 2; the 1 of "in 1–5" in Results 7). Corrected. The
first is listed with the numbers that the rewritten sentences no longer state (the count of refits), the second as
moved to Table 4's caption, where the range now is; four rows remain in the class of numbers still in their paragraph.

**VB-8** (inexact). `numbers_update.out`'s list of the tokens without a row accounted for 191 of 203 and counted the
dates' years among the citation years. Corrected. The file counts each kind apart: 95 citation years; the day numbers
and the years of the dates; the cross-references of the running text and the captions; the ten numbers of the
captions' own heads; the DOI; and it says that the digits of commit identifiers and the numbers inside code spans are
not tokens of the text. The counts are those of the planning session's pass over every number token of the text when
it prepared the table. That pass left the ten references to a figure's panel, as in "Fig 1a", out of every count until
the second check found them missing (W6-1).

**VB-9** (inexact). "A new row with its source file, line and held string", and the record's "each with its source and
line", are true of the data rows only. Corrected. As VE-3.

**VB-10** (inexact). Two glosses of `numbers_update.out` were not exact: the 10 of 10⁻¹⁶ described as of the full run,
and the Discussion's sentence said to name no TR. Corrected. The first as VE-13. The second: "the clause 'the exposure
is not specific to TR 2 s data' is not carried; the sentence keeps that the exposure is almost the same at every TR".

**VB-11** (inexact). The table's head note named S3 Text among the files whose edits moved 17 locators; none of the 17
points into S3 Text. Corrected. "the edits of supplementary.md, the literature file and the figure script";
`numbers_update.out` gives the count for each file (5, 1 and 11).

**VB-12** (inexact). The head note sent all 69 numbers "taken out of their paragraph" to the supporting information, a
table or another paragraph; four went to none of these. Corrected. The class is divided: 64 rows of numbers that are
now at another place, and 7 of numbers that the rewritten sentences no longer state and that are at no other place in
that form, each listed with what became of it (the four the finding names, the count of refits of VB-7, a second
mention in Table 1's caption and a clause of the Discussion that is not carried).

**VB-13** (inexact). The row of "0.0000" in Results 1 was a label row, though it sits on a value that Table 1 prints.
Corrected. It is a data row on the line of `family_atoms_tables.md` that holds +0.0000 for xty, its note naming the
two other atoms whose substituted DiD prints as −0.0000.

**VB-14** (inexact). The reason recorded with the Abstract's replacement said that the excess is printed at the
table's four decimals; the Abstract prints it at three. Corrected. "the excesses as a range at three decimals, the
detectable difference at the table's four".

**VB-15** (inexact). Three reasons said "condensed for the word limit, no statement removed" of replacements that drop
clauses (two of the Discussion, one of Methods), and one quoted words that are in neither the new text nor the
finding. Corrected. Each of the three reasons names the clauses: two that Results 1 states and that are not repeated;
two that Results 2 and Methods state and that are not repeated; and a clause on the null that is dropped from Methods,
the fall it spoke of staying in the sentence. The first reason quotes the committed and the new wording as they are.
The other reasons that said "no statement removed" were read again against their replacements; one more (Results 4's
opening sentence) now names the gloss that is not repeated.

**VB-16** (inexact). The reason recorded with the replacement of Data and code availability said that S5 Text §4 holds
every detail removed; three kinds of pointer are not there. Corrected. The reason lists what S5 Text §4 holds and the
three kinds that are elsewhere: the two outputs of derived numbers (S3 Text §4 and §5; S19 Table's Part B), the names
of the review folders (S5 Text §5) and the calibration scripts, which the committed sentence gave as a range and two
names (the sentence now has `notes/partB*.py`); the reason's words on the folders and the scripts are those that the
second check corrected (W6-2).

**VB-17** (inexact). The reason recorded with one replacement of the reference list named one reference; the
replacement adds two. Corrected. "References added: Schartner et al. (2017) and Seth, Chorley & Barnett (2013), which
follow each other in the list".

**VB-18** (inexact). The reason recorded with the replacement of Table 1's caption called A's point on the TDMI row
the last of its finding; it is the second of four. Corrected. "A's m10 (its point on Table 1's TDMI row)".

**VB-19** (inexact). CLAUDE.md's "Remaining work" asked to check that the sentence of Data and code availability on
the final run still describes "its outputs in the commit that follows"; the sentence no longer says where the outputs
are. Corrected. "(at c25a310; where its outputs are committed is now said in S5 Text §4)".

**VB-20** (note). Committed design rows, carried by the revision, cite a line that holds the anchor but not the
setting (line 6 of `family_atoms_tables.md`; line 189 of the record; two single rows). Corrected. Thirteen rows of the
window sets and of the 14 subjects cite line 4 of `family_atoms_tables.md`, which states them; the five rows of Table
2's caption cite the record's lines on the window sets and on the shape of the data; the rows of the name AR(1), of
"95 %" and of "lag-1" that were design rows on such lines are label rows; the row of "BIC over 1–5" cites the line of
`prewhiten_tables.md` that states the range. The head note and `numbers_update.out` list these, 37 committed rows in
all with those of VB-21 to VB-23 and VR-2; the planning session's preparation of the table stops if the count of any
kind differs.

**VB-21** (note). Five committed label rows carry a note about another token of their sentence. Corrected. Each note
now describes its own token.

**VB-22** (note). One row has the number 1.7 where the text's token is 1.7.0 (the version of rsHRF), the only row not
on a whole token. Stated. The row is kept on the token as the committed table has it, and its note says so: "rsHRF
version 1.7.0: the row sits on the token 1.7 of 1.7.0".

**VB-23** (note). The held string of the five bound rows is "bound on X", of which only X is on the line; one of them
held 5.6e-16 where its note names 6.7e-16, the value that the printed bound bounds. Corrected. The head note explains
the notation (VT2-14), and the row holds 6.7e-16.

**VB-24** (note). Nine number tokens of the headings have no row and were not among the kinds that the head note
excepts. Corrected. The head note and `numbers_update.out` name the headings and the captions' own heads among the
kinds without a row (VE-4).

**VB-25** (note). The head note's list of the sources of the added rows left out the record, the scripts and the files
of the two PubMed searches. Corrected. "to the committed tables, scripts and lines of the record they quote, to a
committed log, to the supporting information where it holds the value (S3 Text; S2, S6, S15 and S18 Tables), to the
files of the two PubMed searches and to the claim record of the source papers", the log and the supporting information
added after the second check (W6-14).

**VB-26** (note). The reason recorded with a replacement in S3 Text §10: "not its first author" is true of Liardi et
al.'s first author and reads as said of Mediano. Corrected. As VC-5.

**VB-27** (note). CLAUDE.md: "each table and figure caption in the text after the paragraph of its first citation";
Table 3 is first named in Fig 3's caption, before the paragraph that cites it. Corrected. "after the paragraph of its
first citation in the running text (Table 3 is named before that in Fig 3's caption, twice)" (W6-10).

**VB-28** (note). CLAUDE.md's condition on the PDF files of Figs 2, 4 and 6 named the dates only. Corrected. As VR-5.

**VB-29** (note). CLAUDE.md, in text the revision had not changed: "Every interval of a mean over subjects is B21's
inverted sign-flip interval"; the main text has two means over subjects with a percentile interval, each named as
such. Corrected. "Every interval of a mean over subjects whose per-subject values are saved is B21's inverted
sign-flip interval", with the others named: the subject-bootstrap percentile intervals of Results 3 and of the
Discussion's Lempel–Ziv check, and the t intervals of Results 3's regional contrast.

**VB-30** (note). README.md and CLAUDE.md still said "Table 3's caption" for the correction of 1 October and named one
PubMed search for the review folder, which holds two. Corrected. Both files: "the correction of the then Table 3's
caption" and "the PubMed searches of 1 and 2 Oct".

**VB-31** (note). "8,498 words with headings" is the output of `wc.py`, which counts the `##` or `###` of a heading
line as a word; without the 29 markers the count is 8,469. Stated. The count stays the one the limit was set in. The
record's paragraph on the checks says what it is: "as `wc.py` counts them, the `##` or `###` of each of the 29 heading
lines as a word, which is the count the limit was set in". The two numbers are those of the tree that the check read;
since the corrections that followed the second check the output is 8,489 words with headings, 8,460 without the 29
markers.

**VB-32** (note). The review folder's README said that each replacement's `why` names the finding or the rule it
answers and, where a sentence was condensed, where its statements now are; 70 of the reasons name neither a finding
nor a rule. Corrected. The README: each has a `why`, "the finding of a read, the finding of an audit or of a check, or
the rule of an entry that it answers, or, for the replacements that answer none of these (the references, the
renumbered rows, the figure script, the bookkeeping files, the condensations), what it does"; where a statement leaves
the main text, "its `why` or the record's entry on the revision says where the statement now is".

**VB-33** (note). A note on the figures of the later commit: in the session's environment, which is not the pinned
one, Figs 2, 4 and 6 come out a few pixels different in size, so that their conditions could not be judged there.
Kept. The conditions are tested on V.S.'s machine in the pinned environment (VE-22); no replacement touches the
drawing code of Figs 2, 4 and 6.

### Found while the findings were settled

Five things that no session of the ten had raised were corrected with their findings. (1) S19 Table's head note said,
in committed text, that the values which the pre-run entries of 23 September 2026 mark as already known, "B21 (b) and
(c); the reproductions in B23", are not counted as predictions. The rows of B23 are counted: each has a verdict in its
outcome entry and is among the 67. The head note now says so (B23 recomputed each value on its own pool and design),
and names the two sets of values that have no row because they were known before their run: B21 (b) and (c), and the
values of B27 that follow from committed per-subject values (VT1-7). (2) In the entry of Luppi et al. (2025) among the
references cited only in S20 Table, "Legare, A." became "Légaré, A.", as the preprint prints the name, with the
correction of the same entry for VN-11. (3) The heading of S3 Text §3's paragraph on the transfer entropies says
"(written for the revision of 1–2 October 2026)" where it had the two dates alone. (4) The source lines of S11 and S18
Tables give the date with the pre-run entry alone, S18 Table's after the entry's title and S11 Table's, which has no
title, after the words "pre-run entry", as the three places of S3 Text do for VO-4. (5) S19 Table's row B27 (a) names
Table 2 among the places that report it, with the three cells corrected for VS-9. The second check found (2) to (5)
named in no disposition (W5-4).

## The second check of the corrections

After the findings of the ten checks were settled, seven further sessions of the AI system, started by the planning
session later on 2 October 2026, checked what had been done about them: each read one part of the revision as it then
stood against the dispositions above, against the files and, for the statements about cited works, against the PDFs.
They read the revision as a commit made for the purpose on 8bd189e in the planning session's working directory
(eed9271, which is not in the repository; the tree that the ten sessions had read was its branch `checked`), so that
the line numbers in their reports are that tree's and the dispositions they quote are those of this file as it then
stood. In their reports VT is that clone and VW the directory in which they worked. The reports are beside this file
as the sessions returned them:

- `recheck_W1.md` (W1-1 to W1-5): the main text; 5 findings (0 errors, 4 inexact, 1 note).
- `recheck_W2.md` (W2-1 to W2-7): S3 Text and the derived numbers; 7 findings (1 error, 3 inexact, 3 notes).
- `recheck_W3.md` (W3-1 to W3-12): the supplementary tables, S4 Text, S5 Text and the literature file; 12 findings (0
  errors, 6 inexact, 6 notes).
- `recheck_W4.md` (W4-1 to W4-14): the record's five new entries; 14 findings (1 error, 5 inexact, 8 notes).
- `recheck_W5.md` (W5-1 to W5-16): the dispositions file; 16 findings (2 errors, 7 inexact, 7 notes).
- `recheck_W6.md` (W6-1 to W6-20): the numbers table, the replacements file and the bookkeeping files; 20 findings (2
  errors, 8 inexact, 10 notes).
- `recheck_W7.md` (W7-1 to W7-12): the statements about cited works changed or added after the ten checks, against the
  PDFs; 12 findings (0 errors, 7 inexact, 5 notes).

The seven reports hold 86 findings, graded by the sessions as 6 errors, 40 inexact statements and 40 notes. None of
the six graded errors is a value of a result in the main text or in the supporting information; one finding graded
inexact is of such values, three limits of the Fisher-z intervals of S3 Text §6, each moved by 0.001 when computed
from the unrounded correlations (W2-1). Several findings are the same thing found by two or three sessions, and many
concern this file: statements of the dispositions above that were not exact. The six graded errors are four things: a
count in `checks/numbers_update.out`, 64 cross-references by number without a row where there are 74, which three
sessions found (W4-1, W5-2, W6-1); a computation label in a comment of `derived_r24.py` (W2-4); a statement of the
disposition of VT2-10 about CLAUDE.md (W5-1); and a count in the reason recorded with one replacement (W6-2). Each
finding was read against the files, and where it concerns a cited work against the PDF, before anything was changed.
Of the 86, 85 were corrected: a file of the commit was changed as the finding says, the dispositions above among those
files, so that they read as corrected. One names something that is kept and that this file now states as what it is.
None is kept without a change. Where several sessions found the same thing, the disposition is written once and the
others point to it.

### W1: the main text

**W1-1** (inexact). Methods' sentence on where the text repeats a computation's status named five sections, "in
Results 2, 3, 5 and 7 and the Discussion"; the text repeats it in the next subsection of Methods as well, and Results
6 has a statement of a neighbouring kind. Corrected. The parenthesis names no sections: "(the text repeats it for
several)". The reason recorded with the replacement names the places, Methods' own subsection and Limitations among
them.

**W1-2** (inexact). The disposition of VM-1 said that the record's disposition of B's MINOR 8 names each place; two
were not in it: Methods' sentence on A_other, the constructions and the generators' slopes, and Limitations' on the
predictions that failed. Corrected. The record's disposition of B's MINOR 8 names both, under "said to rest on a rule
or a prediction recorded beforehand", and the disposition of VM-1 says what the record names.

**W1-3** (note). Results 2: in "(SD 0.0887 against 0.0485 for the post-injection gap; ...)" the first SD, which is the
DiD's, read as the pre-injection gap's. Corrected. "(the DiD's SD 0.0887 against the post-injection gap's 0.0485;
r(DiD, pre-injection gap) = −0.888, r² = 0.79)".

**W1-4** (inexact). The reason that the disposition of VM-8 gave for keeping four titles covered bins and section
references, which the main text does use. Corrected. The disposition of VM-8 says which of the four kinds the main
text does not use (times of day and computation labels) and that the list's entries give the other two titles without
their parentheses. Found also by W3-6.

**W1-5** (inexact). The disposition of VM-10 named two lines for the rows of the window sets and of N = 14; four rows
of Table 2's caption cite a third, the record's line on the window sets. Corrected. The disposition of VM-10 names the
three lines.

### W2: S3 Text and the derived numbers

**W2-1** (inexact). S3 Text §6 and `derived_r24.out`, item 10, gave the Fisher-z intervals of the residual's four
cross-half correlations from the correlations as the split-half log prints them, at three decimals; from the unrounded
correlations, which committed files give, three of the eight limits differ in the third decimal. Corrected. Item 10 of
`derived_r24.py` computes the four correlations from the committed per-subject series (the residual's window series of
`diag_series_<variant>_W60.npz`, halved as the split-half test halves them, and the r₁ half DiDs of
`splithalf_subjects.csv`) and stops unless the correlations, the reliabilities and their p equal the log's printed
values. S3 Text §6 has the limits [−0.897, −0.269], [−0.857, −0.098] and [−0.567, +0.493]; the fourth interval, the
means, the ceilings and the ratios are as they were.

**W2-2** (inexact). The label of item 12 of `derived_r24.py` said that its values are those the tables file does not
print; two of them it prints (the slope and r of the residual's regression), and one value of the pre-run entry that
it does not print, the ratio of means, was not under the label. Corrected. The item's label names the three kinds: the
values that `baseline_gap_tables.md` does not print, the slope and r, which it prints, and the ratio of means, −0.788,
which B28's tables file prints and the item now recomputes.

**W2-3** (inexact). The disposition of VO-6 said that `derived_r24.py` compares the values of item 12 with the pre-run
entry's; the item printed them and compared nothing. Corrected. The item holds the twelve values as the pre-run entry
prints them and compares: its output ends "compared with the entry's values as printed there: 12 of 12 equal". The
record's "B27, outcome" says so, and the disposition of VO-6 is true as amended. Found also by W4-4 and W5-8.

**W2-4** (error). A comment of `derived_r24.py` called the split-half log "B19's log"; it is the log of the split-half
test, B7. Corrected. The comment names the split-half test's log (`splithalf.log`, B7); the item's printed label names
the file and no computation.

**W2-5** (note). S3 Text §5's note under table (a), the script's item 11 and the disposition of VS-12 spoke of three
assignments within 10⁻⁶ of the observed mean; 10⁻⁶ is not the bound that the file's rounding sets on such a
difference, and by the bound that it does set two of the three can change sides and the third cannot. Corrected. Item
11 uses the bound, k/14 × 10⁻⁶ for a difference that k of the fourteen values enter, and reports the two assignments,
with their mirrors, that the file counts by a margin within it (a tie, against 0.64 × 10⁻⁶; 0.43 × 10⁻⁶ against 0.50 ×
10⁻⁶), no uncounted assignment lying as near, so that the unrounded values give between 3,064 and 3,068 and the run's
3,066 is one such pair fewer than the file's. S3 Text §5's note and the disposition of VS-12 say the same.

**W2-6** (note). S3 Text §6 read the two ratios of the mean correlation to its ceiling as showing that "the two
variants stand alike"; on each variant the larger correlation is itself above the ceiling, and the reliability that
makes the ceiling on the sensitivity variant has p = 0.459. Corrected. The paragraph says that the ceilings are point
estimates at N = 14, gives both facts, and reads the comparison as showing only that the four correlations give no
ground for reading the two variants differently; item 10 of the script prints the reliabilities' p and which
correlation exceeds the ceiling.

**W2-7** (note). The disposition of VT2-6, that of T61 (iii) and the record's disposition of A's w1 glossed S3 Text
§9's "not an artefact of scale" as of the scale of sts; the sentence's scale is the series' variance, and it denies
the word of a part of the r₁ change. Corrected. The three say what the sentence says: residualising a contrast on the
ratio of window variance to run variance would remove the part of the r₁ change that coincides with the variance
change, "not an artefact of scale". Found also by W4-3.

### W3: the supplementary tables, S4 Text, S5 Text and the literature file

**W3-1** (inexact). S19 Table's head note named the places of the main text that quote the two sets of values known
before their run; the Discussion was in neither list and the Abstract in one only. Corrected. The first list: "main
text, Abstract, Results 2 and 4, Table 3, Fig 3 and the Discussion"; the second: "main text, Abstract, Tables 2 and 3,
Results 2 and 4, the Discussion and Methods, Inference; S3 Text §5", with Fieller's g named among its values.

**W3-2** (inexact). S19 Table's row of B24's expectations sent the reader to "the paragraph after" the residual table
of S3 Text §6 for A_other's expectation; since a correction that paragraph is a sentence on the caption's −0.74.
Corrected. The cell: "S3 Text §6 (its residual table, last column, and, under the next heading, the text and the table
of the aligned and directed statistics); S18 Table". Found also by W6-20.

**W3-3** (inexact). S4 Text's row S6 said that the supporting texts label every post hoc or review computation where
they report it; S3 Text reports the leave-two-out on the collinearity and several derived numbers without a word on
their status. Corrected. The row: "the supporting texts say of many post hoc or review computations, where they report
them, that they are such, and the main text repeats the status for several (Methods, The primary contrast and the
exploratory analyses); S19 Table's Part B gives the status of each". The row's last clause read "the complete list is
S19 Table's" until the third check found Part B two computations short (X1-2).

**W3-4** (inexact). The "reported at" cell of S19 Table's row B21 (d) did not name the Abstract and the Discussion,
which quote the disattenuated ratio; older cells have the same gap (B22 (d), B4, the regional test, B17 (i), B17b
(i)). Corrected. Every "reported at" cell of Part A was read against the main text, with the source of each number in
the numbers table as a guide, and completed with the places of the main text that print a value of the row's outcome;
some cells also name a place that gives a number derived from the outcome or states it in words (the table's head note
says what the column names and what it does not list: X1-8 and, for its present wording, Y1-1). Besides the six named:
the redundancy prediction (Table 1), B3 (Fig 6), B16 and B16b (Table 4), B17 (ii) and B17b (ii) (Limitations, in
words), B23 (b) (Table 3 and Fig 3, for the rate −0.39), B23 (f) (Fig 2; Methods), the check of B24 against B17b
(Table 3, for the rate −0.18), B28 (b) and (c) (Table 3), B29 (a) (Table 2 and the Discussion, for the mean-FD DiD)
and B16c (a) to (d) (Table 4); in the cell of B22 (a), which named Results 4 before, Results 4 is marked "(in words)"
and the pointer into S3 Text §6 names its two places. B4's cell now reads "Abstract; Results 4; Discussion; Tables 1
and 3; Figs 2, 3 and 5; S3 Text §6 (its residual table); S12 Table; S5 Text §1 (the deviations)", and that of B21 (d)
"Abstract; Results 2; Discussion; Fig 3; S3 Text §5".

**W3-5** (inexact). The disposition of VN-1 said that the second form of the citations audit's report lists the five
page ranges; the report says that five ranges are wider than the pages and quotes one. Corrected. The disposition of
VN-1 says what the report says. Found also by W7-7.

**W3-6** (inexact). The reason of the disposition of VM-8. Corrected. As W1-4.

**W3-7** (note). S19 Table's Part B row of `derived_r24.out` no longer named the two shares that Results 2 states in
words from its item 4, a fifth and a sixth. Corrected. The row: "the FD-residualised r₁ DiD and, in words, the shares
of the two contrasts that the FD residualisation removes, a fifth and a sixth", and, for the Discussion, "the fifth
again".

**W3-8** (note). The same row, the record and the review folder's README said that the script reads "arrays"; it read
one array file. Corrected. The three give the kinds with their counts as the script now stands: "two pickles of
per-subject vectors, eight CSV files, five tables files, three array files and a log" (item 10 reads the two files of
the residual's window series as well; the counts of the CSV and tables files are those after the third check, which
added items 13 and 14 and the additions to items 1 and 6, the last of which reads a tables file). Found also by W4-13.

**W3-9** (note). The source line of S18 Table's part on B28 named two of the three kinds of column that the part
leaves out. Corrected. It names the three: "the r percentiles, the share of replicates with r at or below the data's
and the percentiles of the per-replicate ratio of means".

**W3-10** (note). S4 Text's row R1 listed the exceptions to "mean DiDs with inverted sign-flip 95 % intervals and
exact p"; contrasts that the main text gives as point values or with p alone were not in it. Corrected. The row adds a
sentence on those contrasts, "A contrast that the main text gives only as a point value or with its p, at no place
with its interval, has the interval in the supporting information", with their kinds and their places (S2 Text; S3
Text §4, §5, §6 and §8; S1, S11, S14 and S17 Tables). The sentence and its list are as the third check left them,
which found the first form short of four contrasts (X1-1).

**W3-11** (note). The literature file's title and search paragraph and S20 Table's head note said that the studies
were read in full, beside a row 6 that says the copy of Down et al. (2026) holds pages 1–25 of 55. Corrected. S20
Table's head note: "The full texts are the studies' main articles; where a row also draws on a study's Extended Data,
Reporting Summary or other supplementary material, the row names it; of Down et al. (2026) the copy read holds pages
1–25 of the preprint's 55, its main text and references (row 6)" (the middle clause as the third check corrected it:
X1-3). The literature file's search paragraph says the same, and its title says "every cell verified against the PDF
as read, which the search paragraph describes".

**W3-12** (note). The disposition of VR-14 said of three places what two of them say; in the literature file the
reading and the adding of row 10 still read as of one date. Corrected. The literature file's paragraph: "read in full
from V.S.'s copy on that date and added as row 10 in the revision of 1–2 October 2026"; the disposition of VR-14 says
what each place says. Found also by W5-6.

### W4: the record's five new entries

**W4-1** (error). `checks/numbers_update.out` counted 64 cross-references by number without a row; there are 74. The
ten references to a figure's panel, as in "Fig 1a", were in no count. Corrected. The planning session's pass over the
tokens counts them: the file gives the cross-references by the word they follow, those to the paper's own sections,
tables and figures and those to equations, definitions, an example, figures and a table of cited works (the
Discussion's "their Table 1" is a cited work's, which the third check found counted with the paper's own: X2-1), with
the ten panel references named, and no longer names pages, of which there are none. The head note says that a figure's
number before a panel letter has no row. The count is 70 in the text as corrected: the four numbers of Methods' list
of sections left it with the correction for W1-1. Found also by W5-2 and W6-1.

**W4-2** (inexact). The record said that the list of deleted rows marks a moved number that stands at its new place
with more decimals; for six numbers it did not. Corrected. The list gives the form at each place: −0.0944 and 0.0154
"as −0.09441" and "as −0.01540" in Fig 3's caption and S13 Table's note; A_other's expectation "as +0.00001" and "as
0.00031" in S18 Table; the slope's interval "as −1.133" and "as −0.373" in Table 3. The record's parenthesis names
them, and the reasons recorded with two replacements give the same forms. Found also by W6-9.

**W4-3** (inexact). The record's disposition of A's w1 on S3 Text §9's sentence. Corrected. As W2-7.

**W4-4** (inexact). The disposition of VO-6 on item 12 of the script. Corrected. As W2-3.

**W4-5** (inexact). The record's disposition of C's M1 said of the released derivatives that they have no demographic,
image or identifying field; the Ethics statement says it of the quantities the analysis uses. Corrected. The
disposition gives the statement's content as it stands: "a secondary analysis of derivatives released by the data
authors; the quantities it uses carry no demographic, image or identifying field; no new data; no participant
contacted".

**W4-6** (inexact). The numbers table's head note gave five kinds for the seven rows of numbers no longer stated; the
seventh, the spin p, is of a sixth. Corrected. The head note has the record's six: "a threshold replaced by the p
values themselves, a repeated limit, a second mention, a count of refits, a clause that is not carried, and the spin p
rewritten as p < 1/10,000". Found also by W6-5.

**W4-7** (note). The disposition of VO-2 gave to three places a clause, "with its inverted interval", that one of them
has. Corrected. The disposition of VO-2 says which place has it.

**W4-8** (note). "B28, outcome", item (iii), said that the subject at the floor is named where the band-passed
conditions are reported; Fig 3's caption and S19 Table's rows report values of those conditions without naming it.
Corrected. The item names the three places that name the subject and says of the other two what they do: "Fig 3's
caption, which quotes the band-passed step's slope, points to Table 3's caption for the floor, and S19 Table's rows on
B28 give the conditions' values without it".

**W4-9** (note). The record's disposition of B's MINOR 8 gave the sensory–association contrast as "named as a recorded
prediction"; the text says that it was fixed beforehand. Corrected. The disposition: "the sensory–association
contrast, fixed before the partialled map was computed, and the residual map's network structure, whose p lies below
the range predicted for it", under "said to rest on a rule or a prediction recorded beforehand" (with W1-2).

**W4-10** (note). The record's disposition of A's m8 gave S5 Text §1 as the place where "scope map" stays as the
plans' name; S3 Text §4 has it too. Corrected. "(S3 Text §4 and S5 Text §1 say that it is)".

**W4-11** (note). The record's list of what `checks/` holds left out the parse check of the scripts and
`figures_check.py`. Corrected. The list has "the parse check of the five scripts" (of the four scripts when this
correction was made; the check covers the fifth since the fourth check, Y3-1) and "`figures_check.py`, which tests the
figures commit".

**W4-12** (note). The record's sentence on the works cited for statements newly made did not name Luppi et al. (2026),
nor the two works whose sentences the claim record checks again, and the entry did not mention S3 Text §10's sentence
on ketamine. Corrected. The sentence names Luppi et al. (2022, 2024, 2026), Down et al. (2026) and Gatica et al.
(2024) with the others, says that Luppi et al. (2023) and Murray et al. (2014) were "checked again for the sentences
that cite them", and the paragraph on the searches says what S3 Text §10 says of ketamine. Found also by W7-12.

**W4-13** (note). What the record says that the script reads. Corrected. As W3-8.

**W4-14** (note). The record, the head note and the list did not say that the numbers in the names of the supporting
items have no row. Corrected. The three say that the digits in the names of the supporting items, S1 Text to S20
Table, are not number tokens.

### W5: the dispositions file

**W5-1** (error). The disposition of VT2-10 said that CLAUDE.md's account of this revision has "p < 1/10,000"; the
file has the phrase nowhere. Corrected. The disposition says that the paper's files have it and that CLAUDE.md's
account of the revision does not give the spin p; the reason for keeping the dated bullet stands.

**W5-2** (error). The count of the cross-references in `checks/numbers_update.out`. Corrected. As W4-1.

**W5-3** (inexact). The part on the ten checks began "After the corrections above were made"; the corrections for C27,
C28, C30, C31 and C32 and for the point on S20 Table's rows 2, 5 and 8 came after the ten checks. Corrected. The
sentence says so, with the claim record's item for C26, and that the second check covered those corrections.

**W5-4** (inexact). "One thing that no session raised was corrected with them": four more changes of that kind were in
the tree and in no disposition. Corrected. "Found while the findings were settled" lists the five. Found also by W7-1,
which read the corrected name against the preprint's first page.

**W5-5** (inexact). The disposition of R32 said that the record's paragraph has three lists; since the correction for
VE-8 it has four. Corrected. The disposition of R32 names the four.

**W5-6** (inexact). The disposition of VR-14. Corrected. As W3-12.

**W5-7** (inexact). The disposition of VR-5 said that the disposition of R56 quotes CLAUDE.md's sentence; R56 gives
the condition without quoting it. Corrected. The disposition of VR-5 says that R56 gives the same condition.

**W5-8** (inexact). The disposition of VO-6. Corrected. As W2-3.

**W5-9** (inexact). Row 5 of S20 Table has two cells on HRF deconvolution; the last said what was read and nothing of
the Supplementary Methods, so that the dispositions of R25 and VN-3 held of one cell and that of R38 said "only" of a
cell that says more. Corrected. The last cell, in S20 Table and in the literature file: "not mentioned in the PDF read
(the article, its Extended Data and its Reporting Summary; the Supplementary Methods the article defers to were not
read)". The dispositions of R25 and VN-3 now hold of both cells, and that of R38 says what the cells say and that they
carry no request.

**W5-10** (note). Four cross-references among the headings of the first three parts were one-sided, those of C26, C29
and C31. Corrected. The headings of T51, R12, T29 and R25 name them, and the planning session's preparation of this
file, which is outside the repository, stops on a cross-reference that is not returned.

**W5-11** (note). The disposition of VS-11 quoted S3 Text §5 without the code type of the variant's name. Corrected.
It quotes S19 Table's row and says that S3 Text §5 has the same words with the name in code type.

**W5-12** (note). The disposition of VR-4 said that R48 gives condition (1) in the record's words; four small
differences. Corrected. "in nearly its words".

**W5-13** (note). S20 Table's row 10 quotes "the Gaussian MMI solver" with its article; the claim record quoted the
phrase without it. Corrected. The article is the work's (Gao et al., 2026, PDF p. 3: "computed using the Gaussian MMI
solver implemented in the Java Information Dynamics Toolbox"); the claim record and the disposition of VT2-13 quote
the phrase as the table does.

**W5-14** (note). The counts of the grades of `check_VT2.md` given in this file (7 inexact, 9 notes) are those that
its findings carry; the report's own opening sentence counts 8 and 8. Stated. The grades counted in this file and in
the record are those that the findings carry, in every report; the introduction of the part on the ten checks now says
so and names the report whose summary differs.

**W5-15** (note). The description of the eleven errors named the places that VB-2 found wrong as those of the list
alone; VB-2 found the same in a reason and in the record's entry. Corrected. The introduction of the part on the ten
checks says so.

**W5-16** (note). A comment of the figure script still said that Fig 5c's legend sits "the same distance" below the
taller panel, where the record and the disposition of R49 say "about as far". Corrected. The comment: "about the same
distance below the taller panel".

### W6: the numbers table, the replacements file and the bookkeeping files

**W6-1** (error). The count of the cross-references in `checks/numbers_update.out`. Corrected. As W4-1.

**W6-2** (error). The reason recorded with the replacement of Data and code availability spoke of nine review folders
named there and of calibration scripts listed one by one; the committed sentence named eight folders, and the scripts
as a range and two names. Corrected. The reason: "the names of the eight review folders, which S5 Text §5 gives, with
the folder of this revision; and the calibration scripts, given as a range and two names".

**W6-3** (inexact). The reason recorded with the replacement of Results 2's first paragraph gave r² as "as high" for
the post-injection gap as for the pre-injection gap; they are 0.75 and 0.79. Corrected. "r² being nearly as high for
the post-injection gap (0.75) as for the pre-injection gap (0.79)".

**W6-4** (inexact). The head note explained "@La-b|" as naming the table that occupies lines a to b; of the three
ranges in use one is a line of prose, one the body of a table and one a table with its head. Corrected. The head note:
the anchor "says that the row's line is one of lines a to b of the file (the rows of a table, with or without its
head, or a single line)"; `numbers_update.out` has the same.

**W6-5** (inexact). The kinds of the seven rows of numbers no longer stated, in the head note. Corrected. As W4-6.

**W6-6** (inexact). Seventeen rows of N = 14 had the note "the per-subject rows of the primary result", which
describes neither the record's line they cite nor the result file. Corrected. The note of the seventeen: "N = 14
subjects (the shape of the data: 14 subjects × 2 conditions)"; the head note and `numbers_update.out` count the three
committed and the fourteen added rows.

**W6-7** (inexact). `numbers_update.out` quoted, as of Table 4's caption, words that are the source line's and
Methods'. Corrected. The line quotes the caption: "chosen by the Bayesian information criterion (BIC) in 1–5".

**W6-8** (inexact). `numbers_update.out` said that the paragraph's other 14s are of "14 of 14"; two of the four are.
Corrected. "(the paragraph's other 14s are of '13 of 14', of '14 of 14' and of the windows 5–14)".

**W6-9** (inexact). Six moved numbers stand at a place the list names with more decimals, and two reasons place them
the same way. Corrected. As W4-2.

**W6-10** (inexact). CLAUDE.md said that Table 3 is named once before Results 4 cites it, in Fig 3's caption; the
caption names it twice. Corrected. "(Table 3 is named before that in Fig 3's caption, twice)".

**W6-11** (note). Of the six rows that print as a percentage a value held as a fraction one carried the mark "@pct|";
the five rows of Table 4's shares did not. Corrected. The five carry it.

**W6-12** (note). Three more committed label rows had notes about other tokens of their sentences (the 0 of "q = 0";
the two 1s of "x_{t+1}, y_{t+1}"). Corrected. Their notes name their own tokens; the head note and
`numbers_update.out` count them.

**W6-13** (note). The held string of the row of Results 2's 0.83 was "-0.830", the hyphen of a range taken for a sign,
and `check_numbers` flagged the row for it. Corrected. The row holds 0.830; `check_numbers_revision.out` flags ten
rows, each an unsigned print of a negative value: in seven the wording gives the direction ("fell by", "exceeds the
observed level by", "a fall of", and the derivative printed beside Results 1's 0.019), and in three the text gives a
size (the Abstract's "by 0.019", Results 1's "by 0.031" and Limitations' "only to within 0.053").

**W6-14** (note). The head note's list of the sources of the added rows named neither the supporting information nor a
log. Corrected. The list has "a committed log" and "the supporting information where it holds the value (S3 Text; S2,
S6, S15 and S18 Tables)".

**W6-15** (note). A line of `numbers_update.out` gave a pointer of the Discussion as it was before a correction.
Corrected. "(S3 Text §4, §10)".

**W6-16** (note). The row of Results 7's 18 % derived the share from two printed values, 17.7 %; the run's file holds
the share, 17.6 %. Corrected. The derivation is from the run's unrounded values, with the file and line named: 17.6 %.
The text's 18 % is the same from either.

**W6-17** (note). The reasons recorded with the replacements of the Abstract and of a Discussion paragraph put in
quotation marks words that are not those of the replacements. Corrected. They quote "most fMRI synergy reports we
found" and "the ten empirical studies we found".

**W6-18** (note). The disposition of VE-8 said that the reasons recorded with the two replacements say that the
sentences went for length; that of the Introduction's did not. Corrected. The reason says that the sentence listing
the Results sections "is retired for length"; the disposition of VE-8 says since when.

**W6-19** (note). Three dispositions (VB-8, VB-20, VT2-14) spoke of what "the build" counts, asserts and tests; no
program that builds the table is in the tree. Corrected. The three, and the disposition of VE-20, speak of the
planning session's preparation of the table and of the revision, which is outside the repository, and that of VT2-14
says what the committed `check_numbers.py` tests.

**W6-20** (note). S19 Table's row of B24's expectations. Corrected. As W3-2.

### W7: the statements about cited works changed or added after the ten checks, against the PDFs

**W7-1** (inexact). The change of "Legare, A." to "Légaré, A." answered no finding and stood in no disposition.
Corrected. As W5-4.

**W7-2** (inexact). The claim record's first item on Liardi et al. (2025) gave Results 7 and S3 Text §10 as the places
of a clause that only S3 Text §10 states. Corrected. The pointer says which place states which part: the quantile
reading in both, "the data-driven variant is stated in S3 Text §10 only".

**W7-3** (inexact). The claim record's item on Luppi et al. (2026) did not name S3 Text §10, which states the
anaesthetics of the macaques too. Corrected. The heading names S3 Text §10, and the pointer S3 Text §10 and the search
note.

**W7-4** (inexact). The claim record's head said what the checks added to it: one addition was missing, one was
described too narrowly, and two items that answer findings of the audit of the citations were given to the checks.
Corrected. The head gives the two items on Luppi et al. (2023) and Murray et al. (2014) to the audit's second form
(C27, C26), lists what the ten checks added, the clause on the data-driven variant of Liardi et al. (2025) and the
item on p. 2 of Luppi et al. (2022) among them, describes the item on Luppi et al. (2026) as of the article, its
Extended Data and its Reporting Summary, and says what the second check added.

**W7-5** (inexact). The claim record called the two Reporting Summaries "image-only"; they are PDFs without a text
layer, their text drawn as outlines. Corrected. The record now says what can be extracted from each (the third check
found a single character in one of them, X4-8, and the fourth white space in the other, Y4-5): "its text is drawn as
outlines, so that nothing can be extracted from the PDF as text but one character, an Ω on p. 3; read from images of
its pages"; "from which nothing can be extracted as text but white space, thin spaces on p. 35, and which were read
from images of the pages".

**W7-6** (inexact). The screening file said that the local measure of Pope et al. (2025) "is introduced on PDF p. 6";
the paper names and chooses it on PDF p. 3, derives it from PDF p. 5 and gives its formula on PDF p. 6. Corrected. The
row gives the three pages, read again in the PDF, and the dispositions of C28 and VN-4 quote it as it stands.

**W7-7** (inexact). The disposition of VN-1. Corrected. As W3-5.

**W7-8** (note). S3 Text §10 and the search note said that one study of S20 Table applies ΦID to fMRI under ketamine;
the macaques of a second, Gatica et al. (2024), scanned under isoflurane, were given ketamine before the scan.
Corrected. Both name the second study, read again in the PDF (p. 12: ketamine at 10 mg/kg with five other agents, the
scan about two hours after anaesthesia; p. 1: no drug in the title, the keywords or the abstract). S3 Text §10: "the
macaques of a second (row 4: Gatica et al., 2024, scanned under isoflurane) received injections of ketamine and of
other agents, and their scans began about two hours after anaesthesia" (the plural since the third check, X4-7). The
claim record has the item.

**W7-9** (note). Two statements added after the ten checks had no item in the claim record: on the copy of Down et al.
(2026), and that the abstract of Luppi et al. (2026) names no drug. Corrected. The claim record has a section on Down
et al. (2026) (25 pages, each numbered as one of 55; p. 4 refers to the supplementary materials for the fMRIPrep
output) and, in the item on Luppi et al. (2026), what its title and abstract name.

**W7-10** (note). The claim record said that S3 Text §10 gives the authors of Liardi et al. (2025); it gives their
number and their relation to the ΦID paper's. Corrected. "the number of the authors and their relation to the ΦID
paper's (four of that paper's seven, with two others)".

**W7-11** (note). The claim record's item on Murray et al. (2014) put "the macaque cortex" at p. 1; that page has
"primate cortex" and "monkeys", and the species is named on p. 2. Corrected. The item gives p. 1 in that page's terms
and the seven areas "of the macaque" at p. 2, Fig. 1.

**W7-12** (note). The record's sentence on the works cited for statements newly made. Corrected. As W4-12.

## The third check of the corrections

After the findings of the second check were settled, four further sessions of the AI system, started by the planning
session on 3 October 2026, checked the revision as it then stood: that each disposition of the second check is true of
the files, and that what had been changed in answer to it is itself right. They read the revision as a commit made for
the purpose on 8bd189e in the planning session's working directory (f50c1d3, which is not in the repository; the tree
that the seven sessions had read was its branch `checked2`), so that the line numbers in their reports are that tree's
and the dispositions they quote are those of this file as it then stood. In their reports VT is that clone and VW the
directory in which they worked. The reports are beside this file as the sessions returned them:

- `recheck_X1.md` (X1-1 to X1-11): the paper's files: the main text, S3, S4 and S5 Text, the supplementary tables and
  the literature file; 11 findings (0 errors, 5 inexact, 6 notes).
- `recheck_X2.md` (X2-1 to X2-10): the record's five new entries, the numbers table, the replacements file and the
  bookkeeping files; 10 findings (0 errors, 2 inexact, 8 notes).
- `recheck_X3.md` (X3-1 to X3-13): the dispositions file; 13 findings (0 errors, 5 inexact, 8 notes).
- `recheck_X4.md` (X4-1 to X4-8): the statements about cited works changed or added after the second check, against
  the PDFs; 8 findings (0 errors, 5 inexact, 3 notes).

The four reports hold 42 findings, graded by the sessions as 0 errors, 17 inexact statements and 25 notes: none is
graded an error, and no value of a result in the main text or in the supporting information was found wrong. Eight
things were found by two sessions, so that the findings are 34 different things; two notes of X2 (X2-9, X2-10) that
session took from the report of X3, which lay in the directory in which the four worked, and verified against the
files, as that session said when it returned its report, which does not say it. What the sessions found inexact are
general statements that the corrections had written (two rows of S4 Text; a sentence of S20 Table's head note; a count
in `checks/numbers_update.out`), cells of S19 Table that name a place which does not hold what the cell says, pointers
of the claim record, and four statements of this file, two that a later correction had left behind (the dispositions
of VB-16 and VC-2) and two that were not exact as written (the disposition of W6-13; the first sentence of the part on
the ten checks). Each finding was read against the files, and where it concerns a cited work against the PDF, before
anything was changed. Of the 42, 41 were corrected: a file of the commit was changed as the finding says, the
dispositions above among those files, so that they read as corrected. One names something that is kept and that a text
of the commit now states as what it is. None is kept without a change. Where two sessions found the same thing, the
disposition is written once and the other points to it.

### X1: the paper's files: the main text, S3, S4 and S5 Text, the supplementary tables and the literature file

**X1-1** (inexact). The sentence that the second check had put into S4 Text's row R1, that a contrast which the main
text gives as a point value or with its p alone has its interval in the supporting information, did not hold of four
contrasts: two had their interval there and were not in the row's list (the deconvolved contrast; the whitened series'
r₁ DiD at p = 20), and two had no interval at any place of the paper (the count DiD of the replaced volumes; what the
AR(1)-substituted estimate carries of the contrast at p = 20). Corrected. The row lists the four: "the deconvolved
contrast (S2 Text; S17 Table), the whitened series' r₁ DiD at p = 20 and what the AR(1)-substituted estimate carries
of the contrast there (S3 Text §8; the first also in S11 Table) and the DiD of the count of replaced volumes (S3 Text
§5)", and its sentence is of "A contrast that the main text gives only as a point value or with its p, at no place
with its interval". The two that had no interval have one, each the inversion of the exact sign-flip test on committed
per-subject values: S3 Text §5, "inverted sign-flip interval [−0.58, +2.97], from the per-window file:
`derived_r24.out`, item 14"; S3 Text §8, "carries −0.0037 [−0.0066, −0.0008] (p = 0.0145, negative in 12 of 14;
`derived_r24.out`, item 1)". The two items reproduce what the run printed (the count DiD's mean, p and sign count; the
estimate's mean, p and sign count).

**X1-2** (inexact). The clause that the second check had put into S4 Text's row S6, "the complete list is S19
Table's", did not hold: S19 Table's Part B had no row for the third review's partial correlations, which S3 Text §6
quotes, or for the audit's transfer-entropy check, which S3 Text §3 quotes. Corrected. Part B has a row for each ("The
third review's partial correlations of the residual DiD with the CCS-sts DiD given the autocorrelation DiD"; "The
lag-1 transfer entropies of two AR(1) processes under an invertible filter"), and the reading of Part B against the
whole paper that followed (below) added three more. The row's clause now reads "S19 Table's Part B gives the status of
each".

**X1-3** (inexact). The sentence that the second check had put into S20 Table's head note and into the literature
file, that the full texts are the main articles "with supplementary materials only where a cell names them", did not
hold of row 1 (Luppi et al., 2022), which cites two pages of that study's Reporting Summary without naming it; that no
volume was censored is stated on one of them alone. Corrected. Row 1 names what it cites, in S20 Table and in the
literature file: "3 T (the Reporting Summary, p. 36; the article gives the field strength for the diffusion scan, p.
13)" (the cell as the fourth check left it: Y4-4), "no volume censoring (p. 13 and, in the Reporting Summary, p. 37,
which states it)" and "Lausanne-129 for robustness (Extended Data Fig. 2, p. 23)". The sentence: "The full texts are
the studies' main articles; where a row also draws on a study's Extended Data, Reporting Summary or other
supplementary material, the row names it". The PDF was read again: the article ends on p. 20, the Extended Data are
pp. 21–32 and the Reporting Summary pp. 33–39. Found also by X4-1.

**X1-4** (inexact). S19 Table's row B19 (b) named Results 1 as a place that reports it; Results 1 prints none of the
row's values, and its slopes and per-SD ratio are B22 (d)'s. Corrected. The cell: "S3 Text §4 (Results 1 names the
regression and gives its unstandardised slopes, which are B22 (d)'s)".

**X1-5** (inexact). Two rows of S19 Table's Part A named places of the supporting information that hold neither the
row's values nor its outcome in words: the tier assignment (S1 Text; S2 Table) and the regional ΦR check after
deconvolution (S2 Text, which said only that the test was carried out). Corrected. The tier assignment's cell: "not
quoted (S1 Text defines the tiers and, with S2 Table, gives the test of the tier-2 criterion on the data)". For the
regional check the place is made to hold the outcome: S2 Text now says "its prediction was missed, the increase being
smaller, not larger, inside the Default/Control proxy than outside it (inside minus outside −0.0047 [−0.0079,
−0.0013], a percentile interval; p = 0.023; positive in 4 of 14", the values of the report's table of the prediction
(its section 1) and of the row.

**X1-6** (note). Three cells of Part A named a place that prints none of the row's values: S3 Text §6 for the
run-level mean cross-lag deviation and for the W = 60 statistic and the null, and Results 7 for B16c (b). Corrected.
The cells say what each place holds: "S3 Text §6 (in words: a signed mean cancels on ts_gsr); S9 Table (the values,
among its earlier values)"; "S3 Text §6 (in words: the window-sign statistic superseded); S9 Table (the superseded
values)"; "Table 4; S11 Table; S3 Text §8; Results 7 (the level at p = 20 only as the base of a share, 18 %)".

**X1-7** (note). Methods prints the AR(1) generator's level at W = 60, 0.715, which stands in the outcome of B17 (iv)
as the level its own is set against, and no cell of B17 named Methods. Corrected. The cell of B17 (iv) adds "Methods,
The AR(1)-substituted estimate and its calibration (the level the row's is set against, 0.715)".

**X1-8** (note). Numbers that the numbers table sources to a computation of Part A, outside the row's outcome, are
printed at places which the row's cell does not name (among them subject 8's count of replaced volumes in Results 2,
the AR(1) pairs' rate 3.1, the residual's cross-half correlations with r₁ in Results 4 and CCS-sts's split-half
reliability in Results 6), where the disposition of W3-4 said that the cells had been read by the source of each
number. Stated. The cells are kept as the places of each row's outcome, and the table's head note says what the column
names: "In Part A the last column names where the row's outcome is reported: the supporting text or table that reports
the computation, and every place of the main text that prints a value of the outcome" (the sentence as the fourth
check left it: Y1-1). By value, the session found no place of the main text missing from a cell. The disposition of
W3-4 says what the reading followed.

**X1-9** (note). The disposition of W3-4 listed Results 4 among the places added to the cell of B22 (a); the cell
named it before, and what changed is the mark "(in words)" and the pointer into S3 Text §6. Corrected. The disposition
of W3-4 says so.

**X1-10** (note). The first sentence of S4 Text's row R1 put the intervals without p in S3 Text §6 alone and stopped
at Results 6; Results 4 and Table 3 give two contrasts with an interval and no p, and Results 7 and Table 4 give
contrasts with inverted intervals and exact p. Corrected. The sentence: "(Tables 2 and 4; Results 2, 6 and 7;
intervals without p for the AR(1)-substituted estimate's DiD and the residual DiD in Results 4 and, for the residual,
in Table 3, whose p are in S17 Table, and in the data rows of the residual table of S3 Text §6" (the sections named as
the fourth check left them: Y2-6).

**X1-11** (note). Three cells of S19 Table's Part B omitted a section of S3 Text that quotes the row's computation (§4
for the checks of the review of 17 September 2026 and for the spectral centroid; §9 for the review computations of 14
September 2026); the other cells of Part B had not been read for completeness. Corrected. The three cells name the
sections, and S5 Text §1 says that "three of its checks are quoted, as review computations, in S3 Text §4, §6 and §9".
Part B was then read against the whole paper by a further session and every cell completed (below).

### X2: the record's five new entries, the numbers table, the replacements file and the bookkeeping files

**X2-1** (inexact). `checks/numbers_update.out` gave the 17 numbers that follow "Table" as references to the paper's
own tables; one is "their Table 1", a table of Luppi et al. (2022). Corrected. The file: "25 after "Results", 16 after
"Table" and 14 after "Fig"" for the paper's own, and "to equations, definitions, an example, figures and a table of
cited works (7, 3, 1, 3 and 1, the last "their Table 1" of the Discussion)". The disposition of W4-1 follows. Found
also by X3-5.

**X2-2** (inexact). The disposition of W6-13 said of the ten rows that `check_numbers_revision.out` flags that the
wording gives the direction of each; for three the text gives a size and no direction. Corrected. The disposition of
W6-13 says which seven and which three. Found also by X3-1.

**X2-3** (note). Two groups of digits that follow a letter directly have no row and were in no kind that the list, the
head note or the record named: the 4 of "Fig. S4" and the 540 of the repository's address. Corrected.
`numbers_update.out`: "A group of digits that follows a letter directly is not a number token: the 148 in the names of
the supporting items (S1 Text to S20 Table), the 4 of "Fig. S4", a figure of a cited work's appendix, and the 540 of
the user name in the repository's address". The head note and the record's paragraph on the checks state the rule.

**X2-4** (note). The record's parenthesis on the moved numbers that stand at their new place with more decimals left
out the Abstract's 0.003–0.005. Corrected. The parenthesis adds "the Abstract's 0.003–0.005, which Results 4 gives as
0.0027 and 0.0049".

**X2-5** (note). The record's list of the corrections that the second check brought to the paper's files is complete
as a list of corrections; one more place of those files changed, S5 Text §5's clause on that check. Corrected. The
record's paragraph adds "S5 Text §5's clause on the audits names this check too".

**X2-6** (note). The reason recorded with the replacement of Fig 5c's legend anchor kept "stays as far below the axis
as it was", where the script's comment, the record and the disposition of R49 say "about". Corrected. The reason:
"stays about as far below the axis as it was (0.0714 of the summed height ratios for 0.0700)".

**X2-7** (note). The record's "the parse check of the four scripts" does not say which four; the revision's check is
of four other scripts than those the entries call the four scripts. Corrected. The record: "the parse check of the
five scripts that this commit adds or changes (the figure script, `figures_check.py`, `derived_r24.py`, the counter of
the Abstract's and the Author summary's words and the audit's `te_filter_check.py`)" (the fifth script, in the
sentence and in the check, since the fourth check: Y3-1).

**X2-8** (note). Two dispositions, of R55 and of W5-10, still spoke of a build or a program that is not in the tree,
the kind that W6-19 had found. Corrected. Both speak of the planning session's preparation, which is outside the
repository. Found also by X3-9.

**X2-9** (note). The disposition of W2-4 said that no printed line of `derived_r24.out` named a computation; that is
true of the lines of item 10 alone. Corrected. The disposition says "the item's printed label names the file and no
computation". Found also by X3-13.

**X2-10** (note). The record's sentence that again no value of a result was found wrong holds of the six findings
graded errors; a finding graded inexact, W2-1, changed three interval limits of S3 Text §6 by 0.001. Corrected. The
record's paragraph and the introduction of the part on the second check: none of the errors is such a value, and "one
finding graded inexact is of such values", the three limits. Found also by X3-11.

### X3: the dispositions file

**X3-1** (inexact). The disposition of W6-13. Corrected. As X2-2.

**X3-2** (inexact). The first sentence of the part on the ten checks, as amended for W5-3, said that the corrections
for C26 to C32 came after those checks; that of C29 and the words restored for C26 were made before. Corrected. The
sentence names what came later: "those for C27, C28, C30, C31 and C32, the claim record's item for C26 and the point
on S20 Table's rows 2, 5 and 8". The paragraph of W5-3 states the finding in those terms.

**X3-3** (inexact). The disposition of VB-16 still said that the reason of the replacement of Data and code
availability lists "the calibration scripts one by one", which W6-2 had corrected in the reason. Corrected. The
disposition of VB-16 says "the calibration scripts, which the committed sentence gave as a range and two names".

**X3-4** (inexact). The disposition of VC-2 still said that the claim record's item has S3 Text §10 give the authors
of Liardi et al. (2025), which W7-10 had corrected in the item. Corrected. The disposition of VC-2 says "the number of
the authors and their relation to the ΦID paper's". Found also by X4-5.

**X3-5** (inexact). The 17 numbers after "Table" in `numbers_update.out`. Corrected. As X2-1.

**X3-6** (note). The disposition of W7-3 said that the heading and the pointer of the claim record's item on Luppi et
al. (2026) both name the search note; the heading names S3 Text §10 alone. Corrected. The disposition of W7-3: "The
heading names S3 Text §10, and the pointer S3 Text §10 and the search note". Found also by X4-6.

**X3-7** (note). "Found while the findings were settled", (4), said that the source lines of S11 and S18 Tables put
the date after the pre-run entry's title; S11 Table's has no title. Corrected. The sentence: "S18 Table's after the
entry's title and S11 Table's, which has no title, after the words "pre-run entry"".

**X3-8** (note). The disposition of VB-31 quotes 8,498 words and 8,469, the counts of the tree that the check read;
the output is 8,489 and 8,460 since the corrections for W1-1 and W1-3. Corrected. The disposition of VB-31 says whose
the two numbers are and gives the counts as they now stand.

**X3-9** (note). The dispositions of R55 and of W5-10. Corrected. As X2-8.

**X3-10** (note). The heading of the last point that the audit of the citations raised outside its findings said "read
in full by one of the second checks", which in this file reads as one of the seven sessions of the second check of the
corrections. Corrected. The heading: "S20 Table's rows 2, 5 and 8, read in full within the audit of the citations".

**X3-11** (note). The sentence of the introduction of the part on the second check that again no value of a result was
found wrong. Corrected. As X2-10.

**X3-12** (note). In the disposition of C32, "both" followed a sentence whose subjects are the Discussion's sentence
and the search note; the two places that name the second study are S3 Text §10 and the search note. Corrected. The
sentence: "Since the second check of the corrections, S3 Text §10 and the search note both name a second study of the
table".

**X3-13** (note). The disposition of W2-4. Corrected. As X2-9.

### X4: the statements about cited works changed or added after the second check, against the PDFs

**X4-1** (inexact). S20 Table's head note and row 1. Corrected. As X1-3.

**X4-2** (inexact). The pointer of the claim record's item on Luppi et al. (2026) put what the abstract names in S20
Table's row 5 and in the literature file "also"; that statement is in neither, S3 Text §10 has only that the abstract
names no drug, and what the title names is stated nowhere. Corrected. The pointer says which place states which part:
"Stated in S20 Table's row 5 and in the literature file, the statement of p. 1 apart" (and, since the fourth check,
the awake scans of the five macaques: Y4-2), and "Of the statement of p. 1, S3 Text §10 says that the abstract names
no drug, and the search note that it names no drug and none of the string's decomposition terms; what the title names
is stated at neither place".

**X4-3** (inexact). The pointer of the claim record's item on Gatica et al. (2024) named S3 Text §10 and the search
note without saying which states which part; the dose, the route, the purpose of the delay and what the title and the
keywords name are in the search note alone, and the five agents' names in neither. Corrected. The pointer: "S3 Text
§10 states the isoflurane, the injections of ketamine and of other agents, the two hours and that the abstract names
no drug"; the search note "adds the dose and the route of the ketamine, the number of the other agents, the purpose of
the delay and what the title and the keywords name; the names of the five other agents are stated at neither place".

**X4-4** (inexact). The heading and the pointer of the claim record's item on Down et al. (2026) left out S20 Table's
head note, which states the copy's pages too. Corrected. The heading: "(S20 Table, head note and row 6)"; the pointer
adds "that the copy holds pages 1–25 of 55, the main text and the references, is also in S20 Table's head note and in
the literature file's search paragraph".

**X4-5** (inexact). The disposition of VC-2. Corrected. As X3-4.

**X4-6** (note). The disposition of W7-3. Corrected. As X3-6.

**X4-7** (note). S3 Text §10 and the record had the macaques of Gatica et al. (2024) receive "an injection" of
ketamine; the work has injections, of six agents by two routes. Corrected. S3 Text §10: "received injections of
ketamine and of other agents". The record: "scanned under isoflurane after injections of ketamine and of other agents"
(the drug named in place of a pronoun since the fourth check: Y4-6).

**X4-8** (note). The claim record's "a PDF without a text layer" holds of the two Reporting Summaries but for single
glyphs: one character, an Ω, can be extracted from one of them. Corrected. The record says what can be extracted: "its
text is drawn as outlines, so that nothing can be extracted from the PDF as text but one character, an Ω on p. 3";
"from which nothing can be extracted as text but white space, thin spaces on p. 35, and which were read from images of
the pages" (the white space since the fourth check: Y4-5). The disposition of W7-5 quotes the two as they stand.

### The reading of S19 Table's Part B against the whole paper

The third check had found three cells of Part B short of a section and two computations without a row, and had not
read the rest of Part B for completeness (X1-11, X1-2). The planning session then had a further session read Part B
against the whole paper as it stood: for each of the thirteen rows every place of the main text, of the supporting
texts and of the supporting tables that quotes the computation, with the line and the words, and every computation
without a pre-run entry that the paper quotes and that had no row. Its report is beside this file
(`partB_reading.md`): the session returned it as text, and the planning session saved it as it stood from its heading
on. What was done with it:

(1) The table's head note states what the second column of Part B names: "the places of the main text (its list of
supporting information apart), of S1–S3 Text and of the supporting tables that print a value of the computation or a
number derived from one, name the computation as the source of what they say, or point to where it is reported; it
does not name S17 Table, which holds the intervals of the quantities that had a saved per-subject vector when B21 ran,
the checklist of S4 Text or the predictions that Part A quotes as recorded, some of which cite an earlier value, and
it names S5 Text only where S5 Text quotes the computation's values" (the clauses on S17 Table and on the predictions
as the fourth check left them: Y1-4, Y1-7). The report lists the places by kind; the rule takes those that it marks as
a value, a derived number or a naming, a place that prints the computation's own value counting whether or not the
numbers table names its output there (the Discussion's 1.4: Y1-10), and leaves out those that state a result in words
without naming the computation, those that it marks as mentions of the computation in the study's history or as
re-uses of its parameters, in S5 Text and elsewhere (the predictions that Part A quotes among them), and those where
the same number has another source: another computation by the text or the numbers table or, at two places, the
pipeline's own value, which a file of the review computations reproduces (the phase-randomised p of Table 2; the level
1.155 in Methods).

(2) Ten cells were completed by that rule: those of the review computations of 14 September 2026 (Results 4, which
prints none of their values, is no longer named; the captions of Fig 3 and Table 3, Methods' Remedies, S1 Text, S3
Text §7 to §10 and S11, S13, S15 and S20 Tables are), of the finite-sample null, of the sts-matched null, of the
spectral centroid, of global functional connectivity, of the checks of the review of 17 September 2026, of the
proportionality check, of the residual's source and of the two sets of derived numbers. Two cells name a place fewer,
by the rule: that of the leave-one-out on the primary DiD no longer names S4 Text, and that of the coupled family,
where the reading had kept S18 Table with a gloss (the family named in the rows of B23 (a3), whose values those are),
no longer names it since the fourth check (Y1-9). The cell of the leave-two-out stands.

(3) Five rows were added: the first review's own checks (`notes/review_checks.py`), three values of which S5 Text §1
quotes; the whole-brain ΦR items of the report on the regional ΦR check, three entered with no prediction and four
tests added outside the recorded plan, which S2 Text quotes; the third review's partial correlations (X1-2), with its
variations of the finite-sample null, which S3 Text §6 names without a value; the audit's transfer-entropy check
(X1-2); and the values that S5 Text §4 quotes from the text audit's computations on the released series.

(4) One number of S3 Text §6 was in no committed output: the interval of the difference between the runs in the
directed response, +0.00044 [−0.00061, +0.00149], which the text said was computed on 23 September 2026. Item 13 of
`derived_r24.out` now holds it, recomputed from the per-run file, and the text names the item. Item 6 gained the
Fisher-z intervals of all eight correlations of the whitened contrasts at p = 10 and 20, of which S3 Text §8 says that
seven include zero and which it now names; and S3 Text §6 names the output that holds the conversions of A_other
recomputed on B26's outputs (`conversions_b26.out`).

(5) S4 Text's item P5 said that both consequences of the band-pass for r₁ are stated in Results 7 and in S1 Text; S1
Text states the first. The item: "is stated in Results 7 (r₁ ≈ 0.82 for white noise at TR = 2 s, and r₁ ≥ 0.54 for any
series confined to the band) and, for the first of the two values, in S1 Text".

The report lists as borderline, and the table does not take as post hoc computations of its own: values that the
figure script writes into the captions from the outputs of computations that have entries; the conversion of the
run-level departure to a residual on the family, an evaluation that the outcome entry of the sign(q)-weighted
cross-lag deviation states (the shares 44 % and 37 % are arithmetic on it); arithmetic on printed values that the text
itself states (the Spearman–Brown ceilings; a closed-form share in S8 Table's note); the subject-alignment check, of
which no result is quoted; values that a pre-run entry lists as known; and the validation of the second
implementation, which the pre-specification of the regional ΦR check planned.

## The fourth check of the corrections

After the findings of the third check were settled and the reading of S19 Table's Part B used, four further sessions
of the AI system, started by the planning session later on 3 October 2026, checked the revision as it then stood: that
each disposition of the third check is true of the files, and that what had been changed since that check is itself
right. They read the revision as a commit made for the purpose on 8bd189e in the planning session's working directory
(26156b8, which is not in the repository; the tree that the four sessions of the third check had read was its branch
`checked3`), so that the line numbers in their reports are that tree's and the dispositions they quote are those of
this file as it then stood. In their reports VT is that clone and VW the directory in which they worked. The reports
are beside this file as the sessions returned them:

- `recheck_Y1.md` (Y1-1 to Y1-12): S19 Table: Part B read once more against the whole paper, the changed cells of Part
  A and the head note; 12 findings (0 errors, 7 inexact, 5 notes).
- `recheck_Y2.md` (Y2-1 to Y2-8): the changes of the supporting texts, and the derived numbers recomputed; 8 findings
  (0 errors, 4 inexact, 4 notes).
- `recheck_Y3.md` (Y3-1 to Y3-11): the record's new entries, the numbers table, the replacements file, the bookkeeping
  files and this file; 11 findings (0 errors, 4 inexact, 7 notes).
- `recheck_Y4.md` (Y4-1 to Y4-7): the statements about cited works changed or added after the third check, against the
  PDFs; 7 findings (0 errors, 2 inexact, 5 notes).

The four reports hold 38 findings, graded by the sessions as 0 errors, 17 inexact statements and 21 notes: none is
graded an error, and no value of a result in the main text or in the supporting information was found wrong; each new
value of `derived_r24.out` was recomputed by a session with code of its own and found equal. Three things were found
by two sessions, so that the findings are 35 different things. Two things that the third check had found short were
found complete: every computation that the paper quotes and that has no pre-run entry has a row in S19 Table's Part B,
and every contrast that the main text prints without an interval at any place is in the list of S4 Text's row R1 or
among its exceptions. What the sessions found inexact are, in the paper's files, the sentence of S19 Table's head note
on the last column of Part A, which promised more than the cells hold outside the values that the main text prints,
its clause on S17 Table, a file named for more than it holds in a new row of Part B, and the head of S2 Text with the
main text's list of supporting information, which the outcome now stated in S2 Text had made untrue of one result;
and, outside them, statements of this file and of the record's entry on the revision, two reasons recorded with
replacements, a pointer and a count of the claim record, and a comparison in `derived_r24.py` that was made on sorted
lists. Each finding was read against the files, and where it concerns a cited work against the PDF, before anything
was changed. Of the 38, 36 were corrected: a file of the commit was changed as the finding says, the dispositions
above among those files, so that they read as corrected. Two name something that is kept and that a text of the commit
now states as what it is. None is kept without a change. Where two sessions found the same thing, the disposition is
written once and the other points to it.

### Y1: S19 Table: Part B read once more against the whole paper, the changed cells of Part A and the head note

**Y1-1** (inexact). The sentence that the corrections for the third check had put into S19 Table's head note, that the
last column of Part A names the places of the paper that give a row's outcome by a value, by a derived number or in
words, is more than the cells follow outside the values that the main text prints: in fourteen rows a supporting text
or table repeats a value of the outcome, or gives a number derived from one, at a place that the cell does not name,
and S17 Table holds values of rows that do not name it. Stated. The cells are kept, and the head note says what the
column names and what it does not list: "In Part A the last column names where the row's outcome is reported: the
supporting text or table that reports the computation, and every place of the main text that prints a value of the
outcome. Some cells also name a place that gives a number derived from the outcome or that states it in words; the
column does not list every such place, or every place of the supporting information that repeats a value". By value,
in the main text, this check and the third found no outcome of the 81 rows printed at a place that its cell does not
name.

**Y1-2** (inexact). Of the places that state a row's outcome in words, with no value of it, some cells name one,
marked "(in words)", and other such places are not named: the third paragraph of Results 4 for four rows of B23, the
Abstract, the Discussion and Methods for others, S5 Text §1 for two cells that the third check's corrections had
changed, and S5 Text §4 with the opening note of the supporting tables. Stated. The cells are kept; the head note now
says that the column does not list every place that states an outcome in words (Y1-1).

**Y1-3** (inexact). The disposition of X1-8 said that by the rule the session had found no place missing from a cell,
and that of W3-4 that the cells had been completed with the places that give a number derived from the outcome or
state it in words; the third check had searched the values of the outcomes in the main text only, and had not treated
the places that state an outcome only in words as missing. Corrected. The disposition of X1-8 says that, by value, the
session found no place of the main text missing from a cell, and that of W3-4 what the reading completed and what some
cells also name.

**Y1-4** (inexact). The head note said of S17 Table that it "holds every saved per-subject quantity with its
intervals"; it holds the 932 quantities of B21's runs, and the per-subject values that B16c, B27 and B29 saved on 1
October 2026 are not in it. The closing section of the part on the third check quoted the clause. Corrected. The head
note: "S17 Table, which holds the intervals of the quantities that had a saved per-subject vector when B21 ran"; the
closing section quotes it so. S17 Table's own source note said the same of the table and now reads "All 932 quantities
that had a saved per-subject vector when B21 ran (B27's gaps, B29's counts of replaced volumes and B16c's quantities
at the fixed orders, which the run of 1 October 2026 saved, are not among them; the intervals that the paper gives of
these are in S3 Text §5 and §8 and in S11 Table)" (the parenthesis as the reading of these corrections left it: Z1-1).

**Y1-5** (inexact). The new row of Part B on the whole-brain ΦR items named
`notes/review_results/inference_rows_w30.csv` for the three items entered with no prediction; the file holds the first
of them, the contrasts at W = 30. Corrected. The cell names the log that holds the three, and the file for the first:
"(the deconvolved contrast at W = 30, the per-subject DiDs and the placebo run's series by window:
`notes/review_results/logs/rev_phir_items.log`; the first also in `notes/review_results/inference_rows_w30.csv`)".

**Y1-6** (inexact). The closing section of the part on the third check counted the conversion of the run-level
departure to 44 % and 37 % among arithmetic on printed values; the residuals that the departure gives are evaluations
on the family, which an outcome entry states, and the two shares alone are arithmetic. Corrected. The section's last
paragraph: "the conversion of the run-level departure to a residual on the family, an evaluation that the outcome
entry of the sign(q)-weighted cross-lag deviation states (the shares 44 % and 37 % are arithmetic on it)".

**Y1-7** (inexact). Point (1) of the same section did not account for all that the report lists and the cells leave
out: of the places that the report marks as mentions in the study's history, eleven are outside S5 Text, one of them a
prediction that Part A quotes with a value of the finite-sample null under its name ("near the null's 1.18"); and two
places were left out for a reason that the sentence did not give, the numbers table naming a file of the review
computations as their source. Corrected. The head note sets the predictions that Part A quotes aside, with S17 Table
and the checklist: "or the predictions that Part A quotes as recorded, some of which cite an earlier value" (among
them those of B17 (ii), of B19 (c) and of B17b's first row, each of which cites a value of a computation of Part B).
Point (1) says that the mentions of that kind are left out "in S5 Text and elsewhere", and gives the reason for the
two places: "the pipeline's own value, which a file of the review computations reproduces (the phase-randomised p of
Table 2; the level 1.155 in Methods)".

**Y1-8** (note). The second cell of the new row on the whole-brain ΦR items did not name Results 2, whose parenthesis
points to S2 Text for the scrutiny of a pre-injection gap, where other cells name places that only point. Corrected.
The cell: "Results 2 (S2 Text cited for the scrutiny of a pre-injection gap); S2 Text (the placebo run's share at W =
30, 56 %; the gap, the placebo run's slope and its decline from window 1 to window 4)".

**Y1-9** (note). The coupled family's cell kept S18 Table with a gloss which says that the table holds nothing that
the rule names (the family named in the rows of B23 (a3), whose values those are), and other places that name the
family in the same way were not named. Corrected. The cell no longer names S18 Table: "Results 1; Fig 1c; S3 Text §3".
Point (2) of the closing section says so.

**Y1-10** (note). The cell of the numbers derived on 24 September 2026 names the Discussion with Results 1 for the
ratio 1.4; the numbers table names the output at Results 1 and gives the same derivation at the Discussion without
naming it, so that by point (1) of the closing section, which followed the numbers table, the two places fell on
different sides. Corrected. The cell stands: both places print the ratio that item 5 of the output holds. Point (1)
says that "a place that prints the computation's own value" counts "whether or not the numbers table names its output
there".

**Y1-11** (note). The gloss of the row on `derived_r24.out` gave the inverted intervals of the contrasts at p = 10 and
20 to Results 7 and Table 4 together; Results 7 prints the interval at p = 20 alone. Corrected. The cell: "Results 7
(the inverted interval of the contrast at p = 20 and, in words, the Fisher-z intervals of the whitened correlations)
and Table 4 (the inverted intervals of the contrasts at p = 10 and 20)".

**Y1-12** (note). The record's count of what the corrections for the third check changed in S19 Table's Part B,
"twelve of Part B", is of the second cells of twelve rows; a thirteenth cell changed, the third of the row on
`derived_r24.out`. Corrected. The record: "six cells of Part A, in Part B the second cell of twelve rows and the third
of one, and five new rows of Part B". Found also by Y3-2.

### Y2: the changes of the supporting texts, and the derived numbers recomputed

**Y2-1** (inexact). With the outcome of the regional ΦR check stated in S2 Text, the text's head, "Every result in
this text is post hoc", and the same words of the main text's list of supporting information no longer held of every
result: that check had a prediction recorded before it was run, and S19 Table has it among the recorded predictions.
Corrected. S2 Text's head: "The results of the exploration and of the deconvolution are post hoc except the outcome of
the regional test, whose prediction was recorded before the test was run". The main text's list: "Their results are
post hoc except the outcome of a regional test whose prediction was recorded in advance" (both as the reading of these
corrections left them: Z1-3).

**Y2-2** (inexact). The reason recorded with the replacement in S2 Text and the disposition of X1-5 gave the values to
"the report's first table"; they are in its third, that of the section on the prediction. Corrected. Both say "the
report's table of the prediction (its section 1)".

**Y2-3** (inexact). The reason recorded with the replacement in S4 Text's item P5 said that the point was found "in a
reading of the supporting tables against the paper"; it was found in the reading of S19 Table's Part B. Corrected. The
reason: "found in the reading of S19 Table's Part B against the paper after a third check of the corrected revision".

**Y2-4** (inexact). The block that the third check's corrections added to item 6 of `derived_r24.py` says, in its
comment and in the line it prints, that each of the eight correlations is compared with the value printed for its
cell; it compared the two lists after sorting them, which would pass with two cells exchanged. The eight are equal
cell by cell. Corrected. The script reads each printed value under its cell's heading in B16c's tables file and
compares cell by cell; its line reads "each equal at three decimals to the r that
notes/review_results/partB/prewhiten_fixed_tables.md prints under the cell's heading".

**Y2-5** (note). S5 Text §1 says that three checks of the review of 17 September 2026 are quoted, as review
computations, in S3 Text §4, §6 and §9; §6 and §9 call theirs a computation of that review, and §4 gave the log's path
alone. Corrected. S3 Text §4: "(0 of 36,481; a computation of the review of 17 September 2026,
`notes/fresh_review_2026-09-17/checks/check_A1_atoms_family.log`)".

**Y2-6** (note). The first sentence of S4 Text's row R1 named Results 2–7 for the DiDs with inverted intervals and
exact p; Results 3 prints no DiD and Results 5 gives its DiDs with p alone, which the row's later sentences cover.
Corrected. The sentence names "Results 2, 6 and 7"; the disposition of X1-10 quotes it so.

**Y2-7** (note). The disposition of X1-1 and the reason recorded with the replacement in row R1 said that two
contrasts had no interval anywhere; that holds of the paper, and for one of the two the run's files held a percentile
interval. Corrected. Both say "at any place of the paper".

**Y2-8** (note). Two statements of the docstring of `derived_r24.py`, outside what the third check's corrections had
changed: item 2 gives the SDs of the two gaps and of the DiD, not of the three readings of the contrast; and the
script reads outputs of earlier computations beside those of the four of 1 October 2026. Corrected. The docstring:
"the between-subject SDs of the pre-injection gap, the post-injection gap and the DiD", and "those of B27, B28, B29
and B16c as the run wrote them and, for some items, earlier ones (of B4, B7, B11, B15, B16, B20 and B21, the inference
rows of the raw series and the regional atoms of the windowed estimator)".

### Y3: the record's new entries, the numbers table, the replacements file, the bookkeeping files and this file

**Y3-1** (inexact). The record's parenthesis, written for X2-7, called the four scripts of the parse check "the four
scripts that this commit adds or changes"; the commit adds a fifth, the audit's `te_filter_check.py`, which the check
did not cover. Corrected. The parse check covers the five (`checks/scripts_check_revision.out`), and the record says
"the parse check of the five scripts that this commit adds or changes (the figure script, `figures_check.py`,
`derived_r24.py`, the counter of the Abstract's and the Author summary's words and the audit's `te_filter_check.py`)".
The dispositions of X2-7 and W4-11 quote it so.

**Y3-2** (inexact). The record's "twelve of Part B". Corrected. As Y1-12.

**Y3-3** (inexact). The record's list of the corrections that the third check brought to the paper's files left out
one change of S3 Text §8, the pointer to the eight Fisher-z intervals in `derived_r24.out`, item 6. Corrected. The
list: "two outputs named in §6 and one in §8".

**Y3-4** (note). The same list left out S5 Text §5's clause, which names the third check, as the list written for the
second check had done before X2-5. Corrected. The list ends "S5 Text §5's clause on the audits names this check as
well".

**Y3-5** (note). The record and the introduction of the part on the third check said that no number, page, count or
quotation that the earlier corrections had changed or added was found wrong; one thing graded inexact, found by two
sessions (X2-1, X3-5), is of counts that the correction for W4-1 had written, and its correction changed them.
Corrected. Both say what holds of all 42: "no value of a result in the main text or in the supporting information was
found wrong".

**Y3-6** (inexact). The disposition of W3-10, as amended for the third check, quotes the sentence of S4 Text's row R1
as it stands and gave the places of its first form, without those of the four contrasts that the third check added.
Corrected. The disposition gives the places of the list as it stands: "(S2 Text; S3 Text §4, §5, §6 and §8; S1, S11,
S14 and S17 Tables)".

**Y3-7** (note). The disposition of W3-8, as amended, gave items 13 and 14 as what raised the counts of the files that
`derived_r24.py` reads; the fifth tables file is read by the addition to item 6. Corrected. The disposition: "which
added items 13 and 14 and the additions to items 1 and 6, the last of which reads a tables file".

**Y3-8** (note). The parenthesis of the disposition of R56 on the files that the README names had not been carried
along: the README now names `partB_reading.md` too. Corrected. The parenthesis: "(the three reports,
`te_filter_check.py`, the reports of the checks, the report of the reading of S19 Table's Part B and this file)".

**Y3-9** (note). The introduction of the part on the third check says that X2 took two of its notes from the report of
X3; nothing in the tree says so, the report of X2 naming X3 nowhere. Corrected. The sentence says where the statement
comes from: "as that session said when it returned its report, which does not say it".

**Y3-10** (note). The reason recorded with the two replacements of row 1 in the literature file was that of S20
Table's, word for word, and named "the table's head note"; the literature file has no head note, and its sentence
stands in its search paragraph. Corrected. The reason of the two names "the file's search paragraph". Found also by
Y4-7.

**Y3-11** (note). The claim record's head said that the third check "made four pointers say which place states which
part of an item"; three pointers were changed, and the heading of one item. Corrected. The head: "which made three
pointers say which place states which part of an item, added the head note to a heading and corrected the description
of the two Reporting Summaries". Found also by Y4-1.

### Y4: the statements about cited works changed or added after the third check, against the PDFs

**Y4-1** (inexact). The claim record's head, "four pointers". Corrected. As Y3-11.

**Y4-2** (inexact). The pointer of the claim record's item on Luppi et al. (2026), as rewritten for X4-2, still put
one part of the item in S20 Table's row 5, which does not state it: that the five macaques of p. 3 were scanned awake
too. Corrected. The pointer: "the statement of p. 1 apart and, of p. 3, that the five macaques were scanned awake too;
the anaesthetics of the macaques are also in S3 Text §10 and in `../pubmed_search/psychedelic_phiid_search.md`, which
say as well that they were scanned awake".

**Y4-3** (note). S20 Table's head note says that a row names what it draws from outside a study's article; row 5 names
the Reporting Summary of Luppi et al. (2026) and cites pages of it fifteen times by page alone, and neither the row
nor the head note gave the pages of the three parts of the PDF. No other row cites a page of supplementary material
without naming it. Corrected. Row 5 gives them where it says what was read, in S20 Table and in the literature file:
"(the PDF read, whose pp. 1–26 are the article, pp. 27–32 the Extended Data and pp. 33–41 the Reporting Summary; the
Supplementary Methods the article defers to were not read)". The disposition of VN-3 quotes the cell so.

**Y4-4** (note). Row 1 gave "3 T" with p. 13 of the article and p. 36 of the Reporting Summary; for the HCP data the
article's p. 13 gives a field strength of the diffusion scan alone, and the Reporting Summary gives it of the dataset.
Corrected. The cell, in both files: "first ten volumes removed (p. 13), 3 T (the Reporting Summary, p. 36; the article
gives the field strength for the diffusion scan, p. 13)". The disposition of X1-3 quotes it so.

**Y4-5** (note). The claim record said of the Reporting Summary of Luppi et al. (2026) that no text can be extracted
from it; its p. 35 holds glyphs that the font maps to a thin space, so that white space, and no visible character, can
be extracted. Corrected. The record: "from which nothing can be extracted as text but white space, thin spaces on p.
35". The dispositions of X4-8 and W7-5 quote it so.

**Y4-6** (note). In the record's sentence on the two studies whose macaques were given ketamine, "after injections of
it and of other agents" followed "isoflurane", which was inhaled, so that the pronoun could be read of it. Corrected.
The record names the drug: "scanned under isoflurane after injections of ketamine and of other agents". The
disposition of X4-7 quotes it so.

**Y4-7** (note). The reason of the two replacements of row 1 in the literature file. Corrected. As Y3-10.

### The reading of these corrections

The corrections made for the fourth check were read by two further sessions of the AI system, started by the planning
session later on 3 October 2026, each against the files and the findings that the corrections answer. They read the
revision as a commit made for the purpose on 8bd189e in the planning session's working directory (9f89c23, which is
not in the repository; the tree that the four sessions of the fourth check had read was its branch `checked4`). Their
reports are beside this file as the sessions returned them:

- `reading_Z1.md` (Z1-1 to Z1-3): the paper's files, the script of the derived numbers, the claim record and the
  reasons of the replacements; 3 findings (0 errors, 2 inexact, 1 note).
- `reading_Z2.md` (Z2-1 to Z2-5): the record, this file and the bookkeeping files; 5 findings (0 errors, 3 inexact, 2
  notes).

The two reports hold 8 findings, graded 0 errors, 5 inexact statements and 3 notes; one thing was found by both, so
that the findings are 7 different things, and none is of a value of a result in the main text or in the supporting
information. One of the two searched again, by value, every outcome of S19 Table's Part A in the main text, and found
none printed at a place that its cell does not name. The 8 were corrected as the paragraphs below say. What was done
about them was verified by the planning session with the checks of the build (the replacements applied to 8bd189e, the
validators of the numbers table and the search of the files for every quotation of this file) and was not read by a
further session.

**Z1-1** (inexact). The parenthesis that the correction for Y1-4 had put into S17 Table's source note held of a part
of what the run of 1 October 2026 saved: the per-subject DiDs of B27's file are quantities that the table holds, as
are the DiDs of the mean framewise displacement and of r₁ that B29's file gives by window, and of B16c's 264 rows the
three places named give the intervals of 25. Corrected. The parenthesis names what the table does not hold, and says
of which intervals the three places are the place: "(B27's gaps, B29's counts of replaced volumes and B16c's
quantities at the fixed orders, which the run of 1 October 2026 saved, are not among them; the intervals that the
paper gives of these are in S3 Text §5 and §8 and in S11 Table)". Found also by Z2-5.

**Z1-2** (inexact). The reason recorded with the replacement of S19 Table's head note and the disposition of Y1-7
counted three predictions of Part A that cite a value of a computation of Part B; at least four more carry numbers
that come from such computations (those of B17 (i), of B17b (i), of the sign(q)-weighted cross-lag deviation and of
B27 (a)). The head note's own words, "some of which cite an earlier value", hold. Corrected. Both name the three as
examples and give no count: "among them those of B17 (ii), of B19 (c) and of B17b's first row".

**Z1-3** (note). The head of S2 Text and the main text's list, as corrected for Y2-1, said that every result in the
text is post hoc except the outcome of the regional test; the text also quotes, for comparison, two values of the
pre-specified analysis, the raw sts level and its contrast, as it did before the head was changed. Corrected. The two
sentences speak of the results of the exploration and of the deconvolution. S2 Text's head: "The results of the
exploration and of the deconvolution are post hoc except the outcome of the regional test, whose prediction was
recorded before the test was run". The main text's list: "Their results are post hoc except the outcome of a regional
test whose prediction was recorded in advance".

**Z2-1** (inexact). The record's sentences on the fourth check said that the parse check covers "the fifth script that
this commit adds"; the commit adds four scripts and changes one. Corrected. The record: "the fifth of the scripts that
this commit adds or changes".

**Z2-2** (inexact). The disposition of Y1-4 said that the reason recorded with the replacement had repeated the clause
on S17 Table; the finding names the replacement's new text, which is the head note itself, and no reason held the
clause. Corrected. The disposition says that the closing section of the part on the third check quoted the clause.

**Z2-3** (note). In the disposition of W4-11, as amended, "four when the second check read it" could be read of the
record's list, which named no parse check when the second check read it: the words on the four scripts came into the
list as the correction for that finding. Corrected. The parenthesis: "(of the four scripts when this correction was
made; the check covers the fifth since the fourth check, Y3-1)".

**Z2-4** (note). Point (2) of the closing section of the part on the third check still counted the coupled family's
cell among eleven cells completed by the rule; since the correction for Y1-9 that cell names one place fewer than
before the reading of Part B. Corrected. Point (2) counts ten cells completed and two that name a place fewer by the
rule, the leave-one-out's and the coupled family's.

**Z2-5** (inexact). The parenthesis of S17 Table's source note. Corrected. As Z1-1.
