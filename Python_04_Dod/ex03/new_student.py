import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a unique ID for a student.
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


def generate_login(name: str, surname: str) -> str:
    """
    Generate a login for a student based on their name and surname.
    The login is the first letter of the name (capitalized)
    followed by the surname in lowercase.
    """
    return name[0].upper() + surname.lower()


@dataclass
class Student:
    """A class representing a student with a
    name, surname, active status, and a unique ID."""
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    login: str = field(init=False)
    id: str = field(init=False)

    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname
        self.active = True
        self.login = generate_login(name, surname)
        self.id = generate_id()
