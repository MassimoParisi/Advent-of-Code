import re
from collections import defaultdict

work = set()
workflow = defaultdict(list)
result = ""

with open("input.txt") as f:
    for line in f.readlines():
        tmp = re.match(
            r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.", line)
        before = tmp.group(1)
        after = tmp.group(2)
        work.add(before)
        work.add(after)
        workflow[after].append(before)

while work:
    doable = set()
    for w in work:
        if workflow[w] == []:
            doable.add(w)
    curr = min(doable)
    result += curr
    for wf in workflow:
        if curr in workflow[wf]:
            workflow[wf].remove(curr)
    work.remove(curr)

print(f"Result is: {result}")
