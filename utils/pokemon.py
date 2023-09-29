from colorama import Fore, Back, Style

def get_pokemon_data_by_name(pokemon_name, pokemon_data):
    
    for pokemon in pokemon_data:
        if pokemon["name"] == pokemon_name:
            return pokemon
        
    return None

def print_pokemons(pokemon_1, pokemon_2): ###### provisional function #######
    
    for row in zip(pokemon_1.split('\n'), pokemon_2.split('\n')):
        print(Fore.RED + row[0] + Fore.BLUE +" " + row[1] + Fore.RESET)   