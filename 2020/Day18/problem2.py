import re
from functools import reduce

def eval(eq: str) -> int:
    while "(" in eq:
        tmp = re.findall(r"\([^\(\)]*\)", eq)
        for v in tmp:
            eq = eq.replace(v, eval(v[1:-1]), 1)
    tmp = [int(x) for x in re.findall(r"\d+", eq)]
    oprt = re.findall(r"[+*]{1}", eq)
    while "+" in oprt:
        i = oprt.index("+")                 
        partial = tmp[i] + tmp[i+1]
        oprt.pop(i)
        tmp.pop(i)
        tmp.pop(i)
        tmp.insert(i, partial)
    tmp = reduce(lambda x,y: x*y, tmp)
    return str(tmp)


res = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace(" ", "")
        res += int(eval(line))
    print(f"Result is: {res}")
        