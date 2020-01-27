import sys
from itertools import combinations
from operator import itemgetter
from time import time
from collections import defaultdict, OrderedDict

start_time = time()

lines = list(sys.stdin)
n = int(lines[0])
k = int(lines[1])
m = int(lines[2])

edges = [tuple(int(v) for v in line.split()) for line in lines[3:]]

MAX_VAL = 100000

dist_mat = [[MAX_VAL]*n for _ in range(n)]

for i in range(n):
    dist_mat[i][i] = 0

for i, j, weight in edges:
    dist_mat[i][j] = dist_mat[j][i] = weight

# start_time = time()

new_dist_mat = [None] * n

edges_i = defaultdict(list)
for i, j, _ in edges:
    edges_i[i].append(j)
    edges_i[j].append(i)

# dijkstra
for s in range(n):
    dist = [MAX_VAL]*n
    dist[s] = 0
    queue = sorted(range(n), key=lambda v: dist[v])

    while len(queue) > 0:
        u = queue.pop()
        for v in edges_i[u]:
            if dist[u] + dist_mat[u][v] < dist[v]:
                dist[v] = dist[u] + dist_mat[u][v]
                queue.sort(key=lambda v: dist[v])

    new_dist_mat[s] = dist
dist_mat = new_dist_mat

# print("dijkstra took", time() -start_time)
# start_time = time()

# init: all points are their own cluster
icd = {(i, j): dist_mat[i][j] for i, j in combinations(range(n), 2)}
icd_i = defaultdict(set)

for i,j in icd:
    icd_i[i].add((i,j))
    icd_i[j].add((i,j))


for _ in range(n-k):
    # find min pair
    i, j = min(icd.items(), key=itemgetter(1))[0]

    # join two closest clusters together
    tups = list(icd_i[j])
    for ix, jx in tups:
        icd_i[ix].remove((ix, jx))
        icd_i[jx].remove((ix, jx))

    for ix, jx in icd_i[i]:
        if ix == i:
            icd[ix, jx] = min(icd[ix, jx], icd[jx, j] if jx < j else icd[j, jx])
        elif jx == i:
            icd[ix, jx] = min(icd[ix, jx], icd[ix, j] if ix < j else icd[j, ix])

    for ix, jx in tups:
        del icd[ix, jx]



# print("loop took", time() - start_time)

min_dist = min(icd.values())
print(min_dist)
