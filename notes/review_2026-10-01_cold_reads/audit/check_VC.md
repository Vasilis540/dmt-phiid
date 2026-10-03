# VC — verification of the citation dispositions (C01–C25), the four extra points and the claim record

**Result.** All 25 corrections are present at HEAD (9caa60b) at the places named, and every corrected statement about a cited work is right against the PDFs. I found no `error`. Seven things are `inexact`: four in the claim record, two in `dispositions_revision.md` and one in the replacements file. Two more are `note`. None touches a manuscript file.

**How I checked.** Read-only; the tree is still clean. I read every cited page with `pdftotext -f N -l N`. The Reporting Summary is image-only: I rendered it at 300 dpi and read the four page images, using OCR only to search. `te_filter_check.py` was copied to `VW/VC/` and run there. Scratch is under `$SP/r24/vwork/VC/`.

Paths below are relative to VT; "claim record" is `notes/review_2026-10-01_cold_reads/claims/claims_2026-10-01.md`, "dispositions" is `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`.

## Findings

**VC-1** — inexact
- Where: claim record, Reporting Summary item, lines 57–58: "Cited in S4 Text at D3, D4, D5, D8, A1–A4, P1–P4 and P6, in S1 Text and in the main text's Dataset paragraph."
- Problem: the list is incomplete. S3 Text §5 also states the replacement of volumes and cites the Reporting Summary. The pointers of Timmermann item 4 (lines 29–30, "for the censoring, in the main text's Dataset and Limitations paragraphs") and Singleton item 1 (lines 50–51) omit it too.
- Evidence: `manuscript/si/S3_Text.md` line 264: "The data authors replaced each volume with framewise displacement above 0.4 by the mean of the surrounding volumes (Timmermann et al., 2023, Methods; Singleton et al., 2025, Methods and Reporting Summary)". The statement itself is right (step 7 on Timmermann p. 9 and Singleton p. 8; Reporting Summary p. 4).

**VC-2** — inexact
- Where: claim record, Liardi et al. (2025), second item, lines 157–158: "Stated where the text says that no application of ΦID to psychedelic data was found (Discussion; S3 Text §10)."
- Problem: S3 Text §10 does not say that none was found. It gives the PubMed string and "its 2 records and their screening are in …", and cites Liardi et al. in another paragraph, for the normalisation and ΦID "as a possible further generalisation". The item's other details (MMI on p. 3, the Ns on p. 9, Fig 4, the CCS and dependency-constraints comparison) are stated in neither named place.
- Evidence: "found none" is in `manuscript/draft_v2.md` line 253 (Methods) and line 187 (Discussion: "is a PID on MEG under LSD, ketamine and psilocybin"). The details stand in `pubmed_search/psychedelic_phiid_search.md` lines 53–55 and `notes/partB5_literature_v2.md` line 38.

**VC-3** — inexact
- Where: dispositions, C21, lines 842–843: "S1 Text and S4 Text D6 no longer place the ratings on the day of the analysed runs: "collected in scan runs other than the analysed ones, in the second scanning session"."
- Problem: the quoted words are S1 Text's only (line 11). The substance holds in both places.
- Evidence: `manuscript/si/S4_Text.md` line 14 (D6): "collected in other scan runs, in the second scanning session (Timmermann et al., 2023; Singleton et al., 2025)".

**VC-4** — inexact
- Where: dispositions, "Murray et al. (2014)", lines 877–878: "The words are restored (T51 (ii)), so the sentence is the committed one, which the check of 29–30 September 2026 covered."
- Problem: the sentence at HEAD is not the committed one word for word. "In the literature" is dropped and its end is joined differently. Only the clause on the three works is identical.
- Evidence: `git show 8bd189e:manuscript/draft_v2.md` line 108 begins "In the literature the intrinsic timescale of BOLD lengthens …"; HEAD line 114 begins "The intrinsic timescale of BOLD lengthens …". Replacement R301's `why` records "'In the literature' dropped". `notes/review_2026-09-30/claims/claims.csv` lines 26–28 hold the committed sentence.

**VC-5** — inexact
- Where: `notes/review_2026-10-01_cold_reads/revision/text_replacements_2026-10-01_cold_reads_revision.json`, id S318c, `why`: "the six authors of Liardi et al. (2025) include four of the seven of Mediano et al. (2021), not its first author."
- Problem: "its" is ambiguous. Read with the nearer antecedent (Mediano et al., 2021) the clause is untrue: P. A. M. Mediano is the sixth author of Liardi et al. The audit's point was that Liardi et al.'s own first author is not among the seven.
- Evidence: first pages of Liardi2025.pdf (Liardi, Rosas, Carhart-Harris, Blackburne, Bor, Mediano) and Mediano2021.pdf / Mediano2025.pdf (Mediano, Rosas, Luppi, Carhart-Harris, Bor, Seth, Barrett). S3 Text §10 itself is exact.

**VC-6** — inexact
- Where: claim record, header, lines 5–6: "A page is the page of the PDF as saved, which is the article's own page where the article carries page numbers."
- Problem: for three works the pages given are journal pages, not pages of the PDF as saved. The locators are right as journal pages.
- Evidence: Barnett & Seth pp. 404/405/406/408 are PDF pp. 1/2/3/5; Seth et al. pp. 540/543/545/548 are PDF pp. 1/4/6/9; Strassman & Qualls p. 89 is PDF p. 5 (footer "ARCH GEN PSYCHIATRY/VOL 51, FEB 1994 89").

**VC-7** — inexact
- Where: claim record, Rosas et al. (2020), lines 105–106: "Stated in S3 Text §11 and S20 Table (row 2); the main text's Results 6 cites the work where it names the emergence capacity."
- Problem: S20 Table's row 2 states neither Theorem 1 nor the sentence after Corollary 1. Like Results 6, it only names the work for the quantity.
- Evidence: `manuscript/supplementary.md` line 1718: "(mean pairwise ΦID-derived emergence; the emergence capacity of Rosas et al. 2020)". `manuscript/si/S3_Text.md` line 560 states both.

**VC-8** — note
- Where: dispositions, C14, lines 792–793: "the reasons recorded with the two replacements say the same."
- Problem: only one of the two reasons notes that the paragraph begins on p. 14. Both give PDF p. 15, which is right.
- Evidence: the JSON's D05 `why` ends "…yielded a gradient', PDF p. 15"; S319's has "the paragraph begins on PDF p. 14 and the sentence quoted is at the head of p. 15".

**VC-9** — note
- Where: claim record as a whole (header, line 3: "Every statement the revised text … makes about a cited work …").
- Problem: two statements made by the revision have no item or no named place. (a) S4 Text D3 and D4 cite "the exclusion criteria" (and previous psychedelic experience) to both source papers; no item lists them. (b) The Introduction's new clause on Luppi et al. (2022) is not among that item's places ("(Discussion; S3 Text §10)", PDF p. 15). Both statements are right.
- Evidence: Timmermann 2023 PDF p. 9 and Singleton 2025 PDF p. 8 ("Exclusion criteria included: … absence of experience with a psychedelic …"); Luppi 2022 PDF p. 2 ("the difference between these ranks (synergy minus redundancy)").

## Verdict on each C-finding

- **C01 — verified.** Results 7 (line 173) attributes no invariance to the lag-1 pair; both quoted phrases occur verbatim. S3 Text §3 (line 124) matches Barnett & Seth (abstract, pp. 405, 406, 408) and Seth et al. (abstract, pp. 543, 545, 548), including "often", the infinite model order, the invertible-filter proviso and the exclusion of onset delays.
  - `te_filter_check.py` prints what §3 quotes: filter 1 + 0.6L + 0.3L² (zeros of modulus 1.826), coefficients 0.90 and 0.70, innovation correlation 0.3, lag-1 values 0 before and 0.001508 and 0.000408 after, 0.000000 at ten lags, 0 on the symmetric family.
  - My own state-space recomputation (`VW/VC/te_indep.py`) gives 0.0015079 and 0.0004081, and 1.7e-8 and 5.0e-9 at ten lags.
  - No invariance claim for the lag-1 pair remains in any file searched. The record's disposition of A's m10 agrees.
- **C02 — verified.** Results 7 and S3 Text §10 describe the method as Liardi et al. p. 7 does (same total mutual information, otherwise random, quantile); p. 20 read as well. No subtraction is described anywhere. "Four of the ΦID paper's seven authors, with two others" is right against both author lists. The record's disposition of A's m14 agrees.
- **C03 — verified (as R10).** The Dataset paragraph cites the six to Singleton et al. alone; S1 Text and S4 Text D4 give both counts as Timmermann p. 9 and Singleton p. 8 / Reporting Summary p. 2 state them; "B29, outcome" item (i) says whose count it is. No other attribution of the six remains.
- **C04 — verified.** The Introduction and S20 Table row 3 (and the literature file) give the name (Luppi 2024 p. 6) and the formula (Eq. 5, p. 20, after "we use") without setting one against the other. Results 1 identifies Eq. 5 with the four-atom sum.
- **C05 — verified (as R37).** Results 6 cites Rosas et al. (2020); all 48 reference entries now have a main-text citation.
- **C06 — verified (as R11).** S3 Text §10 has the quoted sentence; `search_string.txt` and the folder's README say PubMed's reading was not kept. Both strings in §10 equal the search files character for character; the exports hold 11 and 2 records.
- **C07 — verified (as T30).** Methods and the literature file carry the quoted wordings. The one remaining "outside the scope" (Discussion) uses the defined scope.
- **C08 — verified.** Only Timmermann p. 9 has the screening visit; "screen" and "initial visit" occur in none of Singleton's three documents.
- **C09 — verified.** Who was blind and global signal regression last are cited to Singleton alone in S1 Text, S4 D8 and P6. Timmermann p. 9 has "single-blind" only and p. 8 "we chose not to perform GSR in our main analyses".
- **C10 — verified.** Results 7 only points to S3 Text §8, which gives Honari et al.'s concern with their simulation's result (their PDF p. 10).
- **C11 — verified.** "Table A of the literature file lists" is in S3 Text §10.
- **C12 — verified.** Pointer and both places as stated.
- **C13 — verified.** The quotation is whole and verbatim (Timmermann p. 9).
- **C14 — verified,** with VC-8. Luppi 2022: the sentence heads PDF p. 15, the paragraph begins on p. 14.
- **C15 — verified.** Theorem 1 and "serves as a measure of the emergence capacity of the system" are on Rosas PDF p. 7, Definition 2 on p. 6; S3 Text §11 has the quoted wording.
- **C16 — verified.** (a) Timmermann 2019 abstract and p. 3, plasma relation on pp. 4–5. (b) Liardi pp. 3, 9, 10, 11, 14, and the search note has the same pages. (c) Gao pp. 3–4 and the variogram-matching surrogates on p. 4.
- **C17 — verified as to the four corrections,** with VC-1 on the completeness of the Reporting Summary pointer.
- **C18 — verified.** The Reporting Summary p. 4 field reads exactly as quoted, with "Volume censoring" as the form's label.
- **C19 — verified.** "often", the equivalence on p. 406 and p. 543, and "in theory and in simulations" are in S3 Text §3 and the record.
- **C20 — verified.** (a) P1, (b) P3, (c) A1 and the closing paragraph, (d) the Ethics statement without "pseudonymised" and Sh5. "Instruct", "pseudonym", "anonym", "handed", "restrain", "mock", FOV, acceleration, phase encoding and distortion occur in none of the five documents for these images.
  - One caveat the audit already weighed: the reference Singleton et al. cite for ANTS is titled "Advanced normalization tools: V1.0" (their ref. 79). S4 P1's "no version of these packages as applied to these images" stands with its qualifier.
- **C21 — verified,** with VC-3. The session descriptions the finding quotes are as the PDFs have them; the Reporting Summary p. 4 does say "Augmented 232 region Schaefer-Tian atlas". The record's list of items for the note to C.T. and S.P.S. includes whether a testing day held one substance or both.
- **C22 — verified (as R38).** Rows 5 and 10 of S20 Table and of the literature file carry no request.
- **C23 — verified.** "their Eq. 5, the four-atom sum of Results 1" precedes "the same four-atom sum".
- **C24 — verified (as R01).** No "@@" remains outside the three audit reports; S5 Text §5 states the audits.
- **C25 — verified** as far as it touches my scope. The check script gives the Abstract 300 words. "Scope map" is gone from the main text's list of supporting information; `manuscript/figures/captions_v2.md` line 7 still has "The scope map", which CLAUDE.md says the figures commit regenerates.

Every phrase the C dispositions (and R01, R10, R11, R13, R19, R37, R38, T19, T30, T51) put in quotation marks as corrected text occurs word for word in a file at HEAD, except as VC-3 says.

## The four extra points

1. **Introduction on Luppi et al. (2022) — verified.** PDF p. 2 ranks each region by synergy and by redundancy and takes "the difference between these ranks (synergy minus redundancy)"; Methods (PDF pp. 14–15) rank by nodal strength. "Its regional rank minus redundancy's" is a correct description; their synergy is the persistent atom (sts).
2. **"The ΦID authors" — verified** (see C02).
3. **Cliff et al. — verified.** "41.8%" and "over 88% (not shown in the figure)" are on article p. 013145-16; the passage begins at the foot of p. 15.
4. **Results 3 — verified against the three PDFs,** with VC-4. Raut p. 2 (sensorimotor to association gradients), Ito (transmodal slower than unimodal), Murray p. 1 (macaque single-neuron spike trains, sensory to prefrontal).

## Checked and found exact

- **Claim record, every item** (except VC-1, VC-2, VC-6, VC-7, VC-9): every page, every fact and all 23 quoted phrases match the sources, and each "Stated in" place holds the content.
  - Timmermann 2023: pp. 2, 4, 8, 9 and SI p. 5 (Fig. S4, whole sample p = 0.003).
  - Singleton 2025: p. 8, p. 4, SI p. 14, Reporting Summary pp. 2–4 (read on the images).
  - Gao 2026: every number on pp. 1, 3, 4; no HRF or global-signal mention in its nine pages; 14 authors.
  - Timmermann 2019 (16 authors), Schartner 2017 (abstract), Strassman & Qualls 1994 (abstract; pp. 88–89), Rosas 2020, Barnett & Seth 2011, Seth et al. 2013, Luppi 2022, Luppi 2024, Cliff 2021, Liardi 2025, Barrett 2015 (p. 4, Fig. 3 caption).
- **S1 Text and S4 Text** (D3, D4, D5, D6, D8, A1–A5, P1–P4, P6, P8, Sh5, closing paragraph), the Dataset paragraph and the Ethics statement: every statement and every single or joint attribution against the five documents.
- **Discussion:** the Singleton SI phrases, Timmermann 2019/2023, Schartner, Strassman, Fig. S4, and Luppi 2022 Table 1 (surrogate 0.09, 0.01, 0.17, 0.21, 0.26, −0.16, one significant, against 0.22–0.54 observed).
- **S3 Text §8:** Honari (PDF p. 10) and Arbabshirani ("reintroduces autocorrelation").
- **The seven added reference entries** against the PDFs' front matter.
- **The three rows of `main_text_numbers.csv`** that point into the claim record resolve to the lines and anchors named.
- **Items the audit could not check for want of PDFs, now checked:**
  - Luppi 2023: counts on pp. 2 and 10; CCS on mean-binarised signals on p. 12; emergence capacity tied to Rosas et al.; lag 1 TR.
  - Luppi 2026: no HRF deconvolution in the text pages 1–33 nor, by OCR, in the image-only pages 34–41; S. P. Singleton is an author.
  - Zhang 2025: "6 × 6 × 6".
  - Pope 2025: "a heuristic measure of redundancy/synergy dominance" on p. 3; 95 subjects.
- **Dispositions:** the 25 C-dispositions all read "Corrected"; the file's totals (140 + 2 + 3 = 145) hold.

## Not verifiable here

- No internet: the Crossref checks; the issue numbers 201(2) and 51(2) (the Strassman footer does say "FEB 1994"); the arXiv id of Liardi et al.
- No PDF supplied: Varley et al. 2024 (*Network Neuroscience*; its line agrees with the PubMed export) and the bioRxiv preprint of Luppi et al. 2025.
- Down et al. 2026: the PDF holds 25 pages only, as in the audit.
- The supplementary files of Gao 2026 and Luppi 2026 were not available.
