from math import log10, floor
from random import randint


def int_to_dec(i):
    sgn = '-' if i < 0 else ''
    if abs(i) < 10:
        return sgn+"0.0"+str(abs(i))
    elif abs(i) < 100:
        return sgn+"0."+str(abs(i))
    else:
        return str(i)[:-2] + "." + str(i)[-2:]


def dec_to_int(d, j=2):
    d = d.replace('.','')
    return int(d)


if __name__ == '__main__':
    vals = [randint(-1000,1000)/100 for _ in range(100000)]
    for v in vals:
        sv = f"{v:0.2f}"
        if sv != int_to_dec(dec_to_int(sv)):
            raise Exception("Failed for", sv,"!=",int_to_dec(dec_to_int(sv)))