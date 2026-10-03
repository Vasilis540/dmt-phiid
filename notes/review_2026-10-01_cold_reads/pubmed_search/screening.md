# The PubMed search of 1 October 2026: screening of its 11 records

The paper's literature search (Methods, "Literature search") was by web searches of 14 September 2026 whose queries
were not recorded (cold reads A, m12, and C, m7, of 1 October 2026). V.S. ran the string of `search_string.txt` on
PubMed on 1 October 2026 and exported the 11 records to `pubmed_search.csv`. The inclusion criterion is the paper's:
published empirical fMRI ΦID studies reporting synergy, redundancy or quantities built on them (S20 Table lists the
nine found by the web searches, their main texts read in full). Each record is screened here from its title, abstract
and, where it is in S20 Table, the table's row; the two that were left on 1 October 2026 to be assessed from their
full texts were read in full that day (Pope et al., 2025: outside the criterion; Gao et al., 2026: in it, added to
S20 Table as its row 10), and the statement of the search in Methods is revised in the commit that records the
run's outcomes. A page given below is the page of the PDF as saved.

| PMID | record | screening |
|---|---|---|
| 33858199 | Gatica et al. 2021, *Brain Connect* 11(9):734 ("High-Order Interdependencies in the Aging Brain") | outside the criterion: O-information (a measure of higher-order interdependence), not ΦID |
| 40563806 | Zhang et al. 2025, *Brain Sci* 15(6):636 | in S20 Table (row 8) |
| 39022924 | Luppi et al. 2024, *eLife* 12:RP88173 | in S20 Table (row 3) |
| 36740030 | Luppi et al. 2023, *NeuroImage* 269:119926 | in S20 Table (row 2) |
| 37467265 | Varley et al. 2023, *PNAS* 120(30):e2300888120 ("Partial entropy decomposition reveals higher-order information structures in human brain activity") | outside the criterion: partial entropy decomposition, not ΦID |
| 41757079 | Down, Huntley, Mediano & Bor 2026, bioRxiv 10.64898/2026.02.18.706630 | in S20 Table (row 6) |
| 40843113 | Pope, Varley, Puxeddu, Faskowitz & Sporns 2025, *J Phys Complex* 6(1):015015 ("Time-varying synergy/redundancy dominance in the human cerebral cortex"; PMC12366633) | read in full: outside the criterion — its measure is the local O-information, the form resolved in time of the O-information, which the paper calls "a heuristic measure of redundancy/synergy dominance" (PDF p. 3, the article's p. 2, where the paper also names the local measure as the one it chooses; the section that derives it begins on PDF p. 5 and its formula is on PDF p. 6), on resting-state BOLD fMRI of 95 subjects; not a ΦID atom |
| 42287597 | Nago et al. 2026, *Brain Inform* 13(1):25 | in S20 Table (row 7) |
| 41913713 | Tarchi et al. 2026, *Brain Behav* 16(4):e71352 | in S20 Table (row 9) |
| 42113765 | Belloli et al. 2026, *PLoS One* 21(5):e0348005 ("THOI: An efficient and accessible library for computing higher-order interactions enhanced by batch-processing") | outside the criterion: a software library (O-information), not an empirical study |
| 42361709 | Gao et al. 2026, *Eur J Radiol* 203:113018 ("Mapping brain synergy dysfunction in heart failure patients with reduced and mildly reduced ejection fraction using multimodal neuroimaging: Functional and molecular insights") | read in full: in the criterion — Gaussian-MMI ΦID synergy and redundancy (synergy-to-synergy, redundancy-to-redundancy, τ = 1) on BOLD at TR 2 s, 246 regions, 48 patients with heart failure against 33 controls; added to S20 Table as its row 10, with its reading, and to the Introduction's count (ten studies); the claim record of the revision holds the pages |

Of the nine studies that S20 Table held before this search the string returns six; it does not return Luppi et al.
2022 (*Nat Neurosci*), Gatica et al. 2024 (*Network Neurosci*) or Luppi et al. 2026 (*Nat Hum Behav*), each found by
the web searches. With Gao et al. (2026), which the string returns, the table now holds ten.
