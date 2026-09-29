## Fourth-round text audit of commit A (`…/b32/audit4/tree2`, kit `…/b32/audit4/kit`): report

Paths: `tree2` = `…/b32/audit4/tree2`, `kit` = `…/b32/audit4/kit`, `modF` = `…/b32/codetest/modF`. I changed nothing outside `…/audit4/agentT4/`. The kit's `__pycache__/code32.cpython-312.pyc`, created at 22:23, is not mine. I did not report «ENTRY_TIME», «SYNTHETIC», or the preview's pending section 3.

Summary: 22 of the 23 third-round text findings are fixed; 16 is pending and not reported. There is one new major problem: a data-free computation whose quoted values change was missed, so finding 3's corrected README sentence is still incomplete. The other findings are minor.

### Findings, most severe first

**1. MAJOR — The correction also changes outputs of two steps that read the data, independently of the data. S3 Text quotes one of them. The preview, the README and B26's entry all omit them.**
- **Where:**
  - `tree2/manuscript/si/S3_Text.md` l. 276–280. They transcribe `notes/review_results/partB/directed_crosslag_tables.md` l. 36–40 (run log l. 65–69; summary l. 42/71).
  - `checks/b26_preview.md` §2, "Quotations" (l. 2113–2127).
  - `README.md` l. 53–57.
  - Record l. 7931–7936 (item (i)) and l. 7950 ("the changes reach Table 3, S13, S18 and S19 Tables and S3 Text").
  - Kit: `preview_cfg.json` (`si_quotes`) and `b26_preview.json`.
- **Evidence, B15:** `notes/partB15_directed_crosslag.py` l. 150–233 is a finite-sample null on synthetic series (no data).
  - I replayed it (`agentT4/b15null_lines.py`, 2.5 min). With d108d66's `rev_phiid_fast` it reproduces S3 l. 276–280 digit for digit.
  - With commit A's code every line changes. The substituted matrix fails in 1, 0, 33, 81 and 88 of the 3,000 pairs; 1, 11, 36, 91 and 120 pairs are left out of the responses.
  - l. 276: residual −0.03535 → −0.03534; responses "−0.03484, −0.00009, −0.03575" → "−0.03484, −0.00008, −0.03574".
  - l. 277: responses "−0.04954, −0.01159, −0.06552" → "−0.04955, −0.01157, −0.06553" (residual unchanged).
  - l. 278: "−0.07353 (−9.52 %)" → "−0.07343 (−9.51 %)"; responses → "−0.01310, −0.05837, −0.07372".
  - l. 279: "−0.07253 (−9.22 %)" → "−0.07245 (−9.21 %)"; responses → "−0.01880, −0.05141, −0.07290".
  - l. 280: "−0.06842 (−8.47 %)" → "−0.06847 (−8.47 %)"; responses → "−0.02712, −0.03945, −0.06955".
- **Evidence, B10:** its §B regenerates the null with the null's own draws (`partB10_crosslag_deviation.py` l. 340–353).
  - Its committed l. 64 of `crosslag_deviation_tables.md` (run log l. 43) equals the null's "−0.0886 (−8.52 %)". It will print −0.0885 (−8.51 %); this is not a rewording.
  - B10's site rows will presumably show the null's 126 failing matrices.
- **Evidence, Fig 3:** `scripts/15_figures_v2.py` l. 269–271 and 301 draw B23's (i) rate (−0.390 → −0.387) in panel (c). The caption's printed −0.39 is unchanged.
- **Consequence:** rule (i) still traces these differences to counted matrices, so it is not a fault at run time. But:
  - The README sentence ("writes the outputs of B5, the null, B23, B17 and B17b …, the lines the correction rewords, and any output that the data's matrices change") is false for these outputs.
  - A supporting-information quotation of a changed output is still missing from the preview.
- **Fix:**
  - (a) Add a preview part that replays the data-free sections of B10 and B15, as `b26_null_sections.py` does for the null. Add S3 Text l. 276–280, with the new texts above, to "Quotations".
  - (b) README: "…writes the outputs of B5, the null, B23, B17 and B17b, the data-free null sections of B10 and B15, and Fig 3 (c), which draws B23's AR(1) rate, with their corrected values (…)…".
  - (c) Record item (i): add that B10 (its regenerated null at W = 30: −0.0885, −8.51 %) and B15 (its lead–lag null, whose five lines S3 Text §6 transcribes and all of which change) evaluate synthetic series, and that their site rows include these matrices. At l. 7950 add "Fig 3 (c)".
  - (d) Add S3 l. 276–280 to disposition findings2_text 3.

**2. MINOR — Two changed sentences of B26's entry are ambiguous or inexact.**
- **B17b (record l. 7956–7959):** "…15 of … its windows (its line 166), and 8 of … the null's function it imports (line 69), all in the draws that solve its generator's parameters, which use a and |q| only and reach no output; the code before had given them sts from +0.8434 to +2.7796."
  - "all" can be read as all 23. The 15 at line 166 do reach output (0.0026686 → 0.0026692).
  - "them" does mean all 23: the range spans both sites.
  - The solves also use a_x − a_y: `cal_stats` l. 122; the DELTA solve at l. 129.
  - Write: "…and 8 of the 5,100,000 of the null's function it imports (line 69), these 8 in the calibration draws that solve its generator's parameters, which use the windows' a, |q| and a_x − a_y and discard the substituted sts; the code before had given the 23 sts from +0.8434 to +2.7796."
  - Same wording in disposition findings3_text 19.
- **B23 (l. 7946):** "8 to 28 in each of (i) and (a1)–(a4)" holds per condition (8 conditions), not per label ((a1) totals 47). Write "in each of the eight conditions of (i) and (a1)–(a4)".

**3. MINOR — Four disposition statements in `dispositions.md` are inexact.**
- findings2_text 9 (l. 255–256) still says "in the section to which Methods already points where it defines the substituted estimate", which findings3_text 17 found inexact. The header (l. 16–17) says earlier dispositions give the state of this commit. Write "at the start of §6, on the residual of the substituted estimate (`findings3_text.md` 17)".
- findings2_text 26 (l. 300–303): with C03 as the third round shortened it, these edits are now two words fewer, not "(one word fewer)". Line 302 is also 169 characters, unwrapped (the file wraps at 120).
- findings2_text 3 (l. 238): "S3 Text l. 241, four, 347 and 349" should be "S3 Text l. 241 (four), 347 and 349".
- findings3_text 10 (l. 390): "printed 10 to 24 ms in the builds" is not what the builds printed.
  - The committed self-tests of the three builds printed 23.7, 18.8 and 15.8 ms.
  - 9.8 and 12.0 ms appear only in audit runs (`b32/audit/aud/b25_selftest.out`, `scratch_b25/selftest.log`).
  - Write "printed 16 to 24 ms in the three builds, 10 and 12 ms in audit runs on the same machine".

**4. MINOR — Preview l. 2116, S19 (a1): the proposed "(\"missed, 1.4 and 1.5 times the predictions\")" keeps quotation marks around words no entry says.** S19's quoted phrases are the outcome entries' verdicts, and B23's entry says "about half as large again". Write `("missed"; 1.4 and 1.5 times the predictions)`, or have B26's outcome entry state it in those words.

**5. MINOR — Preview l. 2131 (kit `preview_cfg.json` captions): "rows 6–11's substituted sts, residual and D" is inexact.** Table 3 prints no substituted-sts or D column; only its W = 60 residual column is affected. Write "rows 6–11's residual changes at W = 60 are now means over the pairs whose substituted matrices are positive definite in all 14 windows (2,980 to 2,995 of the 3,000)…".

**6. MINOR — Record item 7 (l. 7717–7721) says the condensations "take out of the body what the figure captions and the supporting information hold".** C04's statement (when the statistic was fixed) is held by Pre-registration and deviations, which is in the body. Write "what the figure captions, the supporting information or another subsection hold".

**7. MINOR — Item 10 (l. 7758–7764) records no text change of the third round.** Nothing in the record names E13 (a main-text change in Data and code availability) or E12 (README "at 77af7aa"). The second round's sentence lists its edits by id. Add "; and wording of the main text, S1 Text and the README (C03, D02, E12, E13)".

**8. MINOR — `kit/disp3.py` does not reproduce the committed `dispositions.md`.** Run on a copy of `dispositions.md.v2`, its output differs from tree2's in three passages:
- the header ("…and names the later finding");
- findings3_text 10 ("has printed 10 to 24 ms for the longest");
- findings3_code 4 ("none failed but the two…").

The committed file was edited after the script ran. Update the script.

**9. MINOR — `revision/b25_fill.py` l. 360–368: removing G14 leaves the ids G01–G13, G15–G17.** findings2_text 20 corrected the same kind of gap for the K ids. Renumber G15–G17 to G14–G16.

**10. MINOR — Preview l. 2074: "row of commit A's table" is `check_numbers.py`'s index, which is the file line minus 1.** Row 547 is line 548 of `main_text_numbers.csv`; line 547 is an "AR(1)" label row. Say "(row as `check_numbers.py` numbers it: file line − 1)", or give file lines.

### Checked and found correct

- **Third-round text findings:**
  - Fixed: 1, 2, 4, 5, 6, 7, 8, 9, 11, 12, 14, 15, 17, 18, 21, 22.
  - Fixed, with a remaining issue: 3 (see 1), 10 (see 3), 13 (see 6), 19 (see 2), 20 (see 5), 23 (see 4).
  - Not checked (pending by design): 16.
- **Item 11:** all 17 sha256 values match. The JSON equals the applied bundle (189 entries). Since round 3 it changed D02, C03, E12, E13, F17, F26, N01, N10, N12, K04, K10 and K13–K23. The committed audit reports equal the originals, and `dispositions.md` equals `b32/audit/dispositions.md`. tree2 equals `work32A/tree2`.
- **Word count:**
  - Applying the 28 main-text edits to d108d66's draft reproduces tree2's draft byte for byte.
  - By `wc.py`: the non-condensation edits give +61 (D01 −1 = +23 − 24); C01 −30, C02 −23, C03 +7, C04 −18. Total 6,994/6,874, as in the record, README, CLAUDE.md, `wc.out` and dispositions.
- **Numbers table:** 1,183 rows. Against d108d66 there are 24 changed contexts among matched rows (the seed row included), plus the derived "+0.05" row; this matches the build's 24.
  - E13's three rows were recomputed and are found once in the text.
  - The Discussion rows around C03 are unchanged and found.
  - Occurrences are unaffected.
  - `check_numbers` 12 (sign rows), `check_cells` 0, `tablecheck` 0.
- **Preview listings:** all 14 file listings equal the current `b26_changes.py --dirs` output exactly (`agentT4/changes_dirs.out`). CSV cells are given as file lines (l. 171/180, as the numbers table locates them).
- **Preview §2 numbers section:** reproduced with commit A's text and table plus modF's outputs ("rows 1183, data rows 666, flagged 36"). The 24 rows, held values, new values and the 11 changes are as listed; the baseline `checks/check_numbers.out` reads "flagged 12".
- **Preview quotations:** all 13 are on their stated lines, once each, and every new text matches modF.
  - B17 ratios by replicate means: −17.82, −23.61, −22.15, −24.85 (before −17.04, −23.57, −22.22, −24.63). From the printed rows: −17.40, −23.74, −22.11, −25.06. The replicate-means method is verification N2's.
  - S19 (a1) ratios 1.41 and 1.49 (before 1.48, 1.59); (a2) 1.32 and 1.34; (a4) within 2 SE of −0.0052 ± 0.0016 and −0.0056 ± 0.0018.
  - Preview l. 7 ("no site here had more than nine") holds.
- **B26 entry against sources:**
  - B23 by condition, from the ordinals in `F_counts`: 16; 8, 19, 28, 9, 25, 12, 17, 16; (a5) 8, 8, 6. sts from −1.2746 to +3.3136; brackets 5–20; Table 3 rows 6–11 cover 2,980–2,995 pairs.
  - B17: p-values change by up to 0.016 ((iii) 0.521 → 0.505), shares by 0.02, DiDs and SEs by 0.0001. (i) 0.0049320 against 0.0048988.
  - B17b: 15 + 8 of 60,260,000; the 8 all come from `cal_stats` (the only caller of `residual`); two p-values move in the third decimal; 0.0026692 against 0.0026686.
  - The runner's docstring and tables agree with the entry: every bad call kept, `bad_calls_n`, versions in the header, per-step writing, `--from` after an interrupted run.
  - The step list B4, B4's residual source, B10, B14, B15, B19, B22 is exactly the set of `ar1_corr` callers on the data.
  - Rule (i)'s rewording list is complete against F01–F52.
  - Rule (i)'s comparisons match the final run's item 5, and rule (iii) names the heading of S3 Text §6.
- **Other text edits:**
  - P48's difference against `proposals.json`; E12 applied.
  - D02: every named package is pinned in the lock file (phyid by commit).
  - K13: the main text carries no B labels. `b25_fill` anchors G02, G04, G07, G08, G10, G13 and G15–G17 each occur once.
  - B25's "not differentiable" and "1 % (+ 10⁻⁶)" agree with the code (l. 601; fill l. 137) and the entry. The self-test prints 15.8 ms, inside the docstring's 10–24.
  - The crosscheck CSV changed only in C072/C084 (",," removed).
  - The review README and CLAUDE.md sentences are accurate; "eight audits in three rounds" = 4 + 2 + 2.

Scratch files: `…/audit4/agentT4/` — `b15null_lines.py`, `b15null_check.py`, `wcsteps.py`, `changes_dirs.out`, `check_numbers_ovl.out`, `disp3_local.py` with `disp_input.md`, and `ovl/` (a symlinked overlay of tree2 with modF's outputs).
