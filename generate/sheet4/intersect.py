import numpy as np
from shapely.geometry.polygon import Polygon
from shapely.geometry.point import Point
from shapely.errors import TopologicalError
from time import time
import logging

logging.disable()


def make_simple_polygon(k):
    p = None
    while not p:
        points = np.random.randint(0, 10, size=(k, 2))
        p = Polygon(points)
        try:
            if not p.is_simple:
                p = None
        except ValueError:
            p = None
    return points


class Intersect:
    @staticmethod
    def get_random_instance():
        area = 0

        c = 0
        while area == 0:
            # create instance
            n = np.random.randint(3, 7)
            ki = np.random.randint(3, 10, size=n)
            polygons = [make_simple_polygon(k) for k in ki]

            # solve instance
            try:
                ipoly = Polygon(polygons[0])
                for p in polygons[1:]:
                    ipoly = ipoly.intersection(Polygon(p))
                area = ipoly.area
            except TopologicalError:
                pass
            c += 1

        # print("took",c,"to make an instance")

        # try to solve with points
        # find smallest bounding box
        # test points with resolution st rounding error <0.05
        # stime = time()
        #
        # bb = Polygon(polygons[0]).envelope
        # for poly in polygons[1:]:
        #     p = Polygon(poly)
        #     bb = bb.intersection(p.envelope).envelope
        #
        # min_x, min_y = bb.exterior.coords[0]
        # max_x, max_y = bb.exterior.coords[2]
        #
        # # min_x = min_y = 0
        # # max_x = max_y = 10
        #
        # # resolution = 20
        # # samples_x = np.linspace(min_x,max_x,resolution*(max_x-min_x)+1)
        # # samples_y = np.linspace(min_y,max_y,resolution*(max_y-min_y)+1)
        # # xx, yy = np.meshgrid(samples_x, samples_y)
        #
        # num_samples = 100000
        # xx, yy = np.random.random_sample((2, num_samples))
        # xx = (max_x - min_x) * xx + min_x
        # yy = (max_y - min_y) * yy + min_y
        # bb_area = (max_x - min_x) * (max_y - min_y)
        #
        # grid_points = [Point(x, y) for x, y in zip(np.ravel(xx), np.ravel(yy))]
        #
        # for poly in polygons:
        #     p = Polygon(poly)
        #     grid_points = [g for g in grid_points if g.intersects(p)]
        #
        # area_per_gp = area / len(grid_points) if len(grid_points) > 0 else 0
        # area_estimate = bb_area * len(grid_points) / num_samples
        # estimation_error = abs(area_estimate - area)
        #
        # debug_text = f"{n}-poly [{ki.sum()} edges] with an area of {area:.3f} we found {len(grid_points):>4} points intersecting => " \
        #     f"{area_per_gp:.5f} in {time() - stime:.2f}s, estimate of {area_estimate:.3f} is {estimation_error:.3f} off"
        #
        # if estimation_error > 0.05:
        #     print(debug_text, "WIU WIU WIU!")
        # else:
        #     print(debug_text)

        input_str = f"{n}\n" + '\n'.join(f"{k} " + ' '.join(str(v) for v in np.ravel(p)) for k, p in zip(ki, polygons))
        output_str = f"{ipoly.area}"

        return input_str, output_str

    @staticmethod
    def special_instances():
        yield "2\n4 1 1 4 1 4 4 1 4\n3 2 0 6 0 4 2", "0.5"

    @staticmethod
    def validate_output(given_out, correct_out):
        return abs(float(given_out)-float(correct_out)) <= 0.05


if __name__ == "__main__":
    for _ in range(20):
        i, o = Intersect.get_random_instance()
    #
    # print(i)
    # print("+" * 10)
    # print(o)
