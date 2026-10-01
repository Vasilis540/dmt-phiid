*Copy for the repository: paths of the planning session's scratch space are shortened to SP/, and the brand of a Bluetooth device is left out.*

**B26 audit: no faults. All six items PASS.** I checked the evidence myself rather than trusting evidence.txt. I extracted the committed versions of all 99 files at d5a65bd and compared them with /b36/out/ using my own text, cell, pickle, npz and image diffs. My results match b26_changes.txt exactly: 50 files changed, 46 differ only in bytes, 3 are new, and no line was added or removed in any file. I also rebuilt positive_definite_tables.md from the CSV using the runner's own `tables()` function, and it is identical.

**1. Run conditions: PASS**
- **Commit:**
  - The CSV's first line reads `# partB26_positive_definite.py; git=d5a65bd; run 29 Sep 2026 10:04 UTC; python 3.12.3, numpy 2.5.3`.
  - All 154 SHA strings in the outputs are d5a65bd, and none is `-dirty`.
  - Between 820cacd (the commit of the pre-run entry) and d5a65bd, the only script that changed is partB25_binarised.py, which B26 excludes. `run_all.sh`, `rev_phiid_fast.py` and the runner are unchanged, and the pre-run entry (record l. 7885–8049) was not edited.
- **Clean tree:** status_before.txt and b26_prestatus.txt are empty and nothing was staged. Independently, the runner refuses to start if `git status` shows anything but its own log (partB26_positive_definite.py l. 355–362), and it started.
- **Exit statuses:** all 39 CSV step rows show exit 0. The log has 39 step lines, no "STEP FAILED", "=== all done in 225 min" (l. 3377) and "=== unit exit 0" (l. 3512). positive_definite_run.log is byte-identical to the unit log minus its last line.
- **No interruption or re-run:** the first line carries no "partial", "interrupted after" or "re-run with --from". windows.txt shows one attempt.
- **Environment after:** python 3.12.3, numpy 2.5.3, scipy 1.18.1, matplotlib 3.11.1; `pip freeze` equals requirements.lock.txt.
- **During the run:**
  - The heartbeat logged every 300–301 s, with uptime going from 16,209 to 29,411 s, all in one boot (boot −1, 08:39–21:42 EEST).
  - systemd-inhibit blocked sleep, lid and shutdown.
  - logind.txt has only two "Watching system buttons" lines for a Bluetooth speaker. kernel.txt and dpkg_during_run.txt are empty. Peak memory was 945.5M with no swap.
- **DIFFERS, charger (b26_heartbeat.log l. 13–29):**
  - The charger was unplugged from about 14:05 to about 15:30 local time; the battery fell from 95 % to 46 %, then recharged.
  - This cannot affect outputs: nothing suspended or stalled, and the calculations are deterministic.
  - The only steps running then were B17 (13:32–14:42) and B17b (14:42–15:47). Both read no data, and their changes match the planning session's preview (b26_preview.md, computed on another machine) entry for entry. Their (i) means are 0.0049320 and 0.0026692, as predicted.
- **DIFFERS, 'nogit':** positive_definite_run.log l. 894 is review_checks.py's printout of a fixed string, "20-region sanity run (written 12 Sep 10:12, git=nogit)" (review_checks.py l. 133). The same line is l. 70 of the committed and regenerated review_checks.log. The log is a new file, so the evidence script counted it as gained. It has no effect on any output.
- **Side note:** in boots.txt, the current boot (30 Sep) shows a start time after its end, a clock correction after the run. It has no bearing on the run.

**2. Rule (i): PASS, no untraceable difference**
- The 46 byte-only files differ solely in SHA, date and elapsed-time tokens; I checked every masked token is an elapsed time.
- Every change in wording is one of the rewordings the pre-run entry lists. The two exceptions are data-driven: B21's zero-inclusion count (39 → 40) and one cell (yes → no), for "prewhiten arp residual ts_gsr W60 early".
- The only float noise is one B22 check line, "|difference| 0 → 2.22e-16".

Steps whose own counted matrices explain the change:
- **B4** (3,286, l. 75:24):
  - inference_rows_diag.csv (580 cells) and .pkl (48 rows): only the "diag predicted/residual" rows changed, no observed row.
  - The four diag_series npz files: pred, res, r2 and local_res changed in exactly the 3 / 331 / 4 / 291 windows whose calls held such matrices.
  - diag_tables.md: 19 lines.
- **B16** (26,593, all in the 'arp' calls 1–784): only the "prewhiten arp diag predicted/residual" rows of the CSV and pkl, plus 26 log lines and tables l. 29 and 80. The ar1 lines are unchanged.
- **B17:** 1,698 cells, all in the W60 rows of exactly the 350 replicates that held such matrices.
- **B17b:** 54 cells in exactly the 12 affected replicates. A 13th replicate had one only in window 5, which the DiD excludes, and did not change.
- **B14** (8): npz 'pred' changed in exactly the windows of calls #19, 277, 325, 440, 612, 679, 705; CSV 29 cells; one line.
- **B15** (644, all in its null section; none in the data calls from l. 111): the five null lines, the levels line and the two listed sentences. directed_crosslag.csv agrees.
- **B22** (22): 51 cells in exactly the 11 rows of the calls that held such matrices, plus 12 lines.
- **B23** (172): 70 cells in part (b) only, plus 13 + 13 lines, identical to the preview.
- **B5** (171): l. 18. **Null** (126): l. 6 and l. 17. **B10's null replay:** run log l. 43, tables l. 63–64. **B4's residual source** (8): 2 lines.

Steps with no counted matrices, whose change comes from an earlier changed output they read:
- **B19** (bca_intervals.csv 48 cells, exchange_rates 3 lines): reads inference_rows_diag.pkl.
- **B6** (ccs_pub_tables.md l. 86): reads inference_rows_diag.pkl.
- **B7** (splithalf.log and tables): reads diag_series.
- **B10** (crosslag_deviation.csv, 7 w60_residual cells): reads diag_series; the 7 rows are exactly the 7 runs with changed B4 W60 windows.
- **B21** (729 cells, 11 lines): reads the diag and prewhiten pickles and diag_series.
- **15_figures_v2:**
  - captions_v2.md l. 23: the Fig 5 p-values moved from 0.108 / 0.219 to 0.107 / 0.218, read from B21's table.
  - fig2 PDF: reads B14's npz; its PNG is identical.
  - fig3 PDF/PNG: reads the diag pickle and B23's rate.
  - fig5 PDF/PNG: reads diag_series.

**3. Predictions for the no-data steps: PASS, no mismatch**

| Step | Predicted | Found |
|---|---|---|
| B5 | 171 of 2,000; +0.000 to +4.585, mean +0.094, share 0.53 | exact |
| Null | 115 at W = 30, 11 in root searches, 126 of 10,010,000; W = 30 residual −0.0885 (−8.51 %); only the W = 30 line and last-line label change | exact |
| B23 | 172 of 4,336,546 (lines 200/201/202: 109/61/2) | exact |
| B23 by condition | 16 unperturbed; 8–28 per condition; 6–8 per (a5) | 16; 8–28; 8/8/6 |
| B23 other | old sts −1.2746 to +3.3136; brackets 5–20; Fig 3 rate −0.387 (caption still −0.39) | exact |
| B24 | 0 of 17,640,000; outputs unchanged | exact |
| B17 | 11,494 of 41,160,000; old sts −3.1618 to +5.8239 | exact |
| B17 values | (i) 0.0048988 → 0.0049320; p up to 0.016, shares up to 0.02, DiD/SE by 0.0001 | exact |
| B17b | 23 = 15 + 8; old sts +0.8434 to +2.7796; (i) 0.0026686 → 0.0026692; two p-values move in the 3rd decimal | exact |
| B10 | 126; W = 30 line −0.0885 (−8.51 %) | exact |
| B15 counts | 4 in root searches; substituted 1, 0, 33, 81, 88 | exact |
| B15 changes | each of the five lines changes; residuals up to 0.0001, responses up to 0.00027 | exact |
| B15 left out | 1, 11, 36, 91, 120 | exact (see below) |

The CSV can only show that B15's left-out counts for configurations (0) and (1) are 1 and 11. To check 36, 91 and 120, I re-ran B15's null section locally, read-only, from `SP/audit/b15_null_replay.py` (output in `b15_null_replay.out` beside it). It reproduced lines 36–40 character for character and gave 1, 11, 36, 91, 120. The repo tree was still clean afterwards.

The whole preview section 1 (B5, the null, B23, B17, B17b, B24) matches the run entry for entry.

**4. Rule (v), sample correlation matrices: PASS**
The PairPhiID path has 51 site rows and 215,276,476 matrices, of which 0 are not positive definite and 0 are non-finite. The smallest eigenvalue is 2.14e−4 (partB4_diagnostic.py:71:25). 214 are near-singular; they are reported, not excluded. There are no rows for any other path.

**5. B21's check against check_C1_residual_vs_null.log: PASS**
- inference_revision_tables.md l. 6 (and run log l. 11) reads "Checks: 1025 run, 0 failed"; rows l. 58–59 are "ok".
- ts_gsr: −0.0137326 against −0.01373 (difference 2.6e−6). ts_demean: +0.0007936 against +0.00079 (difference 3.6e−6). The tolerance is 5.1e−6.
- Both values are unchanged from the committed ones: the run-level sites (B4 l. 132, B10 l. 185) had no matrices that failed.
- No output contains "CHECK FAILED".

**6. B4's pair-windows without a substituted estimate: PASS**

| Variant | W | Line in diag_tables.md | Left out |
|---|---|---|---|
| ts_gsr | 60 | l. 6 | 4 of 2,569,560 |
| ts_gsr | 30 | l. 18 | 1,617 of 5,139,120 |
| ts_demean | 60 | l. 30 | 4 of 2,569,560 |
| ts_demean | 30 | l. 42 | 1,661 of 5,139,120 |

- These total 3,286, and the per-block sums from the CSV's call ordinals match exactly, as do the subject-1 bracket counts.
- **Whole-run pairs:** B4's run-level site (partB4_diagnostic.py:132:40) has 56 calls and 367,080 matrices, none failing (smallest eigenvalue 0.00403). No whole-run pair of the data lacks a substituted estimate.

My scratch comparison files are in `SP/audit/`. No files in the repo or the evidence were modified, and there is nothing to save to memory.
