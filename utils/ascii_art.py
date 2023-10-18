from colorama import Fore, Back, Style
from PIL import Image
import pyfiglet
import clear_screen

import inspect
import random
import shutil
import time
import os

from config.config import (
    DEFAULT_SPRITE_SIZE,
    ASCII_CHARS,
    SUPPORTED_IMAGE_EXTENSIONS,
)


def set_console_color(color):
    return getattr(Fore, color.upper(), None)


def set_console_background(color):
    return getattr(Back, color.upper(), None)


def set_console_style(style):
    return getattr(Style, style.upper(), None)


def reset_console_color():
    return Fore.RESET


def reset_console_background(color):
    return Back.RESET


def reset_console_style():
    return Style.NORMAL


def reset_console_ansi_escapes():
    return Style.RESET_ALL


def get_random_color():
    available_colors = [
        name
        for name, value in inspect.getmembers(Fore)
        if name.isupper() and isinstance(value, str)
    ]
    random_color = random.choice(available_colors)
    return random_color


def print_full_screen_title(title_text, color, font="slant"):
    terminal_width, terminal_height = shutil.get_terminal_size()

    ascii_art = pyfiglet.figlet_format(title_text, font=font)

    spaces_count = (terminal_width - len(ascii_art.splitlines()[0])) // 2

    padding_lines_top = ((terminal_height - 7) - len(ascii_art.splitlines())) // 2
    padding_lines_bottom = (
        (terminal_height - 7) - len(ascii_art.splitlines()) - padding_lines_top
    )

    print(set_console_color(color))
    print("\n" * padding_lines_top)
    for line in ascii_art.splitlines():
        print(" " * spaces_count + line)
    print("\n" * padding_lines_bottom)
    print(reset_console_ansi_escapes())


def print_full_screen_title_animation(title_text, font="slant"):
    clear_screen.clear()
    for i in range(0, 3):
        print_full_screen_title(title_text, get_random_color(), font)
        time.sleep(0.5)
        clear_screen.clear()
        time.sleep(0.5)


# def save_pokemon_ascii_art(ascii_art, pokemon_name):

#     file_name = pokemon_name
#     file_content = ascii_art

#     try:

#         if not os.path.exists(POKEMON_ASCII_ART_PATH):
#             os.makedirs(POKEMON_ASCII_ART_PATH)

#         file_path = os.path.join(POKEMON_ASCII_ART_PATH, file_name)

#         with open(file_path, "w") as file:
#             file.write(file_content)

#         print("Ascii art saved to file "+file_path+".")

#     except OSError as e:
#         print(f"Error: {e}")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


def resize_image(image, image_width):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(image_width * ratio)
    resized_image = image.resize((image_width, new_height))
    return resized_image


def grayify(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel // 25] for pixel in pixels])
    return characters


def turn_image_into_ascii_art(image_path, image_width=DEFAULT_SPRITE_SIZE):
    
    for ext in SUPPORTED_IMAGE_EXTENSIONS:
        full_image_path = image_path + ext
        
        try:
            image = Image.open(full_image_path)
            break
        except FileNotFoundError:
            continue
        
    else:
        raise FileNotFoundError(f"No valid image found for {image_path} with extensions: {', '.join(SUPPORTED_IMAGE_EXTENSIONS)}")

    new_image_data = pixels_to_ascii(grayify(resize_image(image, image_width)))

    pixel_count = len(new_image_data)
    ascii_image = "\n".join(
        [
            new_image_data[index : (index + image_width)]
            for index in range(0, pixel_count, image_width)
        ]
    )

    return ascii_image
