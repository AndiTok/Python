# from typing import Any
# def ft_statistics(*args: Any, **kwargs: Any) -> None:
#     pass

def ft_statistics(*args, **kwargs) -> None:
    '''a funtion that does mean, median , quartile (Q1 & Q7),
    std deviation & variance according to **kwargs'''
    # try:
    if ("toto" in kwargs or "mean" in kwargs.values()) and len(args) != 0:
        # print(kwargs["toto"])
        print("mean :", sum(args)/len(args))

    if ("tutu" in kwargs or "median" in kwargs.values()) and len(args) != 0:
        # print(kwargs["tutu"])
        sort = sorted(args)
        n = len(sort)
        if n % 2 == 1:  # odd
            median = (n + 1) / 2
            print(("median :"), sort[int(median)])
        else:
            a = n / 2
            b = (n / 2) + 1
            median = (sort[int(a - 1)] + sort[int(b - 1)]) / 2
            print(("median :"), median)

    if ("tata" in kwargs or "quartile" in kwargs.values()) and len(args) != 0:
        # print(kwargs["tata"])
        sort = sorted(args)
        n = len(sort)
        q1 = round(0.25 * (n + 1))
        q3 = round(0.75 * (n + 1))
        # print(q1, q3)
        output = []
        output.append(sort[int(q1 - 1)])
        output.append(sort[int(q3 - 1)])
        output = [float(i) for i in output]
        print("quartile :", output)

    if ("hello" in kwargs or "std" in kwargs.values()) and len(args) != 0:
        mean = sum(args)/len(args)
        # print(mean)
        sort = sorted(args)
        sort = [i - mean for i in sort]
        sort = [i * i for i in sort]
        # print(sort)
        total = sum(sort)
        # print(total)
        var = total / (len(args))
        # print(var)
        sd = var ** 0.5
        print("std :", sd)

    if ("world" in kwargs or "var" in kwargs.values()) and len(args) != 0:
        mean = sum(args)/len(args)
        # print(mean)
        sort = sorted(args)
        sort = [i - mean for i in sort]
        sort = [i * i for i in sort]
        # print(sort)
        total = sum(sort)
        # print(total)
        var = total / (len(args))
        print("var :", var)

    if len(args) == 0:
        for i in kwargs:
            print("ERROR")
# except Exception:
#     print("ERROR")

# should loop trough the kwargs at start to get keys and or vlaue
# according to math do funtion
