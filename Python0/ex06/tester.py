from ft_filter import ft_filter


original = filter.__doc__
copy = ft_filter.__doc__
print(repr(original))  # see escape sequnce
print(repr(copy))  # see escape sequnce
print("---")
print("len :", len(original))  # check len
print("len :", len(copy))  # chekc len
print("---")
print(original)
print("---")
print(copy)  # output: docstring
print("---")
print(original == copy)  # output: True
