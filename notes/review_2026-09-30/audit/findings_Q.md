*Copy for the repository: quotations of the cited works longer than a few words are replaced by a description in square brackets with their page, as the passages themselves are not in the repository, and e-mail addresses by what they identify; paths of the planning session's scratch space are shortened to SP/; the opening sentence on where the report could not be saved is left out.*

I checked every correction Q01–Q31 (Q22a–Q28a and their mirrors Q22b–Q28b) and L05 in `sim/` (HEAD 6ae1cfa against 31f1153). Each was compared with its claim record and the cited PDFs, and S1 Text's file list with the repository code. Each new text appears exactly once. The a/b mirrors are identical, and S20 rows 1, 5, 6 and 8 and Table B item 3 match between `supplementary.md` and `notes/partB5_literature_v2.md`. Page numbers are PDF positions unless marked "printed".

There are 12 findings: 1 error, 4 inaccuracies, 7 wording. In one line each:
1. **Error, Q04:** dropping "by Singleton et al., 2025" brings back the ambiguity fixed on 22 September (Timmermann excluded four of twenty) and breaks S4 Text's D4 quotation.
2. **Inaccuracy, Q26/Q27:** the Introduction still says "six with a Gaussian estimator"; only four name one now that S20 marks Down and Zhang as our reading.
3. **Inaccuracy, Q20/Q30/L05:** S4 Text still calls Nichols 2017 "not read in full", contradicting Q20, the record and L05.
4. **Inaccuracy, Q09:** S1's file list omits the structural-connectome file that `scripts/00_verify.py` loads, and the two MATLAB scripts read as text.
5. **Inaccuracy, Q11:** the sentence still evaluates Ince's CCS "at the samples"; Ince defines it as an expectation under his maximum-entropy distribution.
6. **Wording, Q25:** "companion preprint" is our own word; neither paper cites the other.
7. **Wording, Q17:** "CCS redundancy is the primary analysis" names a redundancy function as an analysis.
8. **Wording, Q29:** "not checked again" implies an earlier check, and the note forgets that row 5 also uses the January 2026 version.
9. **Wording, Q22–Q28:** the S20 and partB5 headers still date all page numbers to the 20 September audit.
10. **Wording, Q30:** Alexander-Bloch 2018 was read in its NIH author manuscript, which is not said.
11. **Wording, Q04/Q09:** the Schaefer-100 identification rests on this repository's CBIG LUT file, which S1 does not name.
12. **Wording (optional), L05:** "every cited work" includes the software entry, which S5 excepts.

(a) Leaving the four competing-interests citations is justified; only the record's reason is worded loosely. (b) The record paragraph is accurate apart from minor points.

---

# Audit of the corrections Q01–Q31 and L05 (claim-by-claim check of 29–30 September 2026)

## Findings (most severe first)

**1. Q04 — `manuscript/draft_v2.md:192`; knock-on at `manuscript/si/S4_Text.md:12` and `:28`. Severity: error.**
- **What is wrong.**
  - Q04 drops "by Singleton et al., 2025" from "(six of twenty excluded for head movement …)". The parenthesis now follows "acquired by Timmermann et al. (2023):" and names nobody.
  - This undoes the fix from the citation pass of 22 September (`notes/review_2026-09-22/citation_pass_2026-09-22.md`, A23). That fix added the attribution because Timmermann et al., named just before, excluded a different number.
  - S4 Text D4 (`:12`) quotes Methods, Dataset as "six of twenty excluded for head movement by Singleton et al., 2025". The main text no longer contains those words.
  - S4 Text A6 (`:28`) points to Methods, Dataset for an exclusion "by the data authors", which the sentence no longer attributes.
- **Evidence.**
  - Singleton2025 p. 8: [the sentences stating that six of the 20 participants were discarded, leaving 14].
  - Timmerman2023 p. 9: [the sentence stating that four of the 20 participants were discarded].
- **Fix.** Restore "(six of twenty excluded for head movement by Singleton et al., 2025)". This makes D4 true again. If length matters, write "(six of twenty excluded by Singleton et al. for head movement)" and update D4 to match.

**2. Q26a/b and Q27a/b — `manuscript/draft_v2.md:25`. Severity: inaccuracy (an inconsistency the corrections created).**
- **What is wrong.**
  - The Introduction still says "seven state the … (MMI) redundancy function (Barrett, 2015; Mediano et al., 2021), six with a Gaussian estimator".
  - The six were Luppi 2022, 2024 and 2026, Gatica, Down and Zhang (citation pass of 22 September, A2).
  - Corrected S20 rows 6 and 8 now say Down and Zhang name no estimator, and that "Gaussian" is our reading.
- **Evidence.**
  - A Gaussian solver is named in:
    - Luppi2022 p. 14 [names the Gaussian solver of the JIDT toolbox];
    - Luppi2024 p. 20 (the same);
    - Luppi2026 p. 19 (the same);
    - Gatica2024 p. 15 [names a Gaussian MMI solver].
  - No estimator is named in:
    - Down2026 pp. 5–6 ("brain activity is suitably Gaussian" as the reason for MMI; no ΦID software or estimator in pp. 1–25);
    - Zhang2025 pp. 4–6 (MMI because linear Gaussian models describe fMRI; "JIDT (v1.5)" with no estimator).
- **Fix.** "… seven state the minimum-mutual-information (MMI) redundancy function (Barrett, 2015; Mediano et al., 2021), four of them naming a Gaussian estimator and two giving a reason we read as implying one (S20 Table, rows 6 and 8), and one uses …".

**3. Q20, with Q30 and L05 — `manuscript/si/S4_Text.md:87`; also `S5_Text.md:27` and `draft_v2.md:236`. Severity: inaccuracy.**
- **What is wrong.** S4's reference for Nichols et al. (2017) still ends "(bibliographic record checked against Crossref on 24 September 2026; not read in full)". Three places now contradict it:
  - Q20 describes the article from its full text.
  - The record says it was read on 29 September (`analysis_record.md:8323–8324`).
  - L05 now says every cited work was audited "against the full text … (S5 Text)". But S5 §5 (as extended by Q30) records only the seven works and the COBIDAS report.
- **Evidence.** The only copy is `b34/new/new_papers/Nichols2017.pdf`, the 10-page PMC author manuscript.
  - p. 2: [the article calls itself a Commentary on the issues met].
  - p. 3: the report's scope, [states the seven domains of practice], and [refers to the report's checklists].
- **Fix.**
  - `S4_Text.md:87`: "(bibliographic record checked against Crossref on 24 September 2026; read in full, in its author manuscript in PubMed Central, for the check of 29–30 September 2026)".
  - Q30's sentence in S5: add "; Nichols et al. (2017), cited in S4 Text, was read in full, in its author manuscript, for the same check".

**4. Q09 — `manuscript/si/S1_Text.md:5`. Severity: inaccuracy.**
- **What is wrong.** "It reads these files of the repository at 77af7aa: …" lists seven files, but the code reads more.
  - `scripts/00_verify.py:66–67` loads `data/Schaefer116_HCP_DTI_count.mat` (the structural connectome) and checks its shape (116, 116).
    - This script is step 00 of `run_all.sh` (`run_all.sh:43`).
    - The record's data check of 11 September lists the file (`analysis_record.md:62–63`).
  - `scripts/10_subject_alignment_check.py:47, 70–71` reads two of the release's MATLAB scripts as text, `scripts/01_gen_time_resolved_ce.m` and `scripts/02_global_ce_analyses.m`, to confirm the subject order.
  - Small point: `sch116_to_yeo.csv` holds 116 codes, 1–7 for cortex and 8 for the 16 subcortical regions (`scripts/11_regional_analysis.py:113`). "Each parcel's Yeo-7 network" is exact only for the cortex.
- **Evidence that the seven listed files are right.** Each is loaded at the path S1 Text gives:
  - `DMT_clean_mni_continuous_fullPreprocsch116.mat`: `scripts/00`, `01`, `09`, `10`, `11` and about thirty `notes/*.py`.
  - `intensity_ratings.mat`: `scripts/00`, `02`, `06`, `10`, `12`.
  - `FDlong.mat`: `scripts/00`, `06`, `10` and `notes/partB21_inference_revision.py`.
  - `RegressorLZInterpscrubbedConvolvedAvg.mat`: `scripts/03`, `10`.
  - `5HTvecs_sch116.mat`: `scripts/00`, `11` and `notes/rev_regional_phir.py`.
  - `sch116_to_yeo.csv`: `scripts/11_regional_analysis.py:110`.
  - `fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat`: `scripts/11_regional_analysis.py:80`, `notes/partB11`, `partB22`, `rev_regional_phir`. It holds 10,000 rotations (`results/run_11_ts_gsr.log`).
- **Fix.**
  - Add "`data/Schaefer116_HCP_DTI_count.mat` (the structural connectome, whose shape the data check `scripts/00_verify.py` verifies; no result uses it)".
  - If the list is meant to be complete, also add "and, as text, `scripts/01_gen_time_resolved_ce.m` and `scripts/02_global_ce_analyses.m` (the subject-order check)".
  - Write "(each region's Yeo-7 network; 8 for the subcortex)".

**5. Q11 — `manuscript/si/S3_Text.md:104`. Severity: inaccuracy (the fix is partial).**
- **What is wrong.**
  - The record named the difference as: Ince evaluates the rule under his maximum-entropy distribution, "not at the observed samples as our sentence says".
  - The corrected sentence now gives P̂ for the local quantities. But it still defines the redundancy as "the local co-information at the samples where … share a sign, and zero elsewhere".
  - Ince's I_ccs is the expectation under P̃, not an average over the observed samples.
  - For Gaussian data the sample average estimates that expectation; the text does not say so.
- **Evidence.**
  - Ince2017 p. 12, Definition 1 / Eq. 30: I_ccs is the sum of p̃ times Δs h_com, [defines it as the expectation of the local redundancy values].
  - P̂ is Definition 2, p. 13.
- **Fix.** "Under CCS (Ince, 2017) the single-target redundancy is the expectation, under Ince's maximum-entropy distribution P̂, of the local co-information where the constituent local mutual informations and the co-information share a sign (zero elsewhere); for two Gaussian sources P̂ is the fitted Gaussian (below), and here, as in phyid, the expectation is estimated by the average over the samples."

**6. Q25a/b — `manuscript/supplementary.md:1668` and `notes/partB5_literature_v2.md:17`. Severity: wording.**
- **What is wrong.** "The companion preprint": "companion" is our own characterisation.
  - The claim record itself notes "'Companion' is our word".
  - A full-text search finds no citation of "Convergent transcriptomic …" in Luppi2025 (version of 10 January 2026), and no citation of "Comprehensive profiling …" in Luppi2026.
- **Fix.** "A preprint by the same first author and group on anaesthetised brain dynamics …", or add "(a companion study in our reading; neither cites the other)".

**7. Q17 — `manuscript/si/S3_Text.md:428`. Severity: wording.**
- **What is wrong.** "CCS redundancy is the primary analysis of one of the empirical fMRI studies of S20 Table (Luppi et al., 2023)". A redundancy function is not an analysis. The count problem the record named is fixed.
- **Evidence.** Luppi2023 p. 12: CCS with a plug-in estimator on mean-binarised signals, [states that every analysis of the paper uses it].
- **Fix.** "… and one of the empirical fMRI studies of S20 Table uses CCS redundancy in its primary analysis (Luppi et al., 2023)". This matches the Introduction's wording at `draft_v2.md:25`.

**8. Q29 — `manuscript/supplementary.md:1688`. Severity: wording.**
- **What is wrong.**
  - "whether version 1 had the same six species was not checked again": "again" implies an earlier check.
    - The check of 25 September covered only the two quotations.
    - The claim record says the question "cannot be checked from the folder".
  - "from which Table B's description of the preprint is taken": row 5's reading (Q25: six species, "all its contrasts") also comes from that version.
- **Fix.** "… from which S20 Table's descriptions of the preprint (Table A, row 5; Table B, item 3) are taken; whether version 1 has the same six species and fifteen contrasts was not checked".

**9. Q22–Q28 (a and b) — `manuscript/supplementary.md:1658` and `notes/partB5_literature_v2.md:1, 3, 7`. Severity: wording.**
- **What is wrong.** Both headers date the page numbers to the audit of 20 September.
  - S20's source note says page numbers are PDF indices "as the citation audit of 20 September 2026 gives them".
  - The partB5 header says every cell was verified against the PDF with pages as in that audit, which "located every cell below".
- **The cells that now come from the check of 29–30 September:**
  - row 1 (Raut p. 2);
  - row 5 (pp. 3, 35 and 37, and its description of the preprint);
  - rows 6 and 8;
  - Table B, item 3.
  - For the preprint, that check read the version of 10 January 2026.
- **Fix.** Add to both headers: "the cells revised after the claim-by-claim check of 29–30 September 2026 (rows 1, 5, 6 and 8 and Table B, item 3) take their page numbers from that check".

**10. Q30 — `manuscript/si/S5_Text.md:27`. Severity: wording.**
- **What is wrong.** The added sentence names the versions read for Tian et al. (2020) and Váša et al. (2018). It does not say that Alexander-Bloch et al. (2018) was read in its NIH author manuscript. The same paragraph does name Arbabshirani et al. (2014)'s author manuscript.
- **Evidence.** The only copy, `b34/new/new_papers/AlexanderBloch2018.pdf` (26 pages), is headed "HHS Public Access / Author manuscript".
- **Fix.** "…, Alexander-Bloch et al. (2018) in its NIH author manuscript, Tian et al. (2020) in its *Nature Neuroscience* version …".

**11. Q04 and Q09 — `manuscript/si/S1_Text.md:5` (supporting `draft_v2.md:192`). Severity: wording.**
- **What is wrong.** Q04's rationale says "S1 Text names the file" for the 100-parcel resolution, but S1 Text names no file of the Schaefer release. What establishes the 100-parcel, 7-network version is this repository's `data/Schaefer2018_100Parcels_7Networks_order.lut`:
  - it was copied from CBIG (`README.md:79`);
  - `scripts/11_regional_analysis.py:107–112` reads it and asserts that it matches `sch116_to_yeo.csv`.
- **Evidence.**
  - Schaefer2018's text describes only the 400–1,000-area versions (p. 6). Its abstract (p. 1) says only that multiresolution parcellations are publicly available.
  - Singleton p. 8 gives 100 cortical regions, citing its ref. 81, which is Schaefer et al. (p. 12).
- **Fix.** "The cortical parcels are the 100-parcel, 7-network version (`data/Schaefer2018_100Parcels_7Networks_order.lut` of this repository, copied from that release) of the multiresolution parcellations released with Schaefer et al. (2018)."

**12. L05 — `manuscript/draft_v2.md:236`. Severity: wording (optional).**
- **What is wrong.** "the full text of every cited work (S5 Text)": the reference list includes the software entry Imperial-MIND-lab (2026) (`draft_v2.md:298`). S5 §5 excepts it: "every entry except the software was read in full". Its code was read.
- With finding 3 fixed, the rest of L05 holds.
- **Fix.** "… against the full text of every cited work (for the software, its code; S5 Text)".

## (a) The four uncorrected differences (competing interests, `draft_v2.md:260`)

**Verdict: leaving them is justified.**
- **Why no correction is needed.** The four records differ only in that the papers do not name the Cognition and Consciousness Imaging Group. The statement cites the papers to identify the studies, not for the group membership. Membership is the author's own disclosure.
- **What the papers show.** Each gives Luppi, Menon and Stamatakis at the Division of Anaesthesia:
  - Luppi2022 p. 1;
  - Luppi2023 p. 1;
  - Luppi2024 p. 1;
  - Luppi2026 p. 26.
- **The group name.** It appears in none of the four papers.
- **The count of four.**
  - No other examined study (S20 rows 1–9) has an author at the Division of Anaesthesia. In Mediano 2025, Luppi's affiliations (p. 11) do not include it.
  - The 2025 preprint is by Division members, but it is an input to Table B, not an examined study.
  - So "four" holds.
- **Nit in the record's reason** (`analysis_record.md:8362`). It says "the studies whose authors the statement names as members of the group", but the statement names no author. Suggested: "the citations identify the studies that, by the statement's own disclosure, members of the group authored; the papers show only their authors' affiliation with the Division of Anaesthesia".

## (b) The record entry's paragraph listing the corrections (`analysis_record.md:8345–8364`)

**Accurate in its counts and in almost every item:**
- 32 of the 36 differences corrected; 4 left.
- Each described change matches the replacement entries.
- The Result counts match DATA: 204 sentences and cells; 303 claims; 43 works; 45 PDFs; 248, 36 and 19 by verdict; 266, 5, 1, 2 and 29 by firsthand status.

**Points that are inexact:**
- **"Ince's sign rule is evaluated under his maximum-entropy distribution."** The text still evaluates "at the samples" (finding 5).
- **"Barrett's rule is for a univariate target, the joint-target nodes following Mediano et al."** This describes Q10. Q05 in the main text only adds Mediano et al. (2021) to the citation. Acceptable as a summary.
- **The Luppi et al. (2025) items leave out two parts of Q25/Q28:**
  - the finding concerns features that change alike in all 15 contrasts;
  - the step from that finding to r₁ is now marked as ours.
- **"Q01–Q31":** L05 is also a correction of this check; the paragraph covers it only in its last clause.
- **"S5 Text §5 records … that every cited work has now been read in full":** S5 records the seven works and the COBIDAS report. S4 still calls Nichols 2017 "not read in full" (finding 3).
- **The reason for the four uncorrected citations:** see the nit in (a).

## Corrections checked and found correct

- **Q01.**
  - Luppi2023 p. 3 (Fig. 1 caption): 1 TR (2 s), with 4 TRs as a check.
  - Down2026 p. 5: one time step (TR) at TR 3 s.
  - No other study states a lag value.
- **Q02.** Varley2024 p. 7, Eqs. 11–12, give the identity for the independent pair. It is consistent with `draft_v2.md:49` and `S3_Text.md:428`.
- **Q03.** Singleton2025 p. 11 states the release but does not call the data pseudonymised. "Pseudonymised" now sits outside the citation and rests on S1 Text.
- **Q04, apart from findings 1 and 11.**
  - The run layout and the two variants are now cited to S1 Text.
  - Schaefer p. 6 clusters the parcels into the networks of Yeo et al. (2011), and Singleton p. 10 uses the seven Yeo networks.
- **Q05 and Q10.**
  - Barrett p. 5, Eq. 26: univariate target.
  - Barrett p. 6: [the common PID does not extend to a multivariate target].
  - Mediano2021 p. 10 uses [a multi-target extension of Barrett's MMI measure].
  - Its Axiom 1 (p. 16) and Appendix (p. 23) include the joint-target single-target redundancies.
  - Consistent with the Limitations (`draft_v2.md:180`).
- **Q06.** Mediano2021 p. 24 gives the atoms as the solution of a linear system (the Möbius inversion). No "sign constraint" claim remains anywhere.
- **Q07, Q14 and Q15.**
  - Vasa2018 p. 5 (printed 285) describes the regional test with 10,000 rotations on its 308 regions.
  - The SI p. 7 describes the rotation procedure.
  - Line 2 of the release's function names `rotate_parcellation` as the source of the permutations.
  - All Váša mentions in the texts are now consistent.
- **Q08.** Singleton p. 11's list of released data has no framewise displacement. The sentence now makes the files the repository's and points to S1 Text.
- **Q09, apart from findings 4 and 11.** The four variants and the 14 × 2 × (116 × 840) layout match `analysis_record.md:45–49` and `scripts/00_verify.py:42–50`.
- **Q12.** Mediano2025_SI p. 4 writes "I(X; Y)". The pointer "(below)" resolves.
- **Q13.** Ince p. 13: Definition 3 uses pairwise target–predictor marginals and comes from a previous version. The conditional independence is now marked as our reading.
- **Q16.** Zhang reports no redundancy result. Down reports both atoms. Nago covers SZ, ASD and ADHD.
- **Q18.** Luppi2022 p. 3 is printed 773. p. 14 is the online Methods, with no printed number.
- **Q19.** "Mean-binarised" appears in Luppi2022 p. 14 and Luppi2023 p. 12. Binarising once is now marked as our reading.
- **Q20, apart from finding 3.** Nichols pp. 2–3 give the Commentary, the scope, the seven domains and the checklists. 20(3): 299–303 is right.
- **Q21.** Consistent with Q03, with Q09 and with S4 row Sh5 (`S4_Text.md:78`).
- **Q22a/b.** Raut p. 2 is printed 20891.
- **Q23a/b.** Luppi2026:
  - p. 37: five sessions, naming four;
  - p. 35: 20 recruited, 16 completed, N = 15, three anaesthesia levels;
  - p. 3: deep anaesthesia.
- **Q24a/b.** The four marmosets are on pp. 3 and 35. TR 2,000 ms, 155 repetitions and 9.4 T are on p. 38.
- **Q25a/b, apart from finding 6.** Luppi2025 (version of 10 January 2026):
  - six species: p. 1 and p. 3; zebrafish N = 7 and nematode N = 10 on p. 4;
  - the quotation is exact (p. 5), and the 485 features are consistent over 15 contrasts;
  - the r₁ step is marked conditional;
  - the same source studies and Ns appear in the preprint (p. 4 and its Methods, including five macaques in the DBS dataset) and in Luppi2026 (pp. 3, 5, 35);
  - HRF deconvolution is absent from both; Luppi2026 mentions only a cell-type deconvolution (printed 792).
- **Q26a/b and Q27a/b as table cells.** The cells are accurate; see finding 2 for the main text.
- **Q28a/b.** Luppi2025:
  - hctsa: pp. 3–4;
  - n = 15: p. 4; TR 1.838 s: p. 20;
  - calcium imaging for zebrafish and nematode: p. 3;
  - the Fig. 3e caption quotation is exact (p. 7).
- **Q29, apart from finding 8.** The version date is right.
- **Q30, apart from findings 3 and 10.** All seven full texts exist and are complete, and "(below)" resolves within §5.
- **Q31.**
  - `perm_sphere_p_al857.m`, lines 3–4 and 48–58: each map is permuted in turn, the one-sided p (strict inequality) is taken in the direction of the observed correlation, and the two are averaged.
  - `scripts/11_regional_analysis.py:272–281` does the same, as does `notes/partB11_regional_sts_r1.py:118–124`.
  - The table columns are headed "[Váša p]".
- **L05, apart from findings 3 and 12.** Consistent with S5 §5 for the main reference list.
