import questionary
import clear_screen

import time

from game.pokemon import Pokemon
from config.config import DEFAULT_STARTING_TURN, DEFAULT_SPRITE_SIZE, DEFAULT_SPACE_BETWEEN_SPRITES

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
                + (' ')*DEFAULT_SPACE_BETWEEN_SPRITES
                + row[1]
                for row in zip(
                    self.pokemon_1.get_visual_stats_sprite().split("\n"),
                    self.pokemon_2.get_visual_stats_sprite().split("\n"),
                )
            ]
        )
        
        return battle_state
    
    def switch_turn(self):
        self.turn = 3 - self.turn
    
    
    def play_battle(self):
        
        while not self.winner:
            
            clear_screen.clear()
            time.sleep(.5)
            
            if self.turn == 1:
            
                print(self.get_battle_state() + ('\n') * 2)
                print('What should '+str(self.pokemon_1)+' do?')
                
                pokemon_1_attack_visible_names_list = self.pokemon_1.get_abilities_visible_name_list()

                selected_ability_visible_name = questionary.select(
                    "",
                    choices=pokemon_1_attack_visible_names_list
                ).ask()

                selected_attack = self.pokemon_1.get_ability_by_visible_name(selected_ability_visible_name)
                clear_screen.clear()
                time.sleep(.8)
                
                print(str(self.pokemon_1)+" used "+selected_attack.visible_name+"!")
                time.sleep(1.2)
                clear_screen.clear()
                
                self.pokemon_2.current_hp -= self.calculate_damage(self.pokemon_1, selected_attack, self.pokemon_2)
                
            elif self.turn == 2:
                
                print(self.get_battle_state() + ('\n'))
                
                selected_attack = self.pokemon_2.pick_random_ability()
                
                time.sleep(.8)
                
                print((" " * (DEFAULT_SPRITE_SIZE + DEFAULT_SPACE_BETWEEN_SPRITES)) + str(self.pokemon_2)+" used "+selected_attack.visible_name+"!")
                time.sleep(1.2)
                clear_screen.clear()
                
                self.pokemon_1.current_hp -= self.calculate_damage(self.pokemon_1, selected_attack, self.pokemon_2)

            
            if self.pokemon_1.current_hp <= 0:
                self.winner = self.pokemon_2
            elif self.pokemon_2.current_hp <= 0:
                self.winner = self.pokemon_1

            self.switch_turn()
            
    def calculate_damage(self, attacker, ability, reciever):
        pass