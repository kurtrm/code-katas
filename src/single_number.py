"""
"""


def single_number(nums):
    """
    """
    counts = {}
    for num in nums:
        try:
            del counts[num]
        except KeyError:
            counts[num] = 1
    for num, count in counts.items():
        return num


if __name__ == '__main__':
    nums = [4, 1, 2, 1, 2]
    print(single_number(nums))
