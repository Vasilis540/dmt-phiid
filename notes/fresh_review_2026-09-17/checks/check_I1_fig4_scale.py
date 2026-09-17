"""
check_I1_fig4_scale.py -- does Figure 4(b) really have "the same nats per unit height"
as Figure 4(a), as its panel title and caption claim?  Measured from the rendered PNG:
the two axes frames are found from the LEFT SPINE's vertical dark runs (the spine exists
only where an axes box is).
"""
import numpy as np
from PIL import Image
p = '/mnt/user-data/uploads/dmt-phiid/manuscript/figures/fig4_v2_residual_diagnostic.png'
im = np.asarray(Image.open(p).convert('L'), float)
H, W = im.shape
print(f"image {W} x {H}")
dark = im < 150
colsum = dark[:, :W//3].sum(0)
xl = int(np.argmax(colsum)); print(f"left spine column x = {xl} ({colsum[xl]} dark px)")
col = dark[:, xl]
runs, s = [], None
for y in range(H):
    if col[y] and s is None: s = y
    elif not col[y] and s is not None:
        if y - s > 50: runs.append((s, y-1))
        s = None
if s is not None and H - s > 50: runs.append((s, H-1))
print("vertical spine runs (y0, y1, height):", [(a, b, b-a) for a, b in runs])
if len(runs) >= 2:
    ha = runs[0][1] - runs[0][0]; hb = runs[1][1] - runs[1][0]
    ra, rb = 0.30, 0.20              # panel a spans 1.00-1.30 ; panel b spans -0.15-0.05
    print(f"\npanel a box height = {ha} px for {ra} nats -> {ha/ra:.1f} px/nat")
    print(f"panel b box height = {hb} px for {rb} nats -> {hb/rb:.1f} px/nat")
    print(f"scale ratio (b/a) = {(hb/rb)/(ha/ra):.4f}")
    print(f"box height ratio a:b = {ha/hb:.4f}   (equal nats-per-height needs 1.5000)")
    if abs((hb/rb)/(ha/ra) - 1) < 0.02:
        print("\nVERDICT: the panels ARE on the same nats-per-unit-height scale; the claim holds.")
    else:
        print(f"\nVERDICT: panel (b) is stretched by a factor {(hb/rb)/(ha/ra):.2f} relative to (a).")
        print("The panel title 'same nats per unit height' and the caption's arithmetic")
        print("(which asserts a panel 67 % of (a)'s height) do not describe the rendered figure.")
