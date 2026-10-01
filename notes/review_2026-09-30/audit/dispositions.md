# What was done with each finding of the audits of this revision

Five separate sessions of the AI system audited this revision before it was committed (record, "The audits of this
revision and its review folder"). `b26_rule_audit.md` audited B26's run against the rule of its pre-run entry, from the
evidence in `../b26/` and the 99 files the run changed or created, with `b15_null_replay.py` and its output. The other
three audited the prepared revision, applied in a copy of the repository to B26's outputs as the run wrote them: its
numbers, the exclusion statements, the numbers table and the word count (`findings_T.md`), the record's entries and the
bookkeeping (`findings_R.md`) and the corrections of the claim-by-claim check against the PDFs (`findings_Q.md`); their
line numbers are those of the build they audited. A fifth, `findings_S.md`, audited the revision as corrected after
them: the record's entries, this file, the folder and the other text changes. Each finding was checked against the files
and corrected in the revision before it was given to the writer's session, except where this list says otherwise. The
last section gives what was done with the findings of the fifth session of the claim-by-claim check
(`../claims/reviews/fifth_check.md`). The findings of the four sessions that checked the claim records before it
(`../claims/reviews/review_A.md` to `review_D.md`) were each read against the PDF and the records corrected where they
held; the records of `../claims/make_claims_check.py` are the result.

## b26_rule_audit.md

No fault: all six items pass. One slip: the report lists B19 among the steps with no counted matrices. B19 counts 8
itself, at line 149, in its part (b), the within-window regression, whose printed values did not change; its changed
lines and cells come from B4's pickle. The record's outcome entry gives both (rule (i)). The report's side note on the
current boot's start time (after its end in `boots.txt`) concerns the clock after the run and nothing the rule needs.

## findings_T.md

1. Applied: "+0.01153 − 0.00267 = +0.00886" (S3 Text §6); the values at full precision are in
   `../checks/conversions_b26.out`.
2. Applied: "+0.00404" and "−0.00109", with B24's expectation taken unrounded, +0.0000088.
3. Applied: S18 Table's source note names part (b) as B26's run regenerated it at d5a65bd, each mean over the pairs
   where its quantity exists (S3 Text §6); "byte for byte" stays with the files at a9d9ca4.
4. Applied: "rate but not the AR(1) generator's" in the Discussion (L02); the cut still takes the six words it took.
5. Applied: S3 Text §6 says that at W = 30 values of S12 Table move in their last digit, "among them" the two it names,
   and "the W = 60 pair-windows (four on each variant)"; the record's rule (iii) says which four move which number.
6. Applied: rule (iii) counts "except three" among the corrections of the claim-by-claim check (7 words net) and the
   cuts as 21 words (L01, L02, L04).
7. Applied by withdrawing the cut: the label "Inference:" stays in Methods, and the sentence keeps its verb.
8. Applied: Table 3's caption says that the last two rates are over the residual's pairs.
9. Applied: "all but the 4 of the 2,569,560 whose substituted matrix is not positive definite".
10. Applied: the sentence of Methods that replaces the definition states the exclusion and points to S3 Text §6, not
    back to Results 4.
11. Applied: `notes/review_2026-09-24/checks/derived_r17.py` was run again on B26's outputs
    (`../checks/derived_r17_b26.out`: −0.788 for −0.787, the same Fieller interval [−1.60, −0.08]; the bootstrap
    interval's upper bound, which the text does not quote, −0.26 for −0.25); the three rows of the numbers table cite
    it, and S19 Table and Data and code availability name it. The partial correlations of S3 Text §6 were recomputed
    (`../checks/partial_b26.py` and `.out`: +0.831, +0.855, and +0.687, +0.820 with `phyid`'s mask; at d5a65bd the
    script gives the third review's values exactly). The record's rule (ii) says so.
12. Applied: S3 Text §6 defines the residual as the observed sts averaged over the pairs minus the AR(1)-substituted sts
    averaged over the pairs where it exists (B24b).
13. Applied: the record names B01–B13, B20–B66, B24b and B57b.

## findings_R.md

1. Applied, and widened: the timing comment of `run_all.sh` now gives the step times of the final run from
   `results/run_all_final.log` for every line, sections 0–5 included, whose figures were also those of earlier logs
   (sections 0–5 ≈ 19,000 s, section 6 ≈ 9,540 s, B17 ≈ 44 min, B17b ≈ 34 min, B16 ≈ 21 min, B21–B24 about 9 min, 475
   min in all); it no longer says single-core, since B26's unit used about 32 h of CPU time in its 3 h 45 min
   (`../b26/unit_journal.txt`); the record's entry on the comment says so.
2. Applied: this folder holds the files under the names the texts give: `audit/b26_rule_audit.md` with its replay,
   `claims/make_claims_check.py` (the program given to V.S. as `make_claims_check_v2.py`, with the notes of item 17
   reworded), `claims/claims.csv`, generated from the program's records, and this file.
3. Applied: S5 Text §4 says that every table and report of the final run named c25a310 and that the outputs of sections
   0–5 still do, the nine files at 66b570e-dirty and `logdet_correction_check.csv` among them, those of section 6 naming
   d5a65bd since B26's run.
4. Applied: README.md's sentence as proposed, with the logs that print a commit kept.
5. Applied: README.md's row for `notes/` and CLAUDE.md's repository map name this folder.
6. Applied: CLAUDE.md says that the re-run reproduced every row of `binarised.csv` after the first line, which holds the
   time, byte for byte.
7. Applied: rule (i) says that B19's 8, in its part (b), changed no printed value, and puts its changed lines and cells
   with the steps that read B4's outputs; the rule audit's slip is noted above.
8. Applied: the record's paragraph on the evidence says that it was gathered on 30 September 2026 after the machine had
   been shut down and started again, that the unit was then no longer loaded, and what its journal shows.
9. Applied: rule (i) names B22's check line whose difference of 0 is now 2.22 × 10⁻¹⁶.
10. Applied: "the 99 files the run changed or created" in the record and "the 96 committed files whose bytes it changed"
    in S5 Text §4.
11. Applied: "the heartbeat found the charger disconnected from 11:09 to 12:29 UTC" (S5 Text §4).
12. Applied, with T5: "the W = 60 pair-windows, four on each variant", in the record and in S3 Text.
13. Applied: the entry's heading is "Fig 5's caption, B3's table header and `run_all.sh`'s timing comment".
14. Applied: "B25's outputs, the text and the review folder of 28 September 2026".
15. Applied, with T13.
16. Applied: the entry on B25's re-run says that the commit after the re-run holds B26's outputs only, so that the
    result is recorded one commit later, and that the logs differ also in the path of `phyid`.
17. Applied: in `claims/make_claims_check.py` the notes on S5 Text's sentences of 22 and 28 September (sentences 100 and
    102 of the check) say that the revision keeps them and adds a sentence after each.
18. Applied: S5 Text §6 says that B25's re-run was made at b36178d and that the figures and captions regenerated at the
    text commit are in the commit after it.
19. Applied: the record's headings read "«ENTRY_TIME» UTC", which the writer's session fills; the commit of B26's
    outputs and its date are filled in the replacements before they are given to it. The figure script's docstring keeps
    "30 Sep 2026", the day the change was made, as it dates its other revisions.
20. Applied: CLAUDE.md gives the statements' 14 words, the corrections' 7 and the 21 taken out.
21. Applied: the new lines of README.md and CLAUDE.md are wrapped; their longer lines that predate this round are left.
22. Applied: "(225 min in its run of 29 Sep 2026)".
23. Applied: "is in the function".

The two notes outside its scope: Table 1's TDMI row (−0.1037, −0.1130, +0.0092) is left as it is, each value rounded
from its own unrounded value (−0.103719, −0.112954, +0.009238), as everywhere in the tables; S3 Text's subtraction now
closes at its printed precision (T1).

## findings_Q.md

1. Applied: the parenthesis of Methods, Dataset keeps "by Singleton et al., 2025", so that S4 Text's D4 and A6 hold.
2. Applied, in fewer words: "four naming a Gaussian estimator" (Introduction); S20 Table, rows 6 and 8, gives the
   reasons Down et al. (2026) and Zhang et al. (2025) state.
3. Applied: S4 Text's reference to Nichols et al. (2017) says it was read in full, in its author manuscript, for the
   check of 29–30 September 2026, and S5 Text §5 says so.
4. Applied: S1 Text lists the structural connectome that the data check verifies (no result uses it), the two MATLAB
   scripts of the release read as text for the subject-order check, and each region's network as 1–7, and 8 for the 16
   subcortical regions.
5. Applied: under CCS a single-target redundancy is the expectation, under Ince's maximum-entropy distribution P̂, of
   the local co-information where the signs agree, and zero elsewhere; for two Gaussian sources P̂ is the fitted
   Gaussian, and here, as in `phyid`, the expectation is estimated by the average over the samples.
6. Applied: "A preprint by the same first author on anaesthetised brain dynamics"; "companion" is not said.
7. Applied: "one of the empirical fMRI studies of S20 Table uses CCS redundancy in its primary analysis".
8. Applied as proposed.
9. Applied: both headers say that the cells revised after the check of 29–30 September 2026 (rows 1, 5, 6 and 8 of Table
   A; Table B, item 3) take their page numbers from that check; the header of `notes/partB5_literature_v2.md` adds that
   the preprint was read in its version of 10 January 2026, which S20 Table states in Table B, item 3.
10. Applied: "Alexander-Bloch et al. (2018) in its NIH author manuscript" (S5 Text §5).
11. Applied: S1 Text names `data/Schaefer2018_100Parcels_7Networks_order.lut`, copied from the release of Schaefer et
    al. (2018), and the script that checks it against `sch116_to_yeo.csv`.
12. Applied in other words: Use of AI tools says "every cited paper" for "every cited work", which leaves out the
    software entry, whose code was read; the proposed words would have taken the counted text above 7,000.

(a) Applied: the record's reason reads as proposed. (b) Applied: the record's paragraph says that Ince's redundancy is
an expectation under his maximum-entropy distribution, which the average over the samples estimates; it gives, for Luppi
et al. (2025), the features that change alike in all 15 contrasts and the step to r₁ as ours; it names the corrections
Q01–Q31 and L05, with Q32–Q34, which this audit led to; and it says that S5 Text §5 records every cited paper read in
full, Nichols et al. (2017) among them.

## The fifth session of the claim-by-claim check (../claims/reviews/fifth_check.md)

It checked the six records that the files added on 30 September 2026 changed (sentences 27, 100, 104, 150 and 202 of the
check), and its specific checks (a)–(f) hold. Sentences 27 and 100 (Tian et al., 2020; Váša et al., 2018): verdicts
stand; as it suggested, the record's entry calls V.S.'s first copy of Tian et al. (2020) its authors' manuscript.
Sentence 104 (Váša et al., 2018): its four errors and three missing points are in the record (the rotation procedure is
Váša et al.'s, applied in the paper to its own 308 regions; the paper rotates one map; the release's function permutes
each map in turn, with permutations precomputed from rotations, and its comment says the copy is otherwise the same; the
regional test is the analogue of earlier vertex-level ones; `al857` and the function's dates); in the text, S5 Table
names the release's function (Q31) and the rotations are "by the method of Váša et al." (Q07, Q14, Q15). Sentence 150
(Luppi et al., 2025): its two errors and its missing points are in the record (one quotation; the version as its header
gives it; "companion" ours; the same source studies with the same numbers; HRF deconvolution; the step to r₁ ours;
whether version 1 has the six species), and in the text (Q25, Q29); Fig. 3a is not added to the record's passages, since
p. 5 states the fifteen contrasts. Sentence 202 (Luppi et al., 2025): verdict Q, as it found, and the text corrected as
it proposed (Q28: example time series from an awake and an anaesthetised macaque, their Fig. 3e); its missing points are
in the record (the fifteen contrasts of the six species; the human data published before, in the firsthand note).

## findings_S.md

1. Applied: the six files are in `../checks/`, made from the final tree, and the README names `figures_check.py` with
   its output. 2. Applied: `figures_check.py` compares the six figures the script writes and masks, with the PDFs'
   dates, the cross-reference table and its offset, which move with the dates' length; the record's entry says that the
   PDFs are to differ only in their creation dates. 3. Applied: `conversions_b26.py` prints the residual DiD, the
   expectation and the excess at ten decimals (+0.0088649893). 4. Applied: the al857 address is replaced in
   `../claims/reviews/fifth_check.md` and in this report's copy; the README says that the committer's address in
   `b26_commit.sh` is the repository's published contact address. 5. Applied: the two paths of `findings_R.md` are
   shortened. 6. Applied: "every commit an output gained is d5a65bd, none `-dirty`". 7. Applied: "logind's journal holds
   no lid, suspend or power-off event and the kernel's no out-of-memory kill or suspend while the run ran". 8. Applied:
   the record says that the unit's log is `positive_definite_run.log` with a last line, `=== unit exit 0`, which
   `evidence.txt` quotes, and the README says so. 9. Applied: "its four `diag_series` files". 10. Applied: "the range of
   B25's three runs, 482–514 s (514 s, 482 s and the re-run's 486 s)". 11. Applied: the disposition of Q9 above. 12.
   Applied: "sentences 27, 100, 104, 150 and 202 of the check", and "Sentence" in that paragraph. 13. Applied: each
   copy's first line lists its edits.

The optional note: applied. S19 Table, Part B, and Data and code availability name `../checks/derived_r17_b26.out`, the
output of `derived_r17.py` run again on B26's outputs (K18, K19).
