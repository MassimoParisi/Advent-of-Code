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
validColors = set()


def check(bagType: str) -> bool:
    # base case: the bag contains directly a shiny gold
    for el in bagDict.get(bagType):
        if el[0] == "shiny gold":
            validColors.add(bagType)
            return True

    # general case: search inside all the directly contained bags
    for el in bagDict.get(bagType):
        if check(el[0]):
            validColors.add(bagType)
            return True
    return False


for key in bagDict.keys():
    check(key)

result = len(validColors)
print(f"Result is: {result}")