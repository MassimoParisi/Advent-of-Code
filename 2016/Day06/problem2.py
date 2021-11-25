words = []

with open("input.txt") as f:
    for line in f.readlines():
        words.append(line[:-1])

#for w in words:
#    print(w)
res = []
n = len(words)
for i in range(8):
    freq_dict = dict()
    for j in range(n):
        curr = words[j][i]
        if curr in freq_dict:
            freq_dict[curr] += 1
        else:
            freq_dict[curr] = 1
    max_chr = min(freq_dict,key= freq_dict.get)
    #print(max_chr)
    res.append(max_chr)

print("".join(res))
