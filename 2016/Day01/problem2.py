with open("input.txt") as f:
    inp = f.read()

inp = inp.split(", ")
x, y = 0, 0
i = 0                   #["N", "E", "S", "W"]

visited = set()
flag = False
for el in inp:
    turn = el[0]
    step = int(el[1:])
    if turn == "R": i += 1
    else: i -= 1
    i %= 4
    if i == 0:
        for _ in range(step):
            y -= 1
            if (x, y) in visited:
                flag = True
                break
            else: visited.add((x, y))
    elif i == 1:
        for _ in range(step):
            x += 1
            if (x, y) in visited:
                flag = True
                break
            else: visited.add((x, y))
    elif i == 2:
        for _ in range(step):
            y += 1
            if (x, y) in visited:
                flag = True
                break
            else: visited.add((x, y))
    else:
        for _ in range(step):
            x -= 1
            if (x, y) in visited:
                flag = True
                break
            else: visited.add((x, y))
    if flag: break
result = abs(x) + abs(y)
print(f"Result is: {result}")
