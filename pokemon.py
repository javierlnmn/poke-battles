from utils import set_console_color, set_console_style, reset_console_ansi_escapes

class Pokemon:
    
    def __init__( self, id, name, visible_name, type, color, stats, abilities ):
        self.id = id
        self.name = name
        self.visible_name = visible_name
        self.type = type
        self.color = color
        self.stats = stats
        self.abilities = abilities
        
    def __repr__(self) -> str:
        return '['+str(self.id)+'] '+str(self.name)+'\n'+str(self.type)+'\n'+str(self.abilities)+'\n'+str(self.stats)
    
    def __str__(self) -> str:
        return set_console_style('bright') + set_console_color(self.color) + self.visible_name + reset_console_ansi_escapes()
        
    