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

    i1 = i
    while i1 > 0 and spot[i1-1][j] == ".":
        i1 -= 1
    if i1 > 0:
        adj.append(spot[i1-1][j])

    i1 = i
    while i1 < n-1 and spot[i1+1][j] == ".":
        i1 += 1
    if i1 < n-1:
        adj.append(spot[i1+1][j])

    j1 = j
    while j1 > 0 and spot[i][j1-1] == ".":
        j1 -= 1
    if j1 > 0:
        adj.append(spot[i][j1-1])

    j1 = j
    while j1 < m-1 and spot[i][j1+1] == ".":
        j1 += 1
    if j1 < m-1:
        adj.append(spot[i][j1+1])

    i1, j1 = i, j
    while i1 > 0 and j1 > 0 and spot[i1-1][j1-1] == ".":
        i1 -= 1
        j1 -= 1
    if i1 > 0 and j1 > 0:
        adj.append(spot[i1-1][j1-1])

    i1, j1 = i, j
    while i1 < n-1 and j1 < m-1 and spot[i1+1][j1+1] == ".":
        i1 += 1
        j1 += 1
    if i1 < n-1 and j1 < m-1:
        adj.append(spot[i1+1][j1+1])

    i1, j1 = i, j
    while i1 > 0 and j1 < m-1 and spot[i1-1][j1+1] == ".":
        i1 -= 1
        j1 += 1
    if i1 > 0 and j1 < m-1:
        adj.append(spot[i1-1][j1+1])

    i1, j1 = i, j
    while i1 < n-1 and j1 > 0 and spot[i1+1][j1-1] == ".":
        i1 += 1
        j1 -= 1
    if i1 < n-1 and j1 > 0:
        adj.append(spot[i1+1][j1-1])

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
                if adj.count("#") >= 5:
                    next_spot[i][j] = "L"
                    change = True
    if not change:
        break
    else:
        spot = [list(x) for x in next_spot]

result = 0
for row in spot:
    result += row.count("#")
print(result)
