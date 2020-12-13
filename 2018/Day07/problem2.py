import re
from collections import defaultdict

work = set()
workflow = defaultdict(list)
with open("input.txt") as f:
    for line in f.readlines():
        tmp = re.match(
            r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.", line)
        before = tmp.group(1)
        after = tmp.group(2)
        work.add(before)
        work.add(after)
        workflow[after].append(before)


doable = set()
curr = []
cost = []
result = 0
while work:
    result += 1
    for w in work:
        if workflow[w] == [] and w not in curr:
            doable.add(w)
    while len(curr) < 5 and doable:
        task = min(doable)
        curr.append(task)
        cost.append(60 + ord(task) - 64)
        doable.remove(min(doable))
    cost = [x-1 for x in cost]
    for i, c in enumerate(cost):
        if c == 0:
            done = curr.pop(i)
            for wf in workflow:
                if done in workflow[wf]:
                    workflow[wf].remove(done)
            work.remove(done)
    cost = [x for x in cost if x != 0]

print(f"Result is: {result}")
