"""Test counter_effect function
"""

import pytest

PARAMS_TABLE = [
    ("1250", [[0, 1], [0, 1, 2], [0, 1, 2, 3, 4, 5], [0]]),
    ("0050", [[0], [0], [0, 1, 2, 3, 4, 5], [0]]),
    ('0000', [[0], [0], [0], [0]]),
    ("0147", [[0], [0, 1], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4, 5, 6, 7]]),
    ("9351", [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3], [0, 1, 2, 3, 4, 5], [0, 1]]),
    ("0832", [[0], [0, 1, 2, 3, 4, 5, 6, 7, 8], [0, 1, 2, 3], [0, 1, 2]]),
    ("1021", [[0, 1], [0], [0, 1, 2], [0, 1]]),
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_counter_effect(l, result):
    """Test counter_effect function"""
    from hit_count import counter_effect
    assert counter_effect(l) == result
