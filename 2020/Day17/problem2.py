from collections import defaultdict

pos = defaultdict(bool)
xr, yr, zr, wr = 0, 0, 0, 0
with open("input.txt") as f:
    for line in f.readlines():
        yr = 0
        line = line.strip()
        for val in line:
            pos[(xr, yr, zr, wr)] = True if val == "#" else False
            yr += 1
        xr += 1
pos_c = pos.copy()
xyzw_min = 0


def neighbors(x0: int, y0: int, z0: int, w0: int) -> int:
    n = [pos[(x, y, z, w)] for x in range(x0 - 1, x0 + 2) for y in range(y0 - 1, y0 + 2) for z in range(z0 - 1, z0 + 2) for w in range(w0 - 1, w0 + 2)]
    n = n.count(True)
    if pos[x0, y0, z0, w0]: n -= 1
    return n


for _ in range(6):
    xyzw_min -= 1                                           
    xr += 1                                                 
    yr += 1
    zr += 1
    wr += 1
    for x in range(xyzw_min, xr):
        for y in range(xyzw_min, yr):
            for z in range(xyzw_min, zr + 1):
                for w in range(xyzw_min, wr + 1):
                    n = neighbors(x, y, z, w)
                    if pos[(x, y, z, w)] and n != 2 and n != 3:
                        pos_c[(x, y, z, w)] = False
                    elif not pos[(x, y, z, w)] and n == 3:
                        pos_c[(x, y, z, w)] = True
    pos = pos_c.copy()
res = [x for x in pos.values()].count(True)
print(f"Result is: {res}")
