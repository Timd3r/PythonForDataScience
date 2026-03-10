from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """King class inherits from both Baratheon and Lannister classes."""

    def __init__(self, first_name, is_alive=True,
                 family="Baratheon", eyes="brown",
                 hairs="dark"):
        """
        Initialize the King class with attributes from both parent classes.
        """
        super().__init__(first_name, is_alive, family, eyes, hairs)

    def set_eyes(self, eyes):
        """Set the eye color of the King."""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set the hair color of the King."""
        self.hairs = hairs

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.hairs
