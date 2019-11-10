from math import log10, floor
from random import randint
import numpy as np
from shapely.geometry import Polygon, LinearRing

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


def generate_star_polygon(n, max_radius, shift_range):
    # generate polygon by polar coordinates
    angles = np.random.random(n) * 2 * np.pi
    angles = -np.sort(-angles)
    radii = np.random.random(n) * max_radius

    # determine cartesian coords and round
    p = np.round(radii * np.stack([np.cos(angles), np.sin(angles)])).T

    # shift polygon
    if shift_range > 0:
        shift = np.random.randint(-shift_range, shift_range, size=2)
        p += shift

    return p


def generate_simple_polygon(n, max_radius, shift_range):
    polygon = None

    while polygon is None or not polygon.is_valid:
        # generate random points inside circle of max_radius
        angles = np.random.random(n) * 2 * np.pi
        radii = np.random.random(n) * max_radius

        # determine cartesian coords and round
        p = np.round(radii * np.stack([np.cos(angles), np.sin(angles)])).T

        # shuffle a bit before retrying completely
        for _ in range(100):
            polygon = Polygon(shell=np.random.shuffle(p))
            if polygon.is_valid:
                break

    if shift_range > 0:
        shift = np.random.randint(-shift_range, shift_range, size=2)
        p += shift

    return p



if __name__ == '__main__':
    vals = [randint(-1000,1000)/100 for _ in range(100000)]
    for v in vals:
        sv = f"{v:0.2f}"
        if sv != int_to_dec(dec_to_int(sv)):
            raise Exception("Failed for", sv,"!=",int_to_dec(dec_to_int(sv)))