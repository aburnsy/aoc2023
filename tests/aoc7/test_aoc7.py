import pytest
from src.aoc7.script import *


def test_sample_input_given_part1():
    hands = import_cards("tests\\aoc7\\sample.txt")
    ordered_hands = sorted(hands, key=lambda x: x[2])
    total_winnings = sum([j[1] * (i + 1) for i, j in enumerate(ordered_hands)])
    assert total_winnings == 6440


def test_sample_input_given_part2_js():
    hands = import_cards("tests\\aoc7\\sample2.txt", jokers_wild=True)
    ordered_hands = sorted(hands, key=lambda x: x[2])
    total_winnings = sum([j[1] * (i + 1) for i, j in enumerate(ordered_hands)])
    assert total_winnings == 7365


def test_sample_input_given_part2():
    hands = import_cards("tests\\aoc7\\sample.txt", jokers_wild=True)
    ordered_hands = sorted(hands, key=lambda x: x[2])
    total_winnings = sum([j[1] * (i + 1) for i, j in enumerate(ordered_hands)])
    assert total_winnings == 5905
