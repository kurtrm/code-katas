"""
Partition a string such that each letter is in at most 1 part.
"""


def partition_labels(S):
    """
    """
    partitions = []
    highest = {item: idx for idx, item in enumerate(S)}
    lowest = {item: S.index(item) for item in set(S)}
    ranges = sorted([(lowest[key], highest[key]) for key in highest],
                    key=lambda x: x[0])
    low, hi = ranges.pop(0)
    for first, second in ranges:
        if low < first < hi:
            if second > hi:
                hi = second
        else:
            partitions.append(S[low:first])
            low, hi = first, second
    partitions.append(S[low:])
    return partitions
