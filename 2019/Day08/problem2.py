wide = 25
tall = 6

with open("input.txt") as f:
    img = f.readline().strip()

def layers(img: str, w: int, t: int) -> list:
    dim = w * t
    return [img[i:dim+i] for i in range(0, len(img), dim)]

img = layers(img, wide, tall)

def render(pxl: int) -> chr:
    val = '2'
    i = 0
    while(val == '2'):
        val = img[i][pxl]
        i += 1
    if val == '0': return u"\u2591"
    else: return u"\u2588"

for i in range(tall):
    for j in range(wide):
        print(render(j + i * wide), end= "")
    print("\n", end="")