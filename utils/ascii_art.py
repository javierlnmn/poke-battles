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
    return random_color

def print_full_screen_title(title_text, font="slant"):

    terminal_width, terminal_height = shutil.get_terminal_size()

    ascii_art = pyfiglet.figlet_format(title_text, font=font)

    spaces_count = (terminal_width- len(ascii_art.splitlines()[0])) // 2

    padding_lines_top = ((terminal_height-7) - len(ascii_art.splitlines())) // 2
    padding_lines_bottom = (terminal_height-7) - len(ascii_art.splitlines()) - padding_lines_top

    
    print(set_console_color(get_random_color()))
    print("\n" * padding_lines_top)
    for line in ascii_art.splitlines():
        print(" " * spaces_count + line)
    print("\n" * padding_lines_bottom)
    print(reset_console_ansi_escapes())
    
def print_full_screen_title_animation(title_text, font="slant"):
    for i in range(0, 3):
        print_full_screen_title(title_text, font)
        time.sleep(.5)
        clear_screen.clear()
        time.sleep(.5)