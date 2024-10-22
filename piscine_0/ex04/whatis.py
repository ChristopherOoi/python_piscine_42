from sys import argv


def main():
    try:
        assert len(argv) <= 2, "more than one argument is provided"
        if len(argv) == 1:
            return
        arg = argv[1][1:] if argv[1][0] == "-" else argv[1]
        assert arg.isnumeric(), "argument is not an integer"
        arg = int(argv[1])
        print(f"I'm {'Even' if arg % 2 == 0 else 'Odd'}.")
    except AssertionError as e:
        print(e)


if __name__ == "__main__":
    main()
