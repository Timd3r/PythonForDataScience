def all_thing_is_obj(object: any) -> int:
    val = type(object)
    if (val == list):
        print(f"List : {val}")
    elif (val == tuple):
        print(f"Tuple : {val}")
    elif (val == set):
        print(f"Set : {val}")
    elif (val == dict):
        print(f"Dict : {val}")
    elif (val == str):
        print(f"{object} is in the kitchen : {val}")
    else:
        print("Type not found")
    return 42
