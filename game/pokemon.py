import questionary
import clear_screen
import time

import random

from utils.general import read_file_data, read_ascii_art
from utils.ascii_art import (
    set_console_color,
    set_console_style,
    reset_console_ansi_escapes,
    reset_console_style,
    reset_console_color,
)
from config.config import (
    POKEMON_DATA_FILE_PATH,
    POKEMON_TYPES_FILE_PATH,
    POKEMON_ABILITIES_FILE_PATH,
    POKEMON_ASCII_ART_PATH,
)

pokemon_list_data = read_file_data(POKEMON_DATA_FILE_PATH)
pokemon_abilities = read_file_data(POKEMON_ABILITIES_FILE_PATH)
pokemon_types = read_file_data(POKEMON_TYPES_FILE_PATH)


class Pokemon:
    def __init__(self, name, visible_name, type, color, stats, abilities):
        self.name = name
        self.visible_name = visible_name
        self.type = type
        self.color = color
        self.stats = stats
        self.current_hp = int(stats["hp"])
        self.abilities = abilities

    def __repr__(self) -> str:
        return (
            str(self.name)
            + "\n"
            + str(self.type)
            + "\n"
            + str(self.abilities)
            + "\n"
            + str(self.stats)
        )

    def __str__(self) -> str:
        return (
            set_console_style("bright")
            + set_console_color(self.color)
            + self.visible_name
            + reset_console_ansi_escapes()
        )

    def get_ascii_art(self) -> str:
        return read_ascii_art(POKEMON_ASCII_ART_PATH, self.name)

    def get_ascii_art_color(self) -> str:
        ascii_art = read_ascii_art(POKEMON_ASCII_ART_PATH, self.name)
        lines = ascii_art.split('\n')
        colored_lines = [f"{set_console_color(self.color)}{line}{reset_console_color()}" for line in lines]
        return '\n'.join(colored_lines)

    def get_visual_stats_sprite(self) -> str:
        max_hp = self.stats["hp"]
        current_hp = self.current_hp
        health_percentage = (current_hp / max_hp) * 100
        bar_length = int(health_percentage / 2)

        health_indicator = (
            "HP: "
            + set_console_style("bright")
            + set_console_color(self.color)
            + str(current_hp)
            + reset_console_ansi_escapes()
            + " / "
            + str(max_hp)
        )

        # ansii characters are counted as well
        unstyled_health_indicator = "HP: " + str(current_hp) + " / " + str(max_hp)

        health_indicator += (" ") * (52 - len(unstyled_health_indicator))

        health_bar = (
            set_console_color(self.color)
            + "["
            + reset_console_color()
            + "#" * bar_length
            + "-" * (48 - bar_length)
            + set_console_color(self.color)
            + "]"
            + reset_console_color()
        )

        ascii_art = self.get_ascii_art_color()

        combined_sprite = ascii_art + "\n" + health_indicator + "\n" + health_bar

        return combined_sprite

    def get_abilities_list(self):
        return [
            pokemon_abilities[ability]["visible_name"]
            for ability in pokemon_abilities
            if self.abilities.count(ability) > 0
        ]


class Ability:
    def __init__(self):
        pass


class Type:
    def __init__(self):
        pass


def choose_pokemon():
    pokemon_list = []

    for name in pokemon_list_data:
        pokemon_data = pokemon_list_data[name]

        pokemon = Pokemon(
            name=name,
            visible_name=pokemon_data["visible_name"],
            type=pokemon_data["type"],
            color=pokemon_data["color"],
            stats=pokemon_data["stats"],
            abilities=pokemon_data["abilities"],
        )

        pokemon_list.append(pokemon)

    pokemon_choose_list = [pokemon.visible_name for pokemon in pokemon_list]

    confirmed = False

    while not confirmed:
        clear_screen.clear()
        time.sleep(0.8)

        print(
            "Select a "
            + set_console_color("blue")
            + "Pokè"
            + set_console_color("yellow")
            + "mon"
            + reset_console_ansi_escapes()
            + "\n"
        )

        selected_pokemon_name = questionary.select(
            "",
            qmark="",
            choices=pokemon_choose_list,  # Use a lambda function
        ).ask()

        clear_screen.clear()
        time.sleep(0.8)

        confirmed = questionary.confirm(
            "Do you want to choose " + str(selected_pokemon_name) + "?"
        ).ask()

        if confirmed:
            selected_pokemon = next(
                pokemon
                for pokemon in pokemon_list
                if pokemon.visible_name == selected_pokemon_name
            )
            break

    return selected_pokemon


def random_pokemon():
    pokemon_list_names = list(pokemon_list_data.keys())
    pokemon_index = random.randint(0, len(pokemon_list_data) - 1)
    selected_pokemon_name = pokemon_list_names[pokemon_index]
    pokemon_data = pokemon_list_data[selected_pokemon_name]

    pokemon = Pokemon(
        name=selected_pokemon_name,
        visible_name=pokemon_data["visible_name"],
        type=pokemon_data["type"],
        color=pokemon_data["color"],
        stats=pokemon_data["stats"],
        abilities=pokemon_data["abilities"],
    )

    return pokemon
