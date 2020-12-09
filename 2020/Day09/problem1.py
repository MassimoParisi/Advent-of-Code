preamble = 25


def first_invalid(pre: int):
    usable = []
    with open("input.txt") as f:
        for _ in range(pre):
            usable.append(int(f.readline()))

        while True:
            curr = int(f.readline())
            found = False
            for i, e1 in enumerate(usable):
                for j, e2 in enumerate(usable):
                    if e1 != e2 and e1+e2 == curr:
                        found = True
                        usable.pop(0)
                        usable.append(curr)
                        break
                if found:
                    break
            if not found:
                return curr


result = first_invalid(preamble)
print(f"Result is: {result}")
