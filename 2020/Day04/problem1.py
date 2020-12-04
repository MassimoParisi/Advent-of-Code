import re
import functools
counter = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
opt = "cid"
toCheck = dict()
for el in fields:
    toCheck.update({el: False})

with open("input.txt") as f:
    for line in f:
        if line != "\n":
            fi = line.split()
            fi[-1] = fi[-1].strip()
            for x in fi:
                pattern = re.match(r"([a-z]{3}):.+", x)
                id = pattern.group(1)
                if id != opt:
                    toCheck.update({id: True})
        else:
            if False not in toCheck.values():
                counter += 1
            for key in toCheck.keys():
                toCheck.update({key: False})

if False not in toCheck.values():
    counter += 1

print(counter)