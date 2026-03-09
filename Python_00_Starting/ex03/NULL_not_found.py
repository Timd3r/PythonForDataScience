def NULL_not_found(object: any) -> int:
    val = type(object)
    if (object is None):
        print(f"Nothing: {object} {val}")
    elif (val is float and object != object):
        print(f"Cheese: {object} {val}")
    elif (val is int and object == 0):
        print(f"Zero: {object} : {val}")
    elif (val is str and object == ""):
        print(f"Empty: {object} {val}")
    elif (val is bool and object is False):
        print(f"Fake: {object} {val}")
    else:
        print("Type not Found")
    return 1
