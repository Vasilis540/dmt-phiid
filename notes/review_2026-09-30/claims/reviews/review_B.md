*Copy for the repository: quotations of the cited works longer than a few words are replaced by a description in square brackets with their page, as the passages themselves are not in the repository, and e-mail addresses by what they identify; paths of the planning session's scratch space are shortened to SP/.*

I checked all 102 records and found 19 problems; they are written to SP/b35/review_out_B.json with page references and proposed fixes. Most records hold up. Every evidence passage appears on its stated page (whitespace, punctuation and ligatures normalised). No quotation is wrong, and the use/why/note/first fields contain no copied passages apart from one borderline case (item 19).

**Wrong verdict or false statement**
1. **46/93 Barrett (2015), verdict S → Q.** Barrett derives the MMI rule for a univariate target only (p. 5, and pp. 2, 4, 12). He says the common PID does not extend to a multivariate target (p. 6). Two of the six single-target redundancies in the lattice have a bivariate target, so the sentence is broader than the work. The p. 12 evidence passage also stops just before Barrett's univariate qualifier. Main-text claim 29/65 in review A uses the same wording.
2. **47/95 Ince (2017), why.** "Two sentences later S3 Text shows…" is wrong. The Gaussian argument is the last sentence of S3 Text §2 (claim 53), thirteen sentences later.
3. **49/98 Mediano et al. (2021), note.** The note says the 9 + 6 split of lattice nodes is our own count. Mediano et al. state that split themselves in their Appendix II (p. 23).
4. **74/142 Nichols et al. (2017), verdict S → Q.** Our sentence says the report is "summarised in" Nichols et al., but they call their article a Commentary (p. 2). The section list and the checklist items come from the COBIDAS report itself.
5. **74/142 Nichols et al. (2017), note.** The note says the article gives the seven domains and the checklists. It only names the range the domains span and mentions the checklists without giving them (p. 3).

**Citations with no record (checked here; all are supported)**
6. **69/135.** No record covers Luppi et al. (2022) in this sentence, including the quotation 'had negligible effects on synergy and redundancy calculations'. The quotation is exact on p. 16; the replication without deconvolution is on p. 3.
7. **48/96.** The "2025, SI Appendix, Definition 2" half of the citation has no record. I propose Q: the SI writes the full mutual information as I(X; Y), not i(x; y) (p. 4).
8. **49/98.** The "2025, SI Appendix, Eq. 6" half has no record. It is supported (pp. 2–3).
9. **68/134.** Three later sentences in the same paragraph attribute content to Luppi et al. (2022) as "Its authors" or "that study", without an author–year citation, so none has a record. All three are supported (pp. 10, 18).
10. **71/138.** A later sentence says "Luppi et al. binarise each signal once" with no year and no record. That the signal is binarised once is our reading; the papers only say "mean-binarised" signals. I propose Q.

**Use fields that leave out part of the sentence**
11. **67/133 Luppi et al. (2022).** The use omits the four significant associations at 0.40–0.54, the description of the glycolytic index as a PET measure, and ρ = 0.26 with spin p = 0.028. All are supported by Table 1 (p. 10).
12. **43/88 Luppi et al. (2024).** The use omits what the sentence says the account holds: loss of consciousness goes with reduced ΦR in the workspace (pp. 1, 8).
13. **41/86 phyid.** "Sixteen local atoms per time point" is covered by neither the use nor the cited code lines. The code supports it (utils.py lines 4–9; calculate.py lines 122–150).

**Minor points**
14. **70/136 Luppi et al. (2022).** "Their pp. 3, 14" are positions in the PDF. The journal's printed pages are 771–782, so the first passage is on printed p. 773, and p. 14 is in the online Methods.
15. **65/131 Luppi et al. (2023).** "In one study used CCS" could be read as a count. The ΦID paper itself used CCS in all its examples (Mediano et al., 2021, pp. 10, 12), so I propose a note or a rewording.
16. **85/154 Timmermann et al. (2023), A4.** The only statement that T1 images were acquired cites ref. 71, C. Timmermann's PhD thesis on the same study. "Own" can stand, but the first field should say so.
17. **87/157 Singleton et al. (2025), note.** The list of version numbers is incomplete: it leaves out the scanner software (syngo MR B17). Their ANTs reference is also titled "…: V1.0"; that is the cited paper's title, not the version run.
18. **97/180 Theiler et al. (1992), why.** "Supports both sentences that cite it" is inaccurate: four sentences cite the paper, and only two cite it for its content.
19. **42/87 Theiler et al. (1992), copying (borderline).** The first field repeats about eight words of Theiler's credit sentence plus the reference numbers.

**For the memory pass:** nothing new about the user came up in this task.
