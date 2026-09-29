# External facts checked against their sources (planning session, 27 Sep 2026), for bundle 32

Kept here, as the planning session wrote it on 27 September 2026, since the reason of proposal P48 (`proposals.json`)
cites it; added to the repository on 29 September 2026, after a note of the writer's session. Its two errors were taken
into the citation crosscheck of 28 September 2026 as P48 and P50, and applied in the revision that followed, not in a
separate entry and folder as its last lines planned; the file and line numbers it gives are those of d108d66.

The citation passes of 22 and 24 September could not check the software and data-release facts locally
(citation_pass_2026-09-24.md, (c)). Checked here from the sources themselves (blob-less clones):

- singlesp/DMT_NCT at 77af7aa (still its HEAD): 242 files. Licence files: fxns/brewermap/LICENSE.TXT (Apache 2.0),
  fxns/spiderplot/LICENSE.txt (BSD, Moses Yoo), fxns/violin/license.txt (BSD, Holger Hoffmann), all three bundled
  third-party MATLAB plotting functions; no licence of the release's own. README: Zenodo 10.5281/zenodo.15177511 (as
  the paper). data/FDlong.mat, data/intensity_ratings.mat, data/RegressorLZInterpscrubbedConvolvedAvg.mat present.
  -> ERROR 1: draft_v2.md:246 "the release carries no licence file" and README.md:116 "The source repository carries
  no licence file" are literally untrue.
- Imperial-MIND-lab/integrated-info-decomp at 6c5f2e9d…: "Merge pull request #4 from liuzhenqi77/updates", author
  and committer date 2026-03-14 12:44:53 +0000; the merged commit 2998072 is dated 2026-03-13 10:43:14 -0400.
  LICENSE: BSD 3-Clause (as the reference). .gitmodules: matlab -> pmediano/PhiID at a633cc1354b8… (as S3 Text §2,
  S5 Text §6). README asks users to cite Mediano et al. 2025 (PNAS) and Luppi et al. 2022 (Nat Neurosci): both cited.
  -> ERROR 2: draft_v2.md:298 "(merge of pull request #4, 13 March 2026; …)": the merge is dated 14 March 2026.
- pmediano/PhiID at a633cc1 (2023-08-24): PhiIDFull.m, PhiIDFullDiscrete.m, private/DoubleRedundancyMMI*.m; MMI only,
  no CCS (as S3 Text §2).
- rsHRF 1.7.0 exists on PyPI (its latest version); requirements.lock.txt pins numpy 2.5.3, scipy 1.18.1,
  matplotlib 3.11.1 and phyid@6c5f2e9 (as S1 and S4 Text).
- main_text_numbers.csv: the 12 flagged rows reread; all correct in their wording (row 498's "-0.830" is the checker
  reading the hyphen of "0.680-0.830" as a minus).

Proposed replacements (to be joined by V.S.'s reading notes in one round):
- draft_v2.md:246  "the release carries no licence file," -> "the release carries no licence of its own (its three
  licence files belong to third-party plotting functions it bundles),"
- draft_v2.md:298  "(merge of pull request #4, 13 March 2026;" -> "(merge of pull request #4, 14 March 2026;"
- README.md:116    "The source repository carries no licence file, and no" -> "The source repository carries no
  licence of its own (its three licence files belong to third-party plotting functions it bundles), and no"
- main_text_numbers.csv: contexts of rows near the two main-text changes, recomputed; any row for "13" of line 298.
- record: one appended entry; notes/review_2026-09-27/ with this note.
