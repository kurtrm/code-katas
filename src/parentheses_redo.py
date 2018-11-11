"""
Refresher on proper parenthetics, not necessarily better.
"""
import sys


def proper_parenthetics(parentheses):
    """
    """
    count = 0
    escaped = False
    for let in parentheses:
        if count < 0:
            return False
        if escaped:
            escaped = False
            continue
        if let == '\\':
            escaped = True
        if let == '(':
            count += 1
        elif let == ')':
            count -= 1
    return count == 0


if __name__ == '__main__':
    arg = sys.argv[1]
    print(proper_parenthetics(arg))
