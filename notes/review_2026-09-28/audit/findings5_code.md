## Fifth-round code audit of B26 (agent C5): the eight corrections, no critical or major defect, 5 minor findings

Paths: T = `…/b32/audit5/tree2`, V = `…/b32/audit5/vs`, K = `…/b32/audit5/kit`. My scratch folder is `…/b32/audit5/agentC5/`.

### Findings, most severe first

**1. MINOR: `b26_changes.py` pairs lines of different lengths by character similarity alone, which caused a regression from round 4.**
- **Where:** `T/notes/review_2026-09-28/checks/b26_changes.py` l.142–144 (the shortcut for a changed stretch whose two sides differ in length), l.103 (R) and l.97 (`similarity`).
- **What is wrong (a):** in such a stretch, pairing ignores the line's form with the numbers masked. Round 4's code aligned on that form, so a row whose form is unchanged was paired with itself.
  - The disposition says "lines of the same masked form are paired by position". That is not true for these stretches.
- **What is wrong (b):** the measure is matched characters over the shorter line's length. A short line that sits inside a long one therefore scores 1.0.
- **Scenario (a), tested:** table rows `| (iv) Δc only | W60 | +0.0380 | … |` and `| (v) Δc only | … |`, with row (v) deleted and the numbers moved by at most 0.005.
  - The listing shows "(iv) … → (none)" and "(v) … → (iv) …". The wrong pair scores 0.882; the true pair scores 0.857.
  - Over 40 random tables with distinct labels and one row inserted or deleted, the mis-pairing rates were:

    | numeric change | this version | round 4's version |
    |---|---|---|
    | 0.005 | 1/40 | 0/40 |
    | 0.05 | 1/40 | 0/40 |
    | 0.3 | 6/40 | 0/40 |
- **Scenario (b), tested:** old lines `(i)` and `mean residual -0.0412 over the pairs`; new lines `mean residual -0.0413 over the pairs (i) where it exists` and `note: 5 pairs left out`.
  - `(i)` is paired with the residual line, and the residual line is listed as removed.
- **Fix:**
  ```python
  # l.97
      return m / max(1, min(len(a), len(b))) if m >= 0.3 * max(len(a), len(b)) else 0.0      # not a short line inside a long one
  # l.103
      ka, kb = [skeleton(a) for _, a in aa], [skeleton(b) for _, b in bs]      # a line of the same form first
      R = [[similarity(a, b) + (ka[x] == kb[y]) for y, (_, b) in enumerate(bs)] for x, (_, a) in enumerate(aa)]
  ```
- **Tested (`agentC5/fix3/`):**
  - All my synthetic cases pair as before, including the auditor's two round-4 cases.
  - Case (b) is fixed, and the labelled tables mis-pair 0/40 at every size of change.
  - The random tables of identically shaped rows mis-pair no more than with the current code.
  - The modF listing is byte-identical to `F_changes3.txt`, and the rehearsal O2→R2 listing is unchanged.
  - Timing is unchanged: a stretch of 300 × 301 lines takes 17 s.

**2. MINOR: the evidence script decides which lines are superseded from the next attempt only.**
- **Where:** `V/b26_evidence.sh.in` l.203–207.
- **What is wrong:** attempt i is cut at the first step of attempt i+1. If attempt i+1 ran no step, nothing of attempt i is superseded. The same happens when a later attempt starts earlier than the next one.
  - An attempt runs no step when the runner refuses it, fails at the new initial write, or is killed in its first second.
- **Scenario (simulated S5, a correct run):**
  - runb26 completes with s1 failed and a traceback.
  - runb26from1 is refused ("B26 --from NOT RUN: files outside the outputs have changed") and prints 0 step lines.
  - runb26from2 re-runs from s1 to the end.
  - The summary prints `DIFFERS no traceback in the logs … [1]`.
- **Fix (replaces l.200–207; `alllog` and `superseded` stay as they are):**
  ```python
  LOGS = {u: read(H / FILES[u][0]).splitlines() for u in ATTEMPTS}
  FIRST = {u: next((STEPL.match(l).group(1) for l in LOGS[u] if STEPL.match(l)), None) for u in ATTEMPTS}
  for i, u in enumerate(ATTEMPTS):
      lf, hf = FILES[u]
      log = LOGS[u]
      steps = [l for l in log if STEPL.match(l)]
      # superseded: this attempt's lines from the first step that any later attempt started from; all of them if it ran no step and another attempt followed
      later = {FIRST[v] for v in ATTEMPTS[i + 1:] if FIRST[v]}
      cut = next((k for k, l in enumerate(log) if STEPL.match(l) and STEPL.match(l).group(1) in later), len(log))
      if not steps and i + 1 < len(ATTEMPTS):
          cut = 0
  ```
- **Tested (`agentC5/evfix/`):** S5 now gives "ok" plus a note of 1 superseded traceback. The S3 and S4 summaries are identical to the template's.

**3. MINOR: the start script does not see a unit that is still starting or stopping.**
- **Where:** `V/b26_start.sh.in` l.127.
- **What is wrong:** the check looks only at SubState `running`. A unit with ActiveState `deactivating` (for example stop-sigterm) or `activating` passes.
  - The change fixed round 4's false STOP on active/exited units, but this gap remains.
- **Scenario:** V.S. stops runb26from1 and at once starts `--from`. The two runners could overlap for the length of the stop.
- **Fix:**
  ```bash
    case "$(systemctl show "$u" -p ActiveState --value 2>/dev/null)/$(systemctl show "$u" -p SubState --value 2>/dev/null)" in
      activating/*|deactivating/*|reloading/*|*/running) stop "the unit $u is running, starting or stopping" ;;
    esac
  ```
- **Tested with a fake systemctl:** running and stop-sigterm give STOP; active/exited and failed do not.

**4. MINOR (wording): the summary's note cuts the CSV's first line at 200 characters.**
- **Where:** `V/b26_evidence.sh.in` l.194.
- **Scenario (S3):** after two resumes the note ends at "…re-run with --from partB/s1_run at … python 3.1". It omits "interrupted after 1 of 3 steps; re-run with --from partB/s2_run". The full line is only in section 4 of `evidence.txt`.
- **Fix:** `note("the CSV's first line records a resumed run: " + head)`.

**5. MINOR (documentation): large stretches can be left unpaired, and the docstrings do not say so.**
- **Where:** `b26_changes.py` l.148–153; the docstrings at l.14–18 and l.126–131.
- **What is wrong:** a part of the masked-form alignment that is a replace block of unequal lengths with more than `SMALL` (250,000) line pairs is listed with every line alone.
  - Round 4's code paired it: 600 × 601 table rows whose form changed took 29 s.
  - The current code lists all 1,201 of those lines unpaired.
  - The docstrings say such stretches are "paired by similarity".
- **Fix:** add to both docstrings: "a stretch of more than 250,000 line pairs is first aligned on the lines' form; a part of it that is still that large, with sides of unequal length, is listed unpaired".
  - No committed output comes near that size; the rehearsal's largest stretches are far smaller.

### Checked and found correct

**The runner, `notes/partB26_positive_definite.py`**
- `--selftest`: 0 failed.
- **Test repository:** a copy of runt with the new runner and two synthetic steps, 7 steps in all; B21 fails by design.
- **Initial write:** the CSV and the tables exist 4 s into a full run. The first line ends "partial: 0 of 7 steps", and the tables print "PARTIAL: 0 of the 7 steps".
- **A SIGTERM to my own group in step 1**, then these checks, all with nothing written and no temporary folder made:
  - `--check-from partB/s1_run` prints "ready".
  - `--check-from rev_assemble` is refused ("(its row: none)").
  - An unknown step and a missing step name are refused with exit 1.
- **Two more interrupted attempts, then completion:**
  - `--from s1` was interrupted in step 1: "…; interrupted after 0 of 7 steps; re-run …; partial: 0 of 7 steps".
  - A third attempt was interrupted in s2 ("partial: 4 of 7").
  - `--check-from inference_revision_run` was then refused (s2 had no row).
  - `--from partB/s2_run` completed. The first line records all three interruptions and re-runs.
- **Rows:** all 23 rows equal an uninterrupted run's in every field but `seconds`. The tables' sha256 equals the CSV's.
- **After the completed run (B21 exit status 1):** `--check-from 15_figures_v2` is refused ("(its row: exit status 1)"), and `--check-from partB/inference_revision_run` is accepted.
- **`write_atomic`:** temporary file in the same folder, file fsync, `os.replace`, folder fsync. No stray `.tmp` was left in any test. A leftover would sit inside the output folders, which the checks allow, and the next write replaces it.
- **Docstring and entry:** both match the behaviour. That includes "any number of times" and "records each interruption and re-run".

**The start script, `b26_start.sh.in`**
- **Numbering** (the template's own code with a fake systemctl):

  | state before the start | unit chosen |
  |---|---|
  | nothing | from1 |
  | a from1 log | from2 |
  | from1 log and from2 git-status file | from3 |
  | from1 log and a failed runb26from2 still loaded | from3 |
  | a loaded runb26from1 and no files | from2 |
  | only a from1 heartbeat file | from2 |

- **Running-unit check:** runb26 or runb26from1 running gives STOP. An active/exited runb26 gives no STOP; round 4's check would have stopped it. A full start with runb26 loaded gives "exists already".
- **`--check-from`:** an accepted step passes. A refused or unknown step gives STOP with the runner's message.
- **INNER:** no `${` or `$$` for the full run or for from12, and both parse. The full INNER is byte-identical to round 4's; the from INNER differs only in its file names.
- `bash -n` and shellcheck find nothing substantive.

**The evidence script, `b26_evidence.sh.in`**
- **Simulation set-up:** the template filled for a test repository, with a fake systemctl and journalctl. Each attempt was run by the template's own INNER with a 5-s heartbeat.
- **S1, a complete single run:** every item ok except pip freeze, which is an artifact of the simulated environment.
- **S2, cut short by SIGKILL and resumed once** (unit not loaded after the "reboot"):
  - The windows and the per-attempt heartbeat checks are correct.
  - A power-off, lid, suspend and dpkg line between the attempts is noted, not failed; the boots are listed.
  - Every attempt's files are copied.
- **S3, resumed twice:** three attempts are found. A lid event inside the third window and an out-of-memory line inside the second are marked DIFFERS, as they should be.
- **S4, a failed step resumed:** the traceback and CHECK FAILED line are noted as superseded, and the attempt is noted "resumed after it".
- **Short attempts:** an attempt under 330 s with no heartbeat line gets the note.
- **Window start:** GNU date parses EEST; EET falls back to the first step line, which is harmless.
- **An event that ends an attempt after its log's last write** is noted, not failed. That is right, because the attempt is superseded.
- **Rules (i) and (iv):** the evidence suffices, apart from finding 2.
  - For (iv): each attempt's log and where it stopped, its window, its heartbeat and git status, the journal lines inside and between attempts, the boots, and the CSV's first line.
  - For (i): the unchanged comparisons on the final tree.

**`b26_changes.py`**
- On a copy of modF the listing is byte-identical to `F_changes3.txt` and to round 4's version, run with `-W error`.
- On the rehearsal's O2 and R2 trees (read only; the rehearsal had ended) the listing is identical to round 4's.
- **NaN and infinity changes:** round 4's case prints "…; 1 of them a change of NaN or infinity (1 become NaN), listed first" with index 20000 first. Infinity, −infinity, NaN to finite, 0-d arrays, complex, float32, pickled scalars and the 2,000-entry cap are all correct.
- **Count of agreeing files:**
  - `agrees_table.csv` is counted as changed, and a name containing ": " and "the same " is read correctly.
  - These are counted as agreeing: PNGs with the same pixels, PDFs that differ only in their dates, npy within 10⁻⁹, a log that agrees once masked, and a CSV within 10⁻⁹.

**`check32.py`:** 15 synthetic cases give the intended results. They include infinity against a finite value, infinity against −infinity, infinity against infinity or "Infinity", NaN cases, overflow, and 10⁻¹⁰ relative differences.

**Safety:** I used no `pkill`, `killall` or pattern kill, and signalled only process groups I created (setsid with a group-ID file). TMPDIR was my scratch folder, and the rehearsal was only read.
- Before copying them, I ran read-only `git log` and `git status` in `…/codetest/runt` and `…/audit4/agentC4/rt2`. Their index files are unchanged; only the `.git` folders' mtimes moved, from git's transient lock.

**Scratch** (`…/b32/audit5/agentC5/`):
- `rt/` and `rtE/`: the test repositories.
- `runs/`: the runner outputs.
- `S1/`–`S5/`: simulated homes with `ev.out` and `evfix.out`.
- `ST/`: the start-script tests.
- `b26c/`: the pairing tests.
- `fix3/`, `evfix/`, `ST/start_fix.sh`: the tested fixes.
- `modF_changes5.txt`, `reh_new.txt`: the listings.
- `c32/`: the `check32.py` tests.
