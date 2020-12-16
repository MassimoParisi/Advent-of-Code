import re

fields = dict()
with open("input.txt") as f:
    parts = f.read().split("\n\n")

for line in parts[0].split("\n"):
    tmp = re.match(r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", line)
    name = tmp.group(1)
    range1 = (int(tmp.group(2)), int(tmp.group(3)))
    range2 = (int(tmp.group(4)), int(tmp.group(5)))
    fields[name] = (range1, range2)

res = 0
for line in parts[2].split("\n"):
    if line == "nearby tickets:" or line == "": continue
    values = [int(x) for x in line.split(",")]
    for v in values:
        good = False
        for f in fields.values():
            if f[0][0] <= v <= f[0][1] or f[1][0] <= v <= f[1][1]:
                good = True
                break
        if not good: res += v

print(f"Result is: {res}")
