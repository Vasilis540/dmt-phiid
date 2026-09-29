# What was done with each finding of the audits of the prepared revision

The first three reports in this folder audited the revision as first prepared (the build the reports call `treeA_v1`;
their line numbers are that build's): `findings_text.md` the text edits and the record's entries, `findings_b25.md`
B25's script, its pre-run entry and `b25_fill.py`, and `findings_ci.md` the repository tool, the tests, the workflow and
the licences. Each finding was checked against the files and then corrected in the prepared revision before it was given
to the writer's session, except where this list says otherwise. The fourth report, `findings_b26code.md`, audited the
correction of the code that the third led to, B26's script and the draft of B26's pre-run entry (its entry numbers
F01–F30 are those of that draft; the correction as committed has F01–F52, in the order of the files). The corrected
revision was then audited again, in a second round (the record's entry, item 10): `findings2_text.md`, of the text, the
entries and B26's preview, and `findings2_code.md`, of the correction, B26's script, the scripts that start its run and
collect its evidence, and the planning session's scripts that package the revision and check the writer's commits; their
line numbers are those of the build they audited. The revision corrected after them was audited a third time, by two
sessions again: `findings3_text.md`, of the text, the entries and the preview, and `findings3_code.md`, of B26's script,
`checks/b26_changes.py`, the new reads, the scripts that start the run and collect its evidence, and the planning
session's scripts. A fourth round, by two sessions, verified the third's corrections: `findings4_text.md` and
`findings4_code.md`. A fifth, by two sessions again, verified the fourth's: `findings5_text.md` and `findings5_code.md`.
The dispositions of each round follow those of the round before; where a later correction changed what an earlier
disposition said, the earlier one gives the state of this commit.

## findings_text.md

1. Table B item 1 and record item 5 gave Luppi et al. (2023)'s MMI emergence capacity as a function of r₁ alone, which
   holds for the Gaussian estimator only. Corrected: "which with the Gaussian estimator is also the MMI emergence
   capacity of Luppi et al. (2023) (row 2)", in S20 Table and `notes/partB5_literature_v2.md`; item 5 likewise. The
   side point: the sentence now names where the identity is checked (`tests/test_closed_form.py`), so that it is not
   read as part of the 2,000-draw check before it.
2. B25's pre-run entry misstated the address Luppi et al. (2023) print. Corrected: the entry names
   github.com/robince/partial-info-decomp as "the repository Luppi et al. (2023, p. 12) print and link".
3. The licence covered the manuscript, whose first line forbids its distribution. Corrected: the manuscript is left
   out of the licence until its preprint ("a draft for co-author review, not yet licensed"), in
   `LICENSE-CC-BY-4.0.md`, Data and code availability, `README.md`, `CLAUDE.md` and `CITATION.cff`; the file of parcel
   names copied from CBIG is listed as third-party material with CBIG's MIT notice (`data/LICENSE-CBIG.md`).
   `CITATION.cff` keeps `license: MIT` (the Citation File Format reads a list of licences as alternatives) and says in
   its abstract which files CC BY 4.0 covers.
4. S20 Table row 3 and record item 5 took the workspace's synergy to be Eq. 5's. Corrected: row 3 gives both readings
   (as Eq. 5 writes it, S; as the persistent synergy sts, 2S − C, which depends on q as well); item 5 says that Eq. 5
   is how Luppi et al. (2024) write the synergy they call persistent.
5. The passage check was said to be by a script written apart from every copier, which is false for 120 passages.
   Corrected in S5 Text §5, record item 1 and the folder's README: 639 passages copied by the seven group sessions,
   120 by the planning session, which also wrote the checking script.
6. `CLAUDE.md` said B25 was applied and pointed to an S3 Text §11 not yet written; `README.md` said the [TK] marks left
   were the co-author items only. Corrected: the state line, the history line, a Round 21 item and the remaining work
   in `CLAUDE.md`; the [TK] sentence in `README.md` names the archive's DOI.
7. The numbers table: two rows of the rewritten Results 1 paragraph out of reading order, and the row of "+0.05"
   pointing at the line of c = −0.05. Corrected: the paragraph's rows put in reading order; the row of "+0.05" made a
   derived row (the coupling at which sts is lowest among the rows with c > 0, from lines 12–14 of
   `coupling_map_tables.md`). The two faults the report's notes found that predate the revision were corrected too:
   the note of the second "1" of Introduction paragraph 2 ("lag-1: a name") and the context of the seed row of Data and
   code availability, which ran past its paragraph.
8. S5 Text §6 used the planning's term "the readiness items" and a label the supporting information does not yet
   define. Corrected: the items are named (the licences, the citation file, the diagnostic tool, the tests and the
   continuous-integration workflow) and B25 and B26 are glossed; `b25_fill.py`'s strings follow.
9. Record item 3 miscounted what S4 Text named and overstated what pandas writes. Corrected: "S1 Text's software line
   named four of these and S4 Text's item S8 five"; pandas "builds, reads and writes the tables of the review and Part
   B computations under `notes/review_results/`"; joblib 1.6.0, which the deconvolution imports, is added to S1 and S4
   Text and to the record.
10. Record item 7 left out the unpartialled map's spin p. Corrected.
11. Record item 1 and the README described the normalisation and the outside sources inexactly. Corrected: white space
    is among the normalisations; the 33 passages that do not come from a PDF of the cited work are described by their
    kinds of source.
12. Record item 9 put the outputs of the tests and the self-test in `checks/`, where they were not. Corrected: `checks/`
    now holds `pytest.out`, `doctest.out`, `b25_selftest.out` and `b26_selftest.out`.
13. B25's entry cited the main text for 0.1957, which the main text prints as 0.196. Corrected: "S3 Text §4, B22 (d);
    0.196 in the main text, Results 1".
14. "`tests/` checks it and the closed form against phyid and `notes/rev_phiid_fast.py`" was true of the tool only.
    Corrected in Data and code availability, the record, the README and the workflow's comment: the tool against phyid
    and `notes/rev_phiid_fast.py`, the closed form against the tool's lattice solve.
15. `b25_fill.py` would have stated that a separate session reproduced every value before that re-run exists.
    Corrected: the fill states no result of the re-run and names it only as still to be made; the outcome entry it
    writes says that the commit that follows the re-run records its result.
16. Bookkeeping: `run_all.sh`'s "minutes" for B25 now reads "about 15–30 min, an estimate" (first 10–15; see
    `findings2_text.md` 22); the README says that
    `text_replacements_2026-09-28_b25.json` is written when the fill runs. The record's entries carry «ENTRY_TIME» in
    `text_replacements_2026-09-28.json`: unchanged, because the file is what was applied, and the writer's session puts
    the date and time into the record afterwards; the README says so.

Notes of the report. P12/P13's "(Fig. 3e)" was read in version 2 of the preprint of Luppi et al. (2025), whose
quotations S20 Table's note records as checked against version 1: P13 is applied without the figure number (record,
item 2).

## findings_b25.md

1. A failed check on a quantity that carries no prediction (the CCS quantities, which jump wherever a sign mask
   changes) could have stopped the report. Corrected: the rate check and the comparison with phyid at 10⁵ samples are
   checks for the quantities that are smooth on the family (MMI-sts, its emergence capacity, 2A, TDMI, MMI's rtr) and
   reported for the four CCS quantities; the rate at step 10⁻³ is written beside the rate at 10⁻⁴ for every quantity,
   and a rate whose two steps differ by more than 1 % is reported as not defined on the 10⁻³ scale; the fill quotes
   the rates of Luppi et al. (2023)'s emergence capacity only where the two steps agree; the entry's rule says which
   checks can stop the fill.
2. The fill stated a re-run before it existed. Corrected (as findings_text.md 15).
3. The entry misstated the address. Corrected (as findings_text.md 2).
4. `binarised.csv` carried no commit. Corrected: its first line gives the commit and the time of the run, and the
   tables' header gives its sha256, which the fill recomputes before it writes anything.
5. An ungrammatical sentence in one branch of the fill. Corrected: "and so does its emergence capacity" only where both
   rise or both fall at every step.
6. The maximum-entropy fit stopped silently at its iteration limit. Corrected: after 2,000 sweeps without reaching the
   tolerance, the fit restarts from the uniform distribution on the solution's support (the cells some distribution
   with the three marginals makes positive, one linear programme per cell), where it converges in a few sweeps; the
   number of fits, those from the support and the largest marginal error are reported, and that error is a check
   (≤ 10⁻¹²). The self-test: 54 fits, 5 from the support, largest error 1.0 × 10⁻¹⁵.
7. Dates were fixed in the templates. Corrected: the run's date and time are written in its outputs; the fill reads
   them, dates its outcome entry by the clock (or `--now`), and takes the pre-run entry's date and time from its
   heading; the entries' headings take the date and the time at the commit, and the texts refer to the entries by
   name.
8. "Seven further entries" miscounted. Corrected: "Six further entries … (B18), and B25 recorded none for its CCS
   quantities (row B25 (d))".
9. The inserted sentence in S20 Table row 2 took the referent of "inside it". Corrected: "inside the map".
10. The per-SD ratio at one decimal, and a negative ratio. Corrected: two decimals; where ∂(MMI-sts)/∂r₁ is not
    positive the text says that the per-SD comparison does not arise.
11. Two statements of the entry did not match their sources. Corrected: 0.1957's source; "to the four decimals of his
    toolbox's `examples2d_output.txt`, the twelve decompositions it prints, seven of which Ince (2017, Tables 6, 8–11
    and 13) also publishes".
12. What the texts attributed to Luppi et al. (2023) beyond the paper. Corrected: the joint future as one target is
    "our reading"; the binarisation of each lagged series at its own mean, against the paper's once per signal, is
    stated with its order, O(1/T).
13. A latent NaN in the self-informations of a table with an empty cell. Corrected (the `keep` mask).
14. The fill crashed if the entry's time was not filled. Corrected: it stops with "NOTHING WRITTEN".
Minor wording: "one generator" (the Genz check seeds its own), "computed exactly" (by numerical quadrature to about
10⁻¹³), the derivation's "in the long-series limit, for 0 < q < 1, where B < A settles every MMI selection", and the
CHECK FAILED message: all corrected.

## findings_ci.md

1. The tool raised for a whole call when one pair's AR(1)-substituted matrix was not positive definite; the paper's
   code returns a value computed from |det| there. Corrected in the tool: a matrix that is not finite and positive
   definite (smallest eigenvalue ≤ 0) has no atoms and gives NaN; the module, `ar1_corr`, `diagnose`, the README and
   Data and code availability say so; new tests check the NaN against the analytic condition on 20,000 draws and on a
   pair sharing a slow signal. In the paper's own code the finding is a fault: `rev_phiid_fast` gave such matrices
   atoms, and they entered the means (on the family, B5's check with unequal coefficients reported values from 171
   such matrices). Corrected in the same commit: `rev_phiid_fast.atoms_from_corr` returns NaN for them, and every
   computation that averages substituted atoms takes its means over the matrices where they exist, by one rule (the
   record, "The matrices that are not positive definite (B26): pre-run entry"). The steps without data were re-run
   with the corrected code by the planning session (`checks/b26_preview.md`); B26 (`notes/partB26_positive_definite.py`)
   runs section 6 of `run_all.sh` on the data with it, counting such matrices per step and calling line, under a rule
   fixed before the run.
2. Too-short inputs passed the guard. Corrected: at least five lag pairs; `diagnose_pairs` validates its input.
3. The licence and the manuscript's first line. Corrected (as findings_text.md 3).
4. The licence's scope. Corrected: `data/LICENSE-CBIG.md` is CBIG's `LICENSE.md` copied unchanged (from
   github.com/ThomasYeoLab/CBIG at 35b5664, whose `.lut` file is byte-identical to the repository's); the README has a
   row for the file; CC BY 4.0 covers `README.md`, `CLAUDE.md`, `CITATION.cff`, the files under `notes/` that are not
   code, and the result files; MIT covers the `.py` and `.sh` files, `requirements.lock.txt`, `.gitignore` and the
   workflow; quotations of other works are named as not covered.
5. The doctest held for one random stream only. Corrected: seed 20261120 and assertions with margins (|sts − 1.2588|
   < 0.03, |residual| < 0.01); an example of the NaN added.
6. `diagnose_windows` accepted series of different lengths. Corrected.
7. NaN and constant inputs. Documented in the module's docstring and the README.
8. `importorskip` could skip the comparisons silently. Corrected: `rev_phiid_fast` and `phyid` are imported at the top
   of the test module.
9. A tautological test. Replaced by a test of the substituted estimate as `notes/partB4_diagnostic.py` computes it,
   through `rev_phiid_fast.PairPhiID`, with NaN exactly where the substituted matrix is not positive definite.
10. A shared generator. Corrected: one generator per test; run with 400 other base seeds, no test failed.
11. The sign-change bracket did not pin 0.008. Corrected: excess(0.0075) > 0 > excess(0.008), with S18 Table's grid
    named.
12. The tests' wording in the manuscript. Corrected (as findings_text.md 14).
13. "Two AR(1) processes correlated only at lag 0" is false: they are correlated at every lag (Results 1 gives
    corr(x_t, y_{t+1}) = aq). Corrected in the tool, the README and `CITATION.cff` ("with no lagged interaction"), and
    in the paper, which had the same shorthand in the Abstract, the Introduction, Fig 1's caption (with the figure
    script and `captions_v2.md`) and the Discussion: "coupled only at lag 0".
Observations. O1: the workflow now pins pytest, setuptools 84.0.0 and versioneer 0.29 and builds phyid without build
isolation; an OSF outage fails phyid's step, which the workflow's comment says. O2: the actions' major versions are
kept. O3: `CITATION.cff` gets its version and date at the release. O4: the licence field of the Zenodo record of the
data release could not be read on 28 September 2026 (the page was refused); Data and code availability now says that
the repository carries no licence of its own at 77af7aa, which was checked, and V.S. is asked to read the Zenodo
record's licence field. O5: the record's expected sha256 is taken with the entries' time masked, by design. O6:
nothing to do.

## findings_b26code.md

1. The draft entry's sentence on B23 was wrong: 109 of B23's failing matrices are the AR(1)-substituted matrices of
   the simulated windows (line 200), not matrices with deviations added, and the substituted sts, the residual, D and
   the ratio change. Corrected: the entry gives the three sets and says which columns change; the numbers come from
   the preview (`checks/b26_preview.md`).
2. Values quoted by scripts from other outputs could go stale. `partB14_family_atoms.py` and
   `partB15_directed_crosslag.py` now read the diagnostic's W = 60 residual from `diag_tables.md` (which B4 writes
   before them in section 6), B15 quotes its own run-level residual, and the null's log reads the data's residual
   shares from `diag_tables.md` and the residual's changes, DiD and interval from `inference_rows_diag.csv`; on
   d108d66's outputs they print exactly the strings they held. B21's three expectations (+0.0027, +0.0049, +0.0054)
   and `15_figures_v2.py`'s look-up of them are data-free: the corrected B17 gives (i) W60 residual DiD +0.0049 ±
   0.0017, as before (0.0049320 against 0.0048988), the corrected B17b +0.0027 ± 0.0014, as before (0.0026692 against
   0.0026686), and the null's DiD is +0.0054 as before (the preview), so they stand.
3. B4's lines for subject 1 did not follow the rule. Corrected: the observed mean and SD over all pairs, the
   substituted mean and SD over the pairs where it exists, the residual as their difference, its SD and the
   correlations over the pairs where both exist, and the number of pairs without the estimate in brackets.
4. The counts could not be read per site. Corrected: a site is the calling line and column, with up to two frames of
   the repository that led to it, so that two calls on one line, a helper's callers, and the evaluations inside a root
   search and the final one are told apart; the tables say that a data window evaluated by several steps is counted in
   each and that the number the text quotes is B4's, which B4 now prints on each level line; the null's final
   evaluations are counted by `checks/b26_null_sections.py`.
5. Rule (iv) could not be carried out under the wrappers. Corrected: a failed step is re-run under the same wrappers,
   on the tree the full run left, its rows replaced in the CSV and the tables (first `--only STEP …`; after the second
   round, `--from STEP`, which re-runs that step and every later one: `findings2_code.md` 2 and 5; tested).
6. A step's `sys.exit("message")` was swallowed in `--child`. Corrected: the step's SystemExit or exception passes
   through, with its message or traceback, as when run directly (the self-test checks it).
7. The counts could be lost at the end. Corrected: the CSV is written first and the tables are made from it; a missing
   value is written empty and formatted as such; the child's output is decoded with replacement.
8. The note added to B23's table would have moved every later line of `diagnostic_alternatives_tables.md`, which the
   numbers table locates by line. Corrected: the note is at the end of the line that describes the table; no edit adds
   a line to an output that the numbers table locates by line (B4's count is on its level lines).
9. B23's D did not follow rule (3). Corrected: D is taken where the pair-window's four matrices are positive definite.
10. B23's displayed numbers no longer added up. The note on the table now says that a number in brackets counts the
    pairs left out of that mean, that the column "pairs excluded" counts those left out of every quantity, and that the
    last column divides the residual's change by r₁'s over the residual's pairs; the entry says that B23's residual is
    taken per pair (rule (4)). The CSV records no counts; the tables and B26's CSV do.
11. Some edits differ from the old code in the last bit of a mean. The entry now says so (below 10⁻¹⁵), and rule (i)
    lists the lines the correction rewords as expected differences.
12. Two sentences of B15's and B22's outputs now name the pairs over which the residual and the responses are taken.
13. The tables now list sites with non-finite matrices too, in their own column; the entry's rule (v) says what is done
    if a sample matrix (PairPhiID) is reported not positive definite.
14. The CI workflow, the tool and the JSON are in the revision's commit; the entry now says that the sts before B26 is
    recorded for the matrices that pass through `atoms_from_corr`.
15. F23 (now the entry that adds `nleft`) was not idempotent. Corrected: its old string spans the line that follows,
    which the replacement changes.
16. F19 (B17b's population reference) is correct; the entry now states the paired choice and why the shifted matrix
    cannot fail.
17. B21's check against the log of 17 September 2026: the entry anticipates it. The comparison's listing: rule (i) now
    requires the listing of `checks/b26_changes.py`, which the evidence script runs (after the second round; first the
    full diff): every changed line and cell in full, and for each changed array and image what `findings3_text.md` 7's
    disposition says.
18. B25 reads no output of section 6 (checked) and parses no B23 cell. The scripts outside `run_all.sh` that call
    `atoms_from_corr` (the checks of 16 and 22 September 2026, also `winsim.py`, `winsim2.py` and `popresid.py`) are
    named in the entry as records of their time, not re-run; the text quotes none of their results (checked).
19. The trailing spaces are gone; the expansion of the deconvolution loop is kept (it is run_all.sh's, and the runner
    reads the loop's structure from it).

## findings2_text.md

1. B23's section of the preview listed a draft's change to its table. Corrected: the preview was made again from a
   clone carrying the final code (75a7dd0), which it names; its B23 section lists the note appended to line 102, and no
   line added.
2. The entry's counts were those of the `atoms_from_corr` path where it named the preview's totals. Corrected: B23's
   172 of the 4,336,546 matrices it evaluates (4,336,530 through `atoms_from_corr`, 16 sample matrices), B24's
   17,640,000 (12,264,000 through `atoms_from_corr`); the preview gives every step's counts by path and by calling line;
   the null's counts per section are cited to `checks/b26_null_sections.out`, its root searches' to the wrappers'
   count.
3. The preview had no list of the numbers whose source changed. Corrected: its section 2 lists the main text's 24 rows
   whose held strings the corrected outputs no longer hold, with the value each gives at its printed precision (11
   change), the tables of the supporting information that transcribe a changed row (S10 Table and S3 Text §7, B17's and
   B17b's rows, which the audit's list did not have; S18 Table, B23's) and eighteen quotations with the text they become
   (S3 Text l. 241 (four), 276–280, 347 and 349; `supplementary.md` l. 339, 1417, 1597, 1599, 1623 and 1673;
   `notes/partB5_literature_v2.md` l. 27; three of them added in the third round, `findings3_text.md` 1, and five in the
   fourth, `findings4_text.md` 1), B23's verdicts read again by their criteria, and the captions that the corrected
   outputs make inexact (`findings3_text.md` 20).
4. B21's expectations were held, not read. Corrected in the entry, which names them and `15_figures_v2.py`'s look-up of
   them as held; the preview shows the corrected steps reproducing them (0.0026692, 0.0049320, +0.0054), and the
   evidence script compares them with the regenerated outputs after the run.
5. Nothing in the tree listed every changed line and cell in full. Corrected: `checks/b26_changes.py`, committed with
   the entry, lists every changed line and cell in full, and for each changed array the number of entries that changed,
   the largest change and the first 2,000 entries, for each image the pixels that differ (the evidence holds the files
   themselves; `findings3_text.md` 7); rule (i) names it, the evidence script runs it, and the preview's listings are
   its output.
6. F01–F30. Corrected: F01–F52 in the review folder's README and the preview.
7. The second round was named but absent. Corrected: its two reports are in this folder with these dispositions, as
   are the third round's; item 10 of the revision's entry describes the rounds; item 11's hashes are computed by the
   build from the final files.
8. B25's entry said that the fill says nothing of the re-run. Corrected in the entry, in `b25_fill.py`'s docstring and
   in this file (`findings_text.md` 15): the fill states no result of the re-run and names it only as still to be made.
9. Rule (iii) would have lengthened Methods, which is at the word limit. Corrected: S3 Text states the rule, at the
   start of §6, on the residual of the substituted estimate (`findings3_text.md` 17), with B4's numbers; the main text
   changes only where the pair-windows left out change one of its numbers at its printed precision, within the 7,000
   words, the outcome entry naming the words taken out for it.
10. The root searches' 11 were cited to the wrong source. Corrected: the entry cites the wrappers' count, 126 of the
    10,010,000 substituted matrices, for them, and `checks/b26_null_sections.out` for the sections.
11. The runner's docstring said that a matrix counted at a site is left out of what it feeds, which is false for the
    PairPhiID and "other" paths, and the steps that evaluate the same windows omitted `partB4_residual_source.py`.
    Corrected in the docstring and the entry: those paths are not corrected and are reported; the list names B4's
    residual source.
12. The tables were not both written from the CSV, and did not say that the number the text quotes is B4's. Corrected:
    the CSV carries the examples and the calls that held the matrices, the tables are made from the CSV alone, and they
    say that the number of the data's pair-windows without a substituted estimate is `partB4_diagnostic.py`'s.
13. The "last bit" claim holds only on the machine that wrote the committed outputs. Corrected in the entry, which also
    names the float noise on another machine; the preview states its tolerance once, at its top.
14. The preview said the second clone's code was this commit's byte for byte, and cited the kit's script. Corrected:
    it states which files are identical, how the second clone's `review_v2_residual_null.py` differs (`data_refs` and
    the script's `__main__` block, which B24 and B17b do not execute), that its wrappers were an earlier version counting
    the same matrices, and that B24 read B17b's committed tables, whose generator parameters and (i) row the corrected
    B17b prints unchanged; it cites `checks/b26_changes.py`.
15. "They are unchanged": corrected to "their calls are unchanged"; the entry names `tests/test_ar1_diagnostic.py`.
16. P13 was also reworded. Corrected: item 2 names the rewording ("in the caption of") as well as the figure number, and
    that P11 removes the blank line before the reference entry.
17. Item 3's "each as the paper states it". Corrected: the excess at 0.006 and 0.008 is "consistent with the change of
    sign at 0.008 that the paper states".
18. "Every package pinned". Corrected in item 4 and in the workflow's comment: NumPy, SciPy, pytest, `phyid` and its
    build backend are pinned; pip and pytest's own dependencies are not, and Python is the latest 3.12.
19. CLAUDE.md's "three sessions audited the prepared round". Corrected: it gives the audits and their rounds (twelve
    audits in five rounds, after the fifth) and points to this file for what was done with each finding
    (`findings3_text.md` 22).
20. N12's `why` said two entries; the K ids skipped K20. Corrected: the N entries name the record's three entries; the
    K ids run K01–K23 (K13, added in the third round, makes CLAUDE.md's range of computation labels B1–B26).
21. B25's entry against the script. Corrected: "not differentiable on the 10⁻³ scale", with the criterion "1 % (+ 10⁻⁶)";
    the checks that can stop the fill include the binarised pair information 1 − H₂(arccos(r₁)/π); what the fill
    writes names S3 Text's caption, the labels B1–B25 of S3 Text and S19 Table, and Data and code availability's list
    of the computations.
22. B25's run time. Corrected to about 15–30 minutes in its docstring, `run_all.sh` and the writer's prompt: the
    planning session timed the per-replicate work on a random stable VAR(1) pair at the three lengths (no point of the
    family evaluated); the docstring gives a bound, under 25 ms per replicate, and says that --selftest times one at the
    longest length (`findings3_text.md` 10).
23. The S3 Text §11 template cited S20 Table's row 1 for Luppi et al. (2022)'s binarised replication. Corrected: "(their
    pp. 3, 14)", and for Luppi et al. (2023) "(their p. 12; S20 Table, row 2)".
24. S1 and S4 Text on joblib and rsHRF. Corrected (D02, D03): joblib 1.6.0 among the packages the lock file pins;
    rsHRF 1.7.0 for the deconvolution (S2 Text), which the lock file does not hold.
25. S4 Text's "its parameters". Corrected (E11): "their acquisition parameters are not reported".
26. Main-text wording, corrected without lengthening Introduction through Methods (two words fewer): Luppi et al. (2024)
    named before "they call" (E09); "at each value computed up to +0.10, most at +0.05" (C01, the build's check of the
    derived row changed with it); "these data have no ground truth" (C03, as the third round shortened it,
    `findings3_text.md` 23); "addressed autocorrelation (in part); it is the subject of Varley (2024)" (E10); "the
    release's repository" (P48).
27. The null's last line named `residual_source.log`. Corrected: "data (inference_rows_diag.csv)".
28. The README did not say that the committed outputs predate the correction. Corrected: it says so, and what a run
    before B26's writes differently.
29. Advisory. The crosscheck CSV's notes are now in the third person ("Not among V.S.'s PDFs"; nine rows);
    `LICENSE-CC-BY-4.0.md` now says that the result files are computed from the data, some per subject, run, region or
    pair, and that the licence grants no right in the data, whose use rests on the agreement described in the README.

## findings2_code.md

1. The start script would not have started the run: it looked for ", 0 failed" where the self-test prints "; 0
   failed". Corrected.
2. A re-run of a step after the full run would always have been refused: `rev_assemble.py`, a step of section 6,
   rewrites `notes/review_computations_2026-09-14.md`, outside the output folders. Corrected: the file is exempt from
   the check of `--from`, and the evidence script treats it as an output (tested on a reduced section 6 that includes
   `rev_assemble.py`).
3. `check32.py` required every file mode to be 100644, which `run_all.sh` (100755) is not. Corrected: the modes of the
   files A and B change are compared with those before, new files 100644.
4. `check32.py`'s re-run of B25 could not import NumPy (a symlinked interpreter outside its environment). Corrected: the
   re-run uses the pinned environment's python directly, and a re-run that writes no outputs stops the check before they
   are read.
5. A re-run of the failed step alone would have left the later steps on its stale outputs. Corrected: `--from STEP`
   re-runs that step and every later one; rule (iv) says so.
6. The evidence could not support rule (i) for the binary outputs, and the counts were per site, not per call.
   Corrected: the evidence carries every output the run changed or wrote, binaries and figures included, and
   `b26_changes.py`'s listing of each changed array (the number of entries that changed, the largest change and the
   first 2,000 entries with their indices); the runner records per site the number of the calls that held matrices
   that are not positive definite or not finite and the ordinal of each with its number of them (every one since the
   third round, `findings3_code.md` 3), from which a step's loop order gives each one's window.
7. `rev_assemble.py`'s file tripped the evidence script. Corrected: exempt from "nothing changed outside the output
   folders" and included in the diffs, the listing, the sha256 list and the copy of the outputs.
8. The chain could include frames of `.venv` on V.S.'s machine. Corrected: frames under the repository's `.venv` are
   left out.
9. 15 of the 20 examples per site were lost. Corrected: the CSV has an `examples` column, read back by `--from`, and the
   tables are made from the CSV alone.
10. `old_sts` could print a RuntimeWarning into a step's log. Corrected: it runs under `np.errstate(all="ignore")`.
11. A failed read was silent in B14 and B15 and would have stopped the null. Corrected: B14 and B15 print "CHECK FAILED
    (not read)" in its place, where the value is not found and, since the third round, where the file cannot be read
    (`findings3_code.md` 7), and the null's `data_refs` catches a failed read and prints CHECK FAILED in the log's
    line, so that the null's log is written and the figure script reads it.
12. B21's table (a) can lose a line if a quoted interval changes. Corrected: rule (ii) says that the numbers table's
    locators follow the lines of the regenerated outputs, naming that table.
13. B21's expectations are constants. The corrected steps that need no data reproduce them (the preview); B21's code is
    left as it is, so that its outputs, which the numbers table locates by line, keep their lines; the evidence script
    compares the three constants with the regenerated outputs and marks a difference.
14. A matrix with a non-finite entry would make the observed level NaN while the substituted one stays finite. No change:
    the NaN would show in the output, the runner counts such matrices per site, and none is plausible on the data (a
    constant series in a window).
15. `check32.py` ignored a NaN on one side of the B25 comparison. Corrected: it fails.
16. Wording and bookkeeping. Corrected: the null's label; B15's label ("this script's run-level section above"); the
    evidence's regex (no trailing comma); `findings_b26code.md` 4's statement is now true of the tables; the evidence
    script checks B26's CSV, which a `--from` re-run merges, and notes such a re-run; the writer's session works in its
    own clone, not in V.S.'s repository, so its pytest does not reach the environment the start script checks.

## findings3_text.md

1. The preview missed three quotations of B17's values: S19 Table's rows B17 (ii) and (iv) (`supplementary.md` l. 1597
   and 1599) and S3 Text §7's ratios (l. 349). Corrected: the preview lists them with the text they become; for the
   ratios it gives both computations, from the replicate means of `calibration.csv` (the method of the verification of
   26 September 2026: −17.82, so −18) and from the printed rows (−17.40), and proposes −18 by the first; B26's entry
   names S19 Table's rows and S3 Text §7's ratios among the passages that quote B17's values; `findings2_text.md` 3's
   disposition gives the quotations (eighteen, after the fourth round).
2. Rule (i) did not list B15's relabelled sentence. Corrected: it lists "B15's label of its run-level residual", and the
   entry's paragraph on the correction says that the label names that residual as the script's own.
3. The root README understated what a run before B26's writes differently. Corrected (and extended in the fourth round,
   `findings4_text.md` 1): "the outputs of B5, the null, B23, B17 and B17b, B10's and B15's sections on synthetic series
   and Fig 3 (c) with their corrected values (`notes/review_2026-09-28/checks/b26_preview.md`), the lines the correction
   rewords (rule (i) of B26's entry), and any output that the data's matrices change".
4. The preview numbered its flagged rows by d108d66's table and misdescribed its baseline. Corrected: it runs
   `check_numbers.py` on commit A's text and numbers table with the corrected outputs of its part 1 laid over commit
   A's, gives the rows as commit A's table numbers them, and compares with commit A's own check ("rows 1183, data rows
   666, flagged 12", `checks/check_numbers.out`).
5. B23's "150 in the conditions (i) and (a1)–(a4)" included the unperturbed pairs. Corrected: the entry gives B23's
   matrices by condition, from the ordinals of the calls that held them: 16 in the unperturbed pairs, 8 to 28 in each of
   the eight conditions of (i) and (a1)–(a4), 6 to 8 in each of (a5)'s three.
6. Item 10. Corrected: "B26's pre-run entry quoted …"; the second round's code report is described with the planning
   session's scripts.
7. "Listed in full" overstated what `b26_changes.py` lists. Corrected in rule (i), the review folder's README and the
   dispositions of `findings_b26code.md` 17, `findings2_text.md` 5 and `findings2_code.md` 6: every changed line and
   cell in full; for each changed array the number of entries that changed, the largest change and the first 2,000
   entries; for each image the pixels that differ; the evidence holds the files themselves.
8. The list of the steps that evaluate the same data was incomplete. Corrected in the runner's docstring and the entry:
   B4, B4's residual source, B10, B14, B15, B19 and B22, for the data windows and the whole runs; the entry says that
   the whole-run pairs without a substituted estimate are in the site rows of B4's run-level line, and rule (iii) has S3
   Text give them with B4's pair-windows.
9. B25's wording. Corrected: `b25_fill.py` writes "not differentiable on the 10⁻³ scale", and the script's docstring
   gives the criterion as "1 % (+ 10⁻⁶)".
10. B25's run time against the self-test's timing. Corrected: the docstring no longer gives the replicates' times, which
    varied with the machine's load (the self-test's timing of one replicate at the longest length ranged from about 9 to
    24 ms in the planning session's builds and the audits' runs); it says under 25 ms each, --selftest timing one at the
    longest length, and the estimate of about 15–30 minutes stands.
11. The cross-reference in `findings2_text.md` 8's disposition. Corrected: `findings_text.md` 15.
12. The doubled comma of C072 and C084. Corrected.
13. Item 7's word accounting. Corrected: item 7 gives the net count of the changes with the ground-truth sentence they
    take out (24 words), then each condensation with its count, and the clause joined to the Discussion's first sentence
    (+7, after `findings3_text.md` 23 shortened it).
14. Item 2 and P48. Corrected: item 2 names "bundled third-party plotting functions" among P48's differences from its
    proposal.
15. The README's licence sentence (P49). Corrected (E12): "carries no licence of its own at 77af7aa".
16. The review README described a section the preview did not have. Corrected: the preview's section 3 gives the
    rehearsal of section 6 on synthetic series, made when it ended, and B26's entry states its result (item (iii) of
    "What is known before the run").
17. Rule (iii) pointed to a section that Methods does not name. Corrected: "S3 Text states the rule at the start of §6".
18. Rule (i)'s comparisons. Corrected: it names the three it uses and says why the final run's fourth,
    `9_wrapper_compare.py`, is not among them.
19. Two statements on B17 and B17b. Corrected: B17's other values at W = 60 change "p-values and shares by up to 0.016
    and 0.02, DiDs and SEs by 0.0001"; B17b's 8 matrices of the null's function are in the calibration draws that solve
    its generator's parameters, which use the windows' a, |q| and a_x − a_y and discard the substituted sts
    (`findings4_text.md` 2).
20. Captions. Corrected: the preview lists Table 3's caption, with S18 Table (b)'s description, among those the
    corrected outputs make inexact (in rows 6–11 the residual change at W = 60; `findings4_text.md` 5).
21. The preview's CSV rows. Corrected: `b26_changes.py` gives a CSV cell's line in the file ("l. N"), as the numbers
    table locates it.
22. CLAUDE.md. Corrected: "(B1–B26)" (K13; `b25_fill.py` no longer edits that line) and "separate sessions audited the
    prepared round, twelve audits in five rounds, after the fifth (…, with what was done with each finding in
    `dispositions.md`)".
23. Wording. Corrected: C03 reads "these data have no ground truth; what the analysis establishes" (one word fewer:
    Introduction through Methods 6,994 words); S1 Text's software line puts "the packages pinned in
    `requirements.lock.txt`" after the packages, not after Python (D02); Data and code availability (E13): "any positive
    definite 4 × 4 correlation matrix (`atoms_from_corr`; NaN for one that is not)"; the preview proposes, for S19
    Table's (a1), ("missed"; 1.4 and 1.5 times the predictions), its ratios being 1.41 and 1.49 (`findings4_text.md` 4).

## findings3_code.md

The audit stopped the rehearsal by accident: its `pkill -f` on its own test run also matched the runner of the rehearsal
with the corrected code, which was in B16. The rehearsal was started again from a clean tree after the third round's
corrections, with the final runner and reads; the rehearsal with d108d66's code, which the incident did not reach, ran
on. The preview's section 3 compares the two.

1. An interrupted run left no counts. Corrected: (a) the runner writes the CSV and the tables after every step (and,
   since the fourth round, before the first, each write replacing the file whole: `findings4_code.md` 2), the CSV's
   first line ending "; partial: k of n steps" until the last; `--from` accepts such a CSV and turns the suffix into ";
   interrupted after k of n steps" (since the fourth round, `findings4_code.md` 7), so that `--from` the interrupted
   step completes the run (tested: a run of the reduced section stopped by SIGTERM in its last step, then completed with
   `--from`); (b) each step's log is written line by line; (c) the evidence script accepts a run cut short (no "=== unit
   exit" line, the unit not active), says so, and checks every attempt's log and heartbeat; (d) the start script has a
   `--from` mode, under a unit of its own with the same inhibitor and heartbeat (numbered, `runb26from1`, `runb26from2`
   and so on, since the fourth round: `findings4_code.md` 1). The entry's paragraph on the run and rule (iv) say that
   `--from` follows a complete or an interrupted run.
2. B15's label. Corrected (`findings3_text.md` 2).
3. The cap on the calls that held matrices that are not positive definite. Corrected: the runner keeps every such call
   (`bad_calls`: its ordinal with its number of matrices), counts them (`bad_calls_n`, a column of the CSV), raises the
   csv module's field limit in the runner and in the evidence script's summary, and the tables print the count before
   the first ten.
4. The evidence summary. Corrected: each comparison script must end with exit status 0 and print its last line; the
   output folders may hold only modified and new files, no output may gain a `nogit`, the kernel's and logind's journals
   are checked only where readable (and a note says when not), and B21–B24's check counts must be those of the final run
   (B21: 1,025 run, none failed other than, possibly, its two checks against the log of 17 September 2026; B22, B23 and
   B24: 22, 63 and 10 run, 0 failed).
5. The pairing of lines in `b26_changes.py`. Corrected: within a block of changes the lines are aligned again on their
   text with the numbers masked and then paired by similarity, the rest reported as added or removed (refined in the
   fourth round, `findings4_code.md` 5); the audit's case (a line inserted before a changed one) pairs correctly.
6. The listing's details. Corrected: the summary counts the files that changed apart from those that agree within the
   tolerance or are the same (images by their pixels, PDFs once their dates are removed); arrays are compared under
   `np.errstate`, the largest difference is taken over the entries finite in both, and a change of the NaN or infinity
   pattern is stated (since the fourth round, `findings4_code.md` 6); the cap of 2,000 entries per array is stated in
   rule (i) and the review README. No change for the PDFs' cross-reference offsets: on V.S.'s machine the committed and
   the regenerated figures carry dates of the same length, and the PNGs are compared by their pixels.
7. The failed reads of B14 and B15. Corrected: the file is read inside `try … except (OSError, UnicodeError)`, and a
   failed read prints "CHECK FAILED (not read)" as a missing value does.
8. `check32.py`'s comparison of B25's re-run. Corrected: the tables' lines are compared with their numbers masked, each
   pair of numbers within 10⁻⁹; the CSV's values within 10⁻⁹, relative above 1; an infinity on one side only fails
   (`findings4_code.md` 8).
9. The self-test's summary. Corrected: a missing row prints nan, so that the list of the failed checks is printed. The
   note after the list: the versions of Python and NumPy are now in the CSV's first line, from which the tables take
   them, and the tables print no wall-clock time.

## findings4_text.md

1. B10's and B15's sections on synthetic series, and Fig 3 (c). Corrected: part 1 of the preview now lists, from the
   rehearsal of its part 3 (where d108d66's code printed these lines on the synthetic series exactly as d108d66
   committed them from the data), B10's replay of the null's first section (its W = 30 line: −0.0885 (−8.51 %) for
   −0.0886 (−8.52 %)) and B15's finite-sample null with lead–lag asymmetry (of the 150,000 pair-windows of each of its
   five configurations, the substituted matrices of 1, 0, 33, 81 and 88 not positive definite and 1, 11, 36, 91 and 120
   left out of the responses, `findings5_text.md` 1; all five lines change, the residuals by up to 0.0001 and the
   responses by up to 0.0003), with the runner's counts for them, and Fig 3 (c), which draws B23's AR(1) rate (−0.387
   for −0.390; the caption prints −0.39 either way); its part 2 lists S3 Text l. 276–280 with the text they become. The
   README's sentence, B26's entry (item (i) of what is known, and the list of what B23's changes reach) and
   `findings2_text.md` 3's disposition name them.
2. B17b's and B23's sentences. Corrected as proposed ("these 8 in the calibration draws that solve its generator's
   parameters, which use the windows' a, |q| and a_x − a_y and discard the substituted sts; the code before had given
   the 23 …"; "in each of the eight conditions of (i) and (a1)–(a4)"), and in `findings3_text.md` 19's disposition.
3. Four dispositions. Corrected: `findings2_text.md` 9 (the start of §6), 26 (two words fewer; refilled) and 3 ("l. 241
   (four)"), and `findings3_text.md` 10 (the docstring gives no range of timings now).
4. S19 Table's (a1). Corrected: ("missed"; 1.4 and 1.5 times the predictions).
5. Table 3's caption. Corrected: in rows 6–11 the residual change at W = 60 is now a mean over the pairs whose
   substituted matrices are positive definite in all 14 windows (2,980 to 2,995 of the 3,000).
6. Item 7. Corrected: "what the figure captions, the supporting information or another subsection hold".
7. Item 10. Corrected: it names the third round's changes of the text (C03, D02, E12, E13) and describes the fourth
   round.
8. `disp3.py`. It was a one-off helper of the planning session, not a record of the dispositions; it is no longer in the
   kit, and `dispositions.md` is the file kept.
9. The fill's ids. Corrected: G01–G16.
10. The preview's row numbers. Corrected: "row of commit A's table as `check_numbers.py` numbers it, its line in the
    file − 1".

## findings4_code.md

1. One resume only. Corrected: a resumed run takes the first number no earlier resumed run used (`runb26from1`,
   `runb26from2` and so on), with its own log, heartbeat and git-status files; the start script checks every `runb26*`
   unit for one still running; the evidence script finds every attempt by its log, and checks and copies each. Tested:
   the naming beside existing files; the evidence script on simulated runs (a run cut short and resumed; a failed step
   resumed).
2. Counts before the first step; whole-file writes. Corrected: the runner writes the CSV and the tables before the first
   step ("partial: 0 of n steps") and after every step, each through a temporary file flushed to the disk and renamed
   over the file. Tested on the reduced section: an interruption in the first step, then `--from` that step, interrupted
   in turn and resumed to the end, the CSV's rows equal to those of an uninterrupted run with the runner before these
   changes but the durations.
3. `--from` against the CSV. Corrected: the runner refuses a step unless every earlier step has its row with exit status
   0, naming the first that has not; `--check-from STEP` makes the checks of `--from` and runs nothing, and the start
   script uses it. Tested: a step after a failed one refused, the failed one accepted.
4. The evidence of a resumed run. Corrected: an attempt shorter than 330 s without a heartbeat line gets a note;
   tracebacks and CHECK FAILED lines of the steps that a later attempt ran again are noted, not failed; the logind,
   kernel and dpkg lines are checked against each attempt's window and those between attempts noted; the last boots are
   listed.
5. The pairing. Corrected: a stretch where a line was inserted or deleted among changed lines is paired by similarity as
   a whole; otherwise lines of the same masked form are paired by position and the others by similarity, measured as the
   share of the shorter line that the longer one holds (at least 0.6), so that a line that gained a note stays paired
   with what it was. The auditor's two cases pair correctly; the listing on modF is unchanged. (Refined in the fifth
   round, `findings5_code.md` 1: in the similarity, two lines of the same masked form score 1 more, and a short line is
   not taken for a part of a long one.)
6. The NaN pattern and the count. Corrected: an array's listing says how many of its changes are a change of NaN or
   infinity and how many entries become NaN, and lists those first; the count of the files that agree reads the text
   after the file's name.
7. The first line after a resume. Corrected: "; interrupted after k of n steps" where it was partial, before the re-run.
8. `check32.py` and infinities. Corrected: an infinity on one side only fails.

## findings5_text.md

1. B15's counts. Corrected in the entry, the kit and `findings4_text.md` 1's disposition: of the 150,000 pair-windows
   (3,000 pairs × 50 windows) of each of its five configurations, the substituted matrices of 1, 0, 33, 81 and 88 are
   not positive definite, and 1, 11, 36, 91 and 120 are left out of the responses, the matrices with a deviation added
   failing too (the auditor's replay, which reproduces the runner's counts).
2. The figure step's stop. Corrected: its look-up of B21's table (d) row for ts_gsr, which it expects to begin with a
   positive value (`| ts_gsr | +`, its line 284), fails on the synthetic series, where that row begins −0.044.
3. Two sources in part 3. Corrected: Fig 2 is drawn from B14's `family_atoms_ts_gsr_W60.npz`; `bca_intervals.csv`'s
   changed rows are B19's BCa intervals of B4's per-subject DiDs (`inference_rows_diag.pkl`).
4. The review folder's README. Corrected: `make_review32.py` was run again; the README lists the fourth and fifth rounds
   and describes the preview's part 1 as it now is; item 11 gives its new sha256.
5. Other traces of part 3. Corrected as proposed: the null's log reads B4's `diag_tables.md` and
   `inference_rows_diag.csv`; B10's W = 60 lines, the diagnostic's residual it reads from B4's
   `diag_series_<variant>_W60.npz`; B15's line of levels, the diagnostic's residual it reads from `diag_tables.md`;
   B19's BCa rows, B4's per-subject DiDs; B22's sentence that names the pairs each quantity is taken over, and B4's
   count on its level lines and lines for subject 1, rewordings of this commit.
6. B13's log. Corrected in the preview and the entry: B13's log differs only in the runner's frames in its traceback,
   and every other step whose outputs changed counted matrices that are not positive definite or reads a changed output
   of a step that did.
7. Stale dispositions. Corrected: `findings3_code.md` 1 (the suffix turned into "; interrupted after k of n steps"),
   `findings3_text.md` 1, 3, 5 and 22, `findings2_text.md` 19.
8. The two timing dispositions. Corrected: `findings2_text.md` 22 (the docstring's bound, under 25 ms per replicate) and
   `findings3_text.md` 10 (about 9 to 24 ms in the builds and the audits' runs).
9. `b26_changes.py`'s docstrings. Corrected: they give the cap of 250,000 line pairs and what happens beyond it, and the
   count of entries that become NaN.

## findings5_code.md

1. The pairing of lines of different lengths. Corrected as proposed: two lines of the same masked form score 1 more, and
   a similarity whose matched characters are under 0.3 of the longer line counts as 0, so that a short line is not taken
   for a part of a long one. The auditor's two cases pair correctly; the listing on modF is unchanged.
2. Superseded lines. Corrected as proposed: an attempt's lines are superseded from the first step that any later attempt
   started from, and all of them if it ran no step and another attempt followed. Tested: a failed step, a refused
   resume, then a resume that completes.
3. Units starting or stopping. Corrected as proposed: the start script stops for a `runb26*` unit that is activating,
   deactivating, reloading or running.
4. The note on the CSV's first line. Corrected: the whole line.
5. The docstrings on large stretches. Corrected (`findings5_text.md` 9).

## The writer's session's notes on 820cacd

The writer's session made commit 820cacd from this revision and reported three notes with it, besides B25's failed check
(record, "The binarised estimators on the AR(1) family (B25): the first run and the correction of one check"). What was
done, in the commit that follows:

1. P48's reason cited `b32/external_checks_2026-09-27.md`, a note of the planning session outside the repository.
   Corrected: the note is `external_checks_2026-09-27.md` in this review folder, with a preface, and P48's reason in
   `proposals.json` and in `revision/text_replacements_2026-09-28.json` names it there.
2. Row 3 of Table A in `notes/partB5_literature_v2.md` held the bars of "|q|" unescaped (since before d108d66), which
   split the row into more cells than its header. Corrected: "\|q\|". The same check
   (`notes/review_2026-09-25/checks/tablecheck.py`) finds the header of one table of
   `notes/review_results/partB/lag_tables.md` split in the same way ("model sts at |q| = 0.25"); that file is written by
   `notes/partB3_lag.py`, a step of B26's run, whose scripts stay unchanged until B26 has run, so it is corrected after
   that run. The other files it flags are kept as written: the superseded `notes/partB5_literature.md`, two earlier
   reviews and one table of an earlier entry of the record.
3. The header of `manuscript/figures/captions_v2.md` names c25a310, the commit at which `scripts/15_figures_v2.py`
   generated it, although this revision edited one phrase of Fig 1 (a) in the file (E07c) and in the script (E07s). Not
   changed: B26's run regenerates the file, with the commit of that run in the header and the script's phrase, and a
   header edited by hand would be one more difference between the regenerated file and the committed one for B26's rule
   (i) to read.

## findings6_code.md

The sixth round audited the changes made after B25's first run (record, "The binarised estimators on the AR(1) family
(B25): the first run and the correction of one check"), on a simulation of the whole flow with a real second run:
`findings6_code.md` the code, the writer's prompt and the planning session's check of the returned bundle,
`findings6_text.md` the entry and the texts. Their line numbers are those of the build they audited.

1. The first run's wall-clock and the two logs. Corrected as proposed in the planning session's check of the bundle
   (`check32c.py`, outside the repository): it checks that the first run's tables and log give 514 s, the value of the
   entry, that the first run's log equals the planning session's run of its script once the commit, the times and the
   paths are masked, and that the second run's log has no CHECK FAILED line and ends with 150 checks, 0 failed.
2. The diagnosis and the machine's BLAS kernels. Corrected: step 8 of the writer's prompt compares only the columns that
   the kernels leave unchanged (the series, (i), the knowns' means and the largest mean absolute local known), and
   `b25_fill.py` requires the second run's values within 10⁻⁹ (relative above 1) of the first run's, the tolerance of
   the separate session's re-run, and says in its text whether they are identical; the entry states the one value of
   `binarised.csv` that the Haswell kernels change.
3. The test for the entry at the first run's commit. Corrected as proposed: its title, with any time.
4. Step 6's test that nothing above the entry is edited. Corrected: `git diff --numstat` must give the entry's lines
   added and none removed.
5. The maximum over the replicates and a NaN. Corrected as proposed (H08).
6. The fill's docstring. Corrected: it lists the stop on the number of checks and the test of the entry with any time.
7. The pattern of the log's last line. Corrected as proposed.
8. The order of the lines of step 7. Corrected: the block is in the order the commands print.
9. The commits' subjects. Corrected: the message of the commit that follows 820cacd says that 820cacd's subject was
   written when the round had two commits.

## findings6_text.md

1. The Rule's statement that the sentences fixed with the pre-run entry are unchanged. Corrected as proposed: the
   verdict criteria and the sentences that state B25's values and verdicts are unchanged, and the sentences that name
   the run, its commit and the places that report it change, `CLAUDE.md` among them.
2. "Found them as that entry describes them". Corrected as proposed, in the outcome entry and the fill's docstring; the
   values the fill does not compare (the time and the wall-clock of the first run, the sha256 of its CSV) are those the
   planning session's check of the bundle compares (`findings6_code.md` 1).
3. "No sum". Corrected: "no sum over the samples" in the entry, the script's docstrings, S3 Text, S5 Text and the
   diagnosis.
4. "No value changes". Corrected as proposed; S3 Text, S5 Text and Data and code availability speak of the values of
   `binarised.csv`.
5. Why `b25_fill.py` was not run. Corrected as proposed.
6. The means of the knowns. Corrected: the entry gives, by series, the mean farthest from its exact value, and the
   diagnosis says which of its columns is over the sixteen knowns.
7. The diagnosis's definitions. Corrected as proposed.
8. The places where the corrected run's tables differ. Corrected.
9. The record's flagged table. Corrected: "one table of an earlier entry of the record".
10. The run at the commit of the correction. Corrected: "B25's second run was made at this commit".
11. The fill's docstring on the free parts of its sentences. Corrected: values read from B25's outputs and the dates and
   times of the entries, the runs and its own run.
12. The opening of the writer's prompt. Corrected as proposed.
13. The message of the commit that follows 820cacd. Corrected as proposed.
14. The outcome entry's long lines. Corrected: its first paragraph is wrapped at 120 columns when it is written.
