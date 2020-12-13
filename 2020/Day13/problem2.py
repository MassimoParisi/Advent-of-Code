import math

with open("input.txt") as f:
    f.readline()
    inp = [int(el) if el != "x" else "x" for el in f.readline().split(",")]

lcm = inp[0]
t = 0
i = 1
while i < len(inp):
    if inp[i] == "x":
        i += 1
        continue
    j = 0
    while ((lcm*j+t) + i) % inp[i] != 0:
        j += 1
    t = lcm*j + t
    lcm = (lcm * inp[i]) // math.gcd(lcm, inp[i])
    i += 1

print(t)
