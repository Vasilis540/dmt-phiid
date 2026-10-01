#!/usr/bin/env bash
# b26_evidence.sh — after B26's run: the run's summary, the comparisons of its rule (i), and the evidence for the
# planning session.
#
# Record: "The matrices that are not positive definite (B26): pre-run entry", the run and rules (i) and (iv). Run it as
# yourself once the run's log ends with "=== unit exit" (or, if the planning session asks for it, after a run that was
# cut short), before any restart or power-off:
#   bash ~/Downloads/b26_evidence.sh
# It changes nothing in the repository: nothing is added, restored or committed, and the comparisons run on the working
# tree the run left. If the run was resumed with b26_start.sh --from (once or more), it reads every attempt's logs. It
# writes, outside the repository:
#   ~/b26_evidence/          what this script prints (evidence.txt); the listing of the changes of the outputs
#                            (b26_changes.txt, by notes/review_2026-09-28/checks/b26_changes.py: rule (i) of the pre-run
#                            entry reads it); the three comparisons of the final run's outcome entry; the full diff of
#                            every changed text output; B26's tables and CSV; the runs' logs and heartbeats; git status
#                            before and after the run; the environment after the run; the system journal of the run;
#                            dpkg's log of the run; the sha256 of every output the run changed or wrote; a note on the
#                            machine; and a copy of every output the run changed or wrote, the binary ones and the
#                            figures too (outputs.tar.gz);
#   ~/b26_evidence.tar.gz    that folder, for the planning session.
set -u
REPO=/home/vilalius/dmt-phiid
RUNFULL=d5a65bdcb2cc9d073f71829c264894937dbe1dc4
NSTEPS=39
H=/home/vilalius
E=$H/b26_evidence
PY=".venv/bin/python -I"
RC=notes/planning_checks_2026-09-16/reproduction_checks
OUT="results notes/review_results manuscript/figures notes/review_computations_2026-09-14.md"   # the last rewritten by rev_assemble.py

cd "$REPO" 2>/dev/null || { echo "$REPO not found"; exit 1; }
RUN=$(git rev-parse --short "$RUNFULL")
[ -f "$H/b26_run_unit.log" ] || { echo "There is no run log at $H/b26_run_unit.log. Nothing done."; exit 1; }
# the attempts, in order: the run (the unit runb26), then each run resumed with --from (runb26from1, runb26from2, …)
ATTEMPTS="runb26"
for k in $(ls "$H" | sed -n 's/^b26_run_unit_from\([0-9][0-9]*\)\.log$/\1/p' | sort -n); do ATTEMPTS="$ATTEMPTS runb26from$k"; done
lf() { if [ "$1" = runb26 ]; then echo "$H/b26_run_unit.log"; else echo "$H/b26_run_unit_${1#runb26}.log"; fi; }
hf() { if [ "$1" = runb26 ]; then echo "$H/b26_heartbeat.log"; else echo "$H/b26_heartbeat_${1#runb26}.log"; fi; }
pf() { if [ "$1" = runb26 ]; then echo "$H/b26_prestatus.txt"; else echo "$H/b26_prestatus_${1#runb26}.txt"; fi; }
win() {  # an attempt's window, "start|end": its unit's start (else its first step line, else its git status file), its log's last write
  local L ts s
  L=$(lf "$1")
  ts=$(systemctl show "$1" -p ExecMainStartTimestamp --value 2>/dev/null)
  s=""; [ -n "$ts" ] && s=$(date -d "$ts" '+%F %T' 2>/dev/null)
  [ -n "$s" ] || s=$(grep -m1 -E '^=== [0-9]{4}-[0-9]{2}-[0-9]{2} ' "$L" | cut -c5-23)
  [ -n "$s" ] || s=$(date -r "$(pf "$1")" '+%F %T' 2>/dev/null)
  echo "$s|$(date -r "$L" '+%F %T')"
}
LAST=${ATTEMPTS##* }
LASTLOG=$(lf "$LAST")
if ! grep -q '^=== unit exit' "$LASTLOG"; then
  if [ "$(systemctl show "$LAST" -p SubState --value 2>/dev/null)" = running ]; then
    echo "The run has not ended: the unit $LAST is running and $LASTLOG has no '=== unit exit' line yet. Nothing done; run this script again when it has."
    exit 1
  fi
  echo "note: $LASTLOG has no '=== unit exit' line and the unit $LAST is not running: the run was cut short. Collecting the evidence of what it did."
fi
[ ! -e "$E" ] || mv "$E" "$E.$(date +%Y%m%d-%H%M%S)"
mkdir -p "$E"
for u in $ATTEMPTS; do echo "$u|$(win "$u")"; done > "$E/windows.txt"
T0=$(head -1 "$E/windows.txt" | cut -d'|' -f2)
T1=$(date -d "$T0 1 minute ago" '+%F %T' 2>/dev/null || echo "$T0")
END=$(date -r "$LASTLOG" '+%F %T')

main() {
  echo "B26 evidence, $(date -u '+%F %T UTC')"
  echo
  for u in $ATTEMPTS; do
    L=$(lf "$u"); B=$(hf "$u")
    echo "--- the unit $u and its log ($(grep "^$u|" "$E/windows.txt" | cut -d'|' -f2-3 | sed 's/|/ to /'))"
    systemctl show "$u" -p LoadState -p ActiveState -p SubState -p Result -p ExecMainStatus \
      -p ExecMainStartTimestamp -p ExecMainExitTimestamp 2>&1 | tee "$E/unit_$u.txt"
    echo "log: $(wc -l < "$L") lines, $(stat -c%s "$L") bytes, last written $(date -r "$L" '+%F %T'); its last two lines:"
    tail -2 "$L"
    echo "the first and the last step line, and every failed step:"
    grep -E '^=== [0-9]{4}-[0-9]{2}-[0-9]{2} ' "$L" | sed -n '1p;$p'
    grep -E '^=== STEP FAILED' "$L"
    echo "heartbeat: $( [ -f "$B" ] && { echo "$(wc -l < "$B") lines; the first and the last:"; sed -n '1p;$p' "$B"; } || echo "no heartbeat file")"
    echo
  done
  echo "--- 3. the repository"
  git log --oneline -1 | cut -c1-100
  git status --porcelain --untracked-files=all > "$E/status_after.txt"
  cp "$H/b26_prestatus.txt" "$E/status_before.txt" 2>/dev/null || echo "(no git status from before the run at $H/b26_prestatus.txt)"
  if git diff --cached --quiet; then st=none; else st=PRESENT; fi
  echo "staged changes: $st" | tee "$E/staged.txt"
  echo "under the output folders (M = modified, ?? = new):"
  git status --porcelain --untracked-files=all -- $OUT | cut -c1-2 | sort | uniq -c
  echo "new files:"
  git status --porcelain --untracked-files=all -- $OUT | grep '^??' | cut -c4-
  echo
  echo "--- 4. B26's tables"
  cat notes/review_results/partB/positive_definite_tables.md
  echo
  echo "--- b26_changes.py $RUN (every change, listed in full in b26_changes.txt; here its file lines and its last line)"
  $PY notes/review_2026-09-28/checks/b26_changes.py "$RUN" > "$E/b26_changes.txt" 2>&1
  echo $? > "$E/b26_changes.exit"
  echo "(exit status $(cat "$E/b26_changes.exit"))"
  grep -E '^#' "$E/b26_changes.txt"
  echo
  for k in 6_committed_compare 8_binary_compare 10_logs_figures_compare; do
    echo "--- $k.py $RUN"
    $PY "$RC/$k.py" "$RUN" > "$E/$k.txt" 2>&1
    echo $? > "$E/$k.exit"
    echo "(exit status $(cat "$E/$k.exit"))"
    cat "$E/$k.txt"
    echo
  done
  echo "--- the full diff of every changed text output (in diffs.txt)"
  git diff --no-color --no-ext-diff -U0 -- $(git ls-files -m -- $OUT | grep -E '\.(md|csv|txt|log)$') > "$E/diffs.txt"
  echo "$(grep -c '^diff --git' "$E/diffs.txt") files, $(wc -l < "$E/diffs.txt") lines"
  echo
  echo "--- the environment after the run"
  { echo "versions: $($PY -c 'import sys, numpy, scipy, matplotlib; print(sys.version.split()[0], numpy.__version__, scipy.__version__, matplotlib.__version__)' 2>&1)"
    d=$(diff <($PY -m pip freeze 2>/dev/null) requirements.lock.txt)
    if [ -z "$d" ]; then echo "pip freeze: identical to requirements.lock.txt"; else echo "pip freeze: DIFFERS from requirements.lock.txt"; echo "$d" | head -20; fi
  } | tee "$E/env_after.txt"
  echo
  echo "--- the system during the run ($T0 to $END; each attempt's window in windows.txt)"
  journalctl -u systemd-logind --since "$T0" --until "$END" --no-pager -o short-iso > "$E/logind.txt" 2>&1
  for u in $ATTEMPTS; do journalctl -u "$u.service" --since "$T1" --no-pager -o short-iso; done > "$E/unit_journal.txt" 2>&1
  journalctl _TRANSPORT=kernel --since "$T0" --until "$END" --no-pager -o short-iso 2>&1 | grep -v 'Lockdown:' \
    | grep -iE 'Hint: |out of memory|killed process|oom-kill|PM: suspend entry|hibernation entry|Freezing user space|thermal|throttl' > "$E/kernel.txt"
  cat /var/log/dpkg.log.1 /var/log/dpkg.log 2>/dev/null | awk -v s="$T0" -v e="$END" '($1 " " $2) >= s && ($1 " " $2) <= e' > "$E/dpkg_during_run.txt"
  journalctl --list-boots --no-pager 2>&1 | tail -5 > "$E/boots.txt"
  echo "logind journal: $(grep -vc '^-- ' "$E/logind.txt") lines; the units' journal: $(grep -vc '^-- ' "$E/unit_journal.txt") lines; kernel lines kept: $(wc -l < "$E/kernel.txt"); dpkg lines from the first start to the end: $(wc -l < "$E/dpkg_during_run.txt"); the last boots:"
  cat "$E/boots.txt"
  echo
  echo "--- the summary"
  $PY - "$E" "$RUN" "$RUNFULL" "$H" "$END" "$NSTEPS" $ATTEMPTS <<'PYEOF'
"""The health of the run, each item marked ok or DIFFERS. The comparisons above are the evidence; what they show is
read by the planning session against the pre-run entry's rule."""
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

E, RUN, RUNFULL, H, END, NSTEPS, ATTEMPTS = Path(sys.argv[1]), sys.argv[2], sys.argv[3], Path(sys.argv[4]), sys.argv[5], int(sys.argv[6]), sys.argv[7:]
OUTD = ("results/", "notes/review_results/", "manuscript/figures/")
OUTF = ("notes/review_computations_2026-09-14.md",)                       # rewritten by rev_assemble.py, a step of section 6
FILES = {u: ("b26_run_unit.log", "b26_heartbeat.log") if u == "runb26" else (f"b26_run_unit_{u[6:]}.log", f"b26_heartbeat_{u[6:]}.log")
         for u in ATTEMPTS}
bad = []


def check(label, ok, detail=""):
    if not ok:
        bad.append(label)
    print(("ok       " if ok else "DIFFERS  ") + label + (f"   [{detail}]" if detail else ""))


def note(text):
    print("note     " + text)


def read(p):
    try:
        return Path(p).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


import csv, io
csv.field_size_limit(sys.maxsize)
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
when = lambda s: datetime.strptime(s[:19].replace("T", " "), "%Y-%m-%d %H:%M:%S")
WIN = {}                                                   # each attempt's window, local time: its start, its log's last write
for l in read(E / "windows.txt").splitlines():
    u, s, e = (l.split("|") + ["", ""])[:3]
    try:
        WIN[u] = (when(s), when(e))
    except ValueError:
        pass


def in_attempt(line):
    """the attempt whose window holds a journal or dpkg line's time; None between attempts or without a time"""
    try:
        t = when(line)
    except ValueError:
        return None
    return next((u for u, (s, e) in WIN.items() if s <= t <= e), None)

# ---- the run as its CSV records it: every step, each at its end (a resumed run merges its rows)
pd_csv = read("notes/review_results/partB/positive_definite.csv")
head = pd_csv.split("\n", 1)[0]
rows = list(csv.DictReader(io.StringIO(pd_csv.split("\n", 1)[1]))) if pd_csv else []
srows = [r for r in rows if r.get("kind") == "step"]
check(f"B26's CSV: {NSTEPS} step rows, every exit status 0, at the run's commit, not partial",
      len(srows) == NSTEPS and all(r["exit"] == "0" for r in srows) and f"git={RUN};" in head and "partial:" not in head,
      f"{len(srows)} rows; exit statuses {sorted(set(r['exit'] for r in srows))}; {head[:160]}")
if "re-run with --from" in head:
    note("the CSV's first line records a resumed run: " + head)
# ---- each attempt's log and heartbeat
alllog, superseded = [], []
STEPL = re.compile(r"=== \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}  (.*)")
LOGS = {u: read(H / FILES[u][0]).splitlines() for u in ATTEMPTS}
FIRST = {u: next((STEPL.match(l).group(1) for l in LOGS[u] if STEPL.match(l)), None) for u in ATTEMPTS}
for i, u in enumerate(ATTEMPTS):
    lf, hf = FILES[u]
    log = LOGS[u]
    steps = [l for l in log if STEPL.match(l)]
    # superseded: this attempt's lines from the first step that a later attempt started from; all of them if it ran no
    # step and another attempt followed
    later = {FIRST[v] for v in ATTEMPTS[i + 1:] if FIRST[v]}
    cut = next((k for k, l in enumerate(log) if STEPL.match(l) and STEPL.match(l).group(1) in later), len(log))
    if not steps and i + 1 < len(ATTEMPTS):
        cut = 0
    alllog += log[:cut]
    superseded += log[cut:]
    if u == "runb26" and len(ATTEMPTS) == 1:
        check(f"{u}: {NSTEPS} step lines", len(steps) == NSTEPS, str(len(steps)))
        check(f"{u}: '=== all done in N min'", any(re.fullmatch(r"=== all done in \d+ min", l) for l in log))
    else:
        note(f"{u}: {len(steps)} step lines; " + ("'=== all done' present" if any(l.startswith("=== all done in ") for l in log) else "no '=== all done'"))
    failed = [l for l in log if l.startswith("=== STEP FAILED")]
    if u == ATTEMPTS[-1]:
        check(f"{u}: no step failed", not failed, " | ".join(failed[:3]))
    elif failed:
        note(f"{u}: failed steps, resumed after: " + " | ".join(failed[:3]))
    ends = bool(log) and log[-1] == "=== unit exit 0"
    if u == ATTEMPTS[-1]:
        check(f"{u}: the log ends with '=== unit exit 0'", ends, log[-1] if log else "empty")
    elif not ends:
        how = "resumed after it" if log and log[-1].startswith("=== unit exit") else "the run was cut short and resumed"
        note(f"{u}: its log ends with {log[-1][:80] if log else 'nothing'!r}: {how}")
    unit = dict(l.split("=", 1) for l in read(E / f"unit_{u}.txt").splitlines() if "=" in l)
    if unit.get("LoadState") == "loaded" and u == ATTEMPTS[-1]:
        check(f"{u}: the unit's Result=success, ExecMainStatus=0", unit.get("Result") == "success" and unit.get("ExecMainStatus") == "0",
              f"Result={unit.get('Result')} ExecMainStatus={unit.get('ExecMainStatus')}")
    elif unit.get("LoadState") != "loaded":
        note(f"{u}: the unit is not loaded (LoadState={unit.get('LoadState')}, after a restart?): its log is its record")
    hb = [l for l in read(H / hf).splitlines() if l.strip()]
    span = (WIN[u][1] - WIN[u][0]).total_seconds() if u in WIN else None
    if not hb and span is not None and span < 330:
        note(f"{u}: no heartbeat line; the attempt lasted {span:.0f} s (a line every 300 s)")
        continue
    cap = [int(m.group(1)) for m in (re.search(r"battery (\d+) %", l) for l in hb) if m]
    fall = max((max(cap[:i + 1]) - c for i, c in enumerate(cap)), default=0)
    check(f"{u}: heartbeat: the charger connected in every line, and the charge never 3 points below its highest",
          bool(hb) and not any("DISCONNECTED" in l for l in hb) and fall < 3,
          f"{len(hb)} lines; {sum('DISCONNECTED' in l for l in hb)} with the charger disconnected; largest fall {fall} points")
    try:
        t = [when(l) for l in hb]
        up = [int(m.group(1)) for m in (re.search(r"uptime (\d+) s", l) for l in hb) if m]
        gaps = [b - a for a, b in zip(up, up[1:])] if len(up) == len(hb) else [(b - a).total_seconds() for a, b in zip(t, t[1:])]
        first_gap = (t[0] - when(steps[0][4:23])).total_seconds() if t and steps else None
        end_u = datetime.fromtimestamp((H / lf).stat().st_mtime)
        last_gap = (end_u - t[-1]).total_seconds() if t else None
        check(f"{u}: heartbeat every five minutes from its start to its end (no gap above 330 s: no suspend, no stall)",
              bool(t) and max(gaps, default=0) <= 330 and first_gap is not None and first_gap <= 330 and last_gap <= 330,
              f"largest gap {max(gaps, default=0):.0f} s; first line {first_gap} s after the first step; last line {last_gap} s before the end")
    except (ValueError, IndexError, OSError) as e:
        check(f"{u}: heartbeat every five minutes from its start to its end", False, f"unreadable: {e}")
check("no traceback in the logs (but in the steps a later attempt ran again)", not any("Traceback" in l for l in alllog),
      str(sum("Traceback" in l for l in alllog)))
if any("Traceback" in l or "CHECK FAILED" in l for l in superseded):
    note(f"{sum('Traceback' in l for l in superseded)} traceback(s) and {sum('CHECK FAILED' in l for l in superseded)} CHECK FAILED "
         "line(s) in steps that a later attempt ran again")
cf = [l for l in alllog if "CHECK FAILED" in l]
cf_other = [l for l in cf if "check C1" not in l]
check("no CHECK FAILED but B21's check against check_C1_residual_vs_null.log", not cf_other,
      " | ".join(x.strip()[:110] for x in cf_other[:4]))
if len(cf) > len(cf_other):
    note(f"{len(cf) - len(cf_other)} line(s) of B21's check against the log of 17 September 2026 (the pre-run entry expects it to "
         "fail if the run-level residual changes at its fifth decimal): " + " | ".join(x.strip()[:110] for x in cf if "check C1" in x))
CK = {"B21": ("notes/review_results/partB/inference_revision_run.log", 1025), "B22": ("notes/review_results/partB/aligned_directed_run.log", 22),
      "B23": ("notes/review_results/partB/diagnostic_alternatives_run.log", 63), "B24": ("notes/review_results/partB/bandpassed_expectations_run.log", 10)}
for k, (f, n) in CK.items():
    m = re.findall(r"^   checks: (\d+) run, (\d+) failed$", read(f), re.M)
    got = (int(m[-1][0]), int(m[-1][1])) if m else None
    if k == "B21":
        check(f"{k}: {n} checks run, none failed but those against the log of 17 September 2026", got is not None and got[0] == n and got[1] <= 2, str(got))
    else:
        check(f"{k}: {n} checks run, 0 failed", got == (n, 0), str(got))
lg = read(E / "logind.txt")
if "Hint: You are currently not seeing messages" in lg or "No journal files were opened" in lg:
    note("the system journal is not readable by this user: lid, suspend and power events not checked")
else:
    ev = [l for l in lg.splitlines() if "Lockdown:" not in l
          and re.search(r"Lid closed|Lid opened|[Ss]uspend|[Hh]ibernat|The system will|Power key|powering down|rebooting", l)]
    ev_in = [l for l in ev if in_attempt(l)]
    check("no lid, suspend or power-off event in logind's journal while an attempt ran", not ev_in, " | ".join(x[-90:] for x in ev_in[:3]))
    if len(ev) > len(ev_in):
        note("logind events between the attempts: " + " | ".join(x[-90:] for x in ev if not in_attempt(x))[:400])
kraw = read(E / "kernel.txt")
if "Hint: You are currently not seeing messages" in kraw or "No journal files were opened" in kraw:
    note("the kernel's journal is not readable by this user: out-of-memory kills and suspends not checked there")
else:
    kl = kraw.splitlines()
    kev = [l for l in kl if re.search(r"(?i)out of memory|killed process|oom-kill|PM: suspend entry|hibernation entry|Freezing user space", l)]
    kev_in = [l for l in kev if in_attempt(l)]
    check("no out-of-memory kill or suspend in the kernel's journal while an attempt ran", not kev_in, " | ".join(x[-90:] for x in kev_in[:3]))
    if len(kev) > len(kev_in):
        note("kernel events between the attempts: " + " | ".join(x[-90:] for x in kev if not in_attempt(x))[:400])
dp = read(E / "dpkg_during_run.txt").splitlines()
dp_in = [l for l in dp if in_attempt(l)]
check("no package installed, upgraded or removed while an attempt ran (dpkg's log)", not dp_in, " | ".join(dp_in[:3]))
if len(dp) > len(dp_in):
    note(f"{len(dp) - len(dp_in)} dpkg line(s) between the attempts (the start script checks the environment again at each "
         "start): " + " | ".join(l for l in dp if not in_attempt(l))[:300])
if len(ATTEMPTS) > 1:
    note("the last boots: " + " | ".join(read(E / "boots.txt").splitlines()[-3:]))
env = read(E / "env_after.txt")
check("the environment after the run: 3.12.3 2.5.3 1.18.1 3.11.1, pip freeze identical to requirements.lock.txt",
      "versions: 3.12.3 2.5.3 1.18.1 3.11.1" in env and "pip freeze: identical to requirements.lock.txt" in env)
check("HEAD is the run's commit", git("rev-parse", "HEAD").strip() == RUNFULL)
check("nothing staged", read(E / "staged.txt").strip() == "staged changes: none")
after = read(E / "status_after.txt").splitlines()
path = lambda l: l[3:].strip('"')
outside = [l for l in after if not path(l).startswith(OUTD) and path(l) not in OUTF]
check("nothing changed outside the output folders", not outside, "; ".join(outside[:5]))
codes = sorted({l[:2] for l in after if path(l).startswith(OUTD) or path(l) in OUTF} - {" M", "??"})
check("under the output folders only modified (' M') and new ('??') files", not codes, " ".join(repr(c) for c in codes))
new = sorted(path(l) for l in after if l.startswith("??"))
B26F = ["notes/review_results/partB/positive_definite.csv", "notes/review_results/partB/positive_definite_run.log",
        "notes/review_results/partB/positive_definite_tables.md"]
check("the new files are B26's three", new == B26F, "; ".join(new[:6]))
changed = [p for p in git("ls-files", "-m", "-o", "--exclude-standard", "--", *OUTD, *OUTF).split("\n") if p.endswith((".md", ".csv", ".txt", ".log"))]
SHA = re.compile(r"\bgit[= ]([0-9a-f]{7,40}(?:-dirty)?)")
dirty, nogit, other = [], [], []
for p in changed:
    txt = read(p)
    if f"{RUN}-dirty" in txt:
        dirty.append(p)
    old = git("show", f"{RUNFULL}:{p}")
    if txt.count("nogit") > old.count("nogit"):
        nogit.append(p)
    if set(SHA.findall(txt)) - set(SHA.findall(old)) - {RUN}:
        other.append(p)
check("no output names -dirty", not dirty, "; ".join(dirty[:5]))
check("no output gains a 'nogit'", not nogit, "; ".join(nogit[:5]))
check(f"every git SHA an output gains is {RUN}", not other, "; ".join(other[:5]))
tb = read("notes/review_results/partB/positive_definite_tables.md")
m = re.search(r"not positive definite (\d[\d,]*\d|\d)", tb)
note(f"B26's tables: {m.group(0) if m else 'no count found'} (summed over the steps; the text quotes B4's level lines)")
b21 = re.search(r"^EXPECTATIONS = \(([^)]*)\)", read("notes/partB21_inference_revision.py"), re.M)
held = tuple(float(x) for x in b21.group(1).split(",")) if b21 else None


def resid_w60(p, cond):
    r = re.search(r"^\| " + re.escape(cond) + r" \| W60 \|(?:[^|]*\|){3} ([+-]\d\.\d{4}) ± ", read(p), re.M)
    return float(r.group(1)) if r else None


nl = re.search(r"null residual change: .*DiD ([+-]\d\.\d{4})", read("notes/review_results/logs/review_v2_residual_null.log"))
regen = (resid_w60("notes/review_results/partB/calibration_filtered_tables.md", "(i) Δa (post filter)"),
         resid_w60("notes/review_results/partB/calibration_tables.md", "(i) Δa = −0.015, Δc = 0"),
         float(nl.group(1)) if nl else None)
check("B21's three expectations (B17b's and B17's (i) residual DiD at W = 60, the null's DiD) as the regenerated outputs print them",
      held is not None and held == regen, f"held {held}; regenerated {regen}")
check("b26_changes.py ran to the end", read(E / "b26_changes.exit").strip() == "0" and "file(s) examined" in read(E / "b26_changes.txt"),
      read(E / "b26_changes.exit").strip())
LASTL = {"6_committed_compare": "untracked files under the output folders: ", "8_binary_compare": "summary: ",
         "10_logs_figures_compare": "10_logs_figures_compare: "}
for k, h_ in LASTL.items():
    ex = read(E / f"{k}.exit").strip()
    check(f"{k}.py ran to the end (exit status 0, its last line written)", ex == "0" and h_ in read(E / f"{k}.txt"), f"exit status {ex}")
print()
print("SUMMARY: every item above holds." if not bad else f"SUMMARY: {len(bad)} item(s) marked DIFFERS.")
print("Whatever the summary says, send ~/b26_evidence.tar.gz to the planning session and change nothing in the repository.")
PYEOF
}

main 2>&1 | tee "$E/evidence.txt"

for f in "$H"/b26_run_unit*.log "$H"/b26_heartbeat*.log "$H"/b26_prestatus*.txt; do
  [ -f "$f" ] && cp "$f" "$E/"
done
cp notes/review_results/partB/positive_definite.csv notes/review_results/partB/positive_definite_tables.md "$E/" 2>/dev/null
git ls-files -m -o --exclude-standard -z -- $OUT | xargs -0 sha256sum > "$E/outputs.sha256"
{ uname -srvm; grep PRETTY_NAME /etc/os-release; lscpu | grep -E '^Model name|^CPU\(s\)'; free -h | sed -n 1,2p; } > "$E/machine.txt" 2>&1
git ls-files -m -o --exclude-standard -z -- $OUT | tar --null -T - -czf "$E/outputs.tar.gz"
tar -czf "$H/b26_evidence.tar.gz" -C "$H" b26_evidence
echo
echo "written: $(ls "$E" | wc -l) files in $E; outputs listed in outputs.sha256 and copied into outputs.tar.gz: $(wc -l < "$E/outputs.sha256")"
ls -l "$H/b26_evidence.tar.gz"
echo "Send $H/b26_evidence.tar.gz to the planning session."
