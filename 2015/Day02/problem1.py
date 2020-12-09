result = 0

with open("input.txt") as f:
    for line in f.readlines():
        l, w, h = line.split("x")
        l, w ,h = int(l), int(w), int(h)
        result += (2 * l * w) + (2 * w * h) + (2 * h * l) + min(l * w, l * h, w * h)

print(f"Result is: {result}")