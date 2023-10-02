import questionary

from game.battle import Battle


class Game:
    def __init__(self, battle: Battle):
        self.gamemode = None  # probably will use this in the future
        # pvp or pve
        self.battle = battle

    def play_battle_pve(self):
        while not self.battle.winner:
            pokemon_1_attack_list = self.battle.pokemon_1.get_abilities_list()

            print(self.battle.get_battle_state() + ('\n') * 2)
            
            print('What should '+str(self.battle.pokemon_1)+' do?')

            user_attack = questionary.select(
                "",
                qmark="",
                choices=pokemon_1_attack_list,  # Use a lambda function
            ).ask()
