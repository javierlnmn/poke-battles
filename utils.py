from colorama import init, Fore, Back, Style
import json


def set_console_color(color):
    return getattr(Fore, color.upper(), None)

def set_console_background(color):
    return getattr(Back, color.upper(), None)

def set_console_style(style):
    return getattr(Style, style.upper(), None)

def reset_console_color():
    return Fore.RESET

def set_console_background(color):
    return Back.RESET

def reset_console_style():
    return Style.NORMAL

def reset_console_ansi_escapes():
    return Style.RESET_ALL

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