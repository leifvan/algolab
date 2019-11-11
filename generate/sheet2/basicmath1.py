import numpy as np
from math import sqrt, ceil, floor
from numba import njit


@njit
def is_int(val):
    return floor(val) == val

class BasicMath1:

    @staticmethod
    def get_random_instance():

        @njit
        def get_solution(u,v,w):
            solutions = []

            # this will only have a solution if u >= v**2/3
            if w >= u ** 2 / 3:
                lower = 1 / 3 * (u - np.sqrt(2) * np.sqrt(3 * w - u ** 2))
                upper = 1 / 3 * (np.sqrt(2) * np.sqrt(3 * w - u ** 2) + u)

                x = np.arange(ceil(lower), floor(upper) + 1)
                root = np.sqrt(2 * w - u ** 2 + 2 * u * x - 3 * x ** 2)
                y = 0.5 * (-root + u - x)
                z = 0.5 * (root + u - x)

                for xi, yi, zi in zip(x, y, z):
                    if xi * yi * zi == v and xi != yi != zi and is_int(xi) and is_int(yi) and is_int(zi):
                        solutions.append((xi,yi,zi))

                y = 0.5 * (root + u - x)
                z = 0.5 * (-root + u - x)

                for xi, yi, zi in zip(x, y, z):
                    if xi * yi * zi == v and xi != yi != zi and is_int(xi) and is_int(yi) and is_int(zi):
                        solutions.append((xi,yi,zi))

            if len(solutions) > 0:
                solutions.sort()
                return solutions[0]
            return None

        ran_vals = np.random.randint(1, 12000, size=(10000, 3))
        ran_vals[:,0] = np.floor(np.sqrt(ran_vals[:,0])).astype(np.int)

        inputs = []
        outputs = []

        for u,v,w in ran_vals:
            s = get_solution(u,v,w)

            # only add empty set with a 0.1% chance
            if s is not None or np.random.random() < 0.001:
                inputs.append(f"{u} {v} {w}")

                if s is None:
                    outputs.append("empty set")
                else:
                    outputs.append(f"{int(s[0])} {int(s[1])} {int(s[2])}")

        assert len(inputs) > 0

        input_str = f"{len(inputs)}\n" + '\n'.join(inputs)
        output_str = '\n'.join(outputs) + '\n'

        return input_str, output_str

    @staticmethod
    def special_instances():
        yield "3\n1 1 1\n88 1136 5298\n42 420 842", "empty set\n1 16 71\n1 20 21\n"


if __name__ == "__main__":
    BasicMath1.get_random_instance()
