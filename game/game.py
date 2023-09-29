from game.battle import Battle

class Game:
    
    def __init__(self, battle: Battle):
        self.gamemode = None # probably will use this in the future
        self.battle = battle
    