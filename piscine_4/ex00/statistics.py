from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    You must take in *args a quantity of unknown number and make the Mean,
    Median, Quartile (25% and 75%), Standard Deviation and Variance
    according to the **kwargs ask.
    """

    if not all(isinstance(arg, (int, float)) for arg in args):
        print("ERROR")
        return
    if len(args) < 2:
        print("ERROR")
        return

    mean = sum(args) / len(args)
    sorted_args = sorted(args)
    mid = len(sorted_args) // 2
    median = (sorted_args[mid] + sorted_args[~mid]) / 2
    q1 = sorted_args[len(sorted_args) // 4]
    q3 = sorted_args[3 * len(sorted_args) // 4]
    variance = sum((x - mean) ** 2 for x in args) / (len(args) - 1)
    std_dev = variance**0.5

    for _, val in kwargs.items():
        if val == "mean":
            print(f"mean : {mean}")
        if val == "median":
            print(f"median : {median}")
        if val == "quartile":
            print(f"quartile : {[q1, q3]}")
        if val == "std":
            print(f"std : {std_dev}")
        if val == "var":
            print(f"var : {variance}")
