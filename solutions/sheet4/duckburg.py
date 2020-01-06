import sys
from math import floor, ceil
from itertools import accumulate
from operator import add

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())

if k >= n:
    print(25*n)
    exit(0)

x = sorted(int(line) for line in sys.stdin)
prefix_sums = [0] + list(accumulate(x, add))


def cc(i, j):
    m_ij = (j + i) / 2
    fm_ij = floor(m_ij)
    mu_ij = (x[floor(m_ij)] + x[ceil(m_ij)]) / 2
    return (2 * fm_ij - i - j + 1) * mu_ij - 2 * prefix_sums[fm_ij + 1] + prefix_sums[i] + prefix_sums[j + 1]


D = [cc(0, m) for m in range(n)]

for i in range(1, k):
    D = [0] + [min(D[j - 1] + cc(j, m) for j in range(1, m + 1)) for m in range(1, n)]

print(25 * n - int(D[-1]))
