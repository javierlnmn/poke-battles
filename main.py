from colorama import init as colorama_init
import clear_screen
import questionary

import time

from game.battle import Battle
from game.game import Game
from game.pokemon import random_pokemon
from utils.ascii_art import print_full_screen_title, get_random_color

clear_screen.clear()

def main():
    # initialize colorama
    colorama_init()
    
    clear_screen.clear()
    print("It's recommended to play the game fullscreen or in a big window.")
    time.sleep(2)
    
    clear_screen.clear()
    time.sleep(1)
    print_full_screen_title("Poke - Battles", get_random_color())
    time.sleep(1.5)
    
    clear_screen.clear()
    time.sleep(1)
    
    play_again = True
    
    while play_again:

        Game.play()
        
        play_again = questionary.confirm(
            "Do you want to play again?"
        ).ask()
        
        clear_screen.clear()
        time.sleep(0.8)

if __name__ == "__main__":
    main()
    # enemy_pokemon = random_pokemon()

    # current_battle = Battle(enemy_pokemon, enemy_pokemon)
        
    # current_battle.play_battle()
