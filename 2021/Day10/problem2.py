match_dict = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">"
}

score_dict = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4
}

score = []
with open("input.txt") as f:
    for line in f.readlines():
        flag = True
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
                    flag = False
                    break
        if flag:
            curr_score = 0
            while stack:
                curr_score *= 5
                curr_score += score_dict[stack.pop()]
            score.append(curr_score)

score.sort()
m = len(score)
print(score[m//2])

