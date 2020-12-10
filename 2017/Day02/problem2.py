result = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip().split("\t")
        for i, num in enumerate(line):
            line[i] = int(num)
        line.sort(reverse=True)
        found = False
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                if line[i] % line[j] == 0:
                    result += line[i] // line[j]
                    found = True
                    break
            if found: break

print(result)
