freq = 0
vis = {0}
twice = False
while not twice:
    with open("input.txt") as f:
        for el in f.readlines():
            freq += int(el)
            if freq in vis:
                twice = True
                break
            vis.add(freq)
print(f"Result is: {freq}")