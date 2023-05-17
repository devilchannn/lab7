from PIL import Image, ImageFilter

def lab1():
    image = Image.open('mishka.jpg')
    image.show()

    w, h = image.size
    f = image.format
    m = image.mode

    print('Ширина:', w)
    print('Высота:', h)
    print('Формат:', f)
    print('Цветовая модель:', m)

def lab2():
    image = Image.open('mishka.jpg')
    newimage = image.resize((image.width//3, image.height//3))
    newimage.save('remishka.jpg')

    conimage = image.transpose(Image.FLIP_LEFT_RIGHT)
    conimage.save('flipmishka.jpg')
    conimage = image.transpose(Image.FLIP_TOP_BOTTOM)
    conimage.save('mishkaflip.jpg')

def lab3():
    images = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    for file in images:
        image = Image.open(file)
        newimg = image.filter(ImageFilter.CONTOUR)
        newimg.show()
        newimg.save('new' + file)

def lab4():
    image = Image.open('watermark.jpg')
    newimg = image.resize((image.width // 3, image.height // 3))

    imge = Image.open('mishka.jpg')
    imge.paste(newimg)
    imge.save('watermark1.png')