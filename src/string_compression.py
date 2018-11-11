"""
"""
import sys


def compress_string(string):
    """
    """
    letter_counts = {}
    for letter in string:
        try:
            letter_counts[letter] += 1
        except KeyError:
            letter_counts[letter] = 1

    partial_comp = [f'{letter}{count}'
                    for letter, count in letter_counts.items()]
    return "".join(partial_comp)


if __name__ == '__main__':
    stringy = sys.argv[1]
    print(compress_string(stringy))
