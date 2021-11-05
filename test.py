from PIL import Image
from collections import Counter
img=Image.open('c1.png')
pix=[]
width,height=img.size
for i in range(0,width):
    for j in range(0,height):
        r, g, b,a = img.getpixel((1, 1))
        pix.append((r,g,b))
data = Counter(pix)
print(data.most_common(1)[0][0])
