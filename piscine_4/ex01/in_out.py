def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x to the power of x."""
    return x**x


def outer(x: int | float, function) -> object:
    """
    returns function that applies given function to x
    repeatedly, increasing the number of applications each time.
    """
    count = 0

    def inner() -> float:
        nonlocal x, count
        for _ in range(count):
            x = function(x)
        count += 1
        return x

    return inner


if __name__ == "__main__":
    my_counter = outer(3, square)
    print(my_counter())
    print(my_counter())
    print(my_counter())
    print("---")
    another_counter = outer(1.5, pow)
    print(another_counter())
    print(another_counter())
    print(another_counter())
