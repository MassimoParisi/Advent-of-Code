with open("input.txt") as f:
    values = [int(l.replace("\n", "")) for l in f.readlines()]

for i in range(len(values)):
    for j in range(i, len(values)):
        for k in range(j, len(values)):
            if values[i] + values[j] + values[k] == 2020:
                print(f"Result is: {values[i] * values[j] * values[k]}")
