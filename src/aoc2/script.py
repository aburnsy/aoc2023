"""Solution to AoC 2023 Day 02: Cube Conundrum """
import re


def input_per_line(file: str):
    """Import the text file and strip out newline characters"""
    with open(file, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def transform_sets(input_set: str) -> dict:
    result = {"red": 0, "green": 0, "blue": 0}
    input_sets = [cubes.strip().split(" ") for cubes in input_set.split(",")]
    for cubes in input_sets:
        result[cubes[1]] = int(cubes[0])
    return result


def transform_games(game: str) -> dict:
    raw = game.split(":")
    subsets = [transform_sets(subset) for subset in raw[1].split(";")]
    return {"name": int(raw[0].split(" ")[1]), "sets": subsets}


def set_is_valid(game_set: dict) -> bool:
    max_red = 12
    max_green = 13
    max_blue = 14
    return (
        game_set["red"] <= max_red
        and game_set["green"] <= max_green
        and game_set["blue"] <= max_blue
    )


def game_is_valid(game: dict) -> bool:
    return all(set_is_valid(game_set) for game_set in game["sets"])


def power_of_cubes(game: dict) -> int:
    return (
        max([set["red"] for set in game["sets"]])
        * max([set["green"] for set in game["sets"]])
        * max([set["blue"] for set in game["sets"]])
    )


if __name__ == "__main__":
    games_raw = input_per_line("src\\aoc2\\input.txt")
    games = [transform_games(game) for game in games_raw]
    valid_games = sum(game["name"] for game in games if game_is_valid(game))
    print(f"The number of valid games is {valid_games}")
    power_of_cubes_sum = sum(power_of_cubes(game) for game in games)
    print(f"The sum of the power of cubes is {power_of_cubes_sum}")
