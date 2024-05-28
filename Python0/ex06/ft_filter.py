def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
# return (item for item in iterable if function(item))  #  1 liner code
# Convert iterable to a list usin list comprehention
    iterable = [item for item in iterable]
    if function is None:
        for item in iterable:
            if item:
                yield item
                #  yield from iterable #  0 is not outputed in filter()
    else:
        for item in iterable:
            if function(item):
                #  not using is True dues to something about "truthiness"
                yield item

#  list comprehention method below
#  return [item for item in iterable if function(item)]  #  1 liner code
# if function is None:
#         return [item for item in iterable if item]
#     else:
#         return [item for item in iterable if function(item)]

# if __name__ == "__main__":
# ages = [5, 12, 17, 18, 24, 32]  #  test

# def myFunc(x):
#   if x < 18:
#     return False
#   else:
#     return True

# adults = filter(myFunc, ages)
# print(adults)
# print(*adults)

#     print(filter.__doc__)
#     print(ft_filter.__doc__)
#     ft_filter()

#  filter(function or None, iterable) --> filter object
#  Return an iterator yielding those items of iterable for which function(item)
#  is true. If function is None, return the items that are true.
#
#  truthy (i.e., not equal to False, None, 0, an empty container, etc.)
#  falsy (e.g., False, None, 0, an empty container)
