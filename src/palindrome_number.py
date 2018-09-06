"""
Determine if a number is a palindrome.
"""


def isPalindrome(x):
    """
    """
    if x < 0:
        return False
    digits = num_digits(x)
    cycles = digits // 2
    for i in range(cycles):
        if get_digit(x, i+1, digits) != get_digit(x, digits-i, digits):
            return False
    return True


def get_digit(num, place, digits=None):
    """
    """
    if digits is None:
        digits = num_digits(num)
    return (num // 10**(digits - place)) % 10


def num_digits(x):
    """
    """
    count = 0
    reduced = x
    while reduced > 0:
        count += 1
        reduced = reduced // 10

    return count
