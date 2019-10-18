import sys
from collections import defaultdict

# parse

lines = [l.strip() for l in sys.stdin]
n = int(lines[0])
m = int(lines[1])
mat_tuples =[tuple(int(v) for v in l.split()) for l in lines[2:2+m]]
b = int(lines[m+2])
vec_tuples = [tuple(int(v) for v in l.split()) for l in lines[m+3:m+b+3]]

# make a dict for vec and result
vec_dict = {int(i): int(v) for i,v in vec_tuples}
res_dict = defaultdict(int)

for i,j,v in mat_tuples:
    if j in vec_dict:
        res_dict[i] += vec_dict[j]*v


# output
print('\n'.join("{} {}".format(i, res_dict[i]) for i in sorted(res_dict) if res_dict[i] != 0))
