from colorama import Fore, Back, Style

def get_pokemon_data_by_name(pokemon_name, pokemon_data):
    
    for pokemon in pokemon_data:
        if pokemon["name"] == pokemon_name:
            return pokemon
        
    return None
