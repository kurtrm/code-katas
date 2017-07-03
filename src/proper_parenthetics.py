"""Function to process a set of parentheses and return if

it's balanced, broken, or open.
"""
import re


def parenthetics(parentheses):
    """Process the set of parentheses."""
    if isinstance(parentheses, str):
        raise TypeError('Please provide a string.')
    if re.search(r'[^\()]', parentheses):
        raise ValueError('Please provide either ( or ) only.')
