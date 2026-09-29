## Audit of A2's text changes and of the fill's texts at B (agentT6)

**How the audit was done.** I compared treeA2 (the same as sim 83a48d7 except for the heading time), treeA0 (the same as sim fb6a071) and sim B (2fc896f). In the simulation, fb6a071 stands for 820cacd and 83a48d7 for A2. Line numbers below are A2's unless marked B. I recomputed everything in agentT6 with the planning session's environment (`scratchpad/v312`: python 3.12.3, numpy 2.5.3, scipy 1.18.1, phyid 0+untagged.8.g6c5f2e9) and `PYTHONDONTWRITEBYTECODE=1`. No file outside agentT6 was changed; I ran one `git status` on the sim clone at the start, which changes no file content.

The helper files are in `…/audit6/agentT6/`:
- `verify_sums.py` and `verify_sums.out` (numpy's summation)
- `recompute_outcome.py`
- `wdiff.py`
- `rebuild/`
- `diag_rerun.out`

## Findings (most severe first)

**1. MAJOR — `manuscript/analysis_record.md` l. 8100–8101 (new entry, "Rule.")**
- **Text:** "Its verdict criteria and the sentences fixed with the pre-run entry are unchanged; it is changed now (L01–L11 …)".
- **What is wrong:** this is false. L04, L06 and L08–L11 rewrite sentences that were fixed with the pre-run entry:
  - L04 (`b25_fill.py` l. 330–331): S3 Text §11's pointer to the record.
  - L06 (l. 426–431): Data and code availability's sentence "it was run at {A} …", now extended with the first run.
  - L08 (l. 401–408): S5 Text §6. For the pre-run commit, "B25 was run at this commit" becomes "B25's first run was made at this commit", and a new item is added.
  - L09 (l. 453–460): CLAUDE.md's two sentences. "B25 run at {A} and reported" becomes "B25's second run made at {A} and reported", and "(B25 was run and reported in the commit that follows {A})" is rewritten.
  - L10 and L11 (l. 548–559, 579–583): the outcome entry's opening ("the commit of the pre-run entry" is replaced; "fixed with the pre-run entry" becomes "… and changed, before this run, under the entry of the first run") and its "Where it is reported".
- **What is actually unchanged:** the verdict code and the sentences that state values and verdicts (RESULTS, TABLE, S19 rows, the S20 sentence, the count sentences, the outcome entry's facts, verdicts and values).
- **Evidence:**
  - The diff of `orig/b25_fill.py` against A2's.
  - The outcome entry the fill writes says the text was "fixed with the pre-run entry and changed, before this run, under the entry of the first run" (B record l. 8131–8133).
  - The fill's own docstring (l. 10–11) claims only that "the other sentences are unchanged".
  - The entry's list of places also leaves out CLAUDE.md.
- **Correction:** "Its verdict criteria and the sentences that state B25's values and verdicts are unchanged; it is changed now (L01–L11 of the same file of replacements), and with it the sentences that name the run, its commit and the places that report it: it takes this commit; …; and its text states the first run, its failed check and this correction in S3 Text §11, S5 Text §4 and §6, Data and code availability and the outcome entry (and `CLAUDE.md` names the second run)."

**2. MAJOR — `notes/review_2026-09-28/revision/b25_fill.py` l. 556–557 (L10); at B this is written to `analysis_record.md` l. 8129–8130**
- **Text:** "and `b25_fill.py` found them as that entry describes them".
- **What is wrong:** this claims more than the fill checks.
- **What the fill checks** (l. 134–188):
  - the three files exist;
  - the tables and log name one commit, which is the parent of the given commit, and the record at that commit holds the pre-run heading and not the new one;
  - the CSV matches the sha256 its own tables give, and its first line has the right form;
  - the tables say "Checks: 150, failed 1", with exactly one NO row and one CHECK FAILED line, both the series-4 check (1.06e-12 against 1e-12);
  - the four times are in order.
- **What it does not compare**, although the entry states them: 06:16 UTC; 514 s (`WALL0` is read at l. 163 and only printed); the versions; the value 2dc288bb…; the other nine series values; 4.82 × 10⁻¹⁴; facts (a)–(c).
- **Correction:** "…, and `b25_fill.py` found that they name this commit's parent and report its 150 checks with the one failed check that entry describes, and every row of this run's `binarised.csv` after its first line equal to the first run's."
  - The docstring l. 9–10 has the same issue. Correction: "it checks that the first run's outputs, kept in …, name the parent of that entry's commit and report the one failed check that entry describes".
  - The alternative, adding these comparisons to the code, cannot include the sha256 value: in the simulation the CSV's first line names fb6a071, so its sha256 differs.

**3. MINOR — "no sum"**
- **Where:**
  - record l. 8080: "no sum enters it";
  - `partB25_binarised.py` l. 57: "(no sum enters the comparison)", and l. 404: "so that no sum enters it";
  - `b25_fill.py` l. 345 (S3 Text l. 432 at B) and l. 444 (S5 Text l. 23 at B): "which involves no sum";
  - `b25_check_diagnosis.py` l. 13–14: "(ii) … that no rounding of a sum makes".
- **What is wrong:** `Kc @ _MINV_T` makes each atom a sum of sixteen products. Its rounding is what the corrected check measures (≤ 8.88e-16 in the ten series, 4e-15 over the replicates), and the same product rounds in (ii). The correction removed only the sum over the samples.
- **Correction:** write "no sum over the samples" in each place (and "a sum over the samples" in the diagnosis).

**4. MINOR — "no value changes" and "every value equal"**
- **Where:**
  - record l. 8083: "no value of the tables or of `binarised.csv` is computed otherwise", and l. 8091: "it changes no computed value";
  - `commit_message_32_2of3.txt` l. 12: "no computed value changes";
  - `b25_fill.py` l. 345–346 (S3 Text l. 432): "the second run's values equal the first run's";
  - l. 445 (S5 Text l. 23): "every value of the second run equals the first run's";
  - l. 430 (draft_v2.md l. 246): "the two runs' values are identical".
- **What is wrong:** the corrected check's eleven values in the tables are computed otherwise, and they differ: 3.56e-13–1.06e-12 and 4.82e-14 in the first run, 0–8.88e-16 and 4e-15 in the corrected one (`planning_runs.md` l. 17–20 says so). The failed-check count and the wall-clock differ too. What is equal, and what l. 166 checks, is `binarised.csv` after its first line. S5 §4 quotes the first run's 1.06 × 10⁻¹² in the same passage.
- **Correction:**
  - record: "no other value of the tables, and no value of `binarised.csv`, is computed otherwise" and "it changes no value of `binarised.csv`";
  - commit message: "no other computed value changes";
  - S3 Text and S5 Text: "every value of the second run's `binarised.csv` equals the first run's";
  - Data and code availability: "the values of the two runs' `binarised.csv` are identical (S5 Text)".

**5. MINOR — record l. 8061–8062**
- **Text:** "As the pre-run entry's rule requires, `b25_fill.py` was not run and nothing was reported."
- **What is wrong:** the rule (l. 7875–7877) says only that the fill "stops without writing if … B25 reports a failed check". Not running the fill came from bundle 32's step 11. The A2 commit message gets this right.
- **Correction:** "As the pre-run entry's rule requires, nothing was reported; `b25_fill.py`, which stops without writing on a failed check, was not run."

**6. MINOR — record l. 8075–8076**
- **Text:** "The mean of the knowns lies 3.1 × 10⁻¹³ to 5.1 × 10⁻¹³ from its exact value".
- **What is wrong:** these figures are, for each series, the largest of the sixteen components (diagnosis l. 61). Individual knowns' means lie as close as 9.2e-17: my recomputation gives per-series minima from 9.2e-17 to 3.2e-15 and maxima from 3.0503e-13 to 5.0937e-13, so 3.1 and 5.1 are right as maxima.
- **Correction:** "lies up to 3.1 × 10⁻¹³ to 5.1 × 10⁻¹³ from its exact value (its largest component, by series)".
- **Related:** the diagnosis prints "each value the largest over the sixteen atoms" (l. 43, and .out l. 3), but its two knowns columns are taken over the sixteen knowns.

**7. MINOR — `b25_check_diagnosis.py` l. 9–10**
- **Text:** "with the definitions of notes/partB25_binarised.py, which the correction left unchanged".
- **What is wrong:** the correction changed `phyid_quantities` (H04, H05). The definitions the script actually uses (l. 38–39) are unchanged.
- **Correction:** "with the definitions it takes from notes/partB25_binarised.py (the simulation, the seed, the operating point, phyid's call, the knowns and the atoms' map), which the correction left unchanged".

**8. MINOR — `b25_first_run/planning_runs.md` l. 17–20**
- **Text:** "in four places only:" followed by three items.
- **What is wrong:** the "eleven rows" item covers two places in the tables (rows 347–356 and row 362).
- **Correction:** "the count of failed checks (0 for 1); the ten rows of the corrected check in the ten series and its row over every replicate, whose names … ; and the wall-clock".

**9. MINOR — `audit/dispositions.md` l. 588–589 (W04)**
- **Text:** "… two earlier reviews and earlier entries of the record".
- **What is wrong:** run over every tracked .md file at A2, `tablecheck.py` flags one table in one earlier entry: record l. 2515–2520, in "Part B, items 6–8: outcomes, 15 Sep 2026", whose header is split by "|Δ|".
- **Correction:** "two earlier reviews and one table of an earlier entry of the record".

**10. MINOR — `b25_fill.py` l. 405–406 (L08); S5 Text l. 31 at B**
- **Text:** "83a48d7 (…; B25 was run at this commit)".
- **What is wrong:** next to "B25's first run was made at this commit" for the previous commit, it does not say which run.
- **Correction:** "B25's second run was made at this commit".

**11. MINOR — `b25_fill.py` l. 4–5 (unchanged docstring sentence)**
- **Text:** "only free parts are values read from `binarised.csv` and the dates and times of the entry, the run and this script's own run".
- **What is wrong:** the templates now also take `A0`, `RUN_DATE0`, `WALL0` and `NCHECKS0` from the first run's outputs and `DATE_K` from the new entry's heading (and, already before this change, the second run's tables).
- **Correction:** "… values read from the two runs' outputs and the dates and times of the two entries, the two runs and this script's own run".

**12. MINOR — writer's prompt opening (`prompt_bundle32_continued.md`)**
- l. 6, "two means over 10⁵ samples". Correction: "over the 99,999 samples of a series of 10⁵".
- l. 7–8, "the rounding of that sum reached the tolerance". The knowns' means are at most 5.1e-13 from exact (series 4: 4.65e-13); the 1.06e-12 is that rounding carried through the atoms' linear map. Correction: "the rounding of those sums, carried into the atoms, reached the tolerance".
- l. 8, "agree sample by sample to 8.9 × 10⁻¹⁶". This holds in the ten series; over every replicate it is 4 × 10⁻¹⁵ (`run_new.out` l. 169). Correction: add "in those ten series".
- l. 8–9, "reproduced your run bit for bit … (your `binarised.csv` has the sha256 its run gives)". The planning run's CSV names git=nogit and 06:55 UTC; only with its first line replaced does it give 2dc288bb…. Correction: "reproduced your run's values bit for bit (its `binarised.csv`, with its first line replaced by yours, has your sha256)".
- l. 20, "the six files A2 adds". A2 adds nine (steps 4 and 7). Correction: "six of the nine files A2 adds (the other three are your first run's outputs)".

**13. MINOR — `commit_message_32_2of3.txt`**
- l. 14, "the planning session's two runs of B25". The folder holds only a note on them. Correction: "a note on the planning session's two runs of B25".
- The log will read "(1 of 2)" (820cacd), "(2 of 3)", "(3 of 3)". Suggested addition to A2's message: "820cacd's subject, written when the round had two commits, reads (1 of 2)."

**14. MINOR (layout) — `b25_fill.py` l. 552 (L10)**
- At B, the outcome entry's line containing `{ENV}` is 173 characters (record l. 8125) and l. 8127 is 121, against the record's 120-character lines. The new entry itself stays within 120.
- **Correction:** re-wrap the template around `{ENV}`.

## Checked and found correct

**The first run's CSV hash and the planning runs**
- The run_old CSV, with the first line `# partB25_binarised.py; git=820cacd; run 29 Sep 2026 06:16 UTC`, has sha256 2dc288bb3357c66a8bb8954861fc13d5351f2748de83900c019e26bcdbce3479.
- After its first line, run_new's CSV equals run_old's: 949 lines, the column names plus 948 rows.

**Numbers in the new entry**
- 150 checks, 1 failed.
- Series 4: 1.06e-12. The other nine series: 3.56e-13 to 9.74e-13. Every replicate: 4.82e-14.
- 514 s; 06:16 UTC (the script takes this time at its start, l. 120–121); the versions.
- Facts: (a) 42/42; (b) +1.8153, −0.1496, 12.13, 1.76; (c) 126/126.
- Diagnosis:
  - (i) equals the first run's values at full precision;
  - (ii) 1.11e-16;
  - (iii) 8.88e-16;
  - the atoms' mean at most 5.55e-17 from exact.
- Corrected run: 150 checks, 0 failed; 8.88e-16 in the series, 4e-15 over the replicates.
- Self-test: 54 checks, 0 failed, differing from A's only in its three timings.
- Script sha256: b51d052c… (A) and 74b6d5f4… (A2).

**numpy's summation, verified bit for bit on numpy 2.5.3**
- Each series gives 99,999 local values.
- Each `at_c[k]` is a one-dimensional contiguous array; `np.mean` of it equals numpy's pairwise algorithm in 160 of 160 cases and never equals the sequential sum.
- `Kc` is C-contiguous, 99,999 × 16; `Kc.mean(0)` equals the sequential sum divided by m in 160 of 160 cases.
- The MMI and CCS calls return identical `I_res`, so the diagnosis reproduces the first run's check exactly.
- The diagnosis, re-run here, reproduces its .out after line 1 in 8 s. The seed and the order of the draws are as its docstring says.

**What A2 changes**
- A2 rebuilt from A, the 28 replacements, the six tarball files and the three first-run outputs is identical to the simulation's A2 (except for the heading time).
- The changes to the script are exactly H01–H07. The planning runs' tables differ only in the check rows, the failed-check count and the wall-clock.
- The 16 sha256 lines of the prompt's step 7 match A2.
- The tarball and message sha256 values match, and the tarball holds exactly the six files.
- There are 28 replacements, each with a "why".

**`b25_fill.py` and the pre-run entry**
- The fill's stop conditions are as the Rule paragraph lists them.
- Its verdict code and value sentences are unchanged.
- The new entry is consistent with the pre-run entry: same check, same tolerance, same criteria. The move of the run to A2's commit and the prior knowledge of (a)–(c) are disclosed. Nothing the first run reported is left out.
- `planning_runs.md` is exact apart from item 8.

**Texts at B**
- Every number in the outcome entry matches my recomputation from the second run's CSV: the counts 56/28/14/14, 0.4355, 1.2588, 0.4539, 0.2188, 0.6410, 0.1639, 0.7082, −0.1914 to −0.0169, −0.0627 to −0.0169, −0.0456, −0.0481, +0.0400, +0.0397, the monotonicity phrases, +0.1244, +0.1415, and +0.0409 ± 0.0005.
- The second run: 461 s, 150 checks, 0 failed, `git=83a48d7` in all three outputs, sha256 consistent.
- The numbers in S3 §11, S5 §4 and §6, and Data and code availability.
- CLAUDE.md and README.md.
- The main text carries no B-labels. The manuscript files gain no new process label; the only one is the pre-existing "a session of the AI system".
- `wc.py`: 6,998 words with headings at B (6,994 at A and A2).

**Other A2 changes**
- K01–K05 are correct.
- W01: the unescaped bars date from 958648f (20 Sep), and the file is no longer flagged.
- W02 and W03 are correct.
- W04: items 1 and 3 are correct. Item 2 is correct except for finding 9: the `lag_tables.md` header, `partB3_lag.py` in section 6, and B26's runner reading section 6 through the figure step, so it regenerates `captions_v2.md`. E07c and E07s each edit one phrase of Fig 1 (a).
- `external_checks_2026-09-27.md` is the b32 note byte for byte plus the preface. The preface's claims hold: P48 is the licence, P50 the merge date, and the line numbers are d108d66's (draft 246 and 298, README 116, CSV row 498).

**Commit messages and prompt**
- The commit messages are otherwise exact. B's "every row … equals" is guaranteed by the fill's stop at l. 166.
- The prompt's opening is otherwise exact: 820cacd on d108d66, the failed line verbatim, stopping before step 12 as bundle 32's step 11 required, replacing steps 12–16, three commits, and «A2» in three places.
