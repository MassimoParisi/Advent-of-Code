with open("input.txt") as f:
    wire1 = f.readline()
    wire2 = f.readline()

wire1 = wire1.split(",")
wire2 = wire2.split(",")

firstSet = set()
interSet = set()
steps = dict()

x = 0
y = 0
t = 0

for el in wire1:
    if el[0] == 'U':
        for _ in range(0, int(el[1:])):
            y += 1
            t += 1
            firstSet.add((x, y))
            steps.update({(x,y): t})
    elif el[0] == 'D':
        for _ in range(0, int(el[1:])):
            y -= 1
            t += 1
            firstSet.add((x, y))
            steps.update({(x,y): t})
    elif el[0] == 'R':
        for _ in range(0, int(el[1:])):
            x += 1
            t += 1
            firstSet.add((x, y))
            steps.update({(x,y): t})
    else:  # left (L) case
        for _ in range(0, int(el[1:])):
            x -= 1
            t += 1
            firstSet.add((x, y))
            steps.update({(x,y): t})


x = 0
y = 0
t = 0
for el in wire2:
    if el[0] == 'U':
        for _ in range(0, int(el[1:])):
            y += 1
            t += 1
            if((x,y) in steps):
                time = t + steps.get((x,y))
                interSet.add(time)
    elif el[0] == 'D':
        for _ in range(0, int(el[1:])):
            y -= 1
            t += 1
            if((x, y) in steps):
                time = t + steps.get((x,y))
                interSet.add(time)
    elif el[0] == 'R':
        for _ in range(0, int(el[1:])):
            x += 1
            t += 1
            if((x, y) in steps):
                time = t + steps.get((x,y))
                interSet.add(time)
    else:  # left (L) case
        for _ in range(0, int(el[1:])):
            x -= 1
            t += 1
            if((x, y) in steps):
                time = t + steps.get((x,y))
                interSet.add(time)


result = min(interSet)
print(f"Result is: {result}")

