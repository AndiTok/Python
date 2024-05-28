from load_image import ft_load
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np


def rotate(input: str):
    '''
this program takes in a .jpg or .jpeg file
from the same directory which then
slice/crop/zoom to aspesific spot in an image
rotate digonally bottum left to top right
and apply grey filter on the image
    '''
    img = ft_load(str)
    img = img[100:500, 450:850]

    h, w, c, = img.shape
    t_img = np.empty((w, h, c), dtype=np.uint8)

    for i in range(w):
        for j in range(h):
            t_img[i, j, :] = img[j, i, :]

    t_img = Image.fromarray(t_img)
    t_img = t_img.convert("L")

    arr = np.array(t_img)
    arr = arr.reshape(400, 400, 1)
    print("The shape of image is:", arr.shape, end=' ')
    tmp = arr.reshape(400, 400)
    print("or", tmp.shape)
    print(arr)
    print("The shape after Transpose:", tmp.shape)
    print(tmp)

    plt.gray()
    plt.imshow(t_img)
    plt.show()

# https://en.m.wikipedia.org/wiki/Transpose


def main():
    rotate("animal.jpeg")
    print(rotate.__doc__)


if __name__ == "__main__":
    main()
