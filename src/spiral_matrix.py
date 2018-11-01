"""
"""


def spiral_matrix(R, C, r0, c0):
    """
    2 moves starting at 1
    right down left up right down left up ...
    1     1    2    2  3     3    4    4  ...
    c+    r+   c-   r- c+    r+   c-   r- ...
    """
    stp = [r0, c0]
    all_stps = [list(stp)]
    ser = 1
    lists = [[False] * C for _ in range(R)]
    for i in range(1, 1000000):
        for idx in [1, 0]:
            for _ in range(i):
                stp[idx] += ser
                try:
                    if not any([idx < 0 for idx in stp]):
                        lists[stp[0]][stp[1]] = True
                        all_stps.append(list(stp))
                except IndexError:
                    continue
        ser *= -1

    return all_stps
