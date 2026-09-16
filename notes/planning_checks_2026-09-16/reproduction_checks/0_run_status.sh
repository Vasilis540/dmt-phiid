cd ~/dmt-phiid && { ps -p 4738 -o pid=,etime=,args= || echo "4738 not running"; }; ls -l results/run_all_tail.log; grep '^===' results/run_all_tail.log | tail -n 1; tail -n 3 results/run_all_tail.log
