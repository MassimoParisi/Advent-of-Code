from collections import deque

with open("input.txt") as f:
    inp = [int(x) for x in f.readline()[:-1].split(',')]

n = len(inp)
new_fish = 0

inp = deque([inp.count(x) for x in range(9)])

for _ in range(256):
    new_fish = inp[0]
    inp.rotate(-1)
    inp[6]