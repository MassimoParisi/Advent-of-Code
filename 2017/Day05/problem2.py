arr = []

with open("input.txt") as f:
    for line in f.readlines():
        arr.append(int(line))

i = 0
result = 0
arr_len = len(arr)
while 0 <= i < arr_len:
    jump = arr[i]
    arr[i] = arr[i] + 1 if arr[i] < 3 else arr[i] - 1
    i += jump
    result += 1

print(result)
