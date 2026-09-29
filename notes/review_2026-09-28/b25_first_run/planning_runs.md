# B25 run twice by the planning session before the entry of the first run

Before writing the record's entry "The binarised estimators on the AR(1) family (B25): the first run and the correction of one check",
the planning session ran B25 to its end twice on 29 September 2026, each time in a copy of the tree outside git (so
that the outputs name `git=nogit`), with python 3.12.3, numpy 2.5.3, scipy 1.18.1 and phyid 0+untagged.8.g6c5f2e9, the
versions of the first run: at 06:55 UTC with the first run's script (`notes/partB25_binarised.py` at 820cacd, sha256
b51d052cc91189cde65de7c32cd1ebfa7b9935ee0d8899d0351a92fa23d63c90), and at 08:29 UTC with the corrected one (sha256
268656078b25ff94f13d0a644328a683630f9e83359280d1ae4cb413f1801e81, the file of the commit of that entry). Their outputs
are not committed; this note records what they showed.

- The first run's script: `checks: 150, failed 1`, the same check with the same value: `CHECK FAILED: operating
  point (0.85, 0.25): phyid's CCS atoms recomputed from its local MIs (series 4): 1.06e-12 above 1e-12`. Its
  `binarised.csv`, with its first line replaced by the first run's (`# partB25_binarised.py; git=820cacd; run 29 Sep 2026
  06:16 UTC`), has sha256 2dc288bb3357c66a8bb8954861fc13d5351f2748de83900c019e26bcdbce3479, the value the first run's
  tables give: the first run's values are reproduced bit for bit on a second machine.
- The corrected script: `checks: 150, failed 0`. The 949 lines of its `binarised.csv` after the first (the column
  names and 948 rows) equal the first run's. Its tables differ from those of the first run's script only in these
  lines: the time of the run and the sha256 of the CSV, whose first line holds that time; the count of failed checks
  (0 for 1); the ten rows of the corrected check in the ten series and its row over every replicate, whose names now
  say "local" and "sample by sample" and whose values are 0 to 8.88e-16 in the ten series (the first run's script:
  3.56e-13 to 1.06e-12) and 4e-15 over every replicate (4.82e-14), a finite value, so that no replicate gave a NaN;
  and the wall-clock (456 s; 438 s).
- The self-test of the corrected script, `b25_selftest.out` beside this note: 54 checks, 0 failed; it differs from
  that of the first run's script (`notes/review_2026-09-28/checks/b25_selftest.out`) only in its three timings.
