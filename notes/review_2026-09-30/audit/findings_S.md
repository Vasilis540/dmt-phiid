*Copy for the repository: e-mail addresses are replaced by what they identify, except the repository's published contact address.*

## Audit S of HEAD 4472b1f against 31f1153: findings

I checked everything read-only. My scratch files are in `SP/audS/`. I removed the two worktrees I added, and `sim2` is back as I found it: the same `git status`, and the uncommitted working-tree `figures_check.py` was not touched. The `notes/__pycache__` folder in `sim2` dates from 01:03:28, before my session, so it is not mine.

The record entries hold up against the evidence, with no wrong numbers. There is **one error**: files the review folder names are missing from it. The rest are inaccuracies and wording.

### 1. Error: `notes/review_2026-09-30/README.md`:42–47 names six files that are not in the commit, and leaves out one that is
- **Statement:** "`checks/` — the checks of the revised text … (`check_numbers.out`, `check_cells.out`, `tablecheck.out`, `wc.out`) and the output of applying the replacements (`apply.out`) … and `figures.out`, the figure script run on the revised tree in the planning session's environment."
- **Evidence:**
  - `git ls-tree -r --name-only HEAD notes/review_2026-09-30/checks/` lists only `conversions_b26.py`/`.out`, `derived_r17_b26.out`, `partial_b26.py`/`.out` and `figures_check.py`. The six named files are not there.
  - `figures_check.py` is in the folder but the README never names it.
- **The same gap makes these statements untrue too:**
  - `manuscript/analysis_record.md`:8176 ("…, their checks and the audits are in `notes/review_2026-09-30/`")
  - `analysis_record.md`:8452–8453 ("the checks of the revised text and the recomputed derived values (`checks/`)")
  - `README.md`:71 and `CLAUDE.md`:527 ("the checks' outputs")
  - `dispositions.md`:57 (R2: "this folder holds the files under the names the texts give")
- **Fix:** commit the six files into `checks/`. My runs give their contents:
  - `check_numbers.out`: "rows 1197, data rows 670, flagged 12", all 12 SIGN DIFFERS
  - `check_cells.out`: "flagged 0"
  - `tablecheck.out`: "rows with a wrong cell count: 0"
  - `wc.out`: "total with headings 6998 without 6878"
  - `apply.out`: "all 253 entries applied" (mine is at `SP/audS/apply.out`)
  - `figures.out`: the output of `figures_check.py`
- **README text:** replace the last clause of the `checks/` item with: "…; and `figures_check.py`, which compares the figures and captions the figure script writes with the committed ones under the conditions of the record's entry on Fig 5's caption, with its output on the revised tree in the planning session's environment (`figures.out`)."

### 2. Inaccuracy: `notes/review_2026-09-30/checks/figures_check.py` at HEAD (lines 42, 57–66)
- **What is wrong:**
  - The PDF test masks only the date strings.
  - When the timezone suffix has a different length ("Z" against "+03'00'"), the xref offsets and `startxref` move with it. The test then reports "DIFFERS beyond its dates" for PDFs that differ only in their date.
  - The globs also take in the superseded `fig1_v2_atoms_mmi_ccs.{png,pdf}`, which the script does not write.
  - The PDFs carry no `/ModDate`. Only the creation date differs.
- **Evidence:**
  - I ran HEAD's checker from `sim2`'s root against the working tree's test-run figures. All six PDFs came out "DIFFERS beyond its dates".
  - With the xref table and `startxref` masked, all six are equal.
  - The PNGs: five identical, Fig 4's 70 pixels different (largest channel difference 1), as the record says.
- **Effect:** on V.S.'s machine (EEST, same date length) the check would work. It fails in any other timezone.
- **Fix:** commit the working tree's uncommitted version before the text commit. It adds a `NAMES` tuple of the six figures, and `masked()`, which applies `DATES.sub`, then `re.sub(rb"\nxref\n.*?\ntrailer", b"\nxref trailer", p, flags=re.S)`, then `re.sub(rb"startxref\n\d+", b"startxref", p)`.

### 3. Inaccuracy: `checks/conversions_b26.py`:88–89 does not print enough digits to back "+0.00886"
- **What is wrong:** the script prints the excess at 7 decimals ("+0.0088650"). Rounded half-up to five decimals that gives +0.00887, not the text's +0.00886. Yet the record (`analysis_record.md`:8303–8304, "computed at full precision") and `dispositions.md`:25–26 (T1) point to this output.
- **Evidence:** the full value is 0.0115342293 − 0.0026692400 = 0.0088649893, so +0.00886 in the text is correct.
- **Fix:** use `{RD:+.10f}`, `{E17:+.10f}` and `{EXC:+.10f}`, then regenerate the `.out`. It will read "+0.0115342293 … +0.0026692400; the excess +0.0088649893".

### 4. Inaccuracy (item 6, masking): an e-mail address remains in two files
- **`claims/reviews/fifth_check.md`:55** has the al857 address, although the same copy replaces Váša's address.
  - **Fix:** "- al857 is Andrea Luppi's Cambridge ID (the address on Luppi 2025, p. 1), so the released file is Luppi's copy."
- **`b26/b26_commit.sh`:9, 244 (twice) and 283** carry sampalisvasilis@gmail.com.
  - It is already public: `CITATION.cff`:8, `README.md`:212, `draft_v2.md`:9 and every commit's author line.
  - **Fix:** either mask it as «e-mail» and add to the README's `b26/` item "; in `b26_commit.sh` the committer's e-mail address is masked", or state there that it is the repository's published contact address.

### 5. Inaccuracy (minor): `audit/findings_R.md`:42 still has two scratch paths
- **What is wrong:** "`scratchpad/audR/simcopy`, with `scratchpad/v312`" was not shortened, although the copy's header says scratch paths are shortened to SP/.
- **Fix:** "`SP/audR/simcopy`, with `SP/v312`".

### 6. Inaccuracy (minor): `analysis_record.md`:8211
- **Statement:** "every commit an output names is d5a65bd".
- **Evidence:**
  - The evidence checks a narrower thing: "every git SHA an output gains is d5a65bd".
  - Two of the 99 files name other identifiers in fixed text: `crosslag_deviation_tables.md`:3 ("reported at 152cc6d") and `review_computations_2026-09-14.md`:4 ("phyid 6c5f2e9").
- **Fix:** "every commit an output gained is d5a65bd, none `-dirty`".

### 7. Wording: `analysis_record.md`:8201–8202
- **Statement:** "logind's and the kernel's journals hold no lid, suspend or power-off event".
- **Evidence:** the kernel filter (`b26_evidence.sh`:122–123) looks for OOM kills, suspend, hibernation and throttling, not lid or power-off events. The summary items say so.
- **Fix:** "logind's journal holds no lid, suspend or power-off event and the kernel's no out-of-memory kill or suspend while the run ran".

### 8. Wording: `analysis_record.md`:8190–8195
- **What is wrong:** "gathered the unit's log and journal … (`notes/review_2026-09-30/b26/`, with the three scripts)". The unit's log (`b26_run_unit.log`) is not in `b26/`. I checked that it equals `positive_definite_run.log` plus the line "=== unit exit 0".
- **Fix:** add "; the unit's log is `positive_definite_run.log` with its last line, `=== unit exit 0`, which `evidence.txt` quotes" inside the parenthesis.

### 9. Wording: `analysis_record.md`:8265
- **What is wrong:** "its four `diag_series` arrays". These are four files, each with four changed arrays (`b26_changes.txt`).
- **Fix:** "its four `diag_series` files".

### 10. Wording: `analysis_record.md`:8426
- **What is wrong:** "It gives B25's three runs (514 s, 482 s and the re-run's 486 s)". `run_all.sh`:17–18 gives "about 8 min (482–514 s in its three runs…)", a range, not the three times.
- **Fix:** "It gives the range of B25's three runs, 482–514 s (514 s, 482 s and the re-run's 486 s), in place of…".

### 11. Wording: `dispositions.md`:113–114 (Q9)
- **What is wrong:** "both headers say … the preprint in its version of 10 January 2026". Only partB5's header (Q34b) says this; S20's source note (`supplementary.md`:1658, Q34a) does not.
- **Fix:** "…take their page numbers from that check; partB5's header adds that the preprint was read in its version of 10 January 2026, which S20 Table states in Table B, item 3."

### 12. Wording: `dispositions.md`:129
- **What is wrong:** "(claims 27, 100, 104, 150 and 202 of the check)". These are the check's sentence numbers (field n); item R17 (:81) calls them sentences.
- **Fix:** "(sentences 27, 100, 104, 150 and 202 of the check)", and "Sentence 104/150/202" in the same paragraph.

### 13. Wording: the copies' header notes do not list every edit
- `findings_T`, `findings_R` and `findings_Q` drop the original's opening sentence about where the report could not be saved.
- `b26_rule_audit.md` drops "JBL".
- **Fix:** for example, "…shortened to SP/; the opening sentence on where the report could not be saved is left out" and "…; the Bluetooth device's brand is left out".

**Optional:** S19 Table Part B (`supplementary.md`:1654) still sources Results 4's Fieller interval to the 24 Sep `derived_r17.out`. The value is identical, and the numbers table now cites `derived_r17_b26.out`.

## Check runs on a clean HEAD checkout
- **`check_numbers.py`:** rows 1197, data rows 670, flagged 12, all "SIGN DIFFERS" (rows 10, 90, 93, 468, 500, 506, 633, 635, 664, 677, 678, 1055).
- **`check_cells.py`:** flagged 0.
- **`tablecheck.py`:** 0 bad rows in `draft_v2`, S1–S5, `supplementary`, `partB5_literature_v2` and `captions_v2`.
- **`wc.py`:** 6998 / 6878 at HEAD and at d5a65bd; 6994 / 6874 at 820cacd.
- **JSON replay:** all 253 entries apply on 31f1153 and reproduce HEAD's 14 files byte for byte.
- **`conversions_b26.py` and `partial_b26.py`:** output identical to the committed `.out` apart from the git line. At d5a65bd, `partial_b26` gives the third review's values exactly.

## Verified correct
- **Record, append-only:** 31f1153's record is an exact byte prefix of HEAD's; the diff is 282 lines added, 0 deleted. The longest new non-heading line is 120 characters; two headings are 122.
- **Run and evidence:**
  - Times 13:04:14–16:49:46 EEST and 225 min; 39 steps, all exit 0, 13,529 s.
  - Versions; commits 820cacd→d5a65bd change no script the run ran.
  - Heartbeat: 45 lines, 17 with the charger disconnected (14:09–15:29), battery 95→46 %, largest gap 301 s. B17 and B17b span the disconnection.
  - Restart: boot −1 ends 21:42:25; LoadState not-found.
  - CPU: "1d 8h 38.653s" is about 32 h. nogit is at `review_checks.py`:133 and log line 70 (run log line 894).
  - Checks 1,025/22/63/10; the expectations print as held.
- **Counts:** 473,262,025, 42,681, 215,276,476, 12,889; B4 4/4/1,617/1,661; B16 10,817/15,776; B5, null, B23, B17, B17b, B24; B15 1/0/33/81/88 and 1/11/36/91/120. All 36 site rows (count, range, mean) match the CSV.
- **Rule (i):** every per-file count matches `b26_changes.txt`; the 46 files differ only in SHA and times; B19's grouping and the B22 2.22e-16 line are as stated.
- **Rule (ii):** the 14 main-text numbers, verdict ratios 1.41/1.49/1.32/1.34, derived values, and the conversion and partial numbers at printed precision.
- **Rule (iii):** 14/7/21 per id (B03 +6, B04 +4, B06 +4; Q02 +4, Q04 +5, Q05 +4, Q06 −7, Q07 +3, L05 −2; L01 −8, L02 −6, L04 −7).
- **`run_all.sh` timing comment:** every figure recomputed from `run_all_final.log` matches (19,019 s; 9,540 s; 2,638, 2,039 and 1,263 s; 8 min 38 s; per-step times).
- **Claims:** DATA equals v2 except the notes of si 94 and 96 (displayed as sentences 100/102); code outside DATA is identical. `claims.csv` has 303 rows that agree field by field with DATA (counts 248/36/19 and 266/5/1/2/29; 43 works; 45 PDFs).
- **Other text changes:** README.md, CLAUDE.md, S5 §4–6, Data and code availability, "every cited paper", the numbers table head note (22 added, 8 deleted, 14 changed, 16 locators, 93 contexts) and its three `derived_r17_b26` rows.
- **Dispositions:** every T, R, Q, (a), (b), rule-audit and fifth-check item is covered, and all are true of HEAD apart from 1, 3, 11 and 12 above.
- **Copies:** the `b26/` copies equal the evidence apart from the «host» and device masks; the three scripts equal the delivered ones. No host or device name remains anywhere in the folder, and apart from the PDF header stamps no quotation of a cited work over about five words remains outside our own text.
- **Not available to me:** B25's re-run evidence. I verified only the committed rows' sha256 (bb888d45…).

Nothing to save to memory.
