import sys
from operator import itemgetter
from time import time

start_time = time()

lines = list(sys.stdin)
n = int(lines[0])
k = int(lines[1])
m = int(lines[2])

edges = [tuple(int(v) for v in line.split()) for line in lines[3:]]
edges = sorted(edges, key=itemgetter(2))

union_find = dict()


def find(v):
    while v in union_find:
        v = union_find[v]
    return v


def union(v, w):
    union_find[v] = w


num_sets = n

# do kruskal

for i, j, w in edges:
    si, sj = find(i), find(j)
    if si != sj:  # check if new edge would form a circle
        union(si, sj)
        num_sets -= 1

        if num_sets == k - 1:
            break

print(w)
