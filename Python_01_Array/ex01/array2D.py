def slice_me(family: list, start: int, end: int) -> list:
    """
    Function that takes as parameters a 2D array,
    prints its shape, and returns a
    truncated version of the array based on
    the provided start and end arguments.
    """
    try:
        if type(family) is not list:
            raise AssertionError("Invalid input types.")
        if type(start) is not int or type(end) is not int:
            raise AssertionError("Invalid input types.")
        for row in family:
            if type(row) is not list:
                raise AssertionError("Invalid input types.")
            if len(row) != len(family[0]):
                raise AssertionError("All rows must have the same length.")
        print(f"My shape is : ({len(family)}, {len(family[0])})")
        print("My new shape is : ", end="")
        print(f"({len(family[start:end])}, {len(family[0])})")
        return family[start:end]
    except AssertionError as error:
        print(f"AssertionError: {error}")
