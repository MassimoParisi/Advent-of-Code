twins = 0
triplets = 0

with open("input.txt") as f:
    for line in f.readlines():
        found2 = False
        found3 = False
        for char in set(line):
            if line.count(char) == 2:
                found2 = True
            elif line.count(char) == 3:
                found3 = True
        if found2: twins += 1
        if found3: triplets += 1
result = twins * triplets
print(f"Result is: {result}")
