import os
from PIL import Image
from numpy import array


def load_image(path: str) -> array:
    """function that loads an image,
    prints its format, and its pixels
    content in RGB format"""
    try:
        if not os.path.exists(path):
            raise FileNotFoundError(f"File '{path}' not found.")
        img = Image.open(path)
        img = img.convert("RGB")
        img_array = array(img)
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            img_array = img_array[:, :, 0:1]
        print(f"the shape of the image is: {img_array.shape}")
        return img_array
    except Exception as e:
        print(f"Error loading image: {e}")
