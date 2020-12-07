import re
import functools

counter = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
opt = "cid"
to_check = dict()
for el in fields:
    to_check.update({el: False})

with open("input.txt") as f:
    for line in f:
        if line != "\n":
            fi = line.split()
            fi[-1] = fi[-1].strip()
            for x in fi:
                pattern = re.match(r"([a-z]{3}):.+", x)
                id = pattern.group(1)
                if id != opt:
                    to_check.update({id: True})
        else:
            if False not in to_check.values():
                counter += 1
            for key in to_check.keys():
                to_check.update({key: False})

if False not in to_check.values():
    counter += 1

print(counter)
