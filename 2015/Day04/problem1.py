import hashlib

with open("input.txt") as f:
    inp = f.read()

result = 0
while True:
    to_check = inp + str(result)
    h = hashlib.md5(to_check.encode())
    if h.hexdigest()[:5] == "00000":
        print(f"Result is: {result}")
        break
    result += 1
