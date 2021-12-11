arr = []

with open("input.txt") as f:
    for line in f.readlines():
        arr.append([int(x) for x in line[:-1]])


n, m = len(arr), len(arr[0])

def check(i,j):
    curr = arr[i][j]
    if (i == 0 or arr[i-1][j] > curr) and \
       (j == 0 or arr[i][j-1] > curr) and \
       (i == n-1 or arr[i+1][j] > curr) and \
       (j == m-1 or arr[i][j+1] > curr):
        return True
    else:
        return False

count = 0
for i in range(n):
    for j in range(m):
        if check(i,j):
            count += arr[i][j] + 1

print(count)
