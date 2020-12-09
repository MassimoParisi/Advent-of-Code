vowels = ["a","e","i","o","u"]
banned = ["ab", "cd", "pq", "xy"]
result = 0

with open("input.txt") as f:
    for line in f.readlines():
        valid = True
        double = False
        vow_count = 0
        for i in range(len(line)):
            if line[i] in vowels: vow_count += 1
            if i == 0: continue
            if line[i-1 : i+1] in banned:
                valid = False
                break
            if line[i] == line[i - 1]: double = True
        if valid and vow_count >= 3 and double:
            result += 1

print(f"Result is: {result}")
