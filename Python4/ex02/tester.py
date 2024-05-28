from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()

# @callLimit(0)
# def h():
#     print("h()")


# @callLimit(2)
# def j():
#     print("j()")


# @callLimit(1)
# def k():
#     print("k()")


# for i in range(2):
#     h()
#     j()
#     k()

# $> python tester.py
# Error: <function h at 0x7fb993152f70> call too many times j()
# k()
# Error: <function h at 0x7fb993152f70> call too many times j()
# Error: <function k at 0x7fb9930f01f0> call too many times
