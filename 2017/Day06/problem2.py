with open("input.txt") as f:
    inp = f.read().split("\t")
for i in range(len(inp)):
    inp[i] = int(inp[i])

num = 0
config = dict()
curr_config = "".join([str(x) for x in inp])

while curr_config not in config.keys():
    config[curr_config] = num
    num += 1
    i = inp.index(max(inp))
    blocks = inp[i]
    inp[i] = 0
    while blocks > 0:
        if(i + 1 == len(inp)): i = 0
        else: i += 1
        inp[i] += 1
        blocks -= 1
    curr_config = ",".join([str(x) for x in inp])

result = len(config) - config[curr_config]
print(result)
