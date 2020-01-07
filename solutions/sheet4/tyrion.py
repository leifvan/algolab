import sys

n = int(sys.stdin.readline())

DEBUG = False


queries = []
names = {}


def print_queries():
    for q in queries:
        print(q)
    print("-----")


for i in range(n):
    line = sys.stdin.readline().split()
    query = 0
    for person in line[:-1]:
        if not person in names:
            names[person] = len(names)
        query |= 1 << names[person]
    val = (line[-1] == "odd")
    queries.append([query, val])

if DEBUG: print_queries()


position = 1 << n
for i in range(n):
    position >>= 1
    j = i
    while not queries[j][0] & position and j < n-1:
        j += 1
    queries[i], queries[j] = queries[j], queries[i]
    query, val = queries[i]
    for j in range(i + 1, n):
        q, v = queries[j]
        if q & position:
            queries[j] = [query ^ q, val ^ v]

if DEBUG: print_queries()

friends = 0
for i in range(n - 1, -1, -1):
    query, val = queries[i]
    friends += val
    for j in range(i):
        q, v = queries[j]
        if q & position:
            queries[j][1] = val ^ v
    position <<= 1

if DEBUG: print_queries()

print(friends)
