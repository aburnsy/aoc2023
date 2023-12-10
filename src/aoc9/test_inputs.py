import pytest
from script import *


def test_sample_input_given_part1():
    report = get_env_report("src\\aoc9\\sample.txt")
    prediction = sum([get_env_prediction(line) for line in report])
    assert prediction == 114


def test_sample_input_given_part2_sample3():
    report = get_env_report("src\\aoc9\\sample.txt")
    backtests = get_env_prediction(report[2][::-1])
    assert backtests == 5


def test_sample_input_given_part2_sample2():
    report = get_env_report("src\\aoc9\\sample.txt")
    backtests = get_env_prediction(report[1][::-1])
    assert backtests == 0


def test_sample_input_given_part2():
    report = get_env_report("src\\aoc9\\sample.txt")
    backtests = sum([get_env_prediction(line[::-1]) for line in report])
    assert backtests == 2
