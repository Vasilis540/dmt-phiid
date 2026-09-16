# Run as:  cd ~/dmt-phiid && .venv/bin/python 3_three_checks.py
import subprocess, io, re, pandas as pd
def old(f): return subprocess.run(['git', 'show', 'HEAD:' + f], capture_output=True, text=True).stdout
f = 'notes/review_results/inference_rows_raw.csv'
o = pd.read_csv(io.StringIO(old(f))); n = pd.read_csv(f)
m = o['survives'].astype(str) != n['survives'].astype(str)
print("1. survives, old vs new, distinct pairs:", pd.DataFrame({'old': o.loc[m, 'survives'].astype(str), 'new': n.loc[m, 'survives'].astype(str)}).drop_duplicates().values.tolist())
a = pd.read_csv('results/bias_check_nonstat.csv', comment='#'); a = a[a.condition == 'nonstat_step_ar'].reset_index(drop=True)
b = pd.read_csv('results/nonstat_ar_step/bias_check_nonstat.csv', comment='#').reset_index(drop=True)
num = a.select_dtypes('number').columns
print("2. extra rows", a.shape, "vs nonstat_ar_step", b.shape, "max |diff|:", (a[num] - b[num]).abs().values.max() if a.shape == b.shape else "shapes differ")
print("   new header:", open('results/bias_check_nonstat.csv').readline().strip()[:150]); print("   old header:", old('results/bias_check_nonstat.csv').splitlines()[0][:150])
print("3. letter-digit-letter tokens in subject_alignment_check.txt:", sorted(set(re.findall(r'\b[A-Z][0-9][A-Z]\b', open('results/subject_alignment_check.txt').read())))[:10])
