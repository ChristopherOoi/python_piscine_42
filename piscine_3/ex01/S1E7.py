from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon character class inheriting from Character.
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(
            first_name,
            is_alive,
            "Baratheon",
            "brown",
            "dark",
        )

    def __str__(self):
        """
        Override base __str__ method to match pdf.
        """
        return super().__str__()

    def __repr__(self):
        """
        Override base __repr__ method to match pdf.
        """
        return super().__repr__()


class Lannister(Character):
    """
    Lannister character class inheriting from Character.
    """

    def __init__(self, first_name, is_alive=True):
        super().__init__(
            first_name,
            is_alive,
            "Lannister",
            "blue",
            "light",
        )

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Class method to create a Lannister character.
        """
        return cls(first_name, is_alive)

    def __str__(self):
        """
        Override base __str__ method to match pdf.
        """
        return super().__str__()

    def __repr__(self):
        """
        Override base __repr__ method to match pdf.
        """
        return super().__repr__()
