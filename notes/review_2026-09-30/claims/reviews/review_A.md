*Copy for the repository: quotations of the cited works longer than a few words are replaced by a description in square brackets with their page, as the passages themselves are not in the repository, and e-mail addresses by what they identify; paths of the planning session's scratch space are shortened to SP/.*

I checked all 83 records and found 19 problems. They are in `SP/b35/review_out_A.json`, each with the PDF pages that show the problem and exact replacement text.

**What held up:**
- Every evidence passage is on the page it names.
- Every other page, equation, section and appendix number I checked in use, why, note and first is correct (Barrett Eqs. 73/79–82; Varley Eqs. 3, 4–6, 11–12; Luppi 2024 Eq. 5; Luppi 2026 Eq. 9; Mediano 2021 Appendix VI and Definitions 1–2; Mediano 2025 SI Sec. III.A and Definition 2; Afyouni Eq. 8). The one exception is the Eq. 80 locator below.
- The two quotations, 'synergistic core' and 'synergistic workspace', match their sources.
- No field copies more than about eight words from a cited work, except near-verbatim in Theiler's first field (listed below).
- The nine Q verdicts the other session gave are sound.

**Findings:**
1. **4/8 Luppi 2023, verdict S → Q.** The paper also reports a 4-TR time step, where no significant difference was observed (p. 3), and says its results depend on the timescale (p. 8). The sentence gives only the 1-TR lag.
2. **5/10 Barrett, use.** The locator "Eqs. 80–82" for the MMI synergy is off: Eq. 80 is the one-lag redundancy; the synergy is in Eqs. 81–82.
3. **7/14 Barrett, use.** It leaves out the negative part of the sentence ("none of them gives the sixteen atoms…"). The use records it for the other works in that sentence.
4. **7/15 Kay & Ince, use.** Same omission as item 3.
5. **7/16 Varley, verdict S → Q.** His identity (Eqs. 11–12) holds only for a disintegrated pair, i.e. q = 0. The Introduction's unqualified "gave the aggregate identity" drops that restriction, which Results 1 states.
6. **14/31 Liardi, note.** The list of authors shared with the ΦID paper leaves out Bor.
7. **17/43 Tarchi, firsthand own → na.** The record's only element is that something is absent from the paper, which no page can state.
8. **21/49 Luppi 2022, use.** It carries "only", which this paper cannot support. That word rests on S20 Table's reading of the other studies. Luppi 2023, Luppi 2024, Tarchi and Luppi 2022 itself all used HRF-deconvolved signals, which Results 7 treats as a remedy.
9. **23/53 Mediano 2021, use.** It leaves out the joint-target nodes as single-target PIDs with a bivariate target (pp. 3, 23), which the note itself says the sentence claims.
10. **27/62 phyid, use.** It does not cover that calc_PhiID returns per-sample atoms (calculate.py lines 16–24 and 149–150), which the sentence's "local atoms" relies on.
11. **28/63 Afyouni, firsthand own → second.** Eq. 8 is Quenouille's estimator in its global form, which they review with citations to Fox (2005) and Van Dijk (2010) (p. 4). The sentence itself says "reviewed by".
12. **28/63 Afyouni, note.** "They derive it" overstates: they review it and note the ρ = 0 assumption.
13. **30/68 Mediano 2021, verdict S → Q.** The paper calls the quantity the local "multi-target co-information" (p. 24, Eq. 5); "double co-information" is the manuscript's own term.
14. **31/69 Mediano 2021, verdict S → Q.** "No sign constraint" is never stated, as the note itself concedes; the 2021 paper never says the atoms can be negative.
15. **32/70 Alexander-Bloch, note.** "Presents the method as its own" misses the paper's own credit to Vandekar (2015) and Gordon (2016) (p. 3).
16. **32/71 Váša, use.** "Released with the data" is not stated by Váša. Its only evidence is a data folder that is not among the sources; the repository scripts name the file but do not show where the rotations came from.
17. **33/72 Theiler, first.** "Their own algorithm" contradicts p. 5, which credits Osborne et al. [5] and refs. [15, 32]. The field also repeats about eight words of the source nearly verbatim. Consider firsthand "second".
18. **Claim 30, missing record for Mediano 2025 (SI Definition 2).** The locator is right. However, the SI (p. 4) says this extension computes CCS on p(x, y), without the maximum-entropy step of Ince's published 2017 version, so the missing record should be Q.
19. **Sentence after 18/44, missing record.** "That study's phase-randomised surrogates … their Table 1 …" attributes numbers to Luppi 2022 but has no record. The values check against Table 1 (p. 10): |ρ| ≤ 0.26 with one significant (GI, Pspin = 0.028), against 0.22–0.54 for the original gradient.

The only file I left is the output; my scratch folder (SP/b35/chkA) is deleted.
