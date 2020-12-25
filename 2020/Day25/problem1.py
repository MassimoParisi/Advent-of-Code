with open("input.txt") as f:
    card = int(f.readline().strip())
    door = int(f.readline().strip())

g = 7
p = 20201227 
i = 1
k = 0
while i != card:
    k += 1
    i = (i * g) % p

res = (door ** k) % p
print(f"Result is: {res}")
