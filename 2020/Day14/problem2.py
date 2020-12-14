import re
mem = dict()                    

with open("input.txt") as f:
    for line in f.readlines():
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1].strip()

        else:
            val = int(line[1].strip())
            tmp = re.match(r"mem\[(\d+)\]", line[0])
            addr = bin(int(tmp.group(1)))[2:]
            off = len(mask) - len(addr)
            addr = list("0" * off + addr)

            i = 0
            arr = []
            while i < len(mask):

                if mask[i] == "0":
                    if not arr:
                        arr.append([addr[i]])
                    else:
                        for a in arr:
                            a.append(addr[i])

                elif mask[i] == "1":
                    if not arr:
                        arr.append(["1"])
                    else:
                        for a in arr:
                            a.append("1")

                else:
                    if not arr:
                        arr.append(["1"])
                        arr.append(["0"])
                    else:
                        arr2 = [list(x) for x in arr]
                        for a in arr:
                            a.append("0")
                        for a2 in arr2:
                            a2.append("1")
                        arr += arr2
                i += 1
            for a in arr:
                a = int("".join(a), 2)
                mem[a] = val
print(sum(mem.values()))
