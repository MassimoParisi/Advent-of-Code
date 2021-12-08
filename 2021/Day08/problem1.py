len_dict = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}

wires_dict = {k:None for k in [1,4,7,8]}
count = 0
with open("input.txt") as f:
    for line in f.readlines():
        pat, out = line[:-1].split(' | ')
        pat = pat.split(' ')
        out = out.split(' ')

        for p in pat:
            if len(p) in len_dict:
              wires_dict[len_dict[len(p)]] = set(p)

        for o in out:
            if set(o) in wires_dict.values():
                count += 1
print(count)
