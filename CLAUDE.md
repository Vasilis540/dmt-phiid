# DMT ΦID Project

Secondary analysis of open DMT fMRI data (Timmermann et al. PNAS 2023;
data from Singleton et al. Commun Biol 2025, `singlesp/DMT_NCT`), applying
Integrated Information Decomposition (ΦID, Gaussian, MMI redundancy, τ = 1)
to test whether whole-brain synergistic information is up-regulated under
DMT and tracks subjective intensity. Produced as evidence of computational
neuroimaging competence for a PhD application to the Cognition and
Consciousness Imaging Group, Division of Anaesthesia, University of
Cambridge (Prof. Emmanuel Stamatakis).

## Deadlines

- **20 Nov 2026** — public preprint + documented repo
- **8 Dec 2026** — Cambridge application (Gates Cambridge / Cambridge Trust)

## Current state (21 Sep 2026, round 14, Stage B)

**Analysis complete. The paper is `manuscript/draft_v2.md`, restructured on 21 Sep 2026 (round 14, Stage B) for a journal reader in the PLOS Computational Biology Methods-article order: new title, abstract and Author summary at their caps, seven Results sections, main text 9,994 words (title through Methods), the supporting information as `manuscript/si/S1_Text.md`–`S5_Text.md` and the tables S1–S11 in `manuscript/supplementary.md`. `manuscript/draft.md` is the superseded first draft, kept as a record; `notes/companion_plain_language.md` is retired. Figures `fig1_v2`–`fig5_v2` built by `scripts/15_figures_v2.py`, whose revision of 21 Sep also writes `fig1_v2_atoms_observed_predicted` and `fig6_v2_regional`; the committed files stay those of 48ea934 until the final full run.**

- Primary result (Primary B, windowed W = 60 estimator, ts_gsr, replicated
  on ts_demean): whole-brain synergy **decreases** under DMT, DiD negative
  and significant on both nulls, survives motion control. **This refutes
  the pre-specified directional hypothesis** and is reported as a
  refutation, never reframed. Tier-2 intensity tracking is **void** under
  the pre-specified controls; the claimed tier is **3** (step contrast +
  methods contribution).
- The two adversarial reviews of 14 and 15 Sep and the Part B analyses
  (dated entries in the record; `notes/partB_prespec_2026-09-14.md`)
  reframed the paper as an account of the estimator: the sts decrease is
  reproduced by the lag-1 autocorrelation change (per-subject r = 0.95;
  0.85–0.97 with any two subjects dropped), with a residual of which a
  stationary finite-sample null accounts for a third to two-thirds (the
  observed interval contains the null) and a CCS-sts increase that stays
  exploratory (record, "Closure entry" and "Correction note, 15 Sep 2026").
  The third review's findings and the changes made in response are in the
  correction note; the verification of that note (15 Sep) led to the
  wording fixes, the within-subject bands of Fig. 4, Fig. 5 and the
  leave-two-out (record, "Leave-two-out", pre-run entry and outcome).
- Data reuse: confirmed by email from C. Timmermann (13 September 2026)
  and S. P. Singleton (14 September 2026), with attribution; the
  correspondence is held by the corresponding author. Subject order across
  files verified at one subject (record, "Subject alignment across files");
  author confirmation still requested.
- Subject codes (an S, a two-digit subject number and two letters, in the
  ratings table) were removed from every tracked file on 15 Sep 2026 (record,
  "Data-governance note, 15 Sep 2026"); they remain in `external/` (not
  tracked) and in the git history. The repository is public (reachable
  without login) and the codes are in the public source release (V.S.
  verified this on 18 Sep 2026 by reading `intensity_ratings.mat` from a
  fresh clone of `singlesp/DMT_NCT`), so the history carries nothing the
  source release does not, and a history rewrite is hygiene rather than a
  governance necessity. Decision (18 Sep 2026; the commission's default,
  V.S. having named no other choice): the history is left as it is, with
  this note (record, "PLOS Computational Biology form",
  18 Sep 2026; the paper's Ethics statement states the facts).
- 15 Sep 2026, afternoon: `notes/companion_plain_language.md` (a
  plain-language companion for the first author) closed with 35 places
  where the paper stated something without justifying it, used an undefined
  term, compressed a step or made a claim not reconstructible from its text;
  every one was addressed (record, "Text revision after the plain-language
  companion", 15:46 UTC; no number changed). Two of them were computations,
  run under a pre-run entry (15:35 UTC; commit 152cc6d, 15:31 UTC): the
  run-level cross-lag deviation (`notes/partB10_crosslag_deviation.py`;
  first as a signed mean over pairs — see the next entry) and the
  regional sts–r₁ test (`notes/partB11_regional_sts_r1.py`; regional sts
  follows regional r₁ at +0.86, spin p < 0.0001 — the spatial-map exposure
  is real on these data). Both are in `run_all.sh` section 6. Tables
  renumbered in order of appearance (CCS/ΦR = Table 3, residual = Table 4,
  split-half = Table 5, lag = Table 6). `notes/defence_questions.md` holds
  25 questions with answers.
- Figures regenerated at 7c7809a (`captions_v2.md` header "at git
  7c7809a"; values unchanged) and committed; the companion's table numbers
  and units match the revised paper. Regenerated again by V.S. at 48ea934
  (5906148, 17 Sep; the captions file records that commit) from unchanged
  results, with the caption strings of rounds 8b and 9; the paper's Figures
  paragraph names 48ea934 since round 11 (18 Sep; no [TK] there any more).
- 15 Sep 2026, evening: a fifth review found that the run-level cross-lag
  deviation, computed as a signed mean over pairs, could not test the
  pooling mechanism on `ts_gsr` (the deviation that lowers sts has the sign
  of q, and 54.5 % of the pairs have q < 0, so the two kinds of pair cancel).
  `partB10` gained the sign(q)-weighted mean and the slope of the deviation
  on q (pre-run entry 18:14 UTC, commit 13f1c6d; outcome 18:18 UTC):
  `ts_gsr` +0.00340 [+0.00300, +0.00380], 14 of 14 subjects, the branch
  recorded for pooling operating. Pooling is a candidate for part of the
  run-level residual, not distinguished from lagged coupling that follows
  the sign of q or from finite sampling; the finite-sample null's value of
  the statistic and its within-window value are not computed. The paper's
  Results 4, Discussion and Limitations and thirteen text items were revised
  with it (record, "Text revision after the fifth review"); the companion
  and the defence questions follow.
- 16 Sep 2026: the sign(q)-weighted deviation within 60-TR windows and on the
  finite-sample null (`partB10` sections A and B; pre-run entry 10:23 UTC,
  commit 9a19b10; outcome 10:32 UTC) — superseded the same day: a correction
  note (16:24 UTC) records that the W = 60 statistic took the sign from each
  window (selection on the same samples; the null's own value with that
  weight is +0.00348 of the data's +0.00611) and that the run-length null was
  read at the wrong q̂ density. The exact budget replaced it (round 7; pre-run
  entry 16:24 UTC, commit 6b5181a; outcome 16:37 UTC; `partB12`/`partB13` with
  `rev_crosslag_budget.py`): δ_run = δ_within + δ_pool + δ_means + ε, s = the
  sign of the run-level q; null solved to the data's run-level a, |q̂| and
  fraction |q̂| < 0.05 per run type in six configurations; two controls.
  `ts_gsr`: δ_run +0.00340; null +0.00029 to +0.00046 (finite sampling a
  minor part, 8–14 % for F = 0.085–0.135); null-corrected +0.00301: within +0.00250 (83–84 %,
  most), pool +0.00046 (15 %, a minor part), means +0.00004 (a minor part);
  pooling larger on the DMT run (+0.00039, p = 0.0006, 11 % of that run's
  signature). Common slow drive and lagged coupling are one account at τ = 1
  (A = Γ₁Γ₀⁻¹); what acts inside the windows is open, and the closure entry
  ends the thread. S9 Table holds the budget and the superseded
  values. `ts_demean` (−0.00262) reported, not read.
- `run_all.sh` has executed once, in two invocations at d145e1c (sections 0–5
  and the first ten steps of section 6 on 15 Sep; the remaining fourteen
  steps on 16 Sep, `results/run_all_tail.log`, 51 min): sections 0–5 CSVs
  reproduce exactly, section 6 to 7.9e-13 (record, 16 Sep 16:24 UTC entry;
  `notes/planning_checks_2026-09-16/reproduction_checks/`). Regenerated
  files not committed (stashed); three provenance differences recorded.
- 16 Sep 2026, readability pass (round 8; record, "Text revision for
  readability", 18:05 UTC; text files only, no number changed, nothing
  under `scripts/`, `results/` or `notes/review_results/` touched, so that
  the single full run of `run_all.sh` started at d51966e keeps one SHA):
  Abstract cut to 300 words (319 after the wording decisions of round 8b
  restored two clauses); status line cut to two sentences; Discussion's
  first section in four paragraphs; Methods sentences over 60 words split,
  symbols defined at first use, the "cell" definition in Estimator only;
  Results 4's budget wording (8–14 % for F = 0.085–0.135; "the DMT run
  carries about a tenth more of it"); Data and code availability states
  which tables carry the git SHA; the AI-use statement no longer names one
  model; "three adversarial reviews" corrected to five (the fourth the
  verification of the correction note) here, in `README.md`, the companion
  and the defence questions.
- Revision chain of `manuscript/draft_v2.md` (moved here from its status
  line on 16 Sep 2026; each entry named is a dated heading of
  `manuscript/analysis_record.md`):
  1. 15 Sep 2026, after the second adversarial review
     (`notes/adversarial_review_draft_v2_2026-09-15.md`).
  2. 15 Sep, after the third
     (`notes/adversarial_review_draft_v2_second_pass_2026-09-15.md`); the
     changes are listed in the record's correction note of 15 Sep
     (10:05 UTC).
  3. 15 Sep, after the verification of that correction note (the fourth
     review, `notes/verification_correction_note_2026-09-15.md`): the
     leave-two-out entries of 11:09 and 11:10 UTC; the finalisation pass
     of 12:40 UTC.
  4. 15 Sep, after the plain-language companion's list of thirty-five
     problems (`notes/companion_plain_language.md`, last section): the
     entries of 15:35, 15:36 and 15:46 UTC (the two computations run for
     it and the text revision, item by item).
  5. 15 Sep, after the fifth review, whose one finding was that the
     run-level cross-lag deviation as first computed could not test the
     mechanism it was run for (quoted in the entry of 18:14 UTC): the
     entries of 18:14, 18:18 and 18:46 UTC.
  6. 16 Sep, when that statistic was computed within 60-TR windows and on
     the finite-sample null and a third look-alike was added to
     Results 4: the entries of 10:23, 10:32 and 10:36 UTC.
  7. 16 Sep, when a correction note recorded the defects of those two
     computations and an exact budget of the statistic against a null
     solved to the data replaced their readings: the entries of 16:24
     (correction note; the `run_all.sh` entry; the budget's pre-run
     entry), 16:37 (outcome) and 16:48 UTC (text revision; closure of
     the thread).
  8. 16 Sep, the readability pass above (record, "Text revision for
     readability", 18:05 UTC).
  9. 16 Sep, the wording decisions on that pass and the three caption
     splits in `scripts/15_figures_v2.py`, not run (record, "Wording
     decisions and caption edits", 19:58 UTC); the Figures paragraph
     carried [TK: SHA] until round 11.
  10. 17 Sep, the response to the fresh adversarial review (the sixth
     review, `notes/fresh_review_2026-09-17/`): record, "Response to the
     fresh adversarial review", 17:19 UTC.
- 17 Sep 2026, round 9: a fresh reviewer session (the sixth review) wrote
  `notes/fresh_review_2026-09-17/` (review.md and checks/, committed
  byte-identical; the `phase1_findings.md` it cites is not in the folder)
  after reading V.S.'s working tree at d51966e while the single full run
  was in progress. The response (record entry of 17:19 UTC; text and
  caption strings only, no new analysis): F1 the 0.953 includes estimation
  error the two DiDs share (full-length ceiling 0.84; Results 3,
  Discussion, Fig. 3a); F2 the residual DiD's remainder is not established
  (p = 0.15–0.47 against the null's values) while the run-level residual,
  −0.0137 [−0.0145, −0.0130], exceeds the null (check C1; Table 4); F3 the
  windowed series and the variance ratio, no variance control, with the
  reason (Results 6; check C2); F4 the claim conditional on lagged
  interaction not changing comparably (Abstract, Discussion); F5 which
  tables carry a SHA (Data and code availability, defence Q25); F6–F15 as
  in the entry, with Tarchi et al. (2026) added to the references; the
  Abstract's CCS bracket as |r| < 0.02 (335 words); defence Q26 on the
  effective-sample factor. Not adopted: the cross-half sts/r₁ computation,
  the variance control, a derivative-ratio range.
- 17–18 Sep 2026: V.S.'s commits 48ea934 (two bias-check tables with a
  d51966e header and the truncated run log), 5906148 (figures at 48ea934)
  and 0a25aaa (`reproduction_checks/6_*`; its message corrects 48ea934's:
  no full run has completed). Round 10 (record, "The attempts at the
  end-to-end run of `run_all.sh`, 16–18 September 2026", 14:45 UTC): four
  attempts, 16–17 Sep, all stopped inside `02_bias_check`; the two that
  stopped within minutes of the lid being closed include one with every
  sleep target masked, so a closed lid stops the run by a route other
  than suspend, and memory was not short (11.7–12.2 GB available); the
  stationary bias tables reproduce at d51966e; the non-stationary tables
  were never rewritten. Text: Results 4's closing clause, Data and code
  availability in three sentences, two wording repeats, README's SHA
  sentence; status line 18 Sep.
  11. 18 Sep, the Figures paragraph filled with the tree as it is (48ea934)
     and the status line set for co-author review (record, "Figures
     paragraph and status line for co-author review", 14:58 UTC).
  12. 18 Sep, the PLOS Computational Biology form (record, "PLOS
     Computational Biology form"): unstructured Abstract, Author summary,
     short title, "Materials and methods" with the Ethics statement and
     "Use of AI tools" as subsections, Funding, Competing interests,
     Supporting information (S1–S4 Text, S1–S9 Table), the exact Ethics
     sentence on the subject codes.
  13. 20 Sep, the citation audit's F1–F19 and the plan's Q1–Q8 (record,
     "Text corrections of round 13"): every attribution checked against the
     full texts; Luppi et al. (2022)'s own surrogate test stated; all four
     residual–CCS correlations; the counterbalanced order; n_eff by
     Bartlett's formula; seventeen references added, Prichard & Theiler
     replaced by Theiler et al. (1992).
- 18 Sep 2026, round 11: the Figures paragraph names the commit at which the
  five figures were generated, 48ea934, as the captions file records, with
  5906148 as the commit that holds them, 7c7809a and the no-git checkout as
  the earlier generations; the status line reads "draft v2 as of
  18 September 2026, for co-author review; not for citation or
  distribution". The figures are to be regenerated once more at the commit
  of the single full run (open item below), not marked as a [TK].
- 18 Sep 2026, round 12 (record, "PLOS Computational Biology form"):
  target journal PLOS Computational Biology (Methods article type),
  preprint to bioRxiv; author-year citations kept, the numbered form done
  at submission. Abstract unstructured and 296 words (the split-half
  sentence and the "spatial synergy maps are exposed" clause dropped, the
  CCS bracket's numbers kept); Author summary (198 words) after it; short
  title (61 characters); "Methods" is "Materials and methods" with
  "Ethics statement" first and "Use of AI tools" last (PLOS wording, no
  [TK]); "Funding" added ([TK] for C.T. and S.P.S.); "Conflicts of
  interest" is "Competing interests"; "Supplement (pointer)" is
  "Supporting information" with S1–S4 Text and S1–S9 Table, renamed
  wherever the paper, the supplement, the COBIDAS checklist, the
  companion, the defence questions, `README.md` and this file cite them;
  the Ethics statement's identifiability sentence replaced by the exact
  facts on the subject codes. The subject-code bullet above records the
  governance facts and the decision on the history. Commit B of the round:
  the git SHA in the output headers of the nineteen `notes/` scripts that
  lacked it, through `notes/rev_git.py` (a `git=<SHA>` line after the title
  of every .md and titled .log, first in the assembled logs, first in the
  run logs; `# script; git=<SHA>` first lines in the five CSVs no reader
  reads without `comment="#"`; `inference_rows_raw/deconv/w30.csv` left
  without one because `rev_tables.py` and `3_three_checks.py` read them
  plain); pre-run entry appended before the run; the run is open (below).
- 20 Sep 2026 (V.S., a75d015): the section-6 verification run at d507728
  passed the pre-run rule (record, "The git SHA in the output headers of
  the notes/ scripts: outcome"); outputs committed; the binaries were
  restored before `8_binary_compare.py` could run, so their direct
  comparison is required before the final full run's commit. The same
  commit filed `notes/review_2026-09-20/`: the citation audit against the
  36 PDFs of `external/papers/` (git-ignored) and the SI Appendix of
  Mediano et al. (2025), the independent adversarial review (44
  findings), its verification, and the plan to submission; record entries
  of 20 Sep for each, and "Decisions of 20 Sep 2026": D1 the multiplicity
  rule withdrawn in round 14 (one confirmatory test, the MMI-sts DiD;
  everything else exploratory, effect size and interval, no threshold
  language; the rule's history to S5 Text); D2 the title changes in round
  14 to option (d) of the plan unless V.S. says otherwise; D3 W = 60 stays
  primary, the global fit beside it with the bias tabulated; D4 "a planned
  directional test recorded before the primary analysis" in round 14; D5
  B16 (prewhitening) run before the preprint; audit F7 and F9 adopted.
- 20 Sep 2026, round 13 (record, "Text corrections of round 13"; commit A):
  F1–F19 and Q1–Q8 applied with the audit's and the plan's wordings;
  `notes/partB5_literature_v2.md` (Table A from the full texts; the 14 Sep
  file kept as the record); references: seventeen added, eight of them not
  yet cited (Arbabshirani, Cliff, Honari, Ito, Kay & Ince, Murray, Raut,
  Faes 2017 — their sentences come with round 14), the † convention gone,
  Tarchi and Mediano 2025 parentheticals amended; Abstract 302 and Author
  summary 204 words after F19 and Q7 (over the caps of 300 and 200 until the
  round-14 rewrite); `captions_v2.md` hand-edited for F16 while its source
  `scripts/15_figures_v2.py` (line 231) was unchanged until 21 Sep, when the
  script was given the same words (round 14, Stage A). Commit B: the pre-run
  entries and scripts of B14–B20 (below).
- 21 Sep 2026: V.S. ran B14–B20 at f1f5fcc (`runb14` completed B16 and was
  killed by a lid closure during B17; `runb17` ran B17, B14, B15, B18, B19,
  B20 from the start; no tracebacks) and committed the outputs as 96e2242,
  with the sixteen never-tracked outputs of the 20 Sep section-6 run.
  Round 14, Stage A (record, "B14, outcome" … "B20, outcome", 21 Sep): the
  seven outcome entries — B14 met (Results 1's "two departures" replaced by
  the asymmetric-family account); B15 the run-level residual located (half
  directed, half symmetric on ts_gsr; the directed part unchanged by DMT);
  B16 prediction not met as recorded — AR(p ≤ 5) leaves r₁ = 0.26, sts 0.22,
  contrast −0.026 (p = 0.14), still predicted by the residual autocorrelation;
  B17 (i), (iii), (iv) met, (ii) wrong in form (the first-order term averages
  out over a sign-symmetric q pool), the test of the residual against zero
  anti-conservative (p < 0.05 in 82 % of null replicates), the family's
  windowed bias larger than the data's; B18 the CCS increase is the
  co-information term; B19 exchange rates in data units, R² = 0.808,
  cross-half r = 0.694 (ceiling 0.729), BCa within 10 % of percentile; B20
  the sensory–association contrast of the regional map is accounted for by
  regional r₁ (−0.0202 → +0.0007, p = 0.90). Two new pre-run entries and
  scripts: B16b `notes/partB16b_whitened_spectrum.py` (data; minutes) and
  B17b `notes/partB17b_calibration_filtered.py` (no data; about an hour),
  in section 6 of `run_all.sh`; V.S. runs them (`runb16b`).
- 21 Sep 2026, round 14, Stage B (record, "Round 14: the restructuring"):
  `manuscript/draft_v2.md` rewritten once, for a journal reader, in the PLOS
  CB order. Title option (d) of decision D2; abstract 300 words and Author
  summary 200 at their caps; main text 9,994 words against 16,508 before.
  Results in seven sections (the closed form and the exchange rates in data
  units; the DMT contrast and its per-pair prediction, with the new Table 5;
  the regional map partialled, with the new Fig 6; the residual diagnostic
  read against its calibrated expectation rather than against zero; the lag
  dependence; CCS; remedies). The "32-fold" per-unit statement, the τ > 1
  recommendation and the multiplicity weighting rule are withdrawn (D1); the
  single confirmatory test is named as such and everything else is reported
  as exploratory with effect sizes and intervals. No SHA, timestamp, file
  path or record reference in the main text (B5); the provenance lives in
  `manuscript/si/S5_Text.md`. `scripts/15_figures_v2.py` revised for Figs 1–4
  and the new Fig 6 (not regenerated in this commit). `supplementary.md`
  gains S10 (calibration) and S11 (prewhitening) and the spin-test p values
  in S5 Table's note; `notes/defence_questions.md` rewritten (24 questions);
  `notes/companion_plain_language.md` retired with a dated note. 36 values
  that depend on B16b and B17b stand as `[TK: B16b]`/`[TK: B17b]` until
  those outputs are committed, then filled in a follow-up commit.
- Remaining work: the 36 `[TK: B16b]`/`[TK: B17b]` values, filled from the
  committed tables of B16b and B17b in a follow-up commit (with the matching
  cells of S3 Text, S10 and S11 Tables, and the outcome entries of B16b and
  B17b in the record); the thirteen permanent [TK] items in `draft_v2.md`
  (affiliations, co-authors, the REC reference number, the co-authors'
  funding statements, contributions, competing interests, the run
  sentence); run `run_all.sh` end-to-end
  once as a single run at the final commit, with the lid open for the whole
  run (four attempts on 16–17 Sep stopped inside `02_bias_check`, two of
  them within minutes of the lid closing, one of those with every sleep
  target masked; record, "The attempts at the end-to-end run") — V.S.; it
  regenerates and commits every output under one SHA, `partB12`/`partB13`
  included, closes the Data and code availability [TK], and regenerates the
  figures once more at that commit — six now, `fig6_v2_regional` included,
  with `captions_v2.md` — after which the Figures paragraph's
  48ea934 and the captions file's header change to it. The `notes/` writers
  write the git SHA since round 12's commit B (`notes/rev_git.py`; record,
  "The git SHA in the output headers of the notes/ scripts: pre-run entry",
  18 Sep): the verification run of section 6 at that commit, its comparison
  (`6_committed_compare.py <commit B>`, plus `git diff -- '*.log'` for the
  logs) and the outcome entry are V.S.'s to do, the regenerated outputs
  committed only if every difference is a header line, a SHA or an
  elapsed-time line; then one full run of `run_all.sh` at the final commit. Venue chosen
  (18 Sep 2026): PLOS Computational Biology, Methods article type; preprint
  to bioRxiv (`notes/venue_options.md`); the numbered citation form and
  the packaging of the Supporting information items as separate files are
  done at submission. Round 13's computations B14–B20 (record, pre-run entries
  of 20 Sep; `notes/partB14_*.py`–`partB20_*.py`; section 6 of `run_all.sh`)
  were run on 21 Sep (96e2242) and their outcome entries appended (Stage A of
  round 14); B16b and B17b are V.S.'s to run (`runb16b`), their outcome
  entries to follow; round 14, Stage B (the restructuring: PLOS CB order, ≤ 10,000 words, S5 Text
  "Provenance and audit trail", the residual against its finite-sample
  expectation, D1–D4, the figures, the abstract, Author summary and title,
  the §5 sentences citing the eight uncited references) quotes B16b's share
  and B17b's rows as [TK: B16b]/[TK: B17b] until they are committed; then
  the final full run at the final code commit with
  `6_committed_compare.py` and `8_binary_compare.py`, a fresh review of the
  finished text, typesetting, and the note to C.T.

## Post-hoc checks (NOT pre-specified; recorded here, not in the record)

Specified after the primary result, labelled post-hoc wherever reported,
reported regardless of outcome. They decide nothing. Full numbers in the
named CSVs.

- **Leave-one-out on the primary DiD (14 Sep 2026; `13_loo_did.py` at
  17dbfcb, `results/loo_did_win60.csv`).** Raw W = 60 primary DiD, each
  subject dropped in turn. LOO mean range ts_gsr −0.0944 to −0.0656,
  ts_demean −0.1182 to −0.0871; **no LOO CI includes zero (0 of 28)**,
  p ≤ 0.0076 throughout. Subject 14 (only positive DiD) is the most
  influential: dropping it strengthens the effect. Dropping subject 8
  (largest magnitude): ts_gsr −0.0656 [−0.1013, −0.0271], p = 0.0076;
  ts_demean −0.0871 [−0.1310, −0.0408], p = 0.0051. No single subject
  carries the result. One sentence in the draft's Results.
- **Proportionality of the synergy decrease (14 Sep 2026; rule recorded
  at dbf2311 BEFORE the run; `14_proportionality.py`,
  `results/proportionality.csv`).** Ratio sts / TDMI (Σ 16 atoms) per
  subject, condition, window/bin; DiD of the ratio in the primary form.
  **Rule (fixed before running):** ratio-DiD CI includes zero →
  proportional, no evidence of a selective synergy effect; significantly
  negative → more than proportional; positive → less. The directional
  refutation stands under all three outcomes (sign, not selectivity).
  **Outcome:**

  | cell | ratio DiD [CI], p | verdict | (i) baseline share | (ii) share of TDMI DiD |
  |---|---|---|---|---|
  | W = 60, ts_gsr | +0.0005 [−0.0081, +0.0083], 0.91 | proportional | 0.782 | 0.780 [0.653, 0.936] |
  | W = 60, ts_demean | −0.0095 [−0.0235, +0.0049], 0.22 | proportional | 0.767 | 0.870 [0.691, 1.006] |
  | global, ts_gsr | **+0.0204 [+0.0048, +0.0340], 0.025** | **less than proportional** | 0.908 | 0.658 [0.486, 0.817] |
  | global, ts_demean | +0.0071 [−0.0167, +0.0292], 0.56 | proportional | 0.897 | 0.787 [0.500, 1.013] |

  Under the primary estimator (W = 60) on both variants, synergy falls in
  proportion to total predictable information: sts is ~78 % of TDMI at
  baseline and carries ~78–87 % of the TDMI drop. The global fit on
  ts_gsr is the one cell with a significant ratio DiD, positive, i.e.
  sts falls *less* than proportionally there (DMT post − pre +0.0167,
  p = 0.018; PCB −0.0037), not replicated on ts_demean. **No cell shows
  a more-than-proportional (selective) synergy reduction.** The
  windowed and global estimators put sts at different shares of TDMI
  (0.78 vs 0.90) because the per-window bias falls on sts and the
  self-transfer atoms differently. In the draft (Results, Discussion, S8 Table).

## The record: `manuscript/analysis_record.md`

**`manuscript/analysis_record.md` is the full pre-specification and results
record.** It was the project `CLAUDE.md` until 14 Sep 2026, when it was
moved with `git mv` (byte-identical; `git log --follow` carries its
history). Every decision, prediction and rule in it was committed before the
result it governs existed; `manuscript/prespecification_summary.md` lists
them by SHA. **Never retroactively edit, reorganise or condense it.**
Corrections and new entries are appended, dated, with the original left in
place. Read the relevant section before touching a script or result.

## Repository layout

```
CLAUDE.md                        this file: orientation and standing rules
manuscript/analysis_record.md    pre-specification + results record (append-only)
manuscript/prespecification_summary.md  decisions by commit, changed-later audit
manuscript/draft_v2.md           the paper (restructured 21 Sep 2026)
manuscript/draft.md              superseded first draft, kept as a record
manuscript/si/                   S1_Text.md–S5_Text.md, the supporting texts of draft_v2.md
manuscript/supplementary.md      supplementary tables S1–S11, values quoted from results/
                                 and notes/review_results/
manuscript/supplementary_cobidas.md  the COBIDAS reporting checklist, pointed to by S4 Text
manuscript/figures/              fig1_v2–fig5_v2 (pdf/png) + captions_v2.md, from 15_figures_v2.py
                                 (the committed files are those of 48ea934 until the final run);
                                 the draft.md figures + captions.md (12_figures.py) kept in place
scripts/                         numbered by execution order, each independently runnable
  00_verify.py                   data + method integrity check; run after any env change
  01_synergy_timecourse.py       all 16 ΦID atoms per pair, whole-brain mean per bin/window
                                 (--fit-mode global|window|placebo, --variant ts_gsr|ts_demean)
  02_bias_check.py               finite-sample bias on simulated VAR(1), stationary + non-stationary
  03_lz_vs_tdmi.py               total TDMI vs EEG Lempel-Ziv regressor
  04_logdet_correction_check.py  decision-tree step 2 (analytic log-det correction)
  05_tier_check_decay_windows.py tier statistics on windows 6–14 from the bias-check tables
  06_primary_b_analysis.py       Primary B inference: step contrast, nulls, motion, tier-2 controls
  07_windowed_atoms_did.py       rtr / total / self-transfer atoms, windowed vs global
  08_robustness_c_analysis.py    Robustness C inference
  09_global_fc_per_bin.py        mean pairwise r per bin, both variants
  10_subject_alignment_check.py  is the subject axis shared across data files?
  11_regional_analysis.py        EXPLORATORY: per-region DiD, spin tests, workspace proxy
  12_figures.py                  draft.md figures, regenerable from results/
  13_loo_did.py                  POST-HOC: leave-one-subject-out on the primary DiD
  14_proportionality.py          POST-HOC: sts / TDMI ratio DiD, four cells, rule in the docstring
  15_figures_v2.py               draft_v2.md figures, from results/ and notes/review_results/
notes/                           adversarial reviews, the verification of the correction note
                                 (verification_correction_note_2026-09-15.md), the sixth review
                                 with its checks (fresh_review_2026-09-17/), the citation audit,
                                 the independent review, its verification and the plan to
                                 submission of 20 Sep (review_2026-09-20/), the applicability
                                 table (partB5_literature.md, 14 Sep; partB5_literature_v2.md,
                                 20 Sep, from the full texts), venue options
                                 (venue_options.md), review computations (rev_*.py, review_*.py;
                                 rev_git.py gives the git SHA for their headers),
                                 Part B plans/notes/scripts (partB*.md, partB*.py; partB10 and
                                 partB11 added 15 Sep for the cross-lag deviation and the regional
                                 test; partB12, partB13 and rev_crosslag_budget.py added 16 Sep for
                                 the cross-lag budget; partB14–partB20 added 20 Sep for the plan
                                 of that date and run 21 Sep; partB16b and partB17b added 21 Sep;
                                 planning_checks_2026-09-16/ the planning
                                 session's checks and V.S.'s reproduction checks; the regional
                                 sts–r₁ test); the plain-language companion and the defence
                                 questions (companion_plain_language.md, defence_questions.md);
                                 outputs under notes/review_results/ (tables, logs, inference
                                 rows, atom arrays)
results/                         every table/array with script + git SHA in its header;
                                 run_*.log are the run logs; nonstat_*/ are bias-check sub-runs
data/                            Schaefer-100 parcel LUT only (all fMRI data is in external/)
external/DMT_NCT/                git clone of singlesp/DMT_NCT (git-ignored, not a submodule): data + original MATLAB
requirements.lock.txt            pinned environment (.venv/bin/python)
```

Data facts are in the record ("Data", "Region exclusion"); do not
re-derive them. Key ones: 14 subjects × 2 conditions, **index 0 = DMT,
1 = placebo**; (116 regions, 840 TRs), TR 2 s; 28 ratings = 30 TRs per
bin; **region 20 (0-based) dropped everywhere → 115 regions, 6,555
pairs**; subject index 2 PCB TR 839 is NaN.

## Standing methodological rules

These govern any new work and are what a Cambridge reviewer will check
first.

1. **Spatial nulls.** Brain-map correlations use spin tests (cortical
   parcels only; subcortex has no spin null and gets a descriptive ρ
   without p) or BrainSMASH. Never naive parametric p-values.
2. **Temporal nulls.** Phase-randomised surrogates for any synergy-vs-
   intensity or synergy-vs-time-course correlation.
3. **No double-dipping.** Never select regions on an effect and re-test
   them on the same data. The FDR-surviving regions from the exploratory
   analysis are not to be selected for any further test.
4. **Motion.** Report FD, residualise, test survival under the definition
   fixed in the record (same sign, bootstrap CI excludes zero).
5. **N = 14.** Effect sizes with CIs, exact sign-flip tests, proof-of-
   concept framing. Never "established".
6. **Preprocessing sensitivity.** Every result on `ts_gsr` (primary) and
   `ts_demean` (sensitivity) at minimum.
7. **FDR** across regions/edges/maps, Benjamini–Hochberg, stated
   explicitly.
8. **Reproducibility.** `SEED = 20261120` everywhere; git SHA in every
   output header (scripts tag `-dirty` if `scripts/` or the record have
   uncommitted changes; the `notes/` scripts through `notes/rev_git.py`,
   which also tests `notes/*.py`); every figure regenerable from a single
   script;
   no manual figure editing.
9. **Directional honesty.** The hypothesis was directional (synergy up).
   The observed decrease is a refutation. Do not reframe it. Tier-2 claims
   stay void; the tier-2 numbers are reported with the void verdict.
10. **Luppi et al. eLife 2024 comparison.** Licensed only as a
    dissociation (workspace-concentrated collapse under propofol/DoC vs a
    spatially uniform DMT decrease), qualified by the network-proxy
    limitation. "Synergy falls under DMT as it does under propofol" is not
    a licensed sentence.
11. **Pre-specify before computing.** Any new analysis gets a dated entry
    appended to the record, with predictions if any, before the first
    number is produced. Exploratory work is labelled exploratory in every
    table and figure and reported regardless of outcome.

## Working conventions

- Python only (`scipy.io.loadmat` for the `.mat` files); no MATLAB.
- `phyid` is not on PyPI; `requirements.lock.txt` pins its git commit.
- Commit scripts before running them for a reportable result so the
  output header carries a clean SHA; record the SHA with the result.
- `results/` is never hand-edited; the record and manuscript quote it
  verbatim. `run_all.sh` regenerates everything (≈ 6 h for the original
  analysis; about an hour more for the review and Part B section).

## Open questions

At the end of the record ("Open questions"), with the later dated entries
("Closure entry", "Part B, items 6–8", "Correction note, 15 Sep 2026",
"Leave-two-out", "Data-governance note, 15 Sep 2026", "Finalisation pass,
15 Sep 2026") after it. The data reuse terms were confirmed by email from
C. Timmermann (13 September 2026) and S. P. Singleton (14 September 2026);
the correspondence is held by the corresponding author (README, "Licence");
author confirmation of the subject order is still requested.
