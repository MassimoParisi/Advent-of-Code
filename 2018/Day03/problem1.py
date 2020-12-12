import re

used = set()
overlap = set()
pattern = r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)"

with open("input.txt") as f:
    for line in f.readlines():
        tmp = re.match(pattern, line)
        id = int(tmp.group(1))
        x0 = int(tmp.group(2))
        y0 = int(tmp.group(3))
        wide = int(tmp.group(4))
        tall = int(tmp.group(5))
        for i in range(x0, x0 + wide):
            for j in range(y0, y0 + tall):
                if (i,j) in used:
                    overlap.add((i,j))
                else:
                    used.add((i,j))
result = len(overlap)
print(f"Result is: {result}")

