# The review and the citation check of 24 September 2026

`adversarial_review_2026-09-24.md` is a referee report on the shortened text at 66c6331 (15 major items, 44 minor
items and six typos). `citation_pass_2026-09-24.md` checks every citing sentence that changed between 90690f4 and
66c6331 against the cited works (111 sentence × work pairs) and the history of S5 Text against git. 
`review_verification_2026-09-24.md` is the planning session's check of both, with a disposition for every item and
twelve findings of its own (V1–V12).

The two reports were written on 24 Sep 2026 by two separate sessions of the same AI system (Claude), launched from the
planning session. Neither held any subject data. The review read the main text, S1–S5 Text, `manuscript/supplementary.md`,
the captions and the six figure images, the record's entries of 23 September and the review of 22 September with its
verification. The citation check read the cited works in the planning session's folder of PDFs and did not use the web.
The PDFs, their text extracts and the rendered page images are not in the repository.

`checks/` holds the scripts, with their paths made repository-relative. None of them reads subject data, and
`run_all.sh` does not run them.

- `chk_core.py`: the review's own exact sign-flip enumeration (2¹⁴ assignments) and interval inversion, run on the
  committed per-subject DiDs. Run from the repository root: `python notes/review_2026-09-24/checks/chk_core.py .`
- `phiid_cf.py`: the review's own Gaussian-MMI ΦID of a 4 × 4 correlation matrix, by Möbius inversion (a module).
- `extract.py`: the citation check's extractor of citing sentences.
  Usage: `python extract.py <manuscript dir at 66c6331> <manuscript dir at 90690f4> <out.json>`.
- `derived_r17.py` and its output `derived_r17.out` (git=66c6331, seed 20261120): the numbers the round-17 text
  derives from committed files. These are the Fieller and bootstrap intervals of the two rates of group means, the
  leave-one-out cross-half table, the t intervals of the partialled regional contrast, the cortex-only regional
  correlation, the band-limit bound and the finite-sample null's own autocorrelation change. They are post hoc: they
  were computed in verifying the review, with no pre-run entry. Run from the repository root:
  `python notes/review_2026-09-24/checks/derived_r17.py .`

The four documents are committed byte-identical to the files the planning session produced; the record's entry for
the review of 24 September 2026 gives their sha256.
