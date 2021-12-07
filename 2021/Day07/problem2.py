with open("input.txt") as f:
    inp = [int(x) for x in f.readline()[:-1].split(',')]

def sumVal(x):
    return sum(range(x+1))

def computeFunc(x):
    return sum([sumVal(abs(y-x)) for y in inp])

res = float('inf')

l,r = min(inp), max(inp)

for i in range(l,r+1):
    curr = computeFunc(i)
    if curr < res:
        res = curr
print(res)
