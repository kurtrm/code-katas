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
    counts = []
    for i in range(nummy):
        current_digit = None
        for digit in num:
            if current_digit is None:
                counts.append(digit)
                counts.append(1)
            elif counts[0] != digit:
                new_num += (counts[0] + str(counts[1]))
                counts = []
            import pdb; pdb.set_trace()
        num = new_num
        new_num = ""

    return num


if __name__ == '__main__':
    x = countAndSay(4)
    print(x)
