with open("input.txt") as f:
    inp = f.readlines()

j = 0
acc = 0
visited = set()
found = False


def change(j: int):
    while "acc" in inp[j]:
        j += 1
    if "jmp" in inp[j]:
        inp[j] = inp[j].replace("jmp", "nop")
    else:
        inp[j] = inp[j].replace("nop", "jmp")


while not found:
    i = 0
    acc = 0
    change(j)
    visited.clear()
    while i not in visited:
        if i >= len(inp):
            found = True
            break
        visited.add(i)
        istr, arg = inp[i].split()
        arg = int(arg)
        if istr == "jmp":
            i += arg
            continue
        if istr == "acc":
            acc += arg
        i += 1

    if not found:
        change(j)
        j += 1

print(f"Result is: {acc}")
