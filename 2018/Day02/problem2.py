with open("input.txt") as f:
    arr = [x for x in f.readlines()]

for i in range(len(arr) - 1):
    for j in range(i+1, len(arr)):
        diff = None
        good = True
        for k in range(len(arr[i])):
            if arr[i][k] != arr[j][k]:
                if diff:
                    good = False 
                    break
                diff = k
        if good:break
    if good: break

result = arr[i][:diff] + arr[i][diff+1:]
print(f"Result is: {result}")

