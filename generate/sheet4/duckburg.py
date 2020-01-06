import numpy as np
from math import floor, ceil
from numba import njit

class Duckburg:
    @staticmethod
    def get_random_instance():
        k = np.random.randint(1,100)
        n = np.random.randint(1,1000)
        x = np.random.choice(np.arange(1,1001), size=n, replace=False)
        str_in = '\n'.join(str(v) for v in [k, n] + list(x))
        x = np.sort(x)

        @njit
        def cc(x, i, j):
            m_ij = (j + i) / 2
            mu_ij = (x[floor(m_ij)] + x[ceil(m_ij)]) / 2
            return np.abs(x[i:j+1]-mu_ij).sum()

        @njit
        def determine_result(k,n,x):
            D = np.zeros((k, n))

            for m in range(n):
                D[0, m] = cc(x, 0, m)

            for i in range(1, k):
                for m in range(1, n):
                    D[i, m] = min([D[i - 1, j - 1] + cc(x, j, m) for j in range(m + 1)])

            return D[-1,-1]

        result = determine_result(k,n,x)

        str_out = str(int(25 * n - result))
        return str_in, str_out


    @staticmethod
    def special_instances():
        yield "10\n11\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11", "274"

    @staticmethod
    def validate_output(given_out, correct_out):
        return given_out.replace('\n','') == correct_out.replace('\n','')

