# B26's run and the claim-by-claim check of 29–30 September 2026

The review folder of the revision that reports B26's run, made by V.S. at d5a65bd on 29 September 2026, and the
claim-by-claim check of the text at d5a65bd made on 29–30 September 2026. Record: "The matrices that are not positive
definite (B26): outcome", "The claim-by-claim check of 29–30 September 2026 and its corrections", "B25: the re-run by a
separate session", "Fig 5's caption, B3's table header and `run_all.sh`'s timing comment" and "The audits of this
revision and its review folder".

## Files

- `b26/` — B26's evidence, as V.S.'s run of `b26_evidence.sh` gathered it on 30 September 2026 at 08:31 UTC, after a
  restart of the machine (the record's entry says what that changed): `evidence.txt`, the summary, with every check and
  its result; `b26_changes.txt`, every change the run made to the committed outputs, line by line and cell by cell
  (`notes/review_2026-09-28/checks/b26_changes.py`), and `diffs.txt`, the same as `git diff`; the outputs of the final
  run's three comparison scripts (`6_committed_compare.txt`, `8_binary_compare.txt`, `10_logs_figures_compare.txt`) and
  their exit statuses (`*.exit`); `b26_heartbeat.log`, the line the unit wrote every five minutes; `outputs.sha256`, the
  sha256 of the 99 files the run changed or created, which `b26_commit.sh` checked before it committed them;
  `env_after.txt`, `status_before.txt`, `b26_prestatus.txt`, `status_after.txt`, `staged.txt`, `windows.txt` (the
  attempts: one), `boots.txt`, `machine.txt`, `unit_runb26.txt` (systemd's state of the unit, which after the restart
  holds no more than that it is not loaded), `unit_journal.txt` and `logind.txt` (the unit's journal and logind's, the
  machine's name and a Bluetooth device's name masked), `kernel.txt` and `dpkg_during_run.txt` (both empty: no event).
  With them the three scripts of the run, by the planning session: `b26_start.sh`, which started the unit,
  `b26_evidence.sh`, which gathered the evidence, and `b26_commit.sh`, which committed the outputs as the run wrote them
  (the committer's address in it is the repository's published contact address). The run's own log and tables are
  `notes/review_results/partB/positive_definite_run.log`, `positive_definite.csv` and `positive_definite_tables.md`; the
  unit's log was the run's log with a last line, `=== unit exit 0`, which `evidence.txt` quotes.
- `claims/` — the claim-by-claim check. `make_claims_check.py`, run on a computer that holds the cited works' PDFs in
  `external/papers/`, cuts the passages of each work that bear on each claim from those PDFs and writes
  `external/claims_check/index.html`, the text sentence by sentence with each claim's passages, their pages, the verdict
  and the firsthand status; the program holds our text, the verdicts and the positions of the passages on the pages but
  no text of any cited work, and nothing it writes enters the repository. `claims.csv` lists the same records, one row
  per claim, without the passages. `reviews/` holds the reports of the five sessions that checked the records against
  the PDFs (`review_A.md` to `review_D.md`, and `fifth_check.md` on the records of the files added on 30 September);
  in these copies quotations of the cited works longer than a few words are replaced by a bracketed description with
  their page, and the detailed findings files they name, which quote the works, are not in the repository.
- `revision/text_replacements_2026-09-30.json` — every replacement of the commit that follows the outputs commit,
  applied in order with `notes/review_2026-09-25/revision/apply_replacements.py`: B01–B13, B20–B66, B24b and B57b (the
  numbers B26's run changed and the statements of its rule), Q01–Q34 and L01–L05 but L03 (the corrections of the
  claim-by-claim check and the cuts that keep the main text within 7,000 words), S01–S07 (the figure script, B3's table
  header and `run_all.sh`), R01 (the record's entries), K01–K19 (the bookkeeping), N01 (the numbers table) and C01–C08
  (CLAUDE.md). The record's entries carry «ENTRY_TIME»: the writer's session put the date and time of the commit into
  them after applying the replacements.
- `checks/` — the checks of the revised text, run with the scripts of `notes/review_2026-09-25/checks/`
  (`check_numbers.out`, `check_cells.out`, `tablecheck.out`, `wc.out`) and the output of applying the replacements
  (`apply.out`); the values derived from outputs that B26's run changed, computed again from its outputs:
  `derived_r17_b26.out` (`notes/review_2026-09-24/checks/derived_r17.py` run again), `partial_b26.py` and `.out` (the
  partial correlations of S3 Text §6) and `conversions_b26.py` and `.out` (the conversions of S3 Text §6, at full
  precision); and `figures_check.py`, which compares the figures and captions the figure script writes with the
  committed ones under the conditions of the record's entry on Fig 5's caption, with its output on the revised tree in
  the planning session's environment (`figures.out`).
- `audit/` — the audits by separate sessions: `b26_rule_audit.md`, B26's run against the rule of its pre-run entry, with
  `b15_null_replay.py` and `.out`, which replay B15's null section to count the pair-windows it leaves out; then the
  audits of the prepared revision, `findings_T.md` (its numbers, the exclusion statements, the numbers table and the
  word count), `findings_R.md` (the record's entries and the bookkeeping) and `findings_Q.md` (the corrections of the
  claim-by-claim check, against the PDFs; quotations of the cited works replaced as in `claims/reviews/`), and
  `findings_S.md`, of the revision as corrected after them; their line numbers are those of the build they audited, and
  their commits those of the copy of the repository that held it, in which 31f1153, the commit of B26's outputs, holds
  the same files as 3ce5707, and 6ae1cfa and 4472b1f the revision as it then stood; and what was done with each finding
  (`dispositions.md`).
