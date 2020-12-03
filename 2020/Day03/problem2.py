import functools

def countTree(shiftX: int, shiftY: int) -> int:
    x = 0
    y = 0
    counter = 0

    with open("input.txt") as f:
        for line in f:
            if y % shiftY == 0:
                if x >= len(line.strip()):
                    x -= (len(line.strip()))
                if line[x] == '#':
                    counter += 1
                x += shiftX
            y += 1

    print(counter)
    return counter


patterns = [[1, 1], [3, 1], [5, 1], [7, 1],[1, 2]]          # list of pattern used
counters = []
for p in patterns:
    counters.append(countTree(p[0], p[1]))

result = functools.reduce(lambda x, y: x*y, counters)
print(f"Result is: {result}")

