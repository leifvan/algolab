import sys
from itertools import combinations
from time import time

stime = time()

lines = list(sys.stdin)
r = int(lines[0])

print("makin fields", time()-stime)
tree_rows = [[j for j,c in enumerate(line) if c == '1'] for i, line in enumerate(lines[1:])]
tree_cols = [[i for i in range(r) if j in tree_rows[i]] for j in range(r)]

print("trees", time()-stime)
trees = set().union(*(set((i,j) for j, c in enumerate(line) if c == '1') for i, line in enumerate(lines[1:])))

count = 0

print("counto bounto", time()-stime)
for i1, row in enumerate(tree_rows):
    for j1, j2 in combinations(row, 2):
        for i2 in tree_cols[j1]:
            if i2 > i1:
                if (i2, j2) in trees:
                    count += 1

print(count)

