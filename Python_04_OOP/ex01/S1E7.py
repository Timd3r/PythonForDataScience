from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family"""

    def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Baratheon", eyes: str = "brown", hairs: str = "dark"):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def die(self):
        """Your docstring for Method"""
        super().die()

    def __repr__(self):
        """Your docstring for Method"""
        out = f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return out

    def __str__(self):
        """Your docstring for Method"""
        out = f" Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return out


class Lannister(Character):
    """Representing the Lannister family"""

    def __init__(self, first_name: str, is_alive: bool = True, family_name: str = "Lannister", eyes: str = "blue", hairs: str = "light"):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def create_lannister(first_name: str, is_alive: bool = True):
        return Lannister(first_name, is_alive)

    def die(self):
        return super().die()

    def __repr__(self):
        """Your docstring for Method"""
        out = f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return out

    def __str__(self):
        """Your docstring for Method"""
        out = f" Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
        return out
