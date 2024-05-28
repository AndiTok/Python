def callLimit(limit: int):
    '''take an argument of call limit &
    returns a reference to the callLimiter function'''
    count = 0

    def callLimiter(function):
        '''takes another funtion as an argument &
        returns a reference to the limit_function function.'''
        def limit_function(*args, **kwds):
            '''returns the result of calling the function with
            the provided arguments, or None if the call limit is reached.'''
            nonlocal count
            if count < limit:
                count += 1
                # function(*args, **kwds)
                return function(*args, **kwds)
            elif count == limit:
                print("Error:", function, "call too many time")
        return limit_function
    return callLimiter
