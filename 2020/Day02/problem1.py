import re

counter = 0

with open("input.txt") as f:
    for line in f:
        pattern = re.match(r'([0-9]+)-([0-9]+) (\D): (\D+)', line)
        minVal = int(pattern.group(1))
        maxVal = int(pattern.group(2))
        char = pattern.group(3)
        text = pattern.group(4)

        if minVal <= text.count(char) <= maxVal: counter += 1

print(f"Result is: {counter}")
