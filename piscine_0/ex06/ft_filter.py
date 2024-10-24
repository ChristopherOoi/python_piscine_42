from typing import Any, Callable, Iterator, List


class ft_filter:
    """
    Return an iterator yielding those items of iterable for which
    function(item)
    is true. If function is None, return the items that are true.
    """

    def __init__(self, function: Callable[[Any], bool], iterable: List[Any]):
        self.function = function
        self.iterable = iterable
        if self.function is None:
            self.result = (i for i in self.iterable if i)
        else:
            self.result = (i for i in self.iterable if self.function(i))

    def __iter__(self) -> Iterator:
        return iter(self.result)

    def __next__(self):
        return next(self.__iter__())


if __name__ == "__main__":

    def is_even(n: int) -> bool:
        return n % 2 == 0

    next(ft_filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = ft_filter(is_even, numbers)
    print(result)
    for i in result:
        print(i)
    result = filter(is_even, numbers)
    print(result)
    for i in result:
        print(i)
    result = ft_filter(None, numbers)
    print(result)
    for i in result:
        print(i)
    result = filter(None, numbers)
    print(result)
    for i in result:
        print(i)

    print(filter.__doc__)
    print(ft_filter.__doc__)
    words = ["apple", "banana", "cherry", "kiwi", "mango"]
    result = ft_filter(lambda x: "a" in x, words)
    print(result)
    for i in result:
        print(i)
    result = filter(lambda x: "a" in x, words)
    print(result)
    for i in result:
        print(i)
    result = ft_filter(None, words)
    print(result)
    for i in result:
        print(i)
    result = filter(None, words)
    print(result)
    for i in result:
        print(i)
