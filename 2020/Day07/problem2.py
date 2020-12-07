import re

bag_dict = dict()
with open("input.txt") as f:
    for line in f.readlines():
        contain = line.split(" bags contain ")
        bag_type = contain[0]
        contained = re.findall(r"\d+ [a-z ]+ bag", contain[1])
        for i, c in enumerate(contained):
            tmp = re.match(r"(\d+) ([a-z ]+) bag", c)
            qty = int(tmp.group(1))
            name = tmp.group(2)
            contained[i] = (name, qty)
        bag_dict.update({bag_type: contained})


def inside(bag_type: str) -> int:
    contained = []
    for el in bag_dict.get(bag_type):
        contained.append(el[1] * inside(el[0]))
    return 1 + sum(contained)


# I don't want to count the shiny gold bag itself
result = inside("shiny gold") - 1
print(f"Result is: {result}")
