arr = []
gamma = []
epsilon = []
with open("input.txt") as f:
    for line in f.readlines():
        arr.append(line[:-1])


n = len(arr[0])
m = len(arr)

oxygen = arr.copy()
co2 = arr.copy()
curr_bit = 0

def removeOxygen(i, x):

    idx = 0
    while idx < len(oxygen):
        if oxygen[idx][i] == x:
            idx += 1
        else:
            oxygen.pop(idx)

def removeCO2(i, x):
    idx = 0
    while idx < len(co2):
        if co2[idx][i] == x:
            idx += 1
        else:
            co2.pop(idx)



while len(oxygen) > 1:
    zeros, ones = 0, 0
    for i in range(len(oxygen)):
        if oxygen[i][curr_bit] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        removeOxygen(curr_bit, "0")
        #removeCO2(curr_bit, "1")
    else:
        removeOxygen(curr_bit, "1")
        #removeCO2(curr_bit, "0")
    curr_bit += 1

curr_bit = 0
while len(co2) > 1:
    zeros, ones = 0, 0
    for i in range(len(co2)):
         if co2[i][curr_bit] == "0":
            zeros += 1
         else:
            ones += 1
    if zeros > ones:
        #removeOxygen(curr_bit, "0")
        removeCO2(curr_bit, "1")
    else:
        #removeOxygen(curr_bit, "1")
        removeCO2(curr_bit, "0")
    curr_bit += 1


print(int(oxygen[0],2) * int(co2[0],2))


