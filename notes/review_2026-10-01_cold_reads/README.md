# The cold reads of 1 October 2026, the literature search of that day, the run of B27, B28, B29 and B16c, and the revision that answers the reads

The review folder of the commit that follows 24919ea: three cold reads of the paper and its supporting information
typeset from 24919ea by separate sessions of the AI system, the PubMed search V.S. ran on 1 October 2026, and the four
computations the reads asked for — B27, B28, B29 and B16c, added with their pre-run entries and run by V.S. on his
machine — with the replacements the commit applies. Record: "The cold reads of 1 October 2026", "The pre-injection gap
and the per-subject relations (B27): pre-run entry", "The per-subject slope under a pure autocorrelation change of the
data's heterogeneity (B28): pre-run entry", "The replaced volumes and the autocorrelation (B29): pre-run entry" and
"Prewhitening at fixed orders (B16c): pre-run entry". The run's evidence came with the outputs' commit (8bd189e:
`b27/b27_unit.log`, `b27_heartbeat.log`, `outputs.sha256`, `evidence.txt`), and the text revision that answers the
reads, with the four outcome entries, is the commit after it, whose files are listed in the second section below
(record, "B27, outcome" to "B16c, outcome" and "The revision of 1–2 October 2026: the cold reads applied").

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
  inclusion criterion, the two that were marked to assess read in full on 1 October 2026 (the file as the revision
  that answers the reads left it).
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

## The revision that answers the reads (the commit after the outputs)

- `revision/text_replacements_2026-10-01_cold_reads_revision.json` — the replacements of the revision, applied in
  order with `notes/review_2026-09-25/revision/apply_replacements.py`, each with a `why`: the finding of a read, the
  finding of an audit or of a check, or the rule of an entry that it answers, or, for the replacements that answer
  none of these (the references, the renumbered rows, the figure script, the bookkeeping files, the condensations),
  what it does; where a replacement takes a statement out of the main text, its `why` or the record's entry on the
  revision says where the statement now is. The record's five new entries (the four outcome entries and the
  revision's) carry «ENTRY_TIME», which the writer's session filled with the commit's time.
- `checks/` — `derived_r24.py` and its output `derived_r24.out` (the inverted sign-flip intervals of B16c's contrasts,
  B27's SDs and r², the regional slopes of sts and rtr on r₁, the disattenuated interval's lower limit as a share, the
  FD-residualised shares and, added after the audits of the prepared revision, the generators' mean residual DiDs over
  the replicates with the step-minus-ramp differences, the Fisher-z intervals of the mean cross-half correlation and
  of the whitened correlations, the regional relation on the windowed estimator's own atoms, and the leave-one-out of
  the sts slope; added after the checks of the corrections, the parts of the sts DiD's variance, the residual's
  cross-half correlations with r₁ and their ceilings, every cell of B27's table (a) recomputed from its per-subject
  file, and twelve of the values that B27's pre-run entry lists as known, recomputed and compared with the entry's;
  added after a third check, the inverted sign-flip intervals of what the AR(1)-substituted estimate carries of the
  whitened contrasts, of the directed response's difference between the runs and of the count DiD of the replaced
  volumes, and the Fisher-z intervals of the eight whitened correlations at p = 10 and 20: computed from committed
  files (two pickles of per-subject vectors, eight CSV files, five tables files, three array files and a log), no data
  read); `numbers_update.out`, what the update of `manuscript/main_text_numbers.csv` did (the rows deleted by class,
  the rows added, the locators moved and corrected); `figures_check.py`, the check the figures commit runs; and this
  commit's outputs of the checks (`apply_revision.out`, `check_numbers_revision.out`, `check_cells_revision.out`,
  `tablecheck_revision.out`, `wc_revision.out`, `abstract_summary_revision.out`, `scripts_check_revision.out`), with
  `abstract_summary.py`, the word counter of the Abstract and the Author summary; `figures.out`, the output of
  `figures_check.py` at the figures commit, comes with that commit.
- `claims/claims_2026-10-01.md` — the claim record: every statement the revised text makes about a cited work that no
  earlier citation pass covered, with where in the work it was checked.
- `pubmed_search/psychedelic_phiid_search.md` — the web searches for applications of ΦID to psychedelic data and the
  PubMed search V.S. ran for them on 2 October 2026, with its export `pubmed_psychedelic_search.csv` and the screening;
  `screening.md` and `search_string.txt` of the first search brought up to date (the two records assessed from their
  full texts; a statement that PubMed's reading of the string, its Search details, was not kept).
- `audit/` — the audits of the prepared revision by three separate sessions before it was committed, as the sessions
  returned them (`findings_text.md`; `findings_record.md`; `findings_citations.md`, in the form its session gave it
  once the PDFs of eight more works had reached it, with `te_filter_check.py`, the population check its first finding
  rests on); the reports of the sessions that then checked the corrections (`check_VO.md`, `check_VE.md`,
  `check_VR.md`, `check_VT1.md`, `check_VT2.md`, `check_VC.md`, `check_VN.md`, `check_VM.md`, `check_VS.md` and
  `check_VB.md`), as those sessions returned them but that the path of the planning session's working directory is
  written `$SP` and that a closing remark of two of them on the session's own memory is left out; the reports of the
  seven sessions that checked the corrections a second time (`recheck_W1.md` to `recheck_W7.md`) and of the four that
  checked them a third time (`recheck_X1.md` to `recheck_X4.md`), as those sessions returned them; the report of the
  session that then read S19 Table's Part B against the whole paper (`partB_reading.md`), which that session returned
  as text and which is saved as it stood from its heading on; the reports of the four sessions that then checked the
  revision a fourth time (`recheck_Y1.md` to `recheck_Y4.md`) and of the two that read the corrections made for that
  check (`reading_Z1.md` and `reading_Z2.md`), as those sessions returned them; and what was done with each finding of
  the audits, of the four checks and of that last reading, and with the reading of Part B
  (`dispositions_revision.md`); `findings.md` and `dispositions.md` are those of the earlier commit (first section).
