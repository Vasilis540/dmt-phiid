"""Independent referee checks on committed result files (no subject data)."""
import pickle, itertools, numpy as np, sys
from scipy import stats
R = (sys.argv[1] if len(sys.argv) > 1 else '.').rstrip('/') + '/'   # repository root (path made repository-relative)

SIGNS = np.array(list(itertools.product((-1, 1), repeat=14)), dtype=float)  # 16384 x 14

def signflip_p(x, mu=0.0):
    x = np.asarray(x, float) - mu
    obs = abs(x.sum())
    s = np.abs(SIGNS @ x)
    return np.mean(s >= obs * (1 - 1e-12))

def inverted_interval(x, alpha=0.05):
    x = np.asarray(x, float)
    m = x.mean()
    # p(mu) as function; bisection on each side
    def p(mu):
        return signflip_p(x, mu)
    def bis(lo, hi):  # p(lo) > alpha (inside), p(hi) <= alpha (outside)
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            if p(mid) > alpha:
                lo = mid
            else:
                hi = mid
        return 0.5 * (lo + hi)
    span = x.max() - x.min()
    lo_out = x.min() - 1e-9
    hi_out = x.max() + 1e-9
    return bis(m, lo_out), bis(m, hi_out)

def tint(x):
    x = np.asarray(x, float); n = len(x)
    se = x.std(ddof=1) / np.sqrt(n)
    t = stats.t.ppf(0.975, n - 1)
    return x.mean() - t * se, x.mean() + t * se

def load(nm):
    return pickle.load(open(R + f'notes/review_results/inference_rows_{nm}.pkl', 'rb'))

def row(rows, label, sset='primary'):
    for r in rows:
        if r['label'] == label and r['set'] == sset:
            return r
    raise KeyError(label, sset)

if __name__ == '__main__':
    raw = load('raw'); diag = load('diag'); ccs = load('ccs_pub'); lag = load('lag'); pw = load('prewhiten')
    for rows, lab, st in [
        (raw, 'sts ts_gsr W60', 'primary'),
        (raw, 'sts ts_demean W60', 'primary'),
        (raw, 'sts ts_gsr W30', 'primary'),
        (raw, 'sts ts_gsr global-bins', 'primary'),
        (raw, 'autocorr ts_gsr W60', 'primary'),
        (raw, 'autocorr ts_demean W60', 'primary'),
        (raw, 'PhiR ts_gsr W60', 'primary'),
        (diag, 'diag predicted sts ts_gsr W60', 'primary'),
        (diag, 'diag residual sts ts_gsr W60', 'primary'),
        (diag, 'diag residual sts ts_gsr W60', 'early'),
        (diag, 'diag residual sts ts_gsr W60', 'late'),
        (diag, 'diag residual sts ts_demean W60', 'primary'),
        (ccs, 'CCSpub sts ts_gsr W60', 'primary'),
        (ccs, 'CCSpub sts ts_gsr global-bins', 'primary'),
        (pw, 'prewhiten arp MMI sts ts_gsr W60', 'primary'),
        (pw, 'prewhiten ar1 MMI sts ts_gsr W60', 'primary'),
        (pw, 'prewhiten arp diag predicted sts ts_gsr W60', 'primary'),
    ]:
        r = row(rows, lab, st)
        x = np.array(r['did_subjects'], float)
        lo, hi = inverted_interval(x)
        print(f"{lab:45s} {st:8s} mean={x.mean():+.5f} p={signflip_p(x):.4f} (committed p={r['did_p']:.4f}) inv=[{lo:+.5f},{hi:+.5f}] "
              f"pct=[{r['did_lo']:+.5f},{r['did_hi']:+.5f}] neg={int((x<0).sum())} phase_p={r.get('phase_p')} pre_dmt={r['pre_dmt']} pre_pcb={r['pre_pcb']}")
