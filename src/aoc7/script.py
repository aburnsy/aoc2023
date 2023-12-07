from itertools import groupby

card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_order.reverse()

card_order_js = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
card_order_js.reverse()


def import_cards(file: str) -> list:
    """Import the hands and convert each bid to an integer."""
    with open(file, "r") as input_file:
        hands_tmp = [line.strip() for line in input_file.readlines()]
        return [
            [
                hand.split()[0],
                int(hand.split()[1]),
            ]
            for hand in hands_tmp
        ]


def get_card_frequencies(cards: list) -> list:
    """
    Return a list of frequencies of each card in the hand.
    The list should be ordered from most frequent to least frequent.
    """
    return sorted(
        [len(list(g)) for card, g in groupby(sorted(cards))],
        reverse=True,
    )


def get_card_frequencies_jokers(cards: list) -> list:
    """
    Return a list of frequencies of each card in the hand.
    The list should be ordered from most frequent to least frequent.
    Jokers are wild here, so we should add them to the most frequently encountered card's frequency value.
    If we only get jokers, return 5.
    """
    card_frequencies = sorted(
        [len(list(g)) for card, g in groupby(sorted(cards)) if card != "J"],
        reverse=True,
    )
    js = cards.count("J")
    if js == 5:  # edge case - are there any others???
        return [5]
    # best place to add the J will always be the largest group of cards
    card_frequencies[0] += js
    return card_frequencies


def score_hand(cards: list, jokers_wild: bool) -> list:
    """Return a list of scores, which can then be ordered later to compare hands.
    The first entry in the list should be the type of hand:
        5 of a kind = 5
        4 of a kind = 4
        3 of a kind = 3
        etc.
    The next 5 entries in the list correspond to each cards score where
        A = 12
        K = 11
        ...
        2 = 0
    When Js are wild, J scores the lowest.
    """

    hand_scores = (
        get_card_frequencies_jokers(cards)
        if jokers_wild
        else get_card_frequencies(cards)
    )

    score_map = [
        [1, 1, 1, 1, 1],
        [2, 1, 1, 1],
        [2, 2, 1],
        [3, 1, 1],
        [3, 2],
        [4, 1],
        [5],
    ]

    # The overall score is the hand score followed by each individual card score
    score = [
        score_map.index(hand_scores),
        *[
            card_order_js.index(card) if jokers_wild else card_order.index(card)
            for card in cards
        ],
    ]

    return score


def get_winnings(hands: list, jokers_wild: bool = False):
    ordered_hands = sorted(hands, key=lambda hand: score_hand([*hand[0]], jokers_wild))
    return sum([j[1] * (i + 1) for i, j in enumerate(ordered_hands)])


if __name__ == "__main__":
    hands = import_cards("src\\aoc7\\input.txt")
    total_winnings = get_winnings(hands)
    print(f"Total Winnings: {total_winnings}")

    hands = import_cards("src\\aoc7\\input.txt")
    total_winnings = get_winnings(hands, jokers_wild=True)
    print(f"Total Winnings: {total_winnings}")
