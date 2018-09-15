"""
Count and say problem.
"""
from collections import defaultdict, Counter
import sys


# def num_digits(x):
#     """
#     """
#     count = 0
#     reduced = x
#     while reduced > 0:
#         count += 1
#         reduced = reduced // 10

#     return count


# def get_digit(num, place, digits=None):
#     """
#     """
#     if digits is None:
#         digits = num_digits(num)
#     return (num // 10**(digits - place)) % 10


# def countAndSay(n):
#     """
#     """
#     num = 1
#     counts = defaultdict(int)
#     for i in range(n):
#         num_digit = num_digits(num)
#         for x in num_digit:
#             digit = get_digit(num, i, num_digit)
#             counts[digit] += 1
#         for key, value in counts:

def countAndSay(nummy):
    """
    """
    num = "1"
    for i in range(nummy - 1):
        new_num = ""
        current_digit = None
        counts = {}
        for digit in num:
            if current_digit is None:
                counts[digit] = 1
                current_digit = digit
            else:
                try:
                    counts[digit] += 1
                except KeyError:
                    new_num += (str(counts[current_digit]) + current_digit)
                    counts = {}
                    counts[digit] = 1
                    current_digit = digit
        new_num += (str(counts[digit]) + current_digit)
        num = new_num

    return num


if __name__ == '__main__':
    i = sys.argv[1]
    x = countAndSay(int(i))
    print(x)
