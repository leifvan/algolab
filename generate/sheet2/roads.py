from utils import generate_star_polygon
import numpy as np
from shapely.geometry import Polygon, Point
import matplotlib.pyplot as plt


class Roads:
    @staticmethod
    def get_random_instance():
        n = np.random.randint(3, 30)
        p = generate_star_polygon(n, 1000, 0).astype(np.int)
        poly = Polygon(p)
        min_x, max_x = p[:,0].min(), p[:,0].max()
        min_y, max_y = p[:,1].min(), p[:,1].max()
        coords_x = np.arange(min_x, max_x+1)
        coords_y = np.arange(min_y, max_y + 1)
        xx, yy = np.meshgrid(coords_x, coords_y)

        num_inside = sum(1 if poly.intersects(Point(x, y)) else 0
                         for x, y in zip(np.ravel(xx), np.ravel(yy)))

        #p_inside = np.array([[x, y] for x, y in zip(np.ravel(xx), np.ravel(yy)) if poly.intersects(Point(x, y))])
        #p_outside = np.array([[x, y] for x, y in zip(np.ravel(xx), np.ravel(yy)) if not poly.intersects(Point(x, y))])

        #num_inside = len(p_inside)

        #print(p)
        # plt.plot(list(p[:, 0]) + [p[0, 0]], list(p[:, 1]) + [p[0, 1]])
        # plt.scatter(p_inside[:, 0], p_inside[:, 1])
        # plt.scatter(p_outside[:, 0], p_outside[:, 1], c='red')
        # plt.scatter(list(p[:, 0]) + [p[0, 0]], list(p[:, 1]) + [p[0, 1]], c='black')
        # plt.suptitle(f"num_inside = {num_inside}")
        # plt.show()

        input_str = f"{n}\n" + '\n'.join(f"{x} {y}" for x, y in p)
        output_str = f"{num_inside}\n"
        return input_str, output_str

    @staticmethod
    def special_instances():
        yield "5\n0 1\n2 0\n0 -2\n-1 -1\n-2 0", "10\n"
        #yield "14\n0 0\n-1 2\n-3 2\n-4 0\n-5 2\n-3 4\n-2 5\n0 5\n2 5\n3 4\n5 2\n4 0\n3 2\n1 2","38\n"


if __name__ == '__main__':
    Roads.get_random_instance()
