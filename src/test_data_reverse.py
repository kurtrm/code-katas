"""Test data_reverse function
"""

import pytest

PARAMS_TABLE = [
    ([1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0],
    [1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]),
    ([0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1],
    [0,0,1,0,1,0,0,1,0,0,1,1,0,1,1,0]),
    ([0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1]),
    ([1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,1],[1,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0]),
    ([1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0], [0,1,1,1,0,0,0,0,1,0,1,0,1,0,1,0]),
    ([0,1,0,1,1,1,0,1], [0,1,0,1,1,1,0,1]),
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_data_reverse(l, result):
    """Test data_reverse function"""
    from data_reverse import data_reverse
    assert data_reverse(l) == result
