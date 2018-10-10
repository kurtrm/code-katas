"""
Sort an array by parity.
"""


def sort_by_parity(A):
    """
    """
    idxed = [(num, num % 2) for num in A]
    sorted_idxed = sorted(idxed, key=lambda x: x[1], reverse=False)
    first_nums, _ = zip(*sorted_idxed)
    return list(first_nums)
