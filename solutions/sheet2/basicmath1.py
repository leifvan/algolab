import sys
from math import sqrt, floor, ceil

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
problems = [[int(v) for v in line.split(' ')] for line in lines[1:]]


def is_int(val):
    return floor(val) == val


def solve_problem(u, v, w):
    if w < u ** 2 / 3:  # requirement for the u and w equations to have any solution
        print("empty set")
        return

    # determine solution range for x
    lower = 1 / 3 * (u - sqrt(2) * sqrt(3 * w - u ** 2))
    upper = 1 / 3 * (sqrt(2) * sqrt(3 * w - u ** 2) + u)

    for x in range(ceil(lower), floor(upper) + 1):
        # check if root is positive
        root_term = 2 * w - u ** 2 + 2 * u * x - 3 * x ** 2

        if root_term >= 0:
            # there are two possible solutions for y,z given x
            root = sqrt(root_term)
            y1 = z2 = 0.5 * (-root + u - x)
            z1 = y2 = 0.5 * (root + u - x)

            if y1 < y2:
                y2, y1 = y1, y2
                z2, z1 = z1, z2
            elif y1 == y2 and z1 < z2:
                z2, z1 = z1, z2

            # check if it satisfies the v-condition
            if x * y1 * z1 == v and x != y1 and x != z1 and y1 != z1 and is_int(x) and is_int(y1) and is_int(z1):
                print(int(x), int(y2), int(z2))
                return

            if x * y2 * z2 == v and x != y2 and x != z2 and y2 != z2 and is_int(x) and is_int(y2) and is_int(z2):
                print(int(x), int(y2), int(z2))
                return

    # there is still no solution
    print("empty set")


for u, v, w in problems:
    solve_problem(u, v, w)
