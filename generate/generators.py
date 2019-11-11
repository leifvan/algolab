import os, inspect, importlib
from collections import defaultdict

# import all generators
generators = defaultdict(dict)


def get_generator_class_from_module(mod, fname):
    for name, data in inspect.getmembers(mod):
        if name.lower() == fname.lower():
            return data
    raise AttributeError(f"Module '{mod.__name__}' does not contain a class corresponding to the file name '{fname}'.")


base = os.path.dirname(__file__)

for dirp in os.listdir(base):
    base_dirp = os.path.join(base,dirp)
    if os.path.isdir(base_dirp) and not dirp.startswith('__'):
        for fp in os.listdir(base_dirp):
            if fp.endswith('.py'):
                name = fp[:-3]
                mod = importlib.import_module(f"generate.{dirp}.{name}")
                generators[dirp][name] = get_generator_class_from_module(mod, name)


class ProblemGenerator:
    @staticmethod
    def get_random_instance():
        raise NotImplementedError

    @staticmethod
    def special_instances():
        raise NotImplementedError