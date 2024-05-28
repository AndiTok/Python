def count_in_list(lst: list, word: str) -> int:
    '''return int number of arg2 word in arg1 list'''
    i = 0
    for item in lst:
        if word == item:
            i += 1
    return i
