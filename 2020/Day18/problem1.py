import re
import operator

ops = {
    '+' : operator.add,
    '*' : operator.mul,
}

def eval(eq: str) -> int:
    while "(" in eq:
        tmp = re.findall(r"\([^\(\)]*\)", eq)
        for v in tmp:
            eq = eq.replace(v, eval(v[1:-1]), 1)
    tmp = [int(x) for x in re.findall(r"\d+", eq)]
    oprt = re.findall(r"[+*]{1}", eq)
    while len(tmp) != 1:
        partial = ops[oprt[0]](tmp[0],tmp[1])
        oprt.pop(0)
        tmp.pop(0)
        tmp.pop(0)
        tmp.insert(0, partial)
    return str(*tmp)

res = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace(" ", "")
        res += int(eval(line))
print(f"Result is: {res}")
        