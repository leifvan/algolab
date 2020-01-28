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

MAX_VAL = 1000000

dist_mat = [[MAX_VAL] * n for _ in range(n)]

for i in range(n):
    dist_mat[i][i] = 0

for i, j, weight in edges:
    dist_mat[i][j] = dist_mat[j][i] = weight

new_dist_mat = [None] * n

edges_i = defaultdict(list)
for i, j, _ in edges:
    edges_i[i].append(j)
    edges_i[j].append(i)

# dijkstra
for s in range(n):
    dist = [MAX_VAL] * n
    dist[s] = 0
    #queue = list(range(n))#sorted(range(n), key=lambda v: dist[v])

    for u in range(n):
        #u = queue.pop()
        for v in edges_i[u]:
            if dist[u] + dist_mat[u][v] < dist[v]:
                dist[v] = dist[u] + dist_mat[u][v]
                #queue.sort(key=lambda v: dist[v])

    new_dist_mat[s] = dist
dist_mat = new_dist_mat

print("dijkstra in {:.3f}".format(time()-start_time))
start_time = time()

nearest_vertex = [None] * n

for i in range(n):
    nearest_vertex[i] = min(enumerate(dist_mat[i]), key=lambda t: t[1] if i != t[0] else MAX_VAL)

for _ in range(n - k):
    i, (j, d) = min(enumerate(nearest_vertex), key=lambda tup: tup[1][1])

    # merge i,j into i
    for k in range(n):
        dist_mat[i][k] = dist_mat[k][i] = min(dist_mat[i][k], dist_mat[j][k])
        dist_mat[j][k] = dist_mat[k][j] = MAX_VAL

    dist_mat[i][j] = MAX_VAL

    nearest_vertex[i] = min(enumerate(dist_mat[i]), key=lambda t: t[1] if i != t[0] and j != t[0] else MAX_VAL)
    nearest_vertex[j] = (-1, MAX_VAL)

    nearest_vertex = [(i, dr) if r == i or r == j else (r, dr) for r, dr in nearest_vertex]

print("loop in {:.3f}".format(time()-start_time))
_, result = min(nearest_vertex, key=itemgetter(1))
print(result)