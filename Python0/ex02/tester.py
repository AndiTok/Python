from find_ft_type import all_thing_is_obj

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
print(all_thing_is_obj(10))

# all_thing_is_obj(ft_list)
# all_thing_is_obj(ft_tuple)
# all_thing_is_obj(ft_set)
# all_thing_is_obj(ft_dict)
# all_thing_is_obj("John")
# print(all_thing_is_obj(1.5))

# $> python tester.py
# List : <class 'list'>$
# Tuple : <class 'tuple'>$
# Set : <class 'set'>$
# Dict : <class 'dict'>$
# John is in the kitchen : <class 'str'>$
# Type not Found$
# 42$
