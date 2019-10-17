import sys

# parse

lines = [l.strip().replace('.','') for l in sys.stdin]
n = int(lines[0])
grid_size = int(lines[1])
points = sum((l.split() for l in lines[2:]), [])


# calc

points = [int(v)//grid_size*grid_size for v in points]


# output

def int_to_dec(i):
    sgn = '-' if i < 0 else ''
    if abs(i) < 10:
        return sgn+"0.0"+str(abs(i))
    elif abs(i) < 100:
        return sgn+"0."+str(abs(i))
    else:
        return str(i)[:-2] + "." + str(i)[-2:]


for x, y in zip(points[::2], points[1::2]):
    print(int_to_dec(x),int_to_dec(y))
