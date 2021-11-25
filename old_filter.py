from PIL import Image
import numpy as np
import cProfile as profile

def transform_image_to_mosaic(input_image, mosaic_width, mosaic_height, scale, mosaic_name, format_name):
    image_array = np.array(input_image)
    mosaic_array = get_gray_mosaic_array(image_array, mosaic_width, mosaic_height, scale)
    mosaic_image = Image.fromarray(mosaic_array)
    mosaic_image.save(mosaic_name + format_name)


def get_gray_mosaic_array(image_array, mosaic_width, mosaic_height, scale):
    width = len(image_array)
    height = len(image_array[1])
    for current_width in range(0, width, mosaic_width):
        for current_height in range(0, height, mosaic_height):
            average_color = get_average_color(image_array, current_width, mosaic_width, current_height, mosaic_height)
            gray_color = average_color - average_color % scale
            image_array[current_width: current_width + mosaic_width,
            current_height: current_height + mosaic_height] = np.full(3, gray_color)
    return image_array


def get_average_color(image_array, width, mosaic_width, height, mosaic_height):
    mosaic_resolution = mosaic_height * mosaic_width
    average_color_on_screen = np.sum(image_array[width: width + mosaic_width, height: height + mosaic_height]) // 3
    average_color = average_color_on_screen // mosaic_resolution
    return average_color


input_image = Image.open(input("Введите путь до изображение: "))
mosaic_width = int(input("Введите целое положительное число для ширины мозайки: "))
mosaic_height = int(input("Введите целое положительное число для высоты мозайки: "))
scale = int(input("Введите целое положительное число для масштаба градации серых цветов в мозайке: "))
mosaic_name = input("Введите название для готовой мозайки: ")
format_name = input("Введите формат для готовой мозайки: ")
pr = profile.Profile()
pr.disable()
pr.enable()
transform_image_to_mosaic(input_image, mosaic_width, mosaic_height, scale, mosaic_name, format_name)
pr.disable()
pr.dump_stats('profile_old.pstat')