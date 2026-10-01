*Copy for the repository: paths of the planning session's scratch space are shortened to SP/; the opening sentence on where the report could not be saved is left out.*

## Audit R: 23 findings (2 errors, 6 inaccuracies, the rest wording or style)

Nothing in the repository or the evidence was modified. My scratch work is in `SP/audR/`, including a separate clone, `SP/audR/simcopy`, used to re-run the figure script and the checks.

The new record entries otherwise hold up: every count, site, sts range and mean, rule (i)–(v) statement, re-read verdict, word figure (19 + 4 − 24, 6,998 → 6,997) and claims tally (204/303/43/45; 248/36/19; 266/5/1/2/29; 32 of 36 corrected) checked out against the primary evidence.

**One-line summary**
1. **error.** `run_all.sh`:14–16 (S06) says "≈ 10,600 s in the final run … B17 ≈ 56, B17b ≈ 39, B16 ≈ 28 min". The final run's section 6 took about 9,540 s (2 h 39 min), with B17 2,638 s, B17b 2,038 s and B16 1,262 s. The record does not mention this change.
2. **error (must be fixed before commit).** `notes/review_2026-09-30/` does not exist yet, but the texts name files in it. `claims.csv` is not written by `make_claims_check_v2.py`, and the audit file is named `b26_rule_audit_report.md`, not `b26_rule_audit.md`. The promised dispositions are missing.
3. **inaccuracy.** S5_Text.md:23 still says "Every table and report the run wrote names c25a310". That is now false for section 6's outputs. The "then carried" edit (K06) hides that ten of the listed files still carry c25a310.
4. **inaccuracy.** README.md:110–115 (K16) attaches the section-6 exception to the logs only, and its B25 aside is misplaced.
5. **inaccuracy.** The README `notes/` row and the CLAUDE.md repository map do not list `review_2026-09-30/`.
6. **inaccuracy.** CLAUDE.md:397 says B25's re-run reproduced "its `binarised.csv` byte for byte". The first line differs; only the rows after it are identical.
7. **inaccuracy.** Record 8258–8264 puts B19 among the steps that only read others' outputs. B19 counts 8 failures itself (line 149), and its printed output there did not change. The audit report has the same slip.
8. **inaccuracy (minor).** Record 8203 says "Every other item passed" without disclosing that the evidence was gathered after a restart (unit not loaded), against the evidence script's instruction.
9. **wording.** Record 8265: "Nothing else changed" leaves out B22's float-noise check line (0 → 2.22e-16).
10. **wording.** "sha256 of every file the run wrote" and "the 96 files it rewrote" should read "changed or created" and "whose bytes changed".
11. **wording.** K07's charger window 11:09–12:29 UTC is the span of the heartbeat lines, not the actual disconnection.
12. **wording.** "The four W = 60 pair-windows" should be four on each variant; B7's number moves with the four on `ts_demean`.
13. **wording.** The heading "the run inventory's timing" means `run_all.sh`'s timing comment.
14. **wording.** "The two commits after 820cacd change …" omits the review folder of 28 September.
15. **wording.** "B01–B66": there is no B14–B19.
16. **wording.** B25's re-run: «OUTCOMMIT» comes between the re-run and the commit that records it, and the logs also differ in phyid's path.
17. **wording.** The claims program's notes on S5's sentence of 28 September promise an update the revision does not make.
18. **wording.** S5 §6's commit list does not mention the figures commit after the text commit, nor B25's re-run at b36178d.
19. **wording (fill).** «ENTRY_TIME» has no "UTC" after it, so the fill must include it; «OUTCOMMIT» (×5) and «OUTDATE» must be filled; the figure-script docstring says "30 Sep".
20. **wording.** C06's "(19 words, with 24 taken out elsewhere)" leaves out the corrections' 4 words.
21. **style.** README.md:37 (122 characters) and CLAUDE.md:389 and :399 (124 and 158) are over-long lines.
22. **wording.** `run_all.sh`:96 still gives B26 as "about three hours"; it took 225 min.
23. **wording.** Record 8226: "line 69 is the function" should be "is in the function".

There are also two optional notes outside my scope: Table 1's TDMI row, and S3 Text's subtraction, which close only before rounding.

---

## Content for findings_R.md

# Findings R: the record's four new entries (R01), K01–K16, C01–C07, S01–S06

Audit of `sim` at 6ae1cfa (HEAD) against 31f1153 («OUTCOMMIT») and d5a65bd, done 30 Sep–1 Oct 2026. Nothing in the repository or the evidence was modified. To re-run the figure script and the numbers, cells and table checks, I used a separate clone, `SP/audR/simcopy`, with `SP/v312` (python 3.12.3, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.1).

Severity: **error** = false, or a file the text points to is missing; **inaccuracy** = misleading or incomplete; **wording** = imprecise or style only.

## Findings

1. **error.** `run_all.sh`:14–16 (S06).
   - **Statement:** "about three hours more (≈ 10,600 s in the final run of 26 Sep 2026: B17 ≈ 56 min, B17b ≈ 39 min, B16 ≈ 28 min, …), of which B21–B24 (round 16) about 15 min".
   - **Evidence:** in the final run, section 6 ran from 20:15:22 to about 22:54:22 (`results/run_all_final.log`). That is about 9,540 s, as README.md:72 says ("2 h 39 min") and the runner's docstring says (`notes/partB26_positive_definite.py`:61–62, "2 h 40 min").
     - B17: 2,638 s ≈ 44 min (20:43:18 → 21:27:16). This is the "(2638s)" of `calibration_run.log` at d5a65bd, `git=c25a310`.
     - B17b: 2,038 s ≈ 34 min.
     - B16: 1,262 s ≈ 21 min.
     - B21–B24: about 9 min (22:45:32 → 22:54:10).
   - **Where the old figures came from:** 10,600 s, 56, 39 and 28 min are the durations of logs older than the final run. The old wording ("in the committed logs") was already stale at d5a65bd, whose logs were the final run's. S06 turned it into a false attribution to the final run.
   - **Not recorded:** the record's paragraph on the comment (analysis_record.md:8396–8397) mentions only B25's times and B26's 13,529 s, so this change goes unrecorded.
   - **Fix:** "(≈ 9,540 s, 2 h 39 min, in the final run of 26 Sep 2026: B17 ≈ 44 min, B17b ≈ 34 min, B16 ≈ 21 min, …), of which B21–B24 about 9 min; 13,529 s in B26's run …". Optionally add B26's B17 4,171 s and B17b 3,904 s. Have the record entry state the change.

2. **error (pre-commit condition).** `notes/review_2026-09-30/` does not exist at the simulated HEAD, yet the texts name files in it:
   - **Where it is named:**
     - Record 8175–8177, 8194 (`b26/` "with the three scripts"), 8252, 8270 (`audit/b26_rule_audit.md`, "with its replay"), 8273 and 8345 (`revision/text_replacements_2026-09-30.json`), 8331–8335 (`claims/make_claims_check.py` and `claims.csv` "beside it"), 8399–8401 (`b26/`, `claims/`, `revision/`, `checks/`, `audit/` "with what was done with each finding").
     - S5_Text.md:27 (K08).
     - draft_v2.md:246 (K10).
     - CLAUDE.md:381–397 (C02, C06).
   - **Evidence:**
     - (a) `make_claims_check_v2.py` writes only `external/claims_check/index.html` and its images (docstring l. 16; no `claims.csv` anywhere in it), so `claims.csv` must be produced separately.
     - (b) The audit exists as `b26_rule_audit_report.md`, with `b15_null_replay.py` and `.out`. The record names `audit/b26_rule_audit.md`.
     - (c) The promised dispositions do not exist yet. These are what was done with each audit finding, including the fifth claims check's wording findings and this audit.
     - (d) The program to commit is `make_claims_check_v2.py`, under the name `claims/make_claims_check.py`.
   - **Fix:** build the folder with exactly these names before the text commit, or change the names in the texts.

3. **inaccuracy.** S5_Text.md:23 (the sentence around K06, and K07).
   - **Statement:** "Every table and report the run wrote names c25a310 in its header, and so does every log of it that prints a commit, …; so, of the files named above, the 13 outputs of B21–B24, the nine at 66b570e-dirty, `results/logdet_correction_check.csv` and `review_checks.log` then carried c25a310."
   - **Evidence:** the present-tense "names" is now false for every output of section 6 (80 headers at 31f1153 name d5a65bd). K07, three sentences later, says so. K06 changed only "now carry" to "then carried". "then carried" also hides that the nine 66b570e-dirty files and `logdet_correction_check.csv` still carry c25a310 (checked at 31f1153).
   - **Fix:** "named c25a310 …; … carried c25a310 (the nine and `logdet_correction_check.csv` still do; B26's run rewrote those of section 6 at d5a65bd, below)".

4. **inaccuracy.** README.md:110–115 (K16).
   - **Statement:** "The tables and reports that the final run … wrote carry its SHA, c25a310, apart from five CSVs …, and so do its logs that print one, apart from those of section 6, which B26's run rewrote at d5a65bd (B25's carry b36178d)".
   - **Evidence:** the exception attaches only to the logs, but section 6's tables and reports also carry d5a65bd now. "B25's carry b36178d" sits in a sentence about files the final run wrote; the final run never ran B25.
   - **Fix:** "The tables, reports and logs that the final run wrote carry c25a310 (five CSVs carry none by design), apart from those of section 6, which B26's run rewrote at d5a65bd; B25's outputs, added after the final run, carry b36178d."

5. **inaccuracy (stale).** README.md:70 (the `notes/` row) and CLAUDE.md:506–533 (the repository map).
   - **Evidence:** both list every review folder up to `review_2026-09-28/` but not `review_2026-09-30/`, the folder this revision adds.
   - **Fix:** add the folder to both.

6. **inaccuracy.** CLAUDE.md:397 (C06).
   - **Statement:** "B25's re-run by the planning session at b36178d reproduced its `binarised.csv` byte for byte."
   - **Evidence:** the first line differs ("run 29 Sep 2026 09:41 UTC" against "09:20 UTC"). Only the rows after it are identical: their sha256 is bb888d45… in both, which I recomputed. The record (8371–8373) states this correctly.
   - **Fix:** "reproduced every row of its `binarised.csv` after the first line, which holds the time, byte for byte".

7. **inaccuracy.** Record 8258–8264, rule (i).
   - **Statement:** "those that count failures changed where they count them: B4 …, B4's residual source …, B14 …, B16 … and B22 …; the steps that read their outputs changed with them: … B19 (… from B4's pickle) …".
   - **Evidence:** B19 also counts 8 failures on the data, at `partB19_exchange_rates.py`:149, on the same W = 60 pair-windows (calls #19 … #705). That site feeds part (b)'s mean R² of the full AR(1) prediction, which is printed at three decimals and is unchanged. So not every counting step "changed where [it] count[s]", and B19 is filed in the wrong group. The audit report repeats the slip: it puts B19 under "Steps with no counted matrices".
   - **Fix:** add "B19 counts 8 (line 149, part (b)'s R², unchanged at its printed precision) and changed only through B4's pickle". Note the audit's slip in its disposition.

8. **inaccuracy (minor).** Record 8203, "Every other item passed".
   - **Evidence:** the summary also has two "note" items. One reads "runb26: the unit is not loaded (LoadState=not-found, after a restart?)". The evidence was gathered on 30 Sep at 08:31 UTC, after the machine was shut down at 21:42 EEST on 29 Sep:
     - `unit_journal.txt`: the unit was stopped at 21:42:21.
     - `boots.txt`: boot −1 ends at 21:42:25, and boot 0's start is later than its end.

     `b26_evidence.sh` asks to be run "before any restart or power-off". Nothing the rule needs was lost, since the unit's journal and log persist.
   - **Fix:** one clause disclosing it.

9. **wording.** Record 8265–8267.
   - **Statement:** "Nothing else changed but the rewordings … and … B21's count (39 to 40)".
   - **Evidence:** also changed, within the rule's allowance for float noise: B22's check line "ts_demean residual per window = diag_series res", whose |difference| went from 0 to 2.22e-16 (`diffs.txt` l. 427, 470).
   - **Fix:** add "and float noise below 10⁻⁹ (one check line of B22)".

10. **wording.** Record 8193–8194, and K07.
    - **Statements:** the record says "the sha256 of every file the run wrote"; K07 says "of the 96 files it rewrote".
    - **Evidence:** `outputs.sha256` lists the 99 files the run changed or created. The run also rewrote files byte for byte, for example the Fig 2 PNG and `results/run_15_figures_v2.log`.
    - **Fix:** "changed or created (99)"; "the 96 committed files whose bytes it changed".

11. **wording.** S5_Text.md:23 (K07).
    - **Statement:** "the charger disconnected from 11:09 to 12:29 UTC".
    - **Evidence:** these are the first and last heartbeat lines that found it disconnected (14:09:15–15:29:16 EEST). The real window is wider: the charger was out after 11:04:15 and back before 12:34:16 UTC. The record phrases it correctly, as heartbeat lines.
    - **Fix:** "the heartbeat found the charger disconnected …".

12. **wording.** Record 8296–8297, and S3_Text.md:225.
    - **Statement:** "The four W = 60 pair-windows move three numbers".
    - **Evidence:** there are four on each variant, eight in all. Table 1's TDMI DiD and the exact p move with the four on `ts_gsr`. The cross-half r (−0.052 → −0.051) moves with the four on `ts_demean`: B7 reads `diag_series_ts_demean_W60.npz`.
    - **Fix:** "the W = 60 pair-windows left out (four on each variant)".

13. **wording.** Record 8378, the heading "… and the run inventory's timing" (also quoted in CLAUDE.md:382–383).
    - **Evidence:** the paragraph is about `run_all.sh`'s timing comment. "The run inventory" is the title of S5 Text §4, which this revision also changes.
    - **Fix:** "… and `run_all.sh`'s timing comment".

14. **wording.** Record 8183–8185.
    - **Statement:** "The two commits after 820cacd … change B25's script …, B25's outputs and the text".
    - **Evidence:** they also change the review folder of 28 September (`b25_fill.py`, `b25_first_run/`, `audit/`, the revision JSONs, README). The conclusion holds: no step script, runner, `rev_phiid_fast.py` or `run_all.sh` changed.
    - **Fix:** add "and the review folder of 28 September 2026".

15. **wording.** Record 8272–8273.
    - **Statement:** "B01–B66".
    - **Evidence:** the file has B01–B13 and B20–B66; there is no B14–B19.
    - **Fix:** "B01–B13 and B20–B66".

16. **wording.** Record 8368–8369 and 8375 (B25's re-run).
    - **Evidence:** the commit that follows the re-run (09:41 UTC) is «OUTCOMMIT», which by design holds only B26's outputs; the result is recorded one commit later. The logs also differ in phyid's path: a source tree in the planning session, site-packages in the writer's.
    - **Fix:** a clause for each.

17. **wording (stale on commit).** `make_claims_check_v2.py`, DATA, sentence si=96 (S5 Text's sentence on the check of 28 September).
    - **Evidence:** Theiler's record says "It will change in the next revision", and Kay's note says "the counts in this sentence will be updated in the next revision". The revision keeps that sentence and adds a new one (K08).
    - **Fix:** reword the two notes before committing the program.

18. **wording.** S5_Text.md:31 (K09).
    - **Evidence:** the commit after the text commit, which will hold the regenerated figures and captions (C07; record 8383–8387), is not mentioned, although the earlier figure commits 66c6331, ddae618 and c25a310 are. Until that commit, the committed `captions_v2.md` still prints 0.107, 0.218 and 0.251. b36178d's entry could also note B25's re-run.
    - **Fix:** add "; the figures and captions regenerated at that commit are in the commit after it".

19. **wording (fill).** The placeholders.
    - «ENTRY_TIME» (record 8173, 8314, 8366, 8378) has no " UTC" after it. The 28 Sep replacements used "«ENTRY_TIME» UTC", and every filled heading reads "… HH:MM UTC (appended …)". The fill must therefore include "UTC".
    - «OUTCOMMIT» (record 8175, 8186; S5_Text.md:23 and 31, the latter twice) and «OUTDATE» (S5_Text.md:31, formatted "30 Sep") must all be filled.
    - The figure script's docstring says "then 30 Sep 2026".

20. **wording.** CLAUDE.md:391.
    - **Statement:** "(19 words, with 24 taken out elsewhere)".
    - **Evidence:** the 24 also offset the corrections' 4 words.
    - **Fix:** "(19 words and the corrections' 4, with 24 taken out elsewhere)".

21. **style.** README.md:37 (K13) is 122 characters in a paragraph wrapped at about 80. CLAUDE.md:389 (124) and :399 (158; C07 joined to the old continuation line) are also too long.
    - **Fix:** rewrap.

22. **wording.** `run_all.sh`:96.
    - **Statement:** B26 "(about three hours)".
    - **Evidence:** the run took 225 min (13,529 s by its rows).
    - **Fix:** "(225 min in its run of 29 Sep 2026)".

23. **wording.** Record 8226.
    - **Statement:** "the null's line 69 is the function of …".
    - **Fix:** "is in the function".

**Outside my scope (optional).** Table 1's TDMI row (draft_v2.md:81) now reads −0.1037, −0.1130, +0.0092. At printed precision, observed − substituted gives +0.0093; the unrounded values are −0.103719, −0.112954 and +0.009238. S3_Text.md:274's "(+0.01153 − 0.00267 = +0.00887)" likewise closes only before rounding (+0.008865).

## What I checked and found correct

**The record is append-only, and its new lines meet the width rule.**
- `git diff 31f1153 HEAD -- manuscript/analysis_record.md` has 230 insertions and 0 deletions; the first 8,171 lines are byte-identical.
- No new non-heading line exceeds 120 characters. There is no trailing whitespace.
- Applying every JSON entry to 31f1153 reproduces HEAD exactly, for all 14 files (the numbers CSV byte for byte, CRLF kept).

**The run.**
- 13:04:14–16:49:46 EEST; "all done in 225 min"; under `systemd-inhibit` sleep, idle, lid and shutdown.
- Clean tree. Versions checked before the run by `b26_start.sh` and after it.
- 39 rows, all exit 0, with no re-run. The rows sum to 13,529 s.
- No step script, runner, `rev_phiid_fast.py` or `run_all.sh` changed between 820cacd and d5a65bd.
- All 99 files in 31f1153 match `outputs.sha256` and `b26_commit.sh`'s list.

**The evidence.**
- Heartbeat: 45 lines, 17 DISCONNECTED (14:09:15–15:29:16 EEST); battery 95 % → 46 %; largest gap 301 s; one boot.
- No logind, kernel or dpkg events. B17 ran 13:32:50–14:42:22 and B17b 14:42:22–15:47:26.
- The preview's change lists for B5, the null, B23, B17 and B17b are identical, block for block, to `b26_changes.txt` (11 files). B15's five lines match the preview.
- `nogit` is at `review_checks.py`:133, line 70 of `review_checks.log`, and line 894 of the run log.
- Checks: B21 1,025, including the 17 September log; B22 22, B23 63, B24 10; 0 failed. The expectations read +0.0027, +0.0049, +0.0054.

**What the run counts, recomputed from `positive_definite.csv`.**
- 473,262,025 matrices, 0 non-finite; 42,681 not positive definite, all on `atoms_from_corr` with a block determinant ≤ 0; 215,276,476 PairPhiID, 0 failing; 12,889 nearly singular.
- B4 by call ordinals: [4, 1,617, 4, 1,661], matching `diag_tables.md` l. 6, 18, 30, 42. The run-level site has 0.
- B14, B19, B22: 8 each, on the same calls. B4's residual source: 4 + 4. B22: 13 + 1. B15's data sites: 0.
- B16: 10,817 / 15,776 / 0 / 0.
- B5 171; the null 126; B10 126; B23 172; B17 11,494; B17b 23; B24 0.
- B15: 4 in root searches; 1, 0, 33, 81, 88 substituted. The audit's replay gives 1, 11, 36, 91, 120 left out.

**Per step and site.** All 36 failing sites are listed, with every count, minimum, maximum and mean matching the CSV. Rule (ii)'s listing requirement is met.

**Rule (i).**
- 50 changed, 46 bytes-only, 3 new.
- Every per-file count in the entry matches `b26_changes.txt`.
- The writing scripts were checked by grep (`bca_intervals.csv` and the exchange tables are B19's; `ccs_pub_tables.md` is B6's).
- The run-level residuals are unchanged.

**Rule (ii).**
- The 14 main-text numbers match the regenerated outputs. I recomputed the S3 conversions.
- I recomputed the exact p over 2¹⁴ sign flips: 1762, 3576 and 4108 out of 16384 (0.10754, 0.21826, 0.25073); at d5a65bd 0.10791, 0.21875, 0.25061.
- S17: 73 rows changed plus 2 notes. 40 quantities' zero-inclusion differs (39 before). The other 929 ratios lie in 1.072–1.191 (6.7–16.1 % narrower, median 12.5 %).
- B5's range: 0.000 to +4.585, with 0.53 over 1,829 draws.
- Verdicts: B23 (b) (i) and (a4) met; (a1) 1.41 and 1.49 times (1.48 and 1.59 before); (a2) 1.32 and 1.34; B17 (ii) and (iv); B7 0.318 < 0.41; B22 (c) +0.00112; B19 (d) largest ratio 1.037.

**Rule (iii) and the word count.**
- Counted with the repository's `wc.py`: 6,994 at 820cacd and b36178d, 6,998 at d5a65bd, 6,997 at HEAD.
- Applying the replacements one at a time: B03 +9, B04 +4, B06 +6; Q02/Q05/Q06/Q07 net +4; L01–L05 −24.

**Rules (iv) and (v).** Both hold.

**The rule as a whole.** The entry satisfies rules (i)–(v).

**The claim-by-claim check, recomputed from DATA.**
- DATA's commit is d5a65bd. 204 sentences and cells, 303 claims, 43 works, 45 PDFs.
- Verdicts: S 248, Q 36, X 19, N 0, P 0.
- Firsthand status: own 266, part 5, second 1, code 2, na 29.
- Reviews: 83, 102, 108 and 78 records, with 19, 19, 23 and 11 findings. The fifth check covered 6 entries and found one wrong verdict.
- Each of the 32 Q claims maps to a correction in Q01–Q31. The other 4 are the competing-interests citations.
- The files added on 29 and 30 Sep are as stated; Luppi 2025 is "posted January 10, 2026".

**B25's re-run.** 09:41 UTC, the stated versions, 150 checks with 0 failed, 486 s. The rows' sha256 is equal. The tables differ only in the time, the sha256 and the wall-clock (486 s against 482 s).

**Fig 5's caption and B3.**
- At HEAD in the clone, the figure script changed only the captions header and Fig 5's caption, plus 70 pixels of Fig 4's PNG (largest channel difference 1). The PDFs differ only in their dates and offsets.
- All six main-text captions equal the regenerated ones without their Source sentence.
- `lag_tables.md` l. 19 is the only malformed header.

**Bookkeeping.**
- K01/K02: S19 has 64 rows: 56 counted (28/14/14) plus 8. "Seven further entries" is correct, and B26 is not counted, consistent with its "No prediction".
- K03/K04: the labels read B1–B26. No "B1–B25", "6,994", "except three", "now carry c25a310", "15–30 min" or claim that B26 or B25's re-run is still to come remains outside the record.
- K05, K08, K10–K15, C01–C05 and C07: correct.
- Counts: 1,196 numbers rows. `check_numbers.py` reproduces the planning output (12 sign flags, as before). The cell and table checks pass.
- S01–S05: correct.

**Nothing to save to memory.**
