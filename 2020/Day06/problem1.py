ans = set()
count = 0

with open("input.txt") as f:
    for line in f.readlines():
        if line != "\n":
            for char in line.strip():
                ans.add(char)
        else:
            count += len(ans)
            ans.clear()
count += len(ans)



print(count)

