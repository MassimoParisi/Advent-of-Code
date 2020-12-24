from collections import defaultdict

tiles = defaultdict(bool)

with open("input.txt") as f:
    for line in f.readlines():
        x, y, z = 0, 0, 0
        i = 0
        while i < len(line):
            if line[i] == "e":
                x += 1
                y += 1
            elif line[i] == "w":
                x -= 1
                y -= 1
            elif line[i] == "s":
                if line[i+1] == "e":
                    x += 1
                    z -= 1
                elif line[i+1] == "w":
                    y -= 1
                    z -= 1
                i += 1
            elif line[i] == "n":
                if line[i+1] == "w":
                    x -= 1
                    z += 1
                elif line[i+1] == "e":
                    y += 1
                    z += 1
                i += 1
            i += 1
        tiles[(x,y,z)] = not tiles[(x,y,z)]


def adjacent(tile: (int, int, int)) -> int:
    adj = 0
    x, y, z = tile
    if tiles[(x, y + 1, z + 1)]: adj += 1
    if tiles[(x + 1, y + 1, z)]: adj += 1
    if tiles[(x + 1, y, z - 1)]: adj += 1
    if tiles[(x, y - 1, z - 1)]: adj += 1
    if tiles[(x - 1, y - 1, z)]: adj += 1
    if tiles[(x - 1, y, z + 1)]: adj += 1
    return adj
    
t_copy = tiles.copy()
for _ in range(100):
    keys = list(tiles.keys())
    for k in keys:
        x, y, z = k
        tiles[(x, y + 1, z + 1)]
        tiles[(x + 1, y + 1, z)]
        tiles[(x + 1, y, z - 1)]
        tiles[(x, y - 1, z - 1)]
        tiles[(x - 1, y - 1, z)]
        tiles[(x - 1, y, z + 1)]

    for tile in list(tiles.keys()):
        adj = adjacent(tile)
        if tiles[tile]:
            if adj == 0 or adj > 2:
                t_copy[tile] = not t_copy[tile]
        else:
            if adj == 2:
                t_copy[tile] = not t_copy[tile]
    tiles = t_copy.copy()


res = list(tiles.values()).count(True)
print(f"Result is: {res}")

