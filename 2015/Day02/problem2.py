result = 0

with open("input.txt") as f:
    for line in f.readlines():
        l, w, h = line.split("x")
        l, w ,h = int(l), int(w), int(h)
        result += (l * w * h) + min(2*l + 2*w, 2*l + 2*h, 2*w + 2*h)

print(f"Result is: {result}")