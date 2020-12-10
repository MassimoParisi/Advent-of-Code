result = 0

def isAnagram(w1: str, w2: str) -> bool:
    return sorted(list(w1)) == sorted(list(w2))


with open("input.txt") as f:
    for line in f.readlines():
        line = line.split()
        anagram = False
        for i in range(len(line) - 1):
            for j in range(i + 1, len(line)):
                if isAnagram(line[i], line[j]):
                    anagram = True
                    break
            if anagram: break
        
        if not anagram: result += 1

print(result)
