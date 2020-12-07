ans = []
count = 0


def everyone():
    group_tot = 0
    for char in ans[0]:
        good = True
        for el in ans:
            if char not in el:
                good = False
                break
        if good:
            group_tot += 1
    return group_tot


with open("input.txt") as f:
    for line in f.readlines():
        if line != "\n":
            ans.append(list(line.strip()))
        else:
            count += everyone()
            ans.clear()
count += everyone()
print(count)
