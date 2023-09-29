from colorama import Fore, Back, Style
import clear_screen
import pyfiglet
import shutil
import colorama

import json
import time
import random
import inspect


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
        for name, value in inspect.getmembers(colorama.Fore)
        if name.isupper() and isinstance(value, str)
    ]
    random_color = random.choice(available_colors)
    return random_color

def get_pokemon_data_by_name(pokemon_name, pokemon_data):
    
    for pokemon in pokemon_data:
        if pokemon["name"] == pokemon_name:
            return pokemon
        
    return None

def print_pokemons(pokemon_1, pokemon_2):
    
    for row in zip(pokemon_1.split('\n'), pokemon_2.split('\n')):
        print(Fore.RED + row[0] + Fore.BLUE +" " + row[1] + Fore.RESET)        
        
def read_file_data(file):
        
    try:
        
        with open(file, 'r') as read_file:
            return json.load(read_file)
        
    except FileNotFoundError:
        print(f"Error: The file '{file}' does not exist.")
        
    except json.JSONDecodeError as e:
        print(f"Error: Failed decoding JSON in '{file}': {e}")

    return None

def read_ascii_art(folder, pokemon):
        
    try:
        
        return open(folder + pokemon, 'r').read()
        
    except FileNotFoundError:
        print(f"Error: The file '{folder + pokemon}' does not exist.")
        
    except json.JSONDecodeError as e:
        print(f"Error: Failed decoding JSON in '{folder + pokemon}': {e}")

    return None


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