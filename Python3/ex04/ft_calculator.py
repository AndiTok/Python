class calculator:
    # def __init__(self, a, b):
    #     self.V1 = a
    #     self.V2 = b

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        output = sum(a * b for a, b in zip(V1, V2))
        print("Dot Product is:", output)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        output = [float(a + b) for a, b in zip(V1, V2)]
        print("Add Vector is :", output)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        output = []
        for (a, b) in zip(V1, V2):
            output.append(float(a - b))
        print("Sous Vector is:", output)

# @staticmethod: allows user to define a method that can be called 
# on the class itself without needing an instance of the class. 
# class does not need def __init__() aka constructor

# @classmethod: used for creating class methods/def funtionss, 
# and it takes cls as its first parameter. 
# Class methods can be called on the class itself 
# and are often used for factory methods or 
# methods that operate on class-level attributes.
# sub-calss of a class

# @property: it defines a "getter method" for an attribute 
# and allows user to access the attribute like an attribute itself, 
# without needing parentheses. -> () 
# A getter method decorated with @property can be called without parentheses, 
# and it's commonly used to implement read-only properties.

# WITH @getattr , @setattr
# class MyClass:
#     def __init__(self):
#         self._value = 0

#     @property/@getattr
#     def value(self):
#         return self._value

#     @setattr
#     def value(self, new_value):
#         if new_value >= 0:
#             self._value = new_value
#         else:
#             print("Value must be non-negative.")

# # Usage
# obj = MyClass()

# # Using the getter without parentheses
# print(obj.value)  # Accesses the value attribute

# # Using the setter to change the attribute's value
# obj.value = 42  # Calls the setter to change the value

# WITHOUT @getattr , @setattr
# class MyClass:
#     def __init__(self):
#         self._value = 0

#     def get_value(self):
#         return self._value

#     def set_value(self, new_value):
#         if new_value >= 0:
#             self._value = new_value
#         else:
#             print("Value must be non-negative.")

#     # You can also define a property method to access the attribute
#     value = property(get_value, set_value)

# # Usage
# obj = MyClass()

# # using basic funtion
# print(obj.get_value())  # Accesses the value attribute with parentheses

# # using basic function
# obj.set_value(42)  # Calls the setter to change the value
