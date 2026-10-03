# VT1 — verification of the dispositions of T01–T31 (the text audit), tree at HEAD (9caa60b)

All 31 corrections are in the tree where the dispositions put them, every quoted phrase occurs word for word in the file named, and every corrected number agrees with its source or with my recomputation from committed files. No error remains in the corrected main text for T01–T31. I have ten findings on the edges: one wrong number in the record (outside T01–T31, met while searching for second roundings), five inexact statements, four notes.

VT was not modified (`git status` clean at the end). The figure script and `figures_check.py` were run in a private clone under `VW/VT1/tree`; no subject data and no internet were used.

## Findings

**VT1-1**
- Where: `manuscript/analysis_record.md` L9264, disposition of B's MINOR 9: "that of the sts slope (4.26: 4.14 to 4.54) in S3 Text §5".
- Problem: the upper leave-one-out slope is 4.534648, which is 4.53 to two decimals. 4.54 is a second rounding of the printed 4.535. This is outside T01–T31 (it belongs with R22/T47); it is the T06–T08 problem persisting in the record's new entries.
- Evidence: recomputed from `inference_rows_raw.pkl` (rows "sts ts_gsr W60" and "autocorr ts_gsr W60", `did_subjects`): 4.139222 without subject 14, 4.534648 without subject 8. The record itself prints "+4.1392 to +4.5346" at L6361; `derived_r24.out` L69, S3 Text L260 and "B27, outcome" L8938 give 4.535.
- Grade: error.

**VT1-2**
- Where: record, "The figures" (L9411–9414): "Fig 5c's y-range and two-line title, with height ratios of 0.30 : 0.20 : 0.20 for 0.30 : 0.20 : 0.10".
- Problem: the diff also re-anchors Fig 5c's legend (`bbox_to_anchor` from (0.0, −0.42) to (0.0, −0.25)). The paragraph does not name this drawing change; the script's revision note (L26) and disposition R49 do. Everything the paragraph does name is in the diff, and the diff makes no other drawing change.
- Evidence: `git diff 8bd189e HEAD -- scripts/15_figures_v2.py`, the `axes[2].legend(...)` line, now L474.
- Grade: inexact.

**VT1-3**
- Where: `dispositions_revision.md` R19 (for T13): 'The main text names "the sts surface of Fig 1a" … and in the list of supporting information (the entries of S3 Text and S20 Table)'; the record's disposition of A's m8 (L9194–9195) says the same.
- Problem: the entry of S3 Text reads "the sts surface over (r₁, q), the within-window regression and the regional maps". The quoted name occurs twice in the main text: Discussion and the entry of S20 Table.
- Evidence: `draft_v2.md` L397, L191, L441.
- Grade: inexact.

**VT1-4**
- Where: `dispositions_revision.md`, T03, last sentence: "The dispositions of A's m9 and B's MINOR 3 (a) say that the reason B offered was not so."
- Problem: only the disposition of B's MINOR 3 (a) says it. The disposition of A's m9 says the windowed atoms "are committed" and does not mention B's reason.
- Evidence: record L9197–9200 against L9241–9243.
- Grade: inexact.

**VT1-5**
- Where: `manuscript/main_text_numbers.csv` L565 (the row for 366, Results 2, paragraph 3), note: "B21 (d): draws excluded (either half's reliability not positive)".
- Problem: the wording T26 found inexact stays in the note of this row, which is new in the revision. The draws left out are those in which the split-half reliability of the sts DiD or of the r₁ DiD is not positive.
- Evidence: `notes/partB21_inference_revision.py` L563–567. Bootstrap repeated from `splithalf_subjects.csv` with seed 20261120: 366 excluded (sts reliability not positive in 175, r₁ in 323, both in 132), interval [0.617, 0.991].
- Grade: inexact.

**VT1-6**
- Where: `manuscript/si/S4_Text.md` L76 (Sh3): "pinned environment, every result table with its git SHA, `run_all.sh`".
- Problem: this is the unqualified statement T17 (i) found in Data and code availability; it is unchanged by the revision. 23 committed result tables carry no commit in their header: the five CSV files and 18 files written only with the deconvolution sandbox, the ones S5 Text §4 lists.
- Evidence: first three lines of every .csv/.md/.txt under `results/` and `notes/review_results/`; `S5_Text.md` L25.
- Grade: inexact.

**VT1-7**
- Where: `draft_v2.md` L241 (Methods): "S19 Table says of each computation whether it had a recorded prediction or was post hoc"; S19 Table, `supplementary.md` L1601, L1671–1674, L1689.
- Problem: for two sets of exploratory p values the main text quotes, S19 has no row.
  - The sts pre- and post-injection gaps (p = 0.2307, p = 0.0001; Results 2, Table 2), the baseline-adjusted contrast and Table 3's rows 2–6. The B27 pre-run entry lists these as known before the run and "not predictions"; S19's B27 rows concern r₁'s gaps and the gap correlations, and neither its head note nor the sentence after Part A names B27's known values.
  - The residual's exact p against the three expectations (0.108, 0.218, 0.251; Abstract 0.11–0.25), B21 (b), which only the head note mentions.
- Evidence: record L8600–8626 ("These values are the script's expected output for those cells and are not predictions"); S19 rows as cited.
- Grade: note.

**VT1-8**
- Where: `manuscript/si/S4_Text.md` L53 (S6): "every post hoc or review computation is labelled at first mention".
- Problem: this is not true of the main text's first mentions; it is the T18 problem in another file, unchanged by the revision. Four computations of S19 Part B are quoted in the main text without such a label: ΦR's contrast (L154), the finite-sample null (L59, L124, L245), manufacture (L173, L249), and the pair r₁ and |q| DiDs (L106). The supporting texts do label them.
- Evidence: `supplementary.md` L1695–1697 and L1705 against the main-text lines cited.
- Grade: note.

**VT1-9**
- Where: `manuscript/si/S3_Text.md` L321 (§6, the residual table's caption): "and its group means by −0.74 per unit of pair r₁".
- Problem: this is the same ratio of the printed means (+0.0115 / −0.0155), without the marking that the T25 disposition says the value carries in Results 4, Fig 3's caption and S13 Table's note. The caption is declared moved "unchanged", and the table's data row prints both means.
- Evidence: `S3_Text.md` L321, L325; `draft_v2.md` L124; `supplementary.md` L363.
- Grade: note.

**VT1-10**
- Where: two unqualified phrasings left beside corrected ones.
  - `manuscript/supplementary.md` L3: "S12–S20 Tables, which carry material moved from the main text on 23 September 2026, the results of B21–B24, the record's predictions …".
  - `draft_v2.md` L150, heading: "### 6. CCS: a near-zero synergy atom, nearly flat in r₁".
- Problem: the head note does not name S18 Table's new part (B28, L1588), the omission T28 found in the main text's list. The heading keeps the phrase to which the Abstract now adds "on the family" (T29 (i)). Both predate the revision and are unchanged by it.
- Evidence: `supplementary.md` L3, L1339, L1588; `draft_v2.md` L150, L152.
- Grade: note.

## Verdict per finding

| Finding | Verdict |
|---|---|
| T01 | Correction verified. |
| T02 | Correction verified. |
| T03 | Correction verified; one sentence of the disposition is inexact (VT1-4). |
| T04, T05 | Corrections verified. |
| T06, T07, T08 | Corrections verified; the same kind of second rounding stands at record L9264 (VT1-1). |
| T09, T10, T11 | Corrections verified. |
| T12 | Verified for (i), (iii) and the captions; for (ii) the record's paragraph still omits one drawing change (VT1-2). |
| T13 | Correction verified in the text; the disposition and the record's A m8 are inexact for the entry of S3 Text (VT1-3). |
| T14, T15, T16 | Corrections verified. |
| T17 | Verified, (i)–(iii); the unqualified statement persists in S4 Text Sh3 (VT1-6). |
| T18 | Verified, (i)–(iii); notes VT1-7 and VT1-8. |
| T19, T20, T21, T22, T23, T24 | Corrections verified. |
| T25 | "Stated, not changed" verified at the three places named; unmarked in S3 Text §6 (VT1-9). |
| T26 | Correction verified in the text; the old wording stays in one numbers-table note (VT1-5). |
| T27 | Correction verified. |
| T28 | Correction verified; note VT1-10. |
| T29 | Correction verified, (i)–(iv); note VT1-10. |
| T30, T31 | Corrections verified. |

Not checkable in the tree: R08's and R09's statements about the planning session's packaging checks, and the cited papers themselves (T19, T21 and T30 were checked against the claim record and `screening.md` only).

## Checked and found exact

**Quotations.** Every phrase the dispositions of T01–T31 (and of the R-findings they point to) put in quotation marks occurs word for word in the file named: 37 phrases checked by script against the main text, S1, S3, S4 and S5 Text, `supplementary.md`, the figure script, the literature file and the record.

**T01.**
- Recomputed from `inference_rows_diag.pkl` and `inference_rows_ccs_pub.pkl`: r(residual DiD, CCS-sts DiD) is 0.799 at W = 60 and 0.094 at the global fit. This matches `ccs_pub_tables.md` L29 and L59 and S3 Text L382.
- CCS-sts's p = 0.0002 belongs to the global fit (0.0559 at W = 60), as the record's A m5 says.
- The numbers table's two rows are on S3 Text L382.
- No other sentence in the main text, S1–S5, `supplementary.md`, CLAUDE.md, README.md or the five new entries joins the global-fit rise to the W = 60 correlation.

**T02.** `primary_b_ts_gsr_win60.csv` L49 gives −0.9833 with "|rho|>=0.80: PASS; sign - vs prereg +"; S2 Table gives VOID. "met in sign" is nowhere in the manuscript files. The record's C m18 agrees.

**T03.**
- Recomputed from `regional_atoms_raw_ts_gsr_win60.npy` (placebo run, windows 1–4, last atom) and `regional_sts_r1.csv`:

| Quantity | Pearson r | Spearman | Slope | Cortical r |
|---|---|---|---|---|
| Windowed sts | 0.898393 | 0.868350 | 2.303755 | 0.849611 |
| Windowed rtr | 0.686293 | 0.672864 | 0.5118 | 0.541037 |
| Global-fit sts | 0.862939 | 0.835114 | 3.088677 | 0.807011 |

- The array's whole-brain sts for windows 1–4 is 1.155377 (DMT) and 1.137790 (placebo).
- All of this equals Results 3, S3 Text §4 (L132) and `derived_r24.out` item 7.
- The relation is marked post hoc in Results 3, in S3 Text §4 and in S19 Part B. The pre-run entry of 15 September does name the two estimators.
- "the only regional atoms saved" occurs only in the audit files, `read_B.md` and the record's statements that it was not so.

**T04.** Results 2 L87 has the refutation sentence; S1 Text L9's pointer holds; Methods (Inference) says the two-sided reading was fixed after the global fit; R201's reason, CLAUDE.md L23–25 and README L14–15 agree.

**T05, T22.**
- Table 2's caption defines the three readings, and "the three rows marked r₁" are rows 8–10.
- Every cell of Table 2's gap and adjusted rows equals `baseline_gap_tables.md` (a).
- Recomputed from `baseline_gap.csv`: r₁'s DiD, post-injection gap and adjusted contrast are −0.0146, −0.0122 (13 of 14) and −0.0110, all negative; its pre-injection gap is +0.0025 (p = 0.4417).
- Also recomputed: r(DiD, pre gap) = −0.888 (r² 0.788); SDs 0.0887, 0.0485, 0.0524; −0.844; +0.939; partial +0.824; slope 4.2627 [3.408, 5.117].

**T06.** From `splithalf_subjects.csv`: r = 0.742180 and 0.645165, mean 0.693672, Fisher-z interval [0.258078, 0.894889], ceiling 0.729225, ratio 0.951246. Abstract "0.69 [0.26, 0.89]", Results 2 and Fig 3's caption "[0.258, 0.895]" and the Discussion's 0.69 all agree. The Abstract's three rows are data rows on `derived_r24.out` L58.

**T07, T25.**
- "2.645 per subject" equals the +2.6450 of `regional_partial_tables.md` and S3 Text L156; no "2.65" is left.
- −0.74 equals +0.0115 / −0.0155 and is marked "from the printed means" in Results 4; Fig 3's caption gives the two means; S13 Table's note has the quoted words.
- No committed file holds the pair r₁ DiD beyond four decimals (`residual_source.log` L10; no array holds windowed pair r₁).
- S5 Text §4 (L27) describes the audit's computations as the findings file does (2.644997; −0.015468; −0.861 [−1.299, −0.422]), and none of those values is used in the paper. The Use of AI tools statement points there.

**T08.** From the two prewhitening pickles, r with its Fisher-z interval:

| Order | r | Interval |
|---|---|---|
| p = 10 | +0.444867 | [−0.112, +0.789] |
| p = 20 | +0.332750 | [−0.240, +0.734] |
| p ≤ 5 | +0.495364 | [−0.048, +0.812] |
| p = 1 | +0.898873 | [+0.704, +0.968] |

These equal S3 Text §8 (L540), Table 4's r column, S11 Table's note and "B16c, outcome". Seven of the eight cells at p = 10 and 20 include zero. No "+0.45" is left.

**T09.** In all nine rows of sts, r₁ and the substituted sts the adjusted contrast is the smallest of the three in size, and the signs agree (table (a), and recomputed).

**T10, T23.**
- `partB28_matched_slope.py`: the data's regressor is the whole-brain r₁ DiD (L98–100); the generators' is the window-level pair a (L196–198, L236).
- The step is at sample 300, the start of window 6; the ramp runs over samples 300–419, windows 6 and 7 (L71, L167, L183).
- The SD uses `np.std` with divisor 100 (L244); the Δa are rescaled to a mean of −0.0150; the floor is −0.0375 with subject 8 at −0.0657.
- Table 3's four generator rows equal `matched_slope_tables.md` and my recomputation from `matched_slope.csv`. No replicate slope is as steep as the data's (the minimum is −0.596).
- Table 3's data rows, recomputed from the pickles:
  - all subjects: −0.753 [−1.133, −0.373], r −0.780;
  - one left out: −0.791 to −0.699, with 0, 0, 11 and 11 intervals containing 0, −0.18, −0.39 and −0.37;
  - two left out: −0.906 to −0.642, with 1, 13, 71 and 63;
  - without subject 8: −0.785 [−1.361, −0.208];
  - without subject 14: −0.699 [−1.180, −0.218];
  - without both: −0.667 [−1.561, +0.227].
- Also recomputed: SE 0.0051; detectable difference 0.015504; excesses 0.0088, 0.0066, 0.0061; exact p 0.1075, 0.2183, 0.2507; g 0.611.
- Results 4, Fig 3's caption, Methods L245, S3 Text §6 and S18 Table name the regressors and the step and ramp consistently. "at the injection", "pair-a" and "like-for-like" are gone from the main text.

**T11, T12.**
- Script L445: (c) spans 0.05 nats on a height ratio of 0.20, against 0.30 on 0.30, a quarter of the nats per unit height.
- Running the HEAD script in my clone, `figures_check.py` condition 1 holds: the header names HEAD, the captions of Figs 1, 3, 4, 5 and 6 changed and equal the main text's without their Source sentence, and Fig 2's is the committed one.
- With the committed and the revised script in one environment (matplotlib 3.10.9): Fig 5's PNG changes by −1.10 % in width and +0.11 % in height, the other five sizes do not change, and Figs 2, 4 and 6 are pixel-identical. This is as R49 says.
- The first line of Fig 5c's title is the committed title and overruns the axes as it does in the committed figure.
- `figures_check.py` tests exactly conditions (1)–(3) of the record's paragraph.
- Six-sevenths is exact (0.60 / 0.70).

**T13.** "scope map" is gone from the main text. "the map" there is only the regional map. S3 Text §4 (L128), S20's head note and S5 Text §1 (L7) say what the record says. The numbers-table note at L105 is reworded; README L22 calls it the surface.

**T14.** S1 Text L5 and L11 and S4 Text D6, D9 and A5 all agree with the two results now in the main text.

**T15, T30.**
- S3 Text §10's string equals `search_string.txt`.
- The folder holds 11 records: six of the nine, four outside the criterion (O-information, local O-information, partial entropy decomposition, a software library) and Gao et al. (2026).
- The Search details were not kept.

**T16.** No reviewer's letter, round, stage or bundle name in any manuscript file. "planning session" and "writer's session" occur only in S5 Text L33 (§5). The four S3 passages name the roles S5 §5 defines. No computation label stands before "## Supporting information".

**T17.** Each of the eight removed details is in S5 Text L29 (§4): `tests.yml` and phyid's own tests; `rev_phiid_fast.py`; the tool's NaN; the figures' file names; "written at its text commit"; "rounded down"; "lag covariance of no process"; the three wall-clock times. The 8, 475 and 225 min agree with the start and end times in L25. The tests and the workflow do what L29 says.

**T18.**
- Every p value of the main text was listed and classed. The five items Methods names are marked where it says: L106, L87, L114 and L116, L146, L171.
- S19 has B22 (e) in Part A ("below its predicted range"), and the leave-one-out, the centroid and the deconvolution in Part B.
- ΦR's sign-flip p is at least 0.0853, and the three phase-randomised p (0.0190–0.0380) are of opposite sign across variants (S15 Table, `inference_rows_raw.csv`).
- No threshold wording on an exploratory quantity is left.
- S19's verdicts count 36 met, 15 partly met and 16 missed, 67 in all.
- Every "reported at" and "where quoted" cell of S19 that names a main-text section holds.

**T19, T20, T21.**
- S20 row 3 and the literature file have the neutral form; the Introduction matches.
- The Abstract has A's clause.
- The six exclusions are cited to Singleton et al. alone in Methods; both counts are in S1 Text and S4 D4; the claim record's pointer agrees.

**T24.** From `matched_slope.csv` (11 fields under a header of 10): means +0.002182, +0.002034, +0.004851, +0.004232; differences 0.000148 and 0.000620. These match Results 4, S3 Text L402, "B28, outcome" (c), S19's row and the two numbers-table rows.

**T26, T27, T28.**
- The exclusion rule is worded correctly in Results 2 and Fig 3's caption.
- "pre-defined" is nowhere in the manuscript files or the script.
- The entries of S3 Text, S5 Text and S18 Table name the new parts, each of which exists.

**T29.**
- Every clause of the Abstract was checked against the Results and Table 4.
- Table 4's five rows were recomputed from the pickles and `whitened_spectrum_tables.md`: r₁ 0.848, 0.751, 0.263, 0.137, 0.052; power above the band; levels; DiDs with inverted intervals; p.
- "No order removes" and "removed the contrast at no order" are gone.
- Eight of the ten studies state MMI.

**T31.** All 12 pointers of S3 Text §9–§10 into the main text hold. So do the main-text pointers of the rest of S3 Text, of S1, S2, S4 and S5 Text and of the supplementary notes.

**Second roundings.** All 781 numbers-table rows with a held source value agree at the printed precision. The two that sit on a tie (0.108 and 0.263) are right from the unrounded values 0.10754 and 0.262547.
