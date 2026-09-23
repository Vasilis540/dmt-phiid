# Citation pass of `manuscript/draft_v2.md`, S3 Text and S5 Text against the full texts — 22 September 2026

Text audited: `dmt-phiid/manuscript/draft_v2.md`, `manuscript/si/S3_Text.md`, `manuscript/si/S5_Text.md` at commit 0b8d1a4 (21 Sep 2026, "Round 15"; working tree clean). Every author–year citation in the Introduction, Results, Discussion, Materials and methods, the table captions, the Figures section and the References head note, and every citation in S3 and S5 Text, was checked against the full text in `papers/` (text extracts in `papers/txt/`, reading-order extracts in `audit/*.nolayout.txt`, the OCR of the Luppi et al. (2026) Reporting Summary in `audit/Luppi2026.reporting_summary.ocr.txt`). Where a page was hard to read in the extract it was rendered and read as an image (Afyouni 2019 p. 4; Barrett 2015 p. 8). The seven references with no file in `papers/` were searched for on the web on 22 September 2026 (Section B).

Conventions. "p. N" is the PDF page index (as `find.py` prints it); the journal's printed page is given in brackets where it helps. Verdicts: SUPPORTED; SWQ = SUPPORTED WITH QUALIFICATION; NOT SUPPORTED; MISATTRIBUTED; CANNOT CHECK. The previous audit (`citation_audit_2026-09-20.md`) was used for page leads only; every item below was re-verified against the source as the sentence is now worded.

Counts (119 sentence × cited-work pairs): SUPPORTED 87; SWQ 21; NOT SUPPORTED 6; MISATTRIBUTED 1; CANNOT CHECK 4. Main text 94 pairs (68 / 20 / 3 / 1 / 2), S3 Text 21 (17 / 1 / 2 / 0 / 1), S5 Text 4 (2 / 0 / 1 / 0 / 1). Quotations attributed to a source: 7 checked, 6 verbatim, 1 not (A4). The universal and negative claims are counted separately in Section C (21 claims). Prichard (1994), Wolff (2022) and Zilio (2021) are not cited anywhere in `draft_v2.md`, S1–S5 Text, `supplementary.md` or `captions_v2.md`.

---

## A. Every item that is not plainly SUPPORTED

Ordered by severity. For each: location and sentence, the problem, the evidence, and a proposed wording the source supports.

### A1. Discussion, "The literature", Luppi et al. (2022) paragraph — the one surrogate exception is misnamed and the observed-gradient range is wrong. NOT SUPPORTED.

Sentence: "Its correlations with the macroscale maps were small and, with one exception (gyrification index, ρ = 0.26, spin p = 0.028), not significant, against 0.40–0.54 for the observed gradient."

Problem 1. "GI" in Luppi et al. (2022) is the **glycolytic index**, a PET measure of aerobic glycolysis, not a gyrification index. The word "gyrification" does not occur anywhere in the paper.
Evidence: p. 9: "the cortical distribution of glycolytic index (GI), a measure of AG obtained from PET measurements of cerebral metabolic rates for oxygen and glucose (Spearman ρ = 0.40, P < 0.001, Pspin = 0.013; Fig. 7a)"; Fig. 7a legend: "the mean regional estimate of AG based on PET measurements of cerebral metabolic rates for oxygen and glucose (GI)"; p. 34: "The maps of average regional Glycolytic Index (GI) are available as Supplementary Materials from Vaishnavi et al. (2010)". Table 1, p. 10 [780], row "GI", phase-randomised column: "Spearman ρ = 0.26, Pspin = 0.028".

Problem 2. The observed gradient's six correlations in Table 1 are 0.40 (expansion), 0.48 (HAR-Brain), 0.22 (PET synaptic density PC1, Pspin = 0.053), 0.28 (PC2, Pspin = 0.059), 0.40 (GI) and 0.54 (receptor diversity). The range is 0.22–0.54; 0.40–0.54 is the range of its four *significant* associations only. For the two PET components the surrogate's 0.17 and 0.21 are close to the observed 0.22 and 0.28.
Evidence: Table 1, p. 10 [780]: original gradient "Spearman ρ = 0.40, Pspin = 0.010 / 0.48, 0.002 / 0.22, 0.053 / 0.28, 0.059 / 0.40, 0.013 / 0.54, P < 0.001"; phase-randomised "0.09, 0.277 / 0.01, 0.492 / 0.17, 0.114 / 0.21, 0.129 / 0.26, 0.028 / −0.16, P = 0.328".

Proposed: "Its correlations with the six macroscale maps of their Table 1 were small (|ρ| ≤ 0.26) and, with one exception (the glycolytic index, a PET measure of aerobic glycolysis: ρ = 0.26, spin p = 0.028), not significant, against 0.22–0.54 for the observed gradient (0.40–0.54 for its four significant associations: cortical expansion, HAR-Brain gene expression, the glycolytic index and receptor diversity)."
Related files: the same "gyrification" error is in `notes/partB5_literature_v2.md` Table A row 1 ("only gyrification, ρ = 0.26, spin p = 0.028, significant"), which S3 Text cites as the applicability table. Both errors originate in the 20 September audit's F9 text, which S5 Text §3 says was "adopted as written".

### A2. Introduction ¶1 — universal claim about the studies' estimator is contradicted by one of the two studies cited in the same sentence. NOT SUPPORTED (pair with Luppi et al., 2023).

Sentence: "The studies whose settings could be read (S3 Text) use the Gaussian estimator with the MMI redundancy function (Barrett, 2015; Mediano et al., 2021) at a single lag — one TR where the lag is stated (Luppi et al., 2023; Down et al., 2026) — on BOLD series whose lag-1 autocorrelation is high because of haemodynamic smoothing and band-pass filtering."

Problem: all nine studies were read (Discussion), so "the studies whose settings could be read" are the nine, and they do not all use the Gaussian estimator with MMI. Luppi et al. (2023), cited in this very sentence, uses CCS with a plug-in estimator on mean-binarised signals as its primary analysis; Tarchi et al. (2026) states no redundancy function or estimator; Nago et al. (2026) states MMI but not a Gaussian estimator. The same Introduction says one paragraph later that the ΦID authors moved "in some studies, towards CCS redundancy (Luppi et al., 2023)".
Evidence: Luppi 2023 p. 12: "Here, we follow the 'common change in surprisal' (CCS) method (Ince, 2017). For all the analyses in the paper we compute information-theoretic quantities for each pair of brain regions, using a standard plug-in estimator applied to the mean-binarised BOLD signals. To validate our results, we also replicated them using continuous instead of discrete signals and the Gaussian solver implemented in the JIDT toolbox (Lizier, 2014). Likewise, we replicate our results using an alternative definition of redundancy known as the minimum mutual information (MMI)". Tarchi p. 3: "Integrated information decomposition of timeseries was then through specific software previously released (Mediano et al. 2021; ΦID—Integrated Information Decomposition, 2025)" (no redundancy function, estimator or lag stated). Nago p. 4: "we adopted the Minimum Mutual Information (MMI) as the redundancy measure" with the Imperial-MIND-lab toolbox; "Gaussian" appears only for the smoothing kernel (p. 3). Gaussian and MMI both stated: Luppi 2022 p. 14, Luppi 2024 pp. 19–20, Luppi 2026 p. 19, Gatica p. 13, Down pp. 5–6, Zhang pp. 4–5. The lag clause is supported (Section C, C2).
Proposed: "Of the nine studies read (S3 Text), seven state the MMI redundancy function (Barrett, 2015; Mediano et al., 2021), six of them with a Gaussian estimator; Luppi et al. (2023) use CCS on binarised signals, with Gaussian and MMI validations, and Tarchi et al. (2026) state neither. Where the lag is written it is a single lag τ, one TR where its value is stated (Luppi et al., 2023, with four TRs as a check; Down et al., 2026), and the series are BOLD series whose lag-1 autocorrelation is high because of haemodynamic smoothing and band-pass filtering."
The Barrett (2015) and Mediano et al. (2021) pairs of this sentence are SUPPORTED as sources for the MMI function; the Down et al. (2026) pair is SUPPORTED (p. 5).

### A3. Methods, Estimator — the general effective-sample-size formula is not Bartlett (1935). MISATTRIBUTED (Bartlett, 1935); the Afyouni et al. (2019) pair is SUPPORTED.

Sentence: "By Bartlett's variance formula the effective sample size of a correlation between two series with these autocorrelations is n / (1 + 2 Σ_k ρ_k²) (Bartlett, 1935; Afyouni et al., 2019); over the six lags of the pooled placebo function (...) the denominator is 3.3, so a 60-TR window holds about 18 effective samples."

Problem: Bartlett (1935) derives only the AR(1) (Markov) case, var(r) ≈ (1/n)(1 + ρ₁ρ₂)/(1 − ρ₁ρ₂). The general form for an arbitrary autocorrelation function, applied here to a six-lag function that decays faster than geometric and turns negative, is attributed by Afyouni et al. — the co-cited source — to Quenouille (1947), building on Bartlett (1946), and the form n/(1 + 2 Σ ρ_k²) with a single shared ACF is their Eq. 8 ("G-Q47"). The numbers differ materially: Bartlett's AR(1) form at ρ₁ = 0.868 gives about 8 effective samples in a 60-TR window, the general form 18.
Evidence: Bartlett 1935 p. 2 [537]: "We suppose any observation in a time-series is correlated with the preceding observation to an extent ρ1. It will consequently be correlated with the preceding observation but one to an extent ρ1² and so on ... the variance of the sample correlation between the two series is (1/n)((1 + ρ1ρ2)/(1 − ρ1ρ2)) approximately". Afyouni p. 2 [610]: "In his 1935 paper, Bartlett proposes a variance estimator of sample correlation coefficients based on a AR(1) model ... In later work he proposed a more general estimator which accounts for higher order AR models (Bartlett, 1946)"; p. 4 [612]: Eq. (6) "B35" = N((1 + ρXX,1ρYY,1)/(1 − ρXX,1ρYY,1))⁻¹ for "uncorrelated (ρ = 0) AR(1) time series"; "Building on work of Bartlett (1946), Quenouille (1947) proposed a more general EDF that allowed for any form of autocorrelation" Eq. (7); "In neuroimaging, a global form of Eq. (7) has been used ... N̂ = N(Σ_{k=−∞}^{∞} ρ²GG,k)⁻¹ (8)"; Table 1: "Q47 — Eq. (8) — Quenouille (1947) & Bartlett (1946)".
Proposed (no new reference needed): "The effective sample size of a correlation between two series that share these autocorrelations is n / (1 + 2 Σ_k ρ_k²), the global form of the effective-degrees-of-freedom estimator reviewed by Afyouni et al. (2019, their Eq. 8; Bartlett, 1935, gave the AR(1) case); over the six lags ...". If the authors prefer to cite the origin, add Quenouille (1947) and Bartlett (1946) and write "(Quenouille, 1947; Afyouni et al., 2019, Eq. 8)".
Note on the Recommendations pair "with the effective sample size it implies (Bartlett, 1935; Afyouni et al., 2019)": SUPPORTED — Bartlett's AR(1) form is exactly the size a lag-1 autocorrelation implies — but a reader applying it will get about 8 effective samples per 60-TR window where the Methods report 18; consider "with the effective sample size computed from the autocorrelation function (Afyouni et al., 2019; the AR(1) case is Bartlett, 1935)".

### A4. Introduction ¶2 — a quotation of Faes et al. (2025) is not verbatim. SWQ (substance supported; quotation altered).

Sentence: "Faes et al. (2025) state the general problem — PID applied to time series rests on an implicit i.i.d. assumption 'typically not tested in practice and often violated', temporal correlations have 'a profound impact' on the lag-zero decomposition, and lagged PIDs on ad hoc variables cover only 'specific portions of the system dynamics' — and propose a rate-based decomposition as the remedy."

Problem: the source reads "is typically not tested in practice and is often violated"; the quoted string drops "is" before "often" inside the quotation marks. The other two quotations are verbatim.
Evidence: Faes 2025 p. 1: "However, the i.i.d. assumption is typically not tested in practice and is often violated in applications of information decomposition where the analyzed data exhibit temporal correlations [8–10]"; "showing that the presence of temporal correlations has a profound impact on the multivariate information shared at lag zero by multiple random processes (Fig. 1)"; "applications of the PID to time-lagged variables selected ad-hoc from the processes (e.g.,[5, 11, 12]) are inherently focused on specific portions of the system dynamics".
Proposed: "... an implicit i.i.d. assumption 'typically not tested in practice and ... often violated' ..." or, better, "... an implicit i.i.d. assumption that 'is typically not tested in practice and is often violated' ...".
Caveat: the folder's PDF is the arXiv version ("Dated: October 7, 2025"); the reference cites the *Physical Review Letters* version. Check the three quotations against the PRL text, or cite the arXiv version for them.

### A5. References head note (and S5 Text §5) — "every entry ... read in full" is not true of seven entries. NOT SUPPORTED.

Head note: "[Every entry except the software (Imperial-MIND-lab, 2026) was read in full from the publisher's or preprint server's PDF on 20 September 2026, including the SI Appendix of Mediano et al. (2025); ...]". S5 Text §5 repeats it ("every entry except the software was read in full from the publisher's or preprint server's PDF on that day").

Problem: seven entries had no full text on 20 September (Theiler et al., 1992; Alexander-Bloch et al., 2018; Váša et al., 2018; Tian et al., 2020; Wu et al., 2021; Cousineau, 2005; Morey, 2008); the 20 September audit (§6) records only bibliographic checks for them. Section B gives what could be obtained today. Two further qualifications: (i) the supplementary materials of six of the nine applicability-table studies were not in the folder (Luppi et al. 2022 Supplementary Tables; Luppi et al. 2023 supplementary figures and tables, e.g. Figs S1, S3, S4 and Tables S1, S3; Luppi et al. 2026 Supplementary Methods, Figures and Tables; Down et al. 2026 appendix section 6; Nago et al. 2026 Additional File, Tables S1–S4 and Figs S1–S2; Tarchi et al. 2026 Supplementary Materials, Table S2 and Fig. S1), so "read in full" holds for the main articles only; (ii) three PDFs are not the version of record: Arbabshirani et al. (2014) is the NIH author manuscript, Faes et al. (2025) the arXiv version, Murray et al. (2014) the advance-online PDF.
Proposed: "[Every entry except the software was read in full (main article; supplementary materials only where named) on 20 September 2026 from the publisher's or preprint server's PDF, including the SI Appendix of Mediano et al. (2025); Arbabshirani et al. (2014) was read in its NIH author manuscript and Faes et al. (2025) in its arXiv version. The exceptions are seven entries added on 20 September: Cousineau (2005), Morey (2008) and Wu et al. (2021) were read in full on 22 September 2026 from the publishers' open-access pages, Tian et al. (2020) from its bioRxiv preprint (v2), and Váša et al. (2018) in its Methods and Results on the publisher's page; Theiler et al. (1992) and Alexander-Bloch et al. (2018) could not be obtained in full text and were checked against their abstracts and bibliographic records only. Bibliographic details ...]". Make the same change in S5 Text §5.

### A6. Discussion, "The literature" — "it is the one place the table argues against the mechanism". NOT SUPPORTED (universal claim; the Down et al. 2026 pair itself is SUPPORTED).

Sentence: "... so on the family synergy and redundancy moving in opposite directions (Down et al., 2026) is the q signature or a mixture, not the r₁ signature; that is a statement about the family, and it is the one place the table argues against the mechanism."

Problem: Tarchi et al. (2026) report the same opposite-direction pattern, and the applicability table's own row 9 reads it the same way ("the q signature or a mixture (as for row 6)"). The paragraph also calls the Luppi et al. (2022) surrogate result "evidence against the exposure". So the table argues against the r₁ mechanism in at least two rows, and the text has two "only" claims that overlap.
Evidence: Down p. 1: "a striking synergy reduction across the entire brain, in concert with widespread redundancy increases". Tarchi pp. 5–6: region-wise classification "mostly by leveraging lower integrated information (Φ), lower synergy, and disrupted, albeit mostly higher, redundancy in patients with schizophrenia"; p. 4: "No significant difference was observed for global information metrics." `notes/partB5_literature_v2.md` row 9: "the pattern of lower synergy with mostly higher redundancy is, on the family, the q signature or a mixture (as for row 6)".
Proposed: "... so on the family synergy and redundancy moving in opposite directions (Down et al., 2026; regionally, Tarchi et al., 2026) is the q signature or a mixture, not the r₁ signature; those are statements about the family, and they are where the table's reading runs against the r₁ mechanism alone, the surrogate test of Luppi et al. (2022) being the one empirical evidence against the exposure."

### A7. S3 Text §2 — the double co-information is misdescribed. NOT SUPPORTED (sentence attributed to Mediano et al., 2021, 2025 via the preceding sentence).

Sentence: "The double co-information is the signed sum, an inclusion–exclusion over the lattice, of the local mutual informations at the fifteen nodes of the product lattice other than its bottom node rtr (the sixteen atom positions, formed as the product of the past and future redundancy lattices)."

Problem: in Mediano et al.'s definition the term at each node is the *pointwise redundancy function*, which is a local mutual information at nine nodes and a local single-target CCS redundancy (Ince, 2017) at the six nodes with two separate sources or two separate targets ({1}{2}→{1}, {1}{2}→{2}, {1}{2}→{12}, {1}→{1}{2}, {2}→{1}{2}, {12}→{1}{2}). The repository's own code computes it that way (nine local MIs plus six `_ccs_red` terms), and only with those six terms does c ≡ rtr − sts hold.
Evidence: Mediano 2021 p. 24 (Appendix III), Eq. (5): "c(x; y) := Σ_{α→β∈A2} (−1)^{f(α,β)+1} i∩^{α→β}(x; y), where i∩^{α→β}(x; y) is the pointwise redundancy function, A2 is the set of nodes in the product lattice excluding the lowest node ... Note that i∩^{α→β}(x; y) above corresponds to the standard pointwise mutual information and a single-target PID redundancy function, which we take here to be the usual CCS function as defined by Ince [7]"; the same text is in Mediano 2025 SI p. 3, Eq. (6). `notes/rev_phiid_fast.py`, `ccs_local_knowns`: "D = (−I_xta − I_xtb − I_yta − I_ytb + I_xtab + I_ytab + I_xyta + I_xytb − I_xytab + R_xyta + R_xytb − R_xytab + R_abtx + R_abty − R_abtxy)".
Proposed: "The double co-information is the signed sum, an inclusion–exclusion over the product lattice, of the pointwise redundancy function at its fifteen nodes other than the bottom node rtr: the local mutual information at the nine nodes whose past and future sets are each a single set, and the local single-target CCS redundancy (Ince, 2017) at the six nodes with two separate past or two separate future variables (Mediano et al., 2021, Appendix, Eq. 5; 2025, SI Appendix, Eq. 6)."

### A8. S3 Text §4 — the range of ideal band-pass r₁ over the published studies is out of date. NOT SUPPORTED (numbers attributed to the studies' settings).

Sentence: "the lag-1 autocorrelation of ideal band-passed white noise at the band-pass and TR settings of the published studies whose settings are stated is 0.78–0.93 (`notes/partB5_literature.md`, Table B; ...) ... at those lower bounds the derivative ratio is 25–60 at |q| = 0.25, and it rises with r₁ (131 at 0.97)."

Problem: the sentence cites the superseded 14 September table. With the settings now read from the full texts, and as S3 Text's own last section lists them, the range is 0.73–0.97 (human datasets 0.78–0.97), and the ratio at |q| = 0.25 is 22–146.
Evidence (all verified in the PDFs; values recomputed with the ideal band-pass formula): 0.008–0.09 Hz at TR 2 s → 0.781 (Luppi 2023 pp. 10–11; Luppi 2024 pp. 16–18; Nago p. 3; Tarchi p. 3); at 1.838 s → 0.813 (Luppi 2026 Reporting Summary, OCR pp. 37–39); at 0.72 s → 0.970 (Luppi 2022 p. 13); 0.0025–0.05 Hz at 2 s → 0.932 (Gatica p. 13), 2.4 s → 0.903 and 1.25 s → 0.973 (Luppi 2026 macaque, OCR), 2.6 s → 0.887 (Luppi 2022 macaque, p. 13–14), 3 s → 0.851 (Down pp. 3–4); 0.01–0.1 Hz at 2.0 / 1.0 / 1.2 s → 0.730 / 0.928 / 0.898 (Luppi 2026 marmoset and mice, OCR). Closed form at |q| = 0.25: |∂sts/∂r₁| / |∂sts/∂q| = 22.3 at 0.73, 24.9 at 0.78, 131 at 0.97, 146 at 0.973.
Proposed: "... is 0.73–0.97 across the datasets of the published studies whose settings are stated (0.78–0.97 for the human datasets; `notes/partB5_literature_v2.md`, Table B item 2) ... at those lower bounds the derivative ratio is 22–146 at |q| = 0.25, rising with r₁."

### A9. Results 7 and Recommendations — Honari et al. (2019) is cited for a cost of prewhitening that it raises as a possibility and did not find. SWQ (2 pairs).

Results 7: "Prewhitening is also not free: it can remove haemodynamic structure that carries neural information (Honari et al., 2019), ..." Recommendations: "... and prewhitening carries its own costs (Honari et al., 2019; Cliff et al., 2021)."

Problem: Honari et al. state the concern conditionally, report that their simulation built to test it found no detrimental effect, and themselves adopt prewhitening. Cliff et al. do show a cost (false-positive rate worse after prewhitening).
Evidence: Honari p. 10: "Alternatively, one can attempt to remove its influence prior to analysis by prewhitening the data. This is the approach we have taken in this work ... the autocorrelation present in the signal is partially due to physiological noise and partially due to brain hemodynamics. Therefore, it is not clear that one actually wants to make the signal entirely uncorrelated, as this may remove the effects of important neuronal information related to the hemodynamic response function (HRF). Simulation 4 was constructed to illustrate such a situation, and it appears that performing prewhitening did not have detrimental effects on the results (Fig. 4)."
Proposed (Results 7): "Prewhitening is also not free: making a BOLD series entirely uncorrelated may remove neuronal information carried by the haemodynamic response, a concern Honari et al. (2019) raise although their own simulation found no detrimental effect; on HCP fMRI ..." (Recommendations): "... and prewhitening carries its own costs (Cliff et al., 2021; see also Honari et al., 2019)."

### A10. Introduction ¶2 — Barrett (2015): only one example, and what vanishes is the net synergy, not the MMI synergy. SWQ.

Sentence: "Barrett (2015) exhibited positive net synergy — hence positive MMI synergy, since MMI redundancy is non-negative — in dynamical Gaussian examples in which a target's own immediate past is one of the sources (his Example 1), vanishing when the infinite pasts are the sources."

Problem: (i) only Example 1 has positive net synergy with the target's own immediate past as a source (Example 2 has zero net synergy for the immediate pasts; Example 3's sources are Y and Z). (ii) After the dashed clause about MMI synergy, "vanishing" reads as if the MMI synergy vanished; Barrett shows the *net* synergy vanishes for the infinite pasts while the MMI synergy stays at ½ ln(1 + α²).
Evidence: Barrett p. 7, Fig. 4 legend: "(a) Example 1. In this system X receives input from its own past and from the past of Y. There is positive net synergy between the information that the immediate pasts of X and Y provide about the future of X, but zero net synergy between the information provided by the infinite pasts of X and Y about the future of X. (b) Example 2 ... There is zero net synergy between the information provided by the immediate pasts ..."; p. 8: Eq. (73) ΔI(Xt; Xt−1, Yt−1) = ½ ln(1 + α⁴) > 0; Eq. (79) ΔI(Xt; Xt⁻, Yt⁻) = 0; Eq. (81) S_MMI(Xt; Xt−1, Yt−1) = ½ ln(1 + α²); Eq. (82) R_MMI(Xt; Xt⁻, Yt⁻) = S_MMI(Xt; Xt⁻, Yt⁻) = ½ ln(1 + α²).
Proposed: "Barrett (2015) exhibited positive net synergy — hence positive MMI synergy, since MMI redundancy is non-negative — in a dynamical Gaussian example in which a target's own immediate past is one of the sources (his Example 1); the net synergy vanishes when the infinite pasts are the sources, while the MMI synergy stays at ½ ln(1 + α²) (his Eqs. 73 and 79–82)."

### A11. Introduction ¶2 — Barrett (2015) is placed among the "static" closed forms, but it also gives closed-form MMI decompositions of lagged MVAR systems. SWQ (novelty claim).

Sentence: "Closed-form Gaussian decompositions exist for transfer entropy (Faes et al., 2017) and for static systems (Barrett, 2015; Kay & Ince, 2018), and Varley (2024) gave the aggregate identity; what none of them gives is an account at the level of the atoms actually reported — ..."

Problem: Barrett's Sec. V gives closed-form MMI redundancy and synergy for MVAR(1) processes with a target's own past among the sources — the nearest prior closed form to Results 1. The "what none of them gives" clause is still true (none is at the level of the sixteen ΦID atoms), but the list of prior closed forms understates Barrett.
Evidence: Barrett title ("static and dynamical Gaussian systems"); p. 2: "In Sec. V we proceed to explore partial information in several example dynamical Gaussian systems, examining (i) the behavior of net synergy ... and (ii) redundancy and synergy according to the MMI PID"; p. 8, Eqs. (80)–(82) (closed-form R_MMI and S_MMI for Example 1 at one lag and infinite lags) and Eqs. (93)–(95) (Example 2).
Proposed: "Closed-form Gaussian decompositions exist for transfer entropy (Faes et al., 2017), for static systems (Barrett, 2015; Kay & Ince, 2018) and for single-target lagged PIDs of MVAR processes with a target's own past among the sources (Barrett, 2015, Sec. V), and Varley (2024) gave the aggregate identity; what none of them gives ...".

### A12. Results 1 — "Varley's (2024) aggregate identity". SWQ.

Sentence: "... and str + stx + sty + sts = S, which is Varley's (2024) aggregate identity."

Problem: Varley's identity (his Eq. 12) is for a *disintegrated* pair (independent processes, i.e. the family's q = 0 and no cross-lag); on the symmetric family the aggregate equals S for every q, which follows from Varley's general expression (his Eq. 3) with the family's mutual informations — an extension made by this paper, not by Varley. (The Introduction's description of Varley is exact.)
Evidence: Varley p. 5, Eq. (3): "ISyn(X) = (Xt ; Xt+1) − max_i I(Xti ; Xt+1)" [the "I" is missing in the source]; p. 7: "If we define X⊥ as the twin of system X, but with X¹ ⊥ X². In X⊥, each X^i has the same first-order autocorrelations as in the original X ... ISyn(X⊥) = H(X²t+1) − H(X²t+1|X²t) = I(X²t; X²t+1) (11)(12)".
Proposed: "... and str + stx + sty + sts = S for every q: Varley's (2024) aggregate synergy (his Eq. 3), which at q = 0 is his identity for a disintegrated pair (his Eq. 12)."

### A13. Results 1 — the negativity attributions. SWQ (3 pairs: Mediano et al. 2025 SI; Luppi et al. 2026; Down et al. 2026).

Sentence: "The four mirror atoms are negative, a property of MMI-ΦID that its authors note (Mediano et al., 2025, SI Appendix, Sec. III.A; Luppi et al., 2026; under MMI only the redundancy and synergy atoms are guaranteed non-negative, Down et al., 2026)."

Problem: (i) the ΦID authors note that MMI-ΦID *can* produce negative atoms; they do not say which atoms, so "a property ... that its authors note" should not read as if they identified the mirror atoms. (ii) Down et al. do not say "only": they say the redundancy and synergy atoms are guaranteed positive and "many of the other atoms can occasionally take negative values".
Evidence: Mediano 2025 SI p. 3 (Sec. III.A): "the MMI double-redundancy is monotonic (but not totally monotonic) on the double-redundancy lattice, and thus can lead to negative ΦID atoms." Luppi 2026 p. 19 [795]: "the MMI double redundancy is monotonic (but not totally monotonic) on the double-redundancy lattice and can thus lead to negative-signed atoms." Down p. 7: "While ΦID-MMI guarantees the positivity of the redundancy and synergy atoms, many of the other atoms can occasionally take negative values."
Proposed: "The four mirror atoms are negative. That MMI-ΦID can produce negative atoms is noted by its authors (Mediano et al., 2025, SI Appendix, Sec. III.A; Luppi et al., 2026); under MMI the redundancy and synergy atoms are guaranteed non-negative while many of the others can take negative values (Down et al., 2026)."

### A14. Discussion ¶1 — Mediano et al. (2025) locator. SWQ.

Sentence: "... balanced by four negative atoms of the kind the ΦID authors note MMI can produce (Mediano et al., 2025; Luppi et al., 2026), ..."

Problem: the statement is in the SI Appendix only; the main article discusses only the negativity of ΦWMS (p. 6, "Why Whole-Minus-Sum Φ Can Be Negative"). Results 1 gives the locator; this sentence does not. The Luppi et al. (2026) pair is SUPPORTED (p. 19).
Proposed: "(Mediano et al., 2025, SI Appendix, Sec. III.A; Luppi et al., 2026)".

### A15. Introduction ¶2 and Results 7 — Liardi et al. (2025). SWQ (2 pairs).

Introduction: "The ΦID authors have moved towards null-model normalisation of atoms (Liardi et al., 2025) ..." Results 7: "Null-model normalisation of atoms (Liardi et al., 2025, for PID on MEG, named there as a future extension to ΦID) is the ΦID authors' stated direction; ..."

Problem: the normalisation is for PID atoms (MEG under ketamine, LSD and psilocybin); ΦID appears once, among possible further generalisations ("may entail"). "Moved towards ... atoms" in the Introduction reads as ΦID atoms; "stated direction" in Results 7 is stronger than "may entail".
Evidence: Liardi p. 3: "directly comparing PID atoms belonging to different distributions may yield results purely dictated by the difference in mutual information. To overcome this issue, a normalisation procedure is needed"; p. 9: "we analyse resting-state magnetoencephalography (MEG) recordings of subjects under the effects of different psychedelic drugs—ketamine (KET) (N=19), LSD (N=15), and psilocybin (PSIL) (N=14)"; p. 14: "Further generalisations of the proposed technique may entail the development of other statistical models ... and more refined TMI-based information frameworks, like Integrated Information Decomposition (ΦID) [72]."
Proposed (Introduction): "The ΦID authors have proposed null-model normalisation of PID atoms, naming ΦID as a possible further generalisation (Liardi et al., 2025), and, in some studies, ...". (Results 7): "... is a direction the ΦID authors have named; ...".

### A16. Discussion and Methods — "Luppi et al. (2022) falls outside the TR range". SWQ (2 pairs).

Discussion: "Luppi et al. (2022) falls outside the TR range the plan fixed for the table, a scoping rule." Methods, Literature search: "a scoping rule that places Luppi et al. (2022) outside the set at its TR of 0.72 s (Discussion)."

Problem: true of its human (HCP) data only. The same paper analyses a macaque dataset at TR 2.6 s, band 0.0025–0.05 Hz, not deconvolved, which is inside the 1–3 s range (and reports a macaque synergy gradient and the human–macaque comparison).
Evidence: Luppi 2022 p. 13: human "TR of 720 ms"; macaque "Resting-state scanning was performed for 21.6 min, with a TR of 2,600 ms"; p. 14: macaque data "bandpass filtered in the range of 0.0025–0.05 Hz"; p. 13: "no HRF deconvolution was performed for macaque data".
Proposed (Discussion): "The human (HCP) data of Luppi et al. (2022), at TR 0.72 s, fall outside the TR range the plan fixed for the table, a scoping rule (its macaque dataset, at TR 2.6 s and not deconvolved, falls inside)." (Methods): "... a scoping rule that places the human data of Luppi et al. (2022), at TR 0.72 s, outside the set (Discussion)."

### A17. Discussion — "By the map it would be the most exposed dataset in the table". SWQ (minor).

Problem: by the same ideal-band-pass computation, the macaque stimulation data of Luppi et al. (2026) (TR 1.25 s, 0.0025–0.05 Hz) sit at 0.973 against 0.970 for the HCP data (derivative ratio 146 against 131); that study reports ΦR, whose exposure to r₁ is small, which is presumably why Luppi et al. (2022) is singled out.
Evidence: Luppi 2026 Reporting Summary (OCR): "TR = 1250 ms ... 500 brain volumes per run"; macaque filtering "low-pass (0.05-Hz cutoff) and high-pass (0.0025-Hz cutoff) filters and a zero-phase fast-Fourier notch filter (0.03 Hz)". S3 Text itself lists "1.25 s → 0.97".
Proposed: "By the map it would be the most exposed sts-reporting dataset in the table (the macaque stimulation data of Luppi et al., 2026, sit at the same ideal-band-pass r₁, but that study reports ΦR): ...".

### A18. Discussion — the applicability-table sentence: "gives every study ... the same conditional statement" and "all nine read in full". SWQ (Luppi et al. 2023 pair; the other eight listing pairs SUPPORTED).

Sentence: "The applicability table (S3 Text), which lists nine empirical studies (...), gives every study — all nine read in full; Tarchi et al. (2026) does not state its redundancy function — the same conditional statement, the sign of r₁ change that would produce its reported effect on the map; ..."

Problem: (i) for Luppi et al. (2023) the table gives no sign: its primary quantity (CCS emergence capacity on binarised signals) is outside the map, and the row says so. (ii) "Read in full" holds for the main articles; the supplementary materials of six of the nine were not read (A5), so the negative statements in this sentence ("does not state its redundancy function", "none of them reports regional r₁") are statements about the main texts.
Evidence: `notes/partB5_literature_v2.md` row 2: "Primary quantity is discrete CCS on binarised data: outside the map ... the map was not evaluated for the emergence atoms"; Luppi 2023 p. 12 (as in A2). Supplementary references: Tarchi p. 5 ("Supplementary Materials Table S2"), Luppi 2026 p. 13 ("Supplementary Fig. 16 and Tables 6–10"), Down p. 7 ("in the appendix in section 6.7"), Nago p. 8 ("Additional File, Table S1 and Fig. S2"), Luppi 2023 ("Fig. S3", "Table S1").
Proposed: "... gives every study within the map — the main texts of all nine read in full; the main text of Tarchi et al. (2026) does not state its redundancy function — the same conditional statement, the sign of r₁ change that would produce its reported effect on the map (the primary quantity of Luppi et al., 2023, CCS emergence capacity on binarised signals, is outside it); ...".

### A19. Results 3 (and S3 Text §4) — "none of which reports regional r₁" is stated for "any published map". SWQ (universal claim, S3 pair; the main-text sentence has no author–year citation and is counted in Section C).

Results 3: "Which gradient is the cause cannot be told on these data, and nothing here bears on any published map, none of which reports regional r₁ (Discussion)." S3 §4: "it says nothing about any published synergy map, none of which reports regional r₁".
Problem: the check covers the maps of the nine table studies (Section C, C4); "any published map" is wider than what was read.
Proposed: "... and nothing here bears on any published map; none of the maps of the studies in the applicability table reports regional r₁ (Discussion)."

### A20. Introduction ¶1 — Luppi et al. (2022): "a redundancy-dominated sensory core". SWQ (terminology).

Sentence: "On resting-state BOLD it separates a redundancy-dominated sensory core from synergy-dominated association cortex (Luppi et al., 2022)."
Problem: in that paper the "core" is the synergistic one (title: "A synergistic core for human brain evolution and cognition"; p. 11: "the brain's synergistic core"); calling the sensory side a "core" inverts the source's term. The attribution of the gradient itself, and of the atoms (the persistent synergy and redundancy, I∂{12}→{12} and I∂{1}{2}→{1}{2}, p. 14), is correct.
Evidence: p. 2 [772]: "redundant interactions are especially prominent in the brain's somatomotor and salience subnetworks, and most visual regions ... In contrast, regions with higher relative importance for synergy predominate in higher-order association cortices".
Proposed: "On resting-state BOLD it separates redundancy-dominated sensory and motor cortex from a synergy-dominated association cortex, the 'synergistic core' (Luppi et al., 2022)."

### A21. Introduction ¶1 — Luppi et al. (2024): "Regions ranked by synergy". SWQ (minor).

Sentence: "Regions ranked by synergy form a "synergistic workspace" whose integrated information is reduced under propofol and in disorders of consciousness (Luppi et al., 2024)."
Problem: the workspace is identified by the redundancy-to-synergy rank gradient (synergy rank minus redundancy rank), not by synergy alone; the reduced quantity is ΦR. The quotation "synergistic workspace" is verbatim (p. 1).
Evidence: p. 6: "we identify the synergistic workspace as regions where synergy predominates"; p. 21: "we ranked all 454 regions based on their nodal strength ... separately for networks of synergy and redundancy. Subtracting each region's redundancy rank from its synergy rank yielded a gradient"; p. 1 (abstract): "loss of consciousness due to general anaesthesia or disorders of consciousness corresponds to diminished ability of the synergistic workspace to integrate information"; p. 8: "almost all regions showing consistent decreases in ΦR when consciousness was lost were members of the global synergistic workspace".
Proposed: "Regions where synergy predominates over redundancy, by rank, form a "synergistic workspace" whose integrated information (ΦR) is reduced under propofol and in disorders of consciousness (Luppi et al., 2024)."

### A22. Introduction ¶2 — Mediano et al. (2021) worked example: clash of the symbol c. SWQ (clarity).

Sentence: "... their own worked example is a coupled AR pair (Mediano et al., 2021, Fig. 5 and Appendix VI), the symmetric coupled family of Methods at coefficient 0.4, whose c = 0 case is the diagonal family used here."
Problem: the identification is correct (self- and cross-coefficient 0.4 = Methods' family at a = c = 0.4), but in Mediano et al. c is the innovation (noise) correlation, the variable on the x-axis of their Fig. 5, while here c is the cross-coefficient; a reader checking Fig. 5 will read "c = 0" as zero noise correlation, which is not the diagonal family.
Evidence: Mediano 2021 p. 10: "A being a 2 × 2 matrix with all entries set to 0.4, and Σ a noise (or innovations) covariance matrix with 1's along the diagonal and a given noise correlation (c in the notation of Ref. [19])"; p. 26 (Appendix VI): "x1t+1 = a(x1t + x2t) + ε1t+1, x2t+1 = a(x1t + x2t) + ε2t+1, where a = 0.4 is a fixed coupling parameter and ε1t, ε2t are zero-mean unit-variance white noise processes with correlation c."
Proposed: "... the symmetric coupled family of Methods with self- and cross-coefficient 0.4 (their c is the innovation correlation, which they vary); the family with zero cross-coefficient is the diagonal family used here."

### A23. Methods, Dataset — "six of twenty excluded by the source authors" is ambiguous. SWQ (Timmermann et al. 2023 pair).

Sentence: "Data are the preprocessed Schaefer-116 regional time series released by Singleton et al. (2025), acquired by Timmermann et al. (2023): fourteen subjects (six of twenty excluded by the source authors for head movement), ..."
Problem: the six are Singleton et al.'s exclusion; Timmermann et al., named immediately before, excluded four.
Evidence: Singleton p. 8: "Six out of 20 participants were discarded from group analyses due to excessive head movement during the 28 min DMT scans ... leaving 14 for analysis." Timmermann p. 9: "Four out of 20 participants were discarded from group analyses due to excessive head movement during the 8-min post DMT timeperiod". The acquisition facts are all supported (Timmermann p. 9: TR = 2000 ms; 3T; 20 mg DMT fumarate "injected over 30 s"; 28-min scans with injection "at the end of 8th min").
Proposed: "... fourteen subjects (six of twenty excluded for head movement by Singleton et al., 2025), ...".

### A24. Methods, Literature search — the stated inclusion criterion does not describe the nine studies. SWQ (counted in Section C, C16).

Sentence: "Published fMRI ΦID studies reporting Gaussian-MMI synergy on BOLD at TR ≈ 1–3 s were identified by web search on 14 September 2026 ..."
Problem: the table's nine include Luppi et al. (2023) (CCS on binarised signals), Luppi et al. (2024, 2026) (ΦR), Tarchi et al. (2026) (redundancy function not stated) and Luppi et al. (2022) (human TR 0.72 s).
Proposed: "Published empirical fMRI ΦID studies reporting synergy, redundancy or quantities built on them were identified ...; the map's scope is Gaussian-MMI at TR ≈ 1–3 s, and the table marks the studies outside it."

### A25. CANNOT CHECK (full text not obtained; see Section B).

- Methods, Scope map (and S3 §4): "The spin test of the regional correlations (Alexander-Bloch et al., 2018, ...)". The PubMed abstract (PMID 29860082) is consistent: "using a spatial permutation framework to generate null models of overlap by applying random rotations to spherical representations of the cortical surface".
- Methods, DMT contrast: "A phase-randomised surrogate ... (1,000 surrogates; Theiler et al., 1992)". Secondary, in-folder support: Prichard & Theiler (1994) p. 1: "A second approach is to Fourier transform (FT) the data set, randomize the phases, and then invert the transform [7,8]", with [8] = "J. Theiler, S. Eubank, A. Longtin, B. Galdrikian, and J. D. Farmer, Physica D 58, 77–94 (1992)".

### A26. Uncited literature statements (outside the author–year scope; not counted)

- Author summary: "Synergy has been reported to differ across the cortex and to fall under anaesthesia and in disorders of consciousness". In the studies the paper cites, what falls under anaesthesia and in DoC is integrated information ΦR (Luppi et al., 2024, p. 8; Luppi et al., 2026, p. 5) and a CCS-based emergence capacity in DoC (Luppi et al., 2023); none reports the sts atom falling. Suggest: "Synergy has been reported to differ across the cortex, and integrated information built from it to fall under anaesthesia and in disorders of consciousness".
- Introduction ¶3 ("against the workspace account's prediction that synergy indexes conscious level"), and S1 Text (same words, cited to Luppi et al., 2024): the workspace account's measure is ΦR within the synergistic workspace (Luppi 2024 p. 1, p. 8), not synergy as such. S1 Text is outside this pass; flagged for the authors.

---

## B. The seven references with no full text in the folder

| reference | obtained? | source used (22 Sep 2026) | what the manuscript attributes | verdict |
|---|---|---|---|---|
| Cousineau (2005), TQMP 1(1), 42–45 | Yes, full text | tqmp.org open-access PDF, `RegularArticles/vol01-1/p042/p042.pdf` | within-subject SEM bands (Figures, Fig 4) | SUPPORTED: the normalisation "Y = Xij − X̄i + X̄ ... all the individual differences will be erased". Bibliographic details match. |
| Morey (2008), TQMP 4(2), 61–64 | Yes, full text | tqmp.org open-access PDF, `RegularArticles/vol04-2/p061/p061.pdf` | correction to Cousineau's within-subject intervals | SUPPORTED: "multiply the sample variances in each condition by M/(M − 1)", M = "the number of within-subjects conditions" (the caption's √(28/27) is this with M = 28). Bibliographic details match. |
| Wu et al. (2021), NeuroImage 244, 118591 | Yes, full text | ScienceDirect open-access article page (pii S1053811921008648; CC BY-NC-ND) | rsHRF toolbox used for deconvolution (Methods, Remedies; S2 Text) | SUPPORTED: "Here we introduce rsHRF, a Matlab and Python toolbox that implements HRF estimation and deconvolution from the resting-state BOLD signal"; builds on the authors' earlier point-process method (Wu et al., 2013). The version "1.7.0" is not in the paper (it names Matlab version 2.4); it is the software's own version number. Seven authors as in the reference list. |
| Tian et al. (2020), Nat Neurosci 23, 1421–1432 | Yes, as preprint (not the version of record) | bioRxiv 10.1101/2020.01.13.903542 v2 full-text PDF | "the 16 subcortical parcels of Tian et al. (2020)" (Dataset) | SUPPORTED against the preprint: "Scale I is the coarsest atlas and comprises 8 bilateral regions" (16 in all); atlas openly available. The Nature Neuroscience version was not read. |
| Váša et al. (2018), Cereb Cortex 28(1), 281–294 | Partly: main-text Methods and Results (the fetch did not return the end of the Discussion or a licence line) | Oxford Academic article page, `academic.oup.com/cercor/article/28/1/281/4566555` | "with the rotations of Váša et al., 2018, released with the data; 10,000 rotations" (Methods; S3 §4) | SUPPORTED: "Such tests were previously implemented at the vertex level; here we implemented an analogous permutation test at the regional level"; P_perm from "a null distribution of 10 000 Spearman correlations, between one empirical map and the randomly rotated projections of the other map". The released `fxns/SpinTests/perm_sphere_p_al857.m` in the DMT_NCT release (77af7aa) is signed "František Váša ... June 2017 - June 2018" and uses permutations from "rotate_parcellation"; `rotated_Schaefer_100.mat` is in the release. Author list matches. |
| Alexander-Bloch et al. (2018), NeuroImage 178, 540–551 | No | PubMed Central (PMC6095687) returned a reCAPTCHA page — blocked, not pursued further; ScienceDirect shows abstract, introduction and section snippets only; no preprint found. PubMed record 29860082 read. | the spin test (Methods; S3 §4) | CANNOT CHECK. The abstract is consistent ("random rotations to spherical representations of the cortical surface"). Bibliographic details match PubMed. |
| Theiler et al. (1992), Physica D 58, 77–94 | No | ScienceDirect returned HTTP 429 (refused); the OSTI record of the conference version (LA-UR-91-3343) is blocked by robots.txt — not pursued further; the INET Oxford page links only to ScienceDirect; no arXiv version exists. | phase-randomised Fourier surrogate (Methods, DMT contrast) | CANNOT CHECK. Secondary support in the folder: Prichard & Theiler (1994) p. 1, ref. [8]. The author order used (Theiler, Eubank, Longtin, Galdrikian, Farmer) matches Prichard & Theiler's citation of it (the INET Oxford page lists a different order). |

For the head note: obtained in full — Cousineau (2005), Morey (2008), Wu et al. (2021); obtained as preprint — Tian et al. (2020); obtained in part — Váša et al. (2018); not obtained — Alexander-Bloch et al. (2018), Theiler et al. (1992). None of the seven had been read in full on 20 September, the date the head note gives.

Also checked on the web: the software entry's claim "The repository asks users to cite Mediano et al. (2025) and Luppi et al. (2022)" — SUPPORTED by the GitHub README of Imperial-MIND-lab/integrated-info-decomp ("If you use `phyid` in your research, please cite the following papers: Mediano, Rosas, et al. (2025) ... Luppi, et al. (2022) ..."; licence BSD-3-Clause). The Down et al. (2026) PubMed/PMC identifiers could not be checked (the PubMed page returned no content).

---

## C. Universal and negative claims about the literature

Search terms run on each of the nine full texts (`papers/txt/*.txt`, PDF pages; reading-order extracts for context): autocorr*, lag / τ / time step, TR / repetition time, minimum mutual information / MMI, CCS / common change in surprisal, surrogate, null, prewhiten*, deconvol*, plus ALFF, spectr*, AC1 / lag-1, intrinsic timescale. Pages with hits:

| study | autocorrelation | lag stated | redundancy function (estimator) | surrogate / null | prewhitening | HRF deconvolution |
|---|---|---|---|---|---|---|
| Luppi 2022 | spatial only (pp. 7–9, 17, 31–32, 38) except p. 18: phase-randomised surrogates "with the same autocorrelation, but no correlation with each other" | symbol τ only (pp. 2, 14) | MMI, Gaussian JIDT solver (p. 14; code "Gaussian MMI solver", p. 18) | p. 18 + Table 1 p. 10 (temporal); spin tests (spatial) | none | yes, Wu et al. 2013 (ref. 60), p. 13; replicated without (Ext. Data Fig. 2c, p. 3); "negligible effects" p. 16 |
| Luppi 2023 | none | "a time-step of 1 TR (2 s) ... slower timescale of 4 TRs" (p. 3) | CCS, plug-in on mean-binarised signals; Gaussian and MMI validations (p. 12) | none | none | yes, Wu et al. 2013 toolbox (p. 12) |
| Luppi 2024 | spatial only (p. 22) | symbol τ only (pp. 19–20) | MMI-ΦID, Gaussian JIDT (pp. 19–20, 23) | spatial nulls only (p. 22) | none | yes, rsHRF / Wu et al. 2013 (pp. 15, 18, 23) |
| Luppi 2026 | spatial only (pp. 8–13, 28) | symbol τ only (pp. 18–20) | MMI double redundancy, Gaussian JIDT (p. 19) | spatial surrogates; p. 13 debiasing surrogate that preserves lag-0 synchrony "while destroying the past–future relationships" | none | not mentioned (p. 16 hit is cell-type deconvolution) |
| Gatica 2024 | none | symbol τ only (p. 14) | MMI "on Gaussian systems" (p. 13); "Gaussian MMI solver" (p. 15) | none | none | none (p. 13 hit is spherical deconvolution in tractography) |
| Down 2026 | none | "one time step (TR) ... the TR is 3 seconds" (p. 5) | MMI; "brain activity is suitably Gaussian" (pp. 5–6); CCS re-validation in the supplement (p. 6) | label/network permutation tests only (pp. 9, 14); p. 7: the null distribution of the atoms "is difficult to determine" | none | none |
| Nago 2026 | spatial only (pp. 5, 12) | symbol τ only (p. 4) | MMI, Imperial-MIND-lab toolbox (p. 4); Gaussian not stated | spin and label permutations only | none | none |
| Tarchi 2026 | none | not stated | not stated (p. 3: "specific software previously released") | none | none | yes, "Standard SPM methods" (p. 3) |
| Zhang 2025 | none | symbol τ only (pp. 4–5) | MMI double redundancy (p. 5); linear-Gaussian, JIDT (pp. 4–6) | none | none | none |

No study reports a regional (temporal) lag-1 autocorrelation, an intrinsic timescale, ALFF of its own data, or any spectral property of its regional series (Zhang's ALFF mentions, pp. 15–16, are discussion of other studies).

C1. Introduction: "The studies whose settings could be read (S3 Text) use the Gaussian estimator with the MMI redundancy function". NOT SUPPORTED — Luppi 2023 (CCS, binarised, plug-in), Tarchi (not stated), Nago (Gaussian not stated). See A2.

C2. Introduction: "at a single lag — one TR where the lag is stated (Luppi et al., 2023; Down et al., 2026)". SUPPORTED WITH QUALIFICATION — only these two state the value, both one TR; six write τ only; Tarchi states nothing; Luppi 2023 also ran 4 TRs as a check (p. 3), so "single lag" holds for the primary analyses.

C3. Introduction: "what none of them [Faes 2017, Barrett 2015, Kay & Ince 2018, Varley 2024] gives is an account at the level of the atoms actually reported — ... whether CCS shares the property ...". SUPPORTED — none decomposes into the sixteen ΦID atoms; Varley mentions CCS only as used by earlier ΦID work "although this function has been critiqued" (p. 10), without testing it; Faes 2017 decomposes transfer entropy with MMI (p. 1, Eq. 2); Kay & Ince are static (p. 1). Qualification on Barrett's closed forms: A11.

C4. Results 3 and S3 §4: "none of which [published maps] reports regional r₁". SUPPORTED for the nine main texts (table above); "any published map" goes beyond what was read — SWQ, A19.

C5. Discussion: "all nine read in full". SUPPORTED for the main articles (all nine PDFs complete in `papers/`, the Luppi 2026 Reporting Summary via OCR); the supplementary materials of Luppi 2022, 2023, 2026, Down, Nago and Tarchi were not read — SWQ, A18.

C6. Discussion: "Tarchi et al. (2026) does not state its redundancy function". SUPPORTED for the main text (no MMI, CCS, "minimum", "Gaussian", "Ince" or "Barrett" in the 10-page PDF; p. 3); its Supplementary Material was not read.

C7. Discussion: "gives every study ... the same conditional statement, the sign of r₁ change that would produce its reported effect on the map". SWQ — the Luppi 2023 row gives none (outside the map). A18.

C8. Discussion: "since none of them reports regional r₁". SUPPORTED (main texts).

C9. Discussion: Luppi 2022 "its measured regional r₁ is not reported". SUPPORTED — the only temporal-autocorrelation mention is the surrogate description (p. 18).

C10. Discussion: "That study also contains the one test of the exposure in the table ... the only such evidence in the table". SUPPORTED — no other study uses an autocorrelation-preserving, cross-correlation-removing null. Note: Luppi 2026's debiasing surrogate (p. 13) removes past–future dependence while keeping lag-0 synchrony; it estimates bias and does not test the exposure.

C11. Discussion: "It leaves open what this paper measures on its own data (Results 3), which that study does not report." SUPPORTED.

C12. Discussion: "it is the one place the table argues against the mechanism". NOT SUPPORTED — Tarchi pp. 5–6 and the table's row 9. A6.

C13. Discussion: "Among the studies in the table, none but Luppi et al. (2022) addressed autocorrelation". SUPPORTED (main texts), with two notes: Luppi 2026's debiasing surrogate (p. 13) removes temporal dependence for bias correction; Luppi 2023 discusses the timescale dependence of its result (pp. 3, 8: "our results about emergence capacity depend on the timescale"). Every other "autocorrelation" hit is spatial.

C14. Discussion / Methods: Luppi 2022 outside the TR range "at its TR of 0.72 s". SWQ — the macaque dataset (TR 2.6 s) is inside. A16.

C15. Discussion: "the most exposed dataset in the table". SWQ — Luppi 2026 macaque stimulation data at 0.973. A17.

C16. Methods: the literature-search inclusion ("studies reporting Gaussian-MMI synergy on BOLD at TR ≈ 1–3 s") against the nine listed. SWQ — Luppi 2023 (CCS), Luppi 2024/2026 (ΦR), Tarchi (unstated), Luppi 2022 (human TR 0.72 s) do not meet it as worded. A24.

C17. Methods, Ethics: Timmermann et al. (2023) "names the committee but gives no reference number". SUPPORTED — p. 9 names "the National Research Ethics Committee London—Brent and the Health Research Authority"; no REC reference number appears in the PDF (the only registry identifier, NCT04673383 on p. 11, is in reference 6 and belongs to a different trial, SPL026 in healthy subjects and MDD patients).

C18. References head note and S5 §5: "Every entry except the software ... was read in full". NOT SUPPORTED. A5, Section B.

C19. S3 §4: ideal band-pass r₁ "of the published studies whose settings are stated is 0.78–0.93". NOT SUPPORTED — 0.73–0.97. A8.

C20. Limitations: "On Gaussian systems every PID whose redundancy depends only on the source–target marginals reduces to MMI when the target is univariate (Barrett, 2015; Kay & Ince, 2018)". SUPPORTED — Barrett p. 5: "Let X, Y, and Z be jointly multivariate Gaussian, with X univariate and Y and Z of arbitrary dimensions n and p. Then there is a unique PID of I(X; Y,Z) such that the redundant and unique information ... depend only on the marginal distributions of (X,Y) and (X,Z). The redundancy according to this PID is given by R_MMI(X; Y,Z) =: min{I(X; Y), I(X; Z)}"; Kay & Ince pp. 2–3.

C21. Results 1: "a property of MMI-ΦID that its authors note" and Down's "only". SWQ. A13.

Tally of the 21 universal/negative claims: SUPPORTED 9 (C3, C6, C8, C9, C10, C11, C13, C17, C20), SWQ 8 (C2, C4, C5, C7, C14, C15, C16, C21), NOT SUPPORTED 4 (C1, C12, C18, C19). The negative claims about the nine studies (C4, C6, C8–C11, C13) hold for their main texts; the supplementary materials of six of them were not read.

---

## D. SUPPORTED pairs, with page and short quote

Main text (68)

| # | location | cited work | page | short quote / evidence |
|---|---|---|---|---|
| 1 | Intro ¶1, ΦID definition | Mediano 2021 | 3 | "not four, but rather 16 distinct information atoms"; TDMI = I(Xt; Xt+1) |
| 2 | same | Mediano 2025 | 2 | "but rather 16 distinct information atoms"; Eq. [1] TDMI |
| 3 | same | Williams & Beer 2010 | 1 | "we use this redundancy lattice to propose a definition of partial information atoms" |
| 4 | Intro ¶1, group differences | Down 2026 | 1 | "a striking synergy reduction across the entire brain, in concert with widespread redundancy increases" |
| 5 | same | Nago 2026 | 1 | "SZ and ASD exhibited a widespread reduction in synergy, whereas ADHD showed a contrasting increase ... ASD ... reduction in redundancy" |
| 6 | same | Zhang 2025 | 1–2 | stage-specific regional synergy decline (synergy only; the sentence's "and redundancy" holds for the set) |
| 7 | Intro ¶1, MMI function | Barrett 2015 | 5 | R_MMI(X; Y,Z) =: min{I(X; Y), I(X; Z)} |
| 8 | same | Mediano 2021 | 24 | "Definition 2. Double-redundancy based on minimum mutual information ... := min I(Xi; Yj)" |
| 9 | Intro ¶1, one TR | Down 2026 | 5 | "their state after one time step (TR) ... the TR is 3 seconds" |
| 10 | Intro ¶2 | Varley 2024 | 1, 7, 8, 10 | "cannot disambiguate between truly integrated systems and disintegrated systems with first-order autocorrelation"; Eq. 12 ISyn(X⊥) = I(X²t; X²t+1); "one subject from the Human Connectome Project ... 1,000 unique pairs"; "(r = 0.97, p ≈ 0)" with pairwise MI |
| 11 | Intro ¶2, CCS | Luppi 2023 | 12 | "Here, we follow the 'common change in surprisal' (CCS) method" |
| 12 | Intro ¶2, closed forms | Faes 2017 | 1 | "exact expressions of the information transfer, as well as redundant and synergistic transfer, for coupled Gaussian processes" |
| 13 | same | Kay & Ince 2018 | 1 | "Closed form solutions for the Idep PID are derived for both univariate and multivariate Gaussian systems" |
| 14 | same | Varley 2024 | 7 | aggregate identity Eq. 12 (the atom-level account is not given; CCS only mentioned, p. 10) |
| 15 | Results 3 | Raut 2020 | 2 [20891] | "intrinsic timescales are organized along spatial gradients extending from (unimodal) sensorimotor regions to (transmodal) association cortex" |
| 16 | same | Ito 2020 | 6 | "transmodal regions had significantly slower intrinsic timescales than unimodal regions" |
| 17 | same | Murray 2014 | 1 | single-neuron spike trains; "Sensory cortex showed shorter timescales ... prefrontal cortex showed longer timescales" |
| 18 | same | Luppi 2022 | 2–3 [772–773] | redundancy-to-synergy gradient, sensorimotor to association |
| 19 | Results 7 | Cliff 2021 | 15–16 | χ²-test of MI between unrelated HCP series: "an FPR of 41.8% ... After prewhitening with an AR(p) filter, this increased to over 88%" |
| 20 | Results 7 | Arbabshirani 2014 | 13 | "Applying a bandpass frequency filter (0.01-0.10 Hz), reintroduces autocorrelation" |
| 21 | Discussion ¶1 | Luppi 2026 | 19 [795] | "can thus lead to negative-signed atoms" |
| 22 | Discussion, literature | Huang 2018 | 1, 3, 4, 11 | AC1 = lag-1 autocorrelation (p. 3); "graded global increase of AC1" in sedation (p. 4); "Conversely, all of these parameters decreased in deep anesthesia and in patients with DOC" (p. 1); deep anaesthesia = propofol 4 µg/ml |
| 23–30 | applicability-table list | Down, Gatica, Luppi 2022, 2024, 2026, Nago, Tarchi, Zhang | see C | each an empirical fMRI ΦID study; Tarchi's redundancy function not stated (p. 3) |
| 31 | Luppi 2022 paragraph | Luppi 2022 | 13 | "TR of 720 ms"; "retaining frequencies between 0.008 and 0.09 Hz"; regional r₁ not reported |
| 32 | same | Wu 2013 | Luppi 2022 p. 13; Wu p. 1 | "state-of-the-art techniques60" (ref. 60 = Wu et al. 2013, "A blind deconvolution approach ...") |
| 33 | same | Luppi 2022 | 3, 16 | "analogous results are also obtained when this step is omitted (Extended Data Fig. 2c,d)"; quote verbatim: "had negligible effects on synergy and redundancy calculations" |
| 34 | same | Luppi 2022 | 18, 10 | surrogates "with the same autocorrelation, but no correlation with each other"; Table 1 |
| 35 | same | Luppi 2022 | — | the only such test in the table; correlation with regional r₁ not reported (C10, C11) |
| 36 | same | Down 2026 | 1 | synergy down with redundancy up (the "one place" claim is A6) |
| 37 | same | Luppi 2024 | 20, 8 | Eq. (7) "ΦR = Φ + Red(X, Y)"; ΦR decreases |
| 38 | same | Luppi 2026 | 20, 5 [781] | ΦR (Eq. 9); reduced under anaesthesia |
| 39 | same | Luppi 2022 | 18 | addressed autocorrelation (surrogate) |
| 40 | same | Varley 2024 | 1 | the note's subject |
| 41 | Recommendations | Bartlett 1935 | 2 [537] | AR(1) variance (1/n)(1 + ρ1ρ2)/(1 − ρ1ρ2) (see the note under A3) |
| 42 | same | Afyouni 2019 | 1–4 | EDF of Pearson correlation under autocorrelation |
| 43 | same | Cliff 2021 | 1, 16 | "this issue cannot be mediated by fitting a time-series model alone (e.g., in Granger causality or prewhitening approaches)"; FPR 41.8% → over 88% |
| 44 | same | Luppi 2022 | 18 | autocorrelation-preserving, correlation-removing null |
| 45 | Limitations | Barrett 2015 | 5 | univariate-target uniqueness of MMI (C20) |
| 46 | same | Kay & Ince 2018 | 2–3 | "for a univariate target, if red, unq0 and unq1 depend only on the predictor-target marginal ... unique non-negative PID ... MMI" |
| 47 | same | Mediano 2021 | 3, 24 | multi-target extension; double-redundancy Definitions 1–2 |
| 48 | same | Faes 2017 | 1, 3 | decomposition of the joint transfer entropy, a different object |
| 49 | Ethics | Timmermann 2023 | 9 | "This study was approved by the National Research Ethics Committee London—Brent and the Health Research Authority ..."; Home Office licence; written informed consent |
| 50 | Ethics | Singleton 2025 | 11 | data availability: GitHub singlesp/DMT_NCT and Zenodo (FD is in the release, `data/FDlong.mat` at 77af7aa, though not listed in the paper's statement) |
| 51 | Dataset | Singleton 2025 | 8 | "Six out of 20 participants were discarded ... leaving 14"; "100 cortical and 16 subcortical regions" |
| 52 | Dataset | Timmermann 2023 | 9 | "separated by two weeks"; "in a counter-balanced order (half of the participants received placebo and the other half received DMT)"; initial session "task free" |
| 53 | Dataset | Schaefer 2018 | 1, 6 | "Multiresolution parcellations ... are publicly available"; networks "using a similar procedure to Yeo et al. (2011)" |
| 54 | Dataset | Yeo 2011 | 4 | "7 networks as well as a finer solution that identified 17 networks" |
| 55 | Dataset | Tian 2020 (preprint) | bioRxiv v2 | "Scale I ... comprises 8 bilateral regions" |
| 56 | Estimator | Afyouni 2019 | 4 [612] | Eq. (8): N̂ = N(Σ ρ²GG,k)⁻¹ |
| 57 | Redundancy functions | Barrett 2015 | 5 | MMI single-target redundancy |
| 58 | same | Mediano 2021 | 24 | Definition 2 (MMI double redundancy) |
| 59 | same | Ince 2017 | 12 | Definition 1: ΔS_com = c if "sgn Δs h(a1) = ... = sgn Δs h(a1,...,an) = sgn c", else 0 |
| 60 | same | Mediano 2021 | 24 | Definition 1: "subset of samples for which all marginal pointwise mutual informations, as well as the pointwise full mutual information i(x; y), have the same sign" |
| 61 | same | Mediano 2025 SI | 4 | Definition 2, same sign condition |
| 62 | same | Ince 2017 | 13 | Definition 2 constraints Q(Ai, S) = P(Ai, S) and Q(A1,...,An) = P(A1,...,An) (for Gaussians these fix the covariance, so P̂ = P) |
| 63 | Closed form | Mediano 2021 | 16, 24 | "atoms ... via the Moebius inversion formula"; "the solution to a linear system of equations" |
| 64 | Scope map | Váša 2018 | publisher page | regional-level spherical permutation, 10,000 rotations |
| 65 | Remedies | Wu 2013 | 1 | blind deconvolution of resting-state fMRI |
| 66 | Remedies | Wu 2021 | OA page | rsHRF Matlab and Python toolbox |
| 67 | Figures | Cousineau 2005 | TQMP | subject-mean normalisation |
| 68 | Figures | Morey 2008 | TQMP | M/(M − 1) correction |

S3 Text (17): Barrett p. 5 (MMI); Mediano 2021 p. 24 Def. 2; Ince p. 12 (CCS); Mediano 2021 p. 24 Def. 1; Mediano 2025 SI p. 4 Def. 2; Mediano 2025 SI p. 3 identity "c(x; y) = i∂{1}{2}→{1}{2}(x; y) − i∂{12}→{12}(x; y)"; Mediano 2025 SI p. 4 verbatim quotation "for which all marginal pointwise mutual informations, as well as the pointwise full mutual information I(X; Y), have the same sign"; Mediano 2025 SI p. 4 "the CCS redundancy is calculated with respect to the distribution of the system of interest, p(x, y)" and "the numerical results in Sec. IX below use CCS without the maximum entropy projection"; Ince p. 13 Def. 2; Ince p. 13 Def. 3 ("In a previous version of this manuscript we used ... the maximum entropy distribution subject to the constraints of pairwise target-predictor marginal equality: Definition 3. P̂ind"); Váša (publisher page); Mediano 2025 SI Def. 2 "retaining Definition 1 verbatim on the sign condition" (wording identical, notation i(x; y) → I(X; Y)); the nine studies of Table A; Varley 2024 and Mediano 2025 in Table A; Luppi 2022 0.72 s and 0.008–0.09 Hz (p. 13) → 0.970; every TR and band of the Table B list (verified, values recomputed; see A8); Huang 2018 (as in #22).

S5 Text (2): "F9 (the Luppi et al. 2022 paragraph)" (a label; note that F9's proposed text is the origin of the errors in A1); "the SI Appendix of Mediano et al. (2025) included" (the SI is in the folder, 11 pp.).

Checked beyond the requested scope, all SUPPORTED: Data and code availability (Singleton et al., 2025: GitHub and Zenodo 10.5281/zenodo.15177511, p. 11 and ref. 99; upstream commit 77af7aa matches the local clone); Competing interests (Luppi et al. 2022 and 2024 have authors in the University Division of Anaesthesia, Cambridge, p. 1 of each; C.T. is an author of Timmermann et al. 2023 and Singleton et al. 2025; S.P.S. first author of Singleton et al. 2025); reference-list notes for Mediano et al. 2021 ("v1; Appendix, Definition 1 is the CCS double-redundancy definition", p. 24) and 2025 ("SI Appendix: Definition 1 is MMI, Definition 2 the CCS ...; Sec. III.A states that MMI ΦID atoms can be negative", pp. 3–4), Tarchi et al. 2026 ("a deconvolving study", p. 3); the software entry (README, Section B).

Bibliographic details (item 6). Compared with each PDF's own header or footer: nothing looks wrong. Confirmed: Afyouni 199:609–625; Arbabshirani 102(Pt 2):294–308 (NIH manuscript header "102(0 2)"); Barrett PRE 91, 052802; Bartlett 98(3), pp. 536–543 (the PDF runs 536–543); Cliff PRR 3, 013145; Down bioRxiv doi 10.64898/2026.02.18.706630 (header); Faes 2017 Entropy 19, 408; Gatica Netw Neurosci 8(4), 1032–1050; Honari 197:37–48; Huang 38(9):2304–2317; Ince Entropy 19, 318; Ito 221, 117141; Kay & Ince Entropy 20, 240; Liardi PLOS Comput Biol e1013629 (Nov 2025); Luppi 2022 25:771–782; Luppi 2023 269, 119926; Luppi 2024 RP88173, version of record 18 July 2024; Luppi 2026 10:777–802 (25 authors match); Mediano 2021 arXiv 2109.13186v1; Mediano 2025 PNAS 122(39) e2423297122; Nago 13:25; Raut 117(34), 20890–20897; Schaefer 28:3095–3114; Singleton 8:631; Tarchi 16:e71352 (the PDF gives no issue number, so "(4)" was not checkable); Timmermann PNAS 120(13) e2218949120; Varley arXiv 2407.16601v1; Williams & Beer arXiv 1004.2515v1; Wu 2013 17:365–374; Yeo 106:1125–1165; Zhang Brain Sci 15, 636. Not checkable from the PDF: Murray 17(12):1661–1663 (the PDF is the advance-online version) and Faes 2025's PRL volume and article number (the PDF is the arXiv version).
