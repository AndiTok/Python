# def cube(x: int | float) -> int | float:
#     """Returns the cube of x"""
#     return (x * x * x)


def square(x: int | float) -> int | float:
    ''' returns square of argument'''
    return x ** 2


def pow(x: int | float) -> int | float:
    '''returns ecponentiation of argument'''
    return x ** x


#  make use of count
def outer(x: int | float, function) -> object:
    '''a funtion that takes in an argument & a function'''
    count = 0

    def inner() -> float:
        '''return the result of argument calculation'''
        nonlocal count
        count += 1
        y = x
        for i in range(count):  #
            y = function(y)
        return y
    return inner

# did not make use of count
# def outer(x: int | float, function) -> object:
#     count = 0

# def inner() -> float:
#         nonlocal count
#         nonlocal x
#         count += 1  #
#         x = function(x)
#         return x
#     return inner
