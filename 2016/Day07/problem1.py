import re

counter = 0

def isAbba(word):
    if not word:
        return False
    n = len(word)
    i = 0
    while i+3 < n:
        if word[i] == word[i+1]:
            i += 1
        else:
            if word[i] == word[i+3] and \
                    word[i+1] == word[i+2]:
                        print("HEY")
                        return True
            i += 1
    return False


with open("input.txt") as f:
    for line in f.readlines():

        arr = re.split('\[|\]',line[:-1])

        print(arr)

        flag = False
        for i,el in enumerate(arr):
            if i % 2 != 0:      # in brackets
                if isAbba(el):
                    flag = False
                    break
            else:               # out brackets
                if isAbba(el):
                    flag = True

        if flag:
            counter += 1

print(counter)
