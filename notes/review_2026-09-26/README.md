# The error-only read of 26 September 2026

A last read of the paper, restricted to outright errors, made on 26 September 2026 while the final run of `run_all.sh`
was in progress: four separate sessions of the AI system, A–C under one brief and D under a brief of its own, read the
main text with its captions and figures (A), S1–S5 Text (B), S1–S20 Table (C) and the typeset PDFs, for layout only
(D); the planning session verified every finding against the committed files, and two further sessions audited the
prepared corrections in turn. The corrections are in the commit after the outputs commit of the final run. The
record's entry "The error-only read of 26 September 2026 and its corrections" describes them and gives the sha256 of
the documents here.

- `BRIEF.md` — the brief, as given, with its three sandbox paths replaced by `<a clone of the repository>`, `<the
  reading copies' folder>` and `<the pinned environment's Python>`; the three assignments of A, B and C; and D's own
  brief, its paths replaced likewise.
- `findings_A.md`, `findings_B.md`, `findings_C.md`, `findings_D.md` — the four reports. The environment refused
  report files from the checkers, so each gave its report as its final message; each file holds that message as
  given, apart from its note on the refused write (removed), its counts (moved under the title), its few sentences
  in the first person (put in the third), its sandbox paths (removed) and, in `findings_D.md`, a first sentence on
  what the preview PDFs were.
- `verification_2026-09-26.md` — the verification of every finding, the five errors found in verifying them (V1–V5),
  the two audits of the prepared corrections and the four errors they found (V6–V9), what was judged not to be an
  error, the layout faults and what the typesetting does about them, and the checks of the corrected files.
- `revision/text_replacements_2026-09-26.json` — the corrections as applied: the verbatim replacements C01–C73 of the
  text, each naming in `why` the finding it applies; the entries N of the numbers table and of the record's entry;
  and the entries B of `CLAUDE.md` and `README.md` ("bookkeeping"). They apply in order with
  `notes/review_2026-09-25/revision/apply_replacements.py <repository root> <this file>` on the tree of the outputs
  commit, this folder's other files copied in.
- `checks/` — the checks of the verification's section 8 on the corrected tree, run from the repository root:
  `check_numbers.out` and `check_cells.out` (`notes/review_2026-09-25/checks/check_numbers.py` and
  `check_cells.py`), `tablecheck.out` (`tablecheck.py` on the seven manuscript files) and `wc.out` (`wc.py
  manuscript/draft_v2.md`).

None of these reads subject data, and `run_all.sh` does not run them.
