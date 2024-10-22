from sys import argv
from string import (
    ascii_lowercase,
    ascii_uppercase,
    digits,
    punctuation,
    whitespace,
    printable,
)


def main() -> None:
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        to_count = argv[1] if len(argv) == 2 else input()
        types = {
            "upper": 0,
            "lower": 0,
            "punctuation": 0,
            "spaces": 0,
            "digits": 0,
        }
        for char in to_count:
            assert char in printable, f"Invalid character: {char}"
            if char in ascii_uppercase:
                types["upper"] += 1
            elif char in ascii_lowercase:
                types["lower"] += 1
            elif char in punctuation:
                types["punctuation"] += 1
            elif char in whitespace:
                types["spaces"] += 1
            elif char in digits:
                types["digits"] += 1
        print(f"The text contains {len(to_count)} characters:")
        print(f"{types['upper']} upper letters")
        print(f"{types['lower']} lower letters")
        print(f"{types['punctuation']} punctuation marks")
        print(f"{types['spaces']} spaces")
        print(f"{types['digits']} digits")
    except AssertionError as e:
        print(e)
    return


if __name__ == "__main__":
    main()
