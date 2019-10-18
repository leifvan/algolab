from random import randint


class TestGenerator:
    @staticmethod
    def get_random_instance():
        n = randint(0,99)
        return f"test no\n{n}", f"test\n{n}\n"

    @staticmethod
    def special_instances():
        yield ("First\ntest instance", "test\n1\n")
        yield ("Second\ntest instance", "test\n2\n")