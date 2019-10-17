import sys
from math import floor, ceil
from fractions import Fraction
from decimal import Decimal

# parse
lines = [l.strip().replace('.','') for l in sys.stdin]
n = int(lines[0])
grid_size = int(lines[1])
#grid_size = Decimal(lines[1])
#grid_size = float(lines[1])
points = sum((l.split() for l in lines[2:]), [])
points = [int(v)//grid_size*grid_size for v in points]

# calc
#points = [Decimal(v) for v in points]
#points = [floor(v/grid_size)*grid_size for v in points]
# grid_size = Fraction(int(grid_size*100), 100)
# points = [Fraction(int(float(v)*100), 100)/grid_size for v in points]
# points = [Fraction(floor(f))*grid_size for f in points]
#points = [floor(float(v)/grid_size)*grid_size for v in points]

def int_to_dec(i):
    sgn = '-' if i < 0 else ''
    if abs(i) < 10:
        return sgn+"0.0"+str(abs(i))
    elif abs(i) < 100:
        return sgn+"0."+str(abs(i))
    else:
        return str(i)[:-2] + "." + str(i)[-2:]

# output
for x, y in zip(points[::2], points[1::2]):
    print(int_to_dec(x),int_to_dec(y))
