import numpy as np
from math import floor, ceil


class Duckburg:
    @staticmethod
    def get_random_instance():
        k = np.random.randint(1,100)
        n = np.random.randint(1,100)
        x = np.random.choice(np.arange(1,1001), size=n, replace=False)
        str_in = '\n'.join(str(v) for v in [k, n] + list(x))
        x = np.sort(x)

        D = np.zeros((k, n))

        def cc(i, j):
            m_ij = (j + i) / 2
            mu_ij = (x[floor(m_ij)] + x[ceil(m_ij)]) / 2
            return sum(abs(x[l] - mu_ij) for l in range(i, j + 1))

        for m in range(n):
            D[0, m] = cc(0, m)

        for i in range(1, k):
            for m in range(1, n):
                D[i, m] = min(D[i - 1, j - 1] + cc(j, m) for j in range(m + 1))

        str_out = str(int(25 * n - D[-1, -1]))
        return str_in, str_out


    @staticmethod
    def special_instances():
        yield "10\n11\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11", "274"

    @staticmethod
    def validate_output(given_out, correct_out):
        return given_out.replace('\n','') == correct_out.replace('\n','')

