import re

with open("input.txt") as f:
    values = f.readline()
values = re.match(r'^([0-9]+)-([0-9]+)$', values)
minVal = int(values.group(1))
maxVal = int(values.group(2))
counter = 0

def nonDecreasing(psw: list) -> bool:
    return psw == sorted(psw)

def twinsCheck(psw: str):
    return max(psw.count(x) for x in set(psw)) >= 2

for num in range(minVal, maxVal):
    num = list(str(num))
    if nonDecreasing(num) and twinsCheck(num): counter += 1
print(counter)
