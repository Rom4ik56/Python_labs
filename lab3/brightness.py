from PIL import Image, ImageDraw

image = Image.open(r'C:\Users\jekov\Desktop\lab3\test.jpg')
ch_image = Image.open(r'C:\Users\jekov\Desktop\lab3\test.jpg')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

level =int(input("Введите уровень яркости (от -100 до 100)"))
for i in range(width):
        for j in range(height):
            r = pix[i, j][0] + level
            g = pix[i, j][1] + level
            b = pix[i, j][2] + level
            if r < 0:
                r = 0
            elif r > 255:
                r = 255

            if g < 0:
                g = 0
            elif g > 255:
                g = 255

            if b < 0:
                b = 0
            elif b > 255:
                b = 255
            draw.point((i, j), (r,g,b))

#image.save(r'C:\Users\jekov\Desktop\lab3\test_br.jpg', "JPEG")
image.show()