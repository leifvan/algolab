import numpy as np
from numba import njit, prange
from random import randint


@njit(parallel=True)
def get_count(field, r):
    counts = np.zeros(r).astype(np.int32)
    for i1 in prange(r):
        for i2 in range(i1+1, r):
            for j1 in range(r):
                for j2 in range(j1+1, r):
                    if field[i1,j1] == 1 and field[i1,j2] == 1 and field[i2,j1] == 1 and field[i2,j2] == 1:
                        counts[i1] += 1
    return counts.sum()


class Fields:
    @staticmethod
    def get_random_instance():

        r = randint(2,500)
        field = np.random.randint(0,2,size=(r,r))
        print("start countin' a whopping",r,"field")
        count = get_count(field, r)
        print("finished countin' the",count,"possibilities")

        input_str = str(r)
        for row in field:
            input_str += '\n' + ''.join(str(v) for v in row)

        output_str = str(count) + '\n'
        return input_str, output_str



    @staticmethod
    def special_instances():
        yield "3\n111\n110\n011","2\n"
