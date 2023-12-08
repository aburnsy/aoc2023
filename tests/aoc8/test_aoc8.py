import pytest
from src.aoc8.script import *


def test_sample_input_given_part1():
    navigations, nodes = load_data("tests\\aoc8\\sample.txt")
    steps = get_steps_to_zzz(navigations, nodes)
    assert steps == 6


def test_sample_input_given_part2():
    navigations, nodes = load_data("tests\\aoc8\\sample2.txt")
    steps = get_steps_to_zzz_p2(navigations, nodes)
    assert steps == 6
