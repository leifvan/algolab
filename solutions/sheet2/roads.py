import sys
from math import ceil, floor

HORIZONTAL = "h"
INTERSECTION = "i"
TOUCH = "t"

# parse

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
points = [tuple(int(v) for v in line.split(' ')) for line in lines[1:]]
edges = list(tuple(zip(points, points[1:] + [points[0]])))


min_x, max_x = min(p[0] for p in points), max(p[0] for p in points)
min_y, max_y = min(p[1] for p in points), max(p[1] for p in points)


def get_x_intersection(e, y):
    a = (y - e[1][1]) / (e[0][1] - e[1][1])
    return round(a * e[0][0] + (1 - a) * e[1][0], 3)


def sign(v):
    if v == 0:
        return 0
    return 1 if v >= 0 else -1


# filter co-linear vertices

def get_edge_slope(e):
    if e[0][0] == e[1][0]:
        return float('inf') if e[0][1] < e[1][1] else float('-inf')
    return (e[1][1] - e[0][1]) / (e[1][0] - e[0][0])


edge_slopes = {e: get_edge_slope(e) for e in edges}
same_slope_vertices = [p for p1, p, p2 in zip([points[-1]] + points[:-1], points, points[1:] + [points[0]])
                       if edge_slopes[(p1, p)] == edge_slopes[(p, p2)]]

points = [p for p in points if p not in same_slope_vertices]
edges = list(tuple(zip(points, points[1:] + [points[0]])))


def get_edge_y_slope(e):
    return e[0][1] - e[1][1]


edge_y_slopes = {e: get_edge_y_slope(e) for e in edges}
point_y_slopes = {p: (edge_y_slopes[(p1, p)], edge_y_slopes[(p, p2)])
                  for p1, p, p2 in zip([points[-1]] + points[:-1], points, points[1:] + [points[0]])}

potential_edges = set(edges)
num_inside = 0


def get_vertex_y_slope(p1, p2, p3):
    return (p1[1] - p2[1]) * (p2[1] - p3[1])


def get_non_null_slope(s1, s2):
    if abs(s1) > abs(s2):
        return s1
    return s2


for y in range(min_y, max_y + 1):
    x = set()
    marked_for_removal = set()

    for e in potential_edges:
        if e[0][1] == y or e[1][1] == y:  # line touches endpoint(s)
            if e[0][1] == e[1][1]:  # edge is horizontal
                # definitely remove
                e0_slope = get_non_null_slope(*point_y_slopes[e[0]])
                e1_slope = get_non_null_slope(*point_y_slopes[e[0]])
                x.add((e[0][0], HORIZONTAL, e0_slope))
                x.add((e[1][0], HORIZONTAL, e1_slope))
                marked_for_removal.add(e)
            else:
                point = e[0] if y == e[0][1] else e[1]
                s1, s2 = point_y_slopes[point]
                x.add((point[0], TOUCH, s1 * s2))

                # remove if endpoint of edge
                if y >= e[0][1] and y >= e[1][1]:
                    marked_for_removal.add(e)
        elif e[0][1] < y < e[1][1] or e[1][1] < y < e[0][1]:  # line intersects edge
            xi = get_x_intersection(e, y)
            x.add((xi, INTERSECTION, None))

    x = sorted(x)

    added = 0

    entry_x = None
    last_x = None
    entry_slope = None
    h_from_inside = False

    for xi, type, slope in x:
        if xi != last_x:  # sometimes we have multiple types at the same xi
            if entry_x is not None:  # coming from inside to p
                added += floor(xi) - ceil(entry_x) + 1

                if type == HORIZONTAL:
                    if entry_slope is None: # was something else before, horizontal begins here
                        entry_x = xi
                        added -= 1
                        entry_slope = slope
                        h_from_inside = True
                    elif entry_slope * slope < 0:  # was h before and we restore inside state
                        if h_from_inside:
                            entry_x = xi
                            added -= 1
                        else:
                            entry_x = None
                        entry_slope = None

                    else: # entry_slope * slope > 0, so we stay inside
                        entry_x = xi
                        added -= 1
                        entry_slope = None
                elif type == TOUCH and slope < 0:
                    entry_x = xi
                    added -= 1
                else:
                    entry_x = entry_slope = None

            else:  # coming from outside to p
                if type == TOUCH and slope < 0:
                    added += 1
                else:
                    entry_x = xi
                    if type == HORIZONTAL:
                        entry_slope = slope
                        h_from_inside = False

        last_x = xi

    if entry_x is not None:
        added += 1

    num_inside += added
    potential_edges.difference_update(marked_for_removal)

# output
print(num_inside)
