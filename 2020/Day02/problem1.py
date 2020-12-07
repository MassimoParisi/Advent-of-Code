import re

counter = 0

with open("input.txt") as f:
    for line in f:
        p = re.match(r'([0-9]+)-([0-9]+) (\D): (\D+)', line)
        min_val = int(p.group(1))
        max_val = int(p.group(2))
        char = p.group(3)
        text = p.group(4)

        if min_val <= text.count(char) <= max_val:
            counter += 1

print(f"Result is: {counter}")
