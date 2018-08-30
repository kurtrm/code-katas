"""
Code Wars kata 'Form the Minimum'
"""
from typing import Sequence


def min_value(digits: Sequence[int]) -> int:
    """
    From a sequence of digits, return the smallest
    value that can be created via a combination of non-repeating
    digits.
    """
    unique_digits = set(digits)
    return int(''.join(str(dgt) for dgt in sorted(unique_digits)))
