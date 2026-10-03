# W1 — the main text (`manuscript/draft_v2.md`), HEAD eed9271 against `checked` (9caa60b) and 8bd189e

**Result: no finding of grade `error`.** Five findings: 4 `inexact` (W1-1 in the main text; W1-2, W1-4 and W1-5 in `audit/dispositions_revision.md`) and 1 `note` (W1-3, main text). No number, pointer, date or count of the main text was found wrong. Nothing under VT was modified (`git status --short --ignored` is empty at the end); every script was run on copies under `VW/W1/` (`git archive` of HEAD and of `checked`).

## Findings

**W1-1** — grade: `inexact`
- Where: `manuscript/draft_v2.md` line 241, Materials and methods, "The primary contrast and the exploratory analyses": "S19 Table says of each computation whether it had a recorded prediction or was post hoc (the text repeats it for several, in Results 2, 3, 5 and 7 and the Discussion)".
- Problem: the sections named are not all the places. The text repeats it in Methods as well, in the next subsection: "The AR(1)-substituted estimate and its calibration" (line 245) says of the aligned statistic A_other, of the residual's response to the five constructions with their pure-autocorrelation expectations and of the generators' per-subject slopes that they "were computed under rules and predictions recorded beforehand". The five places named do each hold such a statement (listed under "Checked and found exact", 1).
- Also, of a neighbouring kind: Results 6 (line 154), a section the parenthesis does not name, says "CCS-sts is a specification chosen after the results were seen". This is a statement of when the specification was chosen, not S19 Table's status of the computation (its row gives an outcome mapping without a predicted branch).
- Evidence: `draft_v2.md` lines 154, 241, 245; `manuscript/supplementary.md`, S19 Table, Part A, lines 1648 (B22 (a), A_other), 1658 (B23 (b)), 1663–1664 (B24), 1675–1677 (B28 (a)–(c)) and 1617 (B2, the CCS comparison).

**W1-2** — grade: `inexact`
- Where: `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`, VM-1 (line 1499): "The record's disposition of B's MINOR 8 names each."
- Problem: the record's list names nine places, the five that Methods had listed and the four that VM-1 added (six marked post hoc, three named as a recorded prediction). Its second part is not all that the main text names as a recorded prediction. Two places are not in it: the sentence of Methods quoted in W1-1 (line 245), and the Limitations' "several recorded predictions failed, among them the calibration's for a coupling change" (line 201; S19 Table, Part A, lines 1632 and 1643).
- Evidence: `manuscript/analysis_record.md` lines 9283–9288 ("Marked post hoc in the text: the r₁ contrast, the leave-one-out and S8 Table's check of the ratio (Results 2), the regional relation on the windowed atoms (Results 3), the spectral centroid (Results 5) and the deconvolved contrast (Results 7 …); named as a recorded prediction: the sensory–association contrast and the residual map's network structure … (Results 3 and Fig 4's caption), and the EEG Lempel–Ziv check (Discussion)").

**W1-3** — grade: `note`
- Where: `draft_v2.md` line 87, Results 2, first paragraph: "The DiD's between-subject variance is mostly the gap's (SD 0.0887 against 0.0485 for the post-injection gap; r(DiD, pre-injection gap) = −0.888, r² = 0.79)".
- Problem: the four numbers are exact, but the sentence does not say whose SD 0.0887 is. It is the DiD's. Since the correction for VM-3 moved the SDs to the head of the parenthesis, "SD 0.0887" stands directly after "the gap's" and is set against "the post-injection gap", so that it reads as the pre-injection gap's SD, which is 0.0524.
- Evidence: `notes/review_2026-10-01_cold_reads/checks/derived_r24.out` line 36 ("SD pre gap 0.0524, SD post gap 0.0485, SD DiD 0.0887"); recomputed from `notes/review_results/partB/baseline_gap.csv` (0.052404, 0.048548, 0.088676); `manuscript/si/S3_Text.md` line 260 gives the attribution in full ("the SD of the DiD 0.0887 against 0.0485 for the post-injection gap and 0.0524 for the pre-injection gap").

**W1-4** — grade: `inexact`
- Where: `dispositions_revision.md`, VM-8 (lines 1532–1534): "the file's titles carry bins (S1), a section reference and a time of day (S9) and computation labels (S17, S18), which the main text does not use, and the list's entries give the same contents without them".
- Problem: as worded the reason covers all four kinds ("without them"). It holds for times of day and for computation labels. It does not hold for bins, nor for section references of S3 Text, both of which the main text uses.
- Evidence: bins in `draft_v2.md` lines 116 ("bins 1–8"), 187 ("over 28 bins"), 217 ("averaged into 28 bins"), 237 ("(bins 1–8), post windows 6–14 (bins 11–28)") and, in the list of supporting information itself, lines 413 ("S6 Table. … global fit, 28 bins.") and 415 ("per bin set"). Section references: 38 "§" in the main text (e.g. "S3 Text §6"), none in the list's titles. No "UTC" and no time of day anywhere in the main text; no computation label.
- The rest of the disposition is true: the four titles differ as it says, S20 Table's title now carries the list's words, and each of the four list entries gives the file title's contents.

**W1-5** — grade: `inexact`
- Where: `dispositions_revision.md`, VM-10 (lines 1543–1544): "The rows of the window sets and of N = 14 cite the line that holds them (line 4 of `family_atoms_tables.md`; the record's line on the shape of the data)".
- Problem: the rows do cite a line that holds them, but the parenthesis names two lines and there are three. Four rows of the window sets (Table 2's caption: "6", "14", "1", "4"; file lines 407–410 of `manuscript/main_text_numbers.csv`) cite `manuscript/analysis_record.md` line 1747, "Primary (pre windows 1–4 / bins 1–8; post windows 6–14 / bins 11–28):".
- Evidence: the table's head note and the disposition of VB-20 name it ("the record's lines on the window sets and on the shape of the data"). The other rows are as the disposition says: 13 rows on line 4 of `family_atoms_tables.md`, the row of N = 14 of Table 2's caption on the record's line 48.

## Checked and found exact

**1. The delta (`git diff checked HEAD -- manuscript/draft_v2.md`)**

Ten lines changed (19, 87, 108, 114, 124, 154, 187, 193, 241, 401) and no other; listed token by token. 8bd189e with the 65 replacements that the replacements file holds for this file equals HEAD byte for byte, each `old` occurring `count` times. Rows of the numbers table are given below by their line in `manuscript/main_text_numbers.csv`.

- Line 19, Author summary. "the signals' autocorrelation" and "from each pair's autocorrelations and correlation": agrees with the Results' opening paragraph (a_x, a_y, q), the Abstract and Recommendations. "synergy rose in one volunteer, autocorrelation in two": subject 14; subjects 5 and 14 (`baseline_gap.csv`).
- Line 87, Results 2. 0.0887, 0.0485, −0.888 and 0.79 against `derived_r24.out` line 36 and `baseline_gap_tables.md` line 10; recomputed from `baseline_gap.csv` (r −0.887968, r² 0.788487; one positive DiD, subject 14, +0.0949, whose pre-injection gap, −0.1121, is the most negative). S3 Text §5 (line 260) states the same four values and the sense of "mostly", with the parts 0.30, 0.35 and 0.35 (recomputed 0.2997, 0.3492, 0.3510).
- Line 108, Results 2, "(Results 4; S13 Table)". Results 4 introduces the two generators (it does not state the two rates); S13 Table's note (line 363) holds +3.08, +6.13, +5.2 and +5.5. Rows 584–598: `derived_r17.out` line 2, `baseline_gap_tables.md` line 44, `inference_revision_tables.md` line 242. Derived: 0.0809 / 0.0155 = 5.22, 0.04240 / 0.01377 = 3.08, 0.09441 / 0.01540 = 6.13, each operand on its source line. Recomputed from `baseline_gap.csv`: ratio 5.522, Fieller [4.45, 10.54], g 0.611, slope 4.2627 [3.4085, 5.1169], intercept −0.01844. "Methods" holds g and the Fieller assumptions. Fig 3a's caption agrees (+4.26, [+3.41, +5.12], −0.018, 6.13).
- Line 114, Results 3, "just over half". `regional_partial_tables.md` line 74 (+0.0007 ± 0.0203) gives, with t on 13 df, [−0.0110, +0.0124]; 0.0110 / 0.0202 = 0.545 (0.540 to 0.551 over the rounding of the saved mean and SD). Rows 674–681 against lines 9 and 74 and `derived_r17.out` lines 37–38. "(S19 Table)": rows B20 (line 1639) and B22 (e) (line 1652). "(Fig 4b)": the panel draws the group map's contrast, −0.0202 to +0.0037 (script and regenerated figure), and its caption sends the per-subject version with its intervals to Results 3.
- Line 124, Results 4, "(unrounded means)". `derived_r24.out` lines 55–56: +0.000148 and +0.000620; recomputed from `matched_slope.csv` (means 0.002182, 0.002034, 0.004851, 0.004232). Table 3's cells (+0.0022 and +0.0020; +0.0049 and +0.0042) differ by 0.0002 and 0.0007. S3 Text §6 (line 404) and "B28, outcome" (c) give both pairs of differences; S19 Table's row B28 (c) gives the cells and the unrounded differences.
- Line 124, the cross-half correlations. `splithalf.log` line 12, ts_gsr: r(res_odd, ac_even) = −0.385, r(res_even, ac_odd) = −0.700; line 24, ts_demean: −0.598 and −0.051. S3 Text §6 (line 406) gives the same variant and half for each. The sentence groups the four by variant correctly and names no half. Fisher-z intervals, ceilings 0.605 and 0.392, and ratios 0.90 and 0.83 recomputed.
- Line 124, the rest of the two sentences. "(Table 3)": every slope of rows 2–6 negative (recomputed: 14 leave-one-out, 91 leave-two-out, the three named omissions; counts 0, 0, 11, 11 and 1, 13, 71, 63). −0.79 (−0.788), [−1.60, −0.08], g 0.61 recomputed; −0.74 = +0.0115 / −0.0155; the interval contains −0.18, −0.39 and −0.37.
- Line 154, Results 6, "as we read it". S3 Text §11 (lines 564, 568), S20 Table row 2 (line 1718) and S19 Table's row B25 (d) (line 1669) carry the same qualifier. +1.815, −0.150, 1.76, +0.124, +0.142 against `binarised_tables.md` lines 55, 60, 65 and `binarised.csv` (1.815276, −0.149607, 0.124430, 0.141548: no second rounding).
- Line 187, Discussion, "(Methods; S3 Text §10; …)". Methods, Literature search, names the searches and the 2 records; S3 Text §10 (line 556) holds the string, the 2 records and the sentence on ketamine anaesthesia; `pubmed_search/psychedelic_phiid_search.md` holds 2 records, neither a ΦID study.
- Line 193, Discussion, "(S3 Text §4, §10)". §4 (line 128): "Per unit of spectral difference, however, the exposure hardly depends on TR" (+0.190, +0.170, +0.165) and "does not rank datasets". §10 (lines 556, 560): r₁ 0.97 and ∂sts/∂r₁ = 32.8 at TR 0.72 s. Row of 0.72: `citation_pass_2026-09-22.md` line 146.
- Line 241, Methods. Each place named holds at least one statement: Results 2 (lines 87, 106, 108: the leave-one-out, the r₁ contrast, S8 Table's check), Results 3 (line 114: the windowed relation, the contrast fixed beforehand, the p below its predicted range; Fig 4's caption), Results 5 (line 146), Results 7 (line 171), the Discussion (lines 187 and 201). See W1-1 for the place not named.
- Line 401, the entry of S5 Text. S5 Text §3 is "The decisions of 20 September 2026"; the entry follows §1 to §6 in order.

**2. The dispositions (VM-1 to VM-10, VE-19, VN-8, VT1-10, VB-31)**

- Every phrase they quote stands word for word in the file named (15 phrases, by script). Each description of the finding and each grade agrees with `check_VM.md`, `check_VE.md`, `check_VN.md`, `check_VT1.md` and `check_VB.md`.
- VM-1: the quoted sentence is at line 241; see W1-1 and W1-2.
- VM-2: 0.0110 / 0.0202 = 0.54.
- VM-3: the parenthesis leads with the SDs; S3 Text §5 gives the sense of "mostly", the three parts and "It is not an apportionment"; `derived_r24.out` item 9.
- VM-4: "B28, outcome" (c) gives both pairs (0.0001 and 0.0006; 0.0002 and 0.0007).
- VM-5: the four values without a verdict; S3 Text §6 sets them against their ceilings (`derived_r24.out` item 10). The old verdict stands nowhere in the manuscript files or the numbers table.
- VM-6: the forward pointer is in Results 2. Fig 3's caption is unchanged and names a source with each rate (S18 Table for 6.13, −0.18 and −0.39; Methods for −0.37); S18 Table holds −0.09441, −0.01540, +0.00279 and −0.387.
- VM-7: 200 words.
- VM-8: titles compared by script. S1 to S5 Text and S2 to S8, S10 to S12, S14 to S16 and S19 Tables are identical; S13 and S20 Tables are identical once the list's title and description are joined; S1, S9, S17 and S18 Tables differ as the disposition says. See W1-4 for the reason.
- VM-9: at HEAD the committed captions of Figs 1, 3, 4, 5 and 6 differ from the main text's and Fig 2's is identical; the committed Fig 3c has no thin lines and the committed Fig 5c runs from −0.04 to +0.06. The record's paragraph on the figures lists the conditions, `checks/figures_check.py` tests each of them, and S5 Text §6 says in which commit the figures are.
- VM-10: the three "95" rows are label rows; the bound row holds 6.7e-16 (line 209 of `diagnostic_alternatives_tables.md`); the rows of the window sets and of N = 14 cite lines that hold them; no row still cites the record's line 189 or line 6 of `family_atoms_tables.md` except rows of "60", which those lines hold. See W1-5.
- VE-19: as line 193 above.
- VN-8: the sentence is the one of 8bd189e. Schaefer2018.pdf, p. 1 (abstract): "Multiresolution parcellations generated from 1489 participants are publicly available" with the release's address; the article names 400, 600, 800 and 1000 parcels and no 100-parcel resolution (its only "100 parcels" is of two earlier network parcellations). The repository holds `data/Schaefer2018_100Parcels_7Networks_order.lut` (100 labels) with `data/LICENSE-CBIG.md`. The reference entry agrees with the PDF (authors, title, 28: 3095–3114, DOI).
- VT1-10: the head note of `supplementary.md` has the quoted words; the heading of Results 6 is that of 8bd189e; the section's second sentence is the one quoted, and the third turns to the data.
- VB-31: 29 heading lines from Introduction to Methods; 8,498 − 29 = 8,469; the record's paragraph "The checks" has the quoted words (lines 9457–9458).
- The last part's counts: 157 dispositions, 142 "Corrected", 7 "Stated", 8 "Kept"; grades 11, 69 and 77.

**3. What the changes could have broken**

- `wc.py`: 8,498 with headings, 8,371 without; output identical to `wc_revision.out`. `abstract_summary.py`: Abstract 300, Author summary 200; identical to `abstract_summary_revision.out`.
- `check_numbers.py` on a copy: "rows 1381, data rows 787, flagged 11", identical to `check_numbers_revision.out`. The 11 flags are magnitudes stated without their sign ("fell by", "exceeds … by", "a fall of", "to within") and one range hyphen; none lies in a changed sentence.
- Rows of the changed sentences (file lines 390–393, 584–598, 674–681, 794–811, 1025–1031, 1170, 1178–1180): every context occurs in the text, the number is in its context, every number token of these sentences has a row, the rows follow the new order of line 87, and each source line was opened. The changed sentences of lines 19, 241 and 401 hold no number token that takes a row.
- Whole table, by script: all 1,381 contexts occur in the text; the anchor of each of the 1,065 data, design, literature and bound rows is on its named line; the 54 derivations recomputed.
- No computation label anywhere in the file; no round, stage or bundle name ("stage" occurs once, in a reference title); no reviewer's letter; no "planning session" or "writer's session" ("session" eight times, never a name). No file path, code span, commit identifier or time of day before "## Data and code availability" or in the list of supporting information.
- Figure captions: the literal text of each of the six `caption(...)` calls of `scripts/15_figures_v2.py` matches the main text's caption with every computed value in place (static comparison, 5 to 34 computed values per caption); a copy of the script run under `VW/W1/figrun/` writes six captions that, without their Source sentence, are byte-identical to the main text's.
- Pointers of the changed sentences: Methods (g), Results 4, S13 Table, S19 Table, Fig 4b, Table 3, S3 Text §4, §6, §10 and §11, Methods (Literature search): each holds what is said above.

**4. The whole main text read once at HEAD**

- No number of the delta changed in value; the 22 source values that the text prints in more than one form are each a correct rounding of the same held value (for example −0.09441 and −0.094; 0.1075 as 0.108 and 0.11; +0.617 as 0.62).
- Terms of the changed sentences are introduced before use or point forward: cross-half correlation (Results 2), primary and sensitivity variant (Results 2, Table 2), the generators (the forward pointer to Results 4).
- Every changed sentence parses. No stray hyphen-minus before a digit and no spacing fault on the changed lines.
- S5 Text §4 records the two occasions that the Use of AI tools statement names; S19 Table's count (67: 36, 15, 16, 0) agrees with Methods.

**Not checked (outside what the tree and the task allow offline)**

- Statements about cited works other than Schaefer et al. (2018).
- That the public release named in that article holds a 100-parcel resolution, beyond the label file and the licence note in the repository.
- The [TK] placeholders, unchanged since 8bd189e.
