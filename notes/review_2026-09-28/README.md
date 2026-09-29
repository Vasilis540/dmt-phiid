# The citation crosscheck of 28 September 2026

Every place where the text at d108d66 attributes something to a cited work — a sentence of the main text or the
supporting information, or a cell of S4 Text or S20 Table — checked against the work itself. A sentence that cites three
works gives three claims: 271 in all (C001–C271). For each claim the sessions that checked it took the passages of the
work that bear on it, word for word, with their PDF pages, and gave a verdict and whether the work states the point as
its own. Record: "The citation crosscheck of 28 September 2026 and the revision it led to".

**Verdicts.** SUPPORTED — the work states everything the claim attributes to it (194). SUPPORTED WITH QUALIFICATION —
supported in substance, but the claim is broader, narrower or more certain than the work, or a detail differs; the note
says what (59). NOT SUPPORTED — the work does not say it, or says something else (2). CANNOT CHECK — the part of the
work needed was not available (2). NOT A CONTENT CLAIM — the sentence attributes nothing to the work's content (14). A
table cell with several facts takes the verdict of its weakest fact. **Firsthand.** OWN — the work states the point as
its own data, method, result or definition (252); SECONDHAND — only by citing someone else, so that citing it for the
point would be a supercitation (1); not applicable (18).

**Who checked.** Eight sessions of the AI system, one per group of works, and the planning session, which checked the
group of Luppi et al. (2024, 2026) after that group's session stopped on a usage limit, and the works not among V.S.'s
PDFs. The planning session read every verdict other than a plain SUPPORTED, re-checked against the PDF the claims behind
each proposed change, and spot-checked a random sample of the plain ones. Each of the 759 passages taken from a PDF was
found again, word for word, on its stated page by a script of the planning session, written separately from the seven
group sessions that copied 639 of them; the other 120 (Luppi et al., 2024, 2026) the planning session cut from the page
texts itself. The script normalises soft hyphens, zero-width characters, ligatures, line-break hyphens and white space.
33 passages do not come from a PDF of the cited work: publishers' and journals' pages, PubMed, bioRxiv, `phyid`'s code
at its pinned commit, the data release and, for Theiler et al. (1992), its abstract and Prichard & Theiler (1994), each
with its source.

## Files

- `crosscheck_claims.csv` — one row per claim: its location in the typeset PDFs of d108d66, the text it is in, what it
  attributes to the work, the verdict, the firsthand status, the note, the proposals that change it, and the PDF pages
  (and printed pages) of its passages. The passages themselves are not in the repository: they are verbatim excerpts of
  the cited works. The full document with them (`citation_crosscheck.md`, `citation_crosscheck.xlsx`) is held by the
  corresponding author; with the works in hand, every passage can be found on the page given here.
- `proposals.json` — the 51 changes the crosscheck proposed (P01–P50, P26b; classes A, B and C), each with the text it
  replaces, its replacement and the reason. All were applied in the revision of 28 September 2026.
- `revision/text_replacements_2026-09-28.json` — every replacement of the revision that followed (the 51, their
  mirrors in `notes/partB5_literature_v2.md`, the readiness, analytic, audit and length items, the correction of the
  code for the matrices that are not positive definite (F01–F52; B26), the numbers table and the record's entries, and
  `README.md`, `CLAUDE.md` and `run_all.sh`), applied with
  `notes/review_2026-09-25/revision/apply_replacements.py`. The record's entries carry «ENTRY_TIME» there: the writer's
  session put the date and time of the commit into the record after applying them.
- `revision/b25_fill.py` — the text that reports B25, written from B25's outputs alone; fixed with B25's pre-run entry,
  before B25 was run. When it runs it writes `revision/text_replacements_2026-09-28_b25.json`, the replacements it
  applies.
- `checks/phiid_indep.py` and `checks/phiid_indep.out` — the closed form of Results 1 re-derived by an implementation
  written from the lattice definitions alone, without `phyid` or the repository's code.
- `checks/check_numbers.out`, `check_cells.out`, `tablecheck.out`, `wc.out` — the checks of the revised text, run with
  the scripts of `notes/review_2026-09-25/checks/`; `checks/pytest.out`, `doctest.out`, `b25_selftest.out`,
  `b26_selftest.out` — the tests, the tool's doctest and the self-tests of B25 and B26 on the revised tree;
  `checks/verbatim.out` — the blocks that scripts of `notes/` copy from other scripts, each against its source.
- `checks/b26_preview.md` — what B26's pre-run entry knows before the run: what the correction changes whatever the
  data (the steps of section 6 that read no data, run by the planning session with the corrected code, their counts of
  matrices that are not positive definite and every line and cell of their outputs that differs from d108d66's; B10's
  and B15's sections on synthetic series; Fig 3 (c)); the numbers of the main text and of the supporting information
  whose source changed; and section 6 run with the corrected code, under B26's runner, and with d108d66's, on synthetic
  series of the data's layout (not the data), with the source of every change. `checks/b26_null_sections.py` and `.out` — the null of
  `review_v2_residual_null.py` replayed with the corrected code, counting per section. `checks/b26_changes.py` — lists
  every change a run makes to the committed outputs: every changed line and cell in full, for each changed array the
  number of entries that changed, the largest change and the first 2,000 entries, and for each image the pixels that
  differ; the listing rule (i) of B26's pre-run entry reads; the preview's listings are its output.
- `audit/` — the audits of the prepared revision by separate sessions (`findings_text.md`, `findings_b25.md`,
  `findings_ci.md`; then `findings_b26code.md`, of the correction of the code and B26's runner, whose entry numbers are
  those of its draft; then a second round, of the corrected revision: `findings2_text.md`, of the text, the entries and
  the preview, and `findings2_code.md`, of the correction, the runner and the scripts of the run; then a third, the same
  way, `findings3_text.md` and `findings3_code.md`, a fourth, which verified the third's corrections,
  `findings4_text.md` and `findings4_code.md`, and a fifth, which verified the fourth's, `findings5_text.md` and
  `findings5_code.md`; their line numbers are those of the build they audited) and what was done with each finding
  (`dispositions.md`).
