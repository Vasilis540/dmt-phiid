cd ~/dmt-phiid && git diff -I 'git' --stat -- '*.md' '*.csv' '*.txt' && echo "--- binaries:" && git diff --stat -- '*.npy' '*.npz' '*.pkl' | tail -n 1
