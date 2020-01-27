import numpy as np
import networkx as nx
from random import randint, random, choice, choices
from collections import defaultdict
from itertools import combinations
from operator import itemgetter

from sklearn.cluster import AgglomerativeClustering


class Islands:
    @staticmethod
    def get_random_instance():
        while True:
            try:
                return Islands.make_instance()
            except nx.NetworkXPointlessConcept:
                pass


    @staticmethod
    def make_instance():
        n = randint(3, 100)
        k = randint(2, n)

        g = nx.connected_watts_strogatz_graph(n, min(n, randint(1, 10)), p=0.1 + random()*0.8)
        dist_mat = np.ones(shape=(n, n), dtype=np.int) * 1000000
        np.fill_diagonal(dist_mat, 0)

        for i, j in g.edges():
            g[i][j]['weight'] = randint(1, 10)

        for s, target_dict in nx.shortest_path_length(g, weight="weight"):
            for t, val in target_dict.items():
                dist_mat[s, t] = dist_mat[t, s] = val

        ac = AgglomerativeClustering(n_clusters=k,
                                     affinity='precomputed',
                                     linkage='single').fit(dist_mat)

        labels_dict = defaultdict(list)

        for i, label in enumerate(ac.labels_):
            labels_dict[label].append(i)

        icd = np.ones(shape=(k, k)) * np.inf
        for ki, kj in combinations(range(k), 2):
            all_dists = [dist_mat[pi, pj] for pi in labels_dict[ki] for pj in labels_dict[kj]]
            min_dist = min(all_dists)
            icd[ki, kj] = icd[kj, ki] = min_dist

        result = icd.min()

        str_in = '\n'.join(str(v) for v in [n, k, len(g.edges())]) + '\n'
        str_in += '\n'.join(f"{i} {j} {g[i][j]['weight']}" for i, j in g.edges())

        str_out = str(int(result))

        return str_in, str_out

    @staticmethod
    def special_instances():
        yield "10\n2\n12\n0 1 1\n0 4 5\n1 2 1\n2 3 1\n3 4 1\n4 5 1\n5 6 1\n6 7 1\n7 8 2\n8 9 1\n1 3 6\n6 9 4", "2"

    @staticmethod
    def validate_output(given_out, correct_out):
        return given_out.replace('\n', '') == correct_out.replace('\n', '')
