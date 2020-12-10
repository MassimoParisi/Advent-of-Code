with open("input.txt") as f:
    inp = f.read().strip()

result = 0
for i, dig in enumerate(inp):
    if int(dig) == int(inp[(i + len(inp)//2) % len(inp)]):
        result += int(dig)
print(result)
