# Audit of the revision of 1–2 October 2026 (bundle 35B): the text

Made on 2 October 2026 by a separate session of the AI system, which had seen none of the revision before. The state
audited is the one the commission describes: a clone of `Vasilis540/dmt-phiid` at
`8bd189e7f03312c1630764a63e6360440760f4f4` ("Round 24 (2 of 4): B27, B28, B29 and B16c, the outputs as the run wrote
them"), the bundle `new_files_35B_audit.tar.gz` (sha256
`7d54465b24d222b856d99721ee1f5f61d210df606131afdc8305d596764dc5db`) unpacked into it, and the 188 replacements applied.
No file of the clone was changed and nothing was committed. At the end the diff of the 15 changed files was the same,
byte for byte, as after step 5, and the 16 new files were those of the bundle.

**The setup.** Steps 1, 2, 3 and 5 printed what the commission gives (16 files and 16 untracked; `418`, tab, `0`), and
step 4's second command printed 15. Step 4's first command did not print the line expected, for a reason that is not a
failure of the step: T53.

**How the audit was made.** I read the revised main text whole, the diff of every changed file, the record's five new
entries and the three reports. Each number of a changed passage was compared with the result file at the line the
numbers table names, and recomputed where a per-subject vector is committed. Seventeen read-only passes by helper
sessions went through the numbers table row by row, the 70 dispositions, the condensation, the supporting information
and the rules; I then checked every finding below myself against the source it cites, and what could not be checked is
marked as such. Three findings rest on the released series, which the repository does not hold (T07, T10, T25): the
time-series file of the public release was fetched outside the clone, and it reproduces the committed values it can be
tested on (Table 3's data row, the regional r₁ map of `regional_sts_r1.csv`, the pair r₁ DiD). The cited papers are not
in the repository, so statements about what a paper says were checked against the claim records only (T21, T63). The
figure script was run once, in a copy of the tree outside the clone (T12).

**Severity.** *blocking*: the main text states something that the result files or the repository contradict, on a
point a reader relies on. *should fix*: a number that is not its source at the printed precision, a statement or a
caption that is not true as written, a disposition the text does not bear out, a rule of the record not applied.
*minor*: an inexact wording, a stale pointer, a count, a piece of bookkeeping. *note*: for the record; it needs no
change by itself, or it could not be verified here.

**Reading the blocks.** `L<n>` is line n of the file in the working tree; the manuscript files hold one paragraph to a
line. "Committed" is `git show HEAD:<file>`. `reviews/`, `checks/` and `claims/` are the folders of
`notes/review_2026-10-01_cold_reads/`. Quotations are exact but for line breaks. Where a block gives the right value of
a number, that is its evidence; no wording is proposed.

**Count.** 63 findings: 3 blocking (T01–T03), 18 should fix (T04–T21),
31 minor (T22–T52), 11 notes (T53–T63).

## Findings

### T01 — blocking
Where: `manuscript/draft_v2.md` L193 (Discussion, "The literature", last sentence); the record's disposition of A's m5 (`manuscript/analysis_record.md` L9150–9151) says the same.
Text: "The one lead this dataset offers for an independent test is CCS-sts's rise at the global fit (Results 6), whose per-subject change correlates with the residual's at r = 0.80 (S3 Text §6)"
Problem: The correlation of 0.80 belongs to the other estimator. Across subjects the residual DiD correlates at +0.799 with the CCS-sts DiD at W = 60, whose DMT contrast is +0.0044 [−0.0001, +0.0088] (p = 0.056). With the CCS-sts DiD of the global fit, the rise the sentence names (+0.0197, p = 0.0002), it correlates at +0.094. The sentence joins the global fit's rise to the W = 60 correlation, as finding A m5, which it answers, had done.
Evidence: `notes/review_results/partB/ccs_pub_tables.md` L29, in the block "ts_gsr W60": "vs the B4 residual DiD (W60): r = +0.799 (p = 0.001)"; L59, in the block "ts_gsr global-bins": "vs the B4 residual DiD (W60): r = +0.094 (p = 0.749)". `manuscript/si/S3_Text.md` L380: "correlates with the CCS-sts DiD at r = +0.799 on `ts_gsr` at W = 60, +0.094 at the `ts_gsr` global fit". `manuscript/main_text_numbers.csv` L1138, the row's own note: "r(residual DiD, CCS-sts DiD) at W = 60, ts_gsr". The two contrasts: draft L154. Finding A m5: `reviews/read_A.md` L34.

### T02 — blocking
Where: `manuscript/draft_v2.md` L108 (Results 2, last sentence); the record's disposition of C's m18 (L9254–9255).
Text: "the pre-specified intensity-tracking criterion, the group-mean sts series against the ratings over the decay windows, was met in sign (Spearman ρ = −0.98) and void under its pre-specified controls"
Problem: The criterion is a threshold on the size of the correlation, |ρ| ≥ 0.80, and −0.98 passes it. Its sign is negative, against the pre-specified positive direction; the record's rule for that case is that the sign is reported separately, as tracking in the direction opposite to the hypothesis. The words "met in sign" say the reverse of what the result file, S2 Table and S1 Text say.
Evidence: `results/primary_b_ts_gsr_win60.csv` L49, the row "raw rho_S group-mean sts series vs template [THRESHOLDED]": value −0.9833, p 0.0020, note "|rho|>=0.80: PASS; sign - vs prereg +". S2 Table's source note (`manuscript/supplementary.md` L21): "Every ρ_S of sts is negative, against the pre-specified positive direction." `manuscript/analysis_record.md` L637–646 ("the sign is reported separately against the pre-registered direction") and L1448–1451 ("sign negative against the pre-registered positive direction"). `manuscript/si/S1_Text.md` L11: "The tracking was significant and negative".

### T03 — blocking
Where: `manuscript/draft_v2.md` L114 (Results 3, first sentence). The record's dispositions of A's m9 (L9156–9158) and of B's MINOR 3 (a) (L9188–9190) rest on it.
Text: "regional MMI-sts (the global-fit value, the only regional atoms saved; S3 Text) correlates with regional r₁ (windowed, windows 1–4) at r = 0.863 over the 115 regions"
Problem: The repository holds regional atoms of the windowed estimator as well: `notes/review_results/regional/regional_atoms_raw_ts_gsr_win60.npy` (with its ts_demean and global-fit counterparts), an array of 14 subjects × 2 runs × 14 windows of 60 TRs × 115 regions × 16 atoms, tracked since 15 September 2026. So the reason the sentence gives for setting a global-fit atom against a windowed r₁ is not true, the S3 Text it cites does not say it, and the same-estimator relation that A's m9 asked for can be computed from committed files. The per-subject slope the disposition offers in its place (2.65) is on the same two estimators as the group slope. The clause is taken from the wording of B's MINOR 3 (a). For the record of what the clause leaves out, and not as a result for the paper (no pre-run entry covers it): on the saved windowed atoms (placebo run, windows 1–4, group mean) regional sts against the same regional r₁ gives r = 0.898 and a slope of 2.30.
Evidence: `git ls-files notes/review_results/regional/` lists eight `regional_atoms_*` arrays; `git log -1 -- notes/review_results/regional/regional_atoms_raw_ts_gsr_win60.npy` gives 9318997 (2026-09-15). The array's shape is (14, 2, 14, 115, 16); its last atom, averaged over regions, subjects and windows 1–4, is 1.155377 on the DMT run and 1.137790 on the placebo run, Table 2's 1.1554 and 1.1378. `notes/rev_regional_phir.py` L10–11: "the 16 atoms per region are stored, so sts etc. are available too"; L16: "regional_atoms_<series>_<variant>_<estimator>.npy (14, 2, n_t, 115, 16)". S3 Text §4 (L130) says only that the map is "from the saved regional atoms of `scripts/11_regional_analysis.py`". `reviews/read_B.md` L35: "say this is because only the global-fit regional atoms were saved"; `reviews/read_A.md` L42: "report the same-estimator version".

### T04 — should fix
Where: `manuscript/draft_v2.md` L87 (Results 2) and L261 (Methods, Pre-registration and deviations); `manuscript/si/S1_Text.md` L9; the reason given with replacement R201; the record's disposition of B's MINOR 6 (L9195–9196).
Text: "under the directional-failure rule the significant decrease refutes that hypothesis as operationalised"
Problem: This clause of the committed Results 2 is removed, and no form of "refute" is left in the main text. The reason recorded with the replacement is that the sentence on the rule is one "which Methods states"; Methods names the rule ("The directional-failure rule and the windowed test statistic were written on the next day") and says neither what the rule is nor that the decrease refutes the hypothesis. The statement now stands in S1 Text alone, whose L9 still sends the reader to the main text for it. B's MINOR 6 asked for the sentence to be made firmer (it "should say that the pre-registered increase failed regardless of the two-sided p"); the disposition answers the first half of that finding only. The record's rule is that a significant decrease "refutes the stated hypothesis and is reported as a refutation", and CLAUDE.md's standing rule 9 repeats it.
Evidence: `git show HEAD:manuscript/draft_v2.md` L87; `grep -c refut manuscript/draft_v2.md` gives 0. S1_Text.md L9: "Under the directional-failure rule this refuted the up-regulation hypothesis as operationalised, an increase of whole-brain MMI-sts (main text, Results 2)." The replacements file, R201, "why": "the sentence on the directional-failure rule, which Methods states, is not repeated". `reviews/read_B.md` L41. analysis_record.md L1125–1130; CLAUDE.md, "Standing methodological rules", 9.

### T05 — should fix
Where: `manuscript/draft_v2.md` L89 (Table 2's caption) against the table's rows (L93–104).
Text: "The last three rows give the same readings for whole-brain lag-1 autocorrelation r₁ (dimensionless), whose DiD is in the text."
Problem: Table 2 has twelve rows and the three r₁ rows are its eighth to tenth. Its last three rows are "r₁, baseline-adjusted contrast", "FD DiD" and "DiD, FD-residualised".
Evidence: draft L100–104, in order: "r₁, pre-injection gap", "r₁, post-injection gap", "r₁, baseline-adjusted contrast", "FD DiD", "DiD, FD-residualised".

### T06 — should fix
Where: `manuscript/draft_v2.md` L15 (Abstract).
Text: "across subjects the two DMT-minus-placebo differences covary (cross-half r 0.69 [0.26, 0.90], disattenuated 0.95), partly through that gap"
Problem: The interval's upper limit is 0.894889, which is 0.89 to two decimals. 0.90 is a second rounding of the three-decimal 0.895 that Results 2 (L108) and Fig 3's caption (L110) print; the numbers table's row (L25) records it as "+0.895 … to two decimals". The clause is new in this revision.
Evidence: Recomputed from `notes/review_results/partB/splithalf_subjects.csv` as `notes/partB21_inference_revision.py` defines it (L35 and L583: tanh(atanh r ± 1.959964/√11) at the arithmetic mean of the two cross-half correlations, 0.693672): [0.258077, 0.894889]. `notes/review_results/partB/inference_revision_tables.md` L273 prints "[+0.258, +0.895]".

### T07 — should fix
Where: `manuscript/draft_v2.md` L114 (Results 3); the record's disposition of A's m9 (L9158) repeats the value.
Text: "The map's slope on regional r₁, 3.09 nats per unit (2.65 per subject; S3 Text), relates a global-fit atom to a windowed r₁"
Problem: The mean per-subject slope is 2.644997, which is 2.64 to two decimals. 2.65 is a second rounding of the +2.6450 that the result file and S3 Text print. The value is new in this revision.
Evidence: `notes/review_results/partB/regional_partial_tables.md` L74 and S3_Text.md L154: "+2.6450". Recomputed with the script's own code (`notes/partB20_regional_partial.py` L99–117) from `results/regional_atoms_bins_115regions-all_ts_gsr_global.npy` and the released series: mean slope 2.644996924, mean r² 0.576258 (0.576 as printed); the same code's group maps equal `regional_sts_r1.csv`. No committed file holds the slope beyond four decimals, so this rests on the released series.

### T08 — should fix
Where: `manuscript/si/S3_Text.md` L538 (§8, the reading of B16c's table).
Text: "with the per-subject correlation of the sts DiD with the whitened r₁ DiD at +0.45 and +0.33 against +0.495 at p ≤ 5"
Problem: At p = 10 the correlation is 0.444867: +0.44 to two decimals, +0.445 to three, as Table 4 and S11 Table's note print it. +0.45 is a second rounding. (+0.33 at p = 20 is right: 0.332750.)
Evidence: Recomputed from the per-subject vectors of `notes/review_results/inference_rows_prewhiten_fixed.pkl` (rows "prewhiten_fixed ar10 MMI sts ts_gsr W60" and "prewhiten_fixed ar10 autocorr ts_gsr W60", set "primary", field `did_subjects`). `notes/review_results/partB/prewhiten_fixed_tables.md` L28: "+0.445".

### T09 — should fix
Where: `manuscript/si/S3_Text.md` L218 (§5, the reading of B27's tables) against table (a) above it (L195–206).
Text: "The three readings of the contrast agree in sign on both variants and at both window lengths, the adjusted contrast lying between the DiD and the post-injection gap."
Problem: In every sts row of the table the adjusted contrast is smaller in size than both of the others and so does not lie between them: on ts_gsr at W = 60 the DiD is −0.0809, the post-injection gap −0.0633 and the adjusted contrast −0.0544; on ts_demean −0.1031, −0.0846, −0.0796; on ts_gsr at W = 30 −0.0686, −0.0526, −0.0453. The same holds in the r₁ rows and the AR(1)-substituted rows. Of the table's twelve rows only the residual on ts_demean (+0.0182, +0.0083, +0.0127) has the adjusted value between the other two.
Evidence: S3_Text.md L195–206, which equal table (a) of `notes/review_results/partB/baseline_gap_tables.md` cell for cell.

### T10 — should fix
Where: `manuscript/draft_v2.md` L126 (Table 3's caption); with it L124 (Results 4) and L110 (Fig 3's caption).
Text: "the slope is the ordinary least-squares (OLS) slope of the residual DiD on the whole-brain r₁ DiD across the 14 subjects (intercept free)"
Problem: That is the regressor of the data rows. The generator rows' slopes are on the simulated pairs' own pair-r₁ DiD, as the result file, S3 Text §6 and S18 Table say; the caption gives the one definition for all ten rows. Results 4 then sets the data's slope per unit of whole-brain r₁ beside the generators' slopes per unit of pair r₁ as "the like-for-like comparison" without naming the difference. Fig 3's caption does name the generators' regressor, as "pair-a DiD", a term the main text does not define (its notation paragraph has "pair r₁"). The comparison's outcome does not turn on this: on its own pair r₁ DiD the data's slope is steeper, not shallower.
Evidence: `notes/review_results/partB/matched_slope_tables.md` L4: "the slope = OLS of the residual DiD on the pair-a DiD across the 14 subjects (intercept free)"; S3_Text.md L391; supplementary.md L1590; draft L110: "means over replicates per unit of pair-a DiD". The data's slope on the pair r₁ DiD, recomputed from the released series and `notes/review_results/partB/diag_series_ts_gsr_W60.npz`: −0.861 [−1.299, −0.422], r = −0.777 (the same computation gives the pair r₁ DiD's mean as −0.015468, the text's −0.0155, and reproduces Table 3's data row, −0.753 [−1.133, −0.373], r = −0.780).

### T11 — should fix
Where: `manuscript/draft_v2.md` L122 (Fig 5's caption); `scripts/15_figures_v2.py` L22, L439 and the caption string (L473); the record's disposition of C's m9 (L9244–9245).
Text: "drawn at four times the nats per unit height of (a) and (b) (y-range −0.02 to +0.03 nats)"
Problem: The statement is the wrong way round. Panels (a) and (b) span 0.30 and 0.20 nats on height ratios of 0.30 and 0.20; panel (c) spans 0.05 nats on a height ratio of 0.20. Panel (c) therefore has a quarter of the nats per unit height of (a) and (b), that is, four times the height per nat.
Evidence: `scripts/15_figures_v2.py` L438–440: `YL_A, YL_B = (1.00, 1.30), (-0.15, 0.05)`; `YL_C, H_C = (-0.02, 0.03), 0.20`; `height_ratios=[YL_A[1] - YL_A[0], YL_B[1] - YL_B[0], H_C]`. Nats per unit of height ratio: 0.30/0.30 = 1, 0.20/0.20 = 1, 0.05/0.20 = 0.25.

### T12 — should fix
Where: `scripts/15_figures_v2.py` L465 (Fig 5c's title), L440 (the height ratios) and the legend line of Fig 3; the record, "The figures" (L9285–9291); `notes/review_2026-10-01_cold_reads/checks/figures_check.py`.
Text: "c the DMT − placebo residual difference against its expectation under a pure autocorrelation change (y-scale four times that of a and b)"
Problem: (i) The new title of panel (c) has 137 characters at 9 pt and starts at the left edge of an axes about 6 inches wide: it runs well past the right edge of the axes. Because `save()` uses `bbox_inches="tight"`, the saved figure is widened to hold it. Run in a copy of the tree outside the clone, the script writes Fig 5 as 2,666 × 2,780 px (8.89 × 9.27 in at 300 dpi), where the committed file has 2,212 × 2,655 px (7.37 × 8.85 in); the axes then end at about three-quarters of the image's width, and the last quarter is empty but for the title's overhang. The fonts of that run are not those of V.S.'s machine, but the three figures the revision leaves alone came out within 0.2 % of their committed widths in it. (ii) The entry gives Fig 5's change as "Fig 5c's y-range and title". The diff also changes the height ratios from 0.30 : 0.20 : 0.10 to 0.30 : 0.20 : 0.20, which leaves panels (a) and (b) six-sevenths of their former height; and for Fig 3 it lowers panel (c)'s legend font from 6.8 to 6.5 pt, which the entry does not name beside the two lines. (iii) The entry says of its conditions that "Any other difference blocks the commit" and that `figures_check.py` tests them. For the PNG and PDF of Figs 1, 3 and 5 the check accepts any difference, a different image size included, and it does not test that the captions file's header names the revision's commit.
Evidence: The run: `python3 scripts/15_figures_v2.py` in a copy of the working tree without `.git`, exit status 0; widths of its Figs 2, 4 and 6: 2,254, 3,850 and 2,488 px against the committed 2,259, 3,854 and 2,491. `git diff HEAD -- scripts/15_figures_v2.py` (the lines with `YL_C, H_C`, `height_ratios`, `set_title` and `fontsize=6.5 if ax is axes[2] else 6.8`); `scripts/15_figures_v2.py` L135–137. `figures_check.py`: `CHANGED = {1, 3, 5}`; for a PNG of another size, `ok &= k in CHANGED`; for a PDF that "differs beyond its dates", `ok &= k in CHANGED`; the header line is accepted on its prefix "Generated by `scripts/15_figures_v2.py` at git " alone.

### T13 — should fix
Where: `manuscript/draft_v2.md` L397 (Supporting information, the entry for S3 Text), L191 (Discussion) and L441 (the entry for S20 Table); `manuscript/si/S3_Text.md` L128; `manuscript/si/S5_Text.md` L7; the record's disposition of A's m8 (L9154–9156).
Text: "the closed form's checks and the coupled family; the scope map, the within-window regression and the regional maps"
Problem: The disposition says that "scope map" is retired from the text and that S3 Text §4's heading, S20 Table's title and column "and the SI list follow". The SI list's entry for S3 Text still names "the scope map", although §4's heading is now "The map over (r₁, q), …"; in the list only S20 Table's entry was changed. The term also stays in S3 Text L128 ("The scope-map tables are") and S5 Text L7 ("scope map, CCS, lag dependence, diagnostic, literature table"). With Fig 1 retitled, "the map" of the Discussion ("the reported effect on the map", "what the map predicts") and of the SI list's entry for S20 Table ("the map's reading of each") has no referent left in the main text, where the only thing now called a map is the regional map.
Evidence: draft L55 (Fig 1's title: "The sts surface of the family, the data's operating point, and the coupled family."), L191, L397, L441; S3_Text.md L126 and L128; S5_Text.md L7; `git diff HEAD -- manuscript/draft_v2.md`, in which L441 is the one line of the SI list changed for this term.

### T14 — should fix
Where: `manuscript/si/S1_Text.md` L5 and L11; `manuscript/si/S4_Text.md` L14 (D6), L17 (D9) and L27 (A5); against `manuscript/draft_v2.md` L108 (Results 2) and L187 (Discussion).
Text: "The intensity ratings supplied with the data enter no result of the main text"
Problem: The revision puts a result from the ratings into Results 2 (the intensity-tracking criterion, ρ = −0.98) and the EEG Lempel–Ziv result into the Discussion (ρ = −0.24, one-sided p = 0.002). The supporting texts still say that neither enters the main text: S1 Text L5 (quoted) and L11 ("which is why they enter no result of the main text"); S4 Text D6 ("used in no main-text result"), D9 ("enter no main-text result") and A5, where the EEG Lempel–Ziv regressor "is used only in the original pre-specified analysis (S1 Text, S6 Table), not in the main text".
Evidence: draft L108 and L187; neither sentence is in `git show HEAD:manuscript/draft_v2.md`. S1_Text.md L5, L11; S4_Text.md L14, L17, L27.

### T15 — should fix
Where: `manuscript/si/S3_Text.md` L550 (§10).
Text: "its 11 records, their screening and PubMed's own reading of the string are in the literature file's folder"
Problem: PubMed's reading of the string was not kept, as the search's own file and the record say. And the records and their screening are in the review folder's `pubmed_search/`, not in the folder of the literature file (`notes/partB5_literature_v2.md` lies in `notes/`).
Evidence: `notes/review_2026-10-01_cold_reads/pubmed_search/search_string.txt`: "how PubMed read the string (the query's "Search details") was not kept at the time of the search and is not recorded here"; analysis_record.md L9133: "records that PubMed's reading of the first string (its Search details) was not kept"; the folder holds `pubmed_search.csv`, `screening.md` and `search_string.txt`.

### T16 — should fix
Where: `manuscript/si/S3_Text.md` L189, L222, L391, L525; `manuscript/si/S5_Text.md` L25 (§4); the record, "The checks" (L9283).
Text: "The cold read of 1 October 2026 (B, MAJOR 1–3) asked for these readings"
Problem: Four passages of S3 Text name the reviewers by letter, with the findings' numbers: "(B, MAJOR 1–3)" (L189), "(C, m1–m3)" (L222), "(A, M1; B, MAJOR 3)" (L391) and "(A, m4; B, MINOR 4)" (L525). No manuscript file says who A, B and C are; S5 Text §5 names the three reads by role. S5 Text §4 (L25) names "the planning session's `b27_start.sh`", a session name used before §5 introduces the names and outside §5, to which the committed text confined them. The record's entry says that the manuscript files carry no process label.
Evidence: S3_Text.md L189, L222, L391, L525; S5_Text.md L25 against L29; `git show HEAD:manuscript/si/S5_Text.md` has "planning session" four times, all in §5. analysis_record.md L9283: "The main text carries no computation label and the manuscript files no process label." The main text itself has none of these (searched for round, stage, bundle, session names and the reviewers' letters); "the cold reads" occurs once in it, in Data and code availability, and is explained only in S5 Text §5.

### T17 — should fix
Where: `manuscript/draft_v2.md` L267 (Data and code availability); the reason given with replacement DCA01; `manuscript/si/S5_Text.md` L25 (§4).
Text: "every result table and report names the commit that produced it in its header"
Problem: (i) S5 Text §4 lists what this sentence leaves out and the committed sentence allowed for: five CSV files that carry no header by design, the files written only with the deconvolution sandbox present, which carry none, and the files whose header says `nogit` or `-dirty`. (ii) The sentence that the run "reproduced every committed output within the tolerances the record set before the run, apart from two arrays that no result uses" drops two limits of the committed one, which spoke of the outputs "it regenerated" and added "apart from the differences the record listed in advance"; S5 Text §4 lists differences beyond the two arrays (rows added to two bias tables, a hand-added line, reworded and added log lines, B21's two files). (iii) The reason recorded with the replacement is that S5 Text §4 "holds every detail removed here". These removed details are in no manuscript file: that the continuous-integration workflow runs phyid's own tests at the pinned commit, and what those compare; that `tests/` checks the tool against `notes/rev_phiid_fast.py`; that the tool returns NaN where a pair's (a_x, a_y, q) are those of no AR(1) pair; the figures' file names, and that each revision's figures were written at its text commit and committed in the next; "the lag covariance of no process"; "rounded down to the minute".
Evidence: S5_Text.md L25: "apart from five CSV files that carry no header by design (named below)" and "The four comparisons found no difference that the entry's rule does not allow but one, in the binaries." with the list that follows it. The first line of `notes/review_results/inference_rows_raw.csv` is its column names; that of `results/synergy_bins_20regions_ts_gsr_global.csv` ends "git=nogit". Committed text: `git show HEAD:manuscript/draft_v2.md` L246. No occurrence in draft_v2.md, si/S1–S5_Text.md or supplementary.md of "tests.yml", "own tests", "discrete modes", "those of no AR(1) pair", "fig1_v2_scope_map", "lag covariance", "written at its text commit" or "rounded down".

### T18 — should fix
Where: `manuscript/draft_v2.md` L241 (Methods, the primary contrast and the exploratory analyses) against L116 (Fig 4's caption), L114, L87, L154 and L171; S19 Table (`manuscript/supplementary.md` L1652, L1703); the record's disposition of B's MINOR 8 (L9198–9200).
Text: "where the text draws on one (the r₁ contrast, Results 2; the residual map's network structure, Results 3; the spectral centroid, Results 5) the quantity is marked post hoc"
Problem: The three named quantities are marked where the sentence says (L106, L114, L146). Three things do not agree with it. (i) Fig 4's caption quotes the same network spin test unmarked and sets its two p values against each other ("spin p 0.0009, against 16.933, spin p 0.0564, for the unpartialled map"), which Results 3 now says are not comparable. (ii) By the paper's own classification the network spin test is not a post hoc computation: S19 Table lists it in Part A as B22 (e), with a prediction recorded before the run (verdict "partly met", the residual map's p "below its predicted range"), S3 Text §4 cites its pre-run entry, and Methods (L261) keeps "the post hoc computations" for those entered without a rule and a prediction. (iii) Other exploratory p values from which the text draws a statement are not marked: "in each leave-one-out refit on each variant (p ≤ 0.008)", given for "The contrast held" (L87; S19 Table's Part B lists the leave-one-out as "A post hoc check"); "no cell's sign-flip p is below 0.05" for ΦR (L154; a threshold wording, which the same Methods sentence excludes, on inference that Part B lists among the review computations of 14 September); and "left the contrast in place (−0.0782, p = 0.0013" for the deconvolved series (L171). The clauses quoted from L154 and L171 are as in the committed text; the Methods sentence that now describes them is new.
Evidence: draft L87, L106 ("(a post hoc quantity)"), L114 ("(p = 0.0009, post hoc; not comparable with the unpartialled map's 0.0564"), L116, L146 ("p = 0.022; post hoc"), L154, L171, L241, L261. supplementary.md L1652 (the row "B22 (e), the network spin test"), L1695 and L1703 (Part B). S3_Text.md L157.

### T19 — should fix
Where: `manuscript/supplementary.md` L1718 (S20 Table, row 3, last cell) and the same cell of `notes/partB5_literature_v2.md`; the record's disposition of C's M5 (a) (L9225–9226).
Text: "the synergy by whose rank the workspace is defined, which the study calls the persistent synergy (p. 6) but writes as the whole-minus-max synergy of Eq. 5"
Problem: C's M5 (a) asked that this point about Luppi et al. (2024) be stated neutrally, and the disposition answers "(a) the Introduction states the definition neutrally". The Introduction and Results 1 do. The "calls … but writes as" form that the finding objected to stays in S20 Table's row 3 and in the literature file it is transcribed from, so that the paper now states the point in two ways.
Evidence: `reviews/read_C.md` L29; draft L25 ("their synergy is the whole-minus-max sum given in Results 1") and L49; supplementary.md L1718; the same words occur once in `notes/partB5_literature_v2.md`.

### T20 — should fix
Where: The record's disposition of A's w4 (`manuscript/analysis_record.md` L9173–9174) against `manuscript/draft_v2.md` L15 (Abstract).
Text: "w4 (the 4.7-to-1 ratio's qualifying clause): Abstract: per within-window standard deviation of the pairs, neither input being lagged coupling (C's w4)."
Problem: The Abstract reads "(4.7 to 1 per within-window standard deviation); lagged coupling can move it either way". The clause A's w4 asked for ("neither input is lagged coupling") is not in it, nor are the words "of the pairs". C's w4, which asked for "within a window", is answered.
Evidence: draft L15; `reviews/read_A.md` L62; `reviews/read_C.md` L81.

### T21 — should fix
Where: `manuscript/draft_v2.md` L213 (Methods, Dataset); `manuscript/si/S1_Text.md` L5; `notes/review_2026-10-01_cold_reads/claims/claims_2026-10-01.md` L12–14. Checked against the claim record only: the two papers are not in the repository, and this overlaps the audit of the citations.
Text: "excluded six of the twenty participants for more than 20 % of such volumes (Timmermann et al., 2023; Singleton et al., 2025, Methods and Reporting Summary)"
Problem: The revision's claim record gives the count "Six out of 20" to Singleton et al. (2025) and a different one to Timmermann et al. (2023): four discarded for the 8-min post-DMT period and three more for the 28-min analysis. The sentence cites both works for six, and S1 Text L5 does the same. The claim record adds that Timmermann's count is "Stated in S4 Text (D4) and beside Singleton et al. (2025)'s count in the main text's Dataset paragraph"; neither place states it (S4 Text D4 gives six and cites Singleton et al. alone).
Evidence: claims_2026-10-01.md L12–14 and L31–35; draft L213; S1_Text.md L5 ("(Timmermann et al., 2023, Methods; Singleton et al., 2025, Methods and Reporting Summary)"); S4_Text.md L12.

### T22 — minor
Where: `manuscript/draft_v2.md` L106 (Results 2) against L87 and Table 2's title and caption (L89).
Text: "r₁'s three readings agree in sign (Table 2: pre-injection gap +0.0025, p = 0.4417; post-injection gap −0.0122, negative in 13 of 14)"
Problem: The phrase "three readings" has two extensions in the paper. Results 2's first paragraph makes them the DiD, the post-injection gap and the baseline-adjusted contrast; for r₁ these are −0.0146, −0.0122 and −0.0110 and they agree in sign. Table 2's title and caption make "the same readings" for r₁ its three r₁ rows, the pre-injection gap, the post-injection gap and the adjusted contrast (+0.0025, −0.0122, −0.0110), which do not. The sentence supports "agree in sign" with two values of opposite sign, one of them the pre-injection gap.
Evidence: draft L87 ("The DiD is one of three readings (Table 2)"), L89, L100–102, L106.

### T23 — minor
Where: `manuscript/draft_v2.md` L126 (Table 3's caption), L110 (Fig 3's caption) and L245 (Methods); `scripts/15_figures_v2.py` L287 and the caption string of Fig 3.
Text: "applied as a step at the injection or built up over the first two post-injection windows (ramp)"
Problem: The simulated step is at sample 300, the start of window 6, one window (60 samples) after the injection at TR 240; the ramp runs over samples 300–420, windows 6 and 7. Window 5, in which the injection falls, is unchanged in the simulation. The words "at the injection" occur three times; the same Methods paragraph says of the calibration that the DMT run is "changed from sample 300".
Evidence: `notes/review_results/partB/matched_slope_tables.md` L4: "(i) and (iii) the step at sample 300; (ii) and (iv) the ramp from sample 300 to 420"; analysis_record.md L8699–8702 ("at sample 300 (window 6, the first primary window)"); draft L213 ("injection at TR 240"), L122 ("injection at 8 min").

### T24 — minor
Where: `manuscript/draft_v2.md` L124 (Results 4); `manuscript/si/S3_Text.md` L400; the record, "B28, outcome" (L8993).
Text: "the ramp moves the generators' mean residual DiD by 0.0002 and 0.0007 nats from the step"
Problem: The two figures are differences of Table 3's rounded cells (+0.0022 − +0.0020 and +0.0049 − +0.0042), as the numbers table records them. The means over the replicates differ by 0.000148 and 0.000619, which are 0.0001 and 0.0006 at the printed precision. The criterion of B28's prediction (c), a difference within 0.003 nats, is met either way.
Evidence: `notes/review_results/partB/matched_slope.csv`, mean of `res_did` over the 100 replicates of each condition: 0.002182 (i), 0.002034 (ii), 0.004851 (iii), 0.004232 (iv). main_text_numbers.csv L793–794 ("|+0.0022 − +0.0020| = 0.0002", "|+0.0049 − +0.0042| = 0.0007"). analysis_record.md L8992–8993.

### T25 — minor
Where: `manuscript/draft_v2.md` L124 (Results 4) and L110 (Fig 3's caption); S13 Table's note (`manuscript/supplementary.md` L363). The value predates this revision; both paragraphs are rewritten by it. It rests on the released series.
Text: "At the group level the ratio of means, −0.79 per unit of whole-brain r₁ (−0.74 per unit of pair r₁)"
Problem: −0.74 is the ratio of two rounded values, +0.0115 / −0.0155 = −0.742. From the group means themselves the ratio is +0.011534 / −0.015468 = −0.7457, which is −0.75 to two decimals. (−0.79 beside it is right: −0.7876.)
Evidence: Recomputed from the released series and `notes/review_results/partB/diag_series_ts_gsr_W60.npz`: pair r₁ DiD −0.015468, whole-brain r₁ DiD −0.014645, residual DiD +0.011534. main_text_numbers.csv L642 and L796: "derived: +0.0115 / −0.0155 = −0.74". The committed files hold the pair r₁ DiD to four decimals only; its per-subject values were not saved (S4_Text.md L62, item R1).

### T26 — minor
Where: `manuscript/draft_v2.md` L108 (Results 2); the record's disposition of B's MINOR 2 (L9187–9188) has the same words.
Text: "a subject bootstrap of 10,000 draws, the 366 in which either half's reliability was not positive left out"
Problem: A draw is left out when the split-half reliability of the sts DiD or that of the r₁ DiD is not positive, the ceiling √(rel(sts) × rel(r₁)) then being zero. These are the reliabilities of two quantities, each a correlation between the two halves; neither is the reliability of a half. Of the 366 draws the sts DiD's reliability is not positive in 175 and the r₁ DiD's in 323 (both in 132).
Evidence: `notes/partB21_inference_revision.py` L563–567 (`ceil = np.sqrt(max(rel_s, 0) * max(rel_a, 0))`, the ratio being NaN where `ceil` is 0) and L587–597. The bootstrap repeated from `notes/review_results/partB/splithalf_subjects.csv` with the script's seed: 366 draws excluded, percentile interval [0.617, 0.991], as printed.

### T27 — minor
Where: `manuscript/draft_v2.md` L116 (Fig 4's caption), twice; the record's disposition of B's W3 (L9206–9207).
Text: "The pre-defined contrast between sensory cortex (visual and somatomotor networks, 31 parcels) and association cortex"
Problem: B's W3 said that "pre-defined" reads as pre-registered. Results 3 now says that the contrast was "fixed in the record before the partialled map was computed (S19 Table)"; Fig 4's caption keeps "pre-defined" in (b) and in its last sentence. The disposition names Results 3 only, so that the two places now differ.
Evidence: draft L114, L116; `reviews/read_B.md` L59.

### T28 — minor
Where: `manuscript/draft_v2.md` L437, L397 and L401 (Supporting information, the entries for S18 Table, S3 Text and S5 Text).
Text: "S18 Table. The residual's response to changes in lagged structure, and the other computations of 23 September 2026."
Problem: S18 Table's title now ends "and the generators' per-subject slopes under the data's heterogeneity (B23, B24, B28)", a computation of 1 October 2026 for which Table 3's caption, Fig 3's caption and Methods cite S18 Table; the SI list's entry does not name it. The entry for S3 Text names none of that text's four new subsections (the pre-injection gap and the three readings; the replaced volumes; the residual table moved from Results 4; the generators' per-subject slopes), and the entry for S5 Text does not name the paragraph on the deviations, to which Methods now sends the reader (S5 Text §1).
Evidence: draft L397, L401, L437, L261; supplementary.md L1339; S3_Text.md L187, L220, L317, L389; S5_Text.md L9.

### T29 — minor
Where: `manuscript/draft_v2.md` L15 (Abstract) against L25, L152, L158 and Table 4 (L164–168).
Text: "Under the common-change-in-surprisal (CCS) redundancy function the atom is near zero and nearly flat in r₁; prewhitening lowers but does not remove the contrast, leaving mostly stop-band residue."
Problem: Four clauses of the Abstract say more than the Results they rest on. (i) "nearly flat in r₁": Results 6 states this for the symmetric family; for the data it states a relation that is "weak and, where estimated, negative". The committed Abstract had "on the family", which the revision drops. (ii) "leaving mostly stop-band residue" holds at p = 10 and 20 (51.2 % and 59.7 % of the power above the band) and not at the two lower orders (0.3 % and 33.8 %); Results 7 keeps the distinction ("the orders that remove r₁ leave mostly stop-band residue"). (iii) "does not remove the contrast": at p ≤ 5 the contrast's interval includes zero (−0.0262 [−0.0636, +0.0107], p = 0.1406, negative in 8 of 14); the same holds of "No order removes the contrast" (L158) and "removed the contrast at no order" (L197). (iv) The first sentence, that MMI "underlies the fMRI synergy reports we found", is wider than the Introduction's count: of the ten studies eight state MMI, one uses CCS in its primary analysis and one does not state its redundancy function.
Evidence: draft L15, L25, L152 ("On the symmetric AR(1) family at fixed q it is nearly flat in r₁"), L158, L164–168, L191, L197; supplementary.md L260 (negative in 8 of 14); the committed Abstract (`git show HEAD:manuscript/draft_v2.md` L15).

### T30 — minor
Where: `manuscript/draft_v2.md` L253 (Methods, Literature search).
Text: "which returned 11 records: six of the nine, four outside the scope and one study added (Gao et al., 2026)"
Problem: The four are the records that the screening marks "outside the criterion", the criterion being an empirical fMRI ΦID study: two O-information studies, a partial entropy decomposition and a software library. The same paragraph defines "the scope" as something else (Gaussian-MMI ΦID synergy on BOLD without HRF deconvolution at TR ≈ 1–3 s) and says that "studies outside it are listed and marked (S20 Table)"; the four are not in S20 Table.
Evidence: `notes/review_2026-10-01_cold_reads/pubmed_search/screening.md`, the four rows marked "outside the criterion" (PMID 33858199, 37467265, 40843113, 42113765); draft L253.

### T31 — minor
Where: `manuscript/si/S3_Text.md` L550, L554 and L544 (§9–§10): pointers to statements the main text no longer has.
Text: "gives +32.8 against +0.06, of which the Discussion quotes the first"
Problem: The revision takes ∂sts/∂r₁ = 32.8 out of the Discussion; no "32.8" is left in the main text. Likewise L554 says that the surrogate gradient's correlations "were small and, with one exception (the glycolytic index), not significant (main text, Discussion)", and the Discussion no longer mentions the exception or significance; and L544 says that a pre/post contrast within a run "is therefore exposed to the within-run variance change (main text, Results 7)", while the last sentence of the same paragraph records that this statement moved out of Results 7 on 1 October 2026.
Evidence: `grep -c` in manuscript/draft_v2.md: "32.8" 0, "glycolytic" 0, "one exception" 0, "variance change" 0. S3_Text.md L544 ("(this sentence moved from the main text's Results 7 on 1 October 2026)"), L550, L554.

### T32 — minor
Where: `manuscript/si/S3_Text.md` L3.
Text: "The computations are numbered as their scripts in `notes/` are (B1–B26, B16b, B17b)"
Problem: S3 Text now reports B27, B28, B29 and B16c, each under its label (L187, L220, L389, L525). S19 Table's head note was brought up to date ("Labels B1–B29, B16b, B16c and B17b"); this one was not.
Evidence: S3_Text.md L3, L187, L220, L389, L525; supplementary.md L1601.

### T33 — minor
Where: `manuscript/si/S3_Text.md` L391 (§6, B28) against L404 (§7), S10 Table's source note (`manuscript/supplementary.md` L192) and `manuscript/draft_v2.md` L245.
Text: "B17's AR(1) generator (a_x, a_y ~ N(0.85, 0.0125), q from the data's window-level pair q)"
Problem: 0.0125 is the standard deviation of the coefficients. The other three places write the distribution as N(0.85, 0.0125²); the new paragraph copies the result file's header, in which the second argument is the standard deviation.
Evidence: `notes/partB17_calibration.py` L141 and L145 (`rng.normal(0.85, 0.0125, N_PAIRS)`); S3_Text.md L404 and supplementary.md L192: "a_x, a_y ~ N(0.85, 0.0125²)"; draft L245.

### T34 — minor
Where: `manuscript/si/S3_Text.md` L222 (§5, B29).
Text: "Per subject, run and 60-TR window: the number of TRs above the threshold, their mean framewise displacement and the window's whole-brain r₁"
Problem: The mean framewise displacement of the tables is that of all the TRs of the run or window, not of the TRs above the threshold, as "their" says: subject 3 has no TR above the threshold on either run and a mean of 0.068 and 0.094. L257 says it correctly (the mean-FD DiD is Table 2's FD DiD).
Evidence: `notes/review_results/partB/censoring_tables.md`, table (a), row 3: "0 (0.000), 0.068 | 0 (0.000), 0.094"; `notes/partB29_censoring.py` L77, L85; S3_Text.md L230, L257.

### T35 — minor
Where: `manuscript/si/S3_Text.md` L546 (§9), a sentence reworded by this revision.
Text: "As the plan anticipated, r_τ falls with τ and the sts level and contrast shrink with it."
Problem: The contrast shrinks at every step. The level does not: it is 0.0262 at τ = 3 and 0.0415 at τ = 5, where r_τ has fallen further, to −0.202. The main text says that the level follows |r_τ|.
Evidence: draft L146 ("the sts level follows |r_τ| (1.1554, 0.1797, 0.0262, 0.0415)"); S14 Table (supplementary.md L365–374). The committed sentence ended "and the artefact weakens."

### T36 — minor
Where: `manuscript/si/S5_Text.md` L25 (§4, the run of 1 October 2026).
Text: "no tracebacks; every output carrying `git=13e7299`; committed as 8bd189e by `b27_commit.sh`, which checked the 29 outputs' sha256 against the run's evidence"
Problem: Of the 29 outputs the twelve text files (tables, CSV files and logs) carry the commit; the sixteen `.npy` arrays and the `.pkl` file cannot. The record and the review folder's README say it exactly.
Evidence: `git show --stat HEAD`: 29 files under `notes/review_results/`, of which 12 have "git=13e7299" in their first lines. analysis_record.md L8889–8890: "each table, CSV and log with `git=13e7299`"; `notes/review_2026-10-01_cold_reads/README.md`: "the twelve text files among them with the commit of the run in their headers".

### T37 — minor
Where: `manuscript/si/S5_Text.md` L29 (§5) and L33 (§6).
Text: "On 1 October 2026 a correction of Table 3's caption, which changes no number, was audited by a separate session before its commit"
Problem: The table whose caption was corrected has left the main text: it is now "the residual table" of S3 Text §6, and Table 3 of the main text is the matched-slope table. Outside the quoted title of the record's entry, "Table 3's caption" (here and in §6: "71cf932 (1 Oct, the correction of Table 3's caption)") now names the wrong table.
Evidence: S5_Text.md L29, L33; S3_Text.md L317 ("The residual table (moved from the main text's Results 4 on 1 October 2026)"); draft L126.

### T38 — minor
Where: `manuscript/draft_v2.md` L261 (Methods, Pre-registration and deviations) and L201 (Limitations); `manuscript/si/S5_Text.md` L9 (§1); S19 Table (`manuscript/supplementary.md` L1599–1707).
Text: "The deviations from the pre-specification (eight, from the interval method to a reading of the residual's direction since withdrawn) are listed with what replaced each in S5 Text §1 and S19 Table."
Problem: (i) S5 Text §1 gives a replacement for three of the eight (the interval; the second null, "now a stationarity check"; the branch rule), says "withdrawn" of two and names no replacement for three (the split-half rule, the three failed predictions, the quotation of the first calibration's coupling rows). (ii) S19 Table has no row for the second null, the weighting rule or the withdrawn reading, and it gives outcomes, not replacements; Limitations cites "(S19 Table)" after the clause on the withdrawn reading. (iii) S5 Text §1's heading says that in Methods the deviations "are now named without their replacements"; Methods names the first and the last of them only. (iv) Five cells of S19 Table's "reported at" column still send the reader to "Methods, Pre-registration and deviations" for items that paragraph no longer states (the rows of B4, B7, B17 (ii), B17b (i) and B17b (ii)).
Evidence: draft L261, L201; S5_Text.md L9; supplementary.md L1599–1707 has no occurrence of "weighting", "stationarity", "phase-randomised" or "withdrawn"; L1619, L1621, L1632, L1642, L1643.

### T39 — minor
Where: `manuscript/draft_v2.md` L160 (Table 4's caption) against the table's rows (L164–165).
Text: "r: the per-subject correlation of the sts DiD with the whitened series' r₁ DiD (S11 Table; S3 Text §8)"
Problem: The AR(1) row's correlation, +0.899, is in neither S11 Table nor S3 Text §8, nor elsewhere in the supporting information; it stands in the result file alone. And the first row is the raw series, whose r₁ and r the caption's two definitions ("the whitened series' …") do not cover.
Evidence: `notes/review_results/partB/prewhiten_tables.md` L130: "per subject r(MMI sts DiD, whitened autocorrelation DiD) = +0.899"; main_text_numbers.csv L1052 cites that line; "0.899" does not occur as this correlation in S3_Text.md or supplementary.md (S11 Table's note, L331, gives +0.445, +0.333 and +0.495).

### T40 — minor
Where: `manuscript/draft_v2.md` L187 (Discussion, "The fall of r₁ under DMT").
Text: "per-subject Spearman ρ over 28 bins −0.24 [−0.40, −0.08], one-sided p = 0.002 against a phase-randomised null; nothing on the placebo run"
Problem: (i) The interval is a subject-bootstrap percentile interval (no per-subject vector is saved). Methods gives the inverted sign-flip interval as the interval of every mean over subjects, and the main text marks its other percentile intervals as such (Results 3); this one is not marked. (ii) "nothing on the placebo run" is the primary variant's result (−0.047 [−0.138, +0.039], one-sided p = 0.22). On the sensitivity variant the placebo run gives −0.093 [−0.180, −0.008], one-sided p = 0.045.
Evidence: supplementary.md L115 (S6 Table's source note: "group mean with subject-bootstrap percentile CI (no per-subject vector is saved)"), L119–120, L123–124; S1_Text.md L17 ("(percentile)"); draft L237.

### T41 — minor
Where: `manuscript/draft_v2.md` L201 (Limitations) with L187 (Discussion); the record's disposition of C's M3 (L9217–9221).
Text: "Why r₁ fell is not identified (Discussion); the account needs only that it did."
Problem: The committed sentence listed the candidates: "Why r₁ fell (neural, haemodynamic, cardiac, respiratory or motion effects) is not identified". The subsection it now points to names the neural, the cardiovascular (blood pressure and heart rate) and the motion routes. The respiratory and the haemodynamic candidates are in neither place and not in the supporting information, and C's M3 (iii) had asked for the "cardiovascular/respiratory effects" with a citation. The disposition ("the cardiovascular and motion candidates") describes the text as it is.
Evidence: `git show HEAD:manuscript/draft_v2.md` L180; draft L187, L201; "respirat" does not occur in draft_v2.md, S1_Text.md, S3_Text.md, S5_Text.md or supplementary.md; `reviews/read_C.md` L23.

### T42 — minor
Where: `manuscript/draft_v2.md` L197 (Discussion, Recommendations); B16c's rule (ii) (`manuscript/analysis_record.md` L8868, L9096) and the record's disposition of A's m4 (L9148).
Text: "whiten before band-pass filtering, or report the in-band power share beside any prewhitened atom"
Problem: The rule and the disposition say that the recommendation names "whitening before the band-pass or no band-pass". The Recommendations paragraph names the first and, in the place of the second, the in-band power share. "or no band-pass" is in Results 7 only.
Evidence: analysis_record.md L8868 ("recommendation names the remedy the released derivatives cannot test, whitening before the band-pass or no band-pass"), L9096, L9148; draft L158, L197.

### T43 — minor
Where: `manuscript/si/S1_Text.md` L5.
Text: "(record, "Git history and the participant codes", 15 September 2026, which states what the repository holds and the question put to the data authors)"
Problem: The entry named states what the repository holds and why its history is not rewritten. It states no question put to the data authors. The question (whether the letters identify anyone) is in the record's entries of 1 October 2026 and of this revision.
Evidence: analysis_record.md L2766–2774; L8556 and L9213.

### T44 — minor
Where: The record's disposition of C's m19 (`manuscript/analysis_record.md` L9255); `CLAUDE.md` L19.
Text: "m19 (the Abstract's length): 300 words (the check's output)."
Problem: The check's output is 299 words, as the same entry says 23 lines below. CLAUDE.md's state paragraph also has "abstract 300 words".
Evidence: `python3 notes/review_2026-10-01_cold_reads/checks/abstract_summary.py manuscript/draft_v2.md` prints "abstract 299 words (limit 300); author summary 200 words (limit 200)", which is the bundle's `checks/abstract_summary_revision.out`; analysis_record.md L9278.

### T45 — minor
Where: The record's disposition of C's M5 (b) (`manuscript/analysis_record.md` L9226) against S20 Table (`manuscript/supplementary.md` L1716–1727).
Text: "(b) the eight observations removed from S20 Table and the literature file"
Problem: C's M5 (b) lists seven observations, and seven are removed (in rows 1, 2, 3, 4, 6, 8 and the last). In rows 2 and 3 the remark is removed and the two unequal counts it was about stay side by side in the cell ("Results: 21 DoC patients … Methods: 22 included"; "N = 15 (pp. 4, 8; "n=16 for analysis", p. 15)"). Row 5's preprocessing cell now says that the Supplementary Methods were not read (C's M4); its last cell still says without that qualification "HRF deconvolution is not mentioned."
Evidence: `reviews/read_C.md` L30; a word-by-word comparison of S20 Table's rows with `git show HEAD:manuscript/supplementary.md`; supplementary.md L1717, L1718, L1720.

### T46 — minor
Where: `manuscript/main_text_numbers.csv`: the head note and the rows named. None of these changes a number of the text.
Text: "the six figure captions and the three table captions and bodies"
Problem: (i) The head note says three tables; the main text has four. (ii) L982 is a second row for 0.0112 in Results 6, paragraph 2 (note "inv_hi"); the text has the number once, and L981 is its row. (iii) No row for: the second "0.05" of Methods, Inference ("p > 0.05" and "p ≤ 0.05" have one row between them); the second "1" of Methods, Remedies ("1–5" and "fixed at 1"); "15–16" (the pages of Cliff et al., Results 7); "2–6" (Table 3's caption). (iv) Notes that do not agree with their source line: L780 "(two-sided 0.05, 12 df)", where the source has "one-sample t, 13 df"; L158 "B23 (a2)", where the anchor's row is "(a3) coupled family"; L677 "(regional_partial_tables.md)", for a spin p that B22 (e) computed. (v) Anchors that are not on the line named: L34, L35 and L775–777 (the lines hold 0.1075, 0.2183 and 0.2507; the anchors have 0.1079, 0.2188 and 0.2506), L631–634, L787–789 and L1120 (the line holds −0.7533; the anchor has −0.7535). (vi) L1115 holds "0.0028" for the Discussion's 0.003; on that line 0.0028 is the SD of the sts DiD, the residual DiD being +0.0027. (vii) 33 rows place N = 14 at line 2 of `results/primary_b_ts_gsr_win60.csv`, the line of column names, which does not hold 14.
Evidence: The rows named; `notes/review_results/partB/inference_revision_tables.md` L234–236 and L243; `calibration_filtered_tables.md` L8; `baseline_gap_tables.md` L43; `diagnostic_alternatives_tables.md` L30; S3_Text.md L157. Every locator of the table was tested for (v) (1,042 rows with a line locator).

### T47 — minor
Where: The record's disposition of B's MINOR 9 (`manuscript/analysis_record.md` L9201–9202) against `manuscript/draft_v2.md` L237 (Methods, Inference).
Text: "MINOR 9 (the OLS and Fieller assumptions and Fieller's g): Methods (Inference) states both and g"
Problem: Methods states the assumption of the t intervals ("which assume normal residuals of constant variance") and, of Fieller's interval, g and when the interval is finite; it states no assumption of that interval. The finding's last clause, that "no leave-one-out is given for either slope", is answered for the residual's slope (Table 3) and not for the sts slope of Results 2 (4.26 per unit); the disposition does not say that this part is left.
Evidence: draft L237; `reviews/read_B.md` L47; S3_Text.md L216 gives the leave-one-out of r(sts DiD, r₁ DiD), not of the slope.

### T48 — minor
Where: The record's disposition of C's m2 (`manuscript/analysis_record.md` L9232–9234) against `manuscript/draft_v2.md` L213 and `manuscript/si/S4_Text.md` L41 (P8).
Text: "m2 (the non-finite TR's place): Methods, S1 Text, S3 Text §5 and S4 Text P8: the last TR of subject 3's placebo run, at the end of window 14."
Problem: S1 Text and S3 Text §5 say so. Methods and S4 Text P8 say only "the last of one placebo run": neither names the subject or the window.
Evidence: draft L213; S4_Text.md L41; S1_Text.md L5; S3_Text.md L255.

### T49 — minor
Where: `manuscript/draft_v2.md` L158 (Results 7); `manuscript/si/S3_Text.md` L538.
Text: "tracking the whitened series' own r₁ DiD (−0.0927) at r = +0.333"
Problem: The paragraph says that the contrast "still tracks" the whitened r₁ at r = +0.495 and is "tracking" it at r = +0.333. At N = 14 the Fisher-z intervals of both correlations include zero ([−0.05, +0.81] and [−0.24, +0.73]); Methods gives correlations across subjects Fisher-z intervals, and Results 6 says of CCS correlations of the same size that each interval includes zero. At p = 20 the other three variant × estimator cells give +0.081, +0.157 and −0.079.
Evidence: Fisher-z intervals computed as Methods and B21 (d) define them (tanh(atanh r ± 1.959964/√11)). The other cells: analysis_record.md L9070–9076; S3_Text.md L533–536. draft L152 ("each Fisher-z interval including zero at N = 14"), L237.

### T50 — minor
Where: `manuscript/si/S4_Text.md` L16 (D8) against `manuscript/draft_v2.md` L213 (Methods, Dataset).
Text: "Methods, Dataset: one DMT run and one placebo run per subject, on two testing days two weeks apart, in counterbalanced order, half the participants receiving placebo first"
Problem: The Dataset paragraph of Methods states the two runs per subject. It does not state the two testing days, their spacing, the counterbalanced order, the half that received placebo first or the blinding, which the cell places there; these are in S1 Text, and Limitations has the counterbalancing in a clause.
Evidence: draft L213, L201; S1_Text.md L5.

### T51 — minor
Where: `manuscript/draft_v2.md` L27 (Introduction), L114 (Results 3) and L193 (Discussion): clauses the condensation removes that are neither in the supporting information nor reworded in place. The reason given with replacement I02 says "no statement removed".
Text: "hence positive MMI synergy, since MMI redundancy is non-negative"
Problem: (i) Introduction: the committed text's reason for "hence positive MMI synergy" (quoted) is removed, and so is the scope "of multivariate autoregressive processes" of Barrett's single-target lagged PIDs; neither is elsewhere in the manuscript files. (ii) Results 3: "in macaque single units, from sensory to prefrontal cortex, Murray et al., 2014" loses "from sensory to prefrontal cortex", so that the sentence's "from sensorimotor to association cortex" now reads on that work too. (iii) Discussion: "the six macroscale maps of their Table 1" and "one significant" are removed, both of which S3 Text §10 and S20 Table's row 1 keep; in the main text "those macroscale associations" is left without an antecedent, and the verdict "argue against it" stands without the one significant association of the surrogate gradient (ρ = 0.26, spin p = 0.028).
Evidence: `git show HEAD:manuscript/draft_v2.md` L27, L108, L172 against draft L27, L114, L193. "multivariate autoregressive" and "prefrontal" do not occur in draft_v2.md, si/S1–S5_Text.md or supplementary.md, and "non-negative" occurs there once, in another sense (S3_Text.md L110). S3_Text.md L552; the replacements file, I02, "why".

### T52 — minor
Where: `manuscript/draft_v2.md` L353 (References).
Text: "Rosas, F. E., Mediano, P. A. M., Jensen, H. J., Seth, A. K., Barrett, A. B., Carhart-Harris, R. L., & Bor, D. (2020)."
Problem: Of the 48 works of the reference list this one, added by the revision, is cited nowhere in the main text. It is cited in S3 Text §11 and in S20 Table's row 2, which give no reference of their own. The other works that only the supporting information cites are given there in full (the COBIDAS commentary in S4 Text, for one).
Evidence: Each entry of the list (L293–L387) was searched for by first author and year in the text above the list. S3_Text.md L558; supplementary.md L1717; S4_Text.md L3.

### T53 — note
Where: The commission, step 4; `notes/review_2026-09-25/revision/apply_replacements.py`.
Text: "all 188 entries applied; files written:"
Problem: Step 4's first command ends in `| tail -1` and is said to print "all 188 entries applied". It prints the last of the fifteen lines that follow that one, the sha256 and name of `scripts/15_figures_v2.py`, because the script lists the files it wrote after its summary line. I did not take this for a failed step: the script ended with status 0 and no mismatch, the second command printed 15, and the whole output is byte for byte the bundle's `checks/apply_revision.out`. I reported it at the time and went on.
Evidence: The output's last sixteen lines; `cmp` of the output with `notes/review_2026-10-01_cold_reads/checks/apply_revision.out`.

### T54 — note
Where: `manuscript/si/S5_Text.md` L29 (§5).
Text: "the revision that answers them was audited by separate sessions before it was committed (`notes/review_2026-10-01_cold_reads/audit/`; @@AUDIT_TEXT@@)"
Problem: A placeholder stands in a manuscript file of the prepared commit. The commission names the record's five «ENTRY_TIME» as left for the writer's session and does not name this one, which the replacements put in. I take it to wait for the audits' outcome; what replaces it could not be checked here, and none of the bundle's checks looks for it.
Evidence: `grep -rn "@@" manuscript/`: this one occurrence; the replacements file holds it in the new text of S5 Text's §5.

### T55 — note
Where: The record's dispositions of B's MINOR 1 (`manuscript/analysis_record.md` L9185–9187), C's M2 (L9214–9217), B's W1 (L9204–9205), A's M1 (L9135–9138) and A's m10 (L9159–9162).
Text: "MINOR 1 (the sensitivity of the "not distinguished" tests): B27: the residual DiD's SE, the minimal detectable difference (0.0155 nats) and the three excesses, in the Abstract, Results 4 and the Discussion."
Problem: Five dispositions say a little more than the text has, or leave a part of their finding without an answer and without saying so. (i) B's MINOR 1: the SE (0.0051) and the three excesses are in Results 4 only; the Abstract and the Discussion give the excesses as a range (0.006–0.009) and the detectable difference as 0.016. The sensitivity is that of a one-sample t test on 13 df, as S3 Text §5 says; Results 4 gives it to "the test", whose p values are sign-flip p values. (ii) C's M2: "the Use of AI tools statement is unchanged until a person has checked the analysis". Its content is unchanged; the revision rewords its third and fourth sentences into one. (iii) B's W1: Results 3 has "p < 1/10,000"; S3 Text §4 (L130) and S5 Table's note (supplementary.md L101) keep "spin p < 0.0001" for the same test. (iv) A's M1 (b) asked for a control that is non-stationary within a window in r₁ "and variance", or a semi-synthetic one; B28's ramp answers it for r₁, and the rest is neither taken up nor declined. (v) A's m10 ends with a point it calls "worth one sentence" (the TDMI residual DiD, +0.0092, beside the sts residual DiD, +0.0115); the disposition, which answers the transfer entropies and the three citations, does not mention it.
Evidence: draft L15, L124, L183, L257 against `git show HEAD:manuscript/draft_v2.md` (Use of AI tools); S3_Text.md L216 ("the one-sample t test (13 df)"), L130; supplementary.md L101; `reviews/read_A.md` L20, L44.

### T56 — note
Where: The record's dispositions of A's M2 (`manuscript/analysis_record.md` L9138–9139), B's MINOR 7 (L9196–9198), C's M1 and M2 (L9211–9217) and C's m17 (L9253–9254); S20 Table, rows 5 and 10 (`manuscript/supplementary.md` L1720, L1725); `CLAUDE.md`, "Remaining work".
Text: "the invitation to reproduce Table 2 is in the note to C.T. and S.P.S. (C's M2)"
Problem: Several dispositions rest on a note to the two co-authors and speak of it as existing ("is in the note", "the data authors are asked for it in the note that accompanies the draft", "asks S.P.S. for the CRediT line"). No such note is in the repository or the bundle. CLAUDE.md lists it under the remaining work and gives it fewer items than the dispositions do: it has the session order, the censoring, the licence field, the subject codes and the reproduction of Table 2, and not the CRediT line, the reproduction of Table 1, of the closed-form identities and of the regional correlation, or the two supplements. Two cells of S20 Table carry the same promise into a manuscript file: row 5 ("the study's co-author S.P.S. is asked with the draft") and row 10 ("V.S. is asked for them with the draft").
Evidence: analysis_record.md at the lines named; CLAUDE.md, the last bullet of "Current state"; supplementary.md L1720, L1725; `grep -rl "note to C.T."` finds the record, CLAUDE.md and three files of earlier review folders.

### T57 — note
Where: S19 Table, Part B and the "reported at" column of Part A (`manuscript/supplementary.md` L1601, L1615, L1655, L1666–1668, L1670, L1691–1706).
Text: "Part B lists the post hoc computations the paper quotes other than the checks of the pipeline's reproduction"
Problem: (i) Part B has a row for the numbers derived on 24 September 2026 (`derived_r17.out`) and none for those derived for this revision (`derived_r24.out`), which the main text quotes: r² = 0.79 and the two SDs, 38 %, the fifth and the sixth that the residualisation removes, rtr's slope of 0.50. (ii) Four "reported at" cells of Part A do not name the place where the revision now reports the item: the EEG Lempel–Ziv prediction (L1615: "S1 Text; S6 Table"; now also the Discussion), B25 (a)–(c) (L1666–1668: "S3 Text §11"; now also Results 6) and B23 (a3) (L1655; now also Results 1); and B26's cell (L1670) still names Results 4, which no longer mentions the matrices that are not positive definite.
Evidence: supplementary.md L1706 (the row of `derived_r17.out`); `notes/review_2026-10-01_cold_reads/checks/derived_r24.out`, items 2–4; draft L57, L154, L187; the main text speaks of those matrices at L61 (Table 1's caption) and L245 (Methods) only.

### T58 — note
Where: `manuscript/draft_v2.md` L108 (Results 2), L124 (Results 4), L110 (Fig 3's caption) and L245 (Methods).
Text: "between the AR(1) pairs' 3.1 and the band-passed generator's 6.1 for the same fall (S13 Table)"
Problem: (i) "for the same fall" is true of the band-passed generator (a fall of 0.0154 in pair r₁ against the data's 0.0155). The AR(1) pairs' 3.1 is a rate taken at a fall of 0.0138. (ii) Results 4 and Fig 3's caption call the three rates −0.18, −0.39 and −0.37 ratios "of group means under one change applied to every simulated subject". The band-passed rate is that. The AR(1) rate is from 3,000 simulated pairs, a whole-run change against the unperturbed pairs, with no simulated subjects, and the null's is from a single simulation. (iii) Methods gives the AR(1) pairs' pair r₁ in 60-sample windows as 0.786 without the committed text's "at a = 0.85"; 0.786 is the value of S18 Table's simulation at a fixed a = 0.85, while the generator of the sentence draws its coefficients around 0.85.
Evidence: supplementary.md L363 (S13 Table's note: "−0.09441 for −0.01540", "−0.04240 for −0.01377"), L1439–1445 (S18 Table (b): "3000 pairs, … a = 0.85", "r₁ +0.78638", "residual change / Δr₁" −0.387); `git show HEAD:manuscript/draft_v2.md` L224.

### T59 — note
Where: `manuscript/draft_v2.md` L126 (Table 3's caption) and rows L131–139; L15 (Abstract); L237 (Methods).
Text: "the slopes without subject 8, without subject 14 and without both, the extreme r₁ changes, each with its t interval"
Problem: (i) The t intervals of rows 4–6, and those counted in rows 2–3, are on 11 and 10 degrees of freedom (13 and 12 subjects). The caption gives 12 df for the data row and Methods gives 12 df for slopes across subjects without exception. (ii) The ± of the generator rows is the SD with divisor 100 (the script's `np.std`); with divisor 99 the four slope SDs print as 0.092, 0.097, 0.088 and 0.095. Elsewhere in the revision the SDs over subjects are stated with divisor n − 1. (iii) The Abstract's "for the subjects' own r₁ changes" and Results 4's "is the data's" are the data's r₁ DiDs rescaled to a mean of −0.015 (the data's is −0.0146), with subject 8 held at −0.0375 on the band-passed generator in the place of −0.0657; Table 3's caption says both, Fig 3's caption neither.
Evidence: Recomputed from `notes/review_results/partB/baseline_gap.csv`: without subject 8, −0.785 [−1.361, −0.208] on 11 df ([−1.355, −0.214] on 12); without both, −0.667 [−1.561, +0.227] on 10 df. `notes/partB28_matched_slope.py` L244 (`SL.std()`); `notes/review_2026-10-01_cold_reads/checks/derived_r24.out`, item 2 ("ddof 1"); `matched_slope_tables.md` L4.

### T60 — note
Where: `manuscript/draft_v2.md` L35 (Results, the notation paragraph) with L120, L61, L15, L87, L114 and L217; S12 Table's source note (`manuscript/supplementary.md` L335).
Text: "replaced by their AR(1) values, a_y q and a_x q (Results 4; Methods)"
Problem: (i) The definition of the AR(1)-substituted estimate now stands in the Results' opening paragraph (C's m8). It points on to Results 4, and Results 4 points back to it ("(defined in the Results' opening paragraph; Methods)"); Table 1's caption and S12 Table's source note still send the reader to Results 4 for it. (ii) The definition uses a_x and a_y before the main text has introduced them: the paragraph speaks of "a pair's two lag-1 correlations", and Fig 2's caption is the first place to name them. (iii) "Global fit" is used in the Abstract, in Results 2 and in Results 3 and is explained in Methods (Estimator) only; the committed Introduction explained it ("whole-run ('global') fits"), in a sentence the revision removes.
Evidence: draft L35, L61 ("put into the AR(1) family (Results 4)"), L83, L120, L217; supplementary.md L335 ("(main text, Results 4)"); `git show HEAD:manuscript/draft_v2.md` L29.

### T61 — note
Where: `manuscript/si/S3_Text.md` L220–297 (§5) and L538 (§8); S19 Table (`manuscript/supplementary.md` L1617–1618); `manuscript/draft_v2.md` L187; the record's disposition of C's M3 (L9221).
Text: "The replaced volumes and the autocorrelation (B29)"
Problem: (i) The two new subsections of §5 are put in before the table of BCa intervals and the three paragraphs on CCS (L259–297), which are §5's own and now stand under the heading of the B29 subsection. (ii) L538 gives two levels of the whitened sts for the same order without saying that they differ in kind: 0.087 and 0.072 are DMT pre-injection levels, and "observed sts level 0.0861 … 0.0705" are means over both runs and all windows. (iii) Of the word "artefact" the disposition says that it "is reserved for nothing". The main text uses it once, to deny it ("the fall is not an artefact"); S19 Table's rows of B2 and B3 keep the plan's "the artefact" without quotation marks, where S3 Text L303 now quotes it as the plan's word.
Evidence: S3_Text.md L220, L259, L293–297, L299, L303; `notes/partB16c_prewhiten_fixed.py` L184 (`np.nanmean(R['obs'])`); supplementary.md L1617–1618; draft L187; analysis_record.md L9221.

### T62 — note
Where: `notes/review_results/partB/matched_slope.csv` (an output of 8bd189e) and `README.md` L43–44: outside the manuscript, met in checking it.
Text: "condition,replicate,slope,slope_lo,slope_hi,r,ratio_of_means,res_did,sts_did,a_did"
Problem: (i) The file's header has ten fields and each of its 400 rows eleven, the condition's name holding an unquoted comma ("(i) band-passed, step"). A CSV reader shifts every column by one unless the first two fields are joined again. The file is an output as the run wrote it; the line that writes it is in `notes/partB28_matched_slope.py`. (ii) README.md lists the computations that "have been run and their values are in the text" as far as B26, without B27, B28, B29 and B16c, in a paragraph the revision otherwise brings up to date.
Evidence: The file's first three lines; README.md L36–44.

### T63 — note
Where: `manuscript/draft_v2.md` L187 (Discussion, "The fall of r₁ under DMT"); S20 Table, row 10 (`manuscript/supplementary.md` L1725); `notes/review_2026-10-01_cold_reads/claims/claims_2026-10-01.md` L8–27, L44–58 and L60–65. Not checked against the papers; this overlaps the audit of the citations.
Text: "under DMT the EEG's signal diversity rises and its alpha power falls (Timmermann et al., 2019, 2023)"
Problem: The revision's claim record holds this statement for Timmermann et al. (2019) alone. Its entries for the 2023 paper are on the design, the exclusions, the preprocessing, framewise displacement, the acquisition and the participants. The sentence is new in this revision, so no earlier citation pass covers the 2023 citation for it. Likewise S20 Table's new row 10 (Gao et al., 2026) agrees with the claim record in every value the record holds and gives two details it does not hold: the patients' two subgroups ("23 HFrEF, 25 HFmrEF") and the matching of the controls for age, sex and education.
Evidence: claims_2026-10-01.md L8–27, L44–58, L60–65; neither "HFrEF" nor "education" occurs in the claim record.

## Checked and found exact

### The prepared commit and the mechanical checks

- The five steps of the commission: the commit and its subject line; the tarball's sha256; 16 files unpacked and 16
  untracked; the replacements applied all or none (188 entries, no mismatch, the output byte for byte the bundle's
  `checks/apply_revision.out`); 15 files changed; the record's numstat 418 and 0; its five «ENTRY_TIME» headings
  (L8875, L8957, L9010, L9051, L9100) left as they are.
- `check_numbers.py`: "rows 1302, data rows 768, flagged 11", byte for byte the bundle's
  `check_numbers_revision.out`. The eleven flagged rows are magnitudes whose sign the wording carries, and each
  wording has the right direction: 0.019 (twice) and 0.031 ("moves", with the derivative's sign beside it); "fell by
  0.0164"; "exceeds the observed level by 4.3 %", "by 1.1 %" and "by 0.049 nats"; "a fall of 0.012–0.015"; "to within
  0.053 nats". The eleventh, 0.83, is flagged through the hyphen of a range in its source ("0.680-0.830") and carries
  no sign.
- `check_cells.py`: "flagged 0". `tablecheck.py` on the main text, S1–S5 Text and the supplementary tables: "rows
  with a wrong cell count: 0". `wc.py`: "total with headings 8498 without 8371" (the limit 8,500).
  `abstract_summary.py`: 299 and 200 words (the limits 300 and 200). These are the bundle's outputs; they were run
  again here.
- `derived_r24.py`, run again with its output kept outside the clone: the output is `checks/derived_r24.out` but for
  the header line.

### The numbers of the changed text

- The numbers table: every row of a paragraph, caption or table that the revision changes was compared with the line
  its locator names, for the value at the printed precision, the sign, and the quantity, variant and estimator that
  the sentence gives it. No number of the main text differs from its source at the printed precision but those of
  T06, T07, T24 and T25, and none is given to the wrong quantity, variant or estimator but that of T01.
- Table 2: the six new rows on both variants (values, intervals, p values, counts) against table (a) of
  `baseline_gap_tables.md`, and recomputed from `baseline_gap.csv` with an inverted sign-flip interval and an exact p
  written apart from the repository's code. All agree. (From the CSV's six decimals the p of r₁'s pre-injection gap on
  ts_demean comes out as 0.1873 against the table's 0.1871, three sign assignments of 16,384, which the CSV's rounding
  can make.)
- Table 3: the six data rows recomputed from `baseline_gap.csv` (slope −0.7533 [−1.1331, −0.3735], r = −0.780; any
  one subject left out, −0.791 to −0.699, no interval of the 14 containing zero, r from −0.871 to −0.670; any two,
  −0.906 to −0.642, 1 interval of the 91, r from −0.930 to −0.465; without subject 8, without subject 14, without
  both). The four generator rows recomputed from `matched_slope.csv` (means, SDs, the central 95 %, the mean r, the
  residual DiD; no replicate at or below the data's slope, the steepest being −0.442, −0.488, −0.566 and −0.596).
- Table 4: its forty cells against S11 Table, `whitened_spectrum_tables.md`, `prewhiten_tables.md`,
  `prewhiten_fixed_tables.md` and `derived_r24.out`; the contrasts and correlations at p = 10 and 20 recomputed from
  the per-subject vectors of `inference_rows_prewhiten_fixed.pkl`.
- Results 2: the three readings with their intervals, p values and counts; r(DiD, pre-injection gap) = −0.888, r² =
  0.79, the SDs 0.0887 and 0.0485; the subject with the one positive DiD and the most negative gap (subject 14); the
  cross-half correlation, its interval at three decimals and its ceiling; the disattenuated interval and its 366
  excluded draws (the bootstrap repeated); 38 %; −0.844, +0.939 and +0.824; subject 8 (−0.064; 24 TRs against 23.6)
  and subject 14 (+0.024); the rates 5.5 and 5.2, the Fieller interval and g = 0.61; the slope 4.26 [3.41, 5.12] with
  its intercept; the fifth and the sixth that the residualisation removes (0.197, 0.163); 0.34 and 0.40.
- Results 4: the SE 0.0051 and the detectable difference 0.0155 (0.01550); the excesses 0.0088, 0.0066 and 0.0061;
  the p values 0.108, 0.218 and 0.251 (0.1075, 0.2183, 0.2507); −0.79 and its Fieller interval; the four cross-half
  correlations against `splithalf.log`.
- Results 1, 5, 6 and 7, the Discussion and Limitations, where the revision touches them: −1.74, 0.035 and +0.009;
  the thirteen atoms; the lag levels and contrasts against S14 Table; the CCS atom's range on the family (−0.01535 to
  −0.03637 over S18 Table's grid); the binarised rates (+1.8153, −0.1496, 1.76; +0.1244, +0.1415); cos(2π × 0.08 Hz ×
  2 s) = 0.54; the thirds, the fifth, 18 % and 7 % of Results 7; ∂C/∂r₁ = 0.056 against 6.07; rtr's slope 0.50 and "a
  sixth of sts's 3.09"; the replaced volumes (23.6 and 10.1 TRs, +1.12, p = 0.2166, 7 of 14, r = −0.107 and −0.124);
  the EEG Lempel–Ziv values against S6 Table.
- The Abstract and the Author summary against the Results: the DiD with its interval, p and count; −0.054; −0.094;
  0.69 and 0.95; 0.86; 0.0115; 0.006–0.009; 0.016; 0.11–0.25; "no replicate as steep"; "synergy rose in one
  volunteer, autocorrelation in two" (subject 14; subjects 5 and 14). The exceptions are T06 and T29.

### The supporting information and the condensation

- S3 Text's new subsections give their result files number for number: B27's tables (a) and (b) and its paragraph
  (c), B29's tables (a) and (b) and its paragraphs (c) to (e), B28's table, and the eight rows of B16c's table (these
  against the pickle and `derived_r24.out`). Their readings were checked sentence by sentence; what is not exact is
  in T08, T09, T33, T34 and T61.
- S11 Table's 24 new rows (MMI-sts, CCS-sts and the whitened r₁ in the eight cells of p = 10 and 20): levels,
  contrasts, intervals, p values and counts against the pickle and `derived_r24.out`; two of the inverted intervals
  recomputed independently.
- The former Table 3 is in S3 Text §6 with its caption unchanged but for the heading and its 13 rows identical.
- The eight moves that the record lists are each in the supporting information, with a sentence of the main text
  that points there: the former Table 3 and the aligned statistic's comparison (S3 Text §6, L317–339), the null's
  four-cell levels (§6, L305), Barrett's reduction and the joint-target nodes (§2, L106), the transfer entropies
  (§3, L124), the global fit's two exposures (§9, L544), the costs of prewhitening (§8, L540), the rank gradient's
  attenuation (§10, L554) and the itemised deviations (S5 Text §1, L9).
- The other sentences and clauses that the revision takes out of the main text were each looked for in the
  supporting information or in the sentence that replaces them. They are there, but for those of T17 (iii), T41 and
  T51.
- S19 Table's count recomputed from its rows: 67 = 36 met + 15 partly met + 16 missed + 0, with 14 rows not counted,
  as its note says; the eleven new predictions and their verdicts agree with S3 Text's readings and with the record's
  outcome entries.
- S20 Table against the Introduction's counts: ten studies; eight state MMI (rows 1, 3–8 and 10), five name a
  Gaussian estimator (rows 1, 3, 4, 5 and 10), one uses CCS on binarised signals (row 2), and the primary lag is
  stated in rows 2, 6 and 10. Row 10 (Gao et al.) against the claim record (T63).
- The PubMed search: 11 records, of which 6 are in S20 Table, 4 outside the criterion and 1 added; three of the nine
  not returned; 2 records in the second search.

### The dispositions

All 70 were read against the finding's text and against the revised text. Borne out as the record states them: of
A's 20, m1, m2, m3, m6, m7, m11 (declined, with its reason), m12, m13, m14, w1, w2 and w3; of B's 19, MAJOR 1, MAJOR
2, MAJOR 3, MINOR 2, 4, 5, 10 and 11, W2, W4 and W5; of C's 31, M4, M6, m1, m3, m4, m5, m6, m7, m8, m10, m11, m12,
m13, m14, m15, m16 and w1 to w6. Small inexactnesses in the passages that some of these point to are in T10, T15,
T17, T26, T29, T30, T45 and T61. The other 25 are the subject of a finding: of A, M1 and m10 (T55), M2 (T56), m4
(T42), m5 (T01), m8 (T13), m9 (T03, T07) and w4 (T20); of B, MINOR 1 (T55), 3 (T03, T18), 6 (T04), 7 (T56), 8 (T18)
and 9 (T47), W1 (T55) and W3 (T27); of C, M1 (T43, T56), M2 (T55, T56), M3 (T41, T61), M5 (T19, T45), m2 (T48), m9
(T11, T12), m17 (T56), m18 (T02) and m19 (T44).

### The rules of the text

- No computation label (B1 to B29, B16b, B16c, B17b) in the main text; the pattern occurs only in file names of Data
  and code availability.
- No process label in the main text: no round, stage or bundle, no session name, no reviewer's letter. The
  supporting files: T16.
- The six figure captions of the main text against the figure script: run in a copy of the tree, the script writes
  six captions each of which, without its Source sentence, is the main text's caption. Those of Figs 2 and 4 are also
  the committed ones; those of Figs 1, 3, 5 and 6 differ from the committed ones in exactly the strings that the
  script's diff changes (Fig 1's title; Fig 3's clause and its last sentence, with −0.200 and −0.355 as the script
  reads them from rows (i) and (iii) of `matched_slope_tables.md`; Fig 5's clause on the scale; Fig 6's "the
  r₁-dependence included").
- The script's diff makes the three drawing changes that the entry names, and the regenerated figures show them:
  Fig 1b's colour-bar label; Fig 3c's two thin lines, which pass through the data's centroid with slopes −0.200 and
  −0.355 while the three rates stay through the origin; Fig 5c's y-range and title, with the dashed step and its
  error bars now legible. What else the diff changes is in T12.
- The three quantities that Methods names are marked post hoc where the Results quote them (L106, L114, L146). The
  rest of that rule is T18.
- The word counts, as above: 8,498 with headings, 8,371 without; 299; 200.
