with open("input.txt") as f:
    inp = f.read()

visited = set()
visited.add((0, 0))

coord = dict()
coord["santa"] = [0, 0]
coord["robot"] = [0, 0]

for i, dir in enumerate(inp):
    if i % 2 == 1: p = "santa"
    else: p = "robot"
    
    if dir == "^":
        coord[p][1] -= 1
    elif dir == ">":
        coord[p][0] += 1
    elif dir == "v":
        coord[p][1] += 1
    else:
        coord[p][0] -= 1
    visited.add((coord[p][0], coord[p][1]))

result = len(visited)
print(f"Result is: {result}")