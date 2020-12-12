import re
from collections import defaultdict

logs = []
sleep = defaultdict(lambda: defaultdict(int))

with open("input.txt") as f:
    for line in f.readlines():
        tmp = re.match(r"\[\d+-(\d+)-(\d+) (\d+):(\d+)\] (.+)", line)
        month = int(tmp.group(1))
        day = int(tmp.group(2))
        hour = int(tmp.group(3))
        mins = int(tmp.group(4))
        istr = tmp.group(5)
        logs.append((month, day, hour, mins, istr))
logs.sort()

for log in logs:
    mins = log[3]
    istr = log[4]
    if istr == "falls asleep":
        begin = mins
    elif istr == "wakes up":
        end = mins
        for m in range(begin, end):
            sleep[guard][m] += 1
    else:
        tmp = re.match(r"Guard #(\d+) begins shift", istr)
        guard = int(tmp.group(1))


max_guard = max(sleep.keys(), key=lambda x: max(sleep[x][m] for m in sleep[x].keys()))
max_m = max(sleep[max_guard].keys(), key=lambda x: sleep[max_guard][x])
print(max_guard * max_m)
