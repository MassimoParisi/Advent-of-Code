with open("input.txt") as f:
    pipes = [x for x in f.read().split('\n')]

n = len(pipes)
for i in range(n):
    line = pipes[i]
    pipes[i] = [int(x) for x in line.split(' <-> ')[1].split(', ')]

n_groups = 0
used = set()

for i in range(n):
    if i not in used:
        to_check = [i]
        while to_check:
            curr = to_check.pop()
            used.add(curr)
            for el in pipes[curr]:
                if el not in used:
                    to_check.append(el)
        n_groups += 1

print(n_groups)