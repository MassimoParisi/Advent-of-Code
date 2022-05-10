with open("input.txt") as f:
    inp = f.read().strip()

score = 0
garbage = False

n = len(inp)
i = 0
while i < n:
    if inp[i] == '!':
        i += 1
    elif garbage:
        if inp[i] == '>':
            garbage = False
        else:
            score += 1
    else:
        if inp[i] == '<':
            garbage = True
    i += 1
print(score)
        
