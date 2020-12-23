num_moves = 100

with open("input.txt") as f:
    inp = [int(x) for x in f.read()]

num_el = len(inp)

next = dict()
for i in range(len(inp) - 1):
    next[inp[i]] = inp[i + 1]
next[inp[len(inp) - 1]] = inp[0]


curr = inp[0]
moves = 0
while moves < num_moves:
    buff = []
    r = curr
    for _ in range(3):
        r = next[r]
        buff.append(r)
    next[curr] = next[r]

    dest = curr - 1 if curr != 1 else num_el
    while dest in buff:
        dest -= 1
        if dest < 1: dest = num_el
        
    tmp = next[dest]
    next[dest] = buff[0]
    next[buff[2]] = tmp

    curr = next[curr]
    moves += 1

res = ""
el = 1
while next[el] != 1:
    el = next[el]
    res += str(el)
print(f"Solution is: {res}")
