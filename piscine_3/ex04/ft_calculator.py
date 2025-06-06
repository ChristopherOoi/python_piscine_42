class calculator:
    """
    calculator
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        calculate dot product of two vectors
        """
        print(f"Dot product is: {sum(v1 * v2 for v1, v2 in zip(V1, V2))}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        element-wise addition for two vectors
        """
        print(f"Add Vector is: {[float(v1 + v2) for v1, v2 in zip(V1, V2)]}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        element-wise subtraction for two vectors
        """
        print(f"Sous Vector is: {[float(v1 - v2) for v1, v2 in zip(V1, V2)]}")


if __name__ == "__main__":
    a = [5, 10, 2]
    b = [2, 4, 3]
    calculator.dotproduct(a, b)
    calculator.add_vec(a, b)
    calculator.sous_vec(a, b)
