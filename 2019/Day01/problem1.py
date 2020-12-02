total = 0

with open("input.txt") as f:
    for line in f:
        total += int(int(line)/3)-2

print(f"Result is: {total}")
