from PIL import Image,ImageFilter
with Image.open(r"C:\Users\614785.old\PycharmProjects\Udemp_Practice\Image/Dora.jpg") as im:
    print(im)
    print(im.format)
    print(im.size)
    print(im.mode)
    filtered_image1=im.filter(ImageFilter.BLUR)
    print(filtered_image1)
    filtered_image1.save('Blur.png','png')#imagefilter support png only
    filtered_image2 = im.filter(ImageFilter.SHARPEN)
    filtered_image2.save('SHARPEN1.png', 'png')
    filtered_image3 = im.convert('L')
    filtered_image3.save('grey.png', 'png')
    filtered_image4=filtered_image3.rotate(90)
    #filtered_image4.show()
    resize = filtered_image2.resize((150,150))
    resize.save('resize.png', 'png')
    box=(100,100,400,400)
    crop1 = filtered_image2.crop(box)
    crop1.save('crop.png', 'png')
    crop1.show()


    #print(dir(im))
