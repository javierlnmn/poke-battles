from colorama import init, Fore, Back, Style
import clear_screen

import time

from game.game import Game
from game.pokemon import choose_pokemon, random_pokemon
from utils.ascii_art import print_full_screen_title_animation


clear_screen.clear()

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
    
    print_full_screen_title_animation('Battle!')


if __name__ == "__main__":
    main()
