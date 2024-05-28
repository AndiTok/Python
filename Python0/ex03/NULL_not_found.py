def NULL_not_found(object: any) -> int:
    if type(object) is type(None):
        print("Nothing:", object, type(object))
    elif type(object) is type(42.42):
        print("Cheese:", object, type(object))
    elif type(object) is type(42):
        print("Zero:", object, type(object))
    elif type(object) is str and len(object) == 0:  # '' or object is "":
        print("Empty:", object, type(object))
    elif type(object) is bool:
        print("Fake:", object, type(object))
    else:
        print("Type not Found")
        return 1
    return 0
