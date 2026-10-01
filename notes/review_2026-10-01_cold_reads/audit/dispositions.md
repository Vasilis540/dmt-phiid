# What was done with each finding of the audit

Numbered as in `findings.md`. "Applied" means the file named in the finding was changed before the commit was made.

1. Applied: B28's docstring now says thirteen multiples of β̄ from 0.03 to 3.
2. Applied: B28's table now prints the 2.5th, 50th and 97.5th percentiles of the per-replicate ratio of means as well,
   and the ratio of the replicate-mean DiDs (the ratio its coverage column uses); the entry and the docstring name both.
3. Applied: B27's entry lists the group means of the r₁ pre and post gaps, derived from the committed rows, as known
   (item (ii)), and predictions (a) and (b) are restated to what is open: the p values, the intervals, the share of
   subjects, the adjusted contrast's interval and the correlations.
4. Applied: the cold-reads entry lists A's fourteen minor points as m1–m14 and its four wording points separately.
5. Applied: "Each report also states what it found right."
6. Applied: the band-limit bounds are named as Results 7's.
7. Applied: the README names S01 and S02.
8. Applied: the README says that the twelve text files carry the commit in their headers.
9. Applied: both entries now say "at this commit", as the scripts of the run require.
10. Applied: B16c's rule names `inference_rows_prewhiten_fixed.csv` for the exact p of a contrast.
11. Applied: B28's entry and docstring name `inference_rows_diag.pkl` among the files it reads.
12. Applied: B27 now checks the saved DiDs at W = 30 too (sts, r₁ and the residual on ts_gsr); the entry says so.
13. Applied: B28 clips the post β at 5, as B17b does; the entry says so.
14. Applied: both ratios are printed (item 2); prediction (a) compares the mean slope with the mean of the
    per-replicate ratios; the data's ratio of means is labelled per unit of whole-brain r₁ DiD, with the main text's
    −0.74 per unit of pair r₁ beside it.
15. Applied: the docstring names the pair-a DiD column and gives the floor as about 0.0375 below the pre level.
16. Applied in part: the entry's gloss of the string now says which terms carry a title-or-abstract tag, that the third
    tag is not a PubMed field tag and that PubMed's reading of the string (its search details) is to be recorded in the
    revision that follows the run; `search_string.txt` says the same. V.S. is asked for the search details.
17. Applied: the entry quotes the comment's "at least one".
18. Applied: B27's docstring says W = 30 on ts_gsr for all four quantities.
19. Applied: "as the sessions returned them, under a header that names the read".
20. Applied: CLAUDE.md's state paragraph says "whose findings that need a computation".
21. Applied: B27 now gives B21's inverted sign-flip intervals for the three means (the text's interval for a mean over
    subjects), with the t intervals kept for the regression coefficients; the entry's specification, its known values
    and its rule (i) name each interval for what it is.
22. Applied: B16c's docstring says that each whitened run keeps its finite TRs but the first p.
23. Applied in part: `run_all.sh`'s timing comment now says that the total does not include B25 or the four steps; the
    hour stays as the docstrings' estimate for V.S.'s machine.
