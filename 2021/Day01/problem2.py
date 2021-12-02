arr = []
with open("input.txt") as f:
    for line in f.readlines():
        arr.append(int(line[:-1]))


n = len(arr)
prev = 0
curr = 0
count = 0
for i in range(n):
    curr += arr[i]
    if i < 2:
        continue
    else:
        if curr > prev:
            count += 1
        prev = curr
        curr -= arr[i-2]

print(count-1)
