from typing import Any


def callLimit(limit: int):
    """Limits the number of times a function can be called."""
    count = 0

    def callLimiter(function):
        """Limits the number of times a function can be called."""

        def limit_function(*args: Any, **kwds: Any):
            """Limits the number of times a function can be called."""
            try:
                nonlocal count
                if count < limit:
                    count += 1
                    return function(*args, **kwds)
                else:
                    out = f"<function {function.__name__} "
                    out += f"at {hex(id(function))}> call too many times"
                    raise Exception(out)
            except Exception as e:
                print(f"Error: {e}")

        return limit_function

    return callLimiter
