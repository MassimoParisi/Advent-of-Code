arr = []
with open("input.txt") as f:
    for line in f.readlines():
        arr.append([int(x) for x in line[:-1]])

def check():
    return sum([sum(x) for x in arr]) == 0

n,m = len(arr), len(arr[0])
count = 1
while True:
    for i in range(n):
        for j in range(m):
            arr[i][j] += 1

    flash_lst = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] > 9:
                flash_lst.append((i,j))
    idx = 0
    while idx < len(flash_lst):
        i,j = flash_lst[idx]
        for (ni,nj) in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
            if (ni >= 0 and ni < n) and \
                (nj >= 0 and nj < m) and \
                (ni,nj) not in flash_lst:
                arr[ni][nj] += 1
                if arr[ni][nj] > 9:
                    flash_lst.append((ni,nj))
        arr[i][j] = 0
        idx += 1
    if check():
        print(count)
        break
    else:
        count += 1
