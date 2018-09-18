"""
"""


def maxIncreaseKeepingSkyline(grid):
    """
    """
    total = 0
    max_tb = [max(row[i] for row in grid) for i in range(len(grid))]
    for i, row in enumerate(grid):
        max_lr = max(row)
        for j, col in enumerate(row):
            cum_min = min(max_lr, max_tb[j])
            total += (cum_min - col)

    return total


if __name__ == '__main__':
    grid = [[3, 0, 8, 4],
            [2, 4, 5, 7],
            [9, 2, 6, 3],
            [0, 3, 1, 0]]
    print(maxIncreaseKeepingSkyline(grid))
