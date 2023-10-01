from game.battle import Battle
import pick


class Game:
    def __init__(self, battle: Battle):
        self.gamemode = None  # probably will use this in the future
        # pvp or pve
        self.battle = battle

    def play_battle_pve(self):
        while not self.battle.winner:
            
            pokemon_1_attack_list = self.battle.pokemon_1.get_abilities_list()
            
            option, index = pick.pick(
                pokemon_1_attack_list, self.battle.get_battle_state(), indicator=">", default_index=0
            )
