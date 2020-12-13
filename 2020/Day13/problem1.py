with open("input.txt") as f:
    arrive = int(f.readline())
    inp = [int(el) for el in f.readline().split(",") if el != "x"]

bus = min(inp, key=lambda x: x - (arrive % x))
mins = bus - (arrive % bus)
print(f"Result is: {bus * mins}")
