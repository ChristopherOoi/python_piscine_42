from abc import ABC, abstractmethod


class Character(ABC):
    """
    Character abstract class.
    """

    @abstractmethod
    def __init__(self, name: str, alive: bool = True):
        """
        Initialize the character with a name.
        """
        self.first_name = name
        self.is_alive = alive

    def die(self):
        """
        Mark the character as dead.
        """
        self.is_alive = False


class Stark(Character):
    """
    Stark class, inherits from Character.
    """

    def __init__(self, name: str, alive: bool = True):
        """
        Initialize the Stark character with a name and alive status.
        """
        super().__init__(name, alive)
