with open("input.txt") as f:
    inp = [int(x) for x in f.readline()[:-1].split(',')]

def computeFunc(x):
    return sum([abs(y-x) for y in inp])

res = float('inf')

l,r = min(inp), max(inp)

for i in range(l,r+1):
    curr = computeFunc(i)
    if curr < res:
        res = curr
print(res)
