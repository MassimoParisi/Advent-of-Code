prev = float("inf")
count = 0
with open("input.txt") as f:
    for line in f.readlines():
        curr = int(line[:-1])
        print(curr)
        if curr > prev:
            count += 1
        prev = curr

print(count)
