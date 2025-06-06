from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    make a king
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        Baratheon.__init__(self, first_name, is_alive)

    def set_eyes(self, color: str):
        """
        change eyes
        """
        self.eyes = color

    def get_eyes(self) -> str:
        """
        get eyes
        """
        return self.eyes

    def set_hairs(self, color: str):
        """
        change hairs
        """
        self.hairs = color

    def get_hairs(self) -> str:
        """
        get hairs
        """
        return self.hairs
