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
    card_groups = []
    counted = set()
    for card in cards:
        if card not in counted:
            c = cards.count(card)
            card_groups.append(c)
            counted.add(card)
    return sorted(card_groups, reverse=True)


def get_card_frequencies_jokers(cards: list) -> list:
    """
    Return a list of frequencies of each card in the hand.
    The list should be ordered from most frequent to least frequent.
    Jokers are wild here, so we should add them to the most frequently encountered card's frequency value.
    If we only get jokers, return 5.
    """
    card_groups = []
    counted = set()
    js = 0
    for card in cards:
        if card not in counted and card != "J":
            c = cards.count(card)
            card_groups.append(c)
            counted.add(card)
        if card == "J":
            js += 1
    if js == 5:  # edge case - are there any others???
        return [5]
    ranked_card_groups = sorted(card_groups, reverse=True)
    # best place to add the J will always be the largest group of cards
    ranked_card_groups[0] += js
    return ranked_card_groups


def score_hand(hand: str, jokers_wild: bool = False) -> list:
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
    cards = [*hand]
    if jokers_wild:
        hand_scores = get_card_frequencies_jokers(cards)
    else:
        hand_scores = get_card_frequencies(cards)

    if hand_scores[0] == 5:
        score = [6]
    elif hand_scores[0] == 4:
        score = [5]
    elif hand_scores[0] == 3 and hand_scores[1] == 2:
        score = [4]
    elif hand_scores[0] == 3:
        score = [3]
    elif hand_scores[0] == 2 and hand_scores[1] == 2:
        score = [2]
    elif hand_scores[0] == 2:
        score = [1]
    else:
        score = [0]  # weakest hand first
    if jokers_wild:
        score.extend([card_order_js.index(card) for card in cards])
    else:
        score.extend([card_order.index(card) for card in cards])
    return score


if __name__ == "__main__":
    hands = import_cards("src\\aoc7\\input.txt")
    ordered_hands = sorted(hands, key=lambda hand: score_hand(hand[0]))
    total_winnings = sum([j[1] * (i + 1) for i, j in enumerate(ordered_hands)])
    print(f"Total Winnings: {total_winnings}")

    hands = import_cards("src\\aoc7\\input.txt")
    ordered_hands = sorted(
        hands, key=lambda hand: score_hand(hand[0], jokers_wild=True)
    )
    total_winnings = sum([j[1] * (i + 1) for i, j in enumerate(ordered_hands)])
    print(f"Total Winnings: {total_winnings}")
