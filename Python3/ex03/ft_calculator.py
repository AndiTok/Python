class calculator:
    def __init__(self, values):
        # if not isinstance(values, (list)):
        #     raise AssertionError ("must be a vector/1D,list")
        # for i in values:
        #     if not isinstance(i, (int, float)):
        #         raise AssertionError ("must be int or float")
        #     else:
        #         self.values = values
        self.values = values
        # print(type(values)) # Scalar (single numeric value)


# deep copy 
    def __add__(self, object) -> None: # __add__ = + , self = list/vector, object = nb
        # output = []
        # for i in self.values:
        #     result = i + object
        #     output.append(result)
        # print(output)
        for i in range(len(self.values)): # len = 5, range =[1,2,3,4,5]
            self.values[i] += object
        print(self.values)

    def __mul__(self, object) -> None:
        # output = []
        # for i in self.values:
        #         output.append(i * object)
        # print(output)
        for i, value in enumerate(self.values): # i as indexing, vlaue as the item in list
            self.values[i] = value * object
        print(self.values)


# directly modif the list + list comprehention
    def __sub__(self, object) -> None:
        # self.values = [i - object for i in self.values]
        # print(self.values)
        output = []
        for i in self.values:
            result = i - object
            output.append(result)
        self.values = output
        print(self.values)

    def __truediv__(self, object) -> None:
        # if object == 0:
        #     print("cannot be divisible by 0")
        #     return None
        # self.values = [i / object for i in self.values]
        # print(self.values)
        try:
            self.values = [i / object for i in self.values]
            print(self.values)
        except ZeroDivisionError:
            print("cannot be divisible by 0")