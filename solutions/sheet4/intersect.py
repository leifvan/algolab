import sys
from random import random
from time import time

stime = time()

n = int(sys.stdin.readline())
lines = [[int(v) for v in line.split(" ")] for line in sys.stdin]
polygons = [line[1:] for line in lines]
polygons = [[(x, y) for x, y in zip(p[::2], p[1::2])] for p in polygons]


def orientation(p1, p2, p3):
    val = (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1])
    return 1 if val > 0 else -1


def lines_intersect(p1, p2, q1, q2):
    o1 = orientation(p1, p2, q1)
    o2 = orientation(p1, p2, q2)
    if o1 != o2:
        o3 = orientation(q1, q2, p1)
        o4 = orientation(q1, q2, p2)
        return o3 != o4

    return False


def point_in_polygon(p1, polygon):
    i = 0
    p2 = (11, p1[1])
    for q1, q2 in zip(polygon, polygon[1:] + [polygon[0]]):
        if lines_intersect(q1, q2, p1, p2):
            i += 1

    return i % 2 == 1


def get_sample_in_bb(min_x, min_y, max_x, max_y):
    return (max_x - min_x) * random() + min_x, (max_y - min_y) * random() + min_y


def polygon_volume(points):
    return 0.5 * sum((p1[0] + p2[0]) * (p1[1] - p2[1]) for p1, p2 in zip(points, points[1:] + [points[0]]))


# find minimal bounding box
min_x = min_y = 0
max_x = max_y = 10

for polygon in polygons:
    cur_min_x = min(p[0] for p in polygon)
    cur_min_y = min(p[1] for p in polygon)
    cur_max_x = max(p[0] for p in polygon)
    cur_max_y = max(p[1] for p in polygon)
    min_x = max(min_x, cur_min_x)
    min_y = max(min_y, cur_min_y)
    max_x = min(max_x, cur_max_x)
    max_y = min(max_y, cur_max_y)


polygons.sort(key=polygon_volume)

bb_area = (max_x - min_x) * (max_y - min_y)
num_samples = 0
num_hits = 0

while time() - stime < 0.9:
    num_samples += 1
    s = get_sample_in_bb(min_x, min_y, max_x, max_y)
    if all(point_in_polygon(s, poly) for poly in polygons):
        num_hits += 1

area = bb_area * num_hits / num_samples

print("{:.2f}".format(area))
