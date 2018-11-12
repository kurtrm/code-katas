"""
"""
import sys


def merge_sorted_arrays(a, b):
    """
    """
    reversed_a = list(reversed(a))
    reversed_b = list(reversed(b))
    final = []
    for _ in range(len(a) + len(b)):
        try:
            if reversed_a[-1] <= reversed_b[-1]:
                final.append(reversed_a.pop())
            else:
                final.append(reversed_b.pop())
        except IndexError:
            final.extend(reversed_a if len(reversed_a) != 0 else reversed_b)
    return final


if __name__ == '__main__':
    arg1, arg2 = eval(sys.argv[1]), eval(sys.argv[2])
    print(merge_sorted_arrays(arg1, arg2))
