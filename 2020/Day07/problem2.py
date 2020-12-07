import re

bagDict = dict()
with open("input.txt") as f:
    for line in f.readlines():
        contain = line.split(" bags contain ")
        bagType = contain[0]
        contained = re.findall(r"\d+ [a-z ]+ bag", contain[1])
        for i, c in enumerate(contained):
            tmp = re.match(r"(\d+) ([a-z ]+) bag", c)
            qty = int(tmp.group(1))
            name = tmp.group(2)
            contained[i] = (name, qty)
        bagDict.update({bagType: contained})


def inside(bagType: str) -> int:
    contained = []
    for el in bagDict.get(bagType):
        contained.append(el[1]*inside(el[0]))
    return 1 + sum(contained)


# I don't want to count the shiny gold bag itself
result = inside("shiny gold") - 1
print(f"Result is: {result}")
