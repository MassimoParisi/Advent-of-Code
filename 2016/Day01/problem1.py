with open("input.txt") as f:
    inp = f.read()

inp = inp.split(", ")
x, y = 0, 0
i = 0                   #["N", "E", "S", "W"]

for el in inp:
    turn = el[0]
    step = int(el[1:])
    if turn == "R": i += 1
    else: i -= 1
    i %= 4
    if i == 0: y -= step
    elif i == 1: x += step
    elif i == 2: y += step
    else: x -= step
result = abs(x) + abs(y)
print(f"Result is: {result}")
