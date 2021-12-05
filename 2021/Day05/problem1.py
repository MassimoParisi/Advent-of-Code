from collections import defaultdict

coord_dict = defaultdict(lambda: 0)

with open("input.txt") as f:
    for line in f.readlines():
        begin, end = line[:-1].split(' -> ')
        x1,y1 = (int(x) for x in begin.split(','))
        x2,y2 = (int(x) for x in end.split(','))
        if x1 != x2 and y1 != y2:
            continue
        elif x1 == x2:
            y1,y2 = min(y1,y2), max(y1,y2)
            for y in range(y1,y2+1):
                coord_dict[(x1,y)] += 1
        else:   #y1 == y2
            x1,x2 = min(x1,x2), max(x1,x2)
            for x in range(x1, x2+1):
                coord_dict[(x,y1)] += 1

count = 0
for v in coord_dict.values():
    if v > 1:
        count += 1
print(count)
