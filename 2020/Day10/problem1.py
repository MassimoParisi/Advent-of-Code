voltages = [0]

with open("input.txt") as f:
    for line in f.readlines():
        voltages.append(int(line))

voltages.sort()
voltages.append(max(voltages) + 3)

diff_1 = 0
diff_3 = 0
for i in range(1, len(voltages)):
    if voltages[i] - voltages[i-1] == 1:
        diff_1 += 1
    elif voltages[i] - voltages[i-1] == 3:
        diff_3 += 1

print(diff_1 * diff_3)

