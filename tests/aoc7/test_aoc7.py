import pytest
from src.aoc7.script import *


def test_sample_input_given_part1():
    hands = import_cards("tests\\aoc7\\sample.txt")
    total_winnings = get_winnings(hands)
    assert total_winnings == 6440


def test_sample_input_given_part2_js():
    hands = import_cards("tests\\aoc7\\sample2.txt")
    total_winnings = get_winnings(hands, jokers_wild=True)
    assert total_winnings == 7365


def test_sample_input_given_part2():
    hands = import_cards("tests\\aoc7\\sample.txt")
    total_winnings = get_winnings(hands, jokers_wild=True)
    assert total_winnings == 5905
