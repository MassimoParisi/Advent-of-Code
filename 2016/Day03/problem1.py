res = 0
with open("input.txt") as f:
    for line in f.readlines():
        a, b, c = [int(x) for x in line.split()]
        if (a + b > c) and (a + c > b) and (b + c > a):
            res += 1
print(f"Result is: {res}")