# Audit of the prepared revision of 28 September 2026 (REVISED tree `b32/audit/treeA_v1`)

Scope: items D01–D07, E01–E04 (and E02L–E04L), C01–C04, N01–N07 (numbers table, the two record entries), K01–K23,
the new files, `notes/review_2026-09-28/`. P-items checked only for consistency with the rest.
Line numbers are those of the REVISED tree. Nothing outside this file was edited; runs were made on a copy
(`b32/audit/aud/tc`) with `v312` (Python 3.12.3, NumPy 2.5.3, SciPy 1.18.1, phyid 6c5f2e9). `partB25_binarised.py`
was run only with `--selftest`; no binarised quantity of the AR(1) family was computed.

Dependencies to keep in mind for every fix: record entry item 10 lists the sha256 of the review folder's `README.md`
and of `revision/b25_fill.py`, so editing either needs the hash updated; `b25_fill.py` matches exact strings of
S5 Text §6, S20 row 2, the Methods count, the DCA and CLAUDE.md/README.md (all 16 of its old strings occur exactly once
now, checked), so a wording change to those strings must be mirrored in `b25_fill.py`; record-entry edits must also go
into the N07 entry of `revision/text_replacements_2026-09-28.json`; a DCA edit near "Attribution 4.0 licence" needs the
context of the `4.0` row of `main_text_numbers.csv` recomputed.

---

## Findings (most serious first)

### 1. [major] Table B item 1 attributes to Luppi et al. (2023)'s MMI emergence capacity a property shown only for the Gaussian estimator (E02, E02L; record item 5)

- `manuscript/supplementary.md` line 1673 and `notes/partB5_literature_v2.md` line 27 (E02/E02L):
  "the whole-minus-max synergy of Luppi et al. (2024, Eq. 5), which is also the MMI emergence capacity of Luppi et al.
  (2023), depends on r₁ alone on this family."
- `manuscript/analysis_record.md` lines 7688–7689 (item 5): "and, under MMI, the emergence capacity of Luppi et al.
  (2023); on the family it depends on r₁ alone."
- What is wrong: "depends on r₁ alone" holds for the Gaussian estimator (sum = S). Luppi et al. (2023) do not say which
  estimator their MMI replication used, and their Methods say every analysis used the plug-in estimator on
  mean-binarised signals; on binarised signals the MMI emergence capacity is T − F of the binarised variables, which is
  exactly what B25 is registered to find out. The sentence contradicts row 2 of the same table and the B25 entry.
- Evidence: Luppi2023 p. 12: "For all the analyses in the paper we compute information-theoretic quantities for each
  pair of brain regions, using a standard plug-in estimator applied to the mean-binarised BOLD signals. To validate our
  results, we also replicated them using continuous instead of discrete signals and the Gaussian solver … Likewise, we
  replicate our results using an alternative definition of redundancy known as the minimum mutual information (MMI)".
  S20 row 2 (line 1660): "The Gaussian and the MMI validations are inside it if each used both the Gaussian estimator
  and MMI, which the paper does not state." Record line 7753–7754 (B25 entry): binarised "emergence capacity T − F; for
  the Gaussian atoms F = A and T = 2A, which gives … emergence capacity S" (so the binarised value is not S in general).
  E03 in the same table correctly says "the Gaussian-MMI emergence capacity".
- Correction (supplementary.md l. 1673 and partB5 l. 27): replace "which is also the MMI emergence capacity of Luppi et
  al. (2023), depends on r₁ alone on this family." by "which under MMI with the Gaussian estimator is also the
  emergence capacity of Luppi et al. (2023) (whose MMI validation's estimator the paper does not state; row 2), depends
  on r₁ alone on this family." Record item 5: replace "and, under MMI, the emergence capacity of Luppi et al. (2023); on
  the family it depends on r₁ alone." by "and, under MMI with the Gaussian estimator, the emergence capacity of Luppi et
  al. (2023) (whose MMI validation's estimator is not stated); on the family it depends on r₁ alone." (See also 4.)
- Side point (minor): E02 is inserted inside "Exact properties on this family (checked to 4e-15 over 2,000 seeded draws
  …)" before "Script `notes/partB5_family_checks.py`, log …"; `family_checks.log` does not check this identity (it
  logs TDMI, rtr + sts, rtr = C, ΦR − rtr). It is checked by `tests/test_closed_form.py` and `checks/phiid_indep.out`
  ("aggregate=S … 4.4e-16"); the "(main text, Results 1)" pointer is right, but a reader will take it as part of the
  2,000-draw check.

### 2. [major] B25 pre-run entry misstates the address Luppi et al. (2023) print

- `manuscript/analysis_record.md` lines 7739–7740: "read, not run; no repository was found on 28 September 2026 at the
  address Luppi et al. (2023) print, github.com/robince/partial-infodecomp)."
- What is wrong: the paper prints and links github.com/robince/partial-info-decomp, the very repository the entry says
  was read. "partial-infodecomp" is an artefact of the raw text extraction, which dropped the line-end hyphen.
- Evidence: `pdftotext -layout` of Luppi2023.pdf p. 12: "tools (https://github.com/robince/partial-info-" / "decomp).
  Here, we follow …" (the hyphen is at a line end; image checked); the PDF's link annotation on that page:
  `https://github.com/robince/partial-info-decomp` (pypdf, /URI). `cite/txt/Luppi2023/p012.raw.txt` line 10 shows the
  joined "partial-infodecomp".
- Correction: "computed as Ince's toolbox computes it (`Iccs.m`, `calc_pi.m`, `mme2.py` of
  github.com/robince/partial-info-decomp, the repository Luppi et al. (2023) link on their p. 12, at 3220716; read, not
  run)." (The entry is append-only once committed; fix it before the commit, and in the N07 JSON entry.)

### 3. [moderate] Data and code availability licenses the manuscript text CC BY 4.0 while the same paragraph says "not for citation or distribution" (D04; new licence files)

- `manuscript/draft_v2.md` line 246: opens "Manuscript for co-author review; not for citation or distribution." and
  now says "The code is released under the MIT licence and the text, figures and result files under the Creative
  Commons Attribution 4.0 licence (`LICENSE`, `LICENSE-CC-BY-4.0.md`)".
- `LICENSE-CC-BY-4.0.md` line 5: "The text (`manuscript/`, the Markdown files under `notes/`, `README.md`) … are licensed
  under … CC BY 4.0 … You may share and adapt them for any purpose". So the co-authored draft (C.T., S.P.S. and [TK]
  co-authors listed; "Copyright (c) 2026 Vasilis Sampalis" only) is granted for redistribution by the file while the
  draft forbids distribution. CLAUDE.md line 373 plans to remove the "not for citation" line only at submission.
- Also: `CITATION.cff` line 10 `license: MIT` while its message covers "this code or its results" (results are CC BY);
  `data/Schaefer2018_100Parcels_7Networks_order.lut` (downloaded from the CBIG repository, record l. 2075–2077) is a
  third-party file covered by neither statement and not in LICENSE-CC-BY-4.0.md's "Not covered" list.
- Correction (one consistent option): LICENSE-CC-BY-4.0.md l. 5: "The text (the Markdown files under `notes/`,
  `README.md`), the figures … and the result files … are licensed under … CC BY 4.0 …; the manuscript files
  (`manuscript/draft_v2.md`, `manuscript/supplementary.md`, `manuscript/si/`) are drafts for co-author review and are
  released under CC BY 4.0 with the preprint." DCA: "The code is released under the MIT licence and the result files
  and figures under the Creative Commons Attribution 4.0 licence (`LICENSE`, `LICENSE-CC-BY-4.0.md`); the manuscript
  will be under the same licence from its preprint; the data are not included." (recompute the `4.0` row's context).
  CITATION.cff: `license:` followed by `  - MIT` and `  - CC-BY-4.0`. Add to the "Not covered" paragraph:
  "`data/Schaefer2018_100Parcels_7Networks_order.lut` (CBIG; its own licence)". (Alternatively drop the "not for
  citation or distribution" line now; README/CLAUDE.md wording would then follow.)

### 4. [moderate] S20 row 3 and record item 5 state that the workspace is defined by the whole-minus-max synergy, dropping the qualification P03 put into the main text (E04, E04L)

- `manuscript/supplementary.md` line 1661 and `notes/partB5_literature_v2.md` line 15: "the synergy that defines the
  workspace, the whole-minus-max synergy of Eq. 5, is str + stx + sty + sts, which on the symmetric family is S, a
  function of r₁ alone".
- `manuscript/analysis_record.md` line 7688: "by whose rank they define the workspace" (item 2 of the same entry,
  l. 7644–7645, gives the qualified version).
- What is wrong: Luppi et al. (2024) say they used the persistent synergy (sts) and write only Eq. 5; which quantity
  defined the workspace is not settled by the paper. The main text (Introduction, P03) says so; S20 and the record
  resolve it silently in favour of Eq. 5, and the conclusion "a function of r₁ alone" depends on that resolution (sts is
  2S − C, which depends on q).
- Evidence: Luppi2024 p. 6: "we focused on the persistent synergy (henceforth simply synergy) and persistent redundancy";
  p. 20: Eq. 5 "syn(X, Y) = I(Xt−τ, Yt−τ; Xt, Yt) − max{I(Xt−τ; Xt, Yt), I(Yt−τ; Xt, Yt)}"; p. 21: regions ranked by
  nodal strength of the synergy and redundancy networks.
- Correction (row 3 and partB5 l. 15): "…not sts; the synergy that defines the workspace, which the study calls the
  persistent synergy (p. 6) but writes as the whole-minus-max synergy of Eq. 5, is, as written, str + stx + sty + sts,
  which on the symmetric family is S, a function of r₁ alone (Table B item 1)." Record l. 7688: "by whose rank, as they
  write it (they call it the persistent synergy, p. 6), they define the workspace".

### 5. [moderate] "by a script written separately from the sessions that copied them" is false for 120 of the 759 passages (D06; record item 1; review README)

- `manuscript/si/S5_Text.md` line 27 (D06); `manuscript/analysis_record.md` lines 7631–7633;
  `notes/review_2026-09-28/README.md` lines 22–23: "Each of the 759 passages taken from a PDF was found again, word for
  word, on its stated page by a script written separately from the sessions that copied them".
- What is wrong: the 120 PDF passages of group g3 (Luppi et al. 2024: 59, 2026: 61) were cut from the page texts by the
  planning session, which also wrote the checking script; only the other 639 were checked by a script written apart
  from their copiers.
- Evidence: `cite/final/units_final.json`: group g3, `checked_by` "planning session (the g3 agent stopped on a usage
  limit)", 30 units, 120 PDF passages; other groups 88+135+61+111+67+77+100 = 639. `cite/g3w/g3_build.py` docstring:
  "Group g3 (Luppi 2024, Luppi 2026): built by the planning session … Every passage is cut from the normalized page text
  by span()". The checker `cite/check_all.py` imports `check_passage` from `cite/g3w/norm.py` (the planning session's
  g3 work folder).
- Correction (all three places): "Each of the 759 passages taken from a PDF was found again, word for word, on its
  stated page by a script of the planning session, written separately from the seven group sessions that copied 639 of
  them; the other 120 (Luppi et al., 2024, 2026) the planning session cut from the page texts itself." (Update the
  README's sha256 in record item 10.)

### 6. [moderate] Stale or forward-dated bookkeeping: CLAUDE.md says B25 is applied and cites a non-existent S3 Text §11; README's [TK] statement is now wrong (K11, K12; README l. 49)

- `CLAUDE.md` line 17 (K11): "the citation crosscheck of 28 September 2026 applied, with the readiness items and B25,
  the binarised estimators on the family; the typeset PDF and the note to C.T. and S.P.S. next".
- `CLAUDE.md` line 19 (K12): "…and B25 (the binarised estimators on the family; S3 Text §11):". S3 Text has sections 1–10
  only (headings at lines 5–422); §11 is written by `b25_fill.py` after B25 runs. B25 has not been run.
- `CLAUDE.md` line 367: "- Remaining work: the typeset PDF … and the note to C.T. and S.P.S." — omits B25's run, its
  separate re-run and `b25_fill.py`, which must precede the typeset PDF. The round list (lines 364–366) has no
  "Round 21" bullet.
- `README.md` line 49: "The [TK] marks left are the co-author items." — D04 added "[TK: the DOI of the archived version
  (Zenodo), at submission.]" (draft line 246), not a co-author item.
- Corrections: CLAUDE.md l. 17: "(round 21, bundle 32: the citation crosscheck of 28 September 2026 applied, with the
  readiness items and B25's script and pre-run entry; next B25's run at that commit, its re-run by a separate session
  and `notes/review_2026-09-28/revision/b25_fill.py`, then the typeset PDF and the note to C.T. and S.P.S.)". l. 19:
  "and B25's script and pre-run entry (the binarised estimators on the family, not yet run; S3 Text §11 is written from
  its outputs by `notes/review_2026-09-28/revision/b25_fill.py`):". l. 367: begin "- Remaining work: B25's run at the
  revision's commit (the command in its docstring), its re-run by a separate session and `b25_fill.py`; then the typeset
  PDF …"; add a "- Round 21 (bundle 32; record, "The citation crosscheck of 28 September 2026 and the revision of that
  date" and B25's pre-run entry): …" bullet. README l. 49: "The [TK] marks left are the co-author items and the archive's
  DOI (Data and code availability), filled at submission." (b25_fill's G13–G15 strings are unaffected.)

### 7. [minor] Numbers table: the rewritten Results 1 paragraph 9 rows are out of reading order, and the `+0.05` row points at the c = −0.05 line (N03)

- `manuscript/main_text_numbers.csv` lines 154–155: the `+0.05` row (context "…most at c = +0.05…") precedes the
  `+0.10` row (context "…up to c = +0.10, lowers…"), but in the text "+0.10" comes first. The head note says "one row
  per occurrence, in reading order". (Reading-order check over all rows: this is the only violation the revision adds;
  the two in Methods/Inference predate it.)
- Line 154's locator "line 9; anchor: 0.05" is the c = −0.05 row of `coupling_map_tables.md` (line 9 = "| -0.05 |
  0.8625 |…"; c = +0.05 is line 13). Pre-existing, but the sentence now claims "most at c = +0.05", a claim resting on
  lines 12–14 (1.2315, 1.2155, 1.2569), and the row is still "design / the coupling evaluated".
- Correction: swap lines 154 and 155; set line 154 to category `derived`, empty source/locator, note "derived: the
  smallest sts of the matched view for c > 0: 1.2155 at +0.05 against 1.2315 at +0.02 and 1.2569 at +0.10
  (coupling_map_tables.md lines 12–14)" (or at least locator "line 13; anchor: | +0.05 | 0.8375 |"). The claim itself
  is right: a fine-grid recomputation with partB8's matched solver puts the minimum at c ≈ 0.052 (sts 1.2154).

### 8. [minor] S5 Text §6 uses the undefined process term "the readiness items" and a label (B25) that the SI does not yet define (D05)

- `manuscript/si/S5_Text.md` line 31: "the revision of 28 September 2026 (the corrections of the citation crosscheck of
  that date, the readiness items and the pre-run entry of B25) is the commit that follows". "Readiness items" is the
  planning's term, defined nowhere in the manuscript files (S5 §5 defines only "the writer's session and the planning
  session"). S3 Text line 3 still says the computations are "(B1–B24, B16b, B17b)" at this commit.
- Correction: "(the corrections of the citation crosscheck of that date, the licence, citation file, diagnostic tool,
  tests and continuous-integration workflow, and the pre-run entry of B25, the binarised estimators on the family)".
  The same wording must replace "the readiness items" in `b25_fill.py` lines 246–250 (S5_COMMIT_OLD/NEW), and the
  sha256 of `b25_fill.py` in record item 10 be updated.

### 9. [minor] Record item 3 miscounts what S4 Text named and overstates what pandas writes

- `manuscript/analysis_record.md` lines 7667–7668: "S1 Text's software line and S4 Text's item S8 named four of these".
  S1's line named four (Python, NumPy, SciPy, Matplotlib); S4 S8 named five (the same and `phyid` at 6c5f2e9d…; base
  S4_Text.md l. 55).
- Line 7665: "pandas 3.0.5, which writes the result CSVs" — pandas is imported only by scripts under `notes/` (19
  files; it writes the CSVs under `notes/review_results/`); `results/*.csv` are written by `scripts/`, none of which
  imports pandas. (The D02 "why" in the committed JSON has the same wording and says "every package the scripts
  import", but `notes/rev_deconv.py` also imports joblib 1.6.0, in the lock, which S1/S4 do not list.)
- Correction: "S1 Text's software line named four of these and S4 Text's item S8 five"; "pandas 3.0.5, which writes the
  CSVs of the review and Part B computations under `notes/review_results/`". Optionally add "joblib 1.6.0 (the
  deconvolution's parallel loop)" beside rsHRF in S1/S4.

### 10. [minor] Record item 7 omits one of the removed numbers

- `manuscript/analysis_record.md` lines 7697–7698: "Results 3's F, network means and contrast p values of the partialled
  map (Fig 4's caption)". C02 also removed the unpartialled map's spin p ("against 0.056 for the unpartialled map"),
  which item 8 lists among the 13 deleted rows.
- Correction: "Results 3's F of the partialled map, the unpartialled map's spin p, the network means and the contrasts'
  spin p values (Fig 4's caption)".

### 11. [minor] Record item 1 and the review README describe the passage check and the outside sources inexactly

- `manuscript/analysis_record.md` lines 7633–7635: "(normalising only soft hyphens, zero-width characters, ligatures and
  line-break hyphens); 33 passages come from sources outside V.S.'s folder (publishers' pages, preprint servers, `phyid`
  at its pinned commit)"; review `README.md` line 24: "33 passages come from sources outside V.S.'s folder".
- `cite/g3w/norm.py` also collapses all white space and maps tab, no-break, thin and narrow no-break spaces to spaces,
  and searches the raw, layout and (Luppi2026 pp. 33–41) OCR page texts. Of the 33 "other" passages, 2 (C072, C084) are
  from Prichard & Theiler (1994), "Prichard1994.pdf in your folder"; 4 are descriptions of the data release (external
  DMT_NCT); 3 are PubMed abstracts; several were taken over from the citation pass of 22 September 2026
  (`units_final.json`, fields `source`, `checked`).
- Correction: "(normalising soft hyphens, zero-width characters, ligatures, line-break hyphens and white space); 33
  passages do not come from the cited work's PDF: publishers', PubMed and bioRxiv pages, `phyid` at its pinned commit,
  the data release, and, for Theiler et al. (1992), Prichard & Theiler (1994), each with its source". README l. 24
  likewise (update its sha256 in item 10).

### 12. [minor] Record item 9 says the outputs of the tests and the self-test are in `checks/`; they are not

- `manuscript/analysis_record.md` lines 7710–7711: "the tests and B25's self-test passed on the revised tree. The
  outputs are in `notes/review_2026-09-28/checks/`." The folder holds check_numbers.out, check_cells.out,
  tablecheck.out, wc.out and the phiid_indep pair only.
- Correction: add `checks/pytest.out` and `checks/b25_selftest.out` (and name them in the review README), or write
  "The outputs of the four text checks are in `notes/review_2026-09-28/checks/`."
- Re-run here: pytest 104 passed; doctest ok; self-test "53 checks, 0 failed" (3-variable 2.78e-17, Genz 9.81e-09).

### 13. [minor] B25 pre-run entry cites the main text for a value the main text prints differently

- `manuscript/analysis_record.md` line 7770: "(0.0284 for pair r₁ and 0.1957 for |q|; main text, Results 1)". The main
  text (draft l. 53) prints "0.196"; 0.1957 is in S3 Text l. 128 (B22 (d); the script's comment cites
  `aligned_directed_tables.md`). The threshold 6.89 = 0.1957/0.0284 is consistent with the script and `b25_fill.py`.
- Correction: "(0.0284 for pair r₁ and 0.1957 for |q|; S3 Text §4; 0.196 in the main text, Results 1)".

### 14. [minor] "tests/ checks it and the closed form against phyid and notes/rev_phiid_fast.py" (D04; record item 4)

- `manuscript/draft_v2.md` line 246; `manuscript/analysis_record.md` line 7680; same wording in the workflow comment and
  README l. 70. `tests/test_closed_form.py` checks the closed form against the lattice solve of `tools/ar1_diagnostic.py`
  (and long AR(1) series through the tool), not against phyid or `rev_phiid_fast`; only `test_ar1_diagnostic.py`
  compares with them (the claim holds only transitively).
- Correction (DCA): "and `tests/` checks it against phyid and `notes/rev_phiid_fast.py` and the closed form against its
  lattice solve;". Record l. 7680 likewise.

### 15. [minor] `b25_fill.py` writes the outcome of the separate re-run before the re-run exists

- `notes/review_2026-09-28/revision/b25_fill.py` lines 268–273 (G09) and 278–283 (G11) insert into the DCA and S5 §4:
  "re-run at the same commit by a separate session, which reproduced every value". The outcome entry the same script
  writes (line 382) says the re-run is still to come ("A separate session re-runs it at {A} before this commit is
  pushed"), and the pre-run entry (l. 7786–7787) schedules it after the run. The text "fixed now, before the run" thus
  asserts a result not yet known.
- Correction: take the re-run's result as a third argument and stop if it is not "reproduced"; or write "and is re-run
  at the same commit by a separate session before this text is committed". (Update the sha256 in item 10.)

### 16. [nit] Smaller bookkeeping slips

- `run_all.sh` line 17 (K23): "B25 (28 Sep 2026, not in the final run) minutes" — no quantity. The self-test times one
  replicate at T = 840 at 9.8 ms (72,000 replicates at most), so e.g. "about 15 min (estimate)".
- Review `README.md` line 39: "`revision/text_replacements_2026-09-28_b25.json` holds what it applied." — the file does
  not exist yet ("will hold what it applies"). Line 35: "every replacement of that revision (the 51, their mirrors …,
  and the readiness, analytic and length items)" — the JSON also holds N01–N07 (numbers table, record) and K01–K23
  (README.md, CLAUDE.md, run_all.sh).
- `revision/text_replacements_2026-09-28.json`, N07: its "new" string carries «ENTRY_TIME» twice; once the times are
  filled in the record the committed JSON no longer rebuilds the committed record. Fill the times in the JSON too.

---

## Notes (not established as errors)

- P12/P13 (S20 row 5, Table B item 3) now place "faster decay of autocorrelation under anaesthesia" in "an example
  macaque time series (Fig. 3e)". Per `crosscheck_claims.csv` C268 this locator comes from bioRxiv version 2 (HTML)
  "fetched … with a web fetch tool that answers through a summarising model, so the words should be confirmed", while
  the S20 reference note says the quotations were "checked against its full text, version 1". Confirm "Fig. 3e" on the
  version cited, or name version 2 in the note.
- Pre-existing, not introduced by the revision: the numbers-table row "Introduction, paragraph 2, 2, 1" carries the note
  "½ ln(1 + α²): formula" but its context is the "lag-1" later in the paragraph; the seed row's context runs past its
  paragraph (only row whose full context is not found; check_numbers passes it on the first 60 characters).

## Checked and found correct

- E01: on the symmetric family str + stx + sty + sts = (S − C) − 2(S − C) + (2S − C) = S; the MMI-ΦID sum of the
  synergistic-source atoms is I(XY; X′Y′) − max[I(X; X′Y′), I(Y; X′Y′)] (R_xytab = min), i.e. Luppi et al. 2024 Eq. 5
  with the joint future as target (Luppi2024 p. 20, "using the MMI-ΦID decomposition for Gaussian variables"); on the
  family I(X; X′Y′) = S (multiple R² = a²), so WMS = 2S − S = S. Varley's Eq. 3 (Varley2024 p. 5) is the same
  whole-minus-max form. Luppi et al. 2023's emergence capacity is downward causation + causal decoupling, CCS primary on
  mean-binarised signals, Gaussian and MMI replications (Luppi2023 pp. 11–12).
- E03 ("the Gaussian-MMI emergence capacity, which on the symmetric family is S"); S20 and partB5 Tables A/B still
  differ only by the known label substitutions (15 rows/items compared before and after).
- D01: Limitations reads correctly; "Two redundancy functions were examined on the data, both Gaussian" true; no other
  sentence claims a cause for the r₁ fall. C03: the ground-truth clause now in the Discussion's first sentence.
- D02/D03: pandas 3.0.5 and h5py 3.16.0 in `requirements.lock.txt`; h5py only reads SPIN (the rotations) in 4 scripts;
  rsHRF 1.7.0 (S2 Text l. 7; `notes/rev_deconv.py`); no script calls MATLAB/Octave (they read .m/.mat files only);
  CLAUDE.md l. 567 "Python only … no MATLAB"; phyid pinned by commit in the lock.
- D04: `tools/ar1_diagnostic.py` (NumPy only; CLI `x_file y_file --window --tau`), `tests/` (104 tests: 96
  parametrised + 8), `.github/workflows/tests.yml` (push, PR, dispatch; pinned NumPy/SciPy; phyid checked out at
  6c5f2e9d…; pytest, doctest, self-test, phyid's tests), phyid's `test_calculate.py` compares gaussian/discrete × MMI/CCS
  with `PhiID_test_simple_1.mat` downloaded from OSF; LICENSE (MIT), LICENSE-CC-BY-4.0.md exist. Re-run: 104 passed,
  doctest ok.
- D05: d108d66 is 2026-09-27 14:43 UTC; the parent statement is right. D06 counts from `crosscheck_claims.csv`: 271
  claims; 194/59/2/2/14; 252 OWN, 1 SECONDHAND (C053 Kay 2018), 18 n/a; NOT SUPPORTED C210 (Luppi 2026 row 5), C256
  (Varley row 10); CANNOT CHECK C072, C084 (Theiler); 759 PDF passages and 33 others; `proposals.json` 51 (A 13, B 35,
  C 3). D07: folder exists.
- C01: Fig 1 caption keeps 1.2588, 1.2155, 1.2569, 1.4111 (and 1.2315, 1.3023); "up to c = +0.10 lowers" (1.2569 <
  1.2588) and "most at c = +0.05" (fine-grid minimum at c ≈ 0.052) true. C02: Fig 4 caption keeps F 8.146, spin p
  0.0009, unpartialled 16.933 / 0.0564, means −0.0235 / +0.0207, contrasts' spin p 0.2240 / 0.3089. C04: Introduction's
  and Results 2's "(Methods)" still land on "Pre-registration and deviations", which states the ordering. No main-text
  sentence refers to the removed values; "the coupled family" (Limitations) is still defined by Fig 1's caption and
  S3 Text §3.
- Numbers table: 1,183 rows (1,193 − 13 + 3); 11 contexts recomputed; the 13 deleted rows are exactly the tokens removed
  from the two paragraphs, and no other number of the 13 changed blocks lost or gained a row (years, file paths,
  "Eq. N" and the References/Competing interests blocks are outside its conventions/scope); rows 4 and 6 follow the
  79–82 precedent; `4.0` row added; every context occurs in the revised text; occurrence numbers correct.
  `check_numbers.py`: "rows 1183, data rows 666, flagged 12", the same 12 sign-wording rows as review_2026-09-25;
  check_cells "flagged 0"; tablecheck 0; wc 6,995 / 6,875 (base 6,997 / 6,877); +61 words before the condensations
  (recomputed by applying the non-C replacements to the base).
- Record entry 1: sha256 of the six documents match item 10; `phiid_indep.py` re-run reproduces `phiid_indep.out`
  byte for byte (max 5.0e-16; 6.0705, −0.1892; +0.00490, −0.00116); main text and S1–S5 keep their line counts;
  supplementary.md loses its last two lines (Varley et al. 2023); the committed replacements JSON equals the bundle;
  `citation_crosscheck.md` 93,396 words (Python split); tests run with Python 3.12.3/NumPy 2.5.3/SciPy 1.18.1/phyid
  6c5f2e9 (the `v312` environment).
- B25 entry vs `partB25_binarised.py` and `b25_fill.py`: grid r₁ 0.60–0.95 step 0.05 × q {0.10, 0.25, 0.50}; T {160,
  300, 840}; 1,000 replicates; steps 10⁻⁴ / 10⁻³; 42 and 126 steps; SD 0.0284 / 0.1957 and the 6.89 threshold;
  met/partly met/missed criteria identical in the entry and in `b25_fill.py` (VA, VB, VC); outputs and log name match
  run_all.sh's `nstep partB/binarised_run`; every old string of b25_fill's G01–G15 occurs exactly once in the tree; the
  five count rows (53, 25, 14, 14, 0) exist; the lattice algebra of (i)–(ii) (sts = T − 2F + 2A − B, EC = T − F; Gaussian
  F = A = S, T = 2S; q = 0 gives 2A and A) verified symbolically, without evaluating the family; the self-test's 53
  checks (1 + 2 + 12 + 2 × 19) and its reported numbers reproduced.
- K items: README badge, K02 (115 regions), K03 (−0.132, −0.031, p 0.004 from −0.1317, −0.0310, 0.0038), K04, K05–K07,
  K08–K09; CLAUDE.md K13 (6,995 / 6,875), K14 (1,183), K15–K18; run_all.sh K21–K22 (B25 after B24, before the
  figures).
- No process label in draft_v2.md, supplementary.md, S1–S5 Text or captions_v2.md except S5 §5's defined "writer's
  session"/"planning session" (and "bundles" as a verb in P48); no B-label in the main text before its References.
