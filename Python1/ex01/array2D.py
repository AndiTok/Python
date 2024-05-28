import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    prints its shape, and returns a truncated version of
    the array based on the provided start and end arguments
    '''
    assert isinstance(family, list), (":not a list")
    assert all(isinstance(f, list) for f in family), (":not a list")
    assert isinstance(start, int), (":not int")
    assert isinstance(end, int), (":not int")

    size = len(family[0])
    for row in family:
        if len(row) != size:
            raise AssertionError("sublist not even")

    arr = np.array(family)
    assert len(arr.shape) == 2, (":not 2D")

    print("My shape is :", arr.shape)
    arr = arr[start:end]
    print("My new shape is :", arr.shape)
    arr = arr.tolist()
    return arr
