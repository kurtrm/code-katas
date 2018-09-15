"""
"""
from collections import Counter


def numJewelsInStones(J, S):
    """
    """
    counts = Counter(S)
    intersection = set(J) & set(counts.keys())
    return sum(counts[jewel] for jewel in intersection)


def alt(J, S):
    """
    fastest
    """
    counts = 0
    set_J = set(J)
    for stone in S:
        if stone in set_J:
            counts += 1
    return counts


def altalt(J, S):
    """
    """
    counts = Counter(S)
    total = 0
    for jewel in J:
        try:
            total += counts[jewel]
        except KeyError:
            continue

    return total
