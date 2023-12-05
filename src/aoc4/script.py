import math


def get_source_data(file: str) -> list:
    """Import source data and strip eol characters"""
    with open(file, "r") as input_file:
        return [line.strip() for line in input_file.readlines()]


def get_card_points(card: str) -> int:
    card_name, raw = card.split(":")
    winning_tmp, actual_tmp = raw.split("|")
    winning = set(winning_tmp.strip().split())
    actual = set(actual_tmp.strip().split())
    winners = winning.intersection(actual)
    if len(winners) == 0:
        return 0
    else:
        points = 1 * math.pow(2, len(winners) - 1)
        # print(f"{card_name} has {len(winners)} winners and returns {points} points")
        return points


def get_cards_won(card: str) -> int:
    card_name, raw = card.split(":")
    winning_tmp, actual_tmp = raw.split("|")
    winning = set(winning_tmp.strip().split())
    actual = set(actual_tmp.strip().split())
    winners = winning.intersection(actual)
    return len(winners)


def part1_total_points(scratch_cards: list) -> int:
    return int(sum([get_card_points(card) for card in scratch_cards]))


def part2_total_cards(scratch_cards: list) -> int:
    winners = {}
    for card in reversed(scratch_cards):
        card_name = int(card.split(":")[0].split()[1])
        cards_won = get_cards_won(card)
        winners[card_name] = cards_won + sum(
            [winners.get(card_name + i) for i in range(1, cards_won + 1)]
        )
    return len(scratch_cards) + sum(list(winners.values()))


if __name__ == "__main__":
    scratch_cards = get_source_data("src\\aoc4\\input.txt")
    total_points = part1_total_points(scratch_cards)
    print(f"Total Points: {total_points}")
    total_cards_won = part2_total_cards(scratch_cards)
    print(f"Total Cards Won: {total_cards_won}")
