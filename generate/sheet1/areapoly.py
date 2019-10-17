import numpy as np


class AreaPoly:
    @staticmethod
    def get_random_instance():
        n = np.random.randint(3,20)

        # generate polygon by polar coordinates
        angles = np.random.random(n) * 2 * np.pi
        angles = -np.sort(-angles)
        radii = np.random.random(n) * 500

        # determine cartesian coords and round
        p = np.round(radii * np.stack([np.cos(angles), np.sin(angles)])).T

        # determine volume
        ps = np.roll(p, -1, axis=0)
        ps[:,1] *= -1
        vols = np.prod(p + ps, axis=1)
        vol = np.sum(vols) / 2

        # shift polygon
        shift = np.random.randint(-500,500)
        p += shift

        str_in = f"{n}\n"+'\n'.join(f"{x:.0f} {y:.0f}" for x,y in p)
        str_out = f"{vol}\n"

        return str_in, str_out

    @staticmethod
    def special_instances():
        yield "5\n-1 0\n0 1\n2 0\n1 -1\n0 -2", "4.5\n"


if __name__ == '__main__':
    i, o = AreaPoly.get_random_instance()
    print(i)
    print(o)