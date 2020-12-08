with open("input.txt") as f:
    inp = f.readlines()

i = 0
acc = 0
visited = set()

while i not in visited:
    visited.add(i)
    istr, arg = inp[i].split()
    arg = int(arg)
    if istr == "jmp":
        i += arg
        continue
    if istr == "acc":
        acc += arg
    i += 1

print(f"Result is: {acc}")
