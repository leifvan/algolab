from random import randint


class KMeans1:
    @staticmethod
    def get_random_instance():
        n = randint(1,10000)
        points = [(randint(-10000,10000), randint(-10000,10000)) for _ in range(n)]
        squares = [x**2 + y**2 for x,y in points]
        # roots = [sp.sqrt(x+y) for x,y in squares]
        # length_sum = sum(roots)
        str_in = f"{n}\n"+'\n'.join(f"{x} {y}" for x,y in points)
        str_out = f"{sum(squares):.30f}\n"
        return str_in, str_out

    @staticmethod
    def special_instances():
        yield "4\n1 1\n1 -1\n-1 1\n-1 -1", "8."+"0"*30+"\n"
