def ft_filter(f, i):
    """
    filter(function or None, iterable) --> filter object
    Return an iterator yielding those items of iterable for
    which function(item) is true.
    If function is None, return the items that are true.
    """
    if f:
        result = [item for item in i if f(i)]
    else:
        result = [item for item in i if item]
    return iter(result)
