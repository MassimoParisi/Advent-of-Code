import re

lights = dict()

with open("input.txt") as f:
    for line in f.readlines():
        tmp = re.match(r"([a-z ]+) (\d+),(\d+) through (\d+),(\d+)", line)
        istr = tmp.group(1)
        x1, y1 = int(tmp.group(2)), int(tmp.group(3))
        x2, y2 = int(tmp.group(4)), int(tmp.group(5))

        if istr == "turn on":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in lights.keys():
                        lights[(x, y)] += 1
                    else:
                        lights[(x, y)] = 1
        elif istr == "turn off":
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in lights.keys():
                        if lights[(x, y)] == 1:
                            lights.pop((x, y))
                        else:
                            lights[(x, y)] -= 1
        else:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if (x, y) in lights.keys():
                        lights[(x, y)] += 2
                    else:
                        lights[(x, y)] = 2

result = sum(lights.values())
print(f"Result is: {result}")
