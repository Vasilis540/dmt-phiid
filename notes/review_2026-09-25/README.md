# The error-only check of 25 September 2026

A last read of the paper at ddae618, restricted to outright errors, made before the final run of `run_all.sh` and
the typesetting: a check by a separate session of the AI system and an end-to-end read by the session that
verified it; the revision prepared from them was itself audited by two further sessions before it was applied. The
record's entry "The error-only check of 25 September 2026 and its verification" describes them and gives the
sha256 of the three documents and of this file; "The error-only revision: the check of 25 September 2026 applied"
records the revision that applied them.

- `BRIEF.md` — the brief the check was given, as given, except that the five absolute paths of the sandbox it ran
  in are replaced by `<a clone of the repository at ddae618>`, `<the checker's folder>` (three times) and
  `<the pinned environment's Python>`.
- `findings.md` — the check's report, as written: 41 findings (T1–T10, N1–N4, X1–X10, C1–C10, U1–U7) and its
  coverage.
- `verification_2026-09-25.md` — the verification of every finding against the committed files, the read's own
  findings (V1–V24), those found in preparing the revision and the final run (V25–V61, of which V35–V52 by an audit
  of the prepared revision by two further sessions and V55–V61 by a second audit, of the corrections, by a third),
  what was judged not to be an error, and the checks of the revised files.
- `revision/` — the revision itself, as applied: `text_replacements_2026-09-25.json`, every verbatim replacement of
  the main text, the SI, the figure script and the repository's `CLAUDE.md` and `README.md`, with the number of
  times its old string must occur (for the two minus-sign entries, a regular expression and the number of
  replacements it must make) and, in `why`, the item of the verification it applies (for `CLAUDE.md` and
  `README.md`, "bookkeeping"); and `apply_replacements.py`, which applies them in order, all or none (`python3
  apply_replacements.py <repository root> text_replacements_2026-09-25.json`, on the tree of the commit before the
  text commit).
- `checks/` — the scripts, run from the repository root unless stated:
  - `check_numbers.py <repository root>` and `check_cells.py <repository root>`: the mechanical checks of
    `manuscript/main_text_numbers.csv` (every data row's source line holds the stated string, which gives the
    printed number at its precision and denotes the right cell); their output on the revised files is
    `check_numbers.out` and `check_cells.out`;
  - `tablecheck.py <file> ...`: every markdown table row has its header's number of cells (`tablecheck.out`);
  - `wc.py manuscript/draft_v2.md`: the word count, Introduction through Methods, by section (`wc.out`);
  - `wrap.py <manuscript folder> <output folder>`: the reading copies both reads used, with line numbers, long
    lines split;
  - `quotecheck.py` and `rowcheck.py`: the check's own scripts (its quotes against the files; table rows against
    their sources), run from a folder holding `findings.md` and a clone named `repo`.

None of these reads subject data, and `run_all.sh` does not run them.
