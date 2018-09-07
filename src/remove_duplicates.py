"""
"""
from collections import Counter


def removeDuplicates(nums):
    """
    """
    counts = Counter(nums)
    for key, value in counts.items():
        for _ in range(value - 1):
            nums.remove(key)
    return len(nums)


def removeDuplicates2(nums):
    """
    """
    for i in range(len(nums)):
        if i == 0:
            num = nums[i]
        else:
            while nums[i] == num:
                try:
                    del nums[i]
                except IndexError:
                    pass
            else:
                num = nums[i]
    return len(nums)


if __name__ == '__main__':
    original = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(f'Original length: {len(original)}')
    x = removeDuplicates(original)
    print(f'In place modification length: {x}')
