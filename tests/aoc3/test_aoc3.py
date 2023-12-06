import pytest
from src.aoc3.script import *


def test_sample_input_given_part1():
    schematic = input_per_line("tests\\aoc3\\sample.txt")
    part_numbers = get_genuine_part_numbers(schematic)
    assert sum(part_numbers) == 4361


def test_sample_input_given_part2():
    schematic = input_per_line("tests\\aoc3\\sample.txt")
    gear_ratios = get_gear_ratios(schematic)
    assert sum(gear_ratios) == 467835
