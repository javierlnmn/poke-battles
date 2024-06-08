import questionary
import clear_screen

import time

from game.pokemon import Pokemon, Types
from config.config import (
    DEFAULT_HEALTH_BAR_LENGTH,
    DEFAULT_SPACE_BETWEEN_SPRITES,
    ATTACK_TYPE_KEYWORD_DAMAGE,
    ATTACK_TYPE_KEYWORD_EFFECT,
    ATTACK_TYPE_KEYWORD_STATUS,
    POKEMON_STAT_KEYWORD_ATTACK_PHYSICAL,
    POKEMON_STAT_KEYWORD_ATTACK_SPECIAL,
    POKEMON_STAT_KEYWORD_DEFENSE_PHYSICAL,
    POKEMON_STAT_KEYWORD_DEFENSE_SPECIAL,
    POKEMON_AFFECTED_KEYWORD_ENEMY,
    POKEMON_AFFECTED_KEYWORD_SELF
)

from utils.ascii_art import print_full_screen_title_animation

class Battle:
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.winner = None
        self.starting_pokemon = pokemon_1 if pokemon_1.stats['speed'] >= pokemon_2.stats['speed'] else pokemon_2
        self.turn = 1 if self.starting_pokemon is pokemon_1 else 2

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
                
                self.use_ability(self.pokemon_1, selected_attack, self.pokemon_2)
                
            elif self.turn == 2:
                
                print(self.get_battle_state() + ('\n'))
                
                selected_attack = self.pokemon_2.pick_random_ability()
                
                time.sleep(.8)
                
                print((" " * (DEFAULT_HEALTH_BAR_LENGTH + DEFAULT_SPACE_BETWEEN_SPRITES)) + str(self.pokemon_2)+" used "+selected_attack.visible_name+"!")
                time.sleep(1.2)
                clear_screen.clear()
                
                self.use_ability(self.pokemon_2, selected_attack, self.pokemon_1)

            
            if self.pokemon_1.current_hp <= 0:
                self.winner = self.pokemon_2
                break

            if self.pokemon_2.current_hp <= 0:
                self.winner = self.pokemon_1
                break

            self.switch_turn()

        time.sleep(1.2)
        print(self.get_battle_state() + ('\n') * 2)
        print(str(self.winner) + ' won the battle!')
        time.sleep(2)
        clear_screen.clear()

        print_full_screen_title_animation('End')
        clear_screen.clear()
                     
    def use_ability(self, attacker, ability, reciever):

        if (POKEMON_AFFECTED_KEYWORD_ENEMY in ability.pokemon_affected):
        
            for attack_type in ability.pokemon_affected[POKEMON_AFFECTED_KEYWORD_ENEMY]:
                
                if attack_type == ATTACK_TYPE_KEYWORD_DAMAGE:
                    # The damage dealt will be either physical or just special

                    if POKEMON_STAT_KEYWORD_ATTACK_SPECIAL in ability.pokemon_affected[POKEMON_AFFECTED_KEYWORD_ENEMY][ATTACK_TYPE_KEYWORD_DAMAGE]:

                        absolute_damage_dealt = self.calculate_attack_damage(
                            attacker.stats[POKEMON_STAT_KEYWORD_ATTACK_SPECIAL],
                            ability.pokemon_affected[POKEMON_AFFECTED_KEYWORD_ENEMY][ATTACK_TYPE_KEYWORD_DAMAGE][POKEMON_STAT_KEYWORD_ATTACK_SPECIAL],
                            reciever.stats[POKEMON_STAT_KEYWORD_DEFENSE_SPECIAL]
                        )

                        reciever.current_hp = (reciever.current_hp - absolute_damage_dealt) if absolute_damage_dealt <= reciever.current_hp else 0

                    elif POKEMON_STAT_KEYWORD_ATTACK_PHYSICAL in ability.pokemon_affected[POKEMON_AFFECTED_KEYWORD_ENEMY][ATTACK_TYPE_KEYWORD_DAMAGE]:

                        absolute_damage_dealt = self.calculate_attack_damage(
                            attacker.stats[POKEMON_STAT_KEYWORD_ATTACK_PHYSICAL],
                            ability.pokemon_affected[POKEMON_AFFECTED_KEYWORD_ENEMY][ATTACK_TYPE_KEYWORD_DAMAGE][POKEMON_STAT_KEYWORD_ATTACK_PHYSICAL],
                            reciever.stats[POKEMON_STAT_KEYWORD_DEFENSE_PHYSICAL]
                        )

                        reciever.current_hp = (reciever.current_hp - absolute_damage_dealt) if absolute_damage_dealt <= reciever.current_hp else 0


                elif attack_type == ATTACK_TYPE_KEYWORD_EFFECT:
                    pass
                
                elif attack_type == ATTACK_TYPE_KEYWORD_STATUS:
                    pass
                    
                else:
                    clear_screen.clear()
                    print('Attack type not defined. Please review the attack data in pokemon_data.json file.')
                    time.sleep(2)
                   
        

        if (POKEMON_AFFECTED_KEYWORD_SELF in ability.pokemon_affected):

            print(ability.pokemon_affected[POKEMON_AFFECTED_KEYWORD_SELF])

    def calculate_attack_damage(self, attacker_attack, move_attack, reciever_defense, attacker_modifier=1, reciever_modifier=1):
        total_damage = (attacker_attack * ((attacker_attack * attacker_modifier / reciever_defense * reciever_modifier) * .6))
        total_damage = 1 if total_damage <= 1 else total_damage
        return round(total_damage)
