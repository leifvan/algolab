import sys
from bisect import bisect, bisect_left
from math import sqrt
from random import randint

# read first line: length of vector
line = sys.stdin.readline().split(" ")
d = int(line[0])
d2 = randint(0, d - 1)
R = int("".join(line[1].split(".")))
R2 = R * R

centers = [[int("".join(a.split("."))) for a in sys.stdin.readline().split()]]
center_dist = [sqrt(sum(x * x for x in centers[0]))]


def included(numbers, dist):
    cen = [c[d2] for c in centers]
    min = bisect_left(cen, numbers[d2] - R)
    if min == len(centers):
        return False, len(centers)
    max = bisect(cen, numbers[d2] + R, lo=min)
    if max == 0:
        return False, 0
    for center, c_dist in zip(centers[min:max], center_dist[min:max]):
        if abs(dist - c_dist) > R - 1:
            continue
        sum = (center[d2] - numbers[d2]) ** 2
        for i in range(d):
            if i == d2:
                continue
            sum += (center[i] - numbers[i]) ** 2
            if sum > R2:
                break
        if sum <= R2:
            return True, 0
    return False, bisect(cen, numbers[d2], lo=min, hi=max)


# read numbers
for line in sys.stdin:
    numbers = [int("".join(a.split("."))) for a in line.split()]
    dist = sqrt(sum(x ** 2 for x in numbers))
    found, pos = included(numbers, dist)

    if not found:
        centers.insert(pos, numbers)
        center_dist.insert(pos, dist)

print(len(centers))
