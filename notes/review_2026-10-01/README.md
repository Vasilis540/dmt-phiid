# The correction of Table 3's caption, 1 October 2026

The review folder of the revision that corrects Table 3's caption of `manuscript/draft_v2.md`: the caption said that
the last two of its five rates per unit of pair r₁ are taken over the residual's pairs; the AR(1) rate is too (S18
Table (b), its last column in row (i)), as the writer's session of the revision committed as df5c160 noted in its
report, and the caption now names three. No number changes. Record: "Table 3's caption: the rates taken over the
residual's pairs".

## Files

- `revision/text_replacements_2026-10-01.json` — the 15 verbatim replacements of the commit, applied in order with
  `notes/review_2026-09-25/revision/apply_replacements.py`, each with its reason: T01 (the caption); N01 and N02 (the
  numbers table: the context of its row for −2.76, a label row for the AR(1) the caption now names, and its head
  note); K01 and K04 (S5 Text §6, the commits the text rests on, and §5, the audit of this correction); K02, K03 and
  K05 (Data and code availability and README.md name this folder, and README.md's paragraph on the paper names the
  correction); C01–C06 (CLAUDE.md); and R01 (the record's entry, whose heading carries «ENTRY_TIME», which the
  writer's session fills with the date and time of the commit).
- `checks/` — the checks of the revised text, run with the scripts of `notes/review_2026-09-25/checks/`
  (`check_numbers.out`, whose twelve flagged rows are the sign-wording rows accepted in every earlier revision;
  `check_cells.out`; `tablecheck.out`; `wc.out`, Introduction through Methods 6,998 words with headings, as before the
  revision), the output of applying the replacements (`apply.out`) and the output of
  `notes/review_2026-09-30/checks/figures_check.py` after the figure script on the revised tree in the planning
  session's environment (`figures.out`): the captions file differs from the committed one in its header alone, the
  PDF files in their creation dates only, five PNG files are identical and Fig 4's differs in 70 pixels by its
  anti-aliasing in that environment, as on 30 September, so the script's verdict line reads "conditions NOT met"; on
  V.S.'s machine, where the committed PNG files were written, they are to be identical (record, the entry on Fig 5's
  caption). The script admits a difference in Fig 5's caption; this revision's condition is the header alone, which
  the script that commits the figures checks line by line.
- `audit/` — the audit of the prepared revision by a separate session of the AI system, against the files of the
  repository (`findings.md`; its line numbers are those of the build it audited), and what was done with each finding
  (`dispositions.md`).
