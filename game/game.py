from game.battle import Battle
import pick


class Game:
    def __init__(self, battle: Battle):
        self.gamemode = None  # probably will use this in the future
        # pvp or pve
        self.battle = battle

    def play_battle_pve(self):
        while not self.battle.winner:
            
            pokemon_1_attack_list = self.battle.pokemon_1.
            
            option, index = pick.pick(
                pokemon_1_attack_list, "Choose a Pokèmon!", indicator=">", default_index=0
            )
