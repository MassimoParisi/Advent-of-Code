with open("input.txt") as f:
    inp = f.read()
result = inp.count("(") - inp.count(")")
print(f"Result is: {result}")