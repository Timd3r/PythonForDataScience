from load_image import load_image
import numpy as np
from matplotlib import pyplot as plt


def transpose(array):
    """function that transposes a 3D array"""
    h, w, c = array.shape
    transposed = np.zeros((w, h, c), dtype=array.dtype)
    for i in range(h):
        for j in range(w):
            transposed[j, i] = array[i, j]
    return transposed


def rotate(path: str):
    """function that rotates an image by 90 degrees"""
    try:
        img = load_image(path)
        if img is None:
            raise ValueError("Failed to load image.")
        print(img)
        rotated_img = transpose(img)
        print(f"New shape after transpose: {rotated_img.shape}")
        print(rotated_img)
        plt.imshow(rotated_img, cmap='gray')
        plt.title("Rotated Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
        save_path = "Python_01_Array/images/rotated_animal.jpeg"
        plt.imsave(save_path, rotated_img.squeeze(), cmap='gray')
    except Exception as e:
        print(f"Error: {e}")
        return


def main():
    path = "Python_01_Array/images/zoomed_animal.jpeg"
    rotate(path)


if __name__ == "__main__":
    main()
