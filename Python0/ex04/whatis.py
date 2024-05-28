import sys as p

if len(p.argv) == 1:
    print("")
    exit()
assert len(p.argv) == 2, ": is more than one argument is provided"
tmp = p.argv[1]
# assert tmp is ValueError, ": argument is not an integer"
if tmp[0] == '-' or tmp[0] == '+':
    assert tmp[1:].isdigit(), ": argument is not an integer"
elif tmp[0].isdigit():
    assert tmp.isdigit(), ": argument is not an integer"

# assert ((p.argv[1].isnumeric())), ": argument is not an integer"

# if len(p.argv) == 2:
# 	if p.argv[1] == True and p.argv[1].isdigit()):
# 		input = p.args[1]
# 		print ('input set')
# 	else:
# 		print ('Error')

try:
    num = int(p.argv[1])
    # print(type(num))
    if num % 2 == 1:
        print("I'm Odd")
    elif num % 2 == 0:
        print("I'm Even")
except ValueError:
    print("Assertion Error: argument is not an integer")

# $> python whatis.py 28
# I'm Even.
# $>
# $> python whatis.py -7
# I'm Odd.
# $>
# $> python whatis.py
# $>
# $> python whatis.py 0
# I'm Even.
# $>
# $> python whatis.py "Hola!"
# AssertionError: argument is not an integer
# $>
# $> python whatis.py 42 42
# AssertionError: more than one argument are provided
# $>
