# import all generators
generators = dict()

from generate.test.test import TestGenerator
generators['test'] = {'test': TestGenerator}

# sheet 1

# TODO automate this
from generate.sheet1.gridsnap import GridSnap
from generate.sheet1.kmeans1 import KMeans1
from generate.sheet1.areapoly import AreaPoly
from generate.sheet1.matrixmul import MatrixMul

generators['sheet1'] = {'gridsnap': GridSnap,
                        'kmeans1': KMeans1,
                        'areapoly': AreaPoly,
                        'matrixmul': MatrixMul}


