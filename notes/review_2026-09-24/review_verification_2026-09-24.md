# Verification of the review and the citation check of 24 September 2026

This file is the planning session's check of two reports on the text at 66c6331 (bundle 27, the shortened text):
the adversarial review, `adversarial_review_2026-09-24.md`, and the citation check of the changed citing sentences,
`citation_pass_2026-09-24.md`. Both were written by separate sessions of the same AI system (Claude). Neither had any
subject data. The check scripts are in `checks/`, with their paths made repository-relative:

- `chk_core.py` and `phiid_cf.py`, the review's own sign-flip enumeration and Gaussian-MMI ΦID;
- `extract.py`, the citation check's sentence extractor;
- `derived_r17.py` and its output `derived_r17.out`, the planning session's computation of the new derived numbers
  (git=66c6331, seed 20261120, committed result files only). These numbers are post hoc: they were computed in
  verifying the review, with no pre-run entry.

Each item gets one verdict:

- **Confirmed**: the facts are as the report says.
- **Partly**: some of the report's facts hold and some do not, or only part of the proposed fix is taken.
- **Judgement**: a matter of presentation, where the report's proposal is taken or modified as stated.
- **Declined**: the report is wrong, or its fix is not taken, with the reason.

The planning session re-derived every fact marked Confirmed below from committed files, unless the item names another
source. The disposition says what round 17 does.

## Checks of bundle 27 itself

- **The bundle.** Size and sha256 match the writer's report. It verifies against 90690f4 and carries the three
  commits 6f34e89, 526090d and 66c6331, with author vilalius and both trailers.
- **The record.** It only gains lines: five entries appended at 6319–6657.
- **Scope.** No file outside `manuscript/`, `scripts/`, `notes/`, `CLAUDE.md` and `README.md` changes. No data file is
  added, and the email address is not added anywhere.
- **The B21 script.** `notes/partB21_inference_revision.py` changes only in `cell()`, which now formats `float(v)`.
- **The figures.** `scripts/15_figures_v2.py` was re-run at 526090d in the pinned environment. All six PNGs are
  identical pixel for pixel to 66c6331's, and `captions_v2.md` is identical.
- **The prompt's quoted passages.** 65 of the 77 quoted passages of the Stage B commission appear verbatim. The other
  12 are instructions, deleted phrases, or passages adapted with the substance kept: the atom names added to the
  mirror-atom sentence; A22 moved into S3 §3; the spin parenthetical shortened. (The script that checked this reads
  the commission, which is not in the repository, so it is not in `checks/`.)
- **Two record points** (outcome entries of 23 Sep 2026 21:40 UTC):
  - **(i)** The B21 entry attributes the seven p differences to reading the committed p "from a four-decimal table".
    Their cause is different. B21 recomputes these rows from `ccs_decomposition.csv`, which partB18 wrote at six
    decimals; partB18's committed p came from full-precision values. The terms are of order 10⁻⁴–10⁻³, and six-decimal
    rounding moves assignments that lie near a tie.
  - **(ii)** The decision entry calls the section budgets "set with the decision". They were set in the Stage B
    commission; V.S.'s decision set the total (≤ 7,000 words), the abstract, the author summary and the counts of
    tables and figures.
  - Both points are corrected by a note in round 17's record entry.

## The adversarial review: major items

**M1 (the abstract and author summary). Confirmed; rewritten** (the prompt gives the text).

- **(a) The per-SD ratio.** 4.7 to 1 is the closed form's derivative ratio applied to within-window SDs. The windowed
  estimator's own ratio is 1.4 to 1 (B22 (d): 5.126 × 0.0284 against 0.528 × 0.1957). The abstract now gives both.
- **(b) "In close to the proportion…".** The phrase was not quantified. Like for like, the band-passed generator gives
  an sts DiD of −0.0944 for a fall of the pair r₁ of 0.0154 (B24). The data give −0.0809 for a fall of 0.0155
  (`residual_source.log`, pair a). The abstract states that comparison.
  - The per-subject slope, 4.26 [3.41, 5.12], lies below the generator's rate. Results 2 says so, with the attenuation
    note.
  - The ratio of group means, 5.52 per unit of regional r₁, has a Fieller interval of [4.45, 10.54] and a bootstrap
    interval of [4.56, 8.21] (`checks/derived_r17.out`, item 1; seed 20261120).
- **(c) Shared variance.** "Share their reliable variance" becomes "share most of their reliable variance
  (disattenuated r 0.95 [0.62, 0.99])".
  - Leverage: without subject 8 (the largest fall of r₁, −0.064), the mean cross-half r is 0.486 on ts_gsr, the
    ceiling 0.542 and the ratio 0.897. Without subject 14 (the largest rise, +0.024) they are 0.571, 0.621 and 0.921.
    Every other single omission gives a mean cross-half r of 0.68–0.83 and a ratio of 0.95–0.97; on ts_demean the
    ratio stays at 0.98–1.00 for every omission (`checks/derived_r17.out`, item 2).
  - Results 2 states subject 8's weight, and S3 Text gains the leave-one-out table (both variants).
- **(d) The residual.** It is stated neutrally, with the p range and the sizes: the estimate falls 0.011 more than
  observed, against 0.003–0.005 in the simulated pure autocorrelation changes (exact p 0.11–0.25).
- **(e) The family.** It is "two AR(1) processes correlated at lag 0, without lagged interaction", not a "bivariate
  AR(1) pair".
- **(f) The operating point.** "The operating point of fMRI region pairs" becomes "these data's operating point".
- **(g) The author summary.** "We show that, with the estimator most of these studies use, the synergy value is mostly
  something simpler" is scoped to the family and this dataset.

**M2 (the refutation). Confirmed.** A fall of MMI-sts refutes the hypothesis as operationalised: an increase of
whole-brain MMI-sts at W = 60. On the paper's own account it is silent about synergy in the intended sense. Results 2,
the Introduction, S1 Text and the author summary say so, and the measured quantity is "MMI-sts" wherever the text
reports a change.

**M3 (the residual's rate against the generators). Confirmed.**

- The data's per-subject slope is −0.75 with t interval [−1.133, −0.374]. That interval contains the AR(1) generator's
  −0.39; the null's −0.370 lies at its edge (0.004 above the limit; at the printed precision the two coincide); the
  band-passed generator's −0.18 lies well outside.
- The ratio of group means is −0.79 per unit of regional r₁, with a Fieller interval of [−1.60, −0.08] and a
  bootstrap interval of [−1.35, −0.25] (`checks/derived_r17.out`, item 1; the review's [−1.33, −0.26] used another
  bootstrap seed). Both contain all three generators.
- The cross-half relation holds on ts_gsr (−0.385 and −0.700). On ts_demean it is −0.598 and −0.052 (`splithalf.log`,
  line 24).
- Results 4 ¶2 and ledger L10 are rewritten. "Not validated for the residual on this dataset" now rests on the
  band-passed comparison, and on the generators' applying one change to every subject.

**M4 (the finite-sample null). Confirmed.** In the null, the band-passed model is solved to the data's four run ×
period operating points. It therefore carries the data's autocorrelation change: its own pair-level DiD is
(0.8532 − 0.8625) − (0.8655 − 0.8602) = −0.0146 (`review_v2_residual_null.log`). Methods' "the same construction with
no change" is wrong and is replaced.

**M5 (the pre-registration account). Confirmed.**

- **(a) "Every later computation was entered … before it was run".** This is false by the SI's own statements:
  - the finite-sample null was run by the second review before any record entry, with no recorded rule (S3 Text l.
    252; S5 Text l. 7);
  - the sts-matched null and the spectral centroid are post hoc (S3 Text l. 203, 390);
  - the coupled family and the leave-two-out had no prediction (S5 Text l. 7);
  - the fresh review's checks had no pre-recorded rule (S3 Text l. 205).
  - Replaced in the Limitations and in "Pre-registration and deviations".
- **(b) Deviations.**
  - Two inference deviations are added to the list, both against the record at l. 730–744. The pre-specified effect
    interval, a subject-bootstrap percentile interval, was replaced by the inverted sign-flip interval (B21). The
    pre-specified second null, the phase-randomised null of rule 2, is now reported as a stationarity check.
  - A new S19 Table lists every recorded prediction and its outcome (met, partly met, missed), from the record's pre-run
    and outcome entries. This makes the misses that are not in the main text visible (B16, B16b, B19 (b), B21 (d),
    B22, B23, B24).
- **(c) Timing.** "The hypothesis was recorded before any data were analysed" is qualified. The record places it
  before the first data check, and git cannot confirm that, since both entered in the initial commit (S5 Text).

**M6 (Results 1's residual pattern). Confirmed.** The stationary null reproduces most of the residual level at W = 60:
−0.0373 against the data's −0.0489, and −0.0353 against −0.0530 before injection on the DMT run. Most of it is the
response to the sampling scatter of the cross-lag departures (S3 Text §6). "The signature of lagged structure the
diagonal family lacks" is replaced.

**M7 (self-containedness and notation). Confirmed.**

- **Notation.** One convention is used throughout: regional r₁ (a region's sample lag-1 autocorrelation within a
  window; its mean over regions is whole-brain r₁, whose DiD is the paper's r₁ contrast) and pair r₁ (the mean of a
  pair's two lag-1 correlations in its window's 4 × 4 matrix, the quantity of the generators and of the
  AR(1)-substituted estimate). On the family both equal a. "Pair-level a" is replaced by "pair r₁" in the text,
  tables and figures.
- **Levels.** Before injection on the DMT run, regional r₁ is 0.848 and pair r₁ 0.863; their DiDs are −0.0146 and
  −0.0155.
- **Labels and paths.** The computation labels (B17, B21–B24 …) and file paths leave the main text; S-table and S-Text
  references replace them.
- **Symbols.** c, δ, δ_sym, δ_anti, A_other, λ, a_s and a_n are each defined in one sentence at first use, and
  "manufacture" is defined where it is first used.

**M8 (the SI). Confirmed.**

- **The applicability table.** It is cited as "(S3 Text)" but lives only in `notes/partB5_literature_v2.md`. Its Tables
  A and B become S20 Table.
- **S4 Text.** It points to `supplementary_cobidas.md`, which is keyed to earlier drafts, and is brought up to the
  current text.
- **Process labels.** Labels such as "Stage B of round 16", "planning session", "writer's session", "the fresh review"
  and "quoted at (90690f4)" are replaced by dated, neutral descriptions, defined once in S5 Text.

**M9 (Ethics). Confirmed.** The exact subject-code sentence of round 12 (record, round 12, item 6) was dropped at
106bd33 and is restored in S1 Text's ethics paragraph, with a pointer in the main text. The decision on the git history
stands (record, 15 Sep 2026, and round 12, item 7): the codes are in the public source release. "Anonymised" becomes
"pseudonymised" (citation check P6). The REC number stays a [TK] for the co-author note.

**M10 (the AI-use statement). Confirmed.**

- **"Independent".** It becomes "separate sessions of the same AI system".
- **Full texts.** The claim that every cited work was read in full becomes "every cited work in full except three"
  (citation check P9).
- **Precision.** The closed form's identities were checked to 4 × 10⁻¹⁵ (`family_checks.log`). The fast implementation
  agrees with phyid to 1.3 × 10⁻¹⁴ on the saved window and bin means and 2.3 × 10⁻¹⁴ on the regional values
  (`phiid_fast_validate.log`), and to 1.0 × 10⁻¹³ on the TR-local series of the four subject-runs and three windows it
  checked (`phiid_fast_validate_local.log`). Methods (Estimator) gives these figures and the statement points to them.
- **Who ran the computations.** The draft's "V.S. … ran every computation on the data on his own machine" is not
  established for the first days, and the planning session's first proposal for the replacement was also wrong.
  - V.S. (24 Sep 2026): the early analyses were run by him with the system, and he does not know which of the two
    executed each script. The early commits carry the system's trailers (44cec4f onwards), and the review of 14
    September read file modification times on his disk (`notes/adversarial_review_2026-09-14.md`, §3.1).
  - From 18 September 2026 every result file committed was produced by V.S.'s runs on his computer (the section-6 run
    of 20 Sep, B14–B20, B16b and B17b, B21–B24; record, their outcome entries).
  - But the record also states that a drafting session's clone held the data files by accident from 15 September, that
    a 28-second smoke test of B19's part (b) ran on them there on 20 September with its output discarded (record,
    "B19, outcome"), and that the session's remaining copies were deleted on 23 September (record, decision entry of
    23 September, the `sch116_to_yeo.csv` paragraph). So "the system's sessions held no data from 18 September" is
    false, and the statement does not say it.
  - The statement says: until 18 September V.S. and the system ran the analysis together and the record does not say
    who executed each script; from 18 September every computation on the data whose output is committed was run by
    V.S.; one session held a copy of the data by accident until 23 September, and one 28-second test ran on it on 20
    September, its output discarded. S5 Text gives the detail.

**M11 (reproducibility). Partly.**

- **The single full run.** It stays at the final commit under a new pre-run entry; its [TK] is unchanged.
- **S2 Text.** It gains the rsHRF parameters and states which deconvolution results the repository can and cannot
  regenerate.
- **S5 Text.** It lists the result files whose headers carry `-dirty` or `nogit`, and which of them the final run
  regenerates.
- **Archiving.** A DOI archive is part of submission, not of this round.

**M12 (the Limitations). Confirmed.** The limitation sentence of 90690f4 (the family's fit beyond lag 1, the symmetric
coupled family, the unidentified within-window source, the unremoved manufacture, and calibration only on this
dataset) was deleted in the shortening and is restored.

**M13 (CCS). Confirmed in substance.**

- The within-window r = −0.011 is from one window of one subject, and the text says so.
- The correlation across the 28 group means runs across the drug time course.
- The per-subject r (−0.43 to −0.27) all have intervals that include zero, and the family is nearly flat (B23 (c)).
- The abstract, the Results 6 heading and ¶1 state CCS's relation to r₁ at that strength, and "not absent" goes. The
  Recommendations' "do not treat CCS as free of it" becomes "check CCS contrasts against r₁ too (Results 6)", and S3
  Text's "not absent" goes with it.

**M14 (the recommended null). Confirmed.** The AR(1)-substituted value is not itself a null. The recommendation names
surrogates simulated from each pair's AR(1)-substituted matrix, or from the two spectra with the measured lag-0
correlation, passed through the same estimator.

**M15 (what the paper delivers). Partly.**

- The Introduction regains one clause on the worked example of Mediano et al. (2021).
- Data availability names the functions that implement the closed form and the substituted estimate in
  `notes/rev_phiid_fast.py`.
- Declined: packaging them as a separate documented library. That is outside a Methods article's revision.

## The adversarial review: minor items and typos

Unless stated, each is **Confirmed**, and the proposed fix is taken as worded in the review.

1. **Figure order: Partly.** PLOS requires figures cited in order. Fig 2 is first cited before Fig 1, and Fig 6
   before Figs 4 and 5. The figures are renumbered by order of first citation; the script and the file names follow.
2. **Section order: Judgement.** The PLOS order (Acknowledgments → References → Supporting information captions) is
   adopted. The PLOS Computational Biology submission guidelines (read 24 Sep 2026) also say that funding, competing
   interests, data availability and author contributions are entered in the submission system; for the preprint they
   stay in the file, after Materials and methods, and their removal goes on the submission list.
   - Figure captions are placed after the paragraph of first citation.
   - The "Manuscript for co-author review" line stays until the co-author review, and its removal goes on the
     submission list in `CLAUDE.md`.
   - Each S-file gets its own caption.
3. **SI citations.** Every S-file is cited in the main text.
4. **References: Partly.**
   - Faes et al. (2025) regains a short main-text citation in the Introduction.
   - The head note moves to S5 Text §5, since it describes checking, not references.
   - Numbered style stays for submission.
   - Nichols et al. (2017), cited by the COBIDAS checklist, gets its own reference entry in S4 Text, checked against
     its Crossref record on 24 Sep 2026 (Nature Neuroscience 20(3), 299–303, doi 10.1038/nn.4500); it was not read in
     full, and S4 Text says so. It is not added to the main reference list.
5. **The "no commit identifier" claims.** S5 and S3 say the main text carries no commit identifier outside Data
   availability; after M7 that is made true.
6. **Stale references in S5 l. 7.** Fixed.
7. **S2 l. 7 "(Discussion)".** Becomes "(S3 Text §10)".
8. **S3 l. 388, the stale reference to Results 7.** Fixed.
9. **S3 l. 388, "−0.069 against −0.081".** It compares unlike Δr₁ and is restated like for like, or removed.
10. **S3 l. 205.** "Positive in every variant × estimator combination" is false for the run-level rows, and "+0.0041
    against +0.0077" is a half, not a reproduction. Both are corrected.
11. **S1 l. 5.** The sensitivity set (windows 5–14) was fixed on 13 Sep, before any real windowed run (record l.
    671–677). Only the early/late sets and the trend corrections came later.
12. **S3 l. 155.** "The account rests on … the AR(1)-substituted estimate" is reworded.
13. **S3 l. 120, −1.77 and −1.74.** Harmonised, with the basis of each stated.
14. **S3 l. 126.** The +0.756 interval is labelled a percentile interval.
15. **S3 l. 254.** "Fig 3c" becomes "the former Fig 3c".
16. **S3 l. 317.** The population-Δa rates are removed, or relabelled on the pair-r₁ basis.
17. **Fig 1 (Fig 2 after renumbering): Partly.** The annotation follows Finding 12: the excess turns negative only
    beyond an asymmetry, 0.008 at (0.85, 0.25). The leader line no longer crosses the text. The atoms stay grouped by
    kind (the grouping is what the figure adds to the table); Table 1's caption says "Fig 2 draws the table, its
    atoms grouped by kind".
18. **Fig 4c.**
    - The expectation's ±1 SD band is made visible, with a stronger fill and outline, or drawn as an error bar.
    - One meaning is kept for "grey band".
    - The legend has no script names and does not overlap the data.
    - The y-label no longer runs into panel b.
19. **Fig 3a, c.** The generator lines are per unit pair r₁ on a regional-r₁ axis. The caption states this and the
    6 % scale difference (0.0155/0.0146).
20. **Fig 2a.** The contour labels are moved clear of the density contours, and the caption lists every curve of 2c.
21. **Results 5.** The sts levels follow |r_τ| and are not monotone in τ; the text says so.
22. **Results 5.** "DMT shifts" becomes "relative to placebo, the … function shifts".
23. **Results 6.** ΦR's other cells are given (ts_demean +0.0157 [−0.0024, +0.0341]; the phase p values), and CCS-sts
    "rose" becomes "was positive".
24. **Results 7.** The bound on the r₁ of any in-band signal, r₁ ≥ cos(2π · 0.08 · 2) = 0.54, is stated. In the
    abstract, "cannot remove" becomes "cannot fully remove".
25. **Proportionality.** Its sentence gives values, without threshold language.
26. **Results 2.** "28 leave-one-out refits" becomes "14 per variant". The global fit is not called an independent
    check.
27. **Results 2: Partly.** No per-subject vector of the pair |q| DiD is saved (`residual_source.log` gives the group
    value and the sign count only), so no interval can be computed without the data. The text gives the DiD with its
    sign count (10 of 14 negative) and says why it has no interval. Units are not mixed, and the quantity is named
    "whole-brain r₁" under the notation of M7.
28. **Results 3.**
    - The spin p belongs to the cortical Spearman 0.771.
    - The cortex-only Pearson r is 0.807.
    - The partialled contrast gets its t interval, [−0.011, +0.012], which admits half the original. The t interval is
      used because B20 saved the per-subject mean and SD, not the vector; it is labelled as a t interval. "Vanishes" is
      used only with that interval.
    - One clause each: the residual map's network structure against the unpartialled map's (spin p 0.0009 against
      0.056); the map's slope, 3.09, against the family's 6.07; rtr's slope, 0.50, against the family's 0.056.
29. **Results 4 ¶1.**
    - The early and late values are cited "(Fig 4)", not Table 3.
    - The substitution replaces the two cross-lag entries and sets the two lag-0 entries to their mean. This is
      confirmed in `partB4_diagnostic.py` l. 73–75: `ar1_corr(ax, ay, q)` with q = ½(C[0,1] + C[2,3]). The text says
      so.
    - The heading includes q.
30. **Results 4 ¶3.** (a1) is "at fixed (a, q)", as in Table 3; (a3) is the "(r₁, q)" row.
31. **Results 4.** The conversions are stated as those of AR(1) pairs at a = 0.85.
32. **Table 3.** The null's value is given without a Monte Carlo SE, as a single construction, and "function"
    replaces "functions".
33. **Results 1.** "For any q" becomes "on the grid checked (mean a 0.80–0.90, q 0.05–0.70)". "Coupling of the same
    sign as q lowers sts" is qualified to the range tabulated: up to c = +0.10 at (0.85, 0.25), where the fall is
    largest near +0.05 and has almost vanished at +0.10 (1.2569 against 1.2588; `coupling_map_tables.md`).
34. **The Huang et al. sentence.** Rewritten, as in citation check P11.
35. **"Two limits on reach remain".** Reworded.
36. **Methods, inference.**
    - "Earlier versions" becomes "the pre-specification".
    - The sign-flip inversion's assumption is stated: symmetry of the per-subject DiDs about the mean under the null.
    - The t-interval method for slopes is added.
37. **The calibration's coefficient.** "The data's population-level coefficient" is corrected: the AR(1) pairs'
    coefficients are drawn around 0.85, the data's mean regional window-level r₁. Their own window-level pair r₁ is
    0.786 (B23 (b)).
38. **The literature search: Partly.** The record (`notes/partB5_literature.md`, §"How the literature was searched";
    `notes/partB_prespec_2026-09-14.md`, B5) gives the date (14 Sep 2026), the tool (web searches and page fetches from
    a session of the AI system) and the scope fixed before the search (committed at 477cccc, 12:50 UTC; the table at
    e2d72d6, 14:24 UTC). It does not record the queries, and Methods says so. B23 (d)'s finding that exposure per unit
    of spectral difference hardly depends on TR stays in the Discussion, beside the scoping rule.
39. **"Branch rule".** "The diagnostic's branch rule" becomes "the residual's branch rule", and S10 Table's "residual
    diagnostic" becomes "the residual of the AR(1)-substituted estimate".
40. **Methods.** "Independent windows" becomes "non-overlapping, separately fitted windows", and l. 204's referent is
    made clear.
41. **Introduction ¶3.**
    - "DMT, a drug that produces a state of intensified conscious content".
    - "The closed form was derived afterwards to account for it".
    - Abbreviations are expanded at first use (TR, BOLD, HCP, BIC, HRF, MEG, PCB, CCS).
42. **Data availability.** "Quoted from, or derived as stated from". The figures were written at 526090d and committed
    in 66c6331; after this round, by the commit that regenerates them.
43. **"Tier".** The jargon is defined once in S1 Text, or replaced.
44. **Cross-file values.** Each value carries its label (window or run level; the basis of each rate).

**Typos.** All taken: l. 116, l. 160, S17 "1.191", S11's 0.8176 against S18's 0.8174 (checked against their sources
and labelled if both are right), S₄ → R₄, and "Fig 1." for "Figure 1.".

## The citation check

**Counts.** The reviewer counted 51 changed citing sentences with an author–year citation, against the writer's 91.
The writer counted every changed sentence that cites any source, including record entries and commits. Both counts are
recorded. Of the 111 sentence × work pairs:

| verdict | pairs |
|---|---|
| supported | 88 |
| supported with qualification | 6 |
| not supported | 4 |
| misattributed | 0 |
| not checkable locally | 13 |

The problems:

- **P1 (the workspace account; A26, second bullet).** Confirmed. The account ties conscious level to integrated
  information (ΦR) in the workspace, not to synergy (Luppi et al. 2024, pp. 1, 8). The proposed wording is taken, in
  S1 Text and Introduction ¶3, with one change: "a prediction derived from" becomes "motivated by", since the account
  makes no prediction about psychedelics (the record's hypothesis extrapolates from it; record, "The scientific claim
  under test").
- **P2 (the workspace's synergy).** Confirmed. It is the whole-minus-max synergy, the aggregate str + stx + sty + sts
  (Luppi et al. 2024, Eq. 5). Taken.
- **P3 (Varley).** Confirmed. The aggregate scope is restored.
- **P4 (Huang).** Confirmed. "In propofol sedation".
- **P5 (Tarchi).** Confirmed. "In part, in the regional classification of Tarchi et al., 2026".
- **P6 ("anonymised").** Confirmed. It becomes "pseudonymised".
- **P7 (Afyouni).** Confirmed. "When their true correlation is zero".
- **P8 (CCS).** Confirmed. The double redundancy is Mediano et al.'s extension of Ince's single-target CCS.
- **P9 (Theiler et al. 1992).** Confirmed. It was checked against its bibliographic record only, not its abstract.
  Corrected in the head note (moved to S5 §5) and in S5.
- **P10 (the surrogate gradient's correlations).** Confirmed. The subject is named.
- **P11 (the Huang sentence).** Confirmed. Rewritten.
- **E1–E8 (S5 history).** Confirmed.
  - The early times are labelled EEST (+03:00) or converted to UTC.
  - d51966e is dated 16 Sep and d507728 18 Sep, each with the date of its later run named.
  - "26 items not plainly supported (A1–A26)".
  - The heading of 44cec4f is described exactly.
  - "Dated to the minute" becomes "dated to the day until 14 September, to the minute from 15 September".
  - The two minute-level claims ("written to disk seventeen minutes earlier"; "on disk at 10:15") are not in the
    record. They are file modification times on V.S.'s disk, in Athens time, as the review of 14 September read them
    (`notes/adversarial_review_2026-09-14.md`, §3.1: 10:12 and 10:15). S5 attributes them to that reading and gives
    them in UTC (07:12 and 07:15), with git's times beside them.
  - The Figures paragraph is corrected (E8); with the captions now placed in the text, the paragraph itself goes.
- **Not checkable locally.** Those pairs (Tian 2020, Alexander-Bloch 2018, Váša 2018, Theiler 1992, Wu 2021,
  Cousineau 2005, Morey 2008, the phyid software) stay as the passes of 20 and 22 September left them.

## Findings of the verification itself

These came up while the planning session checked the reports against the files. Each is taken into round 17.

- **V1. The author summary's "integrated information built from it".** This is the wording A26 of 22 September
  proposed, and it is inaccurate: ΦR (TDMI − I(X;X′) − I(Y;Y′) + rtr) is not built from synergy. What the workspace
  studies report is integrated information in regions ranked by their synergy (Luppi et al. 2024, Eq. 5 and pp. 1, 8).
  The summary says so.
- **V2. The data copy in a drafting session.** See M10. The record's B19 outcome entry and the decision entry of 23
  September state it, and S5 Text and the AI-use statement now say it.
- **V3. The word limit.** Applied as first drafted, the dispositions add roughly a thousand words to Introduction–Methods. PLOS Computational Biology
  sets no length limit for Methods articles (its 3,500-word limit is for Software articles; guidelines read 24 Sep
  2026), so the 7,000-word limit is V.S.'s decision of 23 September and stands. The round moves detail to the
  supporting information, and the prompt lists each move.
- **V4. The substitution's lag-0 entries (item 29).** The AR(1)-substituted matrix also sets the two lag-0 entries to
  their mean q (`partB4_diagnostic.py`, lines 73–75). The lag-0 averaging alone changes the window-mean sts by 0.0005 at
  W = 60 (`residual_source.log`: lag-0 substitution only, residual +0.0005); the level residual is the cross-lag
  substitution's (−0.0489 of −0.0489).
- **V5. The finite-sample null (M4).** Its construction is taken from the docstring of `notes/review_v2_residual_null.py`:
  one band-pass filter per pair applied to two white noises with lag-0 correlation q, so that the cross-lag
  correlations equal the AR(1) values in population; the filter fitted to the pooled placebo autocorrelation function
  (lags 1–6), and to the post-injection DMT function for that cell; β̄ and σ_q solved to the window-level pair r₁ and
  |q| of each run × period cell. It reached a pair-r₁ DiD of −0.0146 against the data's −0.0155. One simulation; no
  replicate SD.
- **V6. The AR(1) generator's window-level pair r₁ (item 37).** 0.786 is B23 (b)'s value for AR(1) pairs at a = 0.85;
  the calibration's pairs draw a from N(0.85, 0.0125), and its own window-level pair r₁ is not reported. The text says
  "0.786 at a = 0.85".
- **V7. S11 Table's 0.8176 against S18 Table's 0.8174.** Both are right: 0.8176 is the flat in-band r₁ on the
  840-sample frequency grid (`rev_extra.log`), 0.8174 the continuous-band value (B23 (d)). Each is labelled.
- **V8. Captions.** The figure captions in `captions_v2.md` carry computation labels and file paths. Once the
  captions are placed in the text (minor item 2) they are main text, so they carry neither; the provenance moves to
  a separate "Source" line under each caption in `captions_v2.md`, which the text does not reproduce.
- **V9. The coupling qualifier (item 33).** The first disposition gave |c| ≲ 0.07; the tabulated values show the
  qualifier is the tabulated range, up to c = +0.10 (item 33 as corrected).
- **V10. The sensitivity window set (item 11).** Confirmed from the record's lines 671–677 at 66c6331: windows 5–14
  were fixed as the sensitivity set on 13 September 2026 "before any real windowed run".
- **V11. The regional slope.** The explanation the review asked for (item 28) is stated qualitatively: a region's r₁
  is one member of each of its pairs, and a pair's sts follows its less autocorrelated member, so the map's slope is
  about half the family's rate for a change of both members' r₁. (A planning-session sanity check on the family with
  the 115 regional r₁ values gives a slope of about 2.9; it is not quoted.)
- **V12. The subject numbering.** "Subject 8" and "subject 14" of the leave-one-out are the same subjects in
  `splithalf_subjects.csv` and in `inference_rows_raw.pkl` (the half-mean r₁ DiDs and the full DiDs correlate at 0.9997
  in that order). The text names them by their r₁ change, not by number.
