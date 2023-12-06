import pytest
from src.aoc6.script import *
import math


def test_sample_input_given_part1():
    races = get_source_data("tests\\aoc6\\sample.txt")
    winning_ways = [get_ways_to_win(race) for race in races]
    assert math.prod(winning_ways) == 288


def test_sample_input_given_part2():
    race = get_source_data_part2("tests\\aoc6\\sample.txt")
    winning_ways = get_ways_to_win(race)
    assert winning_ways == 71503


def test_sample_input_given_part2_eqn():
    race = get_source_data_part2("tests\\aoc6\\sample.txt")
    winning_ways = get_ways_to_win_eqn(race)
    assert winning_ways == 71503
