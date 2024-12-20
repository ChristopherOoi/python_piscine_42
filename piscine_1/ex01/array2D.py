from numpy import shape


def slice_me(family: list, start: int, end: int) -> list:
    """
    this function slices a list
    """
    if type(family) is not list:
        raise TypeError("The input is not a list")
    if type(start) is not int or type(end) is not int:
        raise TypeError("The input is not an integer")
    types = [type(item) for item in family]
    if len(set(types)) != 1:
        raise ValueError("The input is not a 2D list")
    if types[0] is list:
        shapes = [shape(item) for item in family]
        if len(set(shapes)) != 1:
            raise ValueError("The input is not a 2D list")
    print(f"My shape is : {shape(family)}")
    print(f"My new shape is : {shape(family[start:end])}")
    return family[start:end]


if __name__ == "__main__":
    try:
        family = ["John", "Doe", "Jane", "Doe", "Jenny", "Doe"]
        start = 1
        end = 5
        print(slice_me(family, start, end))
        family = [[1.80, 78.4], [2.15, 1.99, 100], [2.10, 98.5], [1.88, 75.2]]
        print(slice_me(family, 0, 2))
        print(slice_me(family, 1, -2))
    except Exception as e:
        print("error", e)
