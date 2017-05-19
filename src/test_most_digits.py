"""Test most_digits function
"""

import pytest

PARAMS_TABLE = [
    ([1, 10, 100], 100),
    ([9000, 8, 800], 9000),
    ([8, 900, 500], 900),
    ([3, 40000, 100], 40000),
    ([1, 200, 100000], 100000),
    ([0, 2, 1], 0),
    ([1234542352345, 123409812730891623, 1235098123740192834],
        1235098123740192834),
    ([685494, 393022, 2011], 685494),
    ([1111, 12, 11111], 11111)
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_find_longest(l, result):
    """Test find_longest function"""
    from most_digits import find_longest
    assert find_longest(l) == result