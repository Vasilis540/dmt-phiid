#!/usr/bin/env bash
# b26_start.sh — checks the conditions of B26's run, then starts it.
#
# Record: "The matrices that are not positive definite (B26): pre-run entry" (the run, and its rules (i) and (iv)).
# Uses, all as yourself (vilalius, not with sudo):
#   bash ~/Downloads/b26_start.sh --check                  every check; starts nothing
#   bash ~/Downloads/b26_start.sh                          every check, then the run
#   bash ~/Downloads/b26_start.sh --check --from <step>    only if the planning session asks for it: the checks of a
#   bash ~/Downloads/b26_start.sh --from <step>            resumed run, then the run of <step> and every later step
# Nothing starts unless every check passes; each failed check prints a STOP line. The script changes nothing in the
# repository. Once the checks pass, sudo asks for your password; the system's automatic package updates are paused
# until the next restart (so that nothing is upgraded while the run is going), and the run starts as the root transient
# unit "runb26" (a resumed run as "runb26from1", then "runb26from2" and so on, each with its own log files). The unit
# runs notes/partB26_positive_definite.py as vilalius inside a sleep, idle, lid-switch and shutdown inhibitor, with a
# heartbeat line every five minutes. The run takes about three hours; the script writes its counts before the first step
# and after every step, so that a run cut short (a power loss) can be resumed from the step it did not finish.
set -u
REPO=/home/vilalius/dmt-phiid
RUN=d5a65bdcb2cc9d073f71829c264894937dbe1dc4                                                  # the tip of bundle 32, which carries B26's pre-run entry
RUN_LOG=notes/review_results/partB/positive_definite_run.log
CSV=notes/review_results/partB/positive_definite.csv
DECONV_MAT=notes/review_results/deconv/DMT_clean_mni_continuous_fullPreprocsch116.mat
MODE=start
FROM=""
while [ $# -gt 0 ]; do
  case "$1" in
    --check) MODE=check ;;
    --from) FROM="${2:-}"; [ -n "$FROM" ] || { echo "STOP: --from needs the name of a step"; exit 1; }; shift ;;
    *) echo "STOP: unknown argument $1"; exit 1 ;;
  esac
  shift
done
case "$FROM" in *[!A-Za-z0-9_./-]*) echo "STOP: '$FROM' is not a step name"; exit 1 ;; esac
H=/home/vilalius
if [ -z "$FROM" ]; then
  UNIT=runb26; SFX=""
else                                                       # a resumed run: the first number no earlier resumed run used
  k=1
  while [ -e "$H/b26_run_unit_from$k.log" ] || [ -e "$H/b26_heartbeat_from$k.log" ] || [ -e "$H/b26_prestatus_from$k.txt" ] \
        || [ "$(systemctl show "runb26from$k" -p LoadState --value 2>/dev/null)" = loaded ]; do
    k=$((k + 1))
  done
  UNIT=runb26from$k; SFX=_from$k
fi
LOG=$H/b26_run_unit$SFX.log                                # the run's standard output and error (also tee'd into the repository)
HB=$H/b26_heartbeat$SFX.log                                # the heartbeat
PRE=$H/b26_prestatus$SFX.txt                               # git status before the run, for the evidence script
go=1
stop() { echo "STOP: $*"; go=0; }
charger() {  # "connected" if a mains or USB power supply is online (a wireless mouse's battery does not count)
  for d in /sys/class/power_supply/*; do
    case "$(cat "$d/type" 2>/dev/null)" in Mains|USB*) grep -qxE "[12]" "$d/online" 2>/dev/null && { echo connected; return; } ;; esac
  done
  echo "NOT connected"
}

cd "$REPO" 2>/dev/null || { echo "STOP: $REPO not found"; exit 1; }
echo "now: $(date -u '+%F %T UTC')  ($(date '+%F %T %Z'))   mode: $MODE${FROM:+, resuming from step $FROM}"
[ "$(id -un)" = vilalius ] || stop "run this script as vilalius, without sudo"

# ---------------------------------------------------------------- the commit
echo "branch: $(git rev-parse --abbrev-ref HEAD)   HEAD: $(git log --oneline -1 | cut -c1-100)"
[ "$(git rev-parse --abbrev-ref HEAD)" = master ] || stop "not on master"
[ "$(git rev-parse HEAD)" = "$RUN" ] || stop "HEAD is not ${RUN:0:7}: pull bundle 32 first (pull32.sh)"
[ "$(git rev-parse -q --verify origin/master)" = "$RUN" ] || stop "origin/master is not ${RUN:0:7}: push first (pull32.sh)"

# ---------------------------------------------------------------- the working tree
t=$(git status --porcelain --untracked-files=all)
if [ -z "$FROM" ]; then
  [ -z "$t" ] || stop "the working tree is not clean (the run requires it): $(echo "$t" | head -5 | tr '\n' ' ')"
else
  # a resumed run: only the outputs the interrupted run wrote may have changed, and its counts must be there
  o=$(echo "$t" | grep -vE '^.. "?(results/|notes/review_results/|manuscript/figures/|notes/review_computations_2026-09-14\.md)' || true)
  [ -z "$o" ] || stop "files outside the outputs have changed: $(echo "$o" | head -5 | tr '\n' ' ')"
  [ -s "$CSV" ] || stop "$CSV is not there: the run to resume has left no counts"
  head -1 "$CSV" 2>/dev/null | grep -q "git=${RUN:0:7};" || stop "$CSV is not that of the run at ${RUN:0:7}"
  echo "the counts so far: $(head -1 "$CSV" 2>/dev/null | cut -c1-240)"
  c=$(.venv/bin/python -I notes/partB26_positive_definite.py --check-from "$FROM" 2>&1 | tail -1)
  echo "B26's script on resuming from $FROM: ${c:0:300}"
  case "$c" in "B26 --check-from $FROM: ready;"*) ;; *) stop "B26's script does not accept --from $FROM (its message above; the step names: .venv/bin/python notes/partB26_positive_definite.py --steps)" ;; esac
fi
[ ! -e "$DECONV_MAT" ] || stop "the deconvolution sandbox is present ($DECONV_MAT); the run is made without it, as the final run was"

# ---------------------------------------------------------------- the data
U=$(git -C external/DMT_NCT rev-parse HEAD 2>/dev/null)
echo "data clone external/DMT_NCT: ${U:-not a git clone}"
case "$U" in 77af7aa*) ;; *) stop "external/DMT_NCT is not at upstream commit 77af7aa" ;; esac
t=$(git -C external/DMT_NCT status --porcelain --untracked-files=no 2>/dev/null)
[ -z "$t" ] || stop "external/DMT_NCT has modified or missing tracked files: $(echo "$t" | head -5 | tr '\n' ' ')"
for f in external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat external/DMT_NCT/data/FDlong.mat \
         external/DMT_NCT/data/intensity_ratings.mat external/DMT_NCT/fxns/SpinTests/rotated_maps/rotated_Schaefer_100.mat; do
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
t=$(.venv/bin/python -I notes/partB26_positive_definite.py --selftest 2>&1 | tail -1)
echo "B26 self-test: ${t:0:160}"
case "$t" in *"; 0 failed") ;; *) stop "B26's self-test did not pass" ;; esac

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
for u in $(systemctl list-units --all --plain --no-legend 'runb26*' 2>/dev/null | awk '{print $1}'); do
  case "$(systemctl show "$u" -p ActiveState --value 2>/dev/null)/$(systemctl show "$u" -p SubState --value 2>/dev/null)" in
    activating/*|deactivating/*|reloading/*|*/running) stop "the unit $u is running, starting or stopping" ;;
  esac
done
[ "$(systemctl show "$UNIT" -p LoadState --value 2>/dev/null)" != loaded ] || stop "a unit named $UNIT exists already"

if [ "$MODE" = check ]; then
  echo
  if [ "$go" = 1 ]; then echo "READY: every check passed. Start the run with: bash ~/Downloads/b26_start.sh${FROM:+ --from $FROM}"
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
# The unit's command: B26's script as vilalius, as its docstring gives it (its output tee'd into the repository's
# notes/review_results/partB/positive_definite_run.log, appended to by a resumed run), everything it prints also written
# to the unit's log, with a heartbeat line every five minutes in the heartbeat file, then the line "=== unit exit
# <status>". The whole command runs inside systemd-inhibit, which blocks sleep, idle, the lid switch and shutdown until it
# ends. It is put together from single-quoted pieces and the two file names (no dollar-brace and no double dollar in it:
# systemd would expand them).
if [ -z "$FROM" ]; then
  CMD='.venv/bin/python -u notes/partB26_positive_definite.py 2>&1 | tee notes/review_results/partB/positive_definite_run.log'
else
  CMD=".venv/bin/python -u notes/partB26_positive_definite.py --from '$FROM' 2>&1 | tee -a notes/review_results/partB/positive_definite_run.log"
fi
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
'"$CMD"'
rc=$?
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
    --why="B26's run (log $LOG)" \
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
else
  echo "The unit is not running as expected. Do not run this script again: send this whole output to the planning session."
fi
