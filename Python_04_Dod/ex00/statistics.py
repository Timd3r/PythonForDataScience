from typing import Any


def mean(data: list) -> float:
    """Calculate the mean of a list of numbers."""
    if not data:
        raise ValueError("Data list is empty.")
    total = 0
    for num in data:
        total += num
    return total / len(data)


def median(data: list) -> float:
    """Calculate the median of a list of numbers."""
    if not data:
        raise ValueError("Data list is empty.")
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


def quartile(data: list) -> list[float]:
    """Calculate the first and third quartiles of a list of numbers."""
    if not data:
        raise ValueError("Data list is empty.")

    s = sorted(data)
    n = len(s)
    q1 = float(s[n//4])
    q3 = float(s[(n*3)//4])
    return [float(q1), float(q3)]


def std(data: list) -> float:
    """Calculate the standard deviation of a list of numbers."""
    if not data:
        raise ValueError("Data list is empty.")
    return (var(data)) ** 0.5


def var(data: list) -> float:
    """Calculate the variance of a list of numbers."""
    if not data:
        raise ValueError("Data list is empty.")
    m = mean(data)
    total = 0
    n = len(data)
    for num in data:
        total += (num - m) ** 2
    return total / n


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate and print statistics based on
    provided data and requested statistics.
    """
    if not args:
        return
    if not kwargs:
        return
    try:
        data = list(args)
        stats_map = {
            "mean": mean,
            "median": median,
            "quartile": quartile,
            "std": std,
            "var": var
        }

        for value in kwargs.values():
            if value in stats_map:
                result = stats_map[value](data)
                print(f"{value} : {result}")
            else:
                print("ERROR")
    except Exception as e:
        print(f"Error processing data: {e}")
        return
