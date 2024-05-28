from load_image import ft_load
from PIL import Image
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

arr = ft_load("animal.jpeg")
print(arr)
arr = arr[100:500, 455:855]
img = Image.fromarray(arr)
# arr.show()
# input("Press ENTER to exit") # pause
# img = img.crop((0,0,400,400))
# img = img.crop((455,100,855,500))
img = img.convert("L")
# img.show()
# img = img.rotate(90)
# img = img.transpose(Image.FLIP_TOP_BOTTOM)
plt.gray()
plt.imshow(img)
plt.show()

arr = np.array(img)
arr = arr.reshape(400, 400, 1)
# arr = arr[100:500,455:855]
# arr = arr[100:500,-575:-175]
print("New shape after slicing:", arr.shape, end=' ')
tmp = arr.reshape(400, 400)
print("or", tmp.shape)
print(arr)


# grey_sacle = 0.299 ∙ Red + 0.587 ∙ Green + 0.114 ∙ Blue
# grey_scale = (R+G+B)/3

# im = Image.open("animal.jpeg")
# input("Press ENTER to exit") # pause
# im.show()
# input("Press ENTER to exit") # pause
# left = 155
# top = 65
# right = 360
# bottom = 270
# im1 = im.crop((left, top, right, bottom))
# im1.show()
# input("Press ENTER to exit") # pause
