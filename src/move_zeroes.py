"""
"""


def moveZeroes(nums):
    """
    """
    counts = 0
    for _ in enumerate(nums):
        try:
            nums.remove(0)
            counts += 1
        except ValueError:
            pass
    for _ in range(counts):
        nums.append(0)
