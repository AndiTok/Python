import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
     -> list[int | float]:
    '''
    return a BMI list vlaue with height list & weight list
    '''
    assert len(height) == len(weight), (":not same size")
    # assert isinstance(height, list) and isinstance(weight, list), \
    # ":not same data type"
    assert type(height) is list and type(weight) is list, (":not same type")
    assert all(isinstance(h, (int, float)) for h in height), (":number only")
    assert all(isinstance(w, (int, float)) for w in weight), (":number only")

    h_arr = np.array(height)
    w_arr = np.array(weight)
    bmi = w_arr / (h_arr ** 2)
    return list(bmi)

    # output=[]
    # for i in range(len(height)):
    #     bmi = weight[i] / (height[i] * height[i])
    #     output.append(bmi)
    # return output


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    ''''
    returns True if BMI value is > limit
    returns false if BMI vlaue is =< limit
    '''
    assert all(isinstance(i, (int, float)) for i in bmi), (":number only")
    assert type(bmi) is list, (":not list type")
    assert type(limit) is int, (":not int type")
    i = 0
    output = []
    while i < len(bmi):
        if bmi[i] > limit:
            output.append('True')
        else:
            output.append('False')
        i += 1
    return output
