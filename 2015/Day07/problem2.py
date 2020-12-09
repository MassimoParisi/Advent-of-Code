import re

wires = dict()


def init():
    with open("input.txt") as f:
        for line in f.readlines():
            tmp = re.match(r"(.+) -> ([a-z]+)", line)
            source = tmp.group(1)
            signal = tmp.group(2)

            tmp = re.match(r"([a-z0-9]*) ?([A-Z]+)* ?([a-z0-9]*)", source)
            val1 = tmp.group(1)
            op = tmp.group(2)
            val2 = tmp.group(3)

            wires[signal] = (val1, op, val2)


def calc_signal(curr_wire: str) -> int:
    if type(wires[curr_wire]) == int:
        return wires[curr_wire]

    val1, op, val2 = wires[curr_wire]
    if val1 != "" and not val1.isnumeric():
        val1 = calc_signal(val1)
    if val2 != "" and not val2.isnumeric():
        val2 = calc_signal(val2)

    if val1 != "":
        val1 = int(val1)
    if val2 != "":
        val2 = int(val2)
    # Manage operations
    if op == "NOT":
        res = ~ val2
    elif op == "AND":
        res = val1 & val2
    elif op == "OR":
        res = val1 | val2
    elif op == "LSHIFT":
        res = val1 << val2
    elif op == "RSHIFT":
        res = val1 >> val2
    else:
        res = val1

    wires[curr_wire] = res
    return res


init()
b = calc_signal("a")
init()
wires["b"] = b
result = calc_signal("a")
print(f"Result is: {result}")
