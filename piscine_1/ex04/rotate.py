from load_image import ft_load
from matplotlib import pyplot as plt
from numpy import array


def main():
    """
    this main function loads the 'animal.jpeg' image
    prints some information about it, and slices it to 'zoom'
    and rotates it
    then display the 'zoomed' image
    """
    path = "animal.jpeg"
    image = ft_load(path)
    if image is None:
        print("Something went wrong!")
        return
    print(image)
    plt.imshow(image)
    plt.show()
    while True:
        try:
            x = int(input("Enter x: "))
            y = int(input("Enter y: "))
            s = int(input("Enter size: "))
            assert x >= 0 and y >= 0, "x and y must be positive"
            assert s > 0, "width and height must be positive"
            assert x + s <= image.shape[1], "width is too big"
            assert y + s <= image.shape[0], "height is too big"
            zoomed = image[y : y + s, x : x + s]
            transposed = array([list(col) for col in zip(*zoomed)])
            print("New shape after rotation: ", transposed.shape)
            print(transposed)
            plt.imshow(transposed)
            plt.show()
        except Exception as e:
            print("Invalid input! ", e)
            continue
        break


if __name__ == "__main__":
    main()
