from numpy import square, divide


def give_bmi(
    height: list[int | float],
    weight: list[int | float],
) -> list[float]:
    """
    This function uses the formula to calculate the BMI of a person.
    :param height: list of height of a person in meters
    :param weight: list of weight of a person in kilograms
    """
    if type(height) is not list or type(weight) is not list:
        raise ValueError("The height and weight should be a list")
    if len(height) != len(weight):
        raise ValueError("The height and weight should have the same length")
    for item in height:
        if type(item) not in [int, float]:
            raise ValueError("The height should be a number")
        else:
            if item <= 0:
                raise ValueError("The height should be a positive number")
    for item in weight:
        if type(item) not in [int, float]:
            raise ValueError("The weight should be a number")
        else:
            if item <= 0:
                raise ValueError("The weight should be a positive number")
    return divide(weight, square(height)).tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    This function checks if the BMI of a person is above a certain limit.
    :param bmi: list of BMI of a person
    :param limit: the limit of BMI
    """
    if type(bmi) is not list:
        raise ValueError("The BMI should be a list")
    for item in bmi:
        if type(item) not in [int, float]:
            raise ValueError("The BMI should be a number")
        else:
            if item <= 0:
                raise ValueError("The BMI should be a positive number")
    if type(limit) is not int:
        raise ValueError("The limit should be an integer")
    return [True if i > limit else False for i in bmi]


if __name__ == "__main__":
    try:
        height = [1.75, 1.80, 1.65]
        weight = [70, 80, 60]
        bmi = give_bmi(height, weight)
        print(bmi)
        print(apply_limit(bmi, 25))
        print(give_bmi([1.75, 1.80, 1.65], [70, 80, "60"]))
    except ValueError as e:
        print(e)
