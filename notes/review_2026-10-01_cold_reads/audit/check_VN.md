# VN — the statements the citation audit left unchecked, against the PDFs (HEAD 9caa60b)

No error found. One locator set is inexact (VN-1); ten notes follow. Three things could not be checked because the pages are in no PDF here (VN-5, VN-6, VN-7).

"p." is the N-th page of the PDF file. Luppi2026.pdf pp. 33–41 (the Reporting Summary) have no text layer; I read them by OCR and on the page images of pp. 35 and 37–40. Nothing under VT was changed; scratch is in `VW/VN/`.

## Findings

**VN-1 — inexact**
- Where: `manuscript/supplementary.md`, S20 Table A, row 5, data and parcellation cells (same text in `notes/partB5_literature_v2.md`, Table A, row 5): "TR 1.838 s, 350 volumes, 3 T (pp. 37–39)"; "500 volumes per run (pp. 38–39)"; "9.4 T (pp. 38–40)"; "7 T (pp. 4, 38–40)"; "mouse Allen CCFv3-162 (pp. 37–40)".
- Problem: the ranges run past, or start before, the pages that carry the facts.
  - Every acquisition parameter (TR, volumes, field strength, all four species) is on p. 38; the 350 volumes are also on p. 37. Pages 39–40 hold preprocessing only.
  - All four parcellations are on p. 39 (atlas names again on p. 40, region counts also on p. 21). Pages 37–38 hold none.
- Evidence: Luppi2026.pdf pp. 37–40, p. 21.

**VN-2 — note**
- Where: S20 row 5, data cell: "sevoflurane at 2 vol% and 3 vol% (burst suppression) and recovery (p. 37, which announces five sessions and names these four; p. 35 speaks of three anaesthesia levels".
- Problem: p. 37 prints "3 vol% burst-suppression" with nothing between; the parenthesis is the table's reading, not the PDF's statement. The PDF's own counts agree with each other only if 3 vol% and burst suppression are two sessions. The cell reports the mismatch but its gloss fixes the other reading. No operating point depends on it.
- Evidence: p. 37 "five scanning sessions"; p. 35 "3 different anaesthesia levels" (twice) and "3 different doses".

**VN-3 — note**
- Where: S20 row 5, preprocessing cell, "**HRF deconvolution not mentioned in the main text** (the Supplementary Methods it defers to were not read)", and last cell, "HRF deconvolution is not mentioned in the main text."
- Problem: true, but narrower than the PDF supports. The committed wording, "not mentioned anywhere in the PDF", holds.
  - The cell's own preprocessing details (p. 39) come from the Reporting Summary, not the main text, and its noise-removal fields (pp. 39–40) name no deconvolution step for any species.
  - The paper does defer to Supplementary Methods (p. 18, first sentence of Methods); they are not in the PDF.
  - The recorded reason of replacements U17.5 and LT07.5 ("an observation … removed") describes a removal; the replacement narrows a statement.
- Evidence, whole-PDF search:
  - "deconvol": once, p. 16 ("cell-type deconvolution", transcriptomics).
  - "HRF", "hemodynamic": none.
  - "haemodynamic": once, p. 3 ("haemodynamic fMRI timeseries").
  - pp. 33–41: none ("spatial convolution", p. 40, is the marmoset smoothing).

**VN-4 — note**
- Where: `notes/review_2026-10-01_cold_reads/pubmed_search/screening.md`, Pope row: "a heuristic measure of redundancy/synergy dominance" (its p. 3).
- Problem: the quotation is verbatim on PDF p. 3, but that page is printed "2"; the PDF opens with a publisher's cover page. "its p. 3" is right only as a PDF index.
- Evidence: Pope2025.pdf p. 3.

**VN-5 — note (not checked)**
- Where: S20 row 6 (Down et al.), "GSR not mentioned … **no deconvolution mentioned**", and "CCS re-validation in the supplement (p. 6)".
- Problem: Down2026.pdf holds only pages 1/55–25/55, in every copy on this machine. Pages 26–55 could not be read. On p. 4 the paper refers to "the boilerplate output from fMRIPrep" in the supplementary materials for full preprocessing details, so both negatives hold for pp. 1–25 only.
- Evidence: pp. 1–25 have no "global signal", "GSR", "deconvol", "HRF" or "h(a)emodynamic".

**VN-6 — note (not checked, with an observation)**
- Where: `manuscript/draft_v2.md`, Results 7, "each atom is read as its quantile among random systems of equal total mutual information"; `manuscript/si/S3_Text.md` §10, "and are otherwise random (their p. 7)".
- Problem: the S1 Appendix is a separate file, not part of Liardi2025.pdf (25 pages), so I could not read it. The article's own account of the further constructions does not contradict either description: each keeps the total mutual information equal, and atoms are read by quantile.
  - One difference: the data-driven nulls fix the coefficient matrix to its empirical estimate and randomise only the residual covariance, so they are not "otherwise random". S3 Text cites p. 7, where that phrase is the primary construction's.
- Evidence: Liardi2025.pdf p. 7 (algorithm), p. 19 (VAR nulls), pp. 20–21 (data-driven variant), p. 21 (list of appendices).

**VN-7 — note (not checked)**
- Where: `pubmed_search/psychedelic_phiid_search.md`, three descriptions of Varley et al. 2024, *Network Neuroscience* 8(4):1421–1438.
- Problem: no PDF of this work is available. Varley2024.pdf in the folder is the arXiv note 2407.16601. Only the bibliographic line could be compared; it agrees with `pubmed_psychedelic_search.csv`.

**VN-8 — note**
- Where: `draft_v2.md`, Methods, Dataset: "Schaefer-100 parcels (released with Schaefer et al., 2018)".
- Problem: the article names the released resolutions as 400, 600, 800 and 1000 parcels and a public multiresolution release; a 100-parcel resolution is not named. "Released with" rests on the release (`data/Schaefer2018_100Parcels_7Networks_order.lut`), not on the PDF. Unchanged from 8bd189e.
- Evidence: Schaefer2018.pdf pp. 1, 3.

**VN-9 — note**
- Where: S3 Text §11: "whose Theorem 1 states that a system has a causally emergent feature if and only if the synergy of its parts about its future is positive".
- Problem: the theorem is stated "of order k", with the k-th-order synergy; the paraphrase drops the order. For pairs (n = 2, k = 1) nothing changes. The claim record keeps "of order k".
- Evidence: Rosas2020.pdf p. 7 (theorem), p. 6 (definition of the k-th-order synergy).

**VN-10 — note**
- Where: S20 row 2, last cell: "inside the map if each used both the Gaussian estimator and MMI, which the paper does not state."
- Problem: exact; p. 12 names the two validations without saying which redundancy function the Gaussian one used or which estimator the MMI one used. The nearest statement is on p. 8, which calls the replication "emergence measures based on a linear-Gaussian approximation (Fig. S3)"; Fig. S3 holds both validations (p. 3). The supplement is not in the PDF.
- Evidence: Luppi2023.pdf pp. 3, 8, 12.

**VN-11 — note (outside the assigned items)**
- Where: S20 Table, "References cited only in this table": "Destexhe, A., Menon, D., Stamatakis, E. A.".
- Problem: the preprint prints "David K. Menon"; the main text's entries have "Menon, D. K.". The entry says it was checked against Crossref.
- Evidence: Luppi2025.pdf p. 1 (in `b35/newpdf/`, version of 10 January 2026).

## Checked and found exact

**1. Luppi et al. 2023 (17 pages, PDF page = article page).**
- (a) S20 row 2, every cell:
  - Study: title, NeuroImage 269, 119926 (p. 1).
  - Data: 21 DoC, 10 UWS, 11 MCS, 18 controls (p. 2). 22 included, 10 UWS and 12 MCS, one with functional data only; 300 volumes in 10 min; controls 160 volumes in 5:20 min; TR 2000 ms; Siemens Trio 3T (all p. 10; Table 1 has 22 rows).
  - Parcellation: Lausanne 234, replication 129 (pp. 4, 11).
  - Preprocessing: 0.008–0.09 Hz and both quoted phrases (p. 11); aCompCor (pp. 10–11); despiking, ART outliers and scrubbing (p. 10); deconvolution with the Wu et al. 2013 toolbox (p. 12).
  - Quantity: "global emergence capacity" (pp. 3, 7). The paper does cite Rosas et al. 2020 for it: p. 2 and p. 11 (three times), reference list p. 16. Rosas p. 8, Eq. 7, gives the same two-part decomposition.
  - Estimator and lag: CCS plug-in on mean-binarised signals and the two validations (p. 12); 1 TR (2 s) (p. 3).
  - The 4-TR quotation is on p. 3; the paper's sentence begins with a capital "No".
  - The timescale quotation is on p. 8. Effect: p. 3.
- (b) S3 Text §11:
  - Luppi 2023 "their p. 12": exact.
  - Luppi 2022 "p. 773 … PDF pp. 3, 14": exact (PDF p. 3 is printed 773; "mean-binarized" and "plug-in estimator" on PDF p. 14).
  - Rosas: Theorem 1 and "a measure of the emergence capacity" on PDF p. 7.
  - Ince 2017 Definition 2 (PDF p. 13) keeps the three pairwise marginals.
  - "Two studies … use binarised signals": no other study PDF mentions binarised or discretised signals.
- (c) Main text: the Introduction's CCS and one-TR statements, Results 6 and the Discussion are exact. No other study PDF states a value of the lag.
- Reference entry: 13 authors in order, title, DOI (p. 1).

**2. Luppi et al. 2026 (41 pages: article 1–26, Extended Data 27–32, Reporting Summary 33–41).**
- S. P. Singleton is the sixth author (p. 1).
- Reference entry: 25 authors in the PDF's order, title, volume 10, 777–802, DOI. The issue number is not printed ("April 2026").
- S20 row 5, all other cells and pages:
  - N = 15, 16 completed, 20 recruited (p. 35); "deep anaesthesia" (p. 3).
  - Macaques 5 + 5, three awake and two DBS (pp. 3, 5, 35); marmosets 4 (pp. 3, 35).
  - Mice 10, 14, 19 (p. 4); the total 43 is on p. 5.
  - Human preprocessing and CONN 17f (p. 39); macaque band and notch (p. 39); marmoset and mouse 0.01–0.1 Hz (p. 40).
  - "No global signal regression" (p. 40, mouse). Human GSR is not mentioned; "global signal" occurs only as an ART threshold (p. 40).
  - ΦR, Eq. 9 (p. 20); MMI double redundancy and JIDT Gaussian solver (p. 19); Imperial-MIND-lab code (p. 22).
  - No value of the lag anywhere. Surrogate quotation (p. 13). Effect (p. 5).
  - Last cell: the five ideal-band-pass values recompute. The preprint's quotation, its "all contrasts" basis, the six species and the same source studies and numbers are confirmed in the preprint PDF.
- Main text: "negative atoms … noted by … Luppi et al., 2026" is on p. 19.

**3. Zhang et al. 2025 (20 pages).** S20 row 8, every cell exact.
- Title, authors, 15, 636 (p. 1).
- 203 = 34 + 60 + 59 + 50; TR 3001.0 ms; 140 volumes; DPABI and SPM12; "6 × 6 × 6"; mean FD > 0.5 mm (p. 3).
- MMI sentence (pp. 4–5); syn→syn atom (p. 5); JIDT v1.5 and AAL-90 in Yeo networks (p. 6); per-subject reconstruction (p. 7); effect (pp. 1, 11–12).
- No "window", band-pass, filter, Hz, regression, nuisance, covariate, global signal, GSR, deconvolution, HRF, value of τ, or redundancy result anywhere.
- 0.61 and 0.45 recompute.
- Reference entry: exact.

**4. Pope et al. 2025.**
- The measure is the local O-information (p. 6).
- 95 subjects (pp. 2, 4, 7, 9).
- Resting-state BOLD; no ΦID computed.
- Authors and title (p. 2); the bibliographic line agrees with the export.

**5. Results 3.** Each work supports its part.
- Raut: PDF p. 2, in nearly the main text's words.
- Ito: PDF pp. 5–6; its terms are unimodal (visual, auditory, somatomotor) and transmodal.
- Murray: PDF p. 1 (sensory shorter, prefrontal longer), pp. 2, 4 (macaque, single-neuron). Its PDF is the advance online version, so volume and pages cannot be confirmed from it.
- Against 8bd189e the statement is the same. HEAD drops the opening "In the literature" and the closing clause on S20 Table; "from sensory to prefrontal cortex" is there.

**6. Down et al. 2026, pp. 1–25.** Row 6 holds on these pages.
- Counts (pp. 2–3); regressors, band and "No blurring step" (p. 4); lag (p. 5); "suitably Gaussian" (p. 6, sentence beginning on p. 5); CCS in the supplement (p. 6); sixteen atoms (p. 7); abstract quotation (p. 1).
- S3 Text §1's statement on non-negative atoms (p. 7).

**7. Liardi et al. 2025.**
- Method as described (p. 7). For time series the total is past-to-future mutual information (pp. 9, 19).
- The psychedelic note's pages 3, 9–11 and 14: exact.
- Reference entry: exact.

**8. Carried-over works, main-text sentences.**
- Faes 2025: i.i.d. assumption "often violated" (p. 1). S3 Text's three quotations are verbatim on p. 1; the PDF is dated 7 October 2025.
- Faes 2017: exact decomposition of transfer entropy for Gaussian processes (pp. 1, 15).
- Ince 2017: CCS, a single-target redundancy (pp. 1, 12).
- Huang 2018: lag-1 autocorrelation defined (p. 3), rises in sedation (p. 4), falls in deep anaesthesia and DoC (p. 1).
- Tarchi 2026: no redundancy function named anywhere; classification sentence (pp. 5–6); 12 authors and citation.
- Nago 2026: an empirical fMRI ΦID study; MMI (p. 4); no Gaussian estimator, lag or deconvolution stated.
- Yeo 2011: seven networks (pp. 4, 9); 13 authors, 106:1125–1165.
- Schaefer 2018: authors, 28:3095–3114; see VN-8.
- Beyond the list, from `b35/finaltest/Downloads/new_papers/`: Theiler 1992, Tian 2020 (Scale I, 16 regions), Cousineau 2005 and Morey 2008 support their sentences.

**9. Literature file.** Table A rows 2, 5, 8 (and 6) are identical to S20 Table cell for cell. The only difference is in row 2's last cell, where "B2" and "B25" stand for the two S3 Text references.
