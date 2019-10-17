import sys

# parse

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
points = [l.split() for l in lines[1:]]
points = [(int(x), int(y)) for x,y in points]

# calc

vol = 0
i = 0
for p1, p2 in zip(points, points[1:]+[points[0]]):
    vol += (p1[0]+p2[0]) * (p1[1]-p2[1])
    i += 1
vol /= 2


# output

print(vol)
