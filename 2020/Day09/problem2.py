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


def find_min_max(inv: int):
    queue = []
    with open("input.txt") as f:
        for val in f.readlines():
            queue.append(int(val))
            while sum(queue) > inv:
                queue.pop(0)
            if sum(queue) == inv:
                min_val = min(queue)
                max_val = max(queue)
                return min_val + max_val


result = find_min_max(first_invalid(preamble))
print(f"Result is: {result}")
