import re


def get_source_data(file: str) -> list:
    """Import source data and strip eol characters"""
    with open(file, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def filter_by_number(line: str) -> list[str]:
    return [
        character
        for character in line
        if character in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    ]


def create_number(numbers: list[str]) -> int:
    return int(f"{numbers[0]}{numbers[-1]}")


def filter_by_number_part2(line: str) -> list[str]:
    """Find all integers and integers which are strings. Then translate the strings back into ints"""
    # compiling here should help with performance
    search_pattern = re.compile(
        r"(?=(1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine|zero))"
    )
    patterns_found = re.findall(search_pattern, line)
    translation = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    return [
        translation[pattern] if pattern in translation.keys() else pattern
        for pattern in patterns_found
    ]


if __name__ == "__main__":
    calibrations = get_source_data("src\\aoc1\\input.txt")
    calibration_numbers = [
        create_number(filter_by_number(line)) for line in calibrations
    ]
    calibration_sum = sum(calibration_numbers)
    print(f"Calibration Sum Part 1: {calibration_sum}")

    calibration_numbers = [
        create_number(filter_by_number_part2(line)) for line in calibrations
    ]
    calibration_sum = sum(calibration_numbers)
    print(f"Calibration Sum Part 2: {calibration_sum}")
