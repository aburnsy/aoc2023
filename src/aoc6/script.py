import math
import re
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        # first item in the args, ie `args[0]` is `self`
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


def get_source_data(file: str) -> list:
    """Import source data and split into array of tuples"""
    with open(file, "r") as input_file:
        times = [line.strip() for line in input_file.readlines()]
        return [
            (int(time), int(distance))
            for time, distance in zip(
                re.findall(r"\d+", times[0]), re.findall(r"\d+", times[1])
            )
        ]


def get_source_data_part2(file: str) -> (int, int):
    """Import source data and split into array of tuples"""
    with open(file, "r") as input_file:
        times = input_file.readlines()
        time = int("".join(re.findall(r"\d+", times[0])))
        distance = int("".join(re.findall(r"\d+", times[1])))
        return time, distance


# Brute force - could use quadratic equation instead?
@timeit
def get_ways_to_win(race: tuple) -> int:
    time = race[0]
    distance_to_beat = race[1]
    number_of_winners = 0
    for charging_time in range(1, time - 1):
        distance_travelled = charging_time * (time - charging_time)
        if distance_travelled > distance_to_beat:
            number_of_winners = number_of_winners + 1
    return number_of_winners


# ax**2 + bx + c = 0
# a = -1
# b = racing_time
# c = -distance_travelled
def equation_solve(a, b, c) -> int:
    x_1 = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    x_2 = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
    solutions = sorted(([x_1, x_2]))
    min_soln = math.ceil(solutions[0])
    max_soln = math.ceil(solutions[1])
    return max_soln - min_soln


@timeit
def get_ways_to_win_eqn(race: tuple) -> int:
    time = race[0]
    distance_to_beat = race[1]
    number_of_winners = equation_solve(-1, time, -distance_to_beat)
    return number_of_winners


if __name__ == "__main__":
    races = get_source_data("src\\aoc6\\input.txt")
    winning_ways = [get_ways_to_win(race) for race in races]
    result = math.prod(winning_ways)
    print(f"Product of ways to win: {result}")

    race = get_source_data_part2("src\\aoc6\\input.txt")
    winning_ways = get_ways_to_win(race)
    print(f"Winning ways part II: {winning_ways}")

    winning_ways2 = get_ways_to_win_eqn(race)
    print(f"Winning ways part II rework: {winning_ways2}")
