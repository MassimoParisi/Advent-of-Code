from math import ceil

pattern = [0,1,0,-1]

with open("input.txt") as f:
    inp = f.read()[:-1]

inp = [int(x) for x in inp]

n = len(inp)
for _ in range(100):
    for i in range(1,n+1):
        curr = []
        pat = []
        for p in pattern:
            pat.extend([p]*i)

        m = len(pat)
        div = ceil(n/m) + 1
        pat *= div
        pat.pop(0)

        tmp = 0
        for j in range(n):
            tmp += inp[j] * pat[j]
        curr.append(tmp%10)
    print(curr)
    inp = curr.copy()

print(inp)


