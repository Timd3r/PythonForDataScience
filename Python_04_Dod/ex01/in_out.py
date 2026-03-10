def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Returns the result of raising x to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Returns a function that applies
    the given function to a count variable."""
    count = x

    def inner() -> float:
        """Applies the given function to the count variable and updates it."""
        nonlocal count
        count = function(count)
        return count

    return inner
