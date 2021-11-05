
from PIL import Image
#open image
img= Image.open('c1.png')

def pixelate(pix_list):
    initial_x=0
    initial_y=0
    for i in pix_list:
        for j in range(initial_x,pix_list[0]):
            for k in range(initial_y,pix_list[1]):
                pass
    pass
def grid(img,m,n):
    width,height=img.size
    m_gradient=round(width/m)
    n_gradient=round(height/n)
    pix_list=[]
    for i in range(m_gradient,width+m_gradient,m_gradient):
        for j in range(n_gradient,height+n_gradient,n_gradient):
            pix_list.append([i,j])
    return pix_list


print(grid(img,100,100))