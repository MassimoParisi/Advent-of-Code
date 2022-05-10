from gc import garbage


with open("input.txt") as f:
    inp = f.read().strip()

score = 0
curr_score = 0
garbage = False

n = len(inp)
i = 0
while i < n:
    if inp[i] == '!':
        i += 2
        continue

    if garbage:
        if inp[i] == '>':
            garbage = False
        i += 1
        continue

    else:
        if inp[i] == '<':
            garbage = True
        elif inp[i] == '{':
            curr_score += 1
        elif inp[i] == '}':
            score += curr_score
            curr_score -= 1
        i += 1
print(score)
        
