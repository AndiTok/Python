from PIL import Image
import numpy as np


def ft_load(path: str) -> list:
    '''
    a function that loads an image, prints its format,
    and its pixels content in RGB format.
    accepts JPEG and JPG format only
    '''
    # assert
    img = Image.open(path)
    tmp = img.format
    assert tmp == 'JPEG' or tmp == 'JPG', (".jpg & .jpeg only")
    # assert tmp.lower() in ('jpeg', 'jpg'), (".jpg & .jpeg only")??
    # img_rgb = img.convert('RGB')
    # img_array = np.array(img_rgb)
    img_array = np.array(img)
    print("The shape of image is:", img_array.shape)
    return img_array

#  pip install pillow
#  https://saturncloud.io/blog/how-to-convert-rgb-pil-image-to-numpy-array-with-3-channels-a-comprehensive-guide/
