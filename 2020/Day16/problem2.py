import re
from collections import defaultdict

fields = dict()
with open("input.txt") as f:
    parts = f.read().split("\n\n")

for line in parts[0].split("\n"):
    tmp = re.match(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
    name = tmp.group(1)
    range1 = (int(tmp.group(2)), int(tmp.group(3)))
    range2 = (int(tmp.group(4)), int(tmp.group(5)))
    fields[name] = (range1, range2)

valid = []

for line in parts[2].split("\n"):
    if line == "nearby tickets:" or line == "": continue
    values = [int(x) for x in line.split(",")]
    valid.append(values)
    for v in values:
        good = False
        for f in fields.values():
            if f[0][0] <= v <= f[0][1] or f[1][0] <= v <= f[1][1]:
                good = True
                break
        if not good:
            valid.pop()
            break

order = defaultdict(list)
merge = list(zip(*valid))
num_field = len(fields)
for f in fields.keys():
    for i in range(num_field):
        if all([fields[f][0][0] <= x <= fields[f][0][1] or fields[f][1][0] <= x <= fields[f][1][1] for x in merge[i]]):
            order[f].append(i)

final = dict()
change = True
while change:
    change = False
    for o in order.keys():
        if len(order[o]) == 1:
            change = True
            idx = order[o][0]
            final[o] = idx
            for o2 in order.keys():
                if idx in order[o2]:
                    order[o2].remove(idx)

ticket = [int(x) for x in parts[1].split("\n")[1].split(",")]
res = 1
for f in final.keys():
    if "departure" in f:
        res *= ticket[final[f]]
print(f"Result is: {res}")
