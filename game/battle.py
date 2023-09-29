from game.pokemon import Pokemon

class Battle:
    
    def __init__(self, pokemon_1: Pokemon, pokemon_2: Pokemon):
        self.pokemon_1 = pokemon_1
        self.pokemon_2 = pokemon_2
        self.winner = None
        
    def print_battle_state(self):
        for row in zip(self.pokemon_1.get_visual_stats_sprite().split('\n'), self.pokemon_2.get_visual_stats_sprite().split('\n')):
            print(row[0] + "   " + row[1]) 
    
