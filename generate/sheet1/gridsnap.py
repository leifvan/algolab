import random
from decimal import Decimal
from math import floor, ceil


class GridSnap:
    @staticmethod
    def get_random_instance():
        grid_size = Decimal(random.randint(1, 100))
        n = random.randint(1, 100)
        # generate 2n numbers
        points = [random.randint(-10000, 10000) for _ in range(2 * n)]
        noise = [Decimal(random.randint(0, grid_size-1)) / 100 for _ in range(2 * n)]
        shifted = [p + e for p, e in zip(points, noise)]
        grid_size /= 100
        points = [p * grid_size for p in points]
        shifted = [p * grid_size for p in shifted]
        input_str = f"{n}\n{grid_size:.2f}\n"
        input_str += '\n'.join(f"{x:.2f} {y:.2f}" for x, y in zip(shifted[::2], shifted[1::2]))
        output_str = '\n'.join(f"{x:.2f} {y:.2f}" for x, y in zip(points[::2], points[1::2]))+"\n"
        return input_str, output_str

    @staticmethod
    def special_instances():
        yield "3\n0.75\n0.00 0.00\n-0.75 0.00\n1.00 2.15", "0.00 0.00\n-0.75 0.00\n0.75 1.50\n"
