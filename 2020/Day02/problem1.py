with open("input.txt") as f:
    values = f.readlines()

counter = 0

for i in range(len(values)):
        values[i] = values[i].split()
        values[i][0] = values[i][0].split("-")
        for j in range(len(values[i][0])):
            values[i][0][j] = int(values[i][0][j])
        values[i][1] = values[i][1][0]

        minVal = values[i][0][0]
        maxVal = values[i][0][1]
        char = values[i][1]
        text = values[i][2]

        if minVal <= text.count(char) <= maxVal:
            counter += 1



print(counter)
