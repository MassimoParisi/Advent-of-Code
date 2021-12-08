from collections import defaultdict

registers = defaultdict(lambda: 0)

cond_dict = {
    ">": lambda x,y: x > y,
    ">=": lambda x,y: x >= y,
    "<": lambda x,y: x < y,
    "<=": lambda x,y: x <= y,
    "==": lambda x,y: x == y,
    "!=": lambda x,y: x != y
}

with open("input.txt") as f:
    for line in f.readlines():
        reg1, op, qty1, _, reg2, cond, qty2 = line[:-1].split(" ")
        qty1, qty2 = int(qty1), int(qty2)
        if cond_dict[cond](registers[reg2], qty2):
            if op == "inc":
                registers[reg1] += qty1
            else:
                registers[reg1] -= qty1

print(max(registers.values()))
