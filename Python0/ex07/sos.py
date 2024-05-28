import sys as p


def main():
    sos()
    # print(sos.__doc__)


def sos():
    '''
    a program that takes a string as an argument and encodes it into Morse Code
    '''
    assert len(p.argv) == 2, "the arguments are bad"
    tmp = p.argv[1].upper()
    for char in tmp:
        if not (char.isalnum() or char == ' '):
            raise AssertionError("The arguments are bad")
    # print (tmp)
    NESTED_MORSE = {
        " ": "/ ", "A": ".-", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ", "I": ".. ",
        "J": ".--- ", "K": "-.- ", "L": ".-.. ", "M": "-- ", "N": "-. ",
        "O": "--- ", "P": ".--. ", "Q": "--.- ", "R": ".-. ", "S": "... ",
        "T": "- ", "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ", "0": "----- ", "1": ".---- ",
        "2": "..---", "3": "...--", "4": "....- ", "5": "..... ",
        "6": "-.... ", "7": "--... ", "8": "---.. ", "9": "----. "}

    output = ''
    for char in tmp:
        if char in NESTED_MORSE:
            output += NESTED_MORSE[char]
    output = output.rstrip()
    print(output)


if __name__ == "__main__":
    main()

# Examine the source code of program.
# Make sure it follows the following restrictions:

# The program use a dictionary.
# The program use AssertionError for the error management
# Carry out at least the following tests to try to stress the error management:

# Test the program without arguments, with more 1 arguments
# Test the program with special character '$', '@' ...
# Expected outputs:

# python sos.py 'SOS' | cat -e
# ... --- ...$
