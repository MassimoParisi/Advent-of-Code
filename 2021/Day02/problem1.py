x,y = 0, 0

with open("input.txt") as f:
    for line in f.readlines():
        istr = line.split(" ")
        istr[1] = int(istr[1][:-1])
        #print(istr)
        if istr[0] == 'forward':
            x += istr[1]
        elif istr[0] == 'up':
            y -= istr[1]
        else:
            y += istr[1]
        print(x,y)

print(x*y)
