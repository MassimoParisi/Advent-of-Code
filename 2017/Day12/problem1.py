with open("input.txt") as f:
    pipes = [x for x in f.read().split('\n')]

n = len(pipes)
for i in range(n):
    line = pipes[i]
    pipes[i] = [int(x) for x in line.split(' <-> ')[1].split(', ')]


to_check = [0]
used = set()
while to_check:
    curr = to_check.pop()
    used.add(curr)
    for el in pipes[curr]:
        if el not in used:
            to_check.append(el)

print(len(used))