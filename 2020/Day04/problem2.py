import re

counter = 0
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
opt = "cid_field"
to_check = dict()
for el in fields:
    to_check.update({el: False})

colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
numb = 0
with open("input.txt") as f:
    for line in f:
        if line != "\n":
            fi = line.split()
            fi[-1] = fi[-1].strip()
            for x in fi:
                pattern = re.match(r"^([a-z]{3}):(.+)$", x)
                id_field = pattern.group(1)
                arg = pattern.group(2)

                if id_field == "cid":
                    continue

                elif id_field == "byr":
                    if 1920 <= int(arg) <= 2002:
                        to_check.update({id_field: True})
                        continue

                elif id_field == "iyr":
                    if 2010 <= int(arg) <= 2020:
                        to_check.update({id_field: True})
                        continue

                elif id_field == "eyr":
                    if 2020 <= int(arg) <= 2030:
                        to_check.update({id_field: True})
                        continue

                elif id_field == "hgt":
                    arg = re.match(r"^([0-9]+)(..)$", arg)
                    if arg != None:
                        num = int(arg.group(1))
                        unity = arg.group(2)
                        if (unity == "cm" and 150 <= num <= 193) or \
                           (unity == "in" and 59 <= num <= 76):
                            to_check.update({id_field: True})
                            continue

                elif id_field == "hcl":
                    pat = re.match(r"^#[0-9a-f]{6}$", arg)
                    if pat != None:
                        to_check.update({id_field: True})
                        continue

                elif id_field == "ecl":
                    if arg in colors:
                        to_check.update({id_field: True})
                        continue

                elif id_field == "pid":
                    arg = re.match(r"^[0-9]{9}$", arg)
                    if arg != None:
                        to_check.update({id_field: True})
                        continue
        else:
            numb += 1
            if False not in to_check.values():
                counter += 1
            for key in to_check.keys():
                to_check.update({key: False})

if False not in to_check.values():
    counter += 1

print(counter)
