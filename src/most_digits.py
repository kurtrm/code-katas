"""Kata: Most Digits - Return number with the most digits

#1 Best Practices Solution Unnamed & Others

def find_longest(xs):
    return max(xs, key=lambda x: len(str(x)))
"""


def find_longest(arr):
    """Return number with the most digits"""
    num = ''
    for number in arr:
        if len(str(number)) > len(str(num)):
            num = number
    return num
