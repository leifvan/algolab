import numpy as np
import random
from sklearn.neighbors import NearestNeighbors
from math import sqrt
from hilbertcurve.hilbertcurve import HilbertCurve


class KMeans3:
    @staticmethod
    def get_random_instance():
        d = random.randint(1,100)
        r = round(random.random()*50*sqrt(d), 3)
        num = random.randint(1,1000)
        points = np.random.randint(-100000, 100000, size=(num, d)) / 1000
        centers = np.array([points[0]])

        for p in points[1:]:
            shortest_dist = np.linalg.norm(centers - p, axis=1).min()
            if shortest_dist > r:
                centers = np.concatenate([centers, p[np.newaxis]])

        str_in = f"{d} {r:.3f}\n" + '\n'.join(' '.join(f"{v:.3f}" for v in p) for p in points)
        str_out = f"{len(centers)}\n"
        return str_in, str_out

    @staticmethod
    def special_instances():
        yield "2 1.000\n0.000 0.000\n1.000 1.000\n0.500 0.500\n2.000 1.000\n2.500 0.500\n", "3\n"


if __name__ == "__main__":
    ...