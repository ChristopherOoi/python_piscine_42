from typing import Any

# any is not a valid type, and typing is required for Any


def all_thing_is_obj(object: Any) -> int:
    if object == None or type(object) == type(None):
        print("Type not found")
    else:
        typestring = type(object).__name__.capitalize()
        if typestring == "Str":
            typestring = object + " is in the kitchen"
        print(f"{typestring} : {type(object)}")
    return 42


if "__name__" == "__main__":
    pass
