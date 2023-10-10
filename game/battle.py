import questionary
import clear_screen

import time

from game.pokemon import Pokemon
from config.config import DEFAULT_STARTING_TURN

class Battle:
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.turn = DEFAULT_STARTING_TURN
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
    
    def switch_turn(self):
        return 3 - self.turn
    
    
    def play_battle(self):
        
        while not self.winner:
            
            clear_screen.clear()
            time.sleep(1)
            
            if self.turn == 1:
            
                print(self.get_battle_state() + ('\n') * 2)
                print('What should '+str(self.pokemon_1)+' do?')
                
                pokemon_1_attack_visible_names_list = self.pokemon_1.get_abilities_visible_name_list()

                selected_ability_visible_name = questionary.select(
                    "",
                    choices=pokemon_1_attack_visible_names_list
                ).ask()

                selected_attack = self.pokemon_1.get_ability_data_by_visible_name(selected_ability_visible_name)
                
                self.pokemon_2.current_hp -= self.calculate_damage(self.pokemon_1, selected_attack, self.pokemon_2)
                
            elif self.turn == 2:
                
                selected_attack = self.pokemon_1.pick_random_ability()
                
                pass
            
            if self.pokemon_1.current_hp <= 0:
                self.winner = self.pokemon_2
            elif self.pokemon_2.current_hp <= 0:
                self.winner = self.pokemon_1

            self.switch_turn()
            
    def calculate_damage(self, attacker, ability, reciever):
        # damage = (MovePower * (AttackStat / DefenseStat)) * TypeModifier
        pass