import re

result = 0

with open("input.txt") as f:
    for line in f:
        p = re.match(r'([0-9]+)-([0-9]+) (\D): (\D+)', line)
        i1 = int(p.group(1))
        i2 = int(p.group(2))
        char = p.group(3)
        text = p.group(4)

        b1 = False
        b2 = False
        if len(text) >= i1:
            b1 = text[i1 - 1] == char
        if len(text) >= i2:
            b2 = (text[i2 - 1] == char)

        if b1 ^ b2: result += 1

print(f"Result is: {result}")
