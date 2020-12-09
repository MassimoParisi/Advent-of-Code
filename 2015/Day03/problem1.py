with open("input.txt") as f:
    inp = f.read()

visited = set()
visited.add((0, 0))

x, y = 0, 0

for dir in inp:
    if dir == "^":
        y += 1
    elif dir == ">":
        x += 1
    elif dir == "v":
        y -= 1
    else:
        x -= 1
    visited.add((x, y))

result = len(visited)
print(f"Result is: {result}")
