from numpy import array, mean
from load_image import ft_load
from matplotlib import pyplot as plt


def ft_invert(array) -> array:
    """
    Inverts the colour of the image received.
    """
    plt.imshow(255 - array)
    plt.show()
    plt.savefig("inverted_image.jpg")
    return 255 - array


def ft_red(array) -> array:
    """
    Applies a red filter to the image received.
    """
    res = array.copy()
    res[..., 1:] = 0
    plt.imshow(res)
    plt.show()
    plt.savefig("red_image.jpg")
    return res


def ft_green(array) -> array:
    """
    Applies a green filter to the image received.
    """
    res = array.copy()
    res[..., ::2] = 0
    plt.imshow(res)
    plt.show()
    plt.savefig("green_image.jpg")
    return res


def ft_blue(array) -> array:
    """
    Applies a blue filter to the image received.
    """
    res = array.copy()
    res[..., :2] = 0
    plt.imshow(res)
    plt.show()
    plt.savefig("blue_image.jpg")
    return res


def ft_grey(array) -> array:
    """
    Turns the image received into a grayscale image.
    """
    val = mean(array, axis=2)
    res = array.copy()
    res[..., :] = val.reshape(val.shape[0], val.shape[1], 1)
    plt.imshow(res)
    plt.show()
    plt.savefig("grey_image.jpg")
    return res


if __name__ == "__main__":
    array = ft_load("landscape.jpg")

    ft_invert(array)
    ft_red(array)
    ft_green(array)
    ft_blue(array)
    ft_grey(array)

    print(ft_invert.__doc__)
