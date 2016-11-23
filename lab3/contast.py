from PIL import Image, ImageDraw, ImageEnhance

n = input("Введите уровень контраста: ")
image = Image.open(r'C:\Users\jekov\Desktop\lab3\test.jpg')
contrast = ImageEnhance.Contrast(image)
contrast.enhance(float(n)).show()
