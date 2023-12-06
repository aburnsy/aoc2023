import pytest
from src.aoc2.script import *


def test_sample_input_given_part1():
    games_raw = input_per_line("tests\\aoc2\\sample.txt")
    games = [transform_games(game) for game in games_raw]
    valid_games = sum(game["name"] for game in games if game_is_valid(game))
    assert valid_games == 8


def test_sample_input_given_part2():
    games_raw = input_per_line("tests\\aoc2\\sample.txt")
    games = [transform_games(game) for game in games_raw]
    power_of_cubes_sum = sum(power_of_cubes(game) for game in games)
    assert power_of_cubes_sum == 2286
