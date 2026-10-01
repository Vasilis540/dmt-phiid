# The cold reads of 1 October 2026, the literature search of that day, and the run of B27, B28, B29 and B16c

The review folder of the commit that follows 24919ea: three cold reads of the paper and its supporting information
typeset from 24919ea by separate sessions of the AI system, the PubMed search V.S. ran on 1 October 2026, and the four
computations the reads asked for — B27, B28, B29 and B16c, added with their pre-run entries and run by V.S. on his
machine — with the replacements the commit applies. Record: "The cold reads of 1 October 2026", "The pre-injection gap
and the per-subject relations (B27): pre-run entry", "The per-subject slope under a pure autocorrelation change of the
data's heterogeneity (B28): pre-run entry", "The replaced volumes and the autocorrelation (B29): pre-run entry" and
"Prewhitening at fixed orders (B16c): pre-run entry". The text revision that answers the reads follows the run, in the
commit after the outputs, with the outcome entries and its own review folder.

## Files

- `reviews/` — the three reports, each with a header naming the read and otherwise as the session returned it:
  `read_A.md` (a researcher in partial information decomposition and ΦID, who reproduced the closed form from an
  implementation of its own), `read_B.md` (a statistician and fMRI time-series methodologist, who reproduced the
  inference numbers from the saved per-subject vectors) and `read_C.md` (a psychedelic-neuroimaging researcher reading
  with the data authors' perspective). Each read the typeset PDFs (main text 27 pages, supporting information 133 pages,
  with line numbers; typeset from the commit's markdown with pandoc and XeLaTeX, not in the repository) and found no
  number wrong; their page and line numbers are those of the PDFs. The scratch paths a report names were the reviewing
  session's own.
- `pubmed_search/` — `search_string.txt`, the PubMed string and how it was run; `pubmed_search.csv`, the 11 records as
  PubMed exported them (its BOM and line endings kept); `screening.md`, each record screened against the paper's
  inclusion criterion, with the two to be read in full in the next revision.
- `b27/` — the scripts of the run: `b27_start.sh`, which checks the conditions (the commit, the clean tree, the data
  clone, the pinned environment, the lid switch, the charger, the disk, no unit running) and starts the four scripts as
  the systemd unit `runb27` under a lock against sleep, idle, the lid switch and shutdown, with a heartbeat; and
  `b27_commit.sh`, which checks the unit's log and the 29 outputs (the twelve text files among them with the commit of
  the run in their headers) and commits them as the run wrote them, with the unit's log (`b27_unit.log`), the heartbeat
  (`b27_heartbeat.log`), the sha256 of the outputs (`outputs.sha256`) and a summary (`evidence.txt`), which that commit
  adds here.
- `revision/text_replacements_2026-10-01_cold_reads.json` — the replacements of this commit, applied in order with
  `notes/review_2026-09-25/revision/apply_replacements.py`: `S01` and `S02` (`run_all.sh`: the four `nstep` lines after
  B25's, and the timing comment), `R01` (the record's five entries), `C01`–`C05` (CLAUDE.md) and `K01`–`K02`
  (README.md). The record's entries carry «ENTRY_TIME»: the writer's session put the date and time of the commit into
  them after applying the replacements. The four scripts (`notes/partB27_baseline_gap.py`, `partB28_matched_slope.py`,
  `partB29_censoring.py`, `partB16c_prewhiten_fixed.py`) and this folder are the commit's new files.
- `audit/` — the audit of the prepared commit by a separate session, before it was committed (`findings.md`, 23
  findings on the entries, the scripts, the scripts of the run and the bookkeeping, every number of the entries
  recomputed from the committed arrays), and what was done with each (`dispositions.md`).
- `checks/` — the output of applying the replacements (`apply.out`), the parse of the four scripts and of `run_all.sh`
  (`scripts_check.out`), and the checks of the text, unchanged by this commit (`check_numbers.out`, `check_cells.out`,
  `tablecheck.out`, `wc.out`; the main text, the supporting information and the numbers table are not touched).
