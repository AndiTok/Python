from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


arr = ft_load("animal.jpeg")
arr = arr[100:500, 450:850]
print(arr)
img = Image.fromarray(arr)
img = img.convert("L")
arr = np.array(img)
arr = arr.reshape(400, 400, 1)

print("The shape of image is:", arr.shape, end=' ')
tmp = arr.reshape(400, 400)
print("or", tmp.shape)
# print(arr.size)
print(arr)
print("New shape after transpose:", tmp.shape)
tmp = arr.reshape(400, 400)
print(tmp)
tmp = tmp.rotate(90)
tmp = tmp.transpose(Image.FLIP_TOP_BOTTOM)
plt.gray()
plt.imshow(tmp)
plt.show()
# https://realpython.com/image-processing-with-the-python-pillow-library/
# originally 0 1 2 <- H W RGB
# arr =np.transpose(arr, (1, 0, 2) <- W H RGB
# inverse inversing the row
# arr = arr[::-1]
