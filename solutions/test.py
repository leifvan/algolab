import sys

lines = [l.strip() for l in sys.stdin]

if lines[0] == "First":
    n = 1
elif lines[0] == "Second":
    n = 2
else:
    n = int(lines[1])

print("test\n"+str(n))
