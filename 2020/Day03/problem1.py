x = 0
result = 0

with open("input.txt") as f:
    for line in f:
        if x >= len(line.strip()):
            x = x - (len(line.strip()))
        if line[x] == '#':
            result += 1
        x += 3

print(f"Result is: {result}")
