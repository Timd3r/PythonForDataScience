from matplotlib import pyplot as plt
from load_image import load_image


def zoom(path: str, factor: int):
    try:
        img = load_image(path)
        if img is None:
            raise ValueError("Image loading failed.")

        print(f"The shape of image is: {img.shape}")
        print(img)

        height, width = img.shape[0], img.shape[1]
        window_h = 400 // factor
        window_w = 400 // factor
        center_y, center_x = height // 2, width // 2
        start_y = center_y - window_h
        end_y = center_y + window_h
        start_x = center_x - window_w
        end_x = center_x + window_w

        zoomed = img[start_y:end_y, start_x:end_x, 0:1]

        print(f"New shape after slicing: {zoomed.shape}")
        print(zoomed)

        plt.imshow(zoomed, cmap='gray')
        plt.title("Zoomed Image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
        save_path = "Python_01_Array/images/zoomed_animal.jpeg"
        plt.imsave(save_path, zoomed.squeeze(), cmap='gray')

    except Exception as e:
        print(f"Error: {e}")


def main():
    image_path = "Python_01_Array/images/animal.jpeg"
    zoom_factor = 2
    zoom(image_path, zoom_factor)


if __name__ == "__main__":
    main()
