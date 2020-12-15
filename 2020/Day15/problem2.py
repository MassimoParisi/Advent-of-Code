from collections import defaultdict
age = dict()

with open("input.txt") as f:
    inp = [int(x) for x in f.read().split(",")]

curr = inp.pop()     
for i in range(len(inp)):
    age[inp[i]] = i

counter = len(inp)
step = 30000000 - 1
while counter < step:
    if curr in age.keys():
        tmp = counter - age[curr]
    else: tmp = 0
    age[curr] = counter
    curr = tmp
    counter += 1
print(tmp)