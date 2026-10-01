#!/usr/bin/env bash
# b27_start.sh — checks the conditions of the run of B27, B28, B29 and B16c, then starts it.
#
# Record: the pre-run entries "The pre-injection gap and the per-subject relations (B27): pre-run entry", "The
# per-subject slope under a pure autocorrelation change of the data's heterogeneity (B28): pre-run entry", "The
# replaced volumes and the autocorrelation (B29): pre-run entry" and "Prewhitening at fixed orders (B16c): pre-run
# entry" (each entry's paragraph "The run").
# Uses, all as yourself (vilalius, not with sudo), from any folder:
#   bash ~/dmt-phiid/notes/review_2026-10-01_cold_reads/b27/b27_start.sh --check     every check; starts nothing
#   bash ~/dmt-phiid/notes/review_2026-10-01_cold_reads/b27/b27_start.sh             every check, then the run
# Nothing starts unless every check passes; each failed check prints a STOP line. The script changes nothing in the
# repository. Once the checks pass, sudo asks for your password; the system's automatic package updates are paused
# until the next restart (so that nothing is upgraded while the run is going), and the run starts as the root transient
# unit "runb27", which runs the four scripts as vilalius, in the order of run_all.sh and as its nstep runs them (each
# script's output tee'd into its log under notes/review_results/partB/), inside a sleep, idle, lid-switch and shutdown
# inhibitor, with a heartbeat line every five minutes. About an hour (B28 about 40 minutes, B16c about 21, B27 and
# B29 seconds). When the unit's log ends with "=== unit exit 0", run b27_commit.sh.
set -u
REPO=/home/vilalius/dmt-phiid
SUBJ_TEXT='Round 24 (1 of 4): the cold reads of 1 October 2026; B27, B28, B29 and B16c, scripts and pre-run entries'                                   # the subject of the commit that holds the scripts and the pre-run entries
SCRIPTS='686b2a5c152dd8d21abfe37d541ec665d6d57fdccc23924bec5812854f85fdfb  notes/partB27_baseline_gap.py
98e4338652af1ea40d9310c8b9d30daa9f37215e52faa46cc69b83a4cac714ba  notes/partB28_matched_slope.py
e9714919e9456779be7a32a3944b050579b242e0d4d68d151d8116ee50729039  notes/partB29_censoring.py
35142d470db694d82bbc5a5235b0b61b1ce5ed6bc91bba9226b21d21d46cb428  notes/partB16c_prewhiten_fixed.py'
STEPS='partB/baseline_gap_run notes/partB27_baseline_gap.py
partB/matched_slope_run notes/partB28_matched_slope.py
partB/censoring_run notes/partB29_censoring.py
partB/prewhiten_fixed_run notes/partB16c_prewhiten_fixed.py'
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
MODE=start
while [ $# -gt 0 ]; do
  case "$1" in
    --check) MODE=check ;;
    *) echo "STOP: unknown argument $1"; exit 1 ;;
  esac
  shift
done
H=/home/vilalius
UNIT=runb27
LOG=$H/b27_run_unit.log                                    # the unit's log: everything the four scripts print, with the step lines
HB=$H/b27_heartbeat.log                                    # the heartbeat
PRE=$H/b27_prestatus.txt                                   # git status before the run, for b27_commit.sh
go=1
stop() { echo "STOP: $*"; go=0; }
charger() {  # "connected" if a mains or USB power supply is online (a wireless mouse's battery does not count)
  for d in /sys/class/power_supply/*; do
    case "$(cat "$d/type" 2>/dev/null)" in Mains|USB*) grep -qxE "[12]" "$d/online" 2>/dev/null && { echo connected; return; } ;; esac
  done
  echo "NOT connected"
}

cd "$REPO" 2>/dev/null || { echo "STOP: $REPO not found"; exit 1; }
echo "now: $(date -u '+%F %T UTC')  ($(date '+%F %T %Z'))   mode: $MODE"
[ "$(id -un)" = vilalius ] || stop "run this script as vilalius, without sudo"

# ---------------------------------------------------------------- the commit
echo "branch: $(git rev-parse --abbrev-ref HEAD)   HEAD: $(git log --oneline -1 | cut -c1-100)"
[ "$(git rev-parse --abbrev-ref HEAD)" = master ] || stop "not on master"
[ "$(git log -1 --format=%s HEAD)" = "$SUBJ_TEXT" ] || stop "HEAD is not the commit of the pre-run entries (pull bundle 35A first: pull35a.sh)"
[ "$(git rev-parse -q --verify origin/master)" = "$(git rev-parse HEAD)" ] || stop "origin/master is not HEAD: push first (pull35a.sh)"
while read -r h f; do
  [ -f "$f" ] || stop "missing $f"
  [ "$(sha256sum < "$f" | cut -c1-64)" = "$h" ] || stop "$f is not the script the planning session built"
done <<< "$SCRIPTS"
for t in "The pre-injection gap and the per-subject relations (B27): pre-run entry" \
         "The per-subject slope under a pure autocorrelation change of the data's heterogeneity (B28): pre-run entry" \
         "The replaced volumes and the autocorrelation (B29): pre-run entry" \
         "Prewhitening at fixed orders (B16c): pre-run entry"; do
  grep -qF "## $t, " manuscript/analysis_record.md || stop "the record has no entry \"$t\""
done
echo "the four scripts and the four pre-run entries are in place"

# ---------------------------------------------------------------- the working tree
t=$(git status --porcelain --untracked-files=all)
[ -z "$t" ] || stop "the working tree is not clean (the run requires it): $(echo "$t" | head -5 | tr '\n' ' ')"
while read -r f; do
  [ ! -e "$f" ] || stop "$f exists already (from an earlier start?): send this output to the planning session"
done <<< "$OUTPUTS"

# ---------------------------------------------------------------- the data
U=$(git -C external/DMT_NCT rev-parse HEAD 2>/dev/null)
echo "data clone external/DMT_NCT: ${U:-not a git clone}"
case "$U" in 77af7aa*) ;; *) stop "external/DMT_NCT is not at upstream commit 77af7aa" ;; esac
t=$(git -C external/DMT_NCT status --porcelain --untracked-files=no 2>/dev/null)
[ -z "$t" ] || stop "external/DMT_NCT has modified or missing tracked files: $(echo "$t" | head -5 | tr '\n' ' ')"
for f in external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat external/DMT_NCT/data/FDlong.mat; do
  [ -s "$f" ] || stop "missing $f"
done

# ---------------------------------------------------------------- the pinned environment
V=$(.venv/bin/python -I -c 'import sys, numpy, scipy, matplotlib; print(sys.version.split()[0], numpy.__version__, scipy.__version__, matplotlib.__version__)' 2>&1)
echo "versions: $V   (pinned: 3.12.3 2.5.3 1.18.1 3.11.1)"
[ "$V" = "3.12.3 2.5.3 1.18.1 3.11.1" ] || stop "not the pinned versions"
t=$(diff <(.venv/bin/python -I -m pip freeze 2>/dev/null) requirements.lock.txt)
if [ -z "$t" ]; then
  echo "environment: pip freeze of .venv identical to requirements.lock.txt ($(grep -c . requirements.lock.txt) packages)"
else
  stop "the packages in .venv differ from requirements.lock.txt (< installed, > requirements.lock.txt):"
  echo "$t" | head -20
fi
for f in notes/partB27_baseline_gap.py notes/partB28_matched_slope.py notes/partB29_censoring.py notes/partB16c_prewhiten_fixed.py; do
  .venv/bin/python -I -c 'import ast, sys; ast.parse(open(sys.argv[1], encoding="utf-8").read())' "$f" 2>/dev/null || stop "$f does not parse"
done
echo "the four scripts parse"

# ---------------------------------------------------------------- the conditions
for p in HandleLidSwitch HandleLidSwitchExternalPower HandleLidSwitchDocked; do
  v=$(busctl get-property org.freedesktop.login1 /org/freedesktop/login1 org.freedesktop.login1.Manager "$p" 2>/dev/null \
      | sed -n 's/^s "\(.*\)"$/\1/p')
  echo "logind $p (in effect): ${v:-unreadable}"
  [ "$v" = ignore ] || stop "$p is not 'ignore' in the running system (the settings of the final run: see the steps file)"
done
ch=$(charger)
echo "power: charger $ch, battery $(cat /sys/class/power_supply/BAT*/capacity 2>/dev/null | head -1) % ($(cat /sys/class/power_supply/BAT*/status 2>/dev/null | head -1))"
[ "$ch" = connected ] || stop "connect the charger"
for f in "$LOG" "$HB" "$PRE"; do
  [ ! -e "$f" ] || stop "$f exists already (from an earlier start?): send this output to the planning session"
done
AV=$(df -BG --output=avail "$REPO" | tail -1 | tr -dc 0-9)
echo "disk: ${AV:-?} GB free   memory: $(free -g | awk '/Mem:/{print $7}') GB available"
[ "${AV:-0}" -ge 2 ] || stop "less than 2 GB free on the disk"
for u in $(systemctl list-units --all --plain --no-legend 'runb2*' 2>/dev/null | awk '{print $1}'); do
  case "$(systemctl show "$u" -p ActiveState --value 2>/dev/null)/$(systemctl show "$u" -p SubState --value 2>/dev/null)" in
    activating/*|deactivating/*|reloading/*|*/running) stop "the unit $u is running, starting or stopping" ;;
  esac
done
[ "$(systemctl show "$UNIT" -p LoadState --value 2>/dev/null)" != loaded ] || stop "a unit named $UNIT exists already"

if [ "$MODE" = check ]; then
  echo
  if [ "$go" = 1 ]; then echo "READY: every check passed. Start the run with: bash $REPO/notes/review_2026-10-01_cold_reads/b27/b27_start.sh"
  else echo "NOT READY. Fix what the STOP lines say and run this again, or send this whole output to the planning session."; fi
  exit $((1 - go))
fi
for u in apt-daily.service apt-daily-upgrade.service; do
  case "$(systemctl show "$u" -p ActiveState --value 2>/dev/null)" in
    active|activating|deactivating|reloading) stop "the system's automatic update ($u) is running: wait ten minutes, then run this script again" ;;
  esac
done
for pr in dpkg apt apt-get; do
  pgrep -x "$pr" >/dev/null && stop "a package installation ($pr) is running: wait until it has finished, then run this script again"
done
if [ "$go" != 1 ]; then
  echo
  echo "NOT STARTED. Fix what the STOP lines say, or send this whole output to the planning session."
  exit 1
fi

# ---------------------------------------------------------------- the run
# The unit's command: the four scripts as vilalius, each as run_all.sh's nstep runs it (python -u, its output tee'd
# into notes/review_results/<log>.log), everything written to the unit's log, a heartbeat line every five minutes in
# the heartbeat file, a line "=== step <script> exit <status>" if a step fails (the later steps are then not run), and
# the line "=== unit exit <status>". The whole command runs inside systemd-inhibit, which blocks sleep, idle, the lid
# switch and shutdown until it ends. It is put together from single-quoted pieces and the two file names (no
# dollar-brace and no double dollar in it: systemd would expand them).
INNER='cd /home/vilalius/dmt-phiid || exit 1
export HOME=/home/vilalius
exec > '"$LOG"' 2>&1
( while sleep 300; do printf "%s  uptime %s s, log %s bytes, available memory %s GB, battery %s %% (%s), charger %s\n" "$(date "+%F %T")" "$(cut -d. -f1 /proc/uptime)" \
    "$(stat -c%s '"$LOG"')" "$(free -g | awk "/Mem:/{print \$7}")" \
    "$(cat /sys/class/power_supply/BAT*/capacity 2>/dev/null | head -1)" "$(cat /sys/class/power_supply/BAT*/status 2>/dev/null | head -1)" \
    "$(for d in /sys/class/power_supply/*; do case "$(cat "$d/type" 2>/dev/null)" in Mains|USB*) grep -qxE "[12]" "$d/online" 2>/dev/null && { echo connected; exit; } ;; esac; done; echo DISCONNECTED)" \
    >> '"$HB"' 2>/dev/null; done ) &
HBPID=$!
set -o pipefail
rc=0
while read -r logname script; do
  echo "=== $(date "+%F %T")  $script   -> notes/review_results/$logname.log"
  .venv/bin/python -u "$script" </dev/null 2>&1 | tee "notes/review_results/$logname.log"
  s=$?
  if [ "$s" != 0 ]; then rc=$s; echo "=== step $script exit $s"; break; fi
done <<EOF
'"$STEPS"'
EOF
echo "=== unit exit $rc"
kill $HBPID 2>/dev/null
exit $rc'
case "$INNER" in *'${'*|*'$$'*) echo "STOP: the unit's command holds a dollar-brace or a double dollar"; exit 1 ;; esac
git status --porcelain --untracked-files=all > "$PRE"
trap 'if [ "$(systemctl show "$UNIT" -p LoadState --value 2>/dev/null)" != loaded ]; then rm -f "$PRE"; echo; echo "NOT STARTED: interrupted. Run this script again."; else echo; echo "Interrupted after the unit was created: send this output to the planning session."; fi; exit 1' INT TERM HUP
echo
echo "All checks passed. sudo asks for your password; then the automatic updates are paused and the unit $UNIT starts."
sudo -v || { rm -f "$PRE"; echo "NOT STARTED: sudo did not accept the password. Run this script again."; exit 1; }
sudo systemctl stop apt-daily.timer apt-daily-upgrade.timer 2>/dev/null
ta=$(systemctl is-active apt-daily.timer apt-daily-upgrade.timer 2>/dev/null | tr '\n' ' ')
echo "automatic updates (apt-daily.timer, apt-daily-upgrade.timer): $ta"
[ "$ta" = "inactive inactive " ] || { rm -f "$PRE"; echo "NOT STARTED: the automatic updates could not be paused; send this output to the planning session."; exit 1; }
sudo systemd-run --unit="$UNIT" --same-dir \
  --property=OOMScoreAdjust=-500 --property=TimeoutStartSec=infinity --property=RemainAfterExit=yes \
  systemd-inhibit --what=sleep:idle:handle-lid-switch:shutdown --mode=block --who="$UNIT" \
    --why="the run of B27, B28, B29 and B16c (log $LOG)" \
  runuser -u vilalius -- bash -c "$INNER" || {
    [ "$(systemctl show "$UNIT" -p LoadState --value 2>/dev/null)" = loaded ] || rm -f "$PRE"
    echo "NOT STARTED: sudo or systemd-run failed. If you mistyped the password, run this script again; otherwise send this output to the planning session."
    exit 1; }
trap - INT TERM HUP
sleep 20
echo
systemctl show "$UNIT" -p ActiveState -p SubState -p ExecMainStartTimestamp
systemd-inhibit --list --no-pager | grep -E "^ *WHO|$UNIT"
echo "--- the log so far:"
head -4 "$LOG"
echo
if [ "$(systemctl show "$UNIT" -p SubState --value)" = running ] && grep -q '^=== ' "$LOG"; then
  echo "STARTED: the unit $UNIT is running. Leave the lid open and the charger connected until the log ends with '=== unit exit'."
  echo "Follow it with:   tail -f $LOG"
else
  echo "The unit is not running as expected. Do not run this script again: send this whole output to the planning session."
fi
