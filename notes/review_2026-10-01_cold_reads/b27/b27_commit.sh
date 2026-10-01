#!/usr/bin/env bash
# b27_commit.sh — commits the outputs of B27, B28, B29 and B16c exactly as the run wrote them, with the unit's log and
# heartbeat as the run's evidence, and pushes that commit.
#
# Run it as yourself, on the laptop the run was made on, once the unit's log ends with "=== unit exit 0":
#   bash ~/dmt-phiid/notes/review_2026-10-01_cold_reads/b27/b27_commit.sh
# It checks everything first and changes nothing unless every check holds:
#   - the repository is on master, at the commit of the pre-run entries, and origin/master is there too;
#   - the unit runb27 is no longer running and its log ends with "=== unit exit 0", with the four step lines;
#   - nothing is staged, and `git status` lists exactly the 29 files the run writes (all new) and nothing else;
#   - every table, CSV and log carries the commit of the run (git=<HEAD>, not "-dirty"), and each log ends "done (";
#   - the environment is still the pinned one (pip freeze identical to requirements.lock.txt).
# Then it copies the unit's log and the heartbeat into notes/review_2026-10-01_cold_reads/b27/ (b27_unit.log,
# b27_heartbeat.log), writes outputs.sha256 (the sha256 of the 29 files) and evidence.txt there, commits those 33 files
# and nothing else (as vilalius <sampalisvasilis@gmail.com>), checks the commit, and pushes it. Run again after a stop,
# it resumes: once the commit is made it checks it again and only pushes.
set -u
REPO=/home/vilalius/dmt-phiid
H=/home/vilalius
SUBJ_TEXT='Round 24 (1 of 4): the cold reads of 1 October 2026; B27, B28, B29 and B16c, scripts and pre-run entries'
SUBJ_RUN='Round 24 (2 of 4): B27, B28, B29 and B16c, the outputs as the run wrote them'
FOLDER=notes/review_2026-10-01_cold_reads
EVID=$FOLDER/b27
OUTPUTS='notes/review_results/partB/baseline_gap_tables.md
notes/review_results/partB/baseline_gap.csv
notes/review_results/partB/baseline_gap_run.log
notes/review_results/partB/matched_slope_tables.md
notes/review_results/partB/matched_slope.csv
notes/review_results/partB/matched_slope_run.log
notes/review_results/partB/censoring_tables.md
notes/review_results/partB/censoring.csv
notes/review_results/partB/censoring_run.log
notes/review_results/partB/prewhiten_fixed_tables.md
notes/review_results/partB/prewhiten_fixed_run.log
notes/review_results/inference_rows_prewhiten_fixed.csv
notes/review_results/inference_rows_prewhiten_fixed.pkl
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_gsr_mmi_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_gsr_mmi_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_gsr_ccs_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_gsr_ccs_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_demean_mmi_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_demean_mmi_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_demean_ccs_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar10_ts_demean_ccs_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_gsr_mmi_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_gsr_mmi_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_gsr_ccs_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_gsr_ccs_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_demean_mmi_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_demean_mmi_bins.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_demean_ccs_win60.npy
notes/review_results/partB/prewhiten_fixed_atoms_ar20_ts_demean_ccs_bins.npy'
TABLES='notes/review_results/partB/baseline_gap_tables.md
notes/review_results/partB/matched_slope_tables.md
notes/review_results/partB/censoring_tables.md
notes/review_results/partB/prewhiten_fixed_tables.md'
CSVS='notes/review_results/partB/baseline_gap.csv
notes/review_results/partB/matched_slope.csv
notes/review_results/partB/censoring.csv
notes/review_results/inference_rows_prewhiten_fixed.csv'
LOGS='notes/review_results/partB/baseline_gap_run.log
notes/review_results/partB/matched_slope_run.log
notes/review_results/partB/censoring_run.log
notes/review_results/partB/prewhiten_fixed_run.log'
LOG=$H/b27_run_unit.log
HB=$H/b27_heartbeat.log
EVIDENCE_FILES="$EVID/b27_unit.log
$EVID/b27_heartbeat.log
$EVID/outputs.sha256
$EVID/evidence.txt"
fail() { echo "STOP: $*"; echo "Nothing has been committed or pushed. Send the planning session the whole output."; exit 1; }
fail_after() { echo "STOP: $*"; echo "The commit is made on this laptop but NOT pushed; do not push it by hand. Send the planning session the whole output."; exit 1; }
check_commit() {  # the commit $1: its parent, subject, author and files
  [ "$(git log -1 --format=%s "$1^")" = "$SUBJ_TEXT" ] || { echo "its parent is not the commit of the pre-run entries"; return 1; }
  [ "$(git log -1 --format=%s "$1")" = "$SUBJ_RUN" ] || { echo "its subject is not the expected one"; return 1; }
  [ "$(git log -1 --format='%an <%ae>' "$1")" = "vilalius <sampalisvasilis@gmail.com>" ] || { echo "its author is not vilalius <sampalisvasilis@gmail.com>"; return 1; }
  [ "$(git diff --name-status "$1^" "$1" | awk '$1!="A"' | wc -l)" = 0 ] || { echo "it modifies, deletes or renames files"; return 1; }
  [ "$(git diff --name-only "$1^" "$1" | sort)" = "$(printf '%s\n%s\n' "$OUTPUTS" "$EVIDENCE_FILES" | sort)" ] || { echo "it does not add exactly the 29 outputs and the 4 evidence files"; return 1; }
  while read -r h f; do
    [ "$(git show "$1:$f" | sha256sum | cut -c1-64)" = "$h" ] || { echo "$f in the commit does not have the sha256 of outputs.sha256"; return 1; }
  done < <(git show "$1:$EVID/outputs.sha256")
  return 0
}

cd "$REPO" 2>/dev/null || fail "$REPO not found"
echo "branch: $(git rev-parse --abbrev-ref HEAD)   HEAD: $(git log --oneline -1 | cut -c1-100)"
[ "$(git rev-parse --abbrev-ref HEAD)" = master ] || fail "not on master"
git fetch -q origin 2>/dev/null || echo "(could not reach GitHub to refresh origin/master; using the last known one)"

if [ "$(git log -1 --format=%s HEAD)" != "$SUBJ_TEXT" ]; then
  # resume: the commit may be made already
  if check_commit HEAD >/dev/null 2>&1; then
    echo "The outputs commit is already made: $(git log --oneline -1 | cut -c1-100)"
  else
    fail "master is neither at the commit of the pre-run entries nor at the outputs commit: $(check_commit HEAD)"
  fi
else
  [ "$(git rev-parse -q --verify origin/master)" = "$(git rev-parse HEAD)" ] || fail "origin/master is not at HEAD"
  RUN=$(git rev-parse --short=7 HEAD)
  # ---- the unit
  st=$(systemctl show runb27 -p ActiveState --value 2>/dev/null)/$(systemctl show runb27 -p SubState --value 2>/dev/null)
  echo "unit runb27: $st"
  case "$st" in activating/*|deactivating/*|reloading/*|*/running) fail "the unit runb27 is still running" ;; esac
  [ -s "$LOG" ] || fail "$LOG is missing or empty"
  [ -s "$HB" ] || fail "$HB is missing or empty (the run was shorter than five minutes?)"
  last=$(tail -1 "$LOG")
  [ "$last" = "=== unit exit 0" ] || fail "the unit's log does not end with '=== unit exit 0' (its last line: ${last:0:200})"
  [ "$(grep -c '^=== .*  notes/partB.*\.py   -> ' "$LOG")" = 4 ] || fail "the unit's log does not hold the four step lines"
  ! grep -q '^=== step ' "$LOG" || fail "a step failed: $(grep '^=== step ' "$LOG")"
  ! grep -q 'Traceback' "$LOG" || fail "the unit's log holds a traceback"
  T1=$(grep -m1 '^=== ' "$LOG" | cut -c5-23); T2=$(stat -c %y "$LOG" | cut -c1-19)
  echo "the run: started $T1, the log last written $T2 (local time)"
  # ---- the working tree
  [ -z "$(git diff --cached --name-only)" ] || fail "something is staged: $(git diff --cached --name-only | head -5 | tr '\n' ' ')"
  got=$(git status --porcelain --untracked-files=all | sort)
  want=$(echo "$OUTPUTS" | sed 's/^/?? /' | sort)
  if [ "$got" != "$want" ]; then
    echo "git status differs from the expected one (lines only in yours with >, only in the expected with <):"
    diff <(echo "$want") <(echo "$got") | grep '^[<>]' | head -20
    fail "the working tree does not hold exactly the 29 new files the run writes"
  fi
  # ---- the headers
  while read -r f; do
    [ "$(sed -n 2p "$f")" = "git=$RUN" ] || fail "$f: its second line is not 'git=$RUN' ($(sed -n 2p "$f" | cut -c1-60))"
  done <<< "$TABLES"
  while read -r f; do
    head -1 "$f" | grep -q "git=$RUN\$" || fail "$f: its first line does not end with 'git=$RUN' ($(head -1 "$f" | cut -c1-80))"
  done <<< "$CSVS"
  while read -r f; do
    [ "$(head -1 "$f")" = "git=$RUN" ] || fail "$f: its first line is not 'git=$RUN'"
    tail -1 "$f" | grep -q '^done (' || fail "$f: its last line is not the script's 'done (' line"
  done <<< "$LOGS"
  ! grep -l -- '-dirty' $(echo "$TABLES" "$CSVS" "$LOGS") >/dev/null 2>&1 || fail "an output carries '-dirty'"
  echo "the 29 files are in place; every table, CSV and log carries git=$RUN; the four logs end with 'done ('"
  # ---- the environment
  V=$(.venv/bin/python -I -c 'import sys, numpy, scipy, matplotlib; print(sys.version.split()[0], numpy.__version__, scipy.__version__, matplotlib.__version__)' 2>&1)
  [ "$V" = "3.12.3 2.5.3 1.18.1 3.11.1" ] || fail "not the pinned versions: $V"
  ENVD=$(diff <(.venv/bin/python -I -m pip freeze 2>/dev/null) requirements.lock.txt)
  [ -z "$ENVD" ] || { echo "$ENVD" | head -20; fail "the packages in .venv differ from requirements.lock.txt"; }
  echo "environment: the pinned versions; pip freeze identical to requirements.lock.txt"
  # ---- the evidence
  mkdir -p "$EVID"
  cp "$LOG" "$EVID/b27_unit.log"; cp "$HB" "$EVID/b27_heartbeat.log"
  echo "$OUTPUTS" | tr '\n' '\0' | xargs -0 sha256sum > "$EVID/outputs.sha256"
  steps=$(grep '^=== ' "$LOG" | sed 's/  */ /g')
  {
    echo "The run of B27, B28, B29 and B16c (notes/review_2026-10-01_cold_reads/b27/b27_start.sh, the unit runb27)"
    echo "commit of the run: $RUN ($(git rev-parse HEAD))"
    echo "started (local time): $T1; the unit's log last written: $T2"
    echo "python/numpy/scipy/matplotlib: $V; pip freeze identical to requirements.lock.txt"
    echo "data clone external/DMT_NCT at $(git -C external/DMT_NCT rev-parse --short=7 HEAD 2>/dev/null || echo unknown)"
    echo "the unit's step lines and its exit line:"
    echo "$steps"
    echo "heartbeat lines: $(grep -c . "$HB"); charger DISCONNECTED in $(grep -c DISCONNECTED "$HB") of them; largest gap between lines: $(awk '{split($2,t,":"); s=t[1]*3600+t[2]*60+t[3]; if (NR>1 && s-p>m) m=s-p; p=s} END {print m+0}' "$HB") s"
    echo "git status before the run (b27_prestatus.txt): $(wc -l < "$H/b27_prestatus.txt" 2>/dev/null || echo 0) lines"
    echo "outputs: 29 files, sha256 in outputs.sha256; committed as the run wrote them by b27_commit.sh"
  } > "$EVID/evidence.txt"
  cat "$EVID/evidence.txt"
  # ---- the commit
  MSGFILE=$(mktemp)
  {
    echo "$SUBJ_RUN"
    echo
    echo "B27, B28, B29 and B16c (record, their pre-run entries, the paragraph \"The run\" of each): the four"
    echo "scripts run in place at $RUN by the unit runb27"
    echo "(notes/review_2026-10-01_cold_reads/b27/b27_start.sh) on V.S.'s machine, in the order of run_all.sh,"
    echo "each as its nstep runs it, started $T1 (local time), every step with exit status 0"
    echo "and the unit with exit status 0. The 29 files the run wrote (B27: baseline_gap_tables.md, .csv and"
    echo "_run.log; B28: matched_slope_*; B29: censoring_*; B16c: prewhiten_fixed_tables.md and _run.log,"
    echo "sixteen atom arrays and inference_rows_prewhiten_fixed.csv and .pkl), as the run wrote them, each"
    echo "table, CSV and log with git=$RUN; with the unit's log, the heartbeat, the sha256 of the 29 files"
    echo "and the evidence summary in notes/review_2026-10-01_cold_reads/b27/. The outcome entries and the"
    echo "text that reports the run follow in the next commit."
    echo
    echo "Co-Authored-By: Claude Fable 5.1 <noreply@anthropic.com>"
    echo "Claude-Session: https://claude.ai/code/session_0172Ln49VR8FQoNbX2oVTzzo"
  } > "$MSGFILE"
  printf '%s\n%s\n' "$OUTPUTS" "$EVIDENCE_FILES" | tr '\n' '\0' | xargs -0 git add -- || fail "git add failed"
  [ "$(git diff --cached --name-only | sort)" = "$(printf '%s\n%s\n' "$OUTPUTS" "$EVIDENCE_FILES" | sort)" ] || { git reset -q; fail "the staged files are not exactly the 33"; }
  git -c user.name=vilalius -c user.email=sampalisvasilis@gmail.com commit -q -F "$MSGFILE" || { git reset -q; fail "git commit failed"; }
  rm -f "$MSGFILE"
  echo "committed: $(git log --oneline -1 | cut -c1-100)"
fi
r=$(check_commit HEAD) || fail_after "the commit does not check: $r"
[ -z "$(git status --porcelain --untracked-files=all)" ] || fail_after "git status is not empty after the commit"
echo "the commit checks: the 29 outputs and the 4 evidence files, each with the sha256 of outputs.sha256; nothing else changed"
TIP=$(git rev-parse HEAD)
if [ "$(git rev-parse -q --verify origin/master)" = "$TIP" ]; then
  echo "Already pushed: origin/master is $(git rev-parse --short=7 HEAD)."
else
  git push origin master || fail_after "the push failed: run this script again to push"
fi
[ "$(git rev-parse -q --verify origin/master)" = "$TIP" ] || fail_after "origin/master is not the outputs commit after the push"
echo "DONE: master and origin/master are at $(git rev-parse --short=7 HEAD). Tell the planning session."
