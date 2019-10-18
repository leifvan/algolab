import sys

# parse

lines = [l for l in sys.stdin]
n = int(lines[0])
points = [tuple(int(v) for v in l.split()) for l in lines[1:]]

# calc

vol = 0
i = 0

vol = 0.5 * sum((p1[0]+p2[0]) * (p1[1]-p2[1]) for p1, p2 in zip(points, points[1:]+[points[0]]))

# output

print(vol)
