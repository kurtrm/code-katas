"""
Count and say problem.
"""
from collections import defaultdict, Counter


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
    new_num = ""
    for i in range(nummy):
        current_digit = None
        counts = []
        for digit in num:
            if current_digit is None:
                counts.append(digit)
                counts.append(1)
                current_digit = digit
            elif counts[0] == digit:
                counts[1] += 1
            else:
                # import pdb; pdb.set_trace()
                new_num += (counts[0] + str(counts[1]))
                counts = []
                counts.append(digit)
                counts.append(1)
                current_digit = digit
        new_num += (counts[0] + str(counts[1]))
        num = new_num
        new_num = ""

    return num


if __name__ == '__main__':
    x = countAndSay(4)
    print(x)
