wide = 25
tall = 6

with open("input.txt") as f:
    img = f.readline().strip()

def layers(img: str, w: int, t: int) -> list:
    dim = w * t
    return [img[i:dim+i] for i in range(0, len(img), dim)]

img = layers(img, wide, tall)
zeros = list(map(lambda x: x.count('0'), img))
layer = zeros.index(min(zeros))
result = img[layer].count('1') * img[layer].count('2')

print(f"Result is: {result}")