res = 0
with open("input.txt") as f:
    values = f.readlines()
i = 0
while i < len(values):
    zipper = [[int(x) for x in values[i].split()],
              [int(x) for x in values[i+1].split()],
              [int(x) for x in values[i+2].split()]]
    for t in zip(*zipper):
        if (t[0] + t[1] > t[2]) and (t[0] + t[2] > t[1]) and (t[1] + t[2] > t[0]):
            res += 1
    i += 3
print(f"Result is: {res}")