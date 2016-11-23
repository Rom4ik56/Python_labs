from PIL import Image, ImageDraw

image = Image.open(r'C:\Users\jekov\Desktop\lab3\test.jpg')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

level1 = int(input("Введите уровень красного канала (от 0 до 255)"))
level2 = int(input("Введите уровень зеленого канала (от 0 до 255)"))
level3 = int(input("Введите уровень синего канала (от 0 до 255)"))
for i in range(width):
        for j in range(height):

            r = pix[i, j][0] + level1
            g = pix[i, j][1] + level2
            b = pix[i, j][2] + level3
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