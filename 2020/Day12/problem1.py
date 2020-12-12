x, y = 0, 0
dir = ["N", "E", "S", "W"]
i = 1
with open("input.txt") as f:
    for line in f.readlines():
        istr = line[0]
        step = int(line[1:])

        def move(istr: str, step: int):
            global x, y, i
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
                    i = (i + 1) % 4
                    step -= 90
            elif istr == "L":
                while step > 0:
                    i = (i - 1) % 4
                    step -= 90

            elif istr == "F":
                move(dir[i], step)

        move(istr, step)

result = abs(x) + abs(y)
print(f"Result is: {result}")
