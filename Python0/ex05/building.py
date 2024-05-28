import sys as p


def main():
    '''
Takes in a single string argument and displays
the sums characters, upper-case characters,
lower-case characters, punctuation characters,
digits and spaces.

Runs with either 1 or 0 parameter
with 0 parameter, will be promted to input a string
    '''
    if len(p.argv) > 2:
        raise AssertionError("more than one argument is provided")
    if len(p.argv) == 1:
        tmp = input("What is the text to count?\n")
        tmp += ' '
    if len(p.argv) == 2:
        tmp = p.argv[1]
    if not tmp.isprintable():
        raise AssertionError("invisbale characters")
    print("The text contains", len(tmp), "characters:")

    ul = 0
    ll = 0
    pm = 0
    s = 0
    d = 0
    # i = 0

    # while i < len(tmp):
    #     char = tmp[i]
    for char in tmp:
        if char.isupper():
            ul += 1
        elif char.islower():
            ll += 1
        elif char.isspace():
            s += 1
        elif char.isdigit():
            d += 1
        else:
            pm += 1

    print(f"{ul} uppercase letters")
    print(f"{ll} lowercase letters")
    print(f"{pm} punctuation marks")
    print(f"{s} spaces")
    print(f"{d} digits")


if __name__ == "__main__":
    main()
    print(main.__doc__)


# "Python 3.0, released in 2008, was a major revision that is not completely
# backward-compatible with earlier versions. Python 2 was discontinued with
# version 2.7.18 in 2020."
# The text contains 171 characters:
# 2 upper letters
# 121 lower letters
# 8 punctuation marks
# 25 spaces
# 15 digit

# $>python building.py
# What is the text to count?
# Hello World!
# The text contains 13 characters:
# 2 upper letters
# 8 lower letters
# 1 punctuation marks
# 2 spaces
# 0 digits

# $>python building.py "Hello" "World!"
# AssertionError: more than one argument are provided
