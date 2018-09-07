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


if __name__ == '__main__':
    x = removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(x)
