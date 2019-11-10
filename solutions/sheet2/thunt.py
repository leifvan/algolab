import sys
from itertools import product

# parse

lines = [l.strip() for l in sys.stdin]
n, m = int(lines[0]), int(lines[1])
rows = [[int(v) for v in line.split(' ')] for line in lines[2:]]

# calc

integral = [[0]*m for _ in range(n)]

for i,j in product(range(n), range(m)):

    integral[i][j] = rows[i][j]

    if i > 0 and j == 0:
        integral[i][j] += integral[i-1][j]
    elif i == 0 and j > 0:
        integral[i][j] += integral[i][j-1]
    elif i > 0 and j > 0:
        integral[i][j] += max(integral[i-1][j], integral[i][j-1])

# output

print(integral[-1][-1])
