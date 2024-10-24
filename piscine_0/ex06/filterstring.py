from ft_filter import ft_filter
from sys import argv


def main():
    """
    main function validates input
    if input is valid, it filters the words in the string by length
    using ft_filter
    """
    try:
        assert len(argv) == 3, "the arguments are bad"
        for c in argv[1]:
            assert c.isalpha() or c.isspace(), "the arguments are bad"
        assert argv[2].isnumeric(), "the arguments are bad"
        words = argv[1].split(" ")
        n = int(argv[2])
        print(list(ft_filter(lambda x: len(x) > n, words)))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
