import sys
from itertools import combinations

lines = list(sys.stdin)
r = int(lines[0])


field = [int(l.strip(), 2) for l in lines[1:]]

count = 0


for a, b in combinations(range(r), r=2):
    cur = bin(field[a] & field[b]).count('1')
    count += ((cur-1)*cur)//2

print(count)