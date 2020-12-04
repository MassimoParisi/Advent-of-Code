import re
counter = 0

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
opt = "cid"
toCheck = dict()
for el in fields:
    toCheck.update({el: False})

colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
numb = 0
with open("input.txt") as f:
    for line in f:
        if line != "\n":
            fi = line.split()
            fi[-1] = fi[-1].strip()
            for x in fi:
                pattern = re.match(r"^([a-z]{3}):(.+)$", x)
                id = pattern.group(1)
                arg = pattern.group(2)

                if id == "cid": continue

                elif id == "byr":
                     if 1920 <= int(arg) <= 2002:
                        toCheck.update({id: True})
                        continue

                elif id == "iyr":
                    if 2010 <= int(arg) <= 2020:
                        toCheck.update({id: True})
                        continue

                elif id == "eyr": 
                    if 2020 <= int(arg) <= 2030:
                        toCheck.update({id: True})
                        continue

                elif id == "hgt":
                    arg = re.match(r"^([0-9]+)(..)$", arg)
                    if arg != None:
                        num = int(arg.group(1))
                        unity = arg.group(2)
                        if (unity == "cm" and 150 <= num <= 193) or \
                           (unity == "in" and 59 <= num <= 76):
                            toCheck.update({id: True})
                            continue

                elif id == "hcl":
                    pat = re.match(r"^#[0-9a-f]{6}$", arg)
                    if pat != None:
                        toCheck.update({id: True})
                        continue

                elif id == "ecl":
                    if arg in colors:
                        toCheck.update({id: True})
                        continue

                elif id == "pid":
                    arg = re.match(r"^[0-9]{9}$", arg)
                    if arg != None:
                        toCheck.update({id: True})
                        continue
        else:
            numb  += 1
            if False not in toCheck.values():
                counter += 1
            for key in toCheck.keys():
                toCheck.update({key: False})

if False not in toCheck.values():
    counter += 1

print(counter)