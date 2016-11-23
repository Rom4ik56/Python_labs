from PIL import Image, ImageDraw

image = Image.open(r'C:\Users\jekov\Desktop\lab3\test.jpg')
ch_image = Image.open(r'C:\Users\jekov\Desktop\lab3\test.jpg')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()

level = int(input("Введите уровень яркости (от 0 до 255)"))

for i in range(width):
    for j in range(height):
        a = pix[i, j][0]
        b = pix[i, j][1]
        c = pix[i, j][2]
        S = a + b + c
        if (S > (((255 + level) // 2) * 3)):
            a, b, c = 255, 255, 255
        else:
            a, b, c = 0, 0, 0
        draw.point((i, j), (a, b, c))

#image.save(r'C:\Users\jekov\Desktop\lab3\test_bw1.jpg', "JPEG")
image.show()
