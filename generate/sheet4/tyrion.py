from random import sample, randint

class Tyrion:
    @staticmethod
    def get_random_instance():
        n = randint(4,20)
        houses = [f"house{i}" for i in range(n)]
        is_friend = {h: randint(0,1) for h in houses}
        friends = sum(is_friend.values())

        blocks = [sample(houses, randint(2,min(2+i,n))) for i in range(n)]
        block_parities = [sum(is_friend[h] for h in block) % 2 for block in blocks]

        str_in = f"{n}\n"
        str_in += '\n'.join(' '.join(block) + (' even' if parity == 0 else ' odd')
                            for block, parity in zip(blocks, block_parities))

        str_out = f"{friends}"
        return str_in, str_out


    @staticmethod
    def special_instances():
        yield "4\nBaratheon Lannet Stark Targaryan odd\nBaratheon Lannet Targaryan odd\nBaratheon Stark Targaryan even\nStark Targaryan even","1"

    @staticmethod
    def validate_output(given_out, correct_out):
        return given_out.replace('\n','') == correct_out.replace('\n','')
