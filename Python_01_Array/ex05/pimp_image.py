from numpy import array
import matplotlib.pyplot as plt


def ft_invert(array) -> array:
    """function that inverts the colors of an image"""
    new_array = 255 - array
    save_image(new_array, "Python_01_Array/images/pimp/inverted_image.jpg")
    return new_array


def ft_red(array) -> array:
    """function that keeps only the red channel of an image"""
    new_array = array.copy()
    new_array[:, :, 1] = new_array[:, :, 1] * 0
    new_array[:, :, 2] = new_array[:, :, 2] * 0
    save_image(new_array, "Python_01_Array/images/pimp/red_channel.jpg")
    return new_array


def ft_green(array) -> array:
    """function that keeps only the green channel of an image"""
    new_array = array.copy()
    new_array[:, :, 0] = new_array[:, :, 0] - new_array[:, :, 0]
    new_array[:, :, 2] = new_array[:, :, 2] - new_array[:, :, 2]
    save_image(new_array, "Python_01_Array/images/pimp/green_channel.jpg")
    return new_array


def ft_blue(array) -> array:
    """function that keeps only the blue channel of an image"""
    new_array = array.copy()
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    save_image(new_array, "Python_01_Array/images/pimp/blue_channel.jpg")
    return new_array


def ft_grey(array) -> array:
    """function that converts an image to grayscale"""
    new_array = array.copy()
    grey = (new_array[:, :, 0] / 1)
    new_array[:, :, 0] = grey
    new_array[:, :, 1] = grey
    new_array[:, :, 2] = grey
    save_image(new_array, "Python_01_Array/images/pimp/grey_channel.jpg")
    return new_array


def save_image(array: array, path: str) -> None:
    """function that saves an image"""
    plt.imsave(path, array.squeeze())
