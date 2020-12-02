fuel = 0

with open("input.txt") as f:
    for line in f:
        unityFuel = int(int(line)/3)-2
        fuel += unityFuel
        while(True):
            unityFuel = max(int(unityFuel/3)-2, 0)
            if unityFuel == 0:
                break
            else:
                fuel += unityFuel

print(f"Result is: {fuel}")