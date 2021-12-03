arr = []
gamma = []
epsilon = []
with open("input.txt") as f:
    for line in f.readlines():
        arr.append(line[:-1])


n = len(arr[0])
m = len(arr)

print(n,m)

for i in range(n):
    zeros, ones = 0, 0
    for j in range(m):
        if arr[j][i] == "0":
            zeros += 1
        else:
            ones += 1

    if zeros >= ones:
        gamma.append("0")
        epsilon.append("1")
    else:
        gamma.append("1")
        epsilon.append("0")

gamma = "".join(gamma)
epsilon = "".join(epsilon)

print(int(gamma,2) * int(epsilon,2))


