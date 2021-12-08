len_dict = {
    2: [1],
    4: [4],
    3: [7],
    5: [2,3,5],
    6: [0,6,9],
    7: [8],
}

wires_dict = {k:None for k in [1,4,7,8]}
count = 0
with open("input.txt") as f:
    for line in f.readlines():
        pat, out = line[:-1].split(' | ')
        pat = pat.split(' ')
        pat.sort(key=lambda x:len(x) in [2,3,4,7], reverse=True)
        out = out.split(' ')

        for p in pat:
            p = set(p)
            possible = len(len_dict[len(p)])
            # if there is only one possible digit
            if possible == 1:
              wires_dict[len_dict[len(p)][0]] = p

            # otherwise, check 5 wires case
            elif len(p) == 5:
                # if 1 wire are a subset --> 3
                if wires_dict[1].issubset(p):
                    wires_dict[3] = p
                elif len(wires_dict[4].intersection(p)) == 3:
                    wires_dict[5] = p
                else:
                    wires_dict[2] = p

            # and 6 wires case
            else:
                if not wires_dict[1].issubset(p):
                    wires_dict[6] = p
                elif len(wires_dict[4].intersection(p)) == 4:
                    wires_dict[9] = p
                else:
                    wires_dict[0] = p
        curr_out = []
        for o in out:
            o = set(o)
            for w in wires_dict.keys():
                if wires_dict[w] == o:
                    curr_out.append(w)
                    break
        count += int(''.join(str(i) for i in curr_out))
print(count)
