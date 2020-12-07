import functools

def count_tree(shift_X: int, shift_Y: int) -> int:
    x = 0
    y = 0
    counter = 0

    with open("input.txt") as f:
        for line in f:
            if y % shift_Y == 0:
                if x >= len(line.strip()):
                    x -= (len(line.strip()))
                if line[x] == '#':
                    counter += 1
                x += shift_X
            y += 1
    
    return counter


patterns = [[1, 1], [3, 1], [5, 1], [7, 1],[1, 2]]          # list of pattern used
counters = []
for p in patterns:
    counters.append(count_tree(p[0], p[1]))

result = functools.reduce(lambda x, y: x * y, counters)
print(f"Result is: {result}")

