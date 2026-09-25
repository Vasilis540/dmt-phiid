"""Independent Gaussian MMI-PhiID for a 4x4 correlation matrix of (x_t, y_t, x_{t+1}, y_{t+1})."""
import numpy as np
from itertools import product

NODES = ['r', 'x', 'y', 's']  # {1}{2}, {1}, {2}, {12}
LEQ = {  # a <= b in the 2-source redundancy lattice
    ('r', 'r'): True, ('r', 'x'): True, ('r', 'y'): True, ('r', 's'): True,
    ('x', 'x'): True, ('x', 's'): True, ('y', 'y'): True, ('y', 's'): True, ('s', 's'): True,
}
def leq(a, b):
    return LEQ.get((a, b), False)

def mi(C, A, B):
    A = list(A); B = list(B)
    dA = np.linalg.det(C[np.ix_(A, A)]); dB = np.linalg.det(C[np.ix_(B, B)])
    AB = A + B
    dAB = np.linalg.det(C[np.ix_(AB, AB)])
    return 0.5 * np.log(dA * dB / dAB)

SRC = {'x': [0], 'y': [1], 's': [0, 1]}
TGT = {'x': [2], 'y': [3], 's': [2, 3]}

def red(C, a, b):
    """MMI redundancy at node a->b."""
    if a != 'r' and b != 'r':
        return mi(C, SRC[a], TGT[b])
    if a == 'r' and b != 'r':
        return min(mi(C, SRC['x'], TGT[b]), mi(C, SRC['y'], TGT[b]))
    if a != 'r' and b == 'r':
        return min(mi(C, SRC[a], TGT['x']), mi(C, SRC[a], TGT['y']))
    return min(mi(C, SRC[i], TGT[j]) for i in 'xy' for j in 'xy')

def atoms(C):
    keys = [(a, b) for a in NODES for b in NODES]
    Rv = np.array([red(C, a, b) for a, b in keys])
    M = np.zeros((16, 16))
    for i, (a, b) in enumerate(keys):
        for j, (a2, b2) in enumerate(keys):
            if leq(a2, a) and leq(b2, b):
                M[i, j] = 1
    at = np.linalg.solve(M, Rv)
    name = lambda a, b: a + 't' + b
    return {name(a, b): at[i] for i, (a, b) in enumerate(keys)}

def ar1_corr(ax, ay, q):
    return np.array([[1, q, ax, ay * q], [q, 1, ax * q, ay], [ax, ax * q, 1, q], [ay * q, ay, q, 1]], float)

if __name__ == '__main__':
    C = ar1_corr(0.85, 0.85, 0.25)
    A = atoms(C)
    for k, v in A.items():
        print(k, round(v, 6))
    print('TDMI', sum(A.values()))
