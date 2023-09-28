from pokemon import Pokemon

class Battle:
    
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon):
        self.pokemon_1 = pokemon_1
    

class Game:
    
    def __init__(self, battle: Battle):
        self.gamemode = '' # probably will use this in the future
        self.battle = battle
    