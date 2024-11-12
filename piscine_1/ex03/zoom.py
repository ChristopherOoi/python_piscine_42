from load_image import ft_load
from matplotlib import pyplot as plt


def main():
    """
    this main function loads the 'animal.jpeg' image
    prints some information about it, and slices it to 'zoom'
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
            w = int(input("Enter width: "))
            h = int(input("Enter height: "))
            assert x >= 0 and y >= 0, "x and y must be positive"
            assert w > 0 and h > 0, "width and height must be positive"
            assert x + w <= image.shape[1], "width is too big"
            assert y + h <= image.shape[0], "height is too big"
            zoomed = image[y : y + h, x : x + w]
            plt.imshow(zoomed)
            plt.show()
        except Exception as e:
            print("Invalid input! ", e)
            continue
        break


if __name__ == "__main__":
    main()
