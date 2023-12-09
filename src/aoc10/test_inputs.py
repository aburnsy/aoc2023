import pytest
from script import *


def test_sample_input_given_part1():
    report = get_env_report("src\\aoc10\\sample.txt")
    prediction = sum([get_env_prediction(line) for line in report])
    assert prediction == 114


def test_sample_input_given_part2_sample3():
    report = get_env_report("src\\aoc10\\sample.txt")
    backtests = get_env_backtest(report[2])
    assert backtests == 5


def test_sample_input_given_part2_sample2():
    report = get_env_report("src\\aoc10\\sample.txt")
    backtests = get_env_backtest(report[1])
    assert backtests == 0


def test_sample_input_given_part2():
    report = get_env_report("src\\aoc10\\sample.txt")
    backtests = sum([get_env_backtest(line) for line in report])
    assert backtests == 2
