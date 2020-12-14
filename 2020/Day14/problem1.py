import re
mem = dict()

with open("input.txt") as f:
    for line in f.readlines():
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1].strip()
        else:
            tmp = re.match(r"mem\[(\d+)\]", line[0])
            addr = int(tmp.group(1))
            val = bin(int(line[1].strip()))[2:]
            off = len(mask) - len(val)
            val = list("0" * off + val)
            i = 0
            while mask[i] == "X" and i < len(mask):
                i += 1
            while i < len(mask):
                if mask[i] != "X":
                    val[i] = mask[i]
                i += 1

            val = int("".join(val), 2)
            mem[addr] = val

print(sum(mem.values()))
