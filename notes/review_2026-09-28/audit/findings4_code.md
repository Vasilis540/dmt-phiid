## Fourth-round code audit of B26 (agent C4): 1 major and 7 minor findings, no critical defect

**The third round's findings.** All nine are fixed. Three fixes have gaps, covered in the findings below:
- 1 (counts survive an interruption): fixed, except for an interruption in step 1 (finding 2) and a second interruption (finding 1).
- 2 (B15's label in rule (i)): fixed.
- 3 (every flagged call kept, `bad_calls_n`, field limits): fixed.
- 4 (evidence checks restored): fixed.
- 5 (line pairing): fixed for insertions and deletions; two pairing cases remain (finding 5).
- 6 (listing details): fixed, except that a NaN or infinity pattern change is not stated (finding 6).
- 7 (B14/B15 failed reads): fixed.
- 8 (`check32.py` comparison): fixed, with an inf gap (finding 8).
- 9 (self-test summary): fixed.

**Safety.** The rehearsal (O2 pgid 18084, R2 pgid 24126) was only read and is still running. I used no `pkill`, `killall` or pattern kill; I only signalled groups I had created.
- Note for later audits: in this environment `setsid … & echo $!` does not return the session's group, because setsid forks when the job leads its own process group. `kill -- -$!` therefore targets a group that no longer exists.
- I wrote the group ID from inside the session instead: `setsid bash -c 'echo $$ > pidfile; …'`.

Paths below: T = `/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/b32/audit4/tree2`, V = `…/b32/audit4/vs`, K = `…/b32/audit4/kit`.

### Findings, most severe first

**1. MAJOR (CRITICAL if the resumed run is interrupted as well): the start and evidence scripts allow exactly one resume.**
- **Where:**
  - `V/b26_start.sh.in` l.34–44: fixed names `runb26from`, `b26_run_unit_from.log`, `b26_heartbeat_from.log`, `b26_prestatus_from.txt`. Also l.116–118 (stops if those files exist) and l.125 (stops if the unit is loaded).
  - `V/b26_evidence.sh.in` l.34–37 and l.59: `ATTEMPTS` is at most `runb26 runb26from`. Also l.130 (`FILES`) and l.307–309 (only fixed names are copied).
- **What is wrong:** rule (iv) and the runner allow any number of `--from` runs.
  - Tested on a runt copy: two SIGTERM interruptions, then completion. All rows merged correctly.
  - The disposition says the evidence script "checks every attempt's log and heartbeat".
- **Scenario:** runb26 is cut by a power-off (both attempts of the final run were), and the `--from` run is cut again.
  - `b26_start.sh --from Y` prints `STOP: /home/vilalius/b26_run_unit_from.log exists already`.
  - Without a reboot, a failed `runb26from` stays loaded as failed, so `a unit named runb26from exists already` is printed too. This also happens when a resumed run's step fails and needs another `--from`.
  - If files are renamed by hand, the evidence script neither reads nor copies the middle attempt.
- **Fix: number the attempts.** The parsing below was tested with from1, from2 and from10.
  - Start script:
    ```bash
    if [ -z "$FROM" ]; then UNIT=runb26; SFX=""; else k=1
      while [ -e /home/vilalius/b26_run_unit_from$k.log ] || [ -e /home/vilalius/b26_prestatus_from$k.txt ] \
            || [ "$(systemctl show runb26from$k -p LoadState --value 2>/dev/null)" = loaded ]; do k=$((k + 1)); done
      UNIT=runb26from$k; SFX=_from$k; fi
    LOG=/home/vilalius/b26_run_unit$SFX.log; HB=/home/vilalius/b26_heartbeat$SFX.log; PRE=/home/vilalius/b26_prestatus$SFX.txt
    ```
    Check running units with `systemctl list-units --all --plain --no-legend 'runb26*'` and SubState `running`.
  - Evidence script:
    ```bash
    ATTEMPTS="runb26"; for f in $(ls "$H"/b26_run_unit_from*.log 2>/dev/null | sort -V); do k=${f##*_from}; ATTEMPTS="$ATTEMPTS runb26from${k%.log}"; done
    lf() { if [ "$1" = runb26 ]; then echo "$H/b26_run_unit.log"; else echo "$H/b26_run_unit_${1#runb26}.log"; fi; }
    LAST=${ATTEMPTS##* }; LASTLOG=$(lf "$LAST")     # main(): L=$(lf "$u"); B=${L/run_unit/heartbeat}
    ```
  - Python summary:
    ```python
    FILES = {u: ("b26_run_unit.log", "b26_heartbeat.log") if u == "runb26" else (f"b26_run_unit_{u[6:]}.log", f"b26_heartbeat_{u[6:]}.log") for u in ATTEMPTS}
    ```
  - Copy step: `for f in "$H"/b26_run_unit*.log "$H"/b26_heartbeat*.log "$H"/b26_prestatus*.txt; do [ -f "$f" ] && cp "$f" "$E/"; done`.

**2. MINOR: no counts exist until step 1 ends, and each write of the counts is neither atomic nor durable.**
- **Where:** `T/notes/partB26_positive_definite.py` l.554–575 (first write after step 1) and l.478 (`CSVP.write_text`, no fsync).
- **Tested** on a copy with a slow first step, interrupted during step 1:
  - No CSV exists. `--from <step 1>` prints "…positive_definite.csv of a full run at … is not there" (l.361–362), as does the start script (l.72: "has left no counts").
  - A fresh run prints "the tree is not clean". The start script also stops on the existing `~/b26_*` files.
  - Step 1 takes 66–102 s in the rehearsals.
- **Also:** a power-off in a write can leave a zero-length CSV, which blocks the resume. A kill in the middle of the write could leave a truncated last row, which `--from` would keep in ROWS_OLD and miscount. This is improbable.
- **Fix (tested: with it, the step-1 interruption leaves "partial: 0 of 6 steps" and `--from rev_assemble` completes):**
  ```python
  import os
  # in write_outputs, in place of CSVP.write_text(...):
  tmp = CSVP.with_name(CSVP.name + ".tmp")
  with open(tmp, "w", encoding="utf-8") as fh:
      fh.write(csv_text); fh.flush(); os.fsync(fh.fileno())
  os.replace(tmp, CSVP)
  # before the loop:
  write_outputs(final=False)
  for kind, log, script, args in STEPS:
  ```

**3. MINOR: `--from` is not checked against the CSV.**
- **Where:** runner l.414–429; `V/b26_start.sh.in` l.69–77.
- **What is wrong:**
  - Both accept a step later than the first step that has no row, or that has a row with exit ≠ 0.
  - The runner's exit status now ignores failed rows kept from before (l.581).
- **Tested** on runt: a kept B21 exit-1 row with runner exit 0 and "=== unit exit 0".
- **Scenario:** a wrong `--from` gives a CSV with fewer than 39 step rows. The evidence marks it DIFFERS, but finding 1 leaves no way to repair it.
- **Fix (tested; it refuses `--from partB/slowB_run` when coupling_map has no row).** Place this before `TMP = mkdtemp`:
  ```python
  if FROM is not None:
      _done = {r["step"]: r["exit"] for r in csv.DictReader(io.StringIO(CSVP.read_text(encoding="utf-8").split("\n", 1)[1])) if r["kind"] == "step"}
      _gap = [n for n in NAMES[:NAMES.index(FROM)] if _done.get(n) != "0"]
      if _gap:
          sys.exit(f"B26 --from NOT RUN: {_gap[0]!r}, before {FROM!r}, has no row of a step that ran to its end; resume from it")
  ```
  Expose the same check as a `--check-from STEP` mode, and have the start script call it instead of `--steps | grep`.

**4. MINOR: the evidence of a resumed run raises false alarms and uses one time window.**
- **Where:** `V/b26_evidence.sh.in` l.193–210, 211–215, 47–53 and 110–114.
- **(a) Short attempts.** An attempt shorter than 300 s has no heartbeat line, so both heartbeat checks say DIFFERS (tested). This covers any resume from 15_figures_v2, and probably B24.
- **(b) Superseded tracebacks.** "no traceback" and "no CHECK FAILED" scan all attempts. So a rule-(iv) resume after a failed step always shows DIFFERS for the failed step's traceback, which the rule expects.
- **(c) One journal window.** logind, kernel and dpkg are read from the first attempt's start to the last one's end. That includes the reboot and the gap between attempts, when the apt timers are active again. Upgrades or lid events between attempts are reported as "during the run".
- **Fix:**
  - For an attempt shorter than 330 s with no heartbeat, print a note instead.
  - Scan tracebacks in the last attempt, plus earlier attempts' lines before the step the next attempt resumed from.
  - Filter journals and dpkg per attempt (first step line to log mtime), and list what happened between attempts as a note.
  - Add `journalctl --list-boots --no-pager | tail -5` to the evidence.

**5. MINOR: `b26_changes.py` still mis-pairs lines in two cases.**
- **Where:** `T/notes/review_2026-09-28/checks/b26_changes.py` l.108 and l.106–112.
- **(a) Equal-length replace blocks** in the masked-text alignment are paired by position, not by similarity as the disposition says.
  - Tested: old `alpha beta gamma 1` + `the residual over the pairs 2`, new `the residual over the pairs where it exists 2` + `omega psi chi 3`.
  - Listed as "alpha… → …where it exists" and "…pairs 2 → omega psi chi 3".
- **(b) Lines with identical skeletons** (numeric-only lines) shift pairs when a line is inserted and all lines change.
  - Tested: `0.101,0.201 → 0.555,0.666`, and every following pair is offset by one.
- **Impact:** nothing is hidden, since every line is printed, but the pairs that rule (i) reads are wrong.
- **Fix:**
  - Pair by position only when `tag2 == "equal"`, and send every replace block through the similarity pass.
  - When a top-level block has unequal lengths and is small (len·len ≤ 2.5e5), run that pass on the raw lines.
  - The pass is O(n·m): 500 × 490 lines took 50 s. No committed output reaches that size today.

**6. MINOR: `b26_changes.py` does not state a NaN or infinity pattern change, and it counts files by a substring that includes the file name.**
- **Where:** l.224–232, l.332–333 and l.373.
- **NaN pattern (tested):** a 23,520-entry array with all entries +1e-6 and one entry turned NaN at index 20,000 is listed as "23,520 of 23,520 entries differ … (the first 2,000 listed)". "nan" appears nowhere in the listing.
- **Counting:** `"agrees" in L[0]` includes the file name. A changed `results/agrees_table.csv` was counted as agreeing (tested). No current output name contains "agrees".
- **Fix:**
  ```python
  pat = (na != nb) | (~both_fin & ~(na & nb) & (fa != fb)); bad = pat | (d > TOL)
  ```
  - Return `int(pat.sum())` and `int((~na & nb).sum())`, print "; N of them a change of NaN or infinity (M become NaN)", and list the `pat` entries first.
  - Count with `agrees = L[0].split(": ", 1)[1].startswith(("the bytes differ; every", "the same "))`.

**7. MINOR: after a resume, the CSV and tables no longer say that an attempt was interrupted.**
- **Where:** runner l.427, which drops "; partial: k of n steps".
- **Tested:** the final head is "…; re-run with --from partB/slowA_run at …; re-run with --from partB/slowB_run at …". It shows neither interruption nor the step counts.
- **Fix:**
  ```python
  HEAD_OLD = re.sub(r"; partial: (\d+) of (\d+) steps$", r"; interrupted after \1 of \2 steps", HEAD_OLD)
  ```
  The evidence script's `"partial:" not in head` check is unaffected.

**8. MINOR: `check32.py` passes an inf in the writer's CSV.**
- **Where:** `K/check32.py` l.177–180.
- **What is wrong:** an infinite writer value against a finite re-run value gives inf/inf = nan, and `max(dmax, nan)` keeps dmax. The difference passes silently (tested: `inf` vs `1.5` gives 0).
- **Likelihood:** B25's `rec()` values are unlikely to be infinite.
- **Fix:**
  ```python
  if math.isinf(fx) or math.isinf(fy):
      nanx += fx != fy; continue
  ```

### Checked and found correct

**The correction**
- F01–F52 applied to d108d66 reproduce tree2's files byte for byte. The JSON's F entries equal code32's, and code32 changed only by finding 7's two edits.

**The runner**
- `--steps` gives 39 unique names on tree2, with `-I` and without git.
- `--selftest` passes. With forced failures it prints the FAILED list (sts shown as nan) and exits 1.
- Runt copy with two synthetic slow steps and 14,000 flagged calls, interrupted twice by SIGTERM to my own group:
  - The CSVs were "partial: 4 of 7", then "…re-run…; partial: 1 of 3", then complete with 7 step rows.
  - Kept rows are byte-identical to the earlier attempts, with no duplicate site keys.
  - A `bad_calls` field of 156,894 characters round-trips.
  - `bad_calls_n` equals the list length.
  - Step logs and the tee log hold every line printed before the kill.
  - The tables' sha256 equals the file's. The tables are made from the CSV alone, show the PARTIAL note, have no wall-clock line, and take the versions from the CSV's first line.

**The start script**
- The from-mode INNER has no `${` or `$$` and parses. The full-mode INNER is identical to round 3's.
- `bash -n` and shellcheck find nothing substantive.

**The evidence script**
- Simulated complete and once-resumed runs (the unit commands remapped to scratch) give the expected summaries.
- Checks restored:
  - Exit status 0 plus each script's last-line marker, which 6, 8 and 10 print at their ends.
  - `' M'`/`'??'` codes and `nogit`.
  - Journal readability (the Hint line is kept by the grep).
  - B21–B24 counts match the committed and modF logs (1025/22/63/10), and "check C1" matches B21's C1 checks.
- positive_definite.csv is never parsed by 6, 8 or 10.

**`b26_changes.py`**
- On a copy of modF, the listing is identical to `F_changes2.txt`. Its text parts are identical to round 3's `F_changes.txt`.
- All 1,822 CSV "l. N" locators point to the right cell.
- Insertion, deletion and table-row-loss cases pair correctly.
- NaN and inf comparisons are correct with warnings raised as errors.
- PNGs with the same pixels and PDFs differing only in dates are counted as agreeing.
- No d108d66 CSV has multi-line records.

**Other**
- B14 and B15 catch OSError and UnicodeError, and their CHECK FAILED lines reach the unit log.
- `check32.py`'s tables comparison tolerates noise-level values (4.44e-16 vs 2.22e-16).
- No section-6 step appends to outputs, creates temporary files in the repository, or reads B26's CSV or tables, which now exist during the run.

Scratch files are in `/tmp/claude-0/-home-claude/2d25c7a4-f19d-5b84-9103-2a9448d3c6aa/scratchpad/b32/audit4/agentC4/`:
- `rt/` — the three-attempt test, with `int1.out`–`int3.out` and `csv_after_int*.csv`
- `rt2/`, `home2/`, `ev_sim.out` — the resumed-run evidence simulation
- `rt4/`, `home4/`, `ev_sim4.out` — the complete-run evidence simulation
- `rt3/` — the step-1 interruption
- `rt5/` — the proposed runner fixes, tested
- `modF_changes4.txt` — the listing on the modF copy
- `b26c/` — synthetic tests of `b26_changes.py`
- `inner_from.txt` — the from-mode unit command
