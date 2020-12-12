with open("input.txt") as f:
    pol = list(f.read().strip())

i = 0
while i < len(pol) - 1:
    if abs(ord(pol[i]) - ord(pol[i+1])) == 32:
        pol.pop(i)
        pol.pop(i)
        if i > 0: i -= 1
    else: i += 1
result = len(pol)
print(f"Result is: {result}")
