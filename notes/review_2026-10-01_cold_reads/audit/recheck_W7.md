# W7 — the statements about cited works that were changed or added after the ten checks, against the PDFs

**Result.** No error found: every fact, page, count and quoted phrase about a cited work that was changed or added between `checked` and HEAD agrees with the PDF named for it. 12 findings: 0 errors, 7 inexact, 5 notes. The inexact ones are pointers of the claim record, one descriptor, one locator's wording, and three statements about what was done or what a report says; none touches a value or a statement of substance in a manuscript file.

**How checked.** Read-only; the tree is unchanged (`git status` empty at the end). Pages were read one by one with `pdftotext -f N -l N`. Pages 33–41 of Luppi2026.pdf, pages 2–4 of Singleton2025_RS.pdf and the footers of Strassman1994.pdf (pp. 1 and 5) were rendered with `pdftoppm` and read on the images; OCR was used to search only. Every quotation in the assigned parts of the dispositions was tested by script against the files at HEAD, and every phrase the claim record gives in quotation marks as a work's words was tested by script against the page texts. Scratch files are under `VW/W7/`.

Paths are relative to VT. "Claim record" is `notes/review_2026-10-01_cold_reads/claims/claims_2026-10-01.md`; "dispositions" is `notes/review_2026-10-01_cold_reads/audit/dispositions_revision.md`; "search note" is `notes/review_2026-10-01_cold_reads/pubmed_search/psychedelic_phiid_search.md`. "p." of a work is the page of the PDF as saved.

## Findings

**W7-1 — inexact**
- Where: dispositions, VN-11 (lines 1492–1493) and "Found while the findings were settled" (line 1761): "One thing that no session raised was corrected with them."
- Problem: The entry of Luppi et al. (2025) under S20 Table was changed in two places after the checks: "Menon, D." to "Menon, D. K." (VN-11) and "Legare, A." to "Légaré, A.". The second answers no finding of any report and stands in no disposition; VN-11's paragraph gives the first alone, and the closing section's count of one thing corrected without a finding leaves it out. The change itself is right.
- Evidence: `git diff checked HEAD -- manuscript/supplementary.md`, line 1742; replacements U21 and U22 of the replacements file (U22's `why`: "The preprint prints the author's name as Antoine Légaré."); neither "Legare" nor "Légaré" occurs in any file of `audit/`; `check_VN.md` lines 68–71 name "Menon, D." alone. Luppi2025.pdf p. 1 prints "Antoine Légaré" and "David K. Menon"; all 27 authors of the entry agree with that page in name and order.

**W7-2 — inexact**
- Where: claim record, Liardi et al. (2025), first item (lines 196–200): "pp. 20–21: in the data-driven variant the null systems keep the coefficient matrix estimated from the data. Stated in the main text's Results 7 and in S3 Text §10".
- Problem: The clause added on pp. 20–21 is stated in S3 Text §10 only. Results 7 has the quantile "among random systems of equal total mutual information" and nothing on the data-driven variant, so the pointer now names a place that does not hold all that the item lists.
- Evidence: `manuscript/draft_v2.md` line 173; `manuscript/si/S3_Text.md` line 558. (The fact is right: Liardi2025.pdf p. 20, "fixing the coefficient matrix", continued on p. 21.)

**W7-3 — inexact**
- Where: claim record, Luppi et al. (2026): heading (line 159) "(S20 Table, row 5)" and pointer (lines 168–169) "Stated in S20 Table's row 5 and in the literature file."
- Problem: S3 Text §10 states the item's first fact too, in the sentence added for C32 ("the macaques of Luppi et al., 2026, scanned awake and under sevoflurane, propofol or ketamine"). The pointer and the heading leave that place out: the same kind of omission as VC-1.
- Evidence: `manuscript/si/S3_Text.md` line 556.

**W7-4 — inexact**
- Where: claim record, head (lines 9–12): "again after the checks of the corrections, which added the items on the exclusion criteria, on the Reporting Summary of Luppi et al. (2026), on Luppi et al. (2023) and on Murray et al. (2014), ...".
- Problem: The list goes on with further details of Gao et al. (2026) and the places that the pointers had left out, and S5 Text §5 (line 33) sends the reader to it for what was added to the record after the audit of the citations had checked it. Three things in this account are not exact. (a) One addition is not in the list: the clause on the data-driven variant of Liardi et al. (2025), pp. 20–21 (for VN-6); the new item on p. 2 of Luppi et al. (2022), with its own quotation, is there only if it is meant by the places that the pointers had left out. (b) The item on Luppi et al. (2026) is on the article's pages (3, 4–5, 18, 21) as well as on its Reporting Summary. (c) As written, the checks added the items on Luppi et al. (2023) and on Murray et al. (2014); the dispositions give these two under C27 and C26, findings of the second form of the citations audit, and no finding of the ten checks asks for either.
- Evidence: `git diff checked HEAD` of the claim record; `manuscript/si/S5_Text.md` line 33 ("its head says what was added to it afterwards"); dispositions lines 884–885 (C26) and 892 (C27); `check_VC.md`, VC-9, which names two missing statements (the exclusion criteria; the Introduction's clause on Luppi et al., 2022); in the other nine reports "claim record" occurs with neither work.

**W7-5 — inexact**
- Where: claim record, Luppi et al. (2026) (line 162): "its Reporting Summary (pp. 33–41, image-only, read from the page images)"; the same word in the unchanged item on the Reporting Summary of Singleton et al. (line 60): "(4 pp., an image-only PDF)".
- Problem: The pages are not images. They have no text layer and their text is drawn as outlines; the one image is the publisher's logo on the summary's first page. The audit of the citations corrected the same description in its own header.
- Evidence: `pdfimages -list -f 33 -l 41 Luppi2026.pdf` lists one image (943 × 148) on p. 33 and none on pp. 34–41; the content streams of pp. 33–40 hold about 130,000 to 220,000 path operators each and no page image; `pdftotext` returns nothing for the nine pages. Singleton2025_RS.pdf is built the same way (one image, on p. 1). `audit/findings_citations.md` line 11: "the two Reporting Summaries are PDFs without a text layer, not image-only ones".

**W7-6 — inexact**
- Where: `pubmed_search/screening.md` line 21 (row of Pope et al., 2025): "(PDF p. 3, the article's p. 2; the local measure is introduced on PDF p. 6)"; quoted in the dispositions at C28 (lines 899–900) and VN-4 (line 1455).
- Problem: The paper names the local O-information, and says that it is the measure chosen ("we choose to use"), on PDF p. 3, the page of the quoted phrase. The section that derives it begins on PDF p. 5 (2.2.2), and PDF p. 6 holds its formula (Eq. 7) and the sentence that it is the measure explored. "Introduced on PDF p. 6" is right for the definition only.
- Evidence: Pope2025.pdf, PDF pp. 3, 5 and 6 (the article's pp. 2, 4 and 5); the abstract (PDF p. 2) does not name the measure. The rest of the row is exact (see "Checked and found exact").

**W7-7 — inexact**
- Where: dispositions, VN-1 (line 1440): "The second form of the citations audit's report lists the same ranges".
- Problem: The report does not list them. It says that "five page ranges of row 5 are wider than the pages that hold the facts" and quotes one cell, "(pp. 4, 38–40)".
- Evidence: `audit/findings_citations.md` line 226. The correction itself is as the disposition says: each of the five ranges that `check_VN.md` lists is narrowed at HEAD, in S20 Table and in the literature file.

**W7-8 — note**
- Where: `manuscript/si/S3_Text.md` §10 (line 556): "one study of the table applies ΦID to fMRI under ketamine at an anaesthetic dose (row 5: the macaques of Luppi et al., 2026 ...)"; the same in the search note (lines 90–92).
- Problem: The macaques of a second study of the table, row 4 (Gatica et al., 2024), were given ketamine as well: 10 mg/kg intramuscularly with other agents, isoflurane being the anaesthetic, and the scan started about two hours later, to avoid "ketamine's clinical peak". "One study" holds for ketamine as the anaesthetic under which the animals were scanned; row 4 has "3 macaques under isoflurane" and does not name the injection. That study's title, abstract and keyword line name no drug, and neither PubMed search returns it.
- Evidence: Gatica2024.pdf p. 12 (the article's p. 1043): "received injections of ketamine". In the PDFs of the other studies of rows 1–10 (Down et al.: pp. 1–25) "ketamine" occurs only in Luppi et al. (2026) and, in a reference each, in Luppi et al. (2023) and (2024).

**W7-9 — note**
- Where: claim record as a whole, against S5 Text §5 (line 33): "every statement it makes about a cited work that no earlier citation check covered is in a claim record with the page on which it was checked".
- Problem: Two statements added after the checks have no item. (a) S20 Table's row 6: that the preprint of Down et al. (2026) has 55 pages and refers on p. 4 to its supplementary materials for the fMRIPrep output; the claim record has no section on that work. (b) S3 Text §10: that the abstract of Luppi et al. (2026) "names no drug"; the item on that work does not cover its abstract (the search note has it). Both statements are right.
- Evidence: `manuscript/supplementary.md` line 1722; `manuscript/si/S3_Text.md` line 556. Down2026.pdf: page labels "1/55" to "25/55"; p. 4, "boilerplate output from fMRIPrep". Luppi2026.pdf p. 1: title and abstract hold none of the string's nine drug terms and none of its decomposition terms.

**W7-10 — note**
- Where: claim record, Liardi et al. (2025), second item (lines 205–206): "S3 Text §10 gives the authors and ΦID as a possible further generalisation".
- Problem: S3 Text §10 does not name the authors. It gives their number and their relation to the ΦID paper's ("Four of the ΦID paper's seven authors, with two others"); the six names that the item lists stand in the main text's reference entry.
- Evidence: `manuscript/si/S3_Text.md` line 558; `manuscript/draft_v2.md` line 331.

**W7-11 — note**
- Where: claim record, Murray et al. (2014) (lines 173–174): "p. 1: the timescales of intrinsic fluctuations in spiking activity, measured across areas of the macaque cortex, show ...".
- Problem: p. 1 has the quoted words, "primate cortex" and "monkeys". The species is named on p. 2 only, in the caption of Fig. 1 ("in the macaque monkey"), which the item cites next for the seven areas.
- Evidence: Murray2014.pdf: "macaque" occurs once in pp. 1–2, on p. 2.

**W7-12 — note (outside the four items of the task; seen with the claim record's new sections)**
- Where: `manuscript/analysis_record.md`, the entry on the revision, lines 9177–9179: "with Barrett (2015), Liardi et al. (2025), Luppi et al. (2022, 2024) and Cliff et al. (2021) cited for statements newly made from them".
- Problem: At `checked` these works, with the seven added references and the two source papers, were the sections of the claim record (`check_VE.md` line 196 verified the sentence so). At HEAD the claim record has three more sections, on Luppi et al. (2023), Luppi et al. (2026) and Murray et al. (2014), and S3 Text §10 and S20 Table's row 5 newly state the anaesthetics of the macaques of Luppi et al. (2026). The sentence, whose words are those of `checked`, names none of the three, and the entry does not mention the sentence on ketamine that S3 Text §10 gains for C32.
- Evidence: claim record lines 150, 159 and 171; in the record from line 9147 on, "ketamine", "anaesthe" and "Murray" do not occur.

## Not checkable here

- The sentence that the search note quotes from an NLM training page (line 67: the tag "will search within a citation's title, collection title, abstract, other abstract, and author keywords") and its address cannot be checked offline. In content it agrees with the definition that the audit of the citations records under C30 from two secondary sources (title, collection title, abstract, other abstracts, keywords).
- The *Network Neuroscience* article of Varley et al. (2024) is not among the PDFs; the note's statements were compared with what the audit records (below).
- That PubMed does not return a study can be checked only against the two exports (11 and 2 records).
- The Crossref checks and the posting date of the first version of Luppi et al. (2025); the PDF read is the version of 10 January 2026.
- The supplements: Down et al. (2026), pp. 26–55; the Supplementary Methods of Luppi et al. (2026); the S1 Appendix of Liardi et al. (2025); the Supplementary Materials of Gao et al. (2026).
- That the CBIG release holds the 100-parcel file (VN-8): checked against the repository's own record of the copy, not against the release.

## Checked and found exact

**1. The claim record: every item changed or added since `checked`.**
- Head. The three works whose pages are the journal's: Barnett & Seth (PDF p. 1 prints 404–419; pp. 405, 406 and 408 are PDF pp. 2, 3 and 5), Seth et al. (540–555; pp. 543, 545 and 548 are PDF pp. 4, 6 and 9), Strassman & Qualls (the footers print 85 on PDF p. 1 and 89 on PDF p. 5; they are on the page images, not in the text layer). Every other page of the record, changed or not, is the PDF's page.
- Exclusion criteria. Timmermann et al. (2023), p. 9: both quoted phrases character for character and each criterion of the list; Singleton et al. (2025), p. 8: the same list. S4 Text D3 and D4 hold it, and no other place of the manuscript files states it.
- The three pointers that now name S3 Text §5. Line 264 of S3 Text states the replacement of volumes and cites the three documents; step 7 on p. 9 of Timmermann et al. and on p. 8 of Singleton et al., and the censoring field on p. 4 of the Reporting Summary (read on the image), each say it. The Reporting Summary is cited at every other place its pointer names (S4 Text D3, D4, D5, D8, A1–A4, P1–P4, P6; S1 Text; the Dataset paragraph); the Limitations paragraph states the censoring.
- Gao et al. (2026). p. 3: "Following Luppi et al.", "persistent synergy", "persistent redundancy", "Gaussian MMI solver" of the Java Information Dynamics Toolbox, "246 x 246" (printed with the letter x); its reference 10 is the *Nature Neuroscience* study of 2022. p. 4: "t-statistic patterns", with and without the adjustment, r = 0.942. The three phrases that S20 Table's row 10 has in quotation marks are on p. 3.
- Rosas et al. (2020). p. 7: Theorem 1 and the quoted sentence; p. 6: Definition 2. S3 Text §11 states both; Results 6 and S20 Table's row 2 cite the work where they name the quantity.
- Luppi et al. (2022). p. 2: the ranking and the quoted phrase; p. 15: the quoted sentence at the head of the page, its paragraph beginning on p. 14. The Introduction, the Discussion and S3 Text §10 hold what the items say.
- Luppi et al. (2023). p. 12: the three quotations (the inner quotation marks apart), the Gaussian solver on continuous signals, the MMI replication. Its Methods (pp. 11–12) define the system as a pair of regions and do not say which sources and target were given to the tool. Results 6, S3 Text §11, S19 Table's row of B25 (d) and S20 Table's row 2 each say "as we read"; +0.124 and +0.142 are the values of `notes/review_results/partB/binarised.csv`.
- Luppi et al. (2026). 41 pages; the article pp. 1–26 (printed 777–802); Extended Data pp. 27–32; the Reporting Summary pp. 33–41. p. 3: five macaques and the quoted phrase; p. 4: the three group sizes of the mice; p. 5: 43 mice; p. 18: the deferral to the Supplementary Methods; p. 21: 100, 82, 70 and 162 regions. Reporting Summary: p. 37, five sessions and 350 volumes; p. 38, every acquisition parameter of the four species; p. 39, the four parcellations and the human and macaque filters; p. 40, the marmoset and mouse band-pass and "No global signal regression". No HRF deconvolution on any page: in pp. 1–32 "deconvolution" occurs once (p. 16, of cell types) and "haemodynamic" once (p. 3); pp. 33–41 name none.
- Murray et al. (2014). p. 1: the quoted phrase character for character; p. 2, Fig. 1: the seven areas; "motor" occurs nowhere in the PDF; the PDF is the advance online publication. Results 3 has both quoted wordings; Raut et al. (2020), p. 2, and Ito et al. (2020), pp. 5–6, support its main clause.
- Liardi et al. (2025). p. 7: the ensemble of equal total mutual information and the quantile; pp. 20–21: the data-driven variant (the matrix is then rescaled to the same total mutual information, as in the primary construction); p. 3: MMI; p. 9: N = 19, 15 and 14, against placebo; p. 10: Fig 4; p. 11: CCS and the dependency-constraints PID; p. 14: ΦID; the six authors. The Discussion, the search note (pages 3, 9–11 and 14) and the literature file (N = 15 / 19 / 14) hold what the second item says of them.
- Every phrase that the record gives in quotation marks as a work's words, in the unchanged items too, is on the page named (those of the two Reporting Summaries read on the images).
- The three rows of `manuscript/main_text_numbers.csv` that point into the claim record (lines 53 and 64) resolve at HEAD.

**2. The search files.**
- `screening.md`, row of Pope et al. (2025): the quoted phrase is on PDF p. 3, which prints 2 (PDF p. 1 is the publisher's cover sheet), and describes the O-information; the paper's measure is the local O-information, its form resolved in time; resting-state BOLD of 95 subjects (PDF pp. 2 and 4); no ΦID is computed. Closing sentences: `pubmed_search.csv` holds 11 records, six of them studies of rows 2, 3, 6, 7, 8 and 9; the studies of rows 1, 4 and 5 are not among them; Gao et al. (2026) is (PMID 42361709); Table A's rows 1–10 are the ten studies.
- Search note, Liardi et al. (2025): the abstract names partial information decomposition and "human neuroimaging data" and no drug, nor does the author summary; the PDF prints no keyword line; the ketamine recordings (N = 19) are cited to its reference 43, whose title has "subanesthetic doses of ketamine".
- Search note, Luppi et al. (2026): the quoted phrase on p. 3 and the ketamine runs on p. 4; the title and abstract hold no drug term and no decomposition term of the string; the export of the second search holds 2 records, neither that study.
- Search note, Varley et al. (2024): its statements (title; 8(4):1421; organotypic rat cortical cultures under DPT; partial information decomposition, transfer entropy and active information storage; no ΦID; not cited in the paper; title and abstract with a drug term and "synergy" alone; "partial information decomposition" in the keyword line of the first page) agree with the audit's "Checked and found exact", check 4, with C30 and with `pubmed_psychedelic_search.csv`. The paper's "Varley (2024)" is the arXiv note.

**3. The paper's changed statements.**
- Results 6: "as we read it" (item on Luppi et al., 2023, above). Discussion: the parenthesis on Liardi et al. (2025), with the pointer to S3 Text §10, which holds the sentence on anaesthesia; "(S3 Text §4, §10)": §4 holds the statement on the exposure per unit of spectral difference and §10 the HCP data at TR 0.72 s.
- S3 Text §10: ketamine is among the second string's terms; row 5's macaques; "whose abstract names no drug"; the data-driven variant on pp. 20–21; "Four of the ΦID paper's seven authors, with two others" (Mediano2021.pdf p. 1: seven authors, four of them among the six of Liardi et al.).
- S3 Text §11: Theorem 1 with its order k ("kth-order synergy" is the work's term, p. 6); "their p. 12" for Luppi et al. (2023); "as we read their Methods" stands for the choice of sources and target and for the binarisation of each signal once, neither of which the Methods state.
- S20 Table, row 5: every page of the cells, the quoted "3 vol% burst-suppression" (p. 37) and "No global signal regression" (p. 40), the three anaesthetics (pp. 3 and 35), 15 analysed, 16 completed and 20 recruited (p. 35); the locators added for p. 5, p. 21 and p. 40 are right; the six ideal-band-pass values recompute (0.81; 0.90 and 0.97; 0.73; 0.93 and 0.90). Row 6: the page labels, p. 4, the reference list ending on p. 25; "global signal", "GSR", "deconvol", "HRF" and "h(a)emodynamic" occur nowhere in pp. 1–25; 0.85 recomputes. The literature file's rows 5 and 6 are identical to S20 Table's.
- The entry of Luppi et al. (2025): 27 authors in the preprint's order, title and DOI (Luppi2025.pdf p. 1).

**4. The dispositions.** C26 to C32, the five points raised outside the findings, VC-1 to VC-9 and VN-1 to VN-11:
- Every text that a disposition quotes as corrected is at the place named, word for word (56 quotations tested; the four not found are quotations of earlier forms or of a report's heading). Each correction answers its finding, but for what W7-1, W7-6 and W7-7 say.
- The reasons recorded with the replacements that the dispositions quote or rely on are as stated: S318c (VC-5), D05 and S319 (VC-8), U17.5 and LT07.5 (C31, VN-3), U19.1–U19.5, U20.1–U20.2 and U23 with their LT counterparts, PM02.
- C31: the last sentence of C's M4 is on S20 Table's row 5; the record's disposition of M5 (b) has "the seven observations".
- "Murray et al. (2014)": the clause on the three works is that of 8bd189e; the report's first form listed it under "Not checked" for the reason given.
- The three kept: VN-7 agrees with the audit's check 4; VN-8: the article announces its public multiresolution release on p. 1 with the CBIG address and names 400, 600, 800 and 1,000 parcels as its resolutions, none of 100; `data/Schaefer2018_100Parcels_7Networks_order.lut` has 100 entries, `data/LICENSE-CBIG.md` is CBIG's notice, `LICENSE-CC-BY-4.0.md` (lines 24–27) records the file as copied from the folder of that release, and the sentence of Methods is that of 8bd189e; VN-10: p. 12 of Luppi et al. (2023) names the two validations without saying which redundancy function the one and which estimator the other used.
