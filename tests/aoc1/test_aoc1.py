import pytest
from src.aoc1.script import *


def test_sample_input_given_part1():
    calibrations = get_source_data("tests\\aoc1\\sample1.txt")
    calibration_numbers = [
        create_number(filter_by_number(line)) for line in calibrations
    ]
    calibration_sum = sum(calibration_numbers)
    assert calibration_sum == 142


def test_sample_input_given_part2():
    calibrations = get_source_data("tests\\aoc1\\sample2.txt")
    calibration_numbers = [
        create_number(filter_by_number_part2(line)) for line in calibrations
    ]
    calibration_sum = sum(calibration_numbers)
    assert calibration_sum == 281
