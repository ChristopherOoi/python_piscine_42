from PIL import Image
from numpy import array, shape


def ft_load(path: str) -> array:
    """
    This function loads an image,
    prints its format and shape,
    and returns it as a numpy array.
    """
    try:
        img = Image.open(path)
        print("The image format is ", img.format)
        print("The shape of the image is ", shape(img))
        print(array(img))
        return array(img)
    except Exception as e:
        print("Error: ", e)
        return None


if __name__ == "__main__":
    path = "landscape.jpg"
    img = ft_load(path)
    print("The image is: ", img)
    path = "animal.jpeg"
    img = ft_load(path)
    print("The image is: ", img)
    path = "landscape.png"
    img = ft_load(path)
    print("The image is: ", img)
    path = "test.jpg"
    img = ft_load(path)
    print("The image is: ", img)
