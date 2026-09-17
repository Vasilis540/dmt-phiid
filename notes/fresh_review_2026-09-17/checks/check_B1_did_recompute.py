"""
check_B1_did_recompute.py -- independent recomputation of the primary DMT contrast,
its exact sign-flip p, and the per-subject sts / r1 collinearity, from the committed
per-subject values (did_subjects in notes/review_results/inference_rows_*.pkl) and from
the saved windowed atom arrays (results/atoms_win60_*.npy).

Nothing here re-runs the pipeline; external/ is absent from this copy.
"""
import pickle, itertools, numpy as np
from pathlib import Path
from scipy import stats

R = Path('/mnt/user-data/uploads/dmt-phiid')
out = []; P = out.append

ATOMS = "rtr,rtx,rty,rts,xtr,xtx,xty,xts,ytr,ytx,yty,yts,str,stx,sty,sts".split(",")
IX = {n: i for i, n in enumerate(ATOMS)}
SIGNS = np.array(list(itertools.product((-1, 1), repeat=14)))

def signflip_p(v):
    v = np.asarray(v, float); obs = abs(v.mean())
    return float(np.mean(np.abs((SIGNS * v).mean(1)) >= obs - 1e-12))

def boot_ci(v, seed=20261120, n=10000):
    rng = np.random.default_rng(seed); v = np.asarray(v, float)
    return np.percentile(v[rng.integers(0, v.size, (n, v.size))].mean(1), [2.5, 97.5])

rows = {}
for f in ['raw', 'diag', 'ccs_pub', 'lag', 'ccs']:
    for r in pickle.load(open(R / f'notes/review_results/inference_rows_{f}.pkl', 'rb')):
        rows[(f, r['label'], r['set'])] = r

P("="*78); P("1. PRIMARY DiD FROM THE SAVED WINDOWED ATOMS (independent of the pkl rows)")
P("="*78)
# cond 0 = DMT, 1 = PCB ; PRE = windows 0-3 (1-4) ; primary = 5-13 (6-14)
PRE, POST = np.arange(0, 4), np.arange(5, 14)
for var in ['ts_gsr', 'ts_demean']:
    A = np.load(R / f'results/atoms_win60_115regions-all_{var}_window.npy')   # (14,2,14,16)
    sts = A[..., IX['sts']]
    ch = sts[:, :, POST].mean(2) - sts[:, :, PRE].mean(2)
    did = ch[:, 0] - ch[:, 1]
    lo, hi = boot_ci(did)
    P(f"  {var}: pre DMT {sts[:,0,PRE].mean():.4f}  pre PCB {sts[:,1,PRE].mean():.4f}")
    P(f"     DMT post-pre {ch[:,0].mean():+.4f}   PCB post-pre {ch[:,1].mean():+.4f}")
    P(f"     DiD mean {did.mean():+.6f}  [{lo:+.4f}, {hi:+.4f}]  sign-flip p = {signflip_p(did):.4f}"
      f"  negative in {int((did<0).sum())}/14")
    P(f"     share of pre-injection DMT mean: {100*did.mean()/sts[:,0,PRE].mean():+.1f} %")
    # TDMI and the proportionality share
    tdmi = A.sum(-1)
    cht = tdmi[:, :, POST].mean(2) - tdmi[:, :, PRE].mean(2); didt = cht[:, 0] - cht[:, 1]
    P(f"     TDMI DiD {didt.mean():+.4f}; sts share of TDMI DiD {did.mean()/didt.mean():.3f}; "
      f"baseline share {sts[:,0,PRE].mean()/tdmi[:,0,PRE].mean():.3f}")
    # all 16 atom levels and DiDs (Table 1 check, ts_gsr)
    if var == 'ts_gsr':
        P("     Table 1 check (level = DMT pre-injection windows 1-4; DiD; n_neg):")
        for a in ATOMS:
            x = A[..., IX[a]]
            c = x[:, :, POST].mean(2) - x[:, :, PRE].mean(2); dd = c[:, 0] - c[:, 1]
            P(f"       {a:4s} level {x[:,0,PRE].mean():+.4f}  DiD {dd.mean():+.4f} ({int((dd<0).sum())})")
        P(f"       TDMI level {tdmi[:,0,PRE].mean():+.4f}  DiD {didt.mean():+.4f}")
P("")

P("="*78); P("2. THE PER-SUBJECT COLLINEARITY r(sts DiD, r1 DiD) = 0.953")
P("="*78)
for var in ['ts_gsr', 'ts_demean']:
    s = np.asarray(rows[('raw', f'sts {var} W60', 'primary')]['did_subjects'], float)
    a = np.asarray(rows[('raw', f'autocorr {var} W60', 'primary')]['did_subjects'], float)
    pr = stats.pearsonr(s, a); sp = stats.spearmanr(s, a)
    P(f"  {var} W60: Pearson r = {pr.statistic:+.4f} (p = {pr.pvalue:.2e}); "
      f"Spearman = {sp.statistic:+.4f}")
    P(f"     sts DiD mean {s.mean():+.6f}  sign-flip p {signflip_p(s):.4f}  neg {int((s<0).sum())}/14")
    P(f"     r1  DiD mean {a.mean():+.6f}  sign-flip p {signflip_p(a):.4f}  neg {int((a<0).sum())}/14")
    P(f"     r^2 = {pr.statistic**2:.4f}; unshared variance = {100*(1-pr.statistic**2):.1f} %")
    # cross-check the saved sts DiD against the one from the atoms array
    A = np.load(R / f'results/atoms_win60_115regions-all_{var}_window.npy')[..., IX['sts']]
    ch = A[:, :, POST].mean(2) - A[:, :, PRE].mean(2)
    P(f"     max |pkl per-subject sts DiD - atoms-array DiD| = "
      f"{np.abs(s - (ch[:,0]-ch[:,1])).max():.3e}")
    # leave-two-out
    rr = [stats.pearsonr(np.delete(s, [i, j]), np.delete(a, [i, j])).statistic
          for i, j in itertools.combinations(range(14), 2)]
    rr = np.array(rr)
    k = int(np.argmin(rr)); pairs = list(itertools.combinations(range(14), 2))
    P(f"     leave-two-out ({len(rr)} refits): range {rr.min():+.3f} to {rr.max():+.3f}, "
      f"median {np.median(rr):+.3f}; min without subjects "
      f"{pairs[k][0]+1} and {pairs[k][1]+1}")
P("")

P("="*78); P("3. CAN r = 0.953 SEPARATE THE PAPER'S READING FROM SHARED ESTIMATION NOISE?")
P("="*78)
s = np.asarray(rows[('raw', 'sts ts_gsr W60', 'primary')]['did_subjects'], float)
a = np.asarray(rows[('raw', 'autocorr ts_gsr W60', 'primary')]['did_subjects'], float)
# split-half reliabilities quoted by the paper for these two DiDs: 0.69-0.72 and 0.71-0.74
P("  The paper quotes split-half reliabilities 0.71-0.74 (r1 DiD) and 0.69-0.72 (sts DiD).")
for rel_s, rel_a in [(0.69, 0.71), (0.72, 0.74), (0.705, 0.725)]:
    ceil = np.sqrt(rel_s * rel_a)
    P(f"    rel_sts={rel_s}, rel_r1={rel_a}: attenuation ceiling sqrt(rel*rel) = {ceil:.3f}; "
      f"observed r = 0.953 -> disattenuated {0.953/ceil:.3f}")
P("  => the observed collinearity EXCEEDS the ceiling two independent-noise measurements of")
P("     perfectly correlated reliable components could reach, so a purely-reliable-signal")
P("     account does not fit either: part of the 0.953 must be noise shared within windows.")
P("     (The same argument the paper applies to the residual/CCS pair, Results 4.)")
P("  Regression slope of the sts DiD on the r1 DiD, and the map slope for comparison:")
sl = np.polyfit(a, s, 1)
P(f"    OLS slope = {sl[0]:.3f} nats per unit r1 (intercept {sl[1]:+.5f});"
  f" family d sts/d r1 at (0.848, 0.24) = 5.99")
P(f"    predicted group DiD from slope*mean r1 DiD = {sl[0]*a.mean():+.5f}; observed {s.mean():+.5f}")
P("")

P("="*78); P("4. RESIDUAL DIAGNOSTIC: DiD, SIGN-FLIP p, AND THE CCS-sts RELATION")
P("="*78)
for lab in ['diag residual sts ts_gsr W60', 'diag residual sts ts_demean W60',
            'diag predicted sts ts_gsr W60', 'diag observed sts ts_gsr W60']:
    for st in ['primary', 'early', 'late']:
        k = ('diag', lab, st)
        if k not in rows: continue
        r = rows[k]; v = np.asarray(r['did_subjects'], float)
        lo, hi = boot_ci(v)
        P(f"  {lab:32s} {st:8s} DiD {v.mean():+.5f} [{lo:+.5f}, {hi:+.5f}] "
          f"p = {signflip_p(v):.4f} neg {int((v<0).sum())}/14  (file: {r['did']:+.5f}, "
          f"[{r['did_lo']:+.5f},{r['did_hi']:+.5f}], p={r['did_p']:.4f})")
res = np.asarray(rows[('diag', 'diag residual sts ts_gsr W60', 'primary')]['did_subjects'], float)
ccs = np.asarray(rows[('ccs_pub', 'CCSpub sts ts_gsr W60', 'primary')]['did_subjects'], float) \
      if ('ccs_pub', 'CCSpub sts ts_gsr W60', 'primary') in rows else None
if ccs is None:
    cands = [k for k in rows if k[0] == 'ccs_pub' and 'W60' in k[1] and k[2] == 'primary']
    P(f"  ccs_pub labels available: {sorted(set(k[1] for k in cands))}")
else:
    pr = stats.pearsonr(res, ccs)
    P(f"  r(residual DiD, CCS-sts DiD) ts_gsr W60 = {pr.statistic:+.4f} (p = {pr.pvalue:.4f})")
    # partial out the autocorrelation DiD
    def partial(x, y, z):
        rx = x - np.polyval(np.polyfit(z, x, 1), z); ry = y - np.polyval(np.polyfit(z, y, 1), z)
        return stats.pearsonr(rx, ry).statistic
    P(f"  partial r controlling the r1 DiD = {partial(res, ccs, a):+.4f}")
    P(f"  r(CCS-sts DiD, r1 DiD) = {stats.pearsonr(ccs, a).statistic:+.4f} "
      f"(p = {stats.pearsonr(ccs, a).pvalue:.4f})")
    P(f"  r(residual DiD, r1 DiD) = {stats.pearsonr(res, a).statistic:+.4f}")
    P(f"  CCS-sts DiD mean {ccs.mean():+.5f}, sign-flip p {signflip_p(ccs):.4f}, "
      f"positive in {int((ccs>0).sum())}/14")
P("")

P("="*78); P("5. CIRCULARITY OF THE RESIDUAL: observed = predicted + residual, same windows")
P("="*78)
z = np.load(R / 'notes/review_results/partB/diag_series_ts_gsr_W60.npz')
obs, pred, res_w = z['obs'], z['pred'], z['res']
P(f"  max |obs - (pred + res)| over the 392 cells = {np.abs(obs-(pred+res_w)).max():.3e}")
P(f"  levels: obs {obs.mean():.4f}  pred {pred.mean():.4f}  res {res_w.mean():.4f} "
  f"({100*res_w.mean()/obs.mean():+.2f} % of obs)")
P(f"  pred_sym level {z['pred_sym'].mean():.4f} -> over-prediction "
  f"{100*(z['pred_sym'].mean()-obs.mean())/obs.mean():+.1f} %")
P(f"  residual SD across the 392 cells {res_w.std():.4f} vs observed sts SD {obs.std():.4f} "
  f"(ratio {res_w.std()/obs.std():.3f})")
cho = obs[:, :, POST].mean(2)-obs[:, :, PRE].mean(2); dido = cho[:, 0]-cho[:, 1]
chp = pred[:, :, POST].mean(2)-pred[:, :, PRE].mean(2); didp = chp[:, 0]-chp[:, 1]
chr_ = res_w[:, :, POST].mean(2)-res_w[:, :, PRE].mean(2); didr = chr_[:, 0]-chr_[:, 1]
P(f"  observed DiD {dido.mean():+.5f}  predicted DiD {didp.mean():+.5f}  "
  f"residual DiD {didr.mean():+.5f}   (identity: {dido.mean()-didp.mean()-didr.mean():+.2e})")
P(f"  over-prediction = predicted/observed = {didp.mean()/dido.mean():.4f} "
  f"-> {100*didp.mean()/dido.mean():.0f} % of the magnitude")
P(f"  r(predicted DiD, observed DiD) per subject = "
  f"{stats.pearsonr(didp, dido).statistic:+.4f}")
P("  NOTE: the residual DiD is an exact algebraic complement of the predicted DiD within the")
P("  observed DiD, so its inference is a test of the SAME 14 numbers re-split, not of new data.")
P(f"  DMT-run-only change {chr_[:,0].mean():+.5f} (p {signflip_p(chr_[:,0]):.3f}); "
  f"placebo {chr_[:,1].mean():+.5f} (p {signflip_p(chr_[:,1]):.3f})")
P(f"  placebo share of the residual DiD = "
  f"{abs(chr_[:,1].mean())/(abs(chr_[:,0].mean())+abs(chr_[:,1].mean())):.3f}")
print("\n".join(out))
