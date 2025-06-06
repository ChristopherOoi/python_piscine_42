class calculator:
    """
    make a calc
    """

    def __init__(self, nums: list):
        self.nums = nums

    def __add__(self, num: int) -> None:
        """
        add num to items in nums
        """
        self.nums = [x + num for x in self.nums]
        print(self.nums)

    def __mul__(self, num: int) -> None:
        """
        multiply items in nums by num
        """
        self.nums = [x * num for x in self.nums]
        print(self.nums)

    def __sub__(self, num: int) -> None:
        """
        subtract num from items in nums
        """
        self.nums = [x - num for x in self.nums]
        print(self.nums)

    def __truediv__(self, num: int) -> None:
        """
        divide items in nums by num
        """
        if num == 0:
            raise ValueError("Cannot divide by zero.")
        self.nums = [x / num for x in self.nums]
        print(self.nums)


if __name__ == "__main__":
    v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v1 + 5
    print("---")
    v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
    v2 * 5
    print("---")
    v3 = calculator([10.0, 15.0, 20.0])
    v3 - 5
    v3 / 5
