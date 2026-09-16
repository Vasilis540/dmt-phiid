# Run as:  cd ~/dmt-phiid && git diff -I 'git' --name-only -- '*.md' '*.csv' '*.txt' > /tmp/changed.txt && .venv/bin/python 2_compare_all.py
# (--name-only lists every modified file regardless of -I, so the comparison covers all regenerated tables.)
import subprocess, io, difflib, numpy as np, pandas as pd
for f in open('/tmp/changed.txt').read().split():
    old = subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True, text=True).stdout
    new = open(f).read()
    if f.endswith('.csv'):
        try:
            o = pd.read_csv(io.StringIO(old), comment='#'); n = pd.read_csv(io.StringIO(new), comment='#')
        except Exception as e:
            print(f, 'parse error', e); continue
        print(f"== {f}: old {o.shape} new {n.shape}")
        if o.shape != n.shape or list(o.columns) != list(n.columns):
            extra = n.merge(o, how='left', indicator=True); extra = extra[extra['_merge'] == 'left_only']
            print("   rows in new not in old:", len(extra)); print(extra.head(3).to_string()[:700]); continue
        num = o.select_dtypes(include=[np.number]).columns
        d = (o[num] - n[num]).abs()
        print(f"   max |diff| over numeric cells {np.nanmax(d.values):.3g}; cells differing by > 1e-9: {int((d > 1e-9).sum().sum())}")
        for c in o.columns.difference(num):
            if not (o[c].astype(str) == n[c].astype(str)).all(): print("   non-numeric column differs:", c)
    else:
        diff = [l for l in difflib.unified_diff(old.splitlines(), new.splitlines(), lineterm='', n=0) if l[:1] in '+-' and l[:3] not in ('+++', '---')]
        print(f"== {f}:"); [print("   ", l[:220]) for l in diff[:8]]
