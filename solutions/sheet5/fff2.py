from itertools import product
import sys

lines = [[int(v) for v in line.split()] for line in sys.stdin]
n, m = lines[0]
edges = lines[1:]
k = 6


def py(n, edges):
    # find maximal matching
    matching = []
    edges_set = [set(e) for e in edges]
    edges_copy = [set(e) for e in edges]

    while len(edges_copy) > 0:
        edge = edges_copy.pop()
        matching.append(edge)
        edges_copy = [e for e in edges_copy if e.isdisjoint(edge)]

    if len(matching) > k:
        return False

    if 2 * len(matching) < k:
        return True

    matching_ordered = [list(m) for m in matching]

    # go through subsets of u by either choosing one or two nodes for every edge in the matching
    # choices has len(matching) with 0=choose first, 1=choose second, 2=choose both for every matching edge
    for choices in product([0, 1, 2], repeat=len(matching)):
        cover_vertices = set()
        for m, choice in zip(matching_ordered, choices):
            if choice == 2:
                cover_vertices.update(m)
            else:
                cover_vertices.add(m[choice])

        v_without_u = set(range(n)).difference(cover_vertices)
        v_wo_u_edge_dict = {v: [e for e in edges_set if v in e] for v in v_without_u}
        v_wo_u_incidence_dict = {v: [e1 if e2 == v else e2 for e1, e2 in vedges] for v, vedges in
                                 v_wo_u_edge_dict.items()}

        # check all vertices in V - U and add if they are not adjacent to a node in cover_vertices
        for v in v_without_u:
            if any(w not in cover_vertices for w in v_wo_u_incidence_dict[v]):
                cover_vertices.add(v)

        if len(cover_vertices) <= k:
            return True

    return False


print("possible" if py(n, edges) else "impossible")
