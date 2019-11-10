import sys

# parse

lines = [l.strip().replace('.', '') for l in sys.stdin]
c, q, r = [int(v) for v in lines[0].split()]
centers = sorted(int(v) for v in lines[1:c + 1]) + [float('inf')]
points = sorted(((i,int(v)) for i,v in enumerate(lines[c + 1:c+1+q])), key=lambda tup: tup[1])

# calc

idxs = [None] * len(points)
ci = 0

for i, p in points:
    dist = abs(p - centers[ci])
    dist_next = abs(p - centers[ci + 1])

    while dist_next < dist:
        ci += 1
        dist = dist_next
        dist_next = abs(p - centers[ci+1])

    if dist <= r:
        idxs[i] = ci

# output


def int_to_dec(i):
    sgn = '-' if i < 0 else ''
    if abs(i) < 10:
        return sgn + "0.0" + str(abs(i))
    elif abs(i) < 100:
        return sgn + "0." + str(abs(i))
    else:
        return str(i)[:-2] + "." + str(i)[-2:]


for i in idxs:
    print('none in range' if i is None else int_to_dec(centers[i]))
