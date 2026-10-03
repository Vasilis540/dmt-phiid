# Audit of the revision of 1–2 October 2026 (bundle 35B): the record and the outcome entries

Audited: the prepared commit on 8bd189e, i.e. the working tree after the 188 replacements, by a separate session on
2 October 2026. Line numbers are those of the working tree unless "HEAD" is said; "CSV line" is a line of
`manuscript/main_text_numbers.csv`.

**The setup.** Steps 1, 2, 3 and 5 gave what the prompt requires (HEAD `8bd189e7f03312c1630764a63e6360440760f4f4`
with the stated subject; the tarball's sha256; 16 untracked files; `418`, tab, `0`). Step 4 did not print the required
line: see R44. I did not stop there, because the application itself was complete by its full output (188 `ok` lines,
"all 188 entries applied; files written:", the whole output byte-identical to `checks/apply_revision.out`, 15 files
changed); the planning session should read R44 first and decide whether that was right.

**What I did and did not do.** I changed no file of the clone: `git status --porcelain --untracked-files=all` has 31
lines (15 modified, 16 untracked) before and after, and the 15 written files still have the sha256 the application
printed. I read no subject data: the data release was not cloned, and B27, B29 and B16c were not re-run; their tables
were recomputed from the committed per-subject files (`baseline_gap.csv`, `censoring.csv`,
`inference_rows_prewhiten_fixed.pkl`, `splithalf_subjects.csv`). B28, which reads no data, was re-run in a scratch
copy of the tree. Python 3.13.15, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.2 (the run: 3.12.3 and 3.11.1).

**Count.** 57 findings: 1 blocking, 12 should fix, 30 minor, 14 notes. A finding marked "record" in its Where concerns a
sentence of the five new entries, which cannot be edited once committed.

---

## Blocking

### R01 — blocking
Where: `manuscript/si/S5_Text.md` §5 (line 29); replacement S502
Text: "the revision that answers them was audited by separate sessions before it was committed (`notes/review_2026-10-01_cold_reads/audit/`; @@AUDIT_TEXT@@)."
Problem: An unfilled placeholder stands in a manuscript file. The prompt names «ENTRY_TIME» in the record's five headings as the only placeholder to be filled after the audit; nothing says who fills this one or with what, so the sentence on the audits, which check 5 asks me to audit, is not in the tree. The folder it names holds the earlier commit's `findings.md` and `dispositions.md` and nothing of this revision yet.
Evidence: `grep -n '@@' manuscript/si/S5_Text.md` gives line 29 only; the same string is in the replacements JSON (S502, whose `why` is "The cold reads and audits of 1–2 October 2026 added (S5 Text §5)"); no other `@@…@@` in the changed or new files.

## Should fix

### R02 — should fix
Where: `manuscript/draft_v2.md`, Results 2, third paragraph, last sentence (line 108), added for C's m18
Text: "the pre-specified intensity-tracking criterion, the group-mean sts series against the ratings over the decay windows, was met in sign (Spearman ρ = −0.98) and void under its pre-specified controls (S1 Text; S2 Table)."
Problem: The sentence reads the value the wrong way round. The criterion was passed in size (|ρ| ≥ 0.80) and the sign was against the pre-registered direction, which was positive.
Evidence: record lines 1448–1451: "both PASS the |ρ| ≥ 0.80 threshold, sign negative against the pre-registered positive direction"; S2 Table's note (`supplementary.md` line 21): "Every ρ_S of sts is negative, against the pre-specified positive direction", and its row "−0.9833 (0.0020), PASS"; S1 Text line 11: "The tracking was significant and negative".

### R03 — should fix
Where: record, "B28, outcome", (c) (lines 8992–8993); `draft_v2.md`, Results 4, second paragraph (line 124); `S3_Text.md` §6 (line 400); CSV lines 793–794
Text: "and the ramp moves the generators' mean residual DiD by 0.0002 and 0.0007 nats from the step."
Problem: Both values are differences of the table's four-decimal means (+0.0022 − +0.0020; +0.0049 − +0.0042), a second rounding. From the replicates the differences are 0.00015 and 0.00062, which print as 0.0001 and 0.0006. The record's (c) has the same two values ("band-passed 0.0002 (yes), AR(1) 0.0007 (yes)"). The verdict (within 0.003) is not affected.
Evidence: `matched_slope.csv`, column `res_did`, means over the 100 replicates: +0.002182 (i) and +0.002034 (ii); +0.004851 (iii) and +0.004232 (iv). The numbers table's rows give the derivation: "|+0.0022 − +0.0020| = 0.0002" and "|+0.0049 − +0.0042| = 0.0007".

### R04 — should fix
Where: `draft_v2.md`, Fig 5's caption, (c) (line 122); record, the revision entry, C m9 (lines 9244–9245); `scripts/15_figures_v2.py` (lines 22 and 439) and the caption it writes
Text: "drawn at four times the nats per unit height of (a) and (b) (y-range −0.02 to +0.03 nats)"
Problem: The reverse holds. Panels (a) and (b) span 0.30 and 0.20 nats at height ratios 0.30 and 0.20; panel (c) spans 0.05 nats at height ratio 0.20, a quarter of their nats per unit height: it is magnified four times. Panel (b)'s title uses "same nats per unit height" in the direct sense. The record adds "which its title and caption say"; the title says "(y-scale four times that of a and b)".
Evidence: `scripts/15_figures_v2.py` lines 438–440: `YL_A, YL_B = (1.00, 1.30), (-0.15, 0.05)`; `YL_C, H_C = (-0.02, 0.03), 0.20`; `height_ratios=[YL_A[1] - YL_A[0], YL_B[1] - YL_B[0], H_C]`; line 465 (the title). At HEAD (c) spanned 0.10 nats at height ratio 0.10.

### R05 — should fix
Where: `manuscript/si/S3_Text.md` §5, "What the tables say" (line 218)
Text: "The three readings of the contrast agree in sign on both variants and at both window lengths, the adjusted contrast lying between the DiD and the post-injection gap."
Problem: In none of the three cells does the adjusted contrast lie between the other two. It is the smallest in size in each; the post-injection gap lies between.
Evidence: table (a) of the same section and `baseline_gap_tables.md`, sts: ts_gsr, W = 60: DiD −0.0809, post-injection gap −0.0633, adjusted −0.0544; ts_demean: −0.1031, −0.0846, −0.0796; W = 30: −0.0686, −0.0526, −0.0453.

### R06 — should fix
Where: `draft_v2.md`, Results 2, first paragraph (line 87); replacement R201; record, the revision entry, B MINOR 6 (line 9195); `S1_Text.md` (line 9); `CLAUDE.md` (lines 22–24 and rule 9, line 650); `README.md` (lines 14–15)
Text: "it was planned as a test of an increase, its two-sided statistic was fixed after global fits on the same data had shown the decrease (Methods), and on the account of Results 1 it bears on MMI-sts"
Problem: The committed sentence "under the directional-failure rule the significant decrease refutes that hypothesis as operationalised" is removed, and the main text no longer says anywhere that the decrease refutes the hypothesis. The replacement's reason is that Methods states the rule; Methods says only when the rule was written. The second half of B's MINOR 6 (the sentence "should say that the pre-registered increase failed regardless of the two-sided p") is not answered, though the disposition reads "Results 2 and Methods (Inference) say so". S1 Text still points to Results 2 for the refutation, and `CLAUDE.md` and `README.md` still say the decrease is reported as a refutation. The removal is not among the statements that "The length and the tables" lists.
Evidence: `git show HEAD:manuscript/draft_v2.md`, line 87; `grep -c refut manuscript/draft_v2.md` is 0; R201's `why`: "the sentence on the directional-failure rule, which Methods states, is not repeated"; `draft_v2.md` line 261: "The directional-failure rule and the windowed test statistic were written on the next day"; `S1_Text.md` line 9: "Under the directional-failure rule this refuted the up-regulation hypothesis as operationalised … (main text, Results 2)"; `CLAUDE.md`: "The observed decrease is a refutation. Do not reframe it."; `reviews/read_B.md`, MINOR 6.

### R07 — should fix
Where: `draft_v2.md`, Data and code availability (line 267)
Text: "The repository's full history is public, and every result table and report names the commit that produced it in its header."
Problem: The condensation dropped the exceptions that the committed sentence gave ("`-dirty` where the tree had uncommitted changes; `nogit` for files written outside a commit; S5 Text lists the files of the last two kinds and those that carry none"). As it stands the sentence is contradicted by S5 Text §4 and by the files.
Evidence: `S5_Text.md` §4 (line 25): "apart from five CSV files that carry no header by design (named below) and those that `run_all.sh` writes only with the deconvolution sandbox present …, which carry none"; `notes/review_results/inference_rows_raw.csv` begins with its column names; `results/synergy_bins_20regions_ts_gsr_global.csv` carries `git=nogit`.

### R08 — should fix
Where: record, the revision entry, "The checks" (line 9283); `manuscript/si/S3_Text.md` lines 189, 222, 391 and 525; `manuscript/si/S5_Text.md` §4 (line 25)
Text: "The main text carries no computation label and the manuscript files no process label."
Problem: Four sentences added to S3 Text name the cold reads by the reviewers' letters with their finding numbers: "(B, MAJOR 1–3)", "(C, m1–m3)", "(A, M1; B, MAJOR 3)", "(A, m4; B, MINOR 4)". The sentence added to S5 Text §4 names "the planning session's `b27_start.sh`"; `CLAUDE.md` says the session names are "defined once in S5 Text §5", and at HEAD they occur in §5 only. The prompt's check 4 counts both kinds as process labels; its grep does not match them (its pattern is "reviewer [ABC]").
Evidence: `git diff HEAD -- manuscript/si/S3_Text.md manuscript/si/S5_Text.md`; `git show HEAD:manuscript/si/S5_Text.md | grep -n "planning session"` gives line 27 (§5) only; `CLAUDE.md` line 19.

### R09 — should fix
Where: `manuscript/main_text_numbers.csv` (CSV lines 982, 1268, 1229, 1259); `checks/numbers_update.out`; record, "The checks" (lines 9279–9283)
Text: "Every number of the revised main text (title to Materials and methods, the captions, the tables, Data and code availability, the Supporting-information captions) has a row"
Problem: (1) Two rows have no occurrence left. The row of the unsigned 0.0112 of Results 6 (CSV line 982): the sentence no longer prints it, and the row's context is now that of "+0.0112", which has its own row (line 981). The row "20, label, date" of Methods, Literature search (line 1268): "20 September" left the paragraph, and its context is now "…marked (S20 Table)." (2) Two occurrences in changed paragraphs lost their rows and got none: "p ≤ 0.05" in Methods, Inference (two 0.05, one row, line 1229) and "p fixed at 1" in Methods, Remedies (two 1, one row, line 1259). So the head note's "one row per occurrence" does not hold in four places, 2 of the 1,302 rows count nothing, and check 6's condition (a deleted row's number absent from its paragraph or present with a new row) fails twice.
Evidence: my scan of every block of `draft_v2.md` against that block's rows, at HEAD and in the working tree. HEAD's CSV lines 965 (0.0112), 1155 (20), 1121–1122 (the two 0.05) and 1151 and 1153 (the two 1); `draft_v2.md` lines 154, 253, 237 and 249.

### R10 — should fix
Where: `draft_v2.md`, Methods, Dataset (line 213); `S1_Text.md` (line 5); record, "B29, outcome", item (i) (lines 9040–9042); `claims/claims_2026-10-01.md` (lines 12–14)
Text: "excluded six of the twenty participants for more than 20 % of such volumes (Timmermann et al., 2023; Singleton et al., 2025, Methods and Reporting Summary)"
Problem: The revision's own claim record gives a different count for Timmermann et al. (2023), "four discarded … in the 8-min post-DMT period, three more for the dynamic analysis over 28 min"; the six of twenty is Singleton et al. (2025)'s. The claim record says that Timmermann's count is "Stated in S4 Text (D4) and beside Singleton et al. (2025)'s count in the main text's Dataset paragraph"; neither states it (S4 Text D4 cites Singleton et al. alone). The outcome entry attributes "the exclusion of six participants" to "the Methods of Timmermann et al. (2023) and Singleton et al. (2025)". I could not read the PDFs, which are not in the repository; the inconsistency is between the claim record and these three places.
Evidence: `claims_2026-10-01.md` lines 12–14 and 31–33; `S4_Text.md` line 12.

### R11 — should fix
Where: `manuscript/si/S3_Text.md` §10 (line 550)
Text: "its 11 records, their screening and PubMed's own reading of the string are in the literature file's folder."
Problem: PubMed's reading of the string was not kept. And the records and the screening are in `notes/review_2026-10-01_cold_reads/pubmed_search/`, not in the folder of the literature file (`notes/partB5_literature_v2.md`).
Evidence: `pubmed_search/search_string.txt`: 'how PubMed read the string (the query's "Search details") was not kept at the time of the search and is not recorded here'; record, the revision entry (line 9134): "`search_string.txt` records that PubMed's reading of the first string (its Search details) was not kept".

### R12 — should fix
Where: `draft_v2.md`, Abstract, first sentence (line 15), against Introduction (line 25) and Discussion, The literature (line 191); record, the revision entry, C m7
Text: "Integrated information decomposition (ΦID) with the minimum-mutual-information (MMI) redundancy function underlies the fMRI synergy reports we found."
Problem: The revision replaced "most fMRI synergy reports" by a statement about all the reports found. The Introduction counts eight of the ten studies as stating MMI and one as using CCS on binarised signals in its primary analysis, and the Discussion says that the tenth does not state its redundancy function. The disposition of C's m7 names the Introduction, the Discussion and Methods, not the Abstract.
Evidence: `draft_v2.md` line 25 ("eight state the minimum-mutual-information (MMI) redundancy function …, and one uses the common-change-in-surprisal (CCS) function"); S20 Table, rows 2 ("primary **CCS plug-in on mean-binarised signals**") and 9 ("redundancy function, estimator and lag not stated").

### R13 — should fix
Where: record, the revision entry, C m19 (line 9255); `CLAUDE.md` (line 19)
Text: "m19 (the Abstract's length): 300 words (the check's output)."
Problem: The check's output is 299 words, as the same entry's paragraph "The checks" says. `CLAUDE.md` keeps "abstract 300 words", which is true of the committed text and not of the revised one.
Evidence: `checks/abstract_summary_revision.out`: "abstract 299 words (limit 300); author summary 200 words (limit 200)"; my run of `abstract_summary.py` gives the same, and 300 on `git show HEAD:manuscript/draft_v2.md`.

## Minor

### R14 — minor
Where: `manuscript/si/S3_Text.md` §8 (line 538)
Text: "with the per-subject correlation of the sts DiD with the whitened r₁ DiD at +0.45 and +0.33 against +0.495 at p ≤ 5"
Problem: The correlation at p = 10 is +0.44487 (+0.445 in the table above the sentence); to two decimals it is +0.44. "+0.45" rounds the rounded value.
Evidence: the per-subject vectors of `inference_rows_prewhiten_fixed.pkl` (primary set): r = +0.44487 at p = 10 and +0.33275 at p = 20; `prewhiten_fixed_tables.md` lines 28 and 126.

### R15 — minor
Where: `draft_v2.md`, Abstract (line 15) and Discussion, What the finding is and is not (line 183); CSV lines 33, 1119 and 780
Text: "a test detecting 0.016 does not resolve this (p = 0.11–0.25)"
Problem: 0.016 is the table's 0.0155 rounded again (the rows' note: "to three decimals"). From the committed per-subject values the minimal detectable difference is 0.0155000, between 0.0154998 and 0.0155002 under the CSV's six-decimal rounding, so the committed files do not decide between 0.015 and 0.016. Results 4 and S3 Text §5 print 0.0155. The note of the row of 0.0155 (CSV line 780) says "12 df"; the source says "one-sample t, 13 df".
Evidence: `baseline_gap.csv` (residual, ts_gsr, W = 60): SE 0.0051146 × 3.030520 (the two t quantiles on 13 df) = 0.0155000; `baseline_gap_tables.md` line 43; `notes/partB27_baseline_gap.py` line 190.

### R16 — minor
Where: `draft_v2.md`, Results 3 (line 114); record, the revision entry, A m9
Text: "The map's slope on regional r₁, 3.09 nats per unit (2.65 per subject; S3 Text)"
Problem: The source prints +2.6450, so the second decimal is a tie that the committed files cannot decide (the per-subject slopes are not saved). 2.65 is the four-decimal value rounded again.
Evidence: `regional_partial_tables.md` line 74 and `S3_Text.md` line 154: "+2.6450"; the row's own locator (CSV line 665) holds "+2.6450".

### R17 — minor
Where: record, "B16c, outcome", "The outputs" (lines 9057–9058)
Text: "(the 264 inference rows of the eight cells' MMI-sts, CCS-sts, xtx + yty and autocorrelation, every set)"
Problem: Those four quantities in eight cells and six sets are 192 rows. The other 72 are the diagnostic's observed, predicted and residual sts in the four W = 60 cells, which the parenthesis does not name.
Evidence: `inference_rows_prewhiten_fixed.csv`: 264 rows = 44 labels × 6 sets; 32 labels of the four quantities, 12 labels "diag observed/predicted/residual sts".

### R18 — minor
Where: `manuscript/si/S5_Text.md` §4 (line 25), the sentence on the run
Text: "no tracebacks; every output carrying `git=13e7299`; committed as 8bd189e by `b27_commit.sh`"
Problem: Twelve of the 29 outputs carry the commit (four tables, four CSVs, four logs). The sixteen atom arrays and the pickle carry none. The outcome entries and the folder's README say it exactly ("each table, CSV and log"; "the twelve text files among them").
Evidence: `b27/b27_commit.sh` (its header checks run over `TABLES`, `CSVS` and `LOGS`); `b27/outputs.sha256` (29 files, 17 of them `.npy` or `.pkl`).

### R19 — minor
Where: record, the revision entry, A m8 (lines 9154–9156); `draft_v2.md`, Supporting information, S3 Text's caption (line 397) and Discussion, The literature (line 191)
Text: ""scope map" retired from the text, the file names staying; S3 Text §4's heading, S20 Table's title and column, and the SI list follow."
Problem: The main text's list of supporting information still describes S3 Text as holding "the scope map, the within-window regression and the regional maps"; only S20 Table's entry of that list was changed. With Fig 1 retitled, "the map" of the Discussion ("the reported effect on the map"; "what the map predicts") has no referent left in the main text, where "the map" is otherwise the regional map. `S5_Text.md` line 7 keeps "scope map" in a list of the plans of 14 September.
Evidence: `draft_v2.md` lines 397 and 191; the second replacement with the id M07 (`why`: "A's m8: S20 Table's title in the list of supporting information").

### R20 — minor
Where: record, the revision entry, A m4 (lines 9147–9149), and "B16c, outcome", item (ii); `draft_v2.md`, Recommendations (line 197)
Text: "the recommendation names whitening before the band-pass or no band-pass (B16c's rule (ii))"
Problem: Recommendations says "whiten before band-pass filtering, or report the in-band power share beside any prewhitened atom". "No band-pass", and that the released derivatives cannot test the remedy, are in Results 7 only. The rule asked for them in the recommendation.
Evidence: `draft_v2.md` lines 197 and 158; the pre-run entry's rule (ii) (record lines 8863–8868).

### R21 — minor
Where: record, the revision entry, A w4 (lines 9173–9174); `draft_v2.md`, Abstract (line 15)
Text: "w4 (the 4.7-to-1 ratio's qualifying clause): Abstract: per within-window standard deviation of the pairs, neither input being lagged coupling (C's w4)."
Problem: The Abstract has "(4.7 to 1 per within-window standard deviation); lagged coupling can move it either way". It has neither "of the pairs" nor the qualifying clause A asked for ("neither input is lagged coupling"); the clause on lagged coupling that follows was in the committed Abstract already. C's w4 ("within a window") is answered.
Evidence: `draft_v2.md` line 15; `reviews/read_A.md`, w4.

### R22 — minor
Where: record, the revision entry, B MINOR 9 (lines 9201–9202), and "B27, outcome", item (v) (line 8953); `draft_v2.md`, Methods, Inference (line 237)
Text: "MINOR 9 (the OLS and Fieller assumptions and Fieller's g): Methods (Inference) states both and g; Results 2 and Results 4 state g where the Fieller intervals are quoted."
Problem: Methods states the assumption of the t intervals ("normal residuals of constant variance") and, for the Fieller intervals, g and the condition for a finite interval; it states no assumption of the Fieller interval. B's third request, a leave-one-out of each slope, is answered for the residual's slope (Table 3) and not for the slope of the sts DiD on the r₁ DiD (4.26), for which S3 Text §5 gives only the range of r; the disposition does not say so.
Evidence: `draft_v2.md` line 237; `reviews/read_B.md`, MINOR 9; the pre-run entry's rule (v) (record lines 8662–8663).

### R23 — minor
Where: `draft_v2.md`, Fig 4's caption (line 116); record, the revision entry, B W3 (line 9206)
Text: "Partialling removes the pre-defined sensory–association contrast at its point estimate but not all network structure."
Problem: The word that B's W3 objected to ("reads as pre-registered") is replaced in Results 3 and stays twice in the caption of the figure that shows the contrast (also "(b) The pre-defined contrast between sensory cortex").
Evidence: `reviews/read_B.md`, W3; `draft_v2.md` lines 114 and 116. Fig 4's caption is not among those that "The figures" lists as changing.

### R24 — minor
Where: record, the revision entry, C m2 (lines 9232–9234); `draft_v2.md`, Methods, Dataset (line 213); `S4_Text.md`, P8 (line 41)
Text: "m2 (the non-finite TR's place): Methods, S1 Text, S3 Text §5 and S4 Text P8: the last TR of subject 3's placebo run, at the end of window 14."
Problem: S1 Text and S3 Text §5 say that. Methods and S4 Text P8 say "the last of one placebo run": neither the subject nor the window.
Evidence: `draft_v2.md` line 213; `S1_Text.md` line 5; `S3_Text.md` line 255; `S4_Text.md` line 41.

### R25 — minor
Where: record, the revision entry, C M5 (b) (line 9226); S20 Table, rows 3 and 5
Text: "(b) the eight observations removed from S20 Table and the literature file;"
Problem: C's M5 (b) lists seven (rows 2, 3, 1, 4, 6, 8 and 11). The eighth replacement with that reason (U17.5) rewords row 5's statement on HRF deconvolution, which is C's M4 and removes nothing. In row 3 the observation is shortened and stays: 'N = 15 (pp. 4, 8; "n=16 for analysis", p. 15)'.
Evidence: `reviews/read_C.md`, M5 (b); replacements U17.1–U17.8; `supplementary.md`, S20 Table A.

### R26 — minor
Where: record, "B27, outcome", item (ii) (lines 8945–8946); `draft_v2.md`, Results 2 (line 87)
Text: "(ii) The scrutiny S2 Text applies to the deconvolved ΦR contrast is applied to sts in Results 2 in the same words."
Problem: The words differ. S2 Text has "a pre-injection baseline gap in the direction that creates it"; Results 2 says the gap "lies in the direction that enlarges the DiD".
Evidence: `S2_Text.md` line 9; `draft_v2.md` line 87; the pre-run entry's rule (ii) (record lines 8652–8654).

### R27 — minor
Where: record, "B27, outcome", item (iv) (lines 8950–8952); `draft_v2.md`, Results 4 and Table 3 (lines 131–132)
Text: "(iv) Results 4 reports the residual's slope and, as rows of its Table 3, the leave-one-out and leave-two-out ranges and counts and the three named omissions;"
Problem: The rule asked for "the ranges and counts of (c)". Table 3 gives the counts of intervals that contain zero (0 of 14; 1 of 91). The counts for the three rates (−0.18: 0 and 13; −0.39: 11 and 71; −0.37: 11 and 63) are in S3 Text §5 only.
Evidence: `draft_v2.md` lines 131–132; `S3_Text.md` line 216; the pre-run entry's rule (iv) (record lines 8660–8662).

### R28 — minor
Where: record, "B29, outcome", item (ii) (lines 9043–9045); `draft_v2.md`, Limitations (line 201)
Text: "while the lower r₁ of the windows holding replaced volumes is motion's own mark (Results 2)"
Problem: The entry says that Limitations states "the correlations of (b) and (c)". Limitations gives one of each, both on ts_gsr (−0.124 within runs; −0.107 across subjects). The within-run correlation on ts_demean (−0.025), which the prediction named ("on both variants"), and the other correlations of (c) are in S3 Text §5 only. The reading quoted is not a result of the computation: the prediction of a positive correlation was missed, and on ts_demean the two means are 0.8342 and 0.8352.
Evidence: `censoring_tables.md` (b) and (c) (lines 28–36); the pre-run entry's prediction (b) and rule (ii) (record lines 8796–8798 and 8806–8809).

### R29 — minor
Where: `draft_v2.md`, Results 7, first paragraph (line 158); `S3_Text.md` §8 (line 538)
Text: "tracking the whitened series' own r₁ DiD (−0.0927) at r = +0.333, of which the AR(1)-substituted estimate carries −0.0037"
Problem: r = +0.333 over 14 subjects has a Fisher-z interval, the paper's interval for a correlation, of about [−0.24, +0.73]; the same paragraph says that the contrast at p ≤ 5 "still tracks" at r = +0.495 (about [−0.05, +0.81]). Results 6 calls CCS-sts's correlations of −0.43 to −0.27 weak, "each Fisher-z interval including zero at N = 14", and Fig 6's caption calls r = +0.626 "only partial". S3 Text says that the contrast "tracks … at the correlations above", which include +0.157, +0.081 and −0.079.
Evidence: `prewhiten_fixed_tables.md` lines 28, 126, 151, 175 and 200; `draft_v2.md` lines 152 and 148.

### R30 — minor
Where: `draft_v2.md`, Table 2's caption (line 89)
Text: "The last three rows give the same readings for whole-brain lag-1 autocorrelation r₁ (dimensionless), whose DiD is in the text."
Problem: The r₁ rows are the eighth to the tenth of twelve. The last three rows are r₁'s baseline-adjusted contrast, the FD DiD and the FD-residualised DiD.
Evidence: Table 2's body (`draft_v2.md` lines 93–104).

### R31 — minor
Where: `draft_v2.md`, Table 3's caption (line 126)
Text: "the slope is the ordinary least-squares (OLS) slope of the residual DiD on the whole-brain r₁ DiD across the 14 subjects (intercept free)"
Problem: That defines the data's rows. The generators' slopes are on the simulated pair-a DiD, as the run's table, S3 Text §6 and Fig 3's caption say; the caption gives one definition for the column.
Evidence: `matched_slope_tables.md` line 4 ("the slope = OLS of the residual DiD on the pair-a DiD across the 14 subjects"); `S3_Text.md` line 391; `draft_v2.md` line 110 ("per unit of pair-a DiD").

### R32 — minor
Where: record, the revision entry, "The length and the tables" (lines 9264–9269); `CLAUDE.md` ("eight statements moved to the SI")
Text: "the sentence on Barrett (2015)'s reduction and the joint-target nodes (S3 Text §2)"
Problem: This and "the costs of prewhitening reported in the literature (S3 Text §8)" are listed among the statements that "left the main text for the supporting information". Both are still stated there in shortened form: Limitations has Barrett's reduction, the joint-target nodes and the double redundancy; Results 7 has the three costs with their citations. S3 Text says it exactly ("which now states it in a clause"; "which now names them in a clause"). What left is the phrase on "MMI-specific" and the rates of 42 % and 88 %.
Evidence: `draft_v2.md` lines 201 and 158; `S3_Text.md` lines 106 and 540.

### R33 — minor
Where: `manuscript/si/S5_Text.md` §1, the added paragraph (line 9)
Text: "(moved from the main text's Methods on 1 October 2026, where they are now named without their replacements)"
Problem: Methods no longer names them. It gives their number and the first and the last: "eight, from the interval method to a reading of the residual's direction since withdrawn".
Evidence: `draft_v2.md` line 261.

### R34 — minor
Where: `manuscript/si/S1_Text.md` (line 5); record, the revision entry, C M1 (lines 9211–9214)
Text: "(record, "Git history and the participant codes", 15 September 2026, which states what the repository holds and the question put to the data authors)"
Problem: That entry states what the history holds and that it is not rewritten. It puts no question to the data authors; the question is in the entry on the cold reads and in the revision entry.
Evidence: record lines 2766–2774; the revision entry, C M1: "the question whether the letters identify anyone is put to the data authors with the draft".

### R35 — minor
Where: `manuscript/supplementary.md`, S19 Table, the sentence after Part A (line 1689)
Text: "B27, B28, B29 and B16c recorded none for some of their parts (rows B27 (d), B28 (d), B29 (c)–(d) and B16c (a) and (e), reported and not counted);"
Problem: B27 (d), B29 (d) and B16c (a) did record a criterion or an expected result (the three predictions on the second variant and at W = 30; the place of the non-finite TR; equality with B16b's values), which their entries call not counted. Only B28 (d), B29 (c) and B16c (e) recorded no prediction, as the rows' own verdict cells say ("not counted", "check", "no prediction").
Evidence: the pre-run entries (record lines 8642–8644, 8800–8801 and 8850–8851); `supplementary.md` lines 1674, 1682 and 1683.

### R36 — minor
Where: `manuscript/si/S3_Text.md`, head note (line 3)
Text: "The computations are numbered as their scripts in `notes/` are (B1–B26, B16b, B17b)"
Problem: The same file now reports B27, B28, B29 and B16c under those labels (lines 187, 220, 389 and 525), and S19 Table's head note, which cites S3 Text for the labels, gives "B1–B29, B16b, B16c and B17b".
Evidence: `S3_Text.md` line 3; `supplementary.md` line 1601.

### R37 — minor
Where: `draft_v2.md`, References; record, the revision entry (lines 9122–9123)
Text: "seven references added (Barnett & Seth, 2011; Gao et al., 2026; Rosas et al., 2020; Schartner et al., 2017; Seth et al., 2013; Strassman & Qualls, 1994; Timmermann et al., 2019)"
Problem: Rosas et al. (2020) is added to the main text's reference list and is cited nowhere in the main text; its citations are in S3 Text §11 and S20 Table, row 2, as A's m10 says. Each of the other 47 entries of the list is cited in the main text, and S20 Table keeps its own list for a work cited only there.
Evidence: no "Rosas" before "## References" in `draft_v2.md`; `S3_Text.md` line 558; `supplementary.md` line 1717 and "References cited only in this table".

### R38 — minor
Where: `manuscript/supplementary.md`, S20 Table A, row 10 (and row 5); `notes/partB5_literature_v2.md`
Text: "(the pipeline's full details are deferred to Supplementary Materials, not read; V.S. is asked for them with the draft)"
Problem: A request to the paper's first author stands in a table of the paper; row 5 has the corresponding request to a co-author ("the study's co-author S.P.S. is asked with the draft"). Both are notes of the drafting, and both leave the row's reading ("HRF deconvolution not mentioned in the main text") resting on a supplement that was not read.
Evidence: `supplementary.md`, S20 Table A, rows 5 and 10; `claims_2026-10-01.md` lines 49–50 ("the supplement was not read: V.S. is asked for it").

### R39 — minor
Where: `manuscript/main_text_numbers.csv` (head note; HEAD's CSV lines 47 and 1018; CSV lines 1200–1215); `checks/numbers_update.out`; record, "The checks"
Text: "of 22 labels the rewritten sentences no longer carry and of 9 numbers whose rewritten sentences re-create them"
Problem: (1) Two of the deleted label rows are of tokens that the rewritten sentences still carry, without a row: "2S" in Results 7 ("would take from sts the 2S of two independent autocorrelated processes"; HEAD's row "TDMI = 2S: formula") and "(Results 1)" in the Introduction's last paragraph, where "(Results 2" keeps its label row. (2) The new sentences of Methods, The closed form, carry formula tokens without rows (six "t+1", "TDMI = 2S", "2S − C"), though the same paragraph's older "x_{t+1}, y_{t+1}" and Results 1's "2S" have label rows. (3) The head note still says "the six figure captions and the three table captions and bodies"; the main text has four tables. (4) The classes 61, 22 and 9 cannot be re-derived: `build24b.py` and `numtable.py`, which `numbers_update.out` names, are not in the repository.
Evidence: my scan of the blocks of `draft_v2.md` against their rows; `draft_v2.md` lines 173, 29 and 229; `numbers_update.out`, first line.

### R40 — minor
Where: `draft_v2.md`, Discussion, The fall of r₁ under DMT (line 187); record, the revision entry, C M3 (lines 9217–9221)
Text: "Non-neural routes are open too: DMT raises blood pressure and heart rate on the time course of its subjective effects (Strassman & Qualls, 1994);"
Problem: C's M3 (iii) asked for "DMT's cardiovascular/respiratory effects named as candidate non-neural contributors". The committed Limitations named "neural, haemodynamic, cardiac, respiratory or motion effects"; the revised main text names no respiratory candidate anywhere. The disposition says "the cardiovascular and motion candidates", which is what the text has.
Evidence: `git show HEAD:manuscript/draft_v2.md`, line 180; no "respirat" in `draft_v2.md`; `reviews/read_C.md`, M3.

### R41 — minor
Where: `CLAUDE.md`, the bullet on the subject codes (lines 45–56)
Text: "(record, "PLOS Computational Biology form", 18 Sep 2026; the paper's Ethics statement states the facts)"
Problem: The bullet is unchanged and no longer true of the working tree. The revised Ethics statement does not state the facts on the codes (C's M1: "replaced by a standard statement"), and the bullet's decision ("the history is left as it is") stands beside the revision entry's "whether the public history is rewritten is V.S.'s decision, to be recorded when made".
Evidence: `draft_v2.md` line 209; record lines 9211–9214.

### R42 — minor
Where: `notes/review_2026-10-01_cold_reads/README.md`, "Files", the bullet on `pubmed_search/`
Text: "`screening.md`, each record screened against the paper's inclusion criterion, with the two to be read in full in the next revision"
Problem: `screening.md` as revised says the two were read in full on 1 October 2026 and gives their assessment; the bullet, unchanged, describes the file as it was. The README's second section says it correctly.
Evidence: `pubmed_search/screening.md` lines 8–10; `git diff HEAD -- notes/review_2026-10-01_cold_reads/README.md` (the bullet is not in the diff).

### R43 — minor
Where: `manuscript/si/S3_Text.md` lines 106, 301, 317, 540 and 544; `manuscript/si/S5_Text.md` line 9; `manuscript/supplementary.md`, S20 Table's head note (line 1710); `CLAUDE.md` line 19
Text: "### The residual table (moved from the main text's Results 4 on 1 October 2026)"
Problem: Eight added statements date the revision's moves and removals to 1 October 2026. The revision is the commit that follows 8bd189e, which is of 2 October 2026; the record names it "The revision of 1–2 October 2026", and its text reports a run that ended at 21:35 UTC on 1 October, 00:35 on 2 October local time. The older headings of the same kind give the dates of their revisions (23 and 25 September 2026).
Evidence: `git log -1 --format=%cd 8bd189e`: 2 October 2026, 12:59:19 +0300; the eight lines named (also "until the revision of 1 October 2026", "removed from the cells on 1 October 2026" and "moved to S3 Text §6 on 1 Oct 2026").

## Notes

### R44 — note
Where: the prompt's setup, step 4
Text: "must print `all 188 entries applied`"
Problem: The command as given, with `| tail -1`, prints the last of the 15 sha256 lines that the script writes after its line "all 188 entries applied; files written:", which is line 190 of 205. The step's literal check therefore fails although the application is complete.
Evidence: the output of the step: `  9ba50aef7c1b1e3a52073e46d70fb0a76f3eb0c610bf814a84569aaac1dc86ab  scripts/15_figures_v2.py`. The full output has 188 `ok` lines and is byte-identical to `checks/apply_revision.out`; `git diff --name-only | wc -l` prints 15.

### R45 — note
Where: the prompt's check 4, the command for the line length
Text: "git diff HEAD -- manuscript/analysis_record.md | grep '^+' | awk 'length > 121'"
Problem: Under mawk, which counts bytes, the command prints 74 lines, none of them a heading (lines with −, ₁, ≤ and the like). Counted in characters no added line exceeds 120: the longest is 120, and the five headings are shorter while they carry «ENTRY_TIME». The rule holds; the command does not show it on every system.
Evidence: `awk -W version` here is mawk 1.3.4; a count by Python's `len` over the 418 added lines.

### R46 — note
Where: `notes/review_results/partB/matched_slope.csv` (committed in 8bd189e)
Text: "(i) band-passed, step,1,-0.366438,-0.517840,-0.215036,-0.835797,-0.082910,0.001042,-0.071641,-0.012562"
Problem: The condition label holds an unquoted comma, so each of the 400 data rows has eleven fields under a header of ten columns; a CSV reader shifts every column by one. The values are right once the label is rejoined.
Evidence: the file's lines 2 and 3.

### R47 — note
Where: record, "B27, outcome", "The run" (lines 8883–8885); `S5_Text.md` §4 (line 25)
Text: "on 1 Oct 2026 from 23:37:10 to 00:35:08 EEST (2 Oct) (20:37:10 to 21:35:08 UTC; 3,478 s by the unit's log)"
Problem: The end time is not in the unit's log or in the evidence as such: it is the last step's start (00:01:08) plus its printed duration (2,040 s). The evidence gives the log's last write as 00:35:10. S5 Text's "the charger was disconnected from 23:57 local time" is the time of the first heartbeat line that shows it; the line before is at 23:52:10.
Evidence: `b27/evidence.txt` line 3 ("the unit's log last written: 2026-10-02 00:35:10"); `b27/b27_unit.log` lines 156 (the step's start) and 686 ("done (2040s)"); `b27/b27_heartbeat.log` lines 3–4.

### R48 — note
Where: record, the revision entry, "The figures" (lines 9285–9291), against `checks/figures_check.py`
Text: "`captions_v2.md` differs from the committed file in its header, which names this commit, and in the captions of Figs 1, 3, 5 and 6, each of which equals the main text's caption with the Source sentence appended"
Problem: The script does not test exactly these conditions. (1) It accepts any change of the header line and does not require one; that the header names the commit is not tested. (2) It compares each changed caption with the main text's after removing " Source: …"; that a Source sentence is present is not tested. (3) For Figs 1, 3 and 5 any difference passes, a change of size included; what differs is not tested. (4) "Anti-aliasing alone" is, in the script only, at most 0.1 % of the pixels and at most 32 of 255 in a channel. (5) For the PDFs it masks CreationDate, ModDate, the cross-reference table and the `startxref` offset, more than "their creation dates". It does cover every file the figure script writes (six PNG, six PDF, the captions), and any other changed line of the captions file fails.
Evidence: `figures_check.py` lines 44–69, 71–91 and 93–113.

### R49 — note
Where: `scripts/15_figures_v2.py` line 465 (Fig 5c's title); record, "The figures"
Text: "Fig 5c's y-range and title"
Problem: In a scratch regeneration from the committed arrays (matplotlib 3.11.2 and this machine's fonts, not the pinned environment) the lengthened title of panel (c) runs past the right edge of the axes, and the saved PNG, cropped to its content, is 2,666 pixels wide against 2,212 at HEAD; the other five figures change by at most 44 pixels in width. `figures_check.py` accepts a change of size for Fig 5. Whether the title overruns in the pinned environment is for the figures commit to see.
Evidence: my run of the revised script in a copy of the tree; `fig.savefig(…, bbox_inches="tight")` (line 136).

### R50 — note
Where: record, "B29, outcome", (d) (line 9035); `draft_v2.md`, Methods, Dataset (line 213)
Text: "The prediction, subject 3's placebo run's TR 839 and no other: confirmed."
Problem: The script's check reads `ts_gsr` only, as its table and S3 Text §5 (e) say. "No other" and the main text's "the released series hold one non-finite TR" are shown for that variant.
Evidence: `notes/partB29_censoring.py` line 123; `censoring_tables.md` line 47 ("Non-finite TRs of ts_gsr").

### R51 — note
Where: `draft_v2.md`, Results 2, third paragraph (line 108); the pre-run entry of B29, rule (iii); C's m1
Text: "its DMT run holds the mean-filled parcel and 24 TRs above the motion threshold, against 23.6 on average"
Problem: The rule asked for "subject 8's motion and its marked TRs", and C's m1 for its framewise displacement. The main text gives the marked TRs; the mean framewise displacement (0.120) is in S3 Text §5. The comparison with the average shows subject 8 as ordinary; its mean-FD DiD, +0.0935, is the largest of the fourteen, which the prose says nowhere.
Evidence: `censoring_tables.md` (a), row 8 and the column of the mean-FD DiD; `S3_Text.md` line 257.

### R52 — note
Where: `draft_v2.md`, Discussion, The fall of r₁ under DMT (line 187)
Text: "nothing on the placebo run"
Problem: True of the variant whose values the sentence quotes (ts_gsr: −0.0468 [−0.1375, +0.0387], one-sided p = 0.22). On ts_demean S6 Table gives −0.0926 [−0.1795, −0.0076] on the placebo run, one-sided p = 0.045.
Evidence: `supplementary.md`, S6 Table (lines 119–124).

### R53 — note
Where: `draft_v2.md`, Results 2 (line 108); record, the revision entry, B MINOR 2 (lines 9187–9188)
Text: "(a subject bootstrap of 10,000 draws, the 366 in which either half's reliability was not positive left out; the ratio is not bounded by one)"
Problem: The count and the interval are right. The rule, exactly: a draw is left out when the split-half reliability of the sts DiD or that of the r₁ DiD is not positive (175 and 323 draws, 366 in either). The reliabilities are those of the two quantities, not of the two halves; Fig 3's caption has had "the two halves' split-half reliabilities" since before this revision.
Evidence: `notes/partB21_inference_revision.py` lines 563–567 and 587–597; my re-run of the bootstrap on `splithalf_subjects.csv` with seed 20261120: 366 left out, [+0.617, +0.991], 108 draws above one.

### R54 — note
Where: `claims/claims_2026-10-01.md`; `notes/review_2026-10-01_cold_reads/README.md`, the bullet on `claims/`
Text: "every statement the revised text makes about a cited work that no earlier citation pass covered, with where in the work it was checked"
Problem: The Discussion cites "(Timmermann et al., 2019, 2023)" for the rise of the EEG's signal diversity and the fall of its alpha power under DMT. The claim record has a line for the 2019 paper and none for the 2023 paper on that statement.
Evidence: `draft_v2.md` line 187; `claims_2026-10-01.md` lines 8–27 and 60–65.

### R55 — note
Where: `revision/text_replacements_2026-10-01_cold_reads_revision.json`
Text: "L01 notes/partB5_literature_v2.md ok"
Problem: Three ids are used twice (L01, M06, M07; 185 distinct ids for 188 entries), so an id does not name one replacement. The line quoted is the second L01 of the application's output; the first is of `manuscript/draft_v2.md`.
Evidence: `checks/apply_revision.out` lines 36 and 140 (L01), 42 and 156 (M06), 43 and 157 (M07); the JSON's entries 35 and 139, 41 and 155, 42 and 156, counted from 0.

### R56 — note
Where: `notes/review_2026-10-01_cold_reads/README.md`, last bullet; `CLAUDE.md` (lines 441–442 and 445–446)
Text: "(`findings_text.md`, `findings_record.md`, `findings_citations.md`) and what was done with each finding (`dispositions_revision.md`)."
Problem: These four files are not in the working tree yet; they come with the audits, so the statement is true only once they are added. `CLAUDE.md` says of Figs 2, 4 and 6 "identical but for the PDFs' dates", where the record's paragraph also allows their PNG files to differ by anti-aliasing.
Evidence: `ls notes/review_2026-10-01_cold_reads/audit/` (`dispositions.md`, `findings.md`); record lines 9289–9290.

### R57 — note
Where: record, the revision entry, C M2 (lines 9216–9217); `draft_v2.md`, Methods, Use of AI tools (line 257); replacement M09
Text: "the Use of AI tools statement is unchanged until a person has checked the analysis."
Problem: The statement was reworded by this revision: the accidental copy of the data and the test run on it moved into a parenthesis (251 words at HEAD, 245 now, by `wc.py`). Its content is the same, as the replacement's reason says.
Evidence: `git diff HEAD -- manuscript/draft_v2.md`, the paragraph of line 257; M09's `why`: "Condensed for the word limit; no statement removed (C's M2 is answered in the covering letter to the co-authors, not by a change of this statement)."

---

## Checked and found exact

**The setup.** HEAD and its subject; the tarball's sha256; 16 untracked files, all under
`notes/review_2026-10-01_cold_reads/`; the application's full output identical to `checks/apply_revision.out`, the 15
files' sha256 among it; 15 files changed; the record's numstat 418 and 0.

**1. The verdicts.**
- The 29 outputs equal `b27/outputs.sha256`; the twelve text outputs carry `git=13e7299`.
- B27: every cell of tables (a), (b) and (c) recomputed from `baseline_gap.csv` (168 rows) with my own exact sign-flip
  test (16,384 assignments), its inversion, the OLS intervals (12 df), the partial correlation, the 14 and 91 refits,
  the sensitivity and Fieller's g; all equal at the printed precision. One p comes out 0.1873 from the six-decimal CSV
  where the table prints 0.1871 (r₁, ts_demean, pre-injection gap): ties among the rounded values, not a finding.
  `derived_r24.py` re-run: its output identical but for the commit in its header.
- B28: the table recomputed from `matched_slope.csv` (400 rows): means, SDs, percentiles, shares, ratios, coverage.
  The script re-run in a scratch copy (2,115 s): `matched_slope_tables.md` and `matched_slope.csv` identical to the
  committed ones but for the commit in their headers, all 3,600 numeric cells equal, the log equal but for its timings.
- B29: tables (a), (b) and (c) recomputed from `censoring.csv` (392 rows): the counts and shares per run, the count
  DiD +1.12 (p = 0.2166, 7 of 14), the mean-FD DiD +0.0143 (p = 0.2452, 8 of 14), the ten correlations of (b), the
  two of (c) with 137 of 392 windows and the four means, and the lines of subjects 8 and 14.
- B16c: the 32 intervals, p values and negative counts of `derived_r24.out`, item 1, recomputed from the pickle's
  per-subject vectors; the levels, the whitened r₁ and its DiD, and the eight correlations against
  `prewhiten_fixed_tables.md`; B16's and B16b's values that the entry compares with (0.2202, 0.2350, 0.1042, 0.1306,
  +0.495; 0.1368, 0.0739, 0.0524, 0.0323; 51.2 % and 59.7 %).
- The eleven counted verdicts, each by its criterion as written: B27 (a), (b), (c) met; B28 (a), (b), (c) met; B29 (a)
  partly met, (b) missed; B16c (b) met, (c) missed, (d) met. They are the entries' verdicts, and each is stated with
  the values it rests on (R03 concerns two of those values, not the verdict). The uncounted parts are reported as the
  pre-run entries say.
- S19 Table: 67 counted rows, 36 met, 15 partly met, 16 missed (56 = 28 + 14 + 14 at HEAD, plus 11); the 17 new rows
  (11 counted, 6 not) give criterion, value and verdict as the entries do; Methods' totals are the same.

**2. The rules for the text.**
- B27 (i), (iii), (vi): Table 2's six new rows on both variants equal `baseline_gap_tables.md`; Results 2's r = −0.888,
  r² = 0.79, SDs 0.0887 and 0.0485, the one positive DiD in the subject with the most negative gap (subject 14), r₁'s
  readings, 0.34 and 0.40, "a fifth" and "a sixth", −0.844, +0.939, +0.824, 38 %; the Abstract's and the Author
  summary's sentences (sts rose in one subject, r₁ in two); the minimal detectable difference beside the excesses in
  the Abstract, Results 4 and the Discussion.
- B28 (i), (iii), (iv), (v): Table 3, every cell; the floor (subject 8, −0.0657 rescaled, −0.0375); Fig 3's caption;
  the Fieller interval [−1.60, −0.08] and the ratios −0.79 and −0.74; S18 Table's rows; S3 Text §6.
- B29 (i), (iii), (iv), (v), (vi) apart from R10, R24, R28 and R51: Limitations' 23.6, 10.1, +1.12, p = 0.2166, 7 of
  14, −0.107, −0.124; Results 2's 24 against 23.6; the FD DiD +0.0143, p = 0.25.
- B16c (i), (iii), (iv), (v): Table 4, every cell (0.263 is right: the unrounded value is 0.26255); 18 % and 7 %;
  −0.0927, +0.333, −0.0037; S11 Table's 24 new rows and S3 Text §8's eight rows and its diagnostic values.
- S3 Text's transcriptions of B27 (a) and (b) and of B29 (a), (b) and (d), cell for cell; the former Table 3 moved to
  S3 Text §6 with its caption and its 13 rows unchanged.

**3. The revision entry.**
- 70 dispositions: A 20 (M1–M2, m1–m14, w1–w4), B 19 (MAJOR 1–3, MINOR 1–11, W1–W5), C 31 (M1–M6, m1–m19, w1–w6), each
  id once, against the items of the three reports.
- Borne out by the text: A M1, M2, m1–m3, m5–m7, m9–m14, w1–w3; B MAJOR 1–3, MINOR 1–5, 7, 8, 10, 11, W1, W2, W4, W5;
  C M1, M2, M4, M6, m1, m3–m6, m8, m10–m18, w1–w6 (the findings above also touch A m9, B MINOR 2 and C M1, m1 and
  m18, whose dispositions say what was done; the other twelve have a finding each). Among the values: −1.74 and 0.035
  (Results 1); −0.015 to −0.036 (the grid of S18 Table); +1.815, −0.150, 1.76, +0.124, +0.142 (S3 Text §11); 0.50 and
  3.09, a sixth; the thirteen atoms, each moving in its substituted value's direction, and the three that print
  0.0000; the EEG check's −0.24 [−0.40, −0.08], p = 0.002.
- "The length and the tables": `wc.py` gives 8,498 words with headings and 8,371 without; four tables and six
  figures, numbered by first citation, each caption after the paragraph of its first citation; the decision of
  23 September 2026 is in the record (line 6574); the eight listed statements are in the named sections of the
  supporting information and each is pointed to (R32 concerns two that also remain).
- "The checks": `check_numbers.py` (rows 1302, data rows 768, flagged 11, the same eleven lines), `check_cells.py`
  (flagged 0), `tablecheck.py` (0 on the seven manuscript files), `wc.py` and `abstract_summary.py` (299 and 200)
  give outputs identical to the `*_revision.out` files; the four scripts of `scripts_check_revision.out` parse.
- "The figures": `figures_check.py` read against the paragraph (R48). In a scratch run of the revised figure script,
  `captions_v2.md` differs from HEAD's in its header and in the captions of Figs 1, 3, 5 and 6 only, and each of the
  four equals the main text's caption once the Source sentence is removed; Fig 3c shows the two matched slopes,
  −0.200 and −0.355.

**4. The record's rules.** Additions only (418 added lines, none removed); no added line longer than 120 characters
(the longest is 120); the five headings in the record's form, each with «ENTRY_TIME»; no trailing whitespace. The
prompt's grep gives 40 matches, all in record entries at or above line 7467, none in the new entries or in another
manuscript file. In the main text: no computation label before "## Supporting information", no file path before Data
and code availability, none of the prompt's process labels.

**5. The bookkeeping.**
- S5 Text §4 against `evidence.txt`, `b27_unit.log` and `b27_heartbeat.log`: the commit 13e7299; the start 23:37:10
  local, 20:37:10 UTC; 7, 1,428, 1 and 2,040 s; exit 0 and no traceback; the root unit under the inhibitor; the
  charger connected at the start and disconnected in 8 of 11 heartbeat lines, 99 % to 83 %, the largest gap 300 s;
  python 3.12.3, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.1, `pip freeze` equal to the lock file; the data clone at
  77af7aa; 29 outputs and 4 evidence files, the 33 files of 8bd189e; `b27_commit.sh` does the checks the record lists.
- S5 Text §6: 71cf932, 24919ea and 13e7299 are of 1 October and 8bd189e of 2 October 2026; the pre-run entries were
  committed at 19:03 UTC and the run began at 20:37 UTC. S5 Text §1: eight deviations. S5 Text §5: three cold reads,
  70 findings, four computations.
- `CLAUDE.md` and `README.md`: 8,498 words (8,371 without headings), the limit 8,500, four tables, six figures, 67
  predictions (36, 15, 16), 1,302 rows, seven references each with a section of the claim record, eight statements
  listed, the commits 13e7299 and 8bd189e.
- The folder's README names the 16 new files. The PubMed files: 11 records, six in S20 Table, four outside the
  criterion, one added, three of the nine not returned; the second search, 2 records, neither an application. S20
  Table A equals Table A of `notes/partB5_literature_v2.md` but for the label replacements its head note states.

**6. The numbers table.**
- 1,198 − 253 + 357 = 1,302 rows (the file has 1,304 lines); 161 + 61 + 22 + 9 = 253; the former Table 3's rows are
  161 (112 of the body, 49 of the caption); 4 numbers changed in place (56 to 67, 28 to 36, 14 to 15, 14 to 16); 17
  locators moved, 5 anchors changed; the count of rows with a changed context is consistent with 263; no row's section
  or paragraph needed relabelling.
- By my scan of every block of the main text against its rows, at HEAD and in the working tree: apart from R09 and
  R39, every number of a changed or new block has a row, and every deleted row's number is absent from its paragraph
  or has a row there. The tokens left without rows are of the kinds that had none at HEAD: cross-references (sections,
  figures, tables, table rows, equations and pages of cited works), citation years, most dates, and identifiers.
- The numbers whose rows were deleted are still in the paper: in another paragraph of the main text (the Abstract's
  1.4, [0.62, 0.99], 0.003 and 0.005), in the tables (the FD-residualised and ts_demean DiDs in Table 2; the
  prewhitening values in Table 4) or in the supporting information (the null's four residual levels; −0.1129 and
  −0.1130; the two cross-half correlations' intervals; 0.219 and −0.052; the aligned statistic and its expectation;
  ΦR's sensitivity cell; the rates of 42 % and 88 %; 0.97 and 32.8; the runs' wall-clock values).
