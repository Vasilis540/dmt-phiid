# Fresh adversarial review of `manuscript/draft_v2.md` at 56df014

## 1. Header

**Date.** 17 September 2026.

**Reviewer.** Claude (Anthropic), configured model identifier `claude-opus-5`; the serving model may
differ from the configured one. Working from a private copy of the repository at 56df014, with no git
remote and without `external/`. I met this manuscript for the first time in this session.

**Files read.** `manuscript/draft_v2.md` (in full, including the bold Status paragraph and "Sources and
notation"); `manuscript/supplementary.md`; `manuscript/supplementary_cobidas.md`;
`manuscript/prespecification_summary.md`; the caption strings in `scripts/15_figures_v2.py` (current) and
`manuscript/figures/captions_v2.md` (stale, for comparison); the five figures
`manuscript/figures/fig{1..5}_v2_*.png`. Evidence: the entries of `manuscript/analysis_record.md` the
paper points to (Pre-registered analysis choices; Primary B result; Correction note 14 Sep; Closure entry;
Part B items 6–8 pre-run and outcomes; Correction note 15 Sep 10:05; Leave-two-out; CCS definition
checked against the journal version; Run-level mean cross-lag deviation and the regional sts–r₁ test,
pre-run and outcomes; Text revision after the plain-language companion; The sign(q)-weighted cross-lag
deviation, pre-run and outcome; The sign(q)-weighted deviation at W = 60 and on the finite-sample null,
pre-run and outcome; Correction note on the computations of 16 Sep 10:23; The end-to-end run of
`run_all.sh`; The cross-lag budget, pre-run and outcome; Closure of the cross-lag thread);
`notes/review_results/partB/{ccs_pub_tables, ccs_tables, coupling_map_tables, crosslag_budget_tables,
crosslag_budget_null_tables, crosslag_deviation_tables, diag_tables, lag_tables, regional_sts_r1_tables,
scope_map_tables, splithalf_tables}.md`; `notes/review_results/partB/{ccs_definition_check,
family_checks, leave_two_out, residual_source, splithalf}.log`;
`notes/review_results/logs/{phiid_fast_validate, rev_extra, review_checks, review_v2_residual_null,
sts_matched_null_F1, F2, F3}.log`; `notes/review_results/inference_rows_{raw, diag, ccs, ccs_pub,
lag}.{csv,pkl}`; `notes/review_results/partB/{crosslag_budget, crosslag_budget_null, crosslag_deviation,
regional_sts_r1, scope_map_overlay, leave_two_out}.csv`;
`notes/review_results/partB/diag_series_ts_{gsr,demean}_W{30,60}.npz`;
`results/{primary_b_ts_gsr_win60, primary_b_ts_gsr_win30, primary_b_ts_demean_win60, proportionality,
loo_did_win60, global_fc_did_ts_gsr, global_fc_did_ts_demean, windowed_atoms_did_ts_gsr_win60,
bias_check, robustness_c_ts_gsr, regional_analysis_ts_gsr}.csv`;
`results/atoms_win60_115regions-all_ts_{gsr,demean}_window.npy`;
`notes/review_results/partB/ccs_{pub_,}atoms_win60_ts_gsr.npy`;
`notes/{partB_prespec, partB_summary, partB1_scope_map, partB2_ccs, partB3_lag, partB4_diagnostic,
partB5_literature, venue_options}.md`; `notes/review_computations_2026-09-14.md` (sections 1, 5, 6);
`README.md`; `run_all.sh`; `requirements.lock.txt`; the scripts `00_verify.py`,
`01_synergy_timecourse.py`, `06_primary_b_analysis.py`, `07_windowed_atoms_did.py`, `11_regional_analysis.py`,
`13_loo_did.py`, `14_proportionality.py`, `15_figures_v2.py`, and `notes/{rev_inference, rev_series,
rev_phiid_fast, rev_crosslag_budget, partB4_diagnostic, partB6_ccs_definition, partB7_splithalf,
partB8_coupling_map, partB9_leave_two_out, partB10_crosslag_deviation, partB11_regional_sts_r1,
partB12_crosslag_budget, partB13_crosslag_budget_null, review_v2_residual_null, partB1_scope_map}.py`.
Phase 2 (after my findings were written to `phase1_findings.md`):
`notes/adversarial_review_2026-09-14.md`, `notes/adversarial_review_draft_v2_2026-09-15.md`,
`notes/adversarial_review_draft_v2_second_pass_2026-09-15.md`,
`notes/verification_correction_note_2026-09-15.md`, `notes/companion_plain_language.md`,
`notes/defence_questions.md`, `notes/planning_checks_2026-09-16/` (README, `planning_chat/*.log`,
`reviewer/*.log`, `audit/audit_bundle15.log`, `reproduction_checks/*.log`, and
`planning_chat/check3_signsel.py`, `reviewer/v_slope_q.py`), `CLAUDE.md`.

**Checks I ran** (each in `notes/fresh_review_2026-09-17/checks/`, with its `.log` beside it; each runs
in under three minutes on one core; none touches `external/`, `run_all.sh` or any script under
`scripts/`).

- `check_A1_atoms_family.py` — an independent implementation of the Gaussian ΦID product lattice with
  MMI redundancy and Möbius inversion, written from the definitions and **not** from
  `notes/rev_phiid_fast.py`, cross-checked against `phyid` at the pinned commit
  6c5f2e9d33c985efbdf875d45cb5a2a6a5cdbf44 (installed outside this folder). Verifies the sixteen atoms
  on the family over 48 (a, q) settings, the closed form for sts, both derivatives, the grid counts and
  the Figure 2(c) minima, the shared-slow-component formula for d, the τ = 1 equivalence over 10,017
  random positive-definite stationary 4 × 4 blocks, ∂sts/∂(cross-lag), and the coupled family's
  slope and curvature.
- `check_B1_did_recompute.py` — recomputes the primary DiD, all sixteen atom levels and DiDs, the exact
  16,384-assignment sign-flip p, the subject bootstrap, the per-subject sts/r₁ collinearity, the 91
  leave-two-out refits, the residual diagnostic's DiDs and the CCS-sts relations, from
  `results/atoms_win60_*.npy`, `diag_series_*.npz` and the `did_subjects` fields of
  `inference_rows_*.pkl`.
- `check_C1_residual_vs_null.py` — the observed residual DiD against each finite-sample-null value; the
  run-level residual with a subject bootstrap; the attenuation ceiling on r = 0.953; the family-scale
  conversion of δ_run at three candidate operating points; and (appended) a reconciliation of my
  ∂sts/∂d with `notes/planning_checks_2026-09-16/reviewer/v_slope_q.log`.
- `check_C2_variance_ratio.py` — the window-variance/run-variance ratio against the windowed sts and
  windowed r₁ group-mean series, from the committed series in `rev_extra.log`.
- `check_I1_fig4_scale.py` — measures Figure 4's two axes boxes from the rendered PNG to test the panel
  title's "same nats per unit height".

Literature was checked against primary sources over the web where they were reachable: Varley (2024,
arXiv 2407.16601 full text), Barrett (2015, arXiv 1411.2832 HTML), Mediano et al. (2021, arXiv
2109.13186v1 including the Appendix), Liardi et al. (2025, PLOS Comput Biol article page), Faes et al.
(2025, PRL abstract page), Ince (2017, Entropy article page), Luppi et al. (2022, Nature Neuroscience
article page), Luppi et al. (2024, eLife article page), Singleton et al. (2025, Communications Biology
article page). Timmermann et al. (2023) and the PNAS SI Appendix of Mediano et al. (2025) were not
reachable (403 / reCAPTCHA); see §6.

---

## 2. Verdict

**Major revision.** This is an unusually careful paper and I could not break its core. I re-derived the
sixteen atoms, the closed form, both derivatives, the grid counts, the Figure 2(c) minima, the
shared-slow-component formula and the τ = 1 non-separability from the definitions, independently of the
project's own module, and they are exact; the primary DiD, its sign-flip p, the whole sixteen-atom table,
the collinearity, the leave-two-out, the diagnostic and the cross-lag budget all reproduce from the
committed per-subject values; and in a sweep of roughly 200 numbers I found not one that disagrees with
its source beyond rounding. What decides the recommendation is two things. First, **three of the
paper's load-bearing inferential statements are stated more strongly than its own numbers allow**: the
headline per-subject collinearity r = 0.953 exceeds the attenuation ceiling that the paper's own
reported split-half reliabilities impose on a correlation between two reliable components (F1), so a
material part of it is noise shared by two quantities read off the same 60-TR windows — the very
argument the paper applies to the residual/CCS pair, and never to this one; the "rest" of the residual
DiD said not to be accounted for by the finite-sample null is not distinguishable from zero, every null
value lying inside the observed interval (F2); and the window-variance exposure is quoted at +0.37 for
the estimator the paper argues against while the same log gives +0.49/+0.77 for the primary windowed
estimator, with no variance control run anywhere (F3). Second, **the Abstract, cut on 16 September, has
lost the one qualification that bounds the paper's central claim**: the r₁-dominance result is a
property of a family with no lagged interaction, and the paper's own coupled family shows lagged
coupling of |c| = 0.02–0.05 moving sts at fixed (r₁, q) by a third to twice the observed contrast,
with no value of c measured on the data — a caveat the Discussion states and the Abstract never
mentions, while its Conclusions generalise to "MMI-sts contrasts … are dominated by lag-1
autocorrelation change wherever r₁ differs" (F4). All four are repairable in text plus one bootstrap
and two numbers already computable from committed outputs; none needs new data, and only one (F3's
variance control) would need a new analysis with a dated pre-run entry.

---

## 3. Findings

### F1 — the headline collinearity cannot separate the mechanism from shared window noise, and the paper does not say so

- **Severity:** MAJOR
- **Location:** Results 3. "First, r = 0.953 leaves 9 % of the per-subject variance of the sts DiD
  unshared with the autocorrelation DiD". Also Abstract ("correlating at r = 0.953 per subject"),
  Results 2 ("the account rests on the closed form, on the per-subject collinearity (Results 3) and on
  the per-pair prediction"), Discussion ("the per-subject collinearity is 0.95"), Recommendations, and
  Figure 3(a).
- **Problem.** The paper's own split-half reliabilities for these two per-subject DiDs are 0.717
  (MMI-sts) and 0.741 (r₁) on `ts_gsr` — it quotes them, as "0.71–0.74 and 0.69–0.72", in
  Results 4. If the two measurements' errors were independent, their correlation could not exceed
  √(0.717 × 0.741) = 0.729 (0.843 after Spearman–Brown). The observed 0.953 exceeds both and
  disattenuates to 1.31 (1.13), which is inadmissible. The errors are therefore not independent: a
  material part of the 0.953 is estimation noise common to the same 60-TR windows, because sts and r̂₁
  are both functions of the same window's sampled autocorrelations at ≈ 20 effective samples. The
  paper makes exactly this argument about the residual/CCS-sts pair ("Both are functions of the same
  per-window 4 × 4 matrices, so the shared variance may be common signal or common estimation noise";
  "most of the within-half correlation … is estimation noise common to the same windows") and runs a
  split-half test for it; it never applies it to the 0.953, reports no split-half of that pair, and
  frames the collinearity's only limitation as the 9 % left over. The 9 % framing has it backwards: the
  question is not what the 91 % leaves out, it is how much of the 91 % is mechanism.
- **Evidence.** `checks/check_C1_residual_vs_null.log` section (3);
  `notes/review_results/partB/splithalf_tables.md`, the "Split-half reliabilities" line of each variant
  ("autocorrelation +0.741; MMI sts +0.717"; ts_demean "+0.712; +0.686"). Per-subject DiDs and the
  correlation recomputed in `checks/check_B1_did_recompute.log` section 2 (Pearson +0.9528, Spearman
  +0.9033, matching `rev_extra.log` (a) and `diag_tables.md`).
- **Fix.** Text, plus one check of existing outputs. In Results 3 replace the "Two facts keep the two
  contrasts from being identical. First, …" sentence with: "Two facts keep the two contrasts from being
  identical. First, r = 0.953 leaves 9 % of the per-subject variance of the sts DiD unshared with the
  autocorrelation DiD; the diagnostic's residual DiD (Results 4), a group-level quantity computed pair by
  pair, is a different remainder, and its significance is not a test of that 9 %. What the 91 % shared
  is, the correlation cannot say: both quantities are read off the same 60-TR windows at about 20
  effective samples, and at the split-half reliabilities of Results 4 (0.72 and 0.74) two measurements
  with independent errors could correlate at no more than √(0.72 × 0.74) = 0.73, so the observed
  0.953 requires errors that are shared. The collinearity therefore shows that the estimator follows the
  window's measured r₁, which is the mechanism's claim, and does not by itself show that the drug's
  effect on sts is the drug's effect on r₁; the group-level magnitudes (Results 2) and the per-pair
  prediction (Results 4) carry that." Then add the ceiling line to Figure 3(a)'s caption, and add the
  cross-half correlation of the sts and r₁ DiDs to `partB7_splithalf.py`'s output — that script already
  computes both quantities' odd/even DiDs to get the reliabilities, so reporting their cross-half
  correlation beside the residual/CCS one is a **check of existing outputs** on the same halves, not a
  new analysis. Correspondingly, drop "the per-subject collinearity" from the list of three things the
  account rests on in Results 2, or qualify it there.
- **Confidence:** certain on the arithmetic and on the absence of the qualification; likely on how much
  of the 0.953 is noise (the ceiling argument bounds it below, not above).

### F2 — the residual DiD's "rest" is asserted although every null value lies inside the observed interval, and the run-level residual still has no interval

- **Severity:** MAJOR
- **Location:** Results 4. "The rest, and on `ts_gsr` a run-level residual three times the null's".
  Repeated in the Discussion: "The rest, together with a run-level residual three times the null's on
  `ts_gsr` (and absent, +0.1 %, on `ts_demean`), is not accounted for by the null as specified." Abstract:
  "a finite-sample null (a review computation) accounts for a third to two-thirds of the residual DiD
  (+0.0037–0.0077 of +0.0115, p = 0.042)".
- **Problem.** Two sentences earlier the paper concedes "the observed interval contains every one of
  those values", and it does: the observed residual DiD is +0.01153 [+0.00181, +0.02111] and the null
  ranges from +0.0037 to +0.0077. The excess over the null is not significant at any null value
  (sign-flip p of observed − null = 0.15 at +0.0037, 0.25 at the primary +0.0054, 0.47 at +0.0077). So
  there is no established "rest" of the residual DiD; it is compatible with being entirely
  finite-sample under this null. The paper then bundles that unsupported claim into one sentence with
  the run-level residual, which **is** supported (−0.01373 [−0.01448, −0.01302], 14 of 14 subjects,
  sign-flip p = 0.0001 against the null's −0.0045) but for which no interval is given in the paper,
  Table 4, Table S9 or `diag_tables.md`. The reader cannot tell which half of the sentence the evidence
  supports. The third review made this point (1d(i), 1d(ii)); the CI-containment concession was added
  and the interval was not.
- **Evidence.** `checks/check_C1_residual_vs_null.log` sections (1) and (2), from
  `inference_rows_diag.pkl` (`did_subjects` of `diag residual sts ts_gsr W60`, primary) and the
  `residual` column of `notes/review_results/partB/crosslag_deviation.csv` (per subject and run at the
  run level); null values from `notes/review_results/logs/review_v2_residual_null.log` and the third
  review's Appendix, computation 3.
- **Fix.** Text, plus one bootstrap of committed values (a **check of existing outputs**:
  `crosslag_deviation.csv` holds the 28 run-level residuals, and `rev_inference.Engine.boot_ci` and
  `signflip_p` are the paper's own primitives). Replace the sentence with: "The residual DiD is
  therefore not distinguishable from the null as specified: the null's point values span a third to
  two-thirds of it and the observed interval contains all of them, so nothing about a component beyond
  finite sampling follows from it. What does exceed the null is the run-level residual on `ts_gsr`,
  −0.0137 [−0.0145, −0.0130], negative in 14 of 14 subjects, against the null's −0.0045 (−1.1 %
  against −0.34 %); on `ts_demean` the run-level residual is +0.1 %, i.e. absent." Carry the same
  split into the Discussion and into the Abstract, whose current sentence should end "…, and the
  observed interval contains every one of those values". Add the run-level CI to Table 4 and Table S9.
- **Confidence:** certain.

### F3 — the window-variance exposure is quoted for the estimator the paper argues against and omitted for the estimator it uses

- **Severity:** MAJOR
- **Location:** Results 6. "the global-fit sts bins correlate with that ratio at +0.37 per run on
  average (review, section 1)". Related: Results 3, "exposed to the within-run variance change on the
  DMT run (window variance / run variance 1.28 in the pre-injection windows against 0.89 after …),
  which moves every local mutual information".
- **Problem.** `notes/review_computations_2026-09-14.md` section 6, the source the paper cites, reports
  in the same place that "The windowed sts and the window-standardised autocorrelation series each
  correlate with this ratio at +0.49 / +0.54 per run on average (group-mean series +0.77 / +0.73)". The
  paper quotes only the +0.37 for the global-fit bins, and quotes it as a reason to distrust the global
  fit — which invites the inference that the primary windowed estimator is not so exposed, when on the
  same log it is more so. The variance contrast is also the largest and most consistent effect in the
  dataset (DiD −0.514 [−0.674, −0.358], p = 0.0001, negative in 14 of 14) — larger and far more
  consistent than the r₁ DiD (−0.0146, p = 0.0106, 12 of 14) that the paper calls "the mechanism's
  input" — and it is the only such quantity for which no control is run: framewise displacement is
  residualised out of every contrast, window variance is not. The two exposures are not the same in
  kind (the global fit's bins are local atoms under one run-level covariance, so a low-variance bin gets
  a lower local mutual information mechanically; the windowed estimator refits a correlation matrix per
  window, so its correlation with the ratio is a co-variation of variance and autocorrelation in the
  data rather than a scale artefact) — but the paper never draws that distinction, and a referee cannot
  draw it from the text.
- **Evidence.** `checks/check_C2_variance_ratio.log`, reproducing +0.77 (sts) and +0.72 (r₁) on the
  group-mean series from the committed series in `notes/review_results/logs/rev_extra.log` sections (b)
  and (d); `review_computations_2026-09-14.md` section 6 for the +0.49/+0.54 per-run figures and section
  1 for the +0.37 and the variance DiD. Partialling the ratio out of the 28-point sts/r₁ correlation
  leaves +0.946 (from +0.974), so the ratio is not the whole of the collinearity.
- **Fix.** Report both figures where the +0.37 appears, with the distinction in kind, and say what is
  not controlled. Results 6, after the +0.37: "The windowed series are correlated with the same ratio
  more strongly — the windowed sts and the window-standardised r₁ at +0.49 and +0.54 per run, +0.77
  and +0.73 on the group-mean series (review, section 6) — but for a different reason: each window is
  refit on its own correlation matrix, so the window's variance level divides out, and the correlation
  is a co-variation of variance and autocorrelation in these runs rather than the global fit's
  mechanical exposure of a local mutual information to a bin's variance. No contrast in this paper is
  residualised on the window-variance ratio, and partialling it out of the 28-window sts/r₁ relation
  leaves +0.95 of +0.97." The corresponding control on the primary contrast — regressing window-mean sts
  on the window-mean variance ratio within each subject and condition, exactly as the FD control is run,
  and recomputing the DiD on the residuals — would be a **new analysis** and needs a dated pre-run entry
  in the record before it is run; it is worth running, because the variance DiD is larger and more
  consistent than the r₁ DiD and a referee will ask.
- **Confidence:** certain that the figures exist and are omitted; likely that a referee would require
  the control.

### F4 — the Abstract has lost the lagged-coupling qualification that bounds the paper's central claim

- **Severity:** MAJOR
- **Location:** Abstract, Conclusions. "On autocorrelated fMRI, MMI-sts contrasts between states or
  groups are dominated by lag-1 autocorrelation change wherever r₁ differs". Also Discussion, "What
  the finding is and is not": "What follows for a between-state contrast is narrow: when the states
  differ in r₁, the MMI-sts contrast is dominated by that difference, scaled by ∂sts/∂r₁, whether or
  not anything the word 'synergy' is meant to capture has changed."
- **Problem.** The r₁-over-q dominance is a property of a family that has no lagged interaction by
  construction, as Methods says. On the paper's own coupled family, at the operating point and at fixed
  (r₁, q), sts moves by −0.027 and +0.044 nats at c = ±0.02 and by −0.043 and +0.152 nats at
  c = ±0.05 — from a third to nearly twice the observed contrast of −0.081 — and no value of c is
  measured on the data. The Abstract never mentions the coupled family, lagged coupling or a common slow
  drive; its 319 words carry the AR(1) identity, the 32-fold ratio and the conclusion, and nothing that
  bounds them. The Discussion states the caveat ("This is a property of the estimator on a family
  without lagged interaction; on the coupled family lagged interaction moves sts by comparable amounts
  at fixed (r₁, q)") and then, in the very next sentence, takes the unconditional step anyway. The
  honest form of the claim is conditional: when the states differ in r₁ **and not in lagged coupling**,
  the contrast is dominated by the r₁ difference; on this dataset the r₁ difference alone reproduces
  the sign and 114 % of the magnitude, and lagged coupling is not measured.
- **Evidence.** `checks/check_A1_atoms_family.log` section 6, which reproduces
  `notes/review_results/partB/coupling_map_tables.md` row for row (sts 1.2315, 1.3023, 1.2155, 1.4111
  against 1.2588; slope −1.771 per unit c, curvature +40.3) and independently confirms the derivative
  ratio, the grid counts and the τ = 1 non-separability. `notes/adversarial_review_draft_v2_2026-09-15.md`
  finding 9.2 raised the family's exclusion of interaction; the fix was the coupled family in Methods and
  Results, and the Abstract was cut afterwards, on 16 September.
- **Fix.** Text only. Add one sentence to the Abstract's Results, after the fold sentence: "The
  dominance is a property of a family without lagged interaction; on a coupled VAR(1) at the same
  (r₁, q), interaction of |c| = 0.02–0.05 moves sts by a third to twice the observed contrast, and
  no value of c is measured here." Change the Conclusions to: "On autocorrelated fMRI, MMI-sts contrasts
  between states or groups are exposed to lag-1 autocorrelation change wherever r₁ differs and lagged
  coupling is not separately established; here the per-pair diagnostic's prediction from each pair's
  (a_x, a_y, q) gives the sign and 114 % of the magnitude." And in the Discussion, make the "What
  follows" sentence conditional: "when the states differ in r₁ and not in lagged coupling, which
  τ = 1 cannot separate, the MMI-sts contrast is dominated by that difference…". The title's
  "dominates" survives: it names the comparison the paper actually makes (r₁ against q), and the
  subtitle "an analytic account, a residual diagnostic, and a within-subject test on DMT fMRI" is
  correctly calibrated — I would leave it.
- **Confidence:** certain that the Abstract omits it; likely on the wording of the fix.

### F5 — the data-availability statement claims a git SHA on every results table; 26 of 30 Part B and review result files carry none, and the project's own rule requires one

- **Severity:** MAJOR
- **Location:** Data and code availability. "every results table with the git SHA that produced it".
  Also `notes/defence_questions.md`: "every results table carries the git SHA that produced it".
- **Problem.** It is true of all eleven files I read under `results/` — but one of those carries a
  `-dirty` SHA, which does not identify a code state (`results/global_fc_did_ts_{gsr,demean}.csv`,
  "git=66b570e-dirty", quoted as such in Table S7's own source line). Of the thirty result files under
  `notes/review_results/` that the Results quote, only four carry a SHA anywhere in the file
  (`crosslag_budget_tables.md`, `crosslag_budget_null_tables.md`, `crosslag_deviation_tables.md`,
  `regional_sts_r1_tables.md` — the four added on 15–16 September). The twenty-six without include
  every table the main Results lean on most: `diag_tables.md`, `lag_tables.md`, `ccs_pub_tables.md`,
  `ccs_tables.md`, `splithalf_tables.md`, `scope_map_tables.md`, `coupling_map_tables.md`,
  `family_checks.log`, `residual_source.log`, `ccs_definition_check.log`, `leave_two_out.{csv,log}`,
  `review_v2_residual_null.log`, `rev_extra.log`, and all five `inference_rows_*.csv`. `CLAUDE.md`
  standing rule 8 requires "git SHA in every output header", and the first adversarial review already
  flagged the `-dirty` variant of this on 14 September (item 11). The substance is sound — the
  reproduction check of 16 September regenerated every table and matched it to ≤ 7.9 × 10⁻¹³ — so
  what fails is only the statement, but it is a statement a referee will spot-check.
- **Evidence.** First-three-lines and whole-file grep for a seven-hex SHA across the 45 result files I
  staged; `manuscript/supplementary.md` Table S7 source line; `CLAUDE.md` §"Standing methodological
  rules", item 8; `notes/adversarial_review_2026-09-14.md` item 11.
- **Fix.** Either add the SHA to the `notes/` writers' headers (the four that do it show the pattern;
  this is a code change, not an analysis) and re-emit the tables in the single full run already planned,
  or state the position accurately: "every table under `results/` with the git SHA that produced it
  (two with a `-dirty` SHA, noted in Table S7), and the Part B and review result files with the script
  that produced it and, for those added on 15–16 September, its SHA; the record gives the commit for
  each". Correct `defence_questions.md` to match.
- **Confidence:** certain.

### F6 — "the pairs' mean point" is a different point from "the pairs' own point", and is defined nowhere in the paper

- **Severity:** MINOR
- **Location:** Results 4. "44 % of the −0.0137 run-level residual at the operating point, 37 % at the
  pairs' mean point". Repeated in the Discussion.
- **Problem.** The record's derivation uses the **run-level** mean pair point (a 0.8666, |q| 0.1945) for
  the 37 %. Results 2 uses the phrase "the pairs' own point (r₁, |q|) = (0.848, 0.24)", which is the
  **window-level** mean. Neither Results 4 nor Methods says which is meant, and at the Results-2 point
  the share is 42 %, not 37 %. A reader who carries the Results-2 point forward gets the wrong number.
- **Evidence.** `checks/check_C1_residual_vs_null.log` section (4): 44.2 % at (0.85, 0.25), 37.0 % at
  (0.8666, 0.1945), 41.6 % at (0.848, 0.24); `manuscript/analysis_record.md`, "Conversion to a residual
  on the family" ("at the pairs' mean run-level point (a 0.8666, |q| 0.1945) it gives −0.0051 (37 %)");
  `crosslag_deviation_tables.md` ("Mean pair a 0.8666, mean pair |q| 0.1945").
- **Fix.** Write the point out: "37 % at the pairs' run-level mean point (a 0.8666, |q| 0.1945)". No
  computation needed.
- **Confidence:** certain.

### F7 — the Abstract's "32-fold" is the value at one chosen point, not a property of where the pairs sit

- **Severity:** MINOR
- **Location:** Abstract. "|∂sts/∂r₁| exceeds |∂sts/∂q| 32-fold where BOLD pairs sit".
- **Problem.** 32 is the ratio at (0.85, 0.25), which Results 2 states plainly is "used for all
  derivative values quoted in this paper". Over the box the observed pair medians occupy (r₁ 0.816–0.867,
  |q| 0.22–0.41) the ratio runs from 15.4 to 40.4 — 40 at (0.867, 0.22), 32 at the operating
  point, 15 at (0.816, 0.41) — and 4–13 % of `ts_gsr` pairs and 7–30 % of `ts_demean` pairs have
  |q| > 0.6, where it falls from 9.8 to 2.0. The Abstract, stripped of the Results-2 sentence,
  presents one figure as characterising the operating region. Separately, Results 2 gives the map
  projection on `ts_gsr` (−0.087 against −0.081) but not on `ts_demean`, where the same source
  records −0.129 against −0.103, a 25 % over-prediction — the only place in the paper where a
  headline projection is given on one variant only.
- **Evidence.** `checks/check_A1_atoms_family.log` section 3 (ratios 24.87 at (0.78, 0.25), 32.09 at
  (0.85, 0.25), 39.06 at (0.84, 0.2), 24.89 at (0.84, 0.3), 9.75 at (0.85, 0.6));
  `checks/check_A2_ratio_range.log` for the ratio over the whole median box and for the |q| > 0.6
  minority;
  `notes/partB1_scope_map.md` items 2, 4 and 5; `notes/review_results/partB/family_checks.log`.
- **Fix.** "…exceeds |∂sts/∂q| by a factor of 15–40 over the pairs' observed medians (32 at the
  operating point (0.85, 0.25))", and add the `ts_demean` projection to Results 2: "on `ts_demean` the
  same projection gives −0.129 against an observed −0.103". Both are reads of existing outputs.
- **Confidence:** certain.

### F8 — "significant … wherever the lag-τ autocorrelation contrast is" is undefined, and at τ = 1 the autocorrelation contrast is not significant on the phase-randomised null

- **Severity:** MINOR
- **Location:** Results 5. "the sts contrast is significant on both nulls at both estimators wherever
  the lag-τ autocorrelation contrast is". Same sentence in the Figure 5 caption string.
- **Problem.** The clause makes the sts contrast's significance track the autocorrelation contrast's,
  but "significant" is not defined for the latter, and Table 6 gives it only one p (the sign-flip).
  At τ = 1 that contrast's phase-randomised p is 0.0729 — the paper says so in Results 2 — so on
  "both nulls" the τ = 1 pairing fails, and on the sign-flip test alone τ = 1, 2 and 3 pass. The
  sentence reads as if both quantities cleared both nulls at τ = 1, 2, 3.
- **Evidence.** `inference_rows_raw.csv`, `autocorr ts_gsr W60`, primary: `did_p` 0.0106, `phase_p`
  0.0729; `inference_rows_lag.csv` for τ = 2, 3, 5; Table 6 and Results 2 of the paper itself.
- **Fix.** "…is significant on both nulls at both estimators at every lag at which the lag-τ
  autocorrelation contrast is significant by sign-flip (τ = 1, 2, 3; the r₁ contrast's own
  phase-randomised p is 0.0729, Results 2) and null where it is not (τ = 5)". Add the phase p of the
  autocorrelation DiD to Table 6's column so the reader can see it. Existing outputs.
- **Confidence:** certain.

### F9 — the null's "9–14 %" holds only for q̂ distributions matched on three moments, and the paper does not say that the statistic is sensitive to the shape near zero

- **Severity:** MINOR
- **Location:** Results 4. "gives finite sampling a minor part (null δ_run +0.00029 to +0.00046,
  9–14 %)". Discussion: "finite sampling and pooling at a minor part each (9–14 % and 15 %)".
- **Problem.** The range is over six configurations that all solve the null to the data's run-level mean
  a, mean |q̂| and fraction |q̂| < 0.05 — which Methods states. But the sensitivity of this statistic
  to the shape of the q̂ density near zero is the reason a previous reading of it was withdrawn, and the
  record's own correction note of 16 September, 16:24 UTC, prints the span: +0.00003 with |q| = 0.19
  fixed, +0.00033–0.00039 for Gaussian q, +0.00053 for Laplace, +0.00071 for a 30 %-at-zero mixture,
  +0.00151 with every pair at q = 0 — 1 % to 44 % of the observed +0.00340. Those shapes are not
  matched on the third moment, so they are not competitors to the paper's configurations; but the paper
  reports a 9–14 % band without saying that the band is conditional on that matching, and that the
  statistic is a sign-weighted mean whose null value is driven by the pairs near q = 0. Separately the
  lower end is a rounding-up: 0.00029/0.00340 = 8.5 %, and the record's own shares are 0.085 to 0.135.
- **Evidence.** `manuscript/analysis_record.md`, "Correction note on the computations of 16 Sep 2026
  10:23 UTC", item (ii); `notes/planning_checks_2026-09-16/audit/audit_bundle15.log`;
  `crosslag_budget_null_tables.md` (a) F values 0.085, 0.092, 0.095, 0.105, 0.116, 0.135.
- **Fix.** "…gives finite sampling a minor part (null δ_run +0.00029 to +0.00046, 8.5–13.5 %, over
  six configurations all solved to the data's mean a, mean |q̂| and fraction |q̂| < 0.05; the
  statistic's null value depends on the density of q̂ near zero, and over q shapes not matched on that
  fraction it ranges from 1 % to 44 % of the observed value — record, correction note of 16 September)".
  Reads of existing outputs.
- **Confidence:** likely (the 8.5 % is certain; whether a referee would require the shape caveat is a
  judgement).

### F10 — an uncited reference

- **Severity:** MINOR
- **Location:** References. "Gatica, M., Atkinson-Clement, C., Mediano, P. A. M., … (2024). Transcranial
  ultrasound stimulation effect in the redundant and synergistic networks consistent across macaques."
- **Problem.** The entry appears nowhere in `draft_v2.md` outside the reference list, nor in
  `supplementary.md` or `supplementary_cobidas.md`. It is cited only in
  `notes/partB5_literature.md` (row 4 of the applicability table), which is pointed to from S3 but is not
  one of the manuscript files. A journal's reference check will flag it.
- **Evidence.** `grep -c Gatica` gives 1 in `draft_v2.md` (the entry itself) and 0 in both supplement
  files; the parsed in-text/reference-list cross-check found it and Luppi et al. (2026) as candidates,
  and Luppi (2026) is cited, in the compound "Luppi et al., 2024, 2026".
- **Fix.** Either cite it in the Discussion's applicability paragraph — it is the one TR 2 s, no-GSR,
  no-deconvolution, Gaussian-MMI row with a stated band, so it is the cleanest in-scope study — or move
  the entry to the supplement's own reference list when S3 becomes a supplementary file.
- **Confidence:** certain.

### F11 — Luppi et al. (2022)'s TR is stated as fact where the source table records it as not stated

- **Severity:** MINOR
- **Location:** Methods, "Literature search for the applicability table". "it places Luppi et al. (2022;
  TR 0.72 s) outside the pre-specified set, which the Discussion addresses."
- **Problem.** `notes/partB5_literature.md` row 1 records "TR not stated in the accessible text (HCP
  standard 0.72 s)", and the Discussion is explicit that the implied r₁ "takes the HCP TR of 0.72 s".
  Methods gives the inferred value without that qualification, and the study's exclusion from the
  pre-specified set rests on it. I could not find the TR in the accessible text either. The inference is
  safe — HCP resting-state fMRI is TR 0.72 s — but the paper is scrupulous about "not determined"
  everywhere else.
- **Evidence.** `notes/partB5_literature.md` row 1 and Table B item 2 ("for rows 1, 3, 5, 8 the band is
  not determined"); Luppi et al. (2022) article page, where the TR is not in the accessible text.
- **Fix.** "…it places Luppi et al. (2022) outside the pre-specified set at the HCP standard TR of
  0.72 s, which that paper's accessible text does not state (Supplement S3), and which the Discussion
  addresses."
- **Confidence:** certain.

### F12 — the budget "splits exactly" by construction, and ε is never defined

- **Severity:** MINOR
- **Location:** Methods, "The cross-lag deviation and its budget". "δ_run splits exactly: δ_run =
  δ_within + δ_pool + δ_means + ε, … δ_means = δ_run − δ_wd, with δ_wd the statistic after each
  region's mean is removed within each window and ε the boundary and standardisation remainder".
- **Problem.** δ_means is defined by difference and ε is not defined at all, so the identity is closed
  by construction and "splits exactly" (and Table S9's "Identity: … to 6.9 × 10⁻¹⁸") reports the
  arithmetic of a definition, not a derived decomposition. Only δ_within and δ_pool are constructed
  independently. `notes/rev_crosslag_budget.py` does define ε = δ_wd − δ_within − δ_pool; the paper
  does not, and calling it "the boundary and standardisation remainder" gives it a substantive reading
  a reader will take as tested rather than assumed. The ε values are small (−0.00002 on `ts_gsr`), so
  nothing turns on it — but the framing invites more confidence in the decomposition than it earns.
- **Evidence.** `notes/review_results/partB/crosslag_budget_tables.md` header ("δ_means = δ_run −
  δ_wd, … ε = δ_wd − δ_within − δ_pool"); `notes/rev_crosslag_budget.py`.
- **Fix.** "…δ_means = δ_run − δ_wd and ε = δ_wd − δ_within − δ_pool, the closing remainder,
  which collects the window-boundary and standardisation effects; δ_within and δ_pool are the two terms
  built independently, so the identity is exact by construction and the reading rests on their sizes,
  not on its exactness (|ε| ≤ 0.00002 here)."
- **Confidence:** certain.

### F13 — "sits at the ceiling"

- **Severity:** WORDING
- **Location:** Results 4. "The observed cross-half correlation of 0.32 sits at the ceiling and
  disattenuates to 0.82". Same phrasing in the Discussion.
- **Problem.** 0.319 against a ceiling of 0.386 is 83 % of it, not at it. The disattenuated 0.82 is
  correctly computed as 0.319/0.386, so the arithmetic is right and only the description overstates.
- **Evidence.** `splithalf_tables.md` reliability-ceiling block ("mean cross-half (disattenuated)
  +0.319 (+0.82)", ceiling 0.386); `checks/check_C1_residual_vs_null.log` section (3).
- **Fix.** "sits at 0.82 of the ceiling".
- **Confidence:** certain.

### F14 — Varley's hedge is dropped from the quotation's frame

- **Severity:** WORDING
- **Location:** Introduction. "He concludes that MMI "should probably not continue to be used in its
  current form" (Varley, 2024)."
- **Problem.** The quoted words are verbatim, but Varley frames them as a personal view: "Speaking just
  as a single author, I feel strongly that, despite its convenience and ease of computation, that the
  minimum mutual information function should probably not continue to be used in its current form."
  "He concludes" promotes an explicitly personal recommendation to a conclusion. Trivial in itself, and
  worth fixing only because this paper is otherwise exact about attribution.
- **Evidence.** Varley (2024), arXiv 2407.16601, full text.
- **Fix.** "He writes, "speaking just as a single author", that MMI "should probably not continue to be
  used in its current form"."
- **Confidence:** certain.

### F15 — "all of it finite sampling" has no antecedent

- **Severity:** WORDING
- **Location:** Results 4. "a shared-slow-component control puts 90 % there, a pooling control 30 %,
  all of it finite sampling".
- **Problem.** "all of it" can attach to the pooling control's 30 %, to both controls, or to the
  preceding 83–84 %. It is the first: in the pooling control the within-window term is +0.00040
  against the null's +0.00040, so that control's 30 % is entirely finite sampling.
- **Evidence.** `crosslag_budget_null_tables.md`, controls block, "(ii) pooling, mean over run types:
  … within +0.00040 … shares: within +0.303" against the primary null's within +0.00040.
- **Fix.** "…a pooling control 30 %, and in that control the within-window term is the null's, i.e.
  entirely finite sampling".
- **Confidence:** certain.

---

## 3b. Expert objections (item H of the brief)

### Three an author of the ΦID-on-fMRI literature would raise

**O1. "Your family is Markov of order one and has no lagged interaction, so it cannot contain synergy in
the sense the framework means; a result about it is a result about a degenerate case."** *Answered, in
Methods and in the Discussion's first two sentences of "What the finding is and is not", and the answer
holds where it is given.* The paper adds the coupled VAR(1) family, re-solves a and q_ε at each c so
that the operating point is held, and reports that lagged coupling moves sts at fixed (r₁, q) by
comparable amounts; it states that the map's q-axis "should not be read as 'the contribution of
interaction'", that no value of c is measured, and that a common slow drive and lagged coupling are the
same account at τ = 1 — which I verified is exactly true. Where the answer does not hold is the Abstract
and the sentence immediately after the caveat, which take the unconditional step anyway; that is F4.

**O2. "The atoms you analyse are estimated at about twenty effective samples, where you have shown the
estimator absorbs 15–45 % of a true difference; the object of your closed form is not the object your
data contain."** *Answered, and the answer is the paper's strongest section.* The bias simulations were
run before any windowed result, with analytic ground truth and the true sign recovered in every cell; the
matched-null family shows manufacture of either sign at −9 % to +16 % of the real DiD at W = 60 and up
to +33 % at W = 30; the global fit is characterised at ≤ 2 % in three of four pairs; Results 1 reports
that the identity's excess has the wrong sign on real BOLD and attributes it to the real ACF decaying
faster than any AR(1); Results 6 reconciles the three separate figures for the r₁-driven change
(−0.087, −0.0924, −0.069/−0.056) and says which question each answers. The one thing the answer
leaves out is that the windowed estimator's own exposure to the run's variance non-stationarity is larger
than the global fit's by the paper's own log; that is F3.

**O3. "You test MMI and CCS and then generalise to 'the estimator'; and your CCS is a Gaussian
continuous CCS with a masked double co-information that has no established reading, so your contrast
between the two is not informative about the framework."** *Answered, and unusually carefully.* The
Discussion states that I_min, I_BROJA and the dependency-based and information-geometric Gaussian
decompositions were not examined, that "MMI-specific" is therefore "not a licensed phrase", that CCS is
not offered as the corrected estimator, that CCS-sts has no scope map or null model and no established
reading, and that its value depends on which fifth sign the mask uses (−0.048 published against −0.039
`phyid`). Better: the CCS comparison was re-done under the published Definition 1/2 against `phyid`'s
different mask, under a rule fixed in the record before the run, and the published values are used
throughout because the rule's agreement threshold was crossed. The remaining gap is that the CCS-sts
non-tracking is a bound rather than a null — which Results 3 and the Abstract both say in terms.

### Two a statistician would raise

**O4. "N = 14, 474 inference rows, no multiplicity correction, and the only quantity with a genuine
pre-specification is the one that refuted its own hypothesis. Everything else is a garden of forking
paths."** *Answered by construction rather than by correction, and the construction is honest.* The
Multiplicity paragraph counts the rows, decomposes them, says which sets carry which null, states that no
correction is applied, and confines inferential weight to the pre-specified primary contrast and to
results clearing p ≤ 0.005 on both nulls across variants — and then discloses that this weighting rule
itself was written after every result it governs, names the commit and time, and says it has no record
entry. The Limitations repeat it. Two things a statistician would still press. The rule is a threshold on
two p-values and not a multiplicity procedure, so it controls nothing; and a rule written after the
results, however disclosed, selects. The paper's reply — that the rule is stated as a reporting
convention with its date, not as error control — is the right reply, and I would leave it, but the word
"weighting rule" should not be allowed to read as a correction.

**O5. "Your two headline quantities are two functions of the same 4 × 4 matrices estimated in the same
windows, so their agreement is not evidence about the world; and you know this, because you argue it
about a different pair of quantities two pages later."** *Not answered.* This is F1 and F3 together, and
it is the objection I would put first in a referee report. The paper has all the material to answer it —
the split-half machinery, both reliabilities, the odd/even halves, and the variance-ratio series — and
applies it to the residual/CCS pair alone. A statistician would also note that the residual DiD's test
re-splits the same 14 numbers that gave the observed DiD (Table 4's caption concedes this at the run
level), that the residual's phase null is by the paper's own statement not a null of the residual, and
that the finite-sample null is a review computation with no recorded rule and free choices that move its
value by a factor of two. Each of those three is stated somewhere in the paper; the 0.953 is the one
place where the same reasoning is not applied at all.

---

## 4. Number sweep

Every number in the Abstract and in Results 1, 3 and 4, and the numbers in Results 2, 5 and 6, the
tables, the supplement and the current caption strings as far as I traced them. "match" means the text
agrees with its source at the precision printed; rounding notes are given where the rounding is not
half-to-even at the last printed digit.

| number in text | location | source file | source value | match |
|---|---|---|---|---|
| sts = −ln(1−r₁²) + ½ln(1−r₁²q²) = xtx+yty+rtr | Abstract, Methods | derivation | reproduced to 2.4e-15 over 48 (a,q) settings | yes (`check_A1` §1) |
| four negative atoms balance the synergy block | Abstract, Results 1 | derivation | xts=yts=stx=sty=−(S−C) exactly | yes (`check_A1` §1) |
| 32-fold derivative ratio | Abstract | `family_checks.log` | 32.1 at (0.85, 0.25) | yes; single point — see F7 |
| ≈20 effective samples per 60-TR window | Abstract, Methods | ACF 0.868…−0.145 | 1+2Σ = 3.35 TRs; 60/3 ≈ 20 | yes |
| holds to 7 % | Abstract | Table 1 | (1.2398−1.1554)/1.2398 = 6.8 % | yes |
| −0.084 against rtr +0.039 | Abstract, Results 1 | `atoms_win60_…gsr` | 1.1554−1.2398 = −0.0844; rtr +0.0388 | yes |
| wrong sign by 0.12 nats | Results 1 | same | −0.0844 − 0.0388 = −0.1232 | yes |
| −0.053 at the global fit (1.3085 vs 1.3616) | Results 1 | `lag_tables.md` τ=1 global | 1.3085, 1.3616 | yes |
| Pearson r = 0.863, r² = 0.745 | Abstract, Results 2 | `regional_sts_r1_tables.md` | +0.863; 0.745 | yes |
| cortical Spearman 0.771, spin p < 0.0001 | Abstract, Results 2 | same | +0.771; 0.0000 | yes |
| Spearman +0.835 (115 regions) | Results 2 | same | +0.835 | yes |
| per subject +0.756 [+0.715, +0.790], 14/14 | Results 2 | same | identical | yes |
| regional r₁ range 0.8118–0.8742 | Results 2 | same | min 0.8118, max 0.8742 | yes |
| sts − rtr vs r₁ +0.792; cortical ρ +0.618, spin p < 0.0001 | Results 2 | same | +0.792; +0.618; 0.0000 | yes |
| rtr vs r₁ +0.638; cortical ρ +0.504, spin p = 0.0002 | Results 2 | same | +0.638; +0.504; 0.0002 | yes |
| SD 0.0098 against 0.0447 (a fifth) | Results 2 | same | 0.0098, 0.0447 | yes |
| ∂rtr/∂r₁ ≈ 0.06 | Results 2, Discussion | `family_checks.log` | +0.056 at (0.85,0.25); +0.064 at (0.97,0.25) | yes |
| DiD −0.0809 nats, p = 0.0038 | Abstract, Results 3, Tables 2, 6 | recomputed | −0.080866; 62/16384 = 0.003784 | yes (`check_B1` §1) |
| CI [−0.1261, −0.0377]; phase p 0.0020; 13/14 | Table 2 | `primary_b_ts_gsr_win60.csv` | identical | yes |
| −7.0 % of the pre-injection DMT mean | Results 3 | same | −0.080866/1.155377 = −7.00 % | yes |
| mean r₁ DiD −0.0146, p = 0.0106 | Abstract, Results 2 | `inference_rows_raw.csv` | −0.014645; 0.0106 | yes |
| [−0.0251, −0.0052]; 12/14; phase 0.0729 | Results 2 | same | identical | yes |
| FD-residualised r₁ −0.0123 [−0.0199, −0.0041], p 0.0135 | Results 2 | same | −0.01226 | yes |
| ts_demean r₁ −0.0216 [−0.0319, −0.0116], p 0.0017, phase 0.0390 | Results 2 | same | identical | yes |
| r = 0.953 per subject (Spearman 0.903) | Abstract, Results 3, Table 6 | recomputed | +0.9528; +0.9033 | yes (interpretation: F1) |
| 0.96 (0.93) on ts_demean | Results 3 | recomputed | +0.9578; +0.9253 | yes |
| leave-two-out 0.846–0.973, median 0.954, min without 8 and 14 | Results 3 | recomputed, `leave_two_out.log` | identical | yes (`check_B1` §2) |
| 28 condition × window means: 0.977 and 0.938 | Results 3 | `rev_extra.log` (b) | +0.977, +0.938 | yes |
| placebo carries 0.34 of the r₁ DiD (sts 0.40) | Results 3 | `inference_rows_raw.csv` | 0.3398; 0.4006 | yes |
| r₁ early −0.0213 p 0.0006; late −0.0093 p 0.1615 | Results 3 | same | identical | yes |
| 3.8 null SD vs 1.8 | Results 3 | same `phase_null_sd` | 3.77; 1.76 | yes |
| sts early −0.1029 p 0.0009; late −0.0633 p 0.0337 | Results 3 | same | identical | yes |
| placebo rise carries 0.69 of the late DiD | Results 3 | same | 0.6851 | yes |
| trend corrections −0.0890 p 0.0021; −0.0995 p 0.0007 | Results 3 | same | identical | yes |
| W = 30 −0.0686 [−0.1084, −0.0293], p 0.0042 | Results 3 | `primary_b_ts_gsr_win30.csv` | −0.068626; 0.004150 | yes |
| global fit −0.0801 [−0.1303, −0.0310], p 0.0071 | Results 3 | `global_fc_did_ts_gsr.csv` | −0.080081; identical CI | yes |
| ts_demean −0.1031 [−0.1558, −0.0522], p 0.0026 | Table 2 | `primary_b_ts_demean_win60.csv` | identical | yes |
| 28 leave-one-out refits | Results 3 | `loo_did_win60.csv` | 14 subjects × 2 variants = 28 | yes |
| ratio DiDs +0.0005/−0.0095/+0.0071/+0.0204 with CIs and p | Results 3, Table S8 | `proportionality.csv` | identical in all four cells | yes |
| 0.66 [0.49, 0.82] against baseline 0.91 | Results 3 | same | 0.6584 [0.4864, 0.8174]; 0.9082 | yes |
| 0.99 and 0.98 (1.2588 of 1.2819) on the family | Results 3 | derivation | 0.9909; 0.9820 | yes (`check_A1` §3) |
| sts carries 0.78 of TDMI and 0.78 [0.65, 0.94] of its DiD | Results 3 | `proportionality.csv` | 0.7820; 0.7797 [0.6531, 0.9362] | yes |
| CCS-sts level −0.0480, 4 % of MMI | Results 1 | `ccs_pub_tables.md` | −0.0480; 4.15 % | yes |
| phyid mask −0.0387; DiDs +0.0036 vs +0.0044; r = 0.974 | Results 1 | same | identical | yes |
| mask selects 35–38 % (0.351, 0.365, 0.366, 0.384) | Results 1 | same | identical | yes |
| 32–34 % vs code 26–28 %; disagree 6–7 % | Results 1 | `ccs_definition_check.log` §0 | 0.320/0.337; 0.264/0.280; 0.063/0.066 | yes |
| level differences 0.002–0.012 nats | Results 1 | `ccs_pub_tables.md` | ts_demean W60 −0.0122 is the largest | yes |
| all sixteen MMI levels and DiDs with negative counts | Table 1 | recomputed from the atoms array | every cell identical | yes (`check_B1` §1) |
| block +2.289 against −2.142; net −0.0017; TDMI −0.1037 | Results 1 | same | 2.2890; −2.1417; −0.0017; −0.10372 | yes |
| pair-level r₁ correlations +0.742, +0.697 (CCS −0.011, −0.018) | Results 2, 3 | `ccs_pub_tables.md` | identical | yes |
| r² = 0.55, 0.49 | Results 2 | derived | 0.5506, 0.4858 | yes |
| 28 group means: CCS −0.639 vs MMI +0.977 | Results 3 | same | identical | yes |
| CCS DiD/r₁ DiD −0.420, −0.275, −0.428, −0.297; all p ≥ 0.127 | Results 3, Table 3 | same | identical; min p 0.127 | yes |
| CCS xtx+yty DiD/r₁ DiD 0.949, 0.963, 0.917, 0.921 | Results 3 | same | identical | yes |
| CCS-sts +0.0044 [+0.0004, +0.0081], p 0.0559, phase 0.006, 11/14 | Results 3, Table 3 | `inference_rows_ccs_pub` | identical | yes |
| CCS-sts global +0.0197 … p 0.0002, phase 0.001, 13/14 | Results 3, Table 3 | same | identical | yes |
| ts_demean CCS-sts +0.0120 p 0.0040; +0.0355 p 0.0001, 14/14 | Results 3 | same | identical | yes |
| ΦR +0.0007 [−0.0078, +0.0100], p 0.8971, phase 0.8372 | Results 3, Table 3 | `inference_rows_raw` | identical | yes |
| ΦR other three cells | Table 3 | same | identical | yes |
| variance ratio 1.28 → 0.89; 0.94 → 1.06 | Results 3, 4, 6 | `rev_extra.log` (d) | 1.277/0.889; 0.936/1.062 | yes |
| global-fit sts bins vs ratio +0.37 | Results 6 | `review_computations` §1 | +0.37 (range −0.53 to +0.75) | yes; incomplete — F3 |
| level 1.1377, predicted 1.1865, residual −0.0489 (−4.3 %) | Abstract, Results 4, Table 4 | `diag_tables.md`, npz | identical | yes |
| run level 1.2883 / 1.3021, −0.0137 (−1.1 %) | Results 4, Table 4 | same | identical | yes |
| symmetric variant over-predicts by 16 % | Results 4 | `diag_tables.md` (1.3212) | +16.1 % | yes |
| residual SD a fifth of observed across 392 cells | Results 4 | npz | 0.0161/0.0790 = 0.204; 14×2×14 = 392 | yes |
| predicted DiD −0.0924, 114 %, r = 0.989 | Abstract, Results 4, 6 | recomputed | −0.09239; 1.1426; +0.9893 | yes |
| over-shoots by 14–29 %; tracks at 0.98–0.99 | Results 4 | `diag_tables.md` | 114/127/118/129 %; 0.989/0.987/0.990/0.981 | yes |
| residual DiD +0.0115 [+0.0021, +0.0211], p 0.042, 4/14 | Abstract, Results 4, Table 4 | recomputed | +0.01153; p 0.0422 | yes |
| early +0.0179 [+0.0099, +0.0260] p 0.0012 phase 0.003, 12/14 | Results 4 | `inference_rows_diag` | +0.01791; 0.0012 | yes |
| late +0.0064, p 0.32 | Results 4 | same | +0.00642; 0.3243 | yes |
| DMT +0.0077 [−0.0001, +0.0149] p 0.080; PCB −0.0038 … p 0.19 | Results 4 | recomputed | +0.00771 p 0.080; −0.00382 p 0.193 | yes |
| placebo contributes 0.33 of the DiD | Results 4 | `inference_rows_diag` | 0.331 | yes |
| r(residual DiD, r₁ DiD) = −0.780 | Results 4, Table 4 | recomputed | −0.7804 | yes |
| cross-lag substitution alone −0.0489 of −0.0489 | Results 4 | `residual_source.log` | 1.1866 vs 1.1865 | yes |
| signed mean offset +0.00014 | Results 4 | same | +0.00014 | yes |
| R² = 0.74 on pair a, |q| and the cross-lag scatter | Results 4 | same | 0.744 | yes |
| null level −0.035 (−3.0 %); homogeneous −3.1 %; −8.5 % / −0.34 % | Results 4, Table 4 | `review_v2_residual_null.log` | four-cell mean −0.0345/−2.95 %; −3.10 %; −8.52 %; −0.34 % | yes |
| null DiD +0.0054 (DMT +0.0041, PCB −0.0013) | Results 4, Table 4 | same | identical | yes |
| range +0.0037 to +0.0077 (0.0059, 0.0052, 0.0077, 0.0037) | Results 4, Table 4 | third review, Appendix comp. 3 | as quoted | yes |
| a third to two-thirds of +0.0115 | Abstract, Results 4 | derived | 32 % and 67 % | yes; reading — F2 |
| δ_run +0.00340 [+0.00300, +0.00380], 14/14; DMT +0.00381, PCB +0.00299 | Results 4, Table S9 | `crosslag_budget_tables.md` | identical | yes |
| 44 % at the operating point | Results 4 | record + derivation | −0.00605/0.0137 = 44.2 % | yes (`check_C1` §4) |
| 37 % at "the pairs' mean point" | Results 4 | record (0.8666, 0.1945) | −0.00507/0.0137 = 37.0 % | yes; point undefined — F6 |
| 54.5 % of pairs have q < 0 | Results 4, Limitations | `crosslag_budget_tables.md` | 0.545 | yes |
| null δ_run +0.00029 to +0.00046, 9–14 % | Results 4, Discussion | `crosslag_budget_null_tables.md` | 0.085–0.135 | value yes; 8.5 rounded up — F9 |
| null-corrected +0.00301 [+0.00261, +0.00340] | Results 4, Table S9 | same | identical | yes |
| δ_within +0.00250, 83–84 % | Results 4, Table S9 | same | 0.833–0.839 | yes |
| δ_pool +0.00046, 15 %; δ_means +0.00004 | Results 4, Table S9 | same | 0.154; +0.00004 | yes |
| controls 90 % / 30 % | Results 4 | same | 0.898; 0.303 | yes; wording — F15 |
| pooling DMT − placebo +0.00039, p 0.0006, 12/14, 11 % of +0.00349 | Results 4 | same (e) k = 0 | identical | yes |
| ts_demean δ_run −0.00262 [−0.00495, −0.00037] | Results 4, Discussion, Table S9 | `crosslag_budget_tables.md` | identical | yes |
| r(residual DiD, CCS-sts DiD) +0.799 / +0.875 | Abstract, Results 4 | recomputed | +0.7993 (p 0.0006); +0.875 | yes |
| partial r +0.83 and +0.86; phyid +0.69 and +0.82 | Results 4 | third review comp. 4; recomputed +0.8313 | yes |
| within-half +0.847/+0.783 (0.815); cross +0.160/+0.478 (0.319, 0.39) | Results 4, Table 5 | `splithalf_tables.md` | identical | yes |
| partialled +0.815 / +0.154 | Results 4, Table 5 | same | identical | yes |
| ts_demean +0.881 within / +0.283 across (0.32) | Results 4 | same | +0.884/+0.878; +0.274/+0.292 | yes |
| reliabilities 0.49, 0.30; 0.22, 0.42; r₁ and sts 0.71–0.74, 0.69–0.72 | Results 4, Table 5 | same | 0.494, 0.302; 0.216, 0.417; 0.741/0.712, 0.717/0.686 | yes |
| ceiling √(0.494 × 0.302) = 0.39; threshold 0.41; 0.30 / 0.44 | Results 4, Table 5 | same | 0.386; 0.407; 0.304; 0.440 | yes |
| cross-half p 0.59 and 0.08 | Results 4 | derived | 0.585, 0.084 | yes |
| disattenuates to 0.82 | Results 4 | same | 0.319/0.386 = 0.826 | yes; "at the ceiling" — F13 |
| half-group means: residual +0.0067/+0.0164; CCS +0.0033/+0.0054 | Results 4 | `splithalf_tables.md` | identical | yes |
| gap 0.1531 nats (1.1554 vs 1.3085) | Results 6 | Tables 1, `lag_tables.md` | 0.1531 | yes |
| τ table: r_τ 0.848/0.513/0.139/−0.202; levels; DiDs; CIs; p; phase p | Table 6 | `lag_tables.md` | every cell identical | yes |
| r(sts DiD, r_τ DiD) +0.953/+0.970/+0.626/−0.832 | Table 6 | same | identical | yes |
| global-fit τ DiDs and CIs | Table 6 | same | identical (CI draw order flagged in the caption) | yes |
| r₃ contrast −0.0681; τ = 3 tracking 0.626 (0.885 global) | Results 5 | same | identical | yes |
| spectral centroid 0.0369 / 0.0374 Hz; DiD +0.0023 [+0.0006, +0.0040] p 0.022, 12/14 | Results 2, 5 | `rev_extra.log` (c) | 0.0369, 0.0374; +0.00231 [+0.00060, +0.00395], 0.0217 | yes |
| ideal band-pass 0.82 vs measured 0.866 | Methods, Results 2 | `rev_extra.log` (c), `family_checks.log` | 0.8176; 0.8661 | yes |
| ideal r₁ 0.78–0.93 across studies with stated settings | Results 2 | `partB5_literature.md` Table B item 2 | "for the rows with a stated band and TR (2, 4, 6, 7) … 0.78–0.93" | yes |
| ratio 25–60 at |q| = 0.25; 131 at 0.97 | Results 2 | `family_checks.log`; derivation | 24.9, 60.0; 131.1 | yes (`check_A1` §3) |
| pair r₁ medians 0.816–0.867; median |q| 0.22–0.41 | Results 2 | `partB1_scope_map.md` item 4 | 0.840–0.867 and 0.816–0.860; 0.22–0.31 and 0.23–0.41 | yes |
| operating point derivatives 6.07 / −0.19 (32); 5.71 / −0.59 (10) | Results 2 | derivation | 6.0705/−0.1891 (32.09); 5.7126/−0.5859 (9.75) | yes |
| minimum ratio 6.55 at (0.61, ±0.6); 1.9 at (0.77, ±0.95) | Results 2 | derivation | 6.553; 1.889 | yes (`check_A1` §4) |
| 0 of 18,336; 0 of 36,481 | Results 2 | derivation | 0 and 0 (191 exact ties on r₁ = 0) | yes (`check_A1` §4) |
| sts at q = 0: 0.041, 0.446, 1.022, 1.282, 1.661, 2.328 | Results 2 | derivation | identical to 4 d.p. | yes |
| 1.282 → 1.131 as |q| → 0.6 | Results 2 | derivation | 1.28185 → 1.13123 | yes |
| (0.848, 0.24): ∂sts/∂r₁ = 5.99; maps to −0.087 | Results 2 | derivation | 5.9869; −0.0874 | yes |
| |q| 0.284 → 0.266 vs 0.284 → 0.282; DiD −0.0164 | Results 2 | `residual_source.log` | identical | yes |
| ts_demean mean r 0.190 → 0.233; DiD +0.0526 [+0.0073, +0.0976] p 0.0470, 28 % | Results 2 | `global_fc_did_ts_demean.csv`, Table S7 | 0.1905; identical | yes |
| ∂sts/∂q −0.15 to −0.23 at r₁ 0.84, q 0.2–0.3 | Results 2 | derivation | −0.1452, −0.2260 | yes |
| coupled family: slope −1.77, curvature +40; rows 1.2315/1.3023/1.2155/1.4111 vs 1.2588 | Methods | `coupling_map_tables.md` | −1.771, +40.3; identical rows | yes (`check_A1` §6) |
| cross-lag departs from a_y q by ≈ 0.94c | Methods | derivation | c(1−q²) = 0.9375c at q = 0.25 | yes |
| worked example: q 0.25, a 0.8375, cross-lag 0.2375, d +0.028125; a 0.83, c 0.03, q_ε 0.093 | Methods | derivation | identical; q_ε = 0.09320 | yes (`check_A1` §5) |
| matched null −9 %, +16 %, +7 % ± 8 %, −8 % ± 6 %; +33 % at W30; ≤ 2 % at 840 except +29 % | Results 6 | `sts_matched_null_F{1,2,3}.log` | identical | yes |
| true change −0.069; estimator returns −0.056 | Results 6 | `sts_matched_null_F3.log` (F3-c) | −0.0688; −0.0557 | yes |
| ≈ +0.07 nats per +0.01 near 0.87 | Results 6 | derivation | 0.0710 | yes |
| 52–77 % absorbed at W30; 15–45 % at W60; true sign in every cell | Methods | `bias_check.csv` | 52.2–77.0 %; 15.1–45.1 %; sign matches in all 12 | yes (recomputed) |
| pooled placebo ACF lags 1–6 | Methods | `review_v2_residual_null.log` targets | 0.868, 0.539, 0.172, −0.085, −0.174, −0.145 | yes |
| filter fit lags 1–6 (0.872 … −0.168) | Methods | same | identical | yes |
| 474 rows = 79 × 6; 186 + 288; 316 + 158 | Methods | arithmetic | all three identities hold | yes |
| 115 regions, 6,555 pairs | Methods | 115 × 114 / 2 | 6,555 | yes |
| closed form reproduces phyid to ≤ 2.1e-14 / 1.1e-13 | Methods | `phiid_fast_validate.log` | as stated | yes |
| rtr fell by a tenth of the sts fall (−0.0078 vs −0.0809); family a hundredth | Discussion | Table 1; derivation | 0.0964; 0.0092 | yes |
| deconvolution takes r₁ from 0.87 to 0.79 | Discussion | `partB5_literature.md` Table B item 4 | 0.866 → 0.790 | yes |
| Table S1, S7, S8, S9 cells | supplement | the named source files | every cell I traced identical | yes |
| Figure 1–5 caption numbers (current strings) | `15_figures_v2.py` | the saved files they read | computed from the same arrays | yes |

---

## 5. Checked and sound

- **The analytic account, independently.** I implemented the Gaussian ΦID product lattice with the MMI
  redundancy function and the Möbius inversion from the definitions, not from `rev_phiid_fast.py`, and
  cross-checked it against `phyid` at the pinned commit on simulated AR(1) pairs (max |difference| over
  the sixteen atoms 6.0e-15). On the family as Methods defines it, all sixteen atoms match the paper's
  statement to 2.4e-15 over 48 (a, q) settings: rtx = rty = xtr = ytr = xty = ytx = 0; xtx = yty = rts =
  str = S − C; xts = yts = stx = sty = −(S − C); rtr = C; sts = 2S − C. So do sts = xtx + yty + rtr,
  sts − (xtx + yty) = rtr, rtr + sts = TDMI, ΦR = rtr on the symmetric family (and ΦR ≠ rtr for
  a_x ≠ a_y), TDMI = −ln(1 − a²) independent of q, ∂rtr/∂q = −∂sts/∂q, and Varley's aggregate
  str + stx + sty + sts = S. The two derivatives are exactly as printed, and the lattice's numerical
  derivatives agree with them. The paper's statement of the family is unambiguous: the innovation
  correlation q equals corr(x_t, y_t) for this parameterisation, which is what makes the S₄ of Methods
  correct.
- **The derivative-ratio figures.** The grids are exactly 96 × 121, 96 × 191 = 18,336 and
  191 × 191 = 36,481; no grid point has |∂sts/∂q| > |∂sts/∂r₁|; the only ties are the 191 points
  of the line r₁ = 0, where both derivatives vanish. The Figure 2(c) minima are 6.553 at (0.61, ±0.60)
  and 1.889 at (0.77, ±0.95), printed as 6.55 and 1.9. Every ratio the paper quotes (32, 10, 25, 60,
  131, 32.8) reproduces.
- **The shared-slow-component formula and the τ = 1 claim.** d(x→y) = q(1 − λ_y)(a_s − a_n) is exact
  (worked example to 2.8e-17), the worked example's 4 × 4 is bit-identical to the symmetric VAR(1) with
  a = 0.83, c = 0.03, q_ε = 0.0932, and the two give the same sixteen atoms to 2.0e-15. The general
  claim holds: over 10,017 random positive-definite stationary 4 × 4 blocks, A = Γ₁Γ₀⁻¹ always gave a
  positive-definite innovation covariance and a spectral radius below 1, so every such matrix is
  realisable as a stationary VAR(1) and the τ = 1 atoms coincide. (One fine caveat the paper does not
  need to state: the coincidence of *CCS*-sts requires the shared-component process to be jointly
  Gaussian, since the CCS mask is evaluated per sample; with Gaussian parts it is.)
- **The DMT inference.** The primary DiD, all sixteen atom levels and DiDs with their negative counts,
  TDMI, the exact 16,384-assignment sign-flip p, the subject bootstrap, the per-subject collinearity, the
  91 leave-two-out refits, the residual diagnostic's three series and their DiDs, and the residual/CCS
  relations all reproduce from the committed arrays and `did_subjects` fields (max |difference| from the
  pickled per-subject DiDs 6.7e-16). The observed = predicted + residual identity is exact to 0.0 over
  the 392 cells.
- **Code against Methods.** 840 TRs; `WINDOW_TRS = 60`, `WINDOW_STRIDE = WINDOW_TRS`, asserted to divide
  840, `N_WINDOWS = 14` — non-overlapping, as stated; W = 30 gives 28 windows; `TAU = 1`,
  `KIND = "gaussian"`, `REDUNDANCY = "MMI"`, `calc_PhiID` called per pair per window;
  `EXCLUDE_REGIONS = (20,)` applied before any result, with an assertion that stops the run if any other
  region is constant; pre = windows 1–4, primary = 6–14, sensitivity = 5–14, early = 6–9, late =
  10–14, exactly as Methods says and as `rev_inference.window_sets` encodes; DiD = (post − pre)_DMT −
  (post − pre)_PCB with condition index 0 = DMT, matching the source `.mat` ordering the script cites;
  sign-flip over all 2¹⁴ sign assignments, two-sided, bootstrap 10,000 draws, phase-randomised p as
  (count + 1)/(N + 1); the r₁ series standardised within each window with ddof = 1, so its window mean is
  the standard sample lag-1 autocorrelation; seed 20261120 throughout. The spin test uses Vasa rotations
  of the 100 Schaefer parcels with region 20 NaN, so 99 cortical parcels, and the paper and `CLAUDE.md`
  rule 1 both scope it that way — the 115-region correlations are reported without a p.
- **The budget.** The identity closes to 6.9e-18 in the source (trivially, see F12), the null-corrected
  terms, shares and labels in Table S9 match `crosslag_budget_null_tables.md` cell for cell, and my
  independent ∂sts/∂(cross-lag) reproduces `reviewer/v_slope_q.log` to three decimals at a = 0.867
  (−0.157, −0.393, −0.793, −1.546, −2.090, −3.720) — a second, unplanned cross-validation of my
  lattice against the project's own.
- **Circularity of the residual.** The paper is right that the residual is not an independent test and
  says so in the places it matters: Results 3 distinguishes the 9 % from the residual ("its significance
  is not a test of that 9 %"), Table 4's caption says the run-level residual DiD "equals the observed DiD
  by construction", Methods flags that the residual's phase-randomised null is a null of the observed
  series and not of the residual's construction, and Results 4 states that the same correlations are
  predicted by both candidate accounts. The predicted and residual DiDs are an exact algebraic split of
  the observed DiD across the same 14 subjects, which the paper never presents as new evidence.
- **The pre-specification audit.** Every result the paper calls pre-specified, predicted or recorded
  before the test has a dated record entry that precedes it, and — the stronger test — the outputs carry
  the SHA of the commit that contains the entry: `regional_sts_r1_tables.md` "git=152cc6d" against the
  pre-run entry committed in 152cc6d; `crosslag_budget_tables.md` and `crosslag_budget_null_tables.md`
  "git=6b5181a" against the 16:24 UTC entry; `crosslag_deviation_tables.md` "git=9a19b10". The record
  discloses the one cosmetic inversion (a heading time of 15:35 UTC on a commit of 15:31). Everything
  post-hoc is labelled post-hoc where it appears (the early/late sets, the two trend corrections,
  proportionality, LOO, deconvolution, the |q| DiD, the `ts_demean` mean-r rise, the symmetric-coefficient
  variant, the CCS-sts increase, ΦR, the matched null, the lag variants). The CCS-sts increase is
  labelled exploratory in the Abstract, in Results 3, in Table 3's caption and in the Discussion, and the
  reasons for not reading it are given as two reasons and one rule. The study's history is told at
  length and against itself: that the confirmatory test was of a different hypothesis, that the
  directional-failure rule was written after the 115-region decrease was known and entered git in the
  same commit as that result, that the hypothesis's precedence rests on document order rather than a
  commit, that the Part B plans postdate the review computations that characterised the phenomenon, and
  that the weighting rule is a write-up convention with no record entry. I could not find a reader-facing
  sentence that would let the present analysis be mistaken for the original plan.
- **Literature.** Varley (2024): the quoted words are verbatim; Eq. 12 is I_Syn(X^⊥) = I(X²_t; X²_{t+1}),
  i.e. the MMI synergy of the disintegrated pair equals one process's self-information, exactly as
  attributed; Eq. 13 is ΔI_Syn = I(X¹_t; X²_t) − I(X¹_t; X_{t+1} | X²_t), so the change on
  disintegration does depend on the instantaneous mutual information; r = 0.97 with pairwise mutual
  information on 1,000 region pairs is verbatim; the quantity is the aggregate forward synergy
  I(X_t; X_{t+1}) − max_i I(X^i_t; X_{t+1}), which on this family equals str + stx + sty + sts, as the
  paper's translation says. The paper's parenthetical that Eq. 12's derivation is "general rather than
  discrete-only" is its own argument, and it is correct (the derivation uses only additivity under
  independence and the MMI minimum); Varley presents his framework for discrete distributions and notes
  an extension to differential mutual information, so a reader could take the generality as Varley's —
  the "derived from" clause just about carries it. Barrett (2015): R_MMI = min{I(X;Y), I(X;Z)} verbatim,
  and Example 1 exhibits positive whole-minus-sum synergy, ½log(1 + α⁴) > 0, with the target's own
  lagged past as a source — exactly as attributed; his uniqueness result is for univariate targets, and
  the paper does not overreach on it. Mediano et al. (2021): the Appendix's Definition 1 is the CCS
  double-redundancy, and its sign condition is verbatim "the subset of samples for which all marginal
  pointwise mutual informations, as well as the pointwise full mutual information i(x; y), have the same
  sign"; the identity c(x; y) = i_∂^{{1}{2}→{1}{2}} − i_∂^{{12}→{12}} is stated there; ΦR adds the
  double redundancy to whole-minus-sum; and the worked coupled AR example is at a = 0.4 with ΦWMS and
  ΦR plotted against the noise correlation — all four as the paper says. Liardi et al. (2025): the null
  preserves total mutual information, it is PID and not ΦID, the data are MEG, and the samples are
  N = 15 / 19 / 14 — the Discussion's characterisation is exact. Faes et al. (2025): authors, PRL 135,
  187401 (2025) and the arXiv number are right, and the paper does identify PID's application to time
  series as giving "an incomplete and sometimes misleading depiction" and proposes a rate decomposition;
  the gloss "under an implicit i.i.d. assumption" is the paper's paraphrase. Ince (2017): the published
  version does evaluate the pointwise terms under a maximum-entropy distribution, as Methods says.
  Luppi et al. (2022): redundancy in sensorimotor and synergy in higher-order networks, as attributed;
  HRF deconvolution used. Luppi et al. (2024): the workspace, ΦR reduced under propofol and in DoC, ΦR
  and not sts as the contrasted quantity, and the version-of-record date (18 July 2024, v4) all check
  out. Singleton et al. (2025): "20 mg DMT (in fumarate form …) injected over 30 s"; the intensity
  ratings "obtained during a separate fMRI" and given at the end of every minute (30 TRs at TR 2 s, 28
  bins); "the National Research Ethics (NRES) Committee London – Brent and the Health Research
  Authority", which the Ethics statement follows. In-text citations and the reference list match except
  for F10.
- **Statements.** Data availability points at the right upstream repository, Zenodo DOI and commit, and
  `run_all.sh` does contain a section 6 with every `notes/` script the sentence names, including
  `partB10`, `partB11`, `partB12`, `partB13` and `scripts/15_figures_v2.py`, in a workable order; the
  claim that the section "has not yet been executed end-to-end as one run" is literally true and the
  record's end-to-end entry explains exactly why (the two invocations split inside section 6) rather than
  papering over it. The conflict-of-interest statement discloses the Cambridge application and names the
  group whose estimator the paper analyses, which is the disclosure a reader needs; `CLAUDE.md` rule 10
  is respected — the licensed dissociation is not asserted anywhere in draft_v2. The AI-use statement is
  specific about what the system did and who is responsible. The Ethics statement correctly says it
  follows Timmermann et al. (2023) and flags the missing reference number as a [TK].
- **Figures.** All five are legible at print size. Panel letters, axis labels and units are present
  throughout; colour pairs are blue/orange (Figure 1) and red/blue (Figure 4), both safe for the common
  dichromacies, and Figure 2(c) uses a perceptually ordered sequential map with numbered contours.
  Figure 4(b)'s claim to be on "the same nats per unit height" as 4(a) is true: I measured the rendered
  axes boxes at 2843 and 2850 px per nat, a ratio of 1.0023 (`check_I1_fig4_scale.log`) — my eyeball
  said otherwise and was wrong. Figure 4's injection line at 8 min, its grey pre-injection band (0–8
  min) and its hatched excluded window 5 (8–10 min) are all consistent with TR 240 at TR = 2 s and with
  the window sets. Figure 3(a) shows subjects 8 and 14 as the two extremes, which is what the
  leave-two-out identifies, and the caption carries the leave-two-out range; the correlation among the
  other 12 is still 0.846, so the relation is not purely leverage. The current caption strings in
  `scripts/15_figures_v2.py` describe what each figure shows, state the grid step as 0.01 (matching
  Methods), state that Figure 1(a) carries no uncertainty and why, and define the ± 1 within-subject
  (Cousineau–Morey) bands of Figure 4 including the Morey factor.

---

## 6. Not checked, and why

- **Nothing was recomputed from the time series.** `external/` is absent from this copy and the rules
  forbid `run_all.sh` and the scripts, so the atoms, the r₁ series, the CCS masks, the per-pair
  predictions, the bias simulations, the matched null, the two finite-sample nulls, the spin test and all
  phase-randomised nulls were taken from the committed outputs. My checks re-derive the analytic layer
  and re-run the *inference* on committed per-subject values; they do not verify the estimation.
- **Timmermann et al. (2023).** Unreachable (PNAS returned 403 to both the article and the PDF; the PMC
  and eScholarship routes returned other content or the abstract only). So the Ethics statement's
  additional clauses (Declaration of Helsinki 2000, ICH GCP, NHS Research Governance Framework, Imperial
  College London as sponsor, the Home Office Schedule 1 licence, written informed consent), the 3 T
  field strength, the 840 TRs at TR 2 s with injection at TR 240, the "six of twenty participants …
  excluded by the source authors for head movement", and "a second, later session of the same day" are
  **unverified** beyond what Singleton et al. (2025)'s accessible text confirms (the committee and HRA
  wording, the 20 mg over 30 s, the separate rating session at one rating per minute, and 14 analysed
  subjects).
- **Mediano et al. (2025) PNAS SI Appendix.** The PMC copy returned a reCAPTCHA page. Definition 2 and
  the "checked 15 September 2026" claim that it "retains the definition verbatim on the sign condition"
  are therefore **unverified**; I verified the identical Definition 1 and its sign condition in the arXiv
  (2021) Appendix instead, which is the definition the computation implements.
- **Luppi et al. (2022) Fig. S1D**, its band-pass and its lag. Not in the accessible text; the paper's
  own source note quotes the replication-without-deconvolution sentence from what it could read, and I
  could not confirm the figure number.
- **Ince (2017) preprint vs published.** I confirmed that the published version uses a maximum-entropy
  distribution, but not that the original preprint did not — so Methods' "as in Ince's original
  preprint" is unverified.
- **The git history before b4f98a8.** `.git-bundles` are incremental and the first lacks its prerequisite
  commit (a226593b), so the history could not be reconstructed; the early commit times (44cec4f,
  33f0b33, 84ea657, febf599, cb1b2cf, e16ebba, e46df8a) are as the record states them and I could not
  check them against git. I ran no mutating git command.
- **Files newer than the commit.** `results/bias_check.csv`, `bias_check_differential.csv`,
  `run_00_verify.log`, `run_02_bias_check_n20000.log` and `run_all_full.log` have modification times
  about 18 hours after `draft_v2.md`'s, i.e. they belong to the run now in progress rather than to
  56df014. I used `bias_check.csv` anyway and its numbers still reproduce the paper's 52–77 % and
  15–45 %; the rest I left alone.
- **Scope.** I traced only the inference rows the paper names, not all 474; Tables S2–S6 (the superseded
  analysis) only as far as their source lines; `supplementary_cobidas.md` was read but not audited item by
  item; `notes/companion_plain_language.md` was searched, not read in full; the [TK] placeholders, the
  stale `captions_v2.md`, the participant codes in the git history and the queued CCS-sts Abstract
  bracket were excluded as instructed, and I see no reason to question the planned handling of any of
  them.
- **Venue.** `notes/venue_options.md` records abstract limits of 250 (NeuroImage), 200 (Network
  Neuroscience) and 300 (PLOS Computational Biology) words; at 319 the Abstract exceeds all three. That
  is the venue-specific item the brief excludes, and F4's addition makes it longer, so the cut will have
  to come from elsewhere — I would take it from the CCS and split-half sentences, which the Results carry
  in full.

---

## 7. Phase 2: findings dropped or added

I wrote my findings to `phase1_findings.md` (P1–P15) before opening
`notes/adversarial_review_*.md`, `notes/verification_correction_note_2026-09-15.md`,
`notes/companion_plain_language.md`, `notes/defence_questions.md`,
`notes/planning_checks_2026-09-16/` and `CLAUDE.md`.

**Dropped: none.** Two of my Phase 1 points were candidates for dropping, and neither survives the test
that the paper's current text resolves it.

- **P2** (residual DiD's "rest") is finding 1d of `adversarial_review_draft_v2_second_pass_2026-09-15.md`:
  "(i) For the DiD, 'the observed interval contains the null value' and 'the other half … [is] a
  systematic departure' cannot both be claimed; the first is true. (ii) … no uncertainty is attached to
  the null value or to the run-level residual (−0.0137, a mean over runs reported without a CI in
  `diag_tables.md`)." `verification_correction_note_2026-09-15.md` dispositions it as "Addressed on (i)
  and (iii); partial on (ii) … Not done from 1d(ii): no uncertainty on the null value … and no CI on
  the run-level residual −0.0137." The current text adds the concession ("the observed interval contains
  every one of those values") and then still asserts "The rest … are not accounted for by the null as
  specified", and still gives no interval. So (i) is half-resolved — the concession is present, the
  contradicting claim is too — and (ii) is not resolved at all. **Kept, and narrowed** to those two
  points, with the run-level bootstrap supplied (my check shows that claim *is* supported, which the
  paper should say).
- **P12/F13** ("sits at the ceiling") is the third review's item 3.2 territory and
  `verification_correction_note_2026-09-15.md` §3 item 2 flags a related confusion of two numbers both
  printed as 0.82. The current text fixed that confusion but kept "sits at the ceiling". **Kept, as
  WORDING.**

**Added, or strengthened, because an earlier point was accepted and the text does not reflect it.**

1. **F5 strengthened.** `notes/adversarial_review_2026-09-14.md` item 11 already raised it in its narrow
   form: "Methods says every results table 'carries the git SHA of the code that produced it'; four
   tables carry `-dirty` SHAs". `CLAUDE.md` standing rule 8 requires "git SHA in every output header",
   and `notes/defence_questions.md` still answers a referee with "every results table carries the git
   SHA that produced it". The `-dirty` case is unfixed a year of revisions later, and the larger case —
   26 of 30 Part B and review result files with no SHA anywhere — was never raised. Reason for adding:
   an accepted point that the text still contradicts, now with a bigger denominator.
2. **F1 confirmed as new.** No review, the verification note, the companion or the defence questions
   applies the reliability ceiling to the 0.953; the ceiling appears only in connection with the
   residual/CCS pair. The third review's 8.2 asked for "leave-two-out r beside 0.95" and for the
   odd/even-TR design, both of which the current text now has — so the *leverage* question is answered
   and the *shared-noise* question was never asked.
3. **F3 confirmed as new.** The +0.37 figure entered the paper from the third review's 1g, which quoted
   it for the global-fit bins only; neither that review nor any later note reports the windowed +0.49 /
   +0.54 per run or +0.77 / +0.73 group-mean figures that sit in the same section of
   `review_computations_2026-09-14.md`.
4. **F4 confirmed as new, and dated.** The second review's 9.2 raised the family's exclusion of
   interaction and the third review marked it addressed by the coupled family entering Methods and
   Results 4. Nobody checked the Abstract, and the Abstract was cut from about 440 to 319 words
   afterwards, on 16 September. This is the qualifier the shortening lost.
5. **F9 added** (it is not in my Phase 1 list in this form). `manuscript/analysis_record.md`'s correction
   note of 16 September 16:24 UTC, item (ii), and
   `notes/planning_checks_2026-09-16/audit/audit_bundle15.log` show the null δ_run running from +0.00003
   to +0.00151 across q shapes — 1 % to 44 % of the observed value — and conclude that "the null's value
   depends on the shape of the q distribution near zero". The paper's 9–14 % band is over six
   configurations that all pin that shape through three moments, which Methods states; what the paper
   does not state is the sensitivity itself, which is the reason a previous reading of this statistic was
   withdrawn.

**Checked and cleared in Phase 2 (a concern I formed, then resolved).**
`notes/planning_checks_2026-09-16/planning_chat/check3_signsel.log` shows the sign(q)-weighted run-level
statistic at +0.00933, +0.00373 and +0.00005 on a toy AR(1) with a population deviation of exactly zero —
values that bracket the observed +0.00340 and would, if that toy were a fair null, make the whole
signature selection bias. It is not a fair null: a pure AR(1) at a = 0.86 has an integrated
autocorrelation time of about 13 TRs against the data's 3, so about a quarter of the effective sample
size, and the sign-selection bias scales with the sampling variance of q̂. The repository says so itself
(the README calls it "sign-selection bias on a toy AR(1) … Not the null's generator"), the correction note
of 16 September derives the same conclusion from the filter generator ("+0.00151 with every pair at
q = 0"), and the null the paper uses is fitted to the data's own ACF and to the density of q̂ near zero.
What survives of the concern is F9, and nothing more.

**Also checked and cleared.** Every other third-review finding that
`verification_correction_note_2026-09-15.md` §2 listed as "not addressed" on 15 September is addressed in
the current text: 5(ii) (CCS-sts bound rather than independence), 12.2 (the ACF shape change at lag 3, now
a paragraph in Results 5), 12.3 (the within-run residual values with their p and the 0.33 placebo share),
12.4 (the global-fit CCS cells stated to meet the weighting rule), all six applicability items (the Luppi
2022 band assumption, the Fig. S1D attribution, the lower-bounds framing, Down 2026 as a family
statement, Liardi as PID on MEG, and "we apply it to all of them"), item 4 (Mediano 2021's own AR example
in the Introduction; "says nothing about … synergy in the brain" now leading the Discussion section), 8.2
(the leave-two-out range in Results 3 and in Figure 3's caption; the odd/even-TR design discussed and
rejected with a reason in Limitations), 8.3 (the effective-N statement now in the Abstract), 9.8 (the
Abstract's "(a_x, a_y, q)" in both places), 9.10 (the current caption string prints grid step 0.01),
9.11 (the atom-code key now in Table 1's caption and the Introduction, not only in the paragraph that is
removed before circulation), 9.13 (the 474 rows decomposed as 79 × 6, 186 + 288 and 316 + 158 — all three
identities hold), 2.2 (both the 35–38 % run means and the 32–34 % test-window shares, each with its
scope), 3.3 (the symmetric-coefficient prediction labelled as not in the plan), item 10's figure items
(Figure 1's uncertainty note, Figure 3a's leave-two-out, Figure 4's within-subject bands on the dashed
lines too, and the stated y-ranges), and Task 1's 5.4 and B8 (both computations since run, under pre-run
entries whose commits the outputs carry). I did not find a case where the paper claims a fix it has not
made.
