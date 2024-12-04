from numpy import mean
from load_image import ft_load
from matplotlib import pyplot as plt


def ft_invert(array) -> array:
    """
    Inverts the colour of the image received.
    """
    plt.imshow(255 - array)
    plt.show()
    return 255 - array


def ft_red(array) -> array:
    """
    Applies a red filter to the image received.
    """
    plt.imshow(array[..., 0])
    plt.show()
    return array[..., 0]


def ft_green(array) -> array:
    """
    Applies a green filter to the image received.
    """
    plt.imshow(array[..., 1])
    plt.show()
    return array[..., 1]


def ft_blue(array) -> array:
    """
    Applies a blue filter to the image received.
    """
    plt.imshow(array[..., 2])
    plt.show()
    return array[..., 2]


def ft_grey(array) -> array:
    """
    Turns the image received into a grayscale image.
    """
    plt.imshow(mean(array, axis=2))
    plt.show()
    return mean(array, axis=2)


if __name__ == "__main__":
    array = ft_load("landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)
