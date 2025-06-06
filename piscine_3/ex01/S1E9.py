from abc import ABC, abstractmethod


class Character(ABC):
    """
    Character abstract class.
    """

    @abstractmethod
    def __init__(
        self,
        first_name: str,
        is_alive: bool,
        family_name: str,
        eyes: str,
        hairs: str,
    ):
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = family_name
        self.eyes = eyes
        self.hairs = hairs

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def die(self):
        """
        Method to mark the character as dead.
        """
        self.is_alive = False
