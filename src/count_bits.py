"""
"""


def count_bits(num: int) -> list:
    """
    counts = []
    range(num)
    iterative over range
    for each i in range(num):
        count = 0
        for each let in bin(i)[2:]
            if let == '1'
                count += 1
        counts.append(count)
    return counts
    """
    # Type check arguments: raise Error
    counts = []
    for i in range(num+1):
        count = 0
        for bit in bin(i)[2:]:
            if bit == '1':
                count += 1
        counts.append(count)  # rather than return a list, yield each count
    return counts
