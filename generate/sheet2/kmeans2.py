import numpy as np
from sklearn.neighbors import NearestNeighbors
from utils import int_to_dec


class KMeans2:
    @staticmethod
    def get_random_instance():
        c = np.random.randint(2, 10000)
        q = np.random.randint(1, 10000)
        r = np.random.randint(1, 100)
        centers = np.unique(np.random.randint(-100, 100, size=c))
        np.random.shuffle(centers)
        c = len(centers)
        points = np.random.randint(-100, 100, size=q)
        nn = NearestNeighbors(n_neighbors=2, p=1).fit(np.reshape(centers, (-1, 1)))
        dists, idxs = nn.kneighbors(np.reshape(points, (-1, 1)))

        in_str = f"{c} {q} {int_to_dec(r)}\n"
        in_str += '\n'.join(int_to_dec(cen) for cen in centers) + '\n'
        in_str += '\n'.join(int_to_dec(p) for p in points) + '\n'

        out_str = ""
        for d, i in zip(dists, idxs):
            if d[0] > r:
                out_str += 'none in range\n'
            else:
                if d[1] == d[0]:
                    cen = min(centers[i[0]], centers[i[1]])
                else:
                    cen = centers[i[0]]
                out_str += int_to_dec(cen)+'\n'
        return in_str, out_str


    @staticmethod
    def special_instances():
        yield "2 3 1.00\n0.00\n1.00\n1.10\n0.50\n10.00", "1.00\n0.00\nnone in range\n"


if __name__ == '__main__':
    i, o = KMeans2.get_random_instance()
    print(i)
    print("-"*10)
    print(o)