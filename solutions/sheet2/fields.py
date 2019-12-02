import sys
from itertools import combinations

lines = list(sys.stdin)
r = int(lines[0])

# num_ones = sum(line.count('1') for line in lines[1:])
# print(num_ones,"of",r**2,"{:.2%}".format(num_ones/r**2))

tree_rows = [[j for j,c in enumerate(line) if c == '1'] for i, line in enumerate(lines[1:])]
tree_cols = [[i for i in range(r) if j in tree_rows[i]] for j in range(r)]

trees = set().union(*(set((i,j) for j in row) for i, row in enumerate(tree_rows)))

count = 0

for i1, row in enumerate(tree_rows):
    for j1, j2 in combinations(row, 2):
        for i2 in tree_cols[j1]:
            if i2 > i1:
                if (i2, j2) in trees:
                    count += 1

print(count)


# tree_rows = [[j for j,c in enumerate(line) if c == '1'] for i, line in enumerate(lines[1:])]
# tree_cols = [[i for i in range(r) if j in tree_rows[i]] for j in range(r)]
#
# trees = set().union(*(set((i,j) for j, c in enumerate(line) if c == '1') for i, line in enumerate(lines[1:])))
#
# count = 0
#
# for i1, row in enumerate(tree_rows):
#     for j1, j2 in combinations(row, 2):
#         for i2 in tree_cols[j1]:
#             if i2 > i1:
#                 if (i2, j2) in trees:
#                     count += 1
#
# print(count)
