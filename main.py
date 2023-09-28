from colorama import init, Fore, Back, Style
import clear_screen
import pick

import time
import json
import random

import game
from config import (
    POKEMON_ASCII_ART_PATH,
    POKEMON_DATA_FILE_PATH,
    POKEMON_TYPES_FILE_PATH,
)
from utils import read_file_data
from pokemon import Pokemon

clear_screen.clear()

pokemon_data = read_file_data(POKEMON_DATA_FILE_PATH)
pokemon_types = read_file_data(POKEMON_TYPES_FILE_PATH)


def main():
    # initialize colorama
    init()
    # clear screen
    clear_screen.clear()

    selected_pokemon = choose_pokemon()
    time.sleep(.8)
    clear_screen.clear()

    print("You chose " + str(selected_pokemon) + "!")
    time.sleep(1.5)
    clear_screen.clear()
    time.sleep(.8)

    enemy_pokemon = random_pokemon()
    print('Oh!')
    time.sleep(1.5)
    clear_screen.clear()
    time.sleep(.8)
    
    print('A wild ' + str(enemy_pokemon) + ' appeared!')
    time.sleep(1.5)
    clear_screen.clear()
    time.sleep(.8)

def choose_pokemon():
    
    pokemon_list = []
    
    for id, data in enumerate(pokemon_data, start=1):
        pokemon = Pokemon(
            id=id,
            name=data["name"],
            visible_name=data["visible_name"],
            type=data["type"],
            color=data["color"],
            stats=data["stats"],
            abilities=data["abilities"],
        )

        pokemon_list.append(pokemon)

    pokemon_choose_list = [pokemon.visible_name for pokemon in pokemon_list]

    option, index = pick.pick(
        pokemon_choose_list, "Choose a Pokèmon!", indicator=">", default_index=0
    )

    return pokemon_list[index]


def random_pokemon():
    
    pokemon_index = random.randint(0, len(pokemon_data)-1)
            
    pokemon = Pokemon(
        id=pokemon_index,
        name=pokemon_data[pokemon_index]["name"],
        visible_name=pokemon_data[pokemon_index]["visible_name"],
        type=pokemon_data[pokemon_index]["type"],
        color=pokemon_data[pokemon_index]["color"],
        stats=pokemon_data[pokemon_index]["stats"],
        abilities=pokemon_data[pokemon_index]["abilities"],
    )
    
    return pokemon


if __name__ == "__main__":
    main()
