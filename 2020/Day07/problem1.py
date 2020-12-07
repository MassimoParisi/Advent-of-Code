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
valid_colors = set()


def check(bag_type: str) -> bool:
    # base case: the bag contains directly a shiny gold
    for el in bag_dict.get(bag_type):
        if el[0] == "shiny gold":
            valid_colors.add(bag_type)
            return True

    # general case: search inside all the directly contained bags
    for el in bag_dict.get(bag_type):
        if check(el[0]):
            valid_colors.add(bag_type)
            return True
    return False


for key in bag_dict.keys():
    check(key)

result = len(valid_colors)
print(f"Result is: {result}")
