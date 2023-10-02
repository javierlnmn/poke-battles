from colorama import Fore, Back, Style
import pyfiglet
import clear_screen

import inspect
import random
import shutil
import time


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
    print(random_color); time.sleep(.6)
    return random_color

def print_full_screen_title(title_text, color, font="slant"):

    terminal_width, terminal_height = shutil.get_terminal_size()

    ascii_art = pyfiglet.figlet_format(title_text, font=font)

    spaces_count = (terminal_width- len(ascii_art.splitlines()[0])) // 2

    padding_lines_top = ((terminal_height-7) - len(ascii_art.splitlines())) // 2
    padding_lines_bottom = (terminal_height-7) - len(ascii_art.splitlines()) - padding_lines_top

    print("\n" * padding_lines_top)
    set_console_color(color)
    for line in ascii_art.splitlines():
        print(" " * spaces_count + line)
    reset_console_ansi_escapes()
    print("\n" * padding_lines_bottom)

    
def print_full_screen_title_animation(title_text, font="slant"):
    clear_screen.clear()
    for i in range(0, 3):
        print_full_screen_title(title_text, get_random_color(), font)
        time.sleep(.5)
        clear_screen.clear()
        time.sleep(.5)