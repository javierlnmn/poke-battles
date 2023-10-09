import questionary
import clear_screen

import time

from game.pokemon import Pokemon

class Battle:
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.winner = None

    def get_battle_state(self):
        
        battle_state = "\n".join(
            [
                row[0]
                + (' ')*15
                + row[1]
                for row in zip(
                    self.pokemon_1.get_visual_stats_sprite().split("\n"),
                    self.pokemon_2.get_visual_stats_sprite().split("\n"),
                )
            ]
        )
        
        return battle_state
    
    
    def play_battle(self):
        
        while not self.winner:
            
            clear_screen.clear()
            time.sleep(1)
            
            print(self.get_battle_state() + ('\n') * 2)
            print('What should '+str(self.pokemon_1)+' do?')
            
            pokemon_1_attack_visible_names_list = self.pokemon_1.get_abilities_visible_name_list()

            selected_ability_visible_name = questionary.select(
                "",
                choices=pokemon_1_attack_visible_names_list
            ).ask()

            selected_attack_data = self.pokemon_1.get_ability_data_by_visible_name(selected_ability_visible_name)
            
