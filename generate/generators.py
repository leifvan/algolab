# import all generators
generators = dict()

from generate.test.test import TestGenerator
generators['test'] = {'test': TestGenerator}

from generate.sheet1.gridsnap import GridSnap
generators['sheet1'] = {'gridsnap': GridSnap}
