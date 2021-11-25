def isValid(letters, checksum):
    if len(checksum) != 5:
        return False

    n = len(letters)
    freq_dict = dict()
    for l in letters:
        if l in freq_dict:
            freq_dict[l] += 1
        else:
            freq_dict[l] = 1
    freq_lst = [[] for _ in range(n)]
    for k,v in freq_dict.items():
        freq_lst[v].append(k)

    for i in range(n):
        freq_lst[i] = sorted(freq_lst[i],reverse=True)


    final_lst = [el for i in range(n) for el in freq_lst[i]]

    m = len(final_lst)
    tmp = "".join((final_lst[m-5:])[::-1])

    return tmp == checksum


rooms = []
with open("input.txt") as f:
    for line in f.readlines():
        # format input
        *words, num_and_checksum = line.split("-")
        num, checksum = num_and_checksum.split("[")
        checksum = checksum[:-2]
        letters = "".join(words)

        if isValid(letters, checksum):
            rooms.append([words, int(num)])

#for r in rooms:
#    print(r)

for r in rooms:
    print(r[1], end="\t")
    shift = r[1] % 26
    for word in r[0]:
        for char in word:
            tmp = ord(char) + shift
            if tmp > 122:
                tmp -= 26
            print(chr(tmp),end="")
        print(" ",end="")
    print("")
