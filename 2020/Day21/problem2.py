import re
from collections import defaultdict

ingredients = set()
allergens = set()
comb = defaultdict(set)
count = defaultdict(int)
danger = []


with open("input.txt") as f:
    for line in f.readlines():
        tmp = re.match(r"(.+) \(contains (.+)\)", line)
        ingr = tmp.group(1).split(" ")
        al = tmp.group(2).split(", ")
        ingredients |= set(ingr)
        allergens |= set(al)
        for i in ingr:
            count[i] += 1
        for a in al:
            comb.setdefault(a, set(ingr))
            comb[a] &= set(ingr)

change = True
while change:
    change = False
    for a in allergens:
        if len(comb[a]) == 1:
            change = True
            delete = "".join(list(comb[a]))
            danger.append((a, delete))
            ingredients.remove(delete)
            for a2 in allergens:
                if a2 != a and delete in comb[a2]:
                    comb[a2].remove(delete)
            comb[a].remove(delete)

res = ""
for d in sorted(danger):
    res += d[1] + ","

print(f"Result is: {res[:-1]}")
