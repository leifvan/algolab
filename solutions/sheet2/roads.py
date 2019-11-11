import sys
from itertools import product
from math import sqrt, ceil, floor
from collections import defaultdict

# parse

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
points = [tuple(int(v) for v in line.split(' ')) for line in lines[1:]]
edges = list(zip(points, points[1:] + [points[0]]))

print(edges)
# calc

min_x, max_x = min(p[0] for p in points), max(p[0] for p in points)
min_y, max_y = min(p[1] for p in points), max(p[1] for p in points)


def get_x_intersection(e, y):
    # TODO careful with VERTICAL edges?
    a = (y - e[1][1]) / (e[0][1] - e[1][1])
    return round(a * e[0][0] + (1 - a) * e[1][0], 3)


def sign(v):
    if v == 0:
        return 0
    return 1 if v >= 0 else -1


y_direction_changes = {p: sign(p1[1] - p[1]) * sign(p[1] - p2[1]) < 0 for p1, p, p2 in
                       zip([points[-1]] + points[:-1], points, points[1:] + [points[0]])}
potential_edges = set(tuple(e) for e in edges)

num_inside = 0

for y in range(min_y, max_y + 1):
    print()
    print("we are in y =", y)
    x = set()
    touchers = set()
    marked_for_removal = set()

    for e in potential_edges:
        if e[0][1] == y or e[1][1] == y:  # line touches endpoint(s)
            if e[0][1] == e[1][1]:  # edge is horizontal
                # definitely remove
                # x.add(e[0][0])
                # x.add(e[1][0])
                if e[1][0] > e[0][0]:
                    touchers.update(range(e[0][0], e[1][0] + 1))
                else:
                    touchers.update(range(e[1][0], e[0][0] + 1))
                marked_for_removal.add(e)
                print(e, "is horizontal")
            else:
                point = e[0] if y == e[0][1] else e[1]
                if y_direction_changes[point]:
                    print(e, "touches and changes direction SPIWI!")
                    touchers.add(point)
                else:
                    print(e, "touches and does not change direction")
                    x.add(point[0])

                # remove if endpoint of edge
                if y >= e[0][1] and y >= e[1][1]:
                    marked_for_removal.add(e)
                    print(" ---> and ends here")
                else:
                    print(" ---> and begins here")
        elif e[0][1] < y < e[1][1] or e[1][1] < y < e[0][1]:  # line intersects edge
            xi = get_x_intersection(e, y)
            x.add(xi)
            print(e, "intersects y at x =", xi)
        else:  # not to be considered
            ...

    x = sorted(x)
    print("sorted x:", x)
    for x0, x1 in zip(x[::2], x[1::2]):
        touchers.update(range(ceil(x0), floor(x1) + 1))
    added = len(touchers)
    # touchers.update(range(ceil(x0), floor(x1) + 1) for x0, x1 in zip(x[::2], x[1::2]))
    # added = sum(floor(x1) - ceil(x0) + 1 for x0, x1 in zip(x[::2], x[1::2]))
    # assert touches % 2 == 0
    num_inside += added
    print("=>", num_inside - added, "+", added, "=", num_inside)
    potential_edges.difference_update(marked_for_removal)
    print(" - and removing", marked_for_removal)

# output
print(num_inside)
