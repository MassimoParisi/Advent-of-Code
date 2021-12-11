#import heapq as hq
arr = []

with open("input.txt") as f:
    for line in f.readlines():
        arr.append([int(x) for x in line[:-1]])


n, m = len(arr), len(arr[0])
seen = set()
max_basin = []


def search_basin(i,j):
    queue = [(i,j)]
    count = 0
    while queue:
        curr_i, curr_j = queue.pop(0)
        if arr[curr_i][curr_j] != 9 and (curr_i, curr_j) not in seen:
            count += 1
            for next_i, next_j in [ (curr_i + 1, curr_j),
                                    (curr_i - 1, curr_j),
                                    (curr_i, curr_j + 1),
                                    (curr_i, curr_j - 1)]:
                if  (next_i >= 0 and next_i < n) and \
                    (next_j >= 0 and next_j < m) and \
                    ((next_i,next_j) not in seen):
                    queue.append((next_i,next_j))
            seen.add((curr_i,curr_j))
    #print(f"basin size: {count}")
    max_basin.append(count)
    return


count = 0
for i in range(n):
    for j in range(m):
        #print(f"{i=},{j=}\tvalue {arr[i][j]}", end=" ")
        if (i,j) in seen:
            #print("[SEEN]")
            continue
        else:
            #print("[NEW]")
            search_basin(i,j)

max_basin.sort(reverse=True)
#print(max_basin)
print(max_basin[0]*max_basin[1]*max_basin[2])