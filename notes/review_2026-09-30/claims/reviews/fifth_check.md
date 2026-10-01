*Copy for the repository: quotations of the cited works longer than a few words are replaced by a description in square brackets with their page, as the passages themselves are not in the repository, and e-mail addresses by what they identify; paths of the planning session's scratch space are shortened to SP/.*

**Adversarial check of new_claims_pack.json (6 entries), verified against the local PDFs and the .m file**

I checked every entry against the PDFs. Five verdicts stand. One is wrong: sentence 202 should be Q as written, or S once one phrase is reworded. The other five entries have wording errors or missing facts, listed below.

## Specific checks

- **(a) Six species: yes.** Human, macaque, marmoset and mouse (fMRI), plus larval zebrafish and C. elegans (calcium imaging).
  - Sources: abstract (p. 1), Fig. 1 caption (p. 3), p. 4, and the species list on p. 7.
  - The quoted finding (p. 5) comes from the 485 features whose direction of change is the same in all 15 contrasts. Fig. 3a (p. 7) lists those 15 contrasts, and they include "zebrafish awake vs tricaine" and "c.elegans awake vs iso". So the statement is accurate.
- **(b) "In the caption of an example macaque time series": not accurate.** The quote is in the caption of Fig. 3e (p. 7): [examples of time series from an awake and an anaesthetised macaque]. The panel is titled [example time series and their autocorrelation]. It shows two series plus their autocorrelation plots, not one series.
- **(c) Human dataset: yes.** N = 15 with sevoflurane (p. 4). Sixteen completed the protocol and one was excluded for motion (p. 20). TR = 1.838 s (p. 20). These data were published before (Ranft et al. 2016, ref. 42; p. 19).
- **(d) Váša's p-value:**
  - Both the main text (p. 5, printed 285) and the SI (p. 7) build the null by permuting one map only, [between one empirical map and the other, unrotated, map].
  - Neither document says whether P_perm is one- or two-sided.
  - Neither mentions permuting both maps or averaging two p-values. "averag" appears in both only in unrelated contexts.
  - The paper does point to its own code (p. 12, printed 292: F.V.'s GitHub and a Zenodo DOI).
- **(e) The .m file (LF line endings, so the line numbers are reliable):**
  - Lines 1–2: the function gives a p-value for the spatial correlation of two parcellated cortical maps. It uses spherical permutations from "rotate_parcellation".
  - Lines 3–4: [the permutation is done in both directions] — it permutes both maps and correlates each with the other, unpermuted, map.
  - Line 15: [the author, F. Váša, his address and the dates June 2017 to June 2018].
  - Line 17: [al857's copy also returns the null distribution, otherwise the same].
  - Lines 48–55: the direction depends on the sign of the empirical correlation. Each p is the fraction of null correlations strictly beyond it (strict > or <, no +1).
  - Lines 57–58: "average p-values", `p_perm = (p_perm_xy + p_perm_yx)/2`.
  - The entry's descriptions of these lines match.
- **(f) Tian 2020 NN: yes.**
  - p. 3: [eight bilateral regions, the scale I atlas].
  - p. 4: [scale I has 16 regions], and the Fig. 3a caption says [eight bilateral regions].
  - This PDF is the advance-online version with no printed page numbers, so the empty "printed" field is correct.

## Entries

**27 / Tian et al. (2020): VERDICT OK** (S, own). Every statement checks out: NN pp. 3–4, manuscript p. 13, and our reference cites the NN version 23(11):1421–1432. Nothing to add.

**100 / Tian et al. (2020): VERDICT OK** (X, na).
- Optional addition: the Tian2020.pdf in the folder has no bioRxiv stamp (it is a Word export dated 19 May 2020). It is therefore not evidently the "bioRxiv preprint (v2)" the sentence names. Keep calling it "the authors' manuscript" in the revision.

**100 / Váša et al. (2018): VERDICT OK** (X, na). The main paper (14 pp.) and the SI (31 pp.) are both in the folder, as are the full texts of the other five works.

**104 / Váša et al. (2018): VERDICT OK** (Q, own).

Errors:
1. "The rotations are Váša et al.'s": the paper gives a rotation *procedure*, applied to its own 308-region parcellation (SI p. 7). It does not supply the rotations released with the data. Write "the rotation procedure is Váša et al.'s". The same caveat applies to our_text's "the rotations of Váša et al., 2018".
2. "in one direction (p. 7)" is ambiguous. Write instead: "permuting only one of the two maps; neither the SI nor the main text (p. 5) says whether the p is one- or two-sided". Cite main text p. 5 as well.
3. "Rotating each map in turn": the function *permutes* each map (lines 32–39) using precomputed rotation-derived permutations (line 2). It does not rotate anything.
4. "a copy changed only to return the null distributions as well":
   - "Only" is the copy's own claim ("otherwise identical"). It cannot be checked, because Váša's original function is not in the folder.
   - The signature (line 19) also returns rho_emp.
   - Every `corr` call carries 'rows','complete' (lines 29, 44, 45); check this against the original before saying "only".
   - Suggested wording: "whose comment (line 17) says it … is otherwise identical".

Missing:
- Firsthand note: Váša et al. present their test as the regional analogue of earlier vertex-level tests (Alexander-Bloch et al. 2013a,b; Vandekar et al. 2015; p. 5). Only the regional implementation is their own.
- al857 is Andrea Luppi's Cambridge ID (the address on Luppi 2025, p. 1), so the released file is Luppi's copy.
- The function's header dates run to June 2018 (line 15), after the paper's Advance Access date of 27 Oct 2017 (p. 1). So the paper's own P_perm cannot be assumed to be the averaged form. This supports the entry's point that "Váša one-sided-average p" names his function, not a method stated in the paper.

**150 / Luppi et al. (2025): VERDICT OK** (Q, own). The quote is exact (raw text reads "nonlinear"), the six-species facts and pages are right, and hctsa is on pp. 3–4.

Errors:
1. good_to_know says "the quotations were first checked; both are in the current version (pp. 5, 7)". Sentence 150 has only one quotation (p. 5); the p. 7 caption quote belongs to sentence 202.
2. "the version bioRxiv now serves" cannot be checked from local files. The PDF header only says "this version posted January 10, 2026".

Missing:
- "Companion" is our own word: neither work cites the other.
- "Whether the datasets coincide is not stated" is true, but both works cite the same source studies with the same Ns. Worth saying:
  - human N = 15: Ranft et al. 2016;
  - macaque N = 5: Uhrig et al. 2018;
  - marmoset N = 4: Muta et al. 2023;
  - mouse N = 43: Gutierrez-Barragan et al.;
  - locations: preprint p. 4; Luppi 2026 pp. 779 and 781.
- "Deconvolution is not mentioned" is true of the preprint (no occurrence). Luppi 2026 does mention "cell-type deconvolution" (p. 792), so if the clause refers to it, say "HRF deconvolution".
- The preprint's named examples are AC_3 (lag 3) and RM_AMI_2 (lag 2) (p. 5); lag-1 autocorrelation is never reported. "Through r₁" is our extrapolation.
  - The per-species support is on p. 7 (Fig. 4b–g): intrinsic timescales are reduced [in every species].
- Add Fig. 3a (p. 7) to the evidence, since it lists the 15 contrasts.
- All page numbers refer to the 10 Jan 2026 version. Whether version 1 (the one our reference cites) has the same six species cannot be checked from the folder.

**202 / Luppi et al. (2025): VERDICT WRONG → Q as written** (S after rewording; firsthand own is right).

Errors:
1. our_text and we_cite_it_for both say "the caption of an example macaque time series". The Fig. 3e caption (p. 7) describes two example series, from an awake and an anaesthetised macaque, plus their autocorrelation plots. Reword as "in the caption of Fig. 3e, example time series from an awake and an anaesthetised macaque"; S then holds.

Everything else is verified: the DOI, hctsa (pp. 3–4), n = 15 and TR 1.838 s (pp. 4, 20), and both quotes (pp. 5, 7).

Missing:
- good_to_know should say that the p. 5 quote comes from features consistent across all 15 contrasts in all six species. The four-species parenthesis suggests it comes from the fMRI species alone.
- Firsthand note: the human data were published before (Ranft et al. 2016; p. 19 [published before], reusing the original wording). The hctsa analysis and both quoted findings are the preprint's own.
- "Posted 24 March 2025" and "version 1" match our reference entry but cannot be checked from the local PDF.
