with open("input.txt") as f:
    inp = f.read()
floor = 0
for i in range(len(inp)):
    if inp[i] == "(": floor += 1
    else: floor -= 1
    if floor == -1:
        print(f"Result is: {i+1}")
        break