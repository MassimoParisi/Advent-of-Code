vowels = ["a","e","i","o","u"]
banned = ["ab", "cd", "pq", "xy"]
result = 0

with open("input.txt") as f:
    for line in f.readlines():
        diff_pair = False
        twins = False

        for i in range(2, len(line)):
            if line[i] == line[i - 2]:
                twins = True
                break
        if not twins: continue

        for i in range(len(line) - 3):
            for j in range(i + 2, len(line) - 1):
                if line[i:i+2] == line[j:j+2]:
                    diff_pair = True
                    break
            if diff_pair: break

        if diff_pair:
            result += 1

print(f"Result is: {result}")
