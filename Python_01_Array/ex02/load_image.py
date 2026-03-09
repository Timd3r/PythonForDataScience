from PIL import Image
from numpy import array
import os


def ft_load(path: str) -> array:
    """function that loads an image,
    prints its format, and its pixels
    content in RGB format"""
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File '{path}' not found.")
        img = Image.open(path)
        img = img.convert("RGB")
        img_array = array(img)
        print(f"the shape of the image is: {img_array.shape}")
        return img_array
    except Exception as e:
        print(f"Error loading image: {e}")
