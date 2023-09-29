from colorama import init, Fore, Back, Style
import clear_screen
import pick

import time
import json
import random

import game
from config import (
    POKEMON_DATA_FILE_PATH,
    POKEMON_TYPES_FILE_PATH,
)
from utils import read_file_data
from pokemon import Pokemon

clear_screen.clear()

pokemon_list_data = read_file_data(POKEMON_DATA_FILE_PATH)
pokemon_list_names = list(pokemon_list_data.keys())
pokemon_types = read_file_data(POKEMON_TYPES_FILE_PATH)


def main():
    # initialize colorama
    init()
    # clear screen
    clear_screen.clear()

    selected_pokemon = choose_pokemon()
    clear_screen.clear()

    print("You chose " + str(selected_pokemon) + "!")
    print(selected_pokemon.get_ascii_art())
    time.sleep(1.5)
    clear_screen.clear()
    time.sleep(0.8)

    enemy_pokemon = random_pokemon()
    print("Oh!")
    time.sleep(1.5)
    clear_screen.clear()
    time.sleep(0.8)

    print("A wild " + str(enemy_pokemon) + " appeared!")
    print(enemy_pokemon.get_ascii_art())
    time.sleep(1.5)
    clear_screen.clear()
    time.sleep(0.8)


def choose_pokemon():
    pokemon_list = []

    for id, name in enumerate(pokemon_list_data, start=1):
        
        pokemon_data = pokemon_list_data[name]
        
        pokemon = Pokemon(
            id=id,
            name=name,
            visible_name=pokemon_data["visible_name"],
            type=pokemon_data["type"],
            color=pokemon_data["color"],
            stats=pokemon_data["stats"],
            abilities=pokemon_data["abilities"],
        )

        pokemon_list.append(pokemon)

    pokemon_choose_list = [pokemon.visible_name for pokemon in pokemon_list]

    option, index = pick.pick(
        pokemon_choose_list, "Choose a Pokèmon!", indicator=">", default_index=0
    )

    return pokemon_list[index]


def random_pokemon():
    pokemon_index = random.randint(0, len(pokemon_list_data) - 1)
    selected_pokemon_name = pokemon_list_names[pokemon_index] 
    pokemon_data = pokemon_list_data[selected_pokemon_name]  

    pokemon = Pokemon(
        id=pokemon_index,
        name=selected_pokemon_name,
        visible_name=pokemon_data["visible_name"],
        type=pokemon_data["type"],
        color=pokemon_data["color"],
        stats=pokemon_data["stats"],
        abilities=pokemon_data["abilities"],
    )

    return pokemon


if __name__ == "__main__":
    main()
