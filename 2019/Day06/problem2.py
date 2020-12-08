links = dict()

with open("input.txt") as f:
    for line in f.readlines():
        link = line.strip().split(")")
        mass = link[0]
        orb = link[1]
        links.update({orb: mass})


def chain(orb: str) -> list:
    chain = []
    mass = links[orb]
    while mass != "COM":
        chain.append(mass)
        mass = links[mass]
    chain.append("COM")
    return chain


def dist(you: list, santa: list):
    for i, x in enumerate(you):
        for j, y in enumerate(santa):
            if x == y:
                result = i + j
                print(f"Result is: {result}")
                return


you = chain("YOU")
santa = chain("SAN")
dist(you, santa)
