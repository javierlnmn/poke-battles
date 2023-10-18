import json

from config.config import POKEMON_DATA_FILE_PATH, DEFAULT_SPRITE_SIZE
from utils.general import read_file_data
from utils.ascii_art import turn_image_into_ascii_art


def get_pokemon_data_by_name(pokemon_name):
    
    pokemon_data = read_file_data(POKEMON_DATA_FILE_PATH)
    
    for pokemon in pokemon_data:
        if pokemon == pokemon_name:
            return pokemon
        
    return None

def get_pokemon_ascii_art(folder, pokemon):
        
    try:
        
        return turn_image_into_ascii_art(folder + pokemon, DEFAULT_SPRITE_SIZE)
        
    except FileNotFoundError:
        print(f"Error: The file '{folder + pokemon}' does not exist.")

    return ""