import sys as p
from ft_filter import ft_filter
# from .py file import function


def main():
    filterstring()
    # print(filterstring.__doc__)


def filterstring():
    '''
This funtion takes in 2 argument in order
1st being a string and 2nd being numbers
Strings do not contain any special characters
Number being digits 0-9 only
it output a list with words greater than 2nd arg
    '''
    # if len(p.argv) != 3:
    #     raise AssertionError ("the arguments are bad")
    assert len(p.argv) == 3, "the arguments are bad"
    if type(p.argv[1]) is not str:
        raise AssertionError("the arguments are bad")
    if not p.argv[2].isdigit():
        raise AssertionError("the arguments are bad")
    if not p.argv[1].isprintable():
        raise AssertionError("the arguments are bad")

    sc = """!"#$%&'()*+,-./:;<=>?@[]^`{|}~"""
    for char in p.argv[1]:
        if char in sc:
            raise AssertionError("the arguments are bad")

    p1 = p.argv[1].split()
    p2 = int(p.argv[2])

    # ft = lambda item: len(item) > p2
    # lamda funtion returns true !!norm not allow
    output = ft_filter(lambda item: len(item) > p2, p1)
    # holds lazy generated format
    output = [item for item in output]
    # list comprehention

    print(output)
    # return(output)
    # print(list(output))
    # return(list(output))


if __name__ == "__main__":
    main()


# python filterwords.py 'A robot may not injure a human being or through
# inaction allow a human being to come to harm' 5

# ['injure', 'through', 'inaction']
