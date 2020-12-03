
x = 0
counter = 0

with open("input.txt") as f:
    for line in f:
        if x >= len(line.strip()): x = x - (len(line.strip()))
        if line[x] == '#' : counter += 1
        x += 3

print(counter)