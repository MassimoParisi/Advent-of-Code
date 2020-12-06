ans = []
count = 0

def everyone():
    groupTot = 0
    for char in ans[0]:
        good = True
        for el in ans:
            if char not in el:
                good = False
                break
        if good:
            groupTot += 1
    return groupTot

with open("input.txt") as f:
    for line in f.readlines():
        if line != "\n":
            ans.append(list(line.strip()))
        else:
            count += everyone()
            ans.clear()
count += everyone()
print(count)
