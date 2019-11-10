import numpy as np
from networkx import DiGraph, shortest_path


class THunt:
    @staticmethod
    def get_random_instance():
        n, m = np.random.randint(1, 1000, size=2)
        field = np.random.randint(0, 100, size=(n, m))

        # solution
        g = DiGraph()
        for (i, j), v in np.ndenumerate(field):
            if i > 0:
                g.add_edge((i - 1, j), (i, j), weight=-v)
            if j > 0:
                g.add_edge((i, j-1), (i, j), weight=-v)

        sp = shortest_path(g, (0,0), (n-1,m-1), weight="weight", method="bellman-ford")
        path_weight = sum(g[i][j]['weight'] for i,j in zip(sp, sp[1:]))
        path_weight -= field[0,0]
        path_weight *= -1

        input_str = f"{n}\n{m}\n"
        input_str += '\n'.join(' '.join(str(v) for v in row) for row in field)
        output_str = f"{path_weight}\n"

        return input_str, output_str

    @staticmethod
    def special_instances():
        yield "3\n4\n1 12 22 5\n0 0 6 0\n1 8 0 1", "42\n"


if __name__ == '__main__':
    THunt.get_random_instance()
