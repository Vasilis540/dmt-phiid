# Citation check of the changed citing sentences (66c6331 against 90690f4), 24 Sep 2026

## Citation audit of the new text (66c6331) against 90690f4

All scratch files are in /tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/verify/cite_b27/: extract.py, rows.json, new_citing_sentences.txt/.csv (N01–N51), closest_old.txt (each new sentence diffed against its nearest old one) and old_citing_lost.txt. I did not modify the repository and did not use the web.

### (a) Counts

**My count is 51**, against the authors' 91:

| file | mine | authors | all author–year sentences in the file now |
|---|---|---|---|
| main | 37 (35 in the text + 2 in the References head note) | 38 | 39 in the text (+ 2 head note + 3 inside reference entries) |
| S1 | 2 | 7 | 7 |
| S2 | 0 | 1 | 1 |
| S3 | 7 | 25 | 20 |
| S5 | 3 | 14 | 4 |
| supplementary | 1 | 6 | 1 |
| captions | 1 | — | 1 |

How I counted:
- Sentences were split with an abbreviation-aware splitter (et al., Eq(s)., Sec., Fig., p., i.i.d., initials).
- An author–year citation is any reference-list name followed by a year.
- Normalisation: NFC, whitespace collapsed, `*`, `_` and backticks removed.
- Each sentence was compared, as a whole sentence and as a substring, against the seven files and S4 Text at 90690f4.
- All 51 have substantive wording changes; none differs only in formatting.
- Of the citing sentences I did not count, 6 were moved verbatim between files: 4 from the old Methods into S1, and 2 from the old Introduction/Discussion into S3 ("Group differences…", "Its primary analysis is HRF-deconvolved…"). The rest are unchanged in place.

Why my count differs from 91:
- **91 is more than the total.** The new text has only 73 author–year citing sentences outside the reference list, so the authors must have used a broader definition.
- **main (+1):** probably the changed Faes et al. (2025) reference entry, which now names the arXiv version.
- **S1 7 and S2 1:** these equal all the citing sentences in those files. That includes the 4 moved sentences, S1:11 (unchanged), and the S2 Wu sentence, which is verbatim at 90690f4 (only the intervals in its paragraph changed).
- **S3 25:** S3 has only 20 author–year sentences in total.
- **S5 14:** S5 has 4 author–year sentences. 22 S5 sentences changed, and 15 of them cite commits, record entries or reviews; the 14 is probably a count of that kind.
- **supplementary 6:** the file has only 1 author–year sentence.

If "any file at 90690f4" meant the whole repository, 8 of the 51 drop out (N02, N04, N06, N10, N18, N36, N37, N40). Their wording appears verbatim in notes/review_2026-09-22/citation_pass_2026-09-22.md, committed in ca2b58b, which gives 43.

**Pair verdicts: 111 sentence × work pairs.**
- 88 supported
- 6 supported with qualification
- 4 not supported
- 0 misattributed
- 13 not checkable here

Every locator is correct: Barrett Example 1, Sec. V and Eqs. 73, 79–82; Varley Eqs. 3 and 12; Afyouni Eq. 8; Mediano 2021 Appendix Defs 1–2, Eq. 5, Fig. 5, Appendix VI; Mediano 2025 SI Sec. III.A, Def. 2, Eq. 6; Luppi 2022 Table 1 and p. 9.

Every quotation is verbatim: 'synergistic core', 'synergistic workspace', "disintegrated", and the three Faes 2025 quotations, which match the arXiv PDF (p. 1, "Dated: October 7, 2025").

### (b) Problems

| # | location | work | verdict | evidence | proposed wording |
|---|---|---|---|---|---|
| P1 | S1_Text.md:7 | Luppi et al. 2024 | **Not supported as worded** | The account ties conscious level to integrated information (ΦR) in the workspace, not to synergy. p. 1: "loss of consciousness … corresponds to diminished ability of the synergistic workspace to integrate information". p. 8: "consistent decreases in ΦR". Their synergy is the whole-minus-max aggregate, not sts (p. 20, Eq. 5). The same phrase stands uncited in Introduction ¶3 (draft_v2.md:29); this is the second bullet of A26, still open. | "…is up-regulated under N,N-dimethyltryptamine, a prediction derived from the synergistic-workspace account, in which loss of consciousness goes with reduced integrated information (ΦR) within the workspace (Luppi et al., 2024); the predicted direction was an increase." In ¶3: "against a prediction derived from the workspace account". |
| P2 | draft_v2.md:25 | Luppi et al. 2024 | Supported with qualification | The workspace is ranked on syn(X,Y) = I(X₋,Y₋;X,Y) − max{I(X₋;X,Y), I(Y₋;X,Y)} (p. 20, Eq. 5; ranking p. 21). That is the aggregate synergy (str+stx+sty+sts), not the sts atom named in the preceding sentence. Luppi 2022 does use sts (p. 14). | "Regions where synergy — there the whole-minus-max synergy of their Eq. 5, in ΦID terms str + stx + sty + sts — predominates over redundancy, by rank, form a 'synergistic workspace'…" |
| P3 | draft_v2.md:27 | Varley 2024 | Supported with qualification | Varley's result is about the aggregate I_Syn (p. 5, Eq. 3; p. 7, Eqs. 11–12; p. 1: "cannot disambiguate between truly integrated systems and disintegrated systems"). The scope ("for the aggregate forward synergy") was lost when the sentence was split; S3 §10 keeps it. | "MMI's aggregate synergy (in ΦID terms str + stx + sty + sts) cannot tell a synergistic pair from two independent autocorrelated processes (Varley, 2024, Eq. 12)." |
| P4 | draft_v2.md:85 | Huang et al. 2018 | Supported with qualification (minor) | Only propofol sedation was studied. p. 1: "MF, AC, and ReHo increased … during propofol sedation". | "…since BOLD lag-1 autocorrelation rises in propofol sedation (Huang et al., 2018)." |
| P5 | draft_v2.md:168 | Tarchi et al. 2026 | Supported with qualification (minor) | The regional pattern comes from L1-logistic-regression weights (Fig. 3 legend, p. 6): "lower synergy, and disrupted, albeit mostly higher, redundancy". Redundancy is reduced in prefrontal, paracingulate and primary sensorimotor/visual regions (p. 6). There is no global group difference (p. 4). | "(Down et al., 2026; in part, in the regional classification of Tarchi et al., 2026)" |
| P6 | draft_v2.md:184 (same word in S1_Text.md:5, a moved sentence) | Singleton et al. 2025 | **Not supported** ("anonymised") | Singleton's data-availability statement (p. 11) says nothing about anonymisation. The repository's own record ("Data-governance note", 15 Sep 12:15 UTC; "Git history and the participant codes") says the release carries codes "of the form S + two digits + initials" and calls them "pseudonymous". | "This is a secondary analysis of pseudonymised data released by the data authors (Singleton et al., 2025)." S1: "pseudonymised, parcellated regional time series…" |
| P7 | draft_v2.md:192 | Afyouni et al. 2019 | Supported with qualification (minor) | Eqs. 7–8 hold "though still assuming ρ = 0" (p. 4 [612]); the pairs here have \|q\| ≈ 0.25. | "…is, when their true correlation is zero, n / (1 + 2 Σ_k ρ_k²), the global form of the effective-degrees-of-freedom estimator reviewed by Afyouni et al. (2019, their Eq. 8; Bartlett, 1935, gave the AR(1) case); …" |
| P8 | draft_v2.md:196 | Ince 2017 | Supported with qualification (minor) | Ince's CCS is single-target (p. 12, Def. 1). The double redundancy is Mediano's extension (2021 p. 24: "a multi-target CCS function that reduces to the original when only a single target is specified"). The sentence makes "CCS (Ince, 2017)" the subject of the double-redundancy rule. | "Under CCS (Ince, 2017) the ΦID double redundancy is the pointwise double co-information at the samples whose marginal and full pointwise mutual informations share a sign (Mediano et al., 2021, Appendix, Definition 1; 2025, SI Appendix, Definition 2); phyid applies a different fifth condition (S3 Text)." |
| P9 | draft_v2.md:290 (head note) and S5_Text.md:27 | Theiler et al. 1992 (how it was checked) | **Not supported** by the audit record | Citation pass §B: no text of Theiler was obtained (ScienceDirect HTTP 429, OSTI blocked, no arXiv). Only its bibliographic record (20 Sep audit §6) and Prichard & Theiler (1994) p. 1 were used. "their abstracts" is true of Alexander-Bloch only (PubMed 29860082). The error comes from A5's own proposed text. | "…Alexander-Bloch et al. (2018) could not be obtained in full text and was checked against its abstract and bibliographic record only, and Theiler et al. (1992) against its bibliographic record only." |
| P10 | draft_v2.md:168 (A1 sentence, no year) | Luppi et al. 2022 | Wording: the subject is lost | The numbers are right (Table 1, p. 10). But after the shortening, "Its" follows sentences in which "its" means the study, so it reads as the observed gradient, which contradicts "against 0.22–0.54 for the observed gradient". | "The surrogate gradient's correlations with the six macroscale maps of their Table 1 were small (\|ρ\| ≤ 0.26) and, …" |
| P11 | draft_v2.md:166 | Huang 2018 pair is fine | Wording | "…(Huang et al., 2018), relative to placebo in this dataset, and within a placebo run with time" has no verb or direction for this dataset. It came from applying the Stage B edit literally. | "…(Huang et al., 2018); in this dataset it fell under DMT relative to placebo and rose within the placebo run with time; …" |

**A-items (task 3).**

Adopted exactly: A3, A6, A7, A10, A11, A12, A14, A18, A20, A23 and A24, plus the A3 Recommendations note.

Adopted with the Stage B prompt's edits or after a move:
- **A2:** second sentence drops "τ" and "and the series are".
- **A4:** second option, moved to S3 §10.
- **A5:** head note and S5 §5, but see P9.
- **A8:** in S3 §4; the numbers recomputed (0.73–0.97; ratio 22–146).
- **A9:** in Results 7, the Honari clause is verbatim and reordered.
- **A13:** the atom names were added.
- **A15:** the Introduction wording moved to S3 §10; the Results 7 wording follows Stage B.
- **A16:** Discussion, Methods and S3 §10.
- **A19:** main per Stage B; S3 §4 also fixed.
- **A21:** single quotes, but see P2.
- **A22:** moved to S3 §3 as "of this section".
- **A1:** main text, S3 §10 and notes row 1 all say "glycolytic index", but see P10.
- **A17:** superseded; "most exposed" appears nowhere.

No uncorrected wording from A1–A24 survives in any of the seven files. No A-item fix is missing from both the main text and the SI, with two exceptions:
- **A9 (Recommendations):** the costs clause was deleted rather than corrected. This is moot.
- **A26, second bullet:** the pass flagged it without proposing wording, and it is still open (P1). The Author-summary part of A26 was adopted exactly.

### (c) Not checkable here

| location | work | note |
|---|---|---|
| draft_v2.md:188 | Tian et al. 2020 | Indirect support: Singleton p. 8, ref. 82 |
| draft_v2.md:192 | Imperial-MIND-lab 2026 | The software is not available locally. The repo's scripts call `calc_PhiID(kind='gaussian', tau=1)`, pinned at 6c5f2e9. |
| draft_v2.md:208 | Alexander-Bloch et al. 2018; Váša et al. 2018 | |
| draft_v2.md:212 | Theiler et al. 1992 | Its null is a linear Gaussian process (Prichard & Theiler 1994 p. 1); "checks stationarity" is this paper's use of it. |
| draft_v2.md:224 | Wu et al. 2021 | The version "1.7.0" cannot be checked. Wu 2013 is supported. |
| draft_v2.md:264 | Cousineau 2005; Morey 2008 | |
| S3_Text.md:153 | Váša et al. 2018 | |
| supplementary.md:101 | Alexander-Bloch et al. 2018; Váša et al. 2018 | |
| captions_v2.md:19 | Cousineau 2005; Morey 2008 | |
| draft_v2.md:270 | Singleton et al. 2025 (partial) | Framewise displacement is not in Singleton's data statement, and "the release carries no licence file" cannot be checked: there is no local clone of DMT_NCT. |

### (d) Reference list

- **Coverage:** every main-text author–year citation has an entry, and 40 of the 41 entries are cited in the main text.
- **SI-only entry:** Faes et al. (2025) is cited only in S3 §10 and S5 §5 (and the head note). Its entry note correctly points to the S3 quotations.
- **Figures section only:** Cousineau (2005) and Morey (2008) are cited in the main text only in the Figure 4 legend.
- **Not in the list:** supplementary_cobidas.md (S4 Text) cites Nichols et al. (2017) inline, and it has no entry.
- **Head note is accurate except:**
  - Theiler et al. (1992): P9.
  - Minor: it names Arbabshirani's NIH manuscript and Faes's arXiv version, but not Murray et al. (2014), which was read in its advance-online PDF.

### (e) S5 history

The dates and contents in git log check out:
- **44cec4f:** the hypothesis is in CLAUDE.md, later renamed to analysis_record.md. The 20-region file's header reads `git=nogit`. I recomputed its DiD as −0.0994, negative in 12 of 14. prespecification_summary.md does not mention it.
- **33f0b33:** the "DECREASE … opposite to the stated hypothesis" quotation is verbatim, immediately above the rule.
- **84ea657:** "gamed either way" and the rtr outcome are there.
- **febf599:** windows 6–14.
- **b7e4595:** the first commit anywhere to mention "step contrast".
- **cb1b2cf:** −0.0809, "REFUTATION".
- **b4f98a8 / 477cccc:** 12:48 and 12:50 UTC.
- **9318997:** 08:47 UTC.
- **66e057a and 0b8d1a4:** both carry the direction reading (0b8d1a4 in its abstract).
- **Record entries:** 23 Sep 11:31 and 15:36 UTC, as cited.
- **a9d9ca4 / 90690f4:** 13 files, all `git=a9d9ca4`. The 172/73/59/227 s and 1,120 checks match the B21 outcome entry.
- **§6:** the other dates are right.
- **Quotations:** the §3 D2, D3 and D4 quotations and "No confirmatory claim attaches to any of them" are verbatim from the record.

Problems:
- **E1 (S5:7, time zone):** the 12–13 Sep times (10:29, 10:40, 11:07, 11:32, 11:36, and "10:15") are EEST (+03:00) but unlabelled. S5 labels its other times UTC and says the record is dated in UTC. Label them, or convert: 07:29, 07:40, 08:07, 08:32 and 08:36 UTC.
- **E2 (S5:31):** d51966e is listed as "17 Sep", but it was committed 16 Sep, 16:49 UTC. The review read it on 17 Sep.
- **E3 (S5:31):** d507728 is listed as "20 Sep", but it was committed 18 Sep, 15:46 UTC. The run at that commit was on 20 Sep.
- **E4 (S5:27):** "26 items needing a change, A1–A26" is inexact: A25 only lists pairs that could not be checked. Suggest "26 items not plainly supported (A1–A26)". The other counts (119 pairs 87/21/6/1/4; 21 claims 9/8/4; verification 16/2/2/0; 20 findings) are right.
- **E5 (S5:7, minor):** in 44cec4f, "Recorded here before any results were inspected" heads the analysis-choices section, not the hypothesis.
- **E6 (S5:3, unchanged, minor):** "every entry dated to the minute, UTC" is not true of the entries from 11–14 Sep, which are dated to the day only.
- **E7 (not checkable from git):** "written to disk seventeen minutes earlier" and "on disk at 10:15". The committed files and logs carry no timestamps.
- **E8 (main-text Figures paragraph, draft_v2.md:264):** it says the figures are "those the script wrote at the commit that carries them". In fact they were written at 526090d (the captions header says so) and committed in 66c6331.
