def all_thing_is_obj(object: any) -> int:
    ClassType = type(object)

    if ClassType == list:
        print("List :", ClassType)
    elif ClassType == tuple:
        print("Tuple :", ClassType)
    elif ClassType == set:
        print("Set :", ClassType)
    elif ClassType == dict:
        print("Dict :", ClassType)
    elif ClassType == str:
        print(object, "is in the kitchen :", ClassType)
    else:
        print("Type not found")
    return 42
