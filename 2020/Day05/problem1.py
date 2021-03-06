maxID = 0

with open("input.txt") as f:
    for line in f.readlines():
        row = 0
        col = 0
        for i in range(6, -1, -1):
            if line[i] == "B":
                row += 2 ** (6 - i)
        for i in range(2, -1, -1):
            if line[7 + i] == "R":
                col += 2 ** (2 - i)
        spotID = row * 8 + col
        maxID = max(maxID, spotID)

print(f"Result is: {maxID}")
