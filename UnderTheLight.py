import math
from PIL import Image

try:
    path = input("Image File: ")
    path = path.replace("\"", "")

    image = Image.open(path)
    rgbImage = image.convert('RGBA')
    width, height = rgbImage.size

    def splotch(xOffset, yOffset, radius, rOffset, gOffset, bOffset):
        for x in range(width):
            for y in range(height):
                    distance = math.sqrt((x-xOffset)**2 + (y-yOffset)**2)
                    if distance >= radius: continue
                    r,g,b,a = rgbImage.getpixel((x,y))
                    rgbImage.putpixel((x,y), (r+rOffset, g+gOffset, b+bOffset))

    splotch(500, 500, 50, 50, 0, 0)
    rgbImage.save(path.replace(".png", "_output.png")) 

except Exception as ex:
    print(ex)
    input()