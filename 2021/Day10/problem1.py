match_dict = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score_dict = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

score = 0
with open("input.txt") as f:
    for line in f.readlines():
        line = line[:-1]
        stack = []
        n = len(line)
        for i in range(n):
            curr = line[i]
            if curr in match_dict:
                stack.append(match_dict[curr])
            else:
                if curr == stack[-1]:
                    stack.pop()
                else:
                    score += score_dict[curr]
                    break
print(score)

