# split() allows a second param - max

# quadratic equations
# https://www.khanacademy.org/math/algebra/x2f8bb11595b61c86:quadratic-functions-equations/x2f8bb11595b61c86:quadratic-formula-a1/v/using-the-quadratic-formula


def practice_groupby():
    """Day 7 Itertools Group by
    We needed to count the frequency of occurances of each card. Initially I performed this myself by looping through the cards and adding to a list and a set(for already counted cards)
    https://docs.python.org/3/library/itertools.html#itertools.groupby
    The returned group is itself an iterator that shares the underlying iterable with groupby(). Because the source is shared, when the groupby() object is advanced, the previous group is no longer visible. So, if that data is needed later, it should be stored as a list:
    """
    from itertools import groupby

    cards = list("K2K52")
    frequencies = sorted(
        [(card, len(list(freq_list))) for card, freq_list in groupby(sorted(cards))],
        key=lambda x: x[1],
        reverse=True,
    )
    print(frequencies)


def practice_counters():
    """Day 7 Counter objects
    Even better than group by is Counter tools
    A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
    """
    from collections import Counter

    cnt = Counter()
    for word in ["red", "blue", "red", "green", "blue", "blue"]:
        cnt[word] += 1
    print(cnt)
    cards = list("K2K52JJ")
    frequencies = [freq for card, freq in Counter(cards).most_common() if card != "J"]
    print(frequencies)


if __name__ == "__main__":
    practice_counters()
    practice_groupby()
