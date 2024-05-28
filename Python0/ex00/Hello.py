ft_list = ["Hello", "tata!"]  # list [ ]
ft_tuple = ("Hello", "toto!")  # tuple ( ) *unchangable*
ft_set = {"Hello", "tutu!"}   # set { , } *unchangable BUT can add/remove
ft_dict = {"Hello": "titi!"}  # dict { : }

ft_list[1] = "World!"  # point to cell and modify

tmp_list = list(ft_tuple)  # conver tuple to list
tmp_list[1] = "KL!"  # modify like a list
ft_tuple = tuple(tmp_list)  # conver the list to tuple

ft_set.remove("tutu!")
# If the item to remove does not exist, remove() will raise an error.
# ft_set.discard("tutu!")
# If the item to remove does not exist, discard() will NOT raise an error.
ft_set.add("Malaysia!")
# sets are unordered meaning it may not be in correct sequence
# list & tuple are orderes
# as of 3.7 ordered but earlier version are unordered

ft_dict["Hello"] = "42KL!"
# ft_dict.update({"Hello":"42KL!"})
# update will either add or replace if found

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
