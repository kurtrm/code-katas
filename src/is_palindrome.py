"""
"""
from string import punctuation


def is_palindrome(s):
    """
    """
    puncs = set(punctuation)
    puncs.add(" ")
    merged = [letter for letter in s.lower() if letter not in puncs]
    # import pdb; pdb.set_trace()
    return merged == merged[::-1]
