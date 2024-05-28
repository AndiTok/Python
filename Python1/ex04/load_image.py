from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    '''
    a function that loads an image only
    and accepts JPEG and JPG format only
    '''
    img = Image.open(path)
    tmp = img.format
    assert tmp == 'JPEG' or tmp == 'JPG', (".jpg & .jpeg only")
    img_array = np.array(img)
    # print("The shape of image is:", img_array.shape)
    return img_array
