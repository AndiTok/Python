from load_image import ft_load
from PIL import Image
# from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import numpy as np


def zoom(input: str):
    '''
this program takes in a .jpg or .jpeg file
from the same directory which then
slice/crop/zoom to a spesific spot in an image
and apply grey filter on the image
    '''
    arr = ft_load(input)
    print(arr)
    arr = arr[100:500, 450:850]

    img = Image.fromarray(arr)
    img = img.convert("L")

    plt.gray()
    plt.imshow(img)

    arr = np.array(img)
    arr = arr.reshape(400, 400, 1)
    print("New shape after slicing:", arr.shape, end=' ')
    tmp = arr.reshape(400, 400)
    print("or", tmp.shape)
    print(arr)

    return (plt.show())


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


def main():
    zoom("animal.jpeg")
    print(zoom.__doc__)


if __name__ == "__main__":
    main()
