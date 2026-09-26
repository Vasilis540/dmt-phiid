import re, pathlib
repo = pathlib.Path('repo')
txt = pathlib.Path('findings.md').read_text()
blocks = re.split(r'\n(?=### )', txt)
for b in blocks:
    m = re.match(r'### (\S+)', b)
    if not m: continue
    fid = m.group(1)
    loc = re.search(r'\*\*Location\*\*:(.*)', b)
    q = re.search(r'\*\*Quote\*\*[^:]*:(.*)', b)
    if not loc or not q: 
        print(fid, 'NO LOC/QUOTE'); continue
    files = re.findall(r'(manuscript/[\w/._-]+\.md)', loc.group(1))
    files = list(dict.fromkeys(files))
    quotes = re.findall(r'"((?:[^"\\]|\\.)*)"', q.group(1))
    for qs in quotes:
        qs2 = qs.replace('\\"', '"')
        counts = []
        for f in files:
            p = repo / f
            if p.exists():
                counts.append((f, p.read_text().count(qs2)))
        print(fid, repr(qs2[:70]), counts)
