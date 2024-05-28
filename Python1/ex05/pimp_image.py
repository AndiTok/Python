from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> np.array:

    '''Inverts the color of the image received'''
    print(array)
    # print("Inverts the color of the image received")
    # max_value = np.iinfo(array.dtype).max
    # print(max_value)
    inverted_array = 255 - array
    # array[:,:,0] = 255 - array[:,:,0]
    # array[:,:,1] = 255 - array[:,:,1]
    # array[:,:,2] = 255 - array[:,:,2]
    img = Image.fromarray(inverted_array)
    plt.imshow(img)
    plt.show()
    # img.show(img)
    print(inverted_array)
    return array


def ft_red(array) -> np.array:

    '''Red filter of the image received'''
    print(array)
    tmp = array.copy()
    # print("Red filter of the image received")
    # Set the green and blue color channels to 0
    tmp[:, :, 1] = 0  # Green channel
    tmp[:, :, 2] = 0  # Blue channel
    img = Image.fromarray(tmp)
    # plt.imshow(img)
    # plt.show()
    img.show(img)
    return array


def ft_green(array) -> np.array:

    '''Green filter of the image received'''
    print(array)
    tmp = array.copy()
    # print("Green filter of the image received")
    # Set the red and blue color channels to 0
    tmp[:, :, 0] = 0  # Red channel
    tmp[:, :, 2] = 0  # Blue channel
    img = Image.fromarray(tmp)
    # plt.imshow(img)
    # plt.show()
    img.show(img)
    return array


def ft_blue(array) -> np.array:

    '''Blue filter of the image received'''
    print(array)
    tmp = array.copy()
    # print("Blue filter of the image received")
    # Set the red and green color channels to 0
    tmp[:, :, 0] = 0  # Red channel
    tmp[:, :, 1] = 0  # Green channel
    img = Image.fromarray(tmp)
    # plt.imshow(img)
    # plt.show()
    img.show(img)
    return array


def ft_grey(array) -> np.array:

    '''Grey filter of the image received'''
    print(array)
    tmp = array.copy()
    # print("Grey filter of the image received")
    img = Image.fromarray(tmp)
    img = img.convert("L")
    # plt.imshow(img)
    # plt.show()
    img.show(img)
    return array
