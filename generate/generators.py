# import all generators
generators = dict()

from generate.test.test import TestGenerator
generators['test'] = {'test': TestGenerator}

# sheet 1

from generate.sheet1.gridsnap import GridSnap
generators['sheet1'] = {'gridsnap': GridSnap}

from generate.sheet1.kmeans1 import KMeans1
generators['sheet1'] = {'kmeans1': KMeans1}

from generate.sheet1.areapoly import AreaPoly
generators['sheet1'] = {'areapoly': AreaPoly}
