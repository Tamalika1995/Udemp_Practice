from PIL import Image,ImageFilter
img=Image.open(r"C:\Users\614785.old\PycharmProjects\Udemp_Practice\Image/model.jpg")
im1=img.resize((400,200))
im1.save('model1.png')
im1.show()
img.thumbnail((400,200))
img.save('model2.png')
img.show()

