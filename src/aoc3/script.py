"""Solution to AoC 2023 Day 03: Gear Ratios"""

not_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]


def input_per_line(file: str):
    """Import the file and strip out line breaks"""
    with open(file, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def is_cell_adjacent(schematic: list, i: int, j: int) -> bool:
    return any(
        schematic[i + a][j + b] not in not_symbols
        for a in [-1, 0, 1]
        for b in [-1, 0, 1]
        if i + a > 0 and j + b > 0 and i + a < len(schematic) and j + b < len(schematic)
    )


def get_genuine_part_numbers(schematic: list) -> list:
    part_numbers = []
    part_number = ""
    part_number_genuine = False

    for i in range(len(schematic)):
        for j in range(len(schematic[0])):
            curr = schematic[i][j]
            if curr in not_symbols and curr != ".":
                part_number = part_number + curr
                if not part_number_genuine:
                    # Check every adjacent cell to see if we are beside a not_symbol
                    part_number_genuine = is_cell_adjacent(schematic, i, j)
            else:
                if part_number != "":
                    if part_number_genuine:
                        part_numbers.append(int(part_number))
                    part_number = ""
                    part_number_genuine = False
    return part_numbers


"""Solution to AOC Day 3 Part II"""
ints = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def get_schematic(file: str):
    with open(file, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def get_adjacent_part_numbers(schematic, i, j):
    height = len(schematic)
    width = len(schematic[0])
    part_numbers = []
    part_numbers_cells = []
    for a in [-1, 0, 1]:
        for b in [-1, 0, 1]:
            if i + a >= 0 and j + b >= 0 and i + a < height and j + b < width:
                if (
                    schematic[i + a][j + b] in ints
                    and not (i + a, j + b) in part_numbers_cells
                ):
                    fn = get_full_number(schematic, i + a, j + b)
                    part_numbers.append(fn["part_number"])
                    part_numbers_cells.extend(fn["cells"])
    return part_numbers


def get_full_number(schematic: list, i: int, j: int) -> dict:
    height = len(schematic)
    width = len(schematic[0])
    y = j
    while True:
        if y - 1 < 0 or schematic[i][y - 1] not in ints:
            break
        else:
            y = y - 1
    part_number_tmp = schematic[i][y]
    cells = [(i, y)]
    while True:
        if y + 1 == height or schematic[i][y + 1] not in ints:
            break
        else:
            y = y + 1
            cells.append((i, y))
            part_number_tmp = part_number_tmp + schematic[i][y]
    part_number = int("".join(part_number_tmp))
    return {"part_number": part_number, "cells": cells}


def get_gear_ratios(schematic: list) -> list:
    height = len(schematic)
    width = len(schematic[0])
    gear_ratios = []

    for i in range(height):
        for j in range(width):
            if schematic[i][j] == "*":
                part_numbers = get_adjacent_part_numbers(schematic, i, j)
                if len(part_numbers) == 2:
                    gear_ratios.append(part_numbers[0] * part_numbers[1])

    return gear_ratios


if __name__ == "__main__":
    schematic = input_per_line("src\\aoc3\\input.txt")
    part_numbers = get_genuine_part_numbers(schematic)
    print(f"The sum of all valid part numbers is: {sum(part_numbers)}")
    gear_ratios = get_gear_ratios(schematic)
    sum_of_gear_ratios = sum(gear_ratios)
    print(f"The sum of gear ratios is {sum_of_gear_ratios}")
