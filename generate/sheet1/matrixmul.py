import numpy as np
from scipy.sparse import csr_matrix, find


def _csr_to_string(mat):
    I,J,V = find(mat)

    if mat.shape[1] == 1:
        s = [f"{i} {v}" for i,v in zip(I,V)]
    else:
        s = [f"{i} {j} {v}" for i, j, v in zip(I, J, V)]

    #s.sort()

    if len(s) > 0:
        return '\n'.join(s) + '\n'
    else:
        return ''


def get_random_nonzero(low, high, size=None):
    a = np.random.randint(low, high-1, size)
    a[a >= 0] += 1
    assert len(a[a == 0]) == 0
    return a


class MatrixMul:
    @staticmethod
    def get_random_instance():
        n = np.random.randint(1,100000)
        m = np.random.randint(0, n // 100 if n > 100 else n)
        b = np.random.randint(0, n // 100 if n > 100 else n)

        i = np.random.choice(n, size=m, replace=False)
        j = np.random.choice(n, size=m, replace=False)
        a = get_random_nonzero(-5, 5, size=m)
        mat = csr_matrix((a, (i,j)), shape=(n,n))

        k = np.random.choice(n, size=b, replace=False)
        v = get_random_nonzero(-5, 5, size=b)
        vec = csr_matrix((v, (k, np.zeros_like(k))), shape=(n, 1))

        res = mat.dot(vec)
        assert mat.has_sorted_indices

        str_in = f"{n}\n{m}\n" + _csr_to_string(mat) + f"{b}\n" + _csr_to_string(vec)
        str_out = _csr_to_string(res)
        if len(str_out) == 0:
            str_out = '\n'

        return str_in, str_out

    @staticmethod
    def special_instances():
        yield "3\n4\n0 0 1\n0 1 -5\n0 2 -4\n1 0 -3\n2\n0 3\n2 3", "0 -9\n1 -9\n"
        yield "5\n0\n0", "\n"
        yield "1\n1\n0 0 3\n1\n0 2", "0 6\n"
