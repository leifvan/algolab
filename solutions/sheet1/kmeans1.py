import sys

# parse

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
points = sum((l.split() for l in lines[1:]), [])

# calc

points = [int(v)**2 for v in points]
s = sum(points)

# output

print("{:.30f}".format(s))

