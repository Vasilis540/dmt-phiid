*Copy for the repository: quotations of the cited works longer than a few words are replaced by a description in square brackets with their page, as the passages themselves are not in the repository, and e-mail addresses by what they identify; paths of the planning session's scratch space are shortened to SP/.*

I checked all 78 records and found 11 problems. They are in `SP/b35/review_out_D.json`, each with the page or line that shows it and exact fix text. No existing file was changed, and the scratch copies I made while checking are deleted.

1. **Claim 66 / 131, Luppi et al. (2023), why:** "Among the empirical fMRI studies of S20 Table this is the only one" is false.
   - Down et al. (2026) re-checked their results with CCS in their supplement (Down2026.pdf p. 6), and S20 Table row 6 already says so.
   - Liardi et al. (2025), cited in the same sentence, also compare CCS with MMI (pp. 11–12).
   - The fix keeps the count point and limits "only one" to CCS as the primary analysis.
2. **Claim 31 / x67, Mediano et al. (2025), note:** it states as fact the SI's own account of Ince's preprint ("as in the original preprint…", "maximum-entropy projection").
   - Ince 2017 p. 13 says his earlier version also used a maximum-entropy distribution (his Definition 3).
   - S20 Table row 11 (audit F7) and S3 Text §2 also contradict it. The fix attributes the account to the SI.
3. **Claim 114 / x196, Raut et al. (2020):** two records share this claim, unit and work, with conflicting verdicts (S and Q). The Q record's why is accurate: PDF p. 2 is printed page 20891, and S20 Table otherwise uses PDF pages. Delete the S record.
4. **Claim 33 / 70, Alexander-Bloch et al. (2018):** firsthand should be "part", with a first. The paper says it builds on earlier rotation tests by Vandekar et al. (2015) and Gordon et al. (2016) (p. 3; Váša et al. 2018, p. 5, agrees). This is the same situation where Theiler et al. (1992) were given "part".
5. **Claim 57 / 107, Alexander-Bloch et al. (2018):** same problem and fix as item 4.
6. **Claim 104 / 185, Alexander-Bloch et al. (2018):** same problem and fix as item 4.
7. **Claim 143 / 225, Luppi et al. (2026), why:** it contrasts "the paper" (p. 35) with "its Reporting Summary" (p. 37), but both pages are in the Reporting Summary, which runs pp. 33–41. The article itself (p. 3) says only awake, deep sevoflurane anaesthesia and recovery.
8. **Claim 77 / 140, Luppi et al. (2023), note:** "checked under the sentence before" points to claim 76, which is about binarising each signal once. The emergence-capacity reading is recorded under claim 75, and only as our reading, not a check.
9. **Claim 156 / 238, Down et al. (2026), why:** "name no estimator or software in the main text" goes too far. The main text names fMRIPrep, Matlab, NumPy and the ENIGMA toolbox (pp. 3–4, 8); what it leaves unnamed is the estimator and the software for the ΦID computation.
10. **Claim 150 / x232, Luppi et al. (2025), verdict P, use:** the use gives only the quotation. It leaves out the other things the cell attributes to the preprint: that it covers the same four species and uses hctsa.
11. **Claim 76 / r43222023, Luppi et al. (2023), why:** it copies an eight-word phrase of p. 12 [on the plug-in estimator and the mean-binarised signals] without quotation marks. That is 8 words (10 counting hyphen parts), right at the limit; a paraphrase is given.

Everything else checked out against the page texts: page and equation numbers, the Table 1 values of Luppi et al. (2022), and every absence claim, which I checked by searching the full texts. The cited phyid lines hold what the records say, at the pinned commit 6c5f2e9. Records 48, 62 and 76 are correctly verdict P, since their PDFs (Váša's Supplementary Information, Luppi2025.pdf) are not available.
