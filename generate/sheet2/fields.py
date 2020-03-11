import numpy as np
from numba import njit, prange
from random import randint
from math import ceil, sqrt
from itertools import combinations, permutations
from tqdm import tqdm
from time import time


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


def check_rect(i1,i2,i3,i4,j1,j2,j3,j4):
    return i1 == i2 and i3 == i4 and i1 != i3 and j1 == j3 and j2 == j4 and j1 != j2


def get_inverse_count(field, r):
    n = (0.5 * (r - 1) * r)**2

    nztime = time()
    ri = np.nonzero(1 - field.T)
    print("nonzero took", time()-nztime)

    base = (r-1)**2
    common = 0
    if len(ri[0]) == 1:
        pr = base
    else:
        for (i1, i2), (j1, j2) in zip(combinations(ri[0],2), combinations(ri[1],2)):
            if i1 == i2 or j1 == j2:
                common = common + r-1
            else:
                common = common + 1

        for (i1, i2, i3), (j1, j2, j3) in zip(combinations(ri[0],3), combinations(ri[1],3)):
            if (i1 == i2 and i2 == i3 and i1 == i3) or (j1 == j2 and j2 == j3 and j1 == j3):
                ... # in one line, do nothing
            else:
                if i1 == i2 and (j1 == j3 or j2 == j3):
                    common = common - 1
                elif i2 == i3 and (j1 == j3 or j2 == j3):
                    common = common - 1
                elif j1 == j2 and (i1 == i3 or i2 == i3):
                    common = common - 1
                elif j2 == j3 and (i1 == i3 or i2 == i3):
                    common = common - 1

        for (i1, i2, i3, i4), (j1, j2, j3,j4) in zip(combinations(ri[0],4), combinations(ri[1],4)):
            if (check_rect(i1,i2,i3,i4,j1,j2,j3,j4) or check_rect(i1,i3,i2,i4,j1,j3,j2,j4) or
                check_rect(i1,i4,i2,i3,j1,j4,j2,j3) or check_rect(i2,i3,i1,i4,j2,j3,j1,j4) or
                check_rect(i2,i4,i1,i3,j2,j4,j1,j3) or check_rect(i3,i4,i1,i2,j3,j4,j1,j2)):

                common = common + 1

        # for (i1, i2, i3, i4), (j1, j2, j3,j4) in zip(combinations(ri[0],4), combinations(ri[1],4)):
        #     if i1 == i2 or j1 == j2:
        #         common += r-1
        #     else:
        #         common += 1
        #
        #     if not ((i1 == i2 and i2 == i3 and i1 == i3) or (j1 == j2 and j2 == j3 and j1 == j3)):
        #         if i1 == i2 and (j1 == j3 or j2 == j3):
        #             common -= 1 # they form a rectangle
        #         elif i2 == i3 and (j1 == j3 or j2 == j3):
        #             common -= 1 # again they form a rectangle
        #         elif j1 == j2 and (i1 == i3 or i2 == i3):
        #             common -= 1  # they form a rectangle
        #         elif j2 == j3 and (i1 == i3 or i2 == i3):
        #             common -= 1  # again they form a rectangle
        #
        #     if (check_rect(i1,i2,i3,i4,j1,j2,j3,j4) or check_rect(i1,i3,i2,i4,j1,j3,j2,j4) or
        #         check_rect(i1,i4,i2,i3,j1,j4,j2,j3) or check_rect(i2,i3,i1,i4,j2,j3,j1,j4) or
        #         check_rect(i2,i4,i1,i3,j2,j4,j1,j3) or check_rect(i3,i4,i1,i2,j3,j4,j1,j2)):
        #         common += 1

        pr = (len(ri[0])*base-common)

    return n-pr


class Fields:
    @staticmethod
    def get_random_instance():

        r = randint(2,200)
        field = np.random.randint(0,2,size=(r,r))
        #print("start countin' a whopping",r,"field")
        count = get_count(field, r)
        #print("finished countin' the",count,"possibilities")

        input_str = str(r)
        for row in field:
            input_str += '\n' + ''.join(str(v) for v in row)

        output_str = str(count) + '\n'
        return input_str, output_str



    @staticmethod
    def special_instances():
        yield "3\n111\n110\n011","2\n"
        yield "2000\n"+("1"*2000+'\n')*2000, str((0.5 * (2000 - 1) * 2000) ** 2)+"\n"

    @staticmethod
    def validate_output(given_out, correct_out):
        return given_out.replace('\n', '') == correct_out.replace('\n', '')


if __name__ == '__main__':
    for _ in range(10):
        r = 400
        n = (0.5 * (r - 1) * r) ** 2
        field = np.random.randint(0, 2, size=(r, r))
        # field = np.ones((r,r))
        # ri = np.sort(np.random.choice(r * r, size=ceil(sqrt(r)), replace=False))
        # ri = np.unravel_index(ri, shape=field.shape)
        #field[ri] = 0

        print("better get countin'")
        stime = time()
        if np.count_nonzero(field) < r:
            print("invertverdertently")
            ci = get_inverse_count(field, r)
        else:
            print("good ol' time")
            c = get_count(field, r)
        #assert c == ci
        print(time() -stime)

        #print("most",n,"count",c,"inv",ci)

    # n = 0
    # for r in range(1,20):
    #     n = 0.5*(r-1)*r
    #     field = np.ones((r,r))
    #     c = get_count(field,r)
    #     print(f"r = {r:>3} |",c, np.sqrt(c),n)
    #
    #     for i in range(1,r):
    #         print('     -> remove',i)
    #         res = np.zeros(10)
    #         pred = np.zeros(10)
    #         for j in range(10):
    #             ri = np.sort(np.random.choice(r*r, size=i, replace=False))
    #             ri = np.unravel_index(ri, shape=field.shape)
    #
    #             base = (r-1)**2
    #             common = 0
    #             if len(ri) == 1:
    #                 pr = base
    #             else:
    #                 # assume indices are sorted column-major
    #                 for (i1, i2), (j1, j2) in zip(combinations(ri[0],2), combinations(ri[1],2)):
    #                     if i1 == i2 or j1 == j2:
    #                         common += r-1
    #                     else:
    #                         common += 1
    #
    #                 for (i1, i2, i3), (j1, j2, j3) in zip(combinations(ri[0],3), combinations(ri[1],3)):
    #                     #print(i1,i2,i3,'|',j1,j2,j3)
    #                     if (i1 == i2 and i2 == i3 and i1 == i3) or (j1 == j2 and j2 == j3 and j1 == j3):
    #                         ... # in one line, do nothing
    #                     else:
    #                         if i1 == i2 and (j1 == j3 or j2 == j3):
    #                             #print("c1")
    #                             common -= 1 # they form a rectangle
    #                         elif i2 == i3 and (j1 == j3 or j2 == j3):
    #                             #print("c2")
    #                             common -= 1 # again they form a rectangle
    #                         # elif i1 == i3 and (j1 == j2 or j2 == j3):
    #                         #     print("c3")
    #                         #     common -= 1
    #                         elif j1 == j2 and (i1 == i3 or i2 == i3):
    #                             #print("d1")
    #                             common -= 1  # they form a rectangle
    #                         elif j2 == j3 and (i1 == i3 or i2 == i3):
    #                             #print("d2")
    #                             common -= 1  # again they form a rectangle
    #                         # elif j1 == j3 and (i1 == i2 or i2 == i3):
    #                         #     print("d3")
    #                         #     common -= 1
    #
    #                 for (i1, i2, i3, i4), (j1, j2, j3,j4) in zip(combinations(ri[0],4), combinations(ri[1],4)):
    #                     if (check_rect(i1,i2,i3,i4,j1,j2,j3,j4) or check_rect(i1,i3,i2,i4,j1,j3,j2,j4) or
    #                         check_rect(i1,i4,i2,i3,j1,j4,j2,j3) or check_rect(i2,i3,i1,i4,j2,j3,j1,j4) or
    #                         check_rect(i2,i4,i1,i3,j2,j4,j1,j3) or check_rect(i3,i4,i1,i2,j3,j4,j1,j2)):
    #
    #                         common += 1
    #
    #             field[ri] = 0
    #             res[j] = get_count(field, r)
    #             pred[j] = (i*base-common)
    #             field[ri] = 1
    #         print('     -> got',c-res-pred)#,"?=",pred)
    #
    #     # field[0,0] = 0
    #     # cu = get_count(field, r)
    #     # base = (r-1)**2
    #     # for j in range(0,r):
    #     #     for i in range(1, ceil(r / 2)):
    #     #         field[i,j] = 0
    #     #         cm = get_count(field, r)
    #     #         field[i,j] = 1
    #     #
    #     #         if i == 0 or j == 0:
    #     #             pr = r-1
    #     #         else:
    #     #             pr = 1
    #     #
    #     #         print(f" - ({i},{j}) |",c-cu,"?=",base,"|",c-cm,"?=",2*base-pr)