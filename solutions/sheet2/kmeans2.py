import sys

# parse

lines = [l.strip().replace('.','') for l in sys.stdin]
c, q, r = [int(v) for v in lines[0].split()]
centers = sorted(int(v) for v in lines[1:c+1])
points = [int(v) for v in lines[c+1:]]

# calc

idxs = []
for i, p in enumerate(points):
    j, dist = min(((j,abs(p-x)) for j,x in enumerate(centers)), key=lambda tup: tup[1])
    idxs.append(j if dist <= r else None)


# output

def int_to_dec(i):
    sgn = '-' if i < 0 else ''
    if abs(i) < 10:
        return sgn+"0.0"+str(abs(i))
    elif abs(i) < 100:
        return sgn+"0."+str(abs(i))
    else:
        return str(i)[:-2] + "." + str(i)[-2:]


for i in idxs:
    print('none in range' if i is None else int_to_dec(centers[i]))
