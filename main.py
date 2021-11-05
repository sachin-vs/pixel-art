
from PIL import Image
from collections import Counter

#open image
img= Image.open('c1.png')

def pixelate(pix_list):
    initial_x=0
    initial_y=0
    pix=[]
    for i in pix_list:
        for j in range(initial_x,pix_list[0]):
            for k in range(initial_y,pix_list[1]):
              r, g, b,a = img.getpixel((1, 1))
              pix.append((r,g,b))  
        data = Counter(pix)
        print(data.most_common(1)[0][0])

    pass
def grid(img,m,n):
    width,height=img.size
    m_gradient=round(width/m)
    n_gradient=round(height/n)
    pix_list=[]
    for i in range(m_gradient,width+m_gradient,m_gradient):
        for j in range(n_gradient,height+n_gradient,n_gradient):
            pix_list.append([i,j])
    return pixelate(pix_list)
    #return pix_list[0][0]


print(grid(img,100,100))