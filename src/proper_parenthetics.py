"""Function to process a set of parentheses and return if

balanced: 0 '()'
broken: -1 ')'
open: 1 '('

"""


def parenthetics(parentheses):
    """Process the set of parentheses."""
    if not isinstance(parentheses, str):
        raise TypeError('Please provide a string.')
    count = 0
    contains_paren = False
    for paren in parentheses:
        if paren in '()':
            contains_paren = True
            if paren == '(':
                count += 1
            else:
                count -= 1
            if count < 0:
                return -1
    if contains_paren:
        return 0 if count == 0 else 1
    else:
        return 'No parentheses in this string.'
