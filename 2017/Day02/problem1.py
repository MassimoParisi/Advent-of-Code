result = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip().split("\t")
        for i, num in enumerate(line):
            line[i] = int(num)
        result += int(max(line)) - int(min(line))

print(result)
