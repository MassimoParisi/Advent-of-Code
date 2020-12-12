with open("input.txt") as f:
    pol = f.read().strip()

min_p = len(pol)
for u in set(pol.lower()):
    curr_pol = [x for x in pol if x != u and x != u.upper()]
    i = 0
    while i < len(curr_pol) - 1:
        if abs(ord(curr_pol[i]) - ord(curr_pol[i+1])) == 32:
            curr_pol.pop(i)
            curr_pol.pop(i)
            if i > 0: i -= 1
        else: i += 1
    if len(curr_pol) < min_p:
        min_p = len(curr_pol)

print(f"Result is: {min_p}")
