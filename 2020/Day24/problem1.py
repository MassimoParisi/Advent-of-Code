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
    
res = list(tiles.values()).count(True)
print(f"Result is: {res}")
        
