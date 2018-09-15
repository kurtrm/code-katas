"""
"""


def removeElement(nums, val):
    """
    """
    while True:
        try:
            nums.remove(val)
        except ValueError:
            return len(nums)
