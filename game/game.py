from game.battle import Battle

class Game:
    
    def __init__(self, battle: Battle):
        self.gamemode = '' # probably will use this in the future
        self.battle = battle
    