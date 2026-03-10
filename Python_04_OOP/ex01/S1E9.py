from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class Character"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """initialize the character with a first name and an alive status"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Your docstring for die method"""
        self.is_alive = False


class Stark(Character):
    """Your docstring for Class"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Your docstring for Constructor"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Your docstring for Method"""
        super().die()
