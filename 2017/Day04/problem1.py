result = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.split()
        if len(line) == len(set(line)):
            result += 1
print(result)
