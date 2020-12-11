spot = []

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        line = list(line)
        spot.append(line)

next_spot = [list(x) for x in spot]


def adjacent(i: int, j: int) -> list:
    adj = []
    n = len(spot)
    m = len(spot[0])
    if i > 0:
        adj.append(spot[i-1][j])
        if j > 0: adj.append(spot[i-1][j-1])
        if j < m - 1: adj.append(spot[i-1][j+1])
    if i < n - 1:
        adj.append(spot[i+1][j])
        if j > 0: adj.append(spot[i+1][j-1])
        if j < m - 1: adj.append(spot[i+1][j+1])
    if j > 0: adj.append(spot[i][j-1])
    if j < m - 1: adj.append(spot[i][j+1])

    return adj


while True:
    change = False
    for i in range(len(spot)):
        for j in range(len(spot[0])):
            if spot[i][j] == ".":
                continue
            if spot[i][j] == "L":
                if "#" not in adjacent(i, j):
                    next_spot[i][j] = "#"
                    change = True
            else:
                adj = adjacent(i, j)
                if adj.count("#") >= 4:
                    next_spot[i][j] = "L"
                    change = True
    if not change: break
    else: spot = [list(x) for x in next_spot]

result = 0
for row in spot:
    result += row.count("#")
print(f"Result is: {result}")
