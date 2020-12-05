links = dict()

with open("input.txt") as f:
    for line in f.readlines():
        link = line.strip().split(")")
        mass = link[0]
        orb = link[1]
        if mass == "COM":
            mass = 1
        links.update({orb: mass})

def numOrbit(orb: str) -> int:
    mass = links[orb]
    if type(mass) == int:
        return links[orb]
    else:
        links.update({orb: 1 + numOrbit(mass)})
        return links[orb]

for m in links.keys():
    numOrbit(m)

print(f"Result is: {sum(links.values())}")