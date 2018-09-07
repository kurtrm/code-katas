"""
"""
from collections import Counter
import timeit


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
    num = nums[0]
    for i in range(1, len(nums)):
        try:
            while nums[i] == num:
                del nums[i]
            else:
                num = nums[i]
        except IndexError:
            pass
    return len(nums)

setup = """
from collections import Counter
original = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDuplicates(nums):

    counts = Counter(nums)
    for key, value in counts.items():
        for _ in range(value - 1):
            nums.remove(key)
    return len(nums)


def removeDuplicates2(nums):

    for i in range(len(nums)):
        if i == 0:
            num = nums[i]
        else:
            try:
                while nums[i] == num:
                    del nums[i]
                else:
                    num = nums[i]
            except IndexError:
                pass
    return len(nums)
"""

if __name__ == '__main__':
    original = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    # print(f'Original length: {len(original)}')
    # x = removeDuplicates2(original)
    # print(f'In place modification length: {x}')
    first = timeit.timeit("removeDuplicates(original)", number=10000, setup=setup)
    second = timeit.timeit("removeDuplicates2(original)", number=10000, setup=setup)
    print(f"Original implementation: {first} seconds")
    print(f"Refactored implementation: {second} seconds")
