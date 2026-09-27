# Findings of checker A: the last error-only read (26 September 2026)

Scope: `manuscript/draft_v2.md` in full, `manuscript/figures/captions_v2.md`, the six figure PNGs, and each main-text quantity, citation and S-item pointer checked against the SI and the reference list. Classes: T text, N numbers, X cross-references, C contradictions, U uncertain. Line numbers are those of the repository files (c25a310 with the pending edits applied).

**Counts:** T 2, N 0, X 2, C 1, U 3 (8 in all). Three of them (T1, T2, X2) are outside this checker's part; they were found while cross-checking and are listed separately.

## 1. manuscript/draft_v2.md

### X1
- **Location:** draft_v2.md, line 332 (References, the Tarchi et al. 2026 entry).
- **Quote:** "(read in full on 20 September 2026; a deconvolving study, see S3 Text)"
- **Problem:** S3 Text never says that Tarchi et al. deconvolve. Its only mentions of the study are the list of nine studies in §10; its one deconvolution statement about a cited study concerns Luppi et al. 2022 (line 428). The statement is in S20 Table. The pointer dates from 20 September (958648f), before the applicability table moved to S20 Table.
- **Evidence:** supplementary.md line 1665 (S20 Table, row 9): "**HRF-deconvolved** with "standard SPM methods" (p. 3)"; line 1678 (Table B, item 4): "Tarchi et al. 2026 (row 9) names "standard SPM methods"". S3_Text.md has no "SPM". `git log -S` puts the phrase at 958648f.
- **Fix:** "(read in full on 20 September 2026; a deconvolving study, see S20 Table)". This is in the reference list, so the body word count is unchanged.

### C1
- **Location:** draft_v2.md, line 118 (Results 4, second paragraph), against line 224 (Methods, The AR(1)-substituted estimate and its calibration).
- **Quote:** "In simulations with a fall of 0.012–0.015 in pair r₁ applied to the DMT run only (Methods; Table 3; S10 Table)"
- **Problem:** The sentence puts all three expectations under "applied to the DMT run only", the third being "+0.0054 on a finite-sample null". The null is not a DMT-only change. Methods says it is "solved to its window-level pair r₁ and |q| in each run × period cell", and its placebo cells change too. Its DMT-run change alone is −0.0093, outside the stated 0.012–0.015. Table 3's caption keeps them apart: generators have "DMT run changed from sample 300"; row 5 is "a single simulation (Methods)".
- **Evidence:** notes/review_results/logs/review_v2_residual_null.log, lines 11–14: window a is 0.8625 (DMT pre), 0.8532 (DMT post), 0.8602 (PCB pre), 0.8655 (PCB post); line 16: "null residual change: DMT +0.0041, PCB -0.0013, DiD +0.0054". derived_r17.out, item 6: "(0.8532 - 0.8625) - (0.8655 - 0.8602) = -0.0146". S3_Text.md line 282: "β and q vary across pairs so that the window-level mean pair r₁ and |q| equal the four run × period cells".
- **Fix:** "In simulations with a fall of 0.012–0.015 in pair r₁ applied to the DMT run only on the two generators (Methods; Table 3; S10 Table)". Adds 4 words to the main text.

### U1
- **Location:** draft_v2.md, line 224 (Methods) and line 118 (Results 4).
- **Quote:** line 224: "so that it carries the data's fall of pair r₁ (its own DiD −0.0146)"; line 118: "+0.0054 on a finite-sample null that carries the data's fall of pair r₁ (Methods)"
- **Problem:** The data's fall of pair r₁ is −0.0155 (Results 2, Table 3 row 1, S13 Table). The null's own is −0.0146, 6 % smaller, because its solved DMT-pre cell is 0.8625 against the data's 0.8632. The paper treats a 6 % gap of this kind as worth stating elsewhere (Fig 3 caption: "the two DiDs differ by 6 % … (−0.0155 against −0.0146)"). The null's −0.0146 also equals the data's whole-brain r₁ DiD, which invites confusion. This is reported as uncertain because "carries" may be meant approximately.
- **Evidence:** residual_source.log line 10: "pair a: DMT pre +0.8632 post +0.8532; PCB pre +0.8603 post +0.8657; primary DiD -0.0155"; review_v2_residual_null.log lines 11–14 as in C1.
- **Fix (if confirmed):** line 224: "so that it nearly carries the data's fall of pair r₁ (its own DiD −0.0146, against −0.0155)" (+3 words); line 118: "that nearly carries the data's fall of pair r₁" (+1 word).

### U2
- **Location:** draft_v2.md, line 246 (Data and code availability).
- **Quote:** "The `notes/` outputs name the producing commit in their headers (`git=<SHA>`; `-dirty` where the tree had uncommitted changes; `nogit` for files written outside a commit; S5 Text lists both kinds)."
- **Problem:** No `notes/` output carries `-dirty`. All 14 `-dirty` files that S5 Text lists are under `results/`, as is one of the five `nogit` files. The `results/` files carry the same headers: S5 §4 says "Every result file names the commit". So the sentence restricts the convention to the `notes/` outputs, then points to a list of mostly `results/` files. Reported as uncertain because the sentence may only be describing the convention.
- **Evidence:** `grep -rl -- '-dirty' notes/review_results` gives 0 files; `results/` gives 14. 57 `results/` files and 80 `notes/review_results/` files carry `git=` headers. S5_Text.md line 23 lists the -dirty and nogit files.
- **Fix (if confirmed):** "The result files name the producing commit in their headers (…; S5 Text lists both kinds)." Removes 1 word from Data and code availability, which is outside the body word count.

## 2. manuscript/figures/captions_v2.md

No finding. The six caption strings (lines 7, 11, 15, 19, 23 and 27, without their closing Source sentence) are identical, character for character, to the paper's captions (lines 55, 83, 104, 110, 116 and 142). Every file named in the Source sentences exists. The header ("at git b02d5ba") matches c25a310's commit message.

## 3. The six figures

### U3
- **Location:** figure annotations in fig2_v2_atoms_observed_substituted.png (panel a), fig4_v2_regional.png (panel c) and fig6_v2_lag_dependence.png (panel a), against their captions (draft_v2.md lines 83, 110 and 142, and the same strings in captions_v2.md).
- **Quote (figures):** Fig 2a: "observed −0.084, AR(1)-substituted −0.100". Fig 4c: "eight-class F = 8.15, spin p = 0.0009", "(unpartialled map: F = 16.93, spin p = 0.0564)", "SomMot − Default −0.00965, spin p = 0.22", "Vis − Default +0.00875, spin p = 0.31". Fig 6a: "+0.95, +0.97, +0.63, −0.83 (τ = 1, 2, 3, 5)".
- **Quote (captions):** line 83: "(−0.0844) and in the substituted atoms (−0.1003)"; line 110: "the eight-class one-way F is 8.146, spin p 0.0009, against 16.933, spin p 0.0564, for the unpartialled map; the residual map's somatomotor − default and visual − default contrasts are −0.00965 (spin p 0.2240) and +0.00875 (0.3089)"; line 142: "(+0.953, +0.970, +0.626, −0.832)"
- **Problem:** The values agree, but each figure prints them at lower precision than its own caption, without a stated reason. The brief asks for the same precision everywhere. The previous revision already aligned Fig 4c's two contrasts with the caption (N4) but left F and the spin p values. Reported as uncertain: it may be an accepted convention for figure annotations.
- **Evidence:** aligned_directed_tables.md lines 60–61 (8.146, 16.933, 0.2240, 0.3089); lag_tables.md / S14 Table (+0.953 … −0.832); family_atoms_tables.md line 29 (−0.0844, −0.1003).
- **Fix (if wanted):** print the captions' precision in `scripts/15_figures_v2.py` and re-render, or round the caption values to the figures' precision. No change to the text's word count.

Otherwise no error in the figures. Checked: panel letters, titles, axis labels, legends and every printed value against the captions and sources. That covers:
- Fig 1: contours 0.25/0.5 labelled inline; the operating point; the four panel-c curves and their styles against `coupling_map_tables.md` (1.2588, 1.2315, 1.2155, 1.2569, 1.3023, 1.4111).
- Fig 2: colours, groupings, whiskers.
- Fig 3: r, intervals, slopes, generator rates.
- Fig 4: parcel counts 17/14/14/12/5/13/24/16, the bar values, the minus signs.
- Fig 5: the y-range; equal nats per unit height, estimated in pixels; the band, hatch, injection line and the +0.0027 ± 0.0014 step.
- Fig 6: points, whiskers, the r_τ labels.

## 4. Found outside this checker's part while cross-checking (S5 Text, supplementary.md, S3 Text)

### T1 (process label)
- **Location:** si/S5_Text.md, line 27 (§5).
- **Quote:** "the record's entries call them the writer's session and the planning session, and here each review is named by its date"
- **Problem:** The brief lists "writer", "planner" and "session" as process labels that no manuscript file may carry. This sentence introduces two of them.
- **Fix:** "The drafts were revised by one session of the AI system and checked by others; here each review is named by its date." That is, delete "the record's entries call them the writer's session and the planning session, and".

### T2 (process labels in quoted record titles)
- **Location:** si/S5_Text.md line 19 (§3), line 27 (§5, three times); supplementary.md line 339 (S13 Table note).
- **Quote:** S5 line 19: 'Finding 9; record, "Stage B of round 16: the shortened text", 23 September 2026); the paper reports both estimators'. S5 line 27: '(record, "Round 14: the restructuring")', '(record, "Stage B of round 16: the shortened text", 23 September 2026)', '(record, "Round 17: the review of 24 September 2026 applied")'. supplementary.md line 339: '(record, "Stage B of round 16: the shortened text", 23 September 2026)'.
- **Problem:** "Round" and "Stage" are process labels under the brief. The headings exist in analysis_record.md (lines 5297, 6571, 6733). The verification of 25 September (T5, V49) kept them as verbatim titles, which conflicts with this brief's rule.
- **Fix (if the rule applies to quoted titles):** cite the entries by date and time: "record, the entry of 21 September 2026, 15:12 UTC"; "record, the entry of 23 September 2026, 21:40 UTC"; "record, the entry of 25 September 2026, 16:34 UTC".

### X2
- **Location:** si/S3_Text.md, line 124 (§4, end of paragraph).
- **Quote:** "Under CCS the same correlations are −0.011 and −0.018 (main text, Results 6)."
- **Problem:** Results 6 (draft_v2.md line 146) gives only −0.011 (DMT window 6), not −0.018.
- **Evidence:** −0.018 is in ccs_pub_tables.md line 34 (subject 1, PCB window 2); −0.011 is in line 33.
- **Fix:** "Under CCS the same correlations are −0.011 and −0.018 (`ccs_pub_tables.md`; the first in main text, Results 6)."

## Coverage

**Read in full:**
- draft_v2.md, every line from the title to the Supporting-information captions: the reading copy, plus the raw lines of every paragraph for word-level reading. This includes Tables 1–3, the six captions, the statements, the References and the pending sentences, which were checked for wording, grammar and cross-references only.
- captions_v2.md and the six PNGs.
- S1, S2, S3 and S5 Text, for cross-checking.
- supplementary.md: S1, S5, S8, S10–S16, S18, S19 (Parts A and B) and S20 Table. S17 Table was parsed by program (932 rows).
- Not read in full: S4 Text (only its exclusion item and headings, since the main text cites it only as the COBIDAS checklist); the numbers of S2–S4, S6, S7 and S9 Table.

**Checked against files:**
- Table 1 cell by cell against family_atoms_tables.md (0 differences; the 16-atom sums agree within rounding).
- Every main-text mean with an interval against its S17 Table row: mean, inverted interval, exact p, negative/14 (all agree).
- Table 2's means, shares and phase p against inference_rows_raw.pkl.
- Table 3 against S18 Table and diagnostic_alternatives.csv, including the unrounded SEs and population values that sit on rounding ties (0.00065, 0.00055, 0.00095, −0.00815, −0.02245, +0.01385: all printed correctly).
- The regional statistics, recomputed from regional_partial.csv: slopes 3.089 and 0.498; r 0.863 and 0.638; the contrasts; the network means (Subcortex −0.023546, so −0.024 is correct).
- The CCS per-subject r recomputed from the pickles (−0.2748, so "−0.27" is correct); the 12.5 % median from inference_revision.csv.
- review_v2_residual_null.log, residual_source.log, diag_tables.md, derived_r17.out, splithalf.log, overlay_points_run.log, coupling_map_tables.md, aligned_directed_tables.md (e), the phiid_fast_validate logs, requirements.lock.txt (phyid hash), rev_phiid_fast.py (function names), run_all.sh (figure step).
- The closed-form identities and ∂sts/∂a, ∂sts/∂q and ∂rtr/∂a at (0.85, 0.25), recomputed by hand.
- The S19 Part A tally: 25/13/14 of 52, plus 6 rule rows. The three failed calibration predictions: B17 (ii), B17b (i), B17b (ii).
- The main-text changes since ddae618, word-diffed; no error was introduced by them other than none found.

**Mechanical checks:**
- check_numbers.py and check_cells.py rerun on the current text: 12 known wording flags and 0 cell flags.
- A double-rounding scan of the numbers CSV (held strings ending in 5 at the rounding position). One candidate, verified correct from the unrounded value.

**Cross-reference classes checked exhaustively:**
- First-citation order of Figs 1–6 and Tables 1–3, and caption placement.
- Every S-item pointer in the main text: all 20 S Tables and 5 S Texts, including S3 Text §4, §5 and §6, each confirmed to hold what is claimed.
- Every author–year citation against the reference list, in both directions (41 entries, all cited, none missing; the entries are in alphabetical order).
- S Text titles and S Table headings against the SI captions.
- The main text quotes no record titles.
- No computation label, file path or process label in the main text outside Data and code availability; no "pair-level a"; no r1 or hyphen-minus in numbers.
- Every Markdown table has the right number of cells; brackets are balanced; abbreviations are expanded at first use; no doubled words.

**By sample only:** the SI's pointers into the main text (S3 Text throughout; S19 Table's "reported at" and "where quoted" columns).

**Not checked, and why:**
- Bibliographic details and quotations of external works: no web access.
- The figure PDFs: the brief names the PNGs.
- The placeholder values of the final run, as the brief instructs.

**Not reported:** precision differences where the running text rounds a value that the SI or a caption gives more precisely (for example 0.073 against 0.0729, the abstract's three-decimal values, 0.056 against 0.06). The values agree, and the running text rounds consistently. The figure-annotation cases are U3.
