import sys
from itertools import product

# parse

lines = [l.strip() for l in sys.stdin]
n, m = int(lines[0]), int(lines[1])
rows = [[int(v) for v in line.split(' ')] for line in lines[2:]]

# calc

prev_irow = [sum(rows[0][:i]) for i in range(1, m+1)]
cur_irow = [0]*m

for i, row in enumerate(rows[1:]):
    cur_irow[0] = prev_irow[0] + row[0]
    for j in range(1,m):
        cur_irow[j] = max(cur_irow[j-1], prev_irow[j]) + row[j]
    prev_irow = cur_irow

# output

print(cur_irow[-1])
