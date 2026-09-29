## Fifth-round text audit of commit A (`…/b32/audit5/tree2`, kit `…/b32/audit5/kit`): report

Paths: `tree2` = `…/b32/audit5/tree2`, `kit` = `…/b32/audit5/kit`, `R2`/`O2` = `…/b32/rehearsal/R2`, `O2`, `modF` = `…/b32/codetest/modF`. I wrote only under `…/audit5/agentT5/`. I used `GIT_OPTIONAL_LOCKS=0`, `PYTHONDONTWRITEBYTECODE=1` and `TMPDIR` in my scratch folder. After the work I confirmed that no file (and no `.git` entry) in tree2, the kit, modF, the rehearsal, final31/gh, r21 or work32A was newer than my runs. I did not report «ENTRY_TIME».

### Findings, most severe first

**1. MAJOR — B26's entry, the disposition and the kit give B15's failing matrices as counts of pairs. They are counts of pair-windows.**
- **Where:**
  - Record l. 7974–7977: "the substituted matrices of 1, 0, 33, 81 and 88 of its five configurations' 3,000 pairs".
  - `dispositions.md` l. 475–477 (findings4_text 1), same words.
  - Kit `b26_preview.json` "data_free".
- **Evidence:**
  - Each configuration evaluates `window_corr` over 3,000 pairs × 50 windows, so 150,000 matrices (B15 l. 149, 154, 170).
  - The runner's rows count matrices: "1 of 150,000", "202 of 450,000 (#1: 33, #2: 81, #3: 88)".
  - My replay (`agentT5/b15pairs.py`, 59 s) reproduces the runner's counts. The failing substituted matrices lie in **1, 0, 23, 56 and 60 pairs**. Those left out of the responses are 1, 11, 36, 91 and 120 pair-windows, in 1, 7, 24, 57 and 60 pairs.
  - The sentence also omits the failing matrices with a deviation added: 11 + 2 in configuration (1) and 149 + 33 + 39 in (2). These are why (1)'s line changes although none of its substituted matrices fails. The preview's total is 644 = 4 + 2 × 203 + 234.
- **Correction (all three places):** "…has 4 matrices not positive definite in its root searches, which use a and |q| only; of the 150,000 pair-windows (3,000 pairs × 50 windows) of each of its five configurations, the substituted matrices of 1, 0, 33, 81 and 88 are not positive definite (in 1, 0, 23, 56 and 60 pairs), and 1, 11, 36, 91 and 120 are left out of the responses (the matrices with a deviation added fail too); each of its five lines changes, …"

**2. MAJOR — Preview l. 2241 (kit `preview_cfg.json` part2.trace for `results/run_15_figures_v2.log`) gives a false cause for the figure step's stop.**
- **What it says:** "(its look-up of B21's rows by their held values fails on these series)".
- **Evidence:**
  - Both runs stop at `scripts/15_figures_v2.py` l. 284, `table_line("partB/inference_revision_tables.md", "| ts_gsr | +")`. This is B21's table (d), the disattenuated ratio: "no line starting '| ts_gsr | +'".
  - On these series that row reads "| ts_gsr | -0.044 | …" (l. 283 in both runs).
  - The look-up by the held values is l. 420. It is never reached, and its rows ("| +0.0027 |", "| +0.0049 |", "| +0.0054 |", l. 233–235) exist in both runs.
- **Correction:** "(its look-up of B21's table (d) row for ts_gsr, which it expects to begin with a positive value, "| ts_gsr | +" at its line 284, fails on these series, where that row begins −0.044)".

**3. MAJOR — Preview part 3: two of the stated sources are not where the changes come from.**
- **l. 2202–2203 (Fig 2 PDF and PNG):** "drew Fig 2 from B4's outputs".
  - Fig 2 is drawn from B14's `family_atoms_ts_gsr_W60.npz` (`15_figures_v2.py` l. 206–242, "Fig 2: … (B14)"). That file changed (l. 2233).
  - Write: "the figure step, which drew Fig 2 from B14's `family_atoms_ts_gsr_W60.npz` before it stopped: an earlier step's changed output".
- **l. 2210 (`bca_intervals.csv`):** "from B19, whose matrices R counted".
  - All 59 changed cells are in the six "diag …" rows (diag predicted sts ts_gsr W60; diag residual sts ts_gsr W60 [primary/early/late], ts_demean W60, ts_gsr W30).
  - B19 computes these rows from B4's `inference_rows_diag.pkl`. B19's own matrices (its l. 149) feed only `exchange_rates_tables.md` l. 28–29.
  - Write: "from B19 (`partB19_exchange_rates.py`), which reads B4's per-subject DiDs (`inference_rows_diag.pkl`): an earlier step's changed output".

**4. MAJOR — The review folder's README was not updated.**
- **Where:** `tree2/notes/review_2026-09-28/README.md` l. 61–66 (audit list) and l. 52–56 (the preview's description).
- **Evidence:**
  - The file equals audit4's byte for byte (sha256 4bfe87d5…, the hash item 11 l. 7773 quotes).
  - Its audit list stops at the third round, although `findings4_text.md` and `findings4_code.md` are in the folder.
  - The kit's `make_review32.py` l. 120–123 has the fourth round but was not run: `r21/files/…/README.md`, which `build32.py` lays into the tree, is from 21:22 and equals tree2's.
  - Run into scratch (`agentT5/review_readme/`), it gives a README that differs only at l. 65–66 (sha256 b992afdc…); the other four files it writes are identical.
  - Minor part: the preview description does not mention part 1's new content.
- **Correction:**
  - Extend the description in `make_review32.py`: "…what B26's pre-run entry knows before the run: what the correction changes whatever the data (the steps of section 6 that read no data, run by the planning session with the corrected code, their counts … and every line and cell of their outputs that differs from d108d66's; B10's and B15's sections on synthetic series; Fig 3 (c)), the numbers …".
  - Run the script, rebuild, and update item 11's README hash.

**5. MINOR — Preview part 3: other traces are inexact or incomplete.**
- **l. 2206 (the null's log):** the shares come from B4's `diag_tables.md`, not from `inference_rows_diag.csv` (`data_refs`, `review_v2_residual_null.py` l. 82–104). Write "…reads from B4's changed `diag_tables.md` and `inference_rows_diag.csv`…".
- **l. 2213–2215 (B10):** its W = 60 lines (l. 43–57) change through the "W = 60 residual of the diagnostic" it reads from B4's `diag_series_<variant>_W60.npz` (B10 l. 245, 265). Add that.
- **l. 2224–2226 (B15):** l. 42 also changes through the diagnostic's W = 60 residual it now reads (`diag_tables.md`) and its own run-level residual. Add "and the diagnostic's W = 60 residual it now reads".
- **l. 2227–2228 (B19):** tables l. 55–60 are the BCa rows from B4's pickle. Add "and B4's per-subject DiDs it reads".
- **l. 2207–2209 (B22):** its reworded sentence (F39; tables l. 23 and 48) is not named. Add "with its two sentences, which this commit rewords".
- **l. 2216–2220 (B4):** its count on the level lines and its lines for subject 1 are rewordings of this commit (rule (i)). Add them.

**6. MINOR — Preview l. 2243 and record l. 7988–7991 (item (iii)) are contradicted by B13's log.**
- **What they say:**
  - The preview: "Every step whose outputs changed either counted … or reads …; no step without either changed an output".
  - The entry: "changes in 40 of 337 files, each in a step that counted … or that reads…".
- **Evidence:** B13's log is one of the 40 files. It differs only in six runner frames, and B13 neither counts nor reads a changed output (it reads the `.mat` and `crosslag_budget.csv`).
- **Correction:**
  - Preview: "…but for B13, whose log differs only in the runner's frames; no other step changed an output…".
  - Entry: "found changes in 40 of 337 files: B13's log only in the runner's frames, each of the others in a step that counted …".

**7. MINOR — Some dispositions no longer give "the state of this commit", which the header (edited this round) says they do.**
- l. 435 (findings3_code 1, edited this round): "`--from` accepts such a CSV and drops the suffix". The runner now turns it into "; interrupted after k of n steps" (runner l. 435; findings4_code 7). Write "…and turns the suffix into "; interrupted after k of n steps" (since the fourth round, `findings4_code.md` 7)".
- l. 367 (findings3_text 1): "thirteen quotations" is now eighteen.
- l. 370–372 (findings3_text 3): quotes the old README sentence, without "B10's and B15's sections on synthetic series and Fig 3 (c)".
- l. 377–379 (findings3_text 5): "8 to 28 in each of (i) and (a1)–(a4)". Write "in each of the eight conditions of (i) and (a1)–(a4)".
- l. 418–419 (findings3_text 22) and l. 285 (findings2_text 19): "eight audits in three rounds". CLAUDE.md now says "ten audits in four rounds".

**8. MINOR — The two timing dispositions do not match what the files show.**
- l. 393–394 (findings3_text 10): "went from 9 to 24 ms across the planning session's builds".
  - The builds printed 23.7, 18.8, 15.8 and 11.1 ms.
  - 9.8 ms is in `b32/audit/aud/`, the first-round text auditor's scratch (`findings_text.md` l. 6), and 12.0 ms is in `scratch_b25`.
  - Write "…was 23.7, 18.8, 15.8 and 11.1 ms in the four builds, 9.8 and 12.0 ms in audit runs…".
- l. 295–296 (findings2_text 22): "the docstring names the self-test's timing … rather than a range".
  - The docstring gives the bound "under 25 ms each" and names no timing.
  - Write "the docstring gives a bound, under 25 ms per replicate, and says that --selftest times one at the longest length".

**9. MINOR — The `checks/b26_changes.py` docstring (l. 15–17, 27–28) leaves out two things the code does.**
- It omits the cap `SMALL` = 250,000 line pairs (l. 142, 148–153). A larger stretch with sides of unequal length goes to the masked-form route: its equal-length blocks are paired by position and the others are reported alone.
- It omits the "(M become NaN)" count that the listing prints (l. 359).
- Add both.

### Checked and found correct

- **The preview is reproduced exactly.** `kit/preview26.py` with `preview_cfg.json`, run into scratch, reproduces the committed preview byte for byte (`agentT5/prev/`). Its JSON gives:
  - `df_same` true for B10 and B15;
  - counts 126 and 644;
  - 37 steps, of which 2 stopped;
  - 40 changed files, none untraced;
  - 24 flagged rows, 11 of them changed.
- **Part 1's title and introduction** are accurate.
- **B10 and B15 sections:**
  - B10 l. 63–73 and B15 l. 34–40 in O2 equal d108d66's committed lines exactly.
  - The listed changes match R2.
  - 126 = 115 + 6 + 5, and 644 is the sum of the 10 site rows.
- **Part 1's list is complete.** A search of all 40 changed text outputs finds every line that O2 prints as d108d66 committed it, both exactly and within 1e-9. The only such lines are the null's log, B10 l. 63–64, B15 l. 36–40 and 42, B23 and B5, plus two coincidental B14 lines. Nothing is missing from part 1.
- **Fig 3 (c):** l. 269–271 and 301 are correct in both script versions. The rate goes −0.390 → −0.387, and the caption and legend print −0.39 either way. The figure step stops before Fig 3.
- **Table 3 note:** rows 6–11 have brackets 12, 16, 13, 20, 19, 12, 16, 6 and 5, so 2,980 to 2,995 pairs. The caption holds "3,000 pairs … ± SE over pairs".
- **S19 (a1):** the ratios are 1.41 and 1.49.
- **The five S3 quotations:** each old text is on its line once, each new text equals R2 l. 36–40, and each old text equals O2's.
- **Row wording:** `check_numbers.py` numbers rows from 2, the CSV has one comment line and no multi-line records, so row = file line − 1. I verified this on 7 rows.
- **Part 3 introduction and counts:**
  - The synthetic `.mat` has ts_gsr and ts_demean, each 14 × 2 of 116 × 840, plus FDlong, the ratings and the rotations.
  - O's script is d108d66's section 6 without B17 and B17b.
  - R's runner differs from commit A's only in how it writes the CSV and in the `--from` checks. Its step scripts equal commit A's.
  - `rt5_v5.csv` and `rt5_v6.csv` have the same rows but for one duration.
  - The files split as 337 = 254 identical + 43 agreeing + 40 changed.
  - B21's 50 failed checks are identical in both runs except the two C1 checks.
  - In the final run, B13's and the figure step's logs end without error.
- **B26 entry:**
  - B17b's 8 matrices are all in the solves (replay `agentT5/b17b_cal.py`: BMEAN 4, QSD 2, DELTA 2, checks 0, over 34 calls).
  - B23's eight conditions are right.
  - B15's 4 are in the bmean search. The residual changes are at most 0.0001 and the responses at most 0.00027.
  - The paragraph on the run matches the runner (the first write before the loop, `write_atomic`, the gap check, "interrupted after", the re-run head).
- **Revision entry:**
  - Item 7's wording is as proposed.
  - Item 10: C03 and E13 are main text, D02 is S1 Text and E12 is the README; the counts 10 and 8 are right.
  - Item 11: all 19 sha256 values match the committed files.
- **Other files:**
  - The root README sentence is complete.
  - CLAUDE.md's count is right: 4 + 2 + 2 + 2 = 10.
  - Disposition findings2_text 3 lists 18 quotations, the same as the preview.
  - findings2_text 26 is right: 6,996 → 6,994 words (E09 and C03).
  - The findings4_code section matches the runner, `vs/` and `check32.py`.
- **B25 and the fill:**
  - B25's docstring holds: 24,000 = 8 × 3 × 1,000, and the self-test printed 11.1 ms.
  - The verbatim copy is now at l. 146–171 and equals its source.
  - `b25_fill.py` ids run G01–G16 (and G05L); only the ids changed.
- **Build checks:**
  - The JSON (189 entries) applied to d108d66 reproduces every changed file of tree2 byte for byte.
  - `wc.py` gives 6,994/6,874, equal to `wc.out`.
  - `check_numbers` gives "rows 1183, data rows 666, flagged 12", equal to `check_numbers.out`; `check_cells` 0; `tablecheck` 0.
  - tree2 equals `work32A/tree2`.

Scratch files are in `…/audit5/agentT5/`:
- `b15pairs.py`, `b17b_cal.py` (with their `.out`)
- `datafree.py`, `datafree2.py`
- `listing.py`
- `prev/`, `rebuild/`, `review_readme/`
