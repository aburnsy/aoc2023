import pytest
from src.aoc4.script import *


def test_sample_input_given_part1():
    scratch_cards = get_source_data("tests\\aoc4\\sample.txt")
    output = part1_total_points(scratch_cards)
    assert output == 13


def test_sample_input_given_part2():
    scratch_cards = get_source_data("tests\\aoc4\\sample.txt")
    output = part2_total_cards(scratch_cards)
    assert output == 30
