import sys
from itertools import combinations
from operator import itemgetter
from time import time

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

start_time = time()

# floyd warshall
for r in range(n):
    for i in range(n):
        for j in range(i+1):
            if dist_mat[i][r] + dist_mat[r][j] < dist_mat[i][j]:
                dist_mat[i][j] = dist_mat[j][i] = dist_mat[i][r] + dist_mat[r][j]

print("floyd took", time() -start_time)
start_time = time()

# init: all points are their own cluster
members = {v: [v] for v in range(n)}
icd = {(i, j): dist_mat[i][j] for i, j in combinations(range(n), 2)}

while len(members) > k:
    # find min pair
    i, j = min(icd.items(), key=itemgetter(1))[0]

    # join two closest clusters together
    members[i].extend(members[j])
    del members[j]
    icd = {(i, j): min(dist_mat[v][w] for v in members[i] for w in members[j])
           for i, j in icd if i in members and j in members}

print("looperz took", time() - start_time)

min_dist = min(icd.values())

print(min_dist)
