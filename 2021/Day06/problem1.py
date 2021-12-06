from tqdm import tqdm

with open("input.txt") as f:
    inp = [int(x) for x in f.readline()[:-1].split(',')]

n = len(inp)

for _ in tqdm(range(80),desc="iteration"):
    new_fish = 0
    for i in range(len(inp)):
        if inp[i] > 0:
            inp[i] -= 1
        else:
            inp[i] = 6
            new_fish += 1

    inp.extend([8]*new_fish)

print(len(inp))