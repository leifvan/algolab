import sys
from math import floor, ceil

k = int(sys.stdin.readline())
n = int(sys.stdin.readline())
x = sorted(int(line) for line in sys.stdin)


def cc(i, j):
    m_ij = (j + i) / 2
    mu_ij = (x[floor(m_ij)] + x[ceil(m_ij)]) / 2
    return sum(abs(x[l] - mu_ij) for l in range(i, j + 1))


lastD = [cc(0,m) for m in range(n)]
curD = [0] * n

for i in range(1, k):
    for m in range(1, n):
        curD[m] = min(lastD[j - 1] + cc(j, m) for j in range(m + 1))
    lastD = list(curD)

print(int(25 * n - lastD[-1]))
