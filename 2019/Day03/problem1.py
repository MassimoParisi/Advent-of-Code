with open("input.txt") as f:
    wire1 = f.readline()
    wire2 = f.readline()

wire1 = wire1.split(",")
wire2 = wire2.split(",")

firstSet = set()
interSet = set()

x = 0
y = 0
for el in wire1:
    if el[0] == 'U':
        for _ in range(0, int(el[1:])):
            y += 1
            firstSet.add((x, y))
    elif el[0] == 'D':
        for _ in range(0, int(el[1:])):
            y -= 1
            firstSet.add((x, y))
    elif el[0] == 'R':
        for _ in range(0, int(el[1:])):
            x += 1
            firstSet.add((x, y))
    else:  # left (L) case
        for _ in range(0, int(el[1:])):
            x -= 1
            firstSet.add((x, y))

x = 0
y = 0
for el in wire2:
    if el[0] == 'U':
        for _ in range(0, int(el[1:])):
            y += 1
            if((x, y) in firstSet):
                interSet.add((x, y))
    elif el[0] == 'D':
        for _ in range(0, int(el[1:])):
            y -= 1
            if((x, y) in firstSet):
                interSet.add((x, y))
    elif el[0] == 'R':
        for _ in range(0, int(el[1:])):
            x += 1
            if((x, y) in firstSet):
                interSet.add((x, y))
    else:  # left (L) case
        for _ in range(0, int(el[1:])):
            x -= 1
            if((x, y) in firstSet):
                interSet.add((x, y))


#print(firstSet)

gaps = list(map(lambda g: abs(g[0])+abs(g[1]), interSet))
#print(gaps)
minDist = min(gaps)


print(f"Result is: {minDist}")


