result = 0
with open("input.txt") as f:
    for line in f.readlines():
        result += int(line)
print(f"Result is: {result}")