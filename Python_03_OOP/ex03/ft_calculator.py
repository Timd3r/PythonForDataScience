class calculator:
    """
    A calculator that can perform basic arithmetic operations
    on a list of numbers.
    """

    def __init__(self, values):
        """Initialize the calculator with a list of values."""
        self.values = values

    def __add__(self, object) -> None:
        """Add a number to each value in the calculator."""
        self.values = [x + object for x in self.values]
        print(self.values)

    def __mul__(self, object) -> None:
        """Multiply each value in the calculator by a number."""
        self.values = [x * object for x in self.values]
        print(self.values)

    def __sub__(self, object) -> None:
        """Subtract a number from each value in the calculator."""
        self.values = [x - object for x in self.values]
        print(self.values)

    def __truediv__(self, object) -> None:
        """Divide each value in the calculator by a number."""
        self.values = [x / object for x in self.values]
        print(self.values)
