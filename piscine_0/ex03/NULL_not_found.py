from typing import Any


def NULL_not_found(object: Any) -> int:
    # special cases
    if object is None:
        print(f"Nothing: {object} {type(object)}")
        return 0
    if object != object:
        print(f"Cheese: {object} {type(object)}")
        return 0
    # others
    if object:
        print("Type not Found")
        return 1
    types = {
        int: "Zero",
        str: "Empty",
        bool: "Fake",
    }
    print(f"{types[type(object)]}: {object} {type(object)}")
    return 0
