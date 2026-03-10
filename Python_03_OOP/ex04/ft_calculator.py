class calculator:
    """A calculator class that performs various vector operations."""

    def __init__(self, values: list[float] = None) -> None:
        """Initialize the calculator."""
        if values is None:
            raise ValueError("Values must be provided for the calculator.")
        self.values = values

    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Calculate the dot product of two vectors."""
        output = []
        if (len(V1) != len(V2)):
            raise ValueError("Vectors must be of the same length.")
        for i in range(len(V1)):
            output.append(V1[i] * V2[i])
        for i in range(1, len(output)):
            output[0] += output[i]
        print(f"Dot product is: {output[0]}")
        # out = numpy.dot(V1, V2)
        # print(out)

    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Add two vectors."""
        if (len(V1) != len(V2)):
            raise ValueError("Vectors must be of the same length.")
        output = []
        for i in range(len(V1)):
            output.append(V1[i] + V2[i])
        print(f"Add Vector is: {output}")
        # out = numpy.add(V1, V2)
        # print(out)

    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Subtract two vectors."""
        if (len(V1) != len(V2)):
            raise ValueError("Vectors must be of the same length.")
        output = []
        for i in range(len(V1)):
            output.append(V1[i] - V2[i])
        print(f"Sous Vector is: {output}")
        # out = numpy.subtract(V1, V2)
        # print(out)
