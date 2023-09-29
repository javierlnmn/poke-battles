from colorama import init
import clear_screen

import time

from game.game import Game
from game.battle import Battle
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
    
    print_full_screen_title_animation('Battle!')
    
    current_battle = Battle(selected_pokemon, enemy_pokemon)
    
    game = Game(current_battle)
    
    game.battle.print_battle_state()

    time.sleep(3)
    
def test_battle_state_art():
    pokemon_1 = random_pokemon()
    pokemon_2 = random_pokemon()
    current_battle = Battle(pokemon_1, pokemon_2)
    
    print(pokemon_2.get_visual_stats_sprite())
    time.sleep(5)
    clear_screen.clear()
    
    game = Game(current_battle)
    
    game.battle.print_battle_state()
    time.sleep(5)
    


if __name__ == "__main__":
    main()
    