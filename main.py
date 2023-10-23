from colorama import init
import clear_screen
import questionary

import time

# from game.game import Game
from game.battle import Battle
from game.pokemon import user_choose_pokemon, random_pokemon
from utils.ascii_art import print_full_screen_title_animation, print_full_screen_title, get_random_color


clear_screen.clear()


def main():
    # initialize colorama
    init()
    
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
        
        selected_pokemon = user_choose_pokemon()
        clear_screen.clear()
        time.sleep(.8)

        print("You chose " + str(selected_pokemon) + "!")
        print(selected_pokemon.get_ascii_art_color())
        time.sleep(1.5)
        clear_screen.clear()
        time.sleep(0.8)


        enemy_pokemon = random_pokemon()
        print("Oh!")
        time.sleep(1.5)
        clear_screen.clear()
        time.sleep(0.8)

        print("A wild " + str(enemy_pokemon) + " appeared!")
        print(enemy_pokemon.get_ascii_art_color())
        time.sleep(1.5)
        clear_screen.clear()
        time.sleep(0.8)

        print_full_screen_title_animation("Battle!")

        current_battle = Battle(selected_pokemon, enemy_pokemon)
        
        current_battle.play_battle()
        
        clear_screen.clear()
        time.sleep(0.8)
        
        play_again = questionary.confirm(
            "Do you want to play again?"
        ).ask()
        
        clear_screen.clear()
        time.sleep(0.8)
        


def test_battle_state_art():
    pokemon_1 = random_pokemon()
    pokemon_2 = random_pokemon()
    current_battle = Battle(pokemon_1, pokemon_2)
    current_battle.play_battle()
    time.sleep(5)


if __name__ == "__main__":
    main()
