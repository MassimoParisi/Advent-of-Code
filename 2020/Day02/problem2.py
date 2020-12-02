import re

counter = 0

with open("input.txt") as f:
    for line in f:
        pattern = re.match(r'([0-9]+)-([0-9]+) (\D): (\D+)', line)
        i1 = int(pattern.group(1))
        i2 = int(pattern.group(2))
        char = pattern.group(3)
        text = pattern.group(4)

        b1 = False
        b2 = False
        if len(text) >= i1:
            b1 = text[i1-1] == char
        if len(text) >= i2:
            b2 = (text[i2-1] == char)

        if b1 ^ b2: counter += 1

print(f"Result is: {counter}")