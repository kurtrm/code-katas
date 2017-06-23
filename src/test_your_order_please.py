"""Test order function
"""

import pytest

PARAMS_TABLE = [
    ("is2 Thi1s T4est 3a", "Thi1s is2 3a T4est"),
    ("man2y H1ow i3s 4this", "H1ow man2y i3s 4this"),
    ("fo4r re3ady the5 1I weeke6nd 2am", "1I 2am re3ady fo4r the5 weeke6nd"),
    ("not4 o3r Py2thon 1To P6ython t5o", "1To Py2thon o3r not4 t5o P6ython"),
    ("yea1h", "yea1h"),
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_order(l, result):
    """Test order function"""
    from your_order_please import order
    assert order(l) == result
