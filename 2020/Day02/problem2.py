with open("input.txt") as f:
    values = f.readlines()

counter = 0

for i in range(len(values)):
        values[i] = values[i].split()
        values[i][0] = values[i][0].split("-")
        for j in range(len(values[i][0])):
            values[i][0][j] = int(values[i][0][j])
        values[i][1] = values[i][1][0]

        i1 = values[i][0][0]
        i2 = values[i][0][1]
        char = values[i][1]
        text = values[i][2]
        
        b1 = False
        b2 = False
        if len(text) >= i1:
            b1 = text[i1-1] == char
        if len(text) >= i2:
            b2 = (text[i2-1] == char)

        if b1 ^ b2: counter += 1



print(counter)
