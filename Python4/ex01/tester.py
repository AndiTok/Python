from in_out import outer
from in_out import square
from in_out import pow
# from in_out import cube

my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())
# print("---")
# again_another_counter = outer(4, cube)
# print(again_another_counter())
# print(again_another_counter())
# print(again_another_counter())

# $> python tester.py 36.0
# 1296.0
# 1679616.0
# ---
# 2.1212505710975917 4.929279084950403 2599.697171916239 ---
# 64
# 262144
# 18014398509481984
