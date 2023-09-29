import json

def read_file_data(file):
        
    try:
        
        with open(file, 'r') as read_file:
            return json.load(read_file)
        
    except FileNotFoundError:
        print(f"Error: The file '{file}' does not exist.")
        
    except json.JSONDecodeError as e:
        print(f"Error: Failed decoding JSON in '{file}': {e}")

    return None

def read_ascii_art(folder, pokemon):
        
    try:
        
        return open(folder + pokemon, 'r').read()
        
    except FileNotFoundError:
        print(f"Error: The file '{folder + pokemon}' does not exist.")
        
    except json.JSONDecodeError as e:
        print(f"Error: Failed decoding JSON in '{folder + pokemon}': {e}")

    return None

