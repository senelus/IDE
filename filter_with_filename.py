from PIL import Image
import numpy as np


def convert_image_to_mosaic(image, size, gradation_step):
    for x in range(0, len(image), size):
        for y in range(0, len(image[0]), size):
            image[x:x + size, y:y + size] = get_average_brightness(
                image[x:x + size, y:y + size], size, gradation_step)
    return image


def get_average_brightness(block, size, gradation_step):
    average_color = (block[:size, :size].sum() / 3) // size ** 2
    return int(average_color // gradation_step) * gradation_step


def main():
    image_file = Image.open("scale1200.jpg")
    block_size = 10
    gradations_count = 50
    image = np.array(image_file)
    gradation_step = 255 // gradations_count

    res = Image.fromarray(convert_image_to_mosaic(image, block_size, gradation_step))
    res.save("res_new.jpg")


if __name__ == '__main__':
    main()
