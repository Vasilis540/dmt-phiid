import re,sys,glob,os
num=re.compile(r'[-+−]?\d+(?:[.,]\d+)*(?:\s?%)?')
def toks(s):
    s=s.replace('−','-').replace(' ',' ')
    out=[]
    for m in re.finditer(r'[-+]?\d[\d,]*(?:\.\d+)?',s):
        t=m.group(0).replace(',','')
        try: out.append(float(t))
        except: pass
    return out
def load_sources(paths):
    lines=[]
    for p in paths:
        for f in glob.glob(p):
            try:
                for i,l in enumerate(open(f,encoding='utf-8',errors='replace'),1):
                    lines.append((f,i,l,toks(l)))
            except IsADirectoryError: pass
    return lines
def is_subseq(a,b):
    it=iter(b)
    return all(any(abs(x-y)<1e-12 for y in it) for x in a)
def check(sfile, lo, hi, srcs, minnums=3):
    src=load_sources(srcs)
    L=open(sfile,encoding='utf-8').read().split('\n')
    bad=[]
    for n in range(lo,hi+1):
        l=L[n-1]
        if not l.startswith('|') or set(l.replace('|','').strip())<=set('-: '): continue
        t=toks(l)
        if len(t)<minnums: continue
        ok=[ (f,i) for f,i,sl,st in src if is_subseq(t,st)]
        if not ok:
            # try partial: find best line with most tokens in order
            best=max(src,key=lambda x: sum(1 for v in t if any(abs(v-y)<1e-12 for y in x[3])))
            miss=[v for v in t if not any(abs(v-y)<1e-12 for y in best[3])]
            bad.append((n,l[:160],os.path.basename(best[0]),best[1],miss[:10]))
    return bad
if __name__=='__main__':
    sfile=sys.argv[1]; lo=int(sys.argv[2]); hi=int(sys.argv[3]); srcs=sys.argv[4:]
    for b in check(sfile,lo,hi,srcs): print(b)
