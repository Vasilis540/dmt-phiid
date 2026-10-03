% octave_crosscheck.m
% Recomputes two contrasts of the paper from the released time series in GNU Octave, independently of the Python
% pipeline: the whole-brain lag-1 autocorrelation (r1) contrast and the primary contrast of whole-brain mean MMI-sts
% (Gaussian estimator, minimum-mutual-information redundancy, tau = 1, 14 separately fitted windows of 60 TRs,
% 115 regions, 6,555 pairs). Nothing of the Python code is called: the atoms are computed here from each window's
% lagged correlation matrices.
%
% Run:   octave --no-gui octave_crosscheck.m        (inside Octave: run('octave_crosscheck.m'))
% Writes, in the current folder: octave_crosscheck.out (the summary printed on screen) and
% octave_crosscheck_windows.csv (subject, run, window, r1, sts; run 1 = DMT, run 2 = placebo).
1;

datafile = getenv('DMT_TS_FILE');
if isempty(datafile)
  datafile = '/home/vilalius/dmt-phiid/external/DMT_NCT/data/DMT_clean_mni_continuous_fullPreprocsch116.mat';
end
variant = 'ts_gsr';
S = load(datafile);
ts = S.(variant);                       % 14 x 2 cell: {subject, 1} = DMT, {subject, 2} = placebo; regions x TRs

[nsub, ncond] = size(ts);
nreg = size(ts{1, 1}, 1);
T = size(ts{1, 1}, 2);
W = 60;
nwin = T / W;
regions = setdiff(1:nreg, 21);          % region 21 (20 counting from 0) is dropped for every subject and run
R = numel(regions);
[I, J] = find(triu(true(R), 1));        % every pair i < j
npairs = numel(I);

% The PhiID lattice: knowns = M * atoms. Rows (knowns): rtr, Rxy>a, Rxy>b, Rxy>ab, Rab<x, Rab<y, Rab<xy, Ix;a, Ix;b,
% Iy;a, Iy;b, Ixy;a, Ixy;b, Ix;ab, Iy;ab, Ixy;ab. Columns (atoms): rtr rtx rty rts xtr xtx xty xts ytr ytx yty yts
% str stx sty sts.
M = [1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
     1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
     1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0
     1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
     1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0
     1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0
     1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0
     1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0
     1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0
     1 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0
     1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0
     1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
     1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
     1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0
     1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1];
Minv = inv(M);
w_sts = Minv(16, :)';                   % sts = knowns * w_sts

el = @(A, i, j) A(sub2ind(size(A), i, j));
det3 = @(a11, a22, a33, a12, a13, a23) a11 .* (a22 .* a33 - a23 .^ 2) - a12 .* (a12 .* a33 - a23 .* a13) ...
       + a13 .* (a12 .* a23 - a22 .* a13);

r1 = nan(nsub, ncond, nwin);
sts = nan(nsub, ncond, nwin);
ndrop = zeros(nsub, ncond);
for s = 1:nsub
  for c = 1:ncond
    X = double(ts{s, c}(regions, :));
    ok = all(isfinite(X), 1);
    ndrop(s, c) = sum(~ok);
    for w = 1:nwin
      idx = (w - 1) * W + (1:W);
      idx = idx(ok(idx));
      Xw = X(:, idx);

      % whole-brain lag-1 autocorrelation of the window: each region standardised within the window (SD with N - 1),
      % the product of consecutive time points averaged over regions and over the pairs of consecutive TRs
      Z = (Xw - mean(Xw, 2)) ./ std(Xw, 0, 2);
      zz = mean(Z(:, 1:end-1) .* Z(:, 2:end), 1);
      r1(s, c, w) = mean(zz(diff(idx) == 1));

      % the correlation matrix of [x_t, y_t, x_t+1, y_t+1] of every pair, from the window's past and future segments
      P = Xw(:, 1:end-1);
      F = Xw(:, 2:end);
      P = (P - mean(P, 2)) ./ std(P, 0, 2);
      F = (F - mean(F, 2)) ./ std(F, 0, 2);
      n = size(P, 2);
      pp = (P * P') / (n - 1);
      ff = (F * F') / (n - 1);
      pf = (P * F') / (n - 1);          % pf(i, j) = <past of i, future of j>
      c11 = el(pp, I, I); c12 = el(pp, I, J); c22 = el(pp, J, J);
      c13 = el(pf, I, I); c14 = el(pf, I, J); c23 = el(pf, J, I); c24 = el(pf, J, J);
      c33 = el(ff, I, I); c34 = el(ff, I, J); c44 = el(ff, J, J);

      % determinants of the blocks (1 = x past, 2 = y past, 3 = x future, 4 = y future)
      d12 = c11 .* c22 - c12 .^ 2;  d13 = c11 .* c33 - c13 .^ 2;  d14 = c11 .* c44 - c14 .^ 2;
      d23 = c22 .* c33 - c23 .^ 2;  d24 = c22 .* c44 - c24 .^ 2;  d34 = c33 .* c44 - c34 .^ 2;
      d123 = det3(c11, c22, c33, c12, c13, c23);
      d124 = det3(c11, c22, c44, c12, c14, c24);
      d134 = det3(c11, c33, c44, c13, c14, c34);
      d234 = det3(c22, c33, c44, c23, c24, c34);
      u1 = (c22 .* c13 - c12 .* c23) ./ d12;  u2 = (c22 .* c14 - c12 .* c24) ./ d12;
      v1 = (c11 .* c23 - c12 .* c13) ./ d12;  v2 = (c11 .* c24 - c12 .* c14) ./ d12;
      s11 = c33 - (c13 .* u1 + c23 .* v1);
      s12 = c34 - (c13 .* u2 + c23 .* v2);
      s22 = c44 - (c14 .* u2 + c24 .* v2);
      d1234 = d12 .* (s11 .* s22 - s12 .^ 2);

      % the nine Gaussian mutual informations (nats)
      Ixa  = 0.5 * (log(c11) + log(c33) - log(d13));
      Ixb  = 0.5 * (log(c11) + log(c44) - log(d14));
      Iya  = 0.5 * (log(c22) + log(c33) - log(d23));
      Iyb  = 0.5 * (log(c22) + log(c44) - log(d24));
      Ixya = 0.5 * (log(d12) + log(c33) - log(d123));
      Ixyb = 0.5 * (log(d12) + log(c44) - log(d124));
      Ixab = 0.5 * (log(c11) + log(d34) - log(d134));
      Iyab = 0.5 * (log(c22) + log(d34) - log(d234));
      Ixyab = 0.5 * (log(d12) + log(d34) - log(d1234));

      % the minimum-mutual-information redundancies, and the sts atom by the lattice
      K = [min(min(Ixa, Ixb), min(Iya, Iyb)), min(Ixa, Iya), min(Ixb, Iyb), min(Ixab, Iyab), ...
           min(Ixa, Ixb), min(Iya, Iyb), min(Ixya, Ixyb), ...
           Ixa, Ixb, Iya, Iyb, Ixya, Ixyb, Ixab, Iyab, Ixyab];
      sts(s, c, w) = mean(K * w_sts);
    end
  end
end

pre = 1:4;                              % windows 1-4
post = 6:14;                            % windows 6-14 (window 5 holds the injection)
if exist('OCTAVE_VERSION', 'builtin')
  prog = ['GNU Octave ' version()];
else
  prog = ['MATLAB ' version()];
end
rep = sprintf('octave_crosscheck.m; %s; %s\n', prog, datafile);
rep = [rep sprintf('variant %s: %d subjects, %d regions, %d pairs, %d windows of %d TRs; non-finite TRs dropped: %d\n', ...
       variant, nsub, R, npairs, nwin, W, sum(ndrop(:)))];
[sd, cd] = find(ndrop > 0);
for k = 1:numel(sd)
  rep = [rep sprintf('  subject %d, run %d (1 = DMT, 2 = placebo): %d\n', sd(k), cd(k), ndrop(sd(k), cd(k)))];
end
names = {'whole-brain lag-1 autocorrelation r1', 'whole-brain mean MMI-sts (nats)'};
vals = {r1, sts};
for q = 1:2
  V = vals{q};
  a = mean(V(:, :, pre), 3);            % subject x run
  b = mean(V(:, :, post), 3);
  pregap = a(:, 1) - a(:, 2);
  postgap = b(:, 1) - b(:, 2);
  did = postgap - pregap;
  rep = [rep sprintf('%s\n', names{q})];
  rep = [rep sprintf('  pre-injection mean, DMT / placebo: %.5f / %.5f\n', mean(a(:, 1)), mean(a(:, 2)))];
  rep = [rep sprintf('  pre-injection gap %+.5f; post-injection gap %+.5f; DiD %+.5f (means over %d subjects)\n', ...
         mean(pregap), mean(postgap), mean(did), nsub)];
  rep = [rep sprintf('  DiD per subject:') sprintf(' %+.6f', did) sprintf('\n')];
end
fprintf('%s', rep);
fid = fopen('octave_crosscheck.out', 'w');
fprintf(fid, '%s', rep);
fclose(fid);
fid = fopen('octave_crosscheck_windows.csv', 'w');
fprintf(fid, 'subject,run,window,r1,sts\n');
for s = 1:nsub
  for c = 1:ncond
    for w = 1:nwin
      fprintf(fid, '%d,%d,%d,%.12g,%.12g\n', s, c, w, r1(s, c, w), sts(s, c, w));
    end
  end
end
fclose(fid);
