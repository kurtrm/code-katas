"""Function to process a set of parentheses and return if

balanced: 0 '()'
broken: -1 ')'
open: 1 '('

"""
import re


def parenthetics(parentheses):
    """Process the set of parentheses."""
    if isinstance(parentheses, str):
        raise TypeError('Please provide a string.')
    if re.search(r'[^\(\)]', parentheses):
        raise ValueError('Please provide either ( or ) only.')
    count = 0
    for paren in parentheses:
        if paren == '(':
            count += 1
        elif paren == ')':
            count -= 1
        if count < 0:
            return -1
    return 0 if count == 0 else 1
