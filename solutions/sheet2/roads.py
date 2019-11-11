import sys
from itertools import product
from math import sqrt

# parse

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
points = [[int(v) for v in line.split(' ')] for line in lines[1:]]

# calc

min_x, max_x = min(p[0] for p in points), max(p[0] for p in points)
min_y, max_y = min(p[1] for p in points), max(p[1] for p in points)


def is_left(p0, p1, p2):
    return (p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] - p0[0]) * (p1[1] - p0[1])


def dist(a,b):
    return sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)


edges = list(zip(points, points[1:] + [points[0]]))


def is_inside(p):
    wn = 0  # winding number

    for p1, p2 in edges:
        # is vertex or on edge
        if p == p1 or p == p2 or abs(dist(p1,p) + dist(p2,p) - dist(p1,p2)) < 1e-8:
            return True

        if p1[1] <= p[1]:
            if p2[1] > p[1] and is_left(p1, p2, p) > 0:
                wn += 1
        elif p2[1] <= p[1] and is_left(p1, p2, p) < 0:
            wn -= 1

    return wn != 0


num = sum(1 if is_inside((x,y)) else 0 for x, y in product(range(min_x, max_x + 1), range(min_y, max_y + 1)))

# output
print(num)
