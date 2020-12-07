with open("input.txt") as f:
    values = [int(l.replace("\n", "")) for l in f.readlines()]

for i in range(len(values)):
    for j in range(i, len(values)):
        if values[i] + values[j] == 2020:
            result = values[i] * values[j]
            print(f"Result is: {result}")
