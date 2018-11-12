"""
"""


def solve_tower(source, aux, dest):
    """
    """
    if source[-1] == 1:
        dest.append(source.pop())
        solve_tower(source, aux, dest)
    pass

