"""Test is_thue_morse function
"""

import pytest

PARAMS_TABLE = [
    ([0, 1, 1, 0, 1], True),
    ([0], True),
    ([1], False),
    ([0, 1, 0, 0], False),
    ([0, 1, 1, 0, 1, 0, 1, 0], False),
    ([0, 1, 1, 0, 1, 0, 0, 1, 1, 0], True),
    ([0, 1, 1, 1], False),
    ([1, 0, 0, 1, 0, 0, 1], False)
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_is_thue_morse(l, result):
    """Test test_is_thue_morse function"""
    from Is_Thue_Morse import is_thue_morse
    assert is_thue_morse(l) == result
