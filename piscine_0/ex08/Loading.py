from time import time


def generate_bar(
    current: int,
    total: int,
    bar_length: int,
    time_elapsed: float,
) -> str:
    """
    this function generates the progress bar
    """
    p = current / total
    fill_length = int(p * bar_length)
    bar = "=" * fill_length + "-" * (bar_length - fill_length)
    return f"{p * 100:.0f}%[{bar}] {current}/{total} - {time_elapsed:.2f}s"


def ft_tqdm(lst: range) -> None:
    """
    this function mimics tqdm, displaying a progress bar
    """
    total = len(lst)
    current = 0
    # initial bar
    start = time()
    print(generate_bar(current, total, 64, 0), end="\r")

    for i in lst:
        yield i
        current += 1
        time_elapsed = time() - start
        print(generate_bar(current, total, 64, time_elapsed), end="\r")


if __name__ == "__main__":
    pass
