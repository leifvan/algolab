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

set_size = [1] * n
union_find = dict()


def find(v):
    # use path splitting
    child = None
    while v in union_find:
        grandchild = child
        child = v
        v = union_find[v]

        if grandchild is not None:
            union_find[grandchild] = v
    return v


def union(v, w):
    if set_size[v] < set_size[w]:
        v, w = w, v
        # w is now the bigger set
    union_find[v] = w
    set_size[w] += set_size[v]


num_sets = n

# do kruskal

for i, j, w in edges:
    si, sj = find(i), find(j)
    if si != sj:  # check if new edge connects same cluster
        union(si, sj)
        num_sets -= 1

        if num_sets == k - 1:
            break

print(w)
