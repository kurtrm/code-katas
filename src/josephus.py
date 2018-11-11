"""
2**0
2**1
"""


def solve_josephus(N):
    """
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 3, 4, 5, 6, 7, 8, 9, 10]
    [1, 3, 4, 6, 7, 8, 9, 10]
    [1, 3, 5, 6, 8, 9, 10]
     0  1  2  3  4  5  6  7  8  9 
    [1, 3, 5, 7, 9]
     0  2  4  6  8
     0  1  2  3  4
    [1, 5, 9]
     0  4  8
    [5]
     4
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
     0  1  2  3  4  5  6  7  8  9   10
    [1, 3, 5, 7, 9, 11]
     0  1  2  3  4  5
    [3, 7, 11]
     0  1  2
    [7]
     0
    """
    all_folks = list(range(1, N+1))
    i = 1
    last = all_folks[-1]
    while len(all_folks) > 1:
        try:
            del all_folks[i]
            i += 1
        except IndexError:
            if last == all_folks[-1]:
                i = 0
            else:
                i = 1
            last = all_folks[-1]

    return all_folks[0]
