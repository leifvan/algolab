import numpy as np
from itertools import product, chain
from random import randint, random, choice, choices


class FFF2:
    @staticmethod
    def get_random_instance():
        n = randint(6, 100)
        m = min(randint(10, 100), n*(n-1)//2)

        edges = set()
        looperz = 0

        # force a vertex cover <= 6
        cover_vertices = choices(range(n), k=6)
        while len(edges) < m and looperz < 10*m:
            v = choice(cover_vertices)
            w = randint(0, n-1)

            v, w = min(v,w), max(v,w)
            if v != w and (v,w) not in edges:
                edges.add((v,w))

            looperz += 1

        # randomly flip some edges
        edges = [(v,w) if random() < 0.5 else (w,v) for v,w in edges]

        str_in = f"{n} {m}\n"+'\n'.join(f"{v} {w}" for v,w in edges)
        str_out = "possible"

        return str_in, str_out


    @staticmethod
    def special_instances():
        yield make_ring_instance(7)
        yield "1 0", "possible"
        yield "100000 0", "possible"
        yield "0 0", "possible"
        yield make_ring_instance(13)

    @staticmethod
    def validate_output(given_out, correct_out):
        return given_out.replace('\n', '') == correct_out.replace('\n', '')


def make_ring_instance(n):
    str_in = f"{n} {n}\n"+'\n'.join(f"{a} {b}" for a,b in zip(range(n), chain(range(1,n), [0])))
    str_out = "possible" if n < 13 else "impossible"
    return str_in, str_out


"""
Papadimitriou and Yannakakis
----------------------------
Step 1: Find a maximal matching in the graph. Let the
size of the matching (the number of edges) be m.
If m > k answer “NO”. If 2m < k, then answer
“YES”. The 2m vertices form a vertex cover.

Step 2: Let U be the set of the endpoints of the m
edges of the maximal matching. For every edge of
the matching, either one of the endpoints or both
are in any vertex cover of G. Furthermore, once a
subset of U is picked in a vertex cover, the rest
of the vertex cover is uniquely determined: for
every vertex in V - U, it is included in the vertex
cover if and only if there is an edge incident with
it whose other endpoint (which is in U) has not
been picked in the vertex cover. So, cycle through
the 3^m subsets of U (by picking either one or both
of the endpoints of each edge in the matching) and
check, for each subset whether it along with its
unique extension to V is of size at most k. If it is
so for any subset, answer “YES”, otherwise answer
“NO”.
"""