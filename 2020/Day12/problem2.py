x0, y0 = 0, 0
x, y = 10, 1
dir = ["N", "E", "S", "W"]
i = 1
with open("input.txt") as f:
    for line in f.readlines():
        istr = line[0]
        step = int(line[1:])

        if istr == "N":
            y += step
        elif istr == "E":
            x += step
        elif istr == "S":
            y -= step
        elif istr == "W":
            x -= step

        elif istr == "R":
            while step > 0:
                x, y = y, -1 * x
                step -= 90
        elif istr == "L":
            while step > 0:
                x, y = -1 * y, x
                step -= 90

        elif istr == "F":
            while step > 0:
                x0 += x
                y0 += y
                step -= 1

result = abs(x0) + abs(y0)
print(f"Result is: {result}")
