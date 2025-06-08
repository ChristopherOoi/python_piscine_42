from typing import Any


def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwds)
            else:
                print(f"Error: {function} call too many times")

        return limit_function

    return callLimiter


if __name__ == "__main__":

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()
