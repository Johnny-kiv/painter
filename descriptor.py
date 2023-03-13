import numpy as np
from PIL import Image
def translate_image(fileout,color1,color2,color3):
    file = open(fileout,"w")
    img = Image.open("./imgs/img.jpg")
    mas = np.array(img).tolist()
    for line in mas:
        for pixel in line:
            res = str(pixel[color1])+" "+str(pixel[color2])+" "+str(pixel[color3])+"|"
            file.write(res)
        file.write("\n")
translate_image("descriptor.txt",0,1,2)