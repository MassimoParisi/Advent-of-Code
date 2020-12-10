voltages = [0]
connection = dict()

with open("input.txt") as f:
    for line in f.readlines():
        voltages.append(int(line))

voltages.sort()
voltages.append(max(voltages) + 3)


dp = [1]
for i in range(1, len(voltages)):
    ans = 0
    for j in range(i):
        if voltages[j] + 3 >= voltages[i]:
            ans += dp[j]
    dp.append(ans)

result = dp[-1]
print(f"Result is: {result}")
