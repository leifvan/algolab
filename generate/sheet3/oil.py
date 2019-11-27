import numpy as np
from itertools import product
from numba import njit, prange


class Oil:
    @staticmethod
    def get_random_instance():
        n = np.random.randint(1,300)
        field = np.zeros((n+1,n+1), dtype=np.int)
        field[1:,1:] = np.random.randint(-100,100, size=(n,n))
        #field = np.random.randint(-100,100,size=(300,300))
        ii = np.cumsum(field, axis=0)
        ii = np.cumsum(ii, axis=1)

        @njit
        def find_max(ii):
            maxval = -100*300*300
            for x1 in prange(1,field.shape[0]):
                for y1 in range(1,field.shape[1]):
                    for x2 in range(x1,field.shape[0]):
                        for y2 in range(y1,field.shape[1]):
                            val = ii[x1-1,y1-1] + ii[x2,y2] - ii[x1-1,y2] - ii[x2, y1-1]
                            if val > maxval:
                                maxval = val
            return maxval

        maxval = find_max(ii)
        input_str = f"{n}\n"+' '.join(str(v) for v in np.ravel(field[1:,1:]))+"\n"
        output_str = f"{maxval}\n"

        return input_str, output_str



    @staticmethod
    def special_instances():
        yield "3\n-1 4 -1 -2 1 2 -2 -1 -3", "6\n"


if __name__ == '__main__':
    Oil.get_random_instance()
