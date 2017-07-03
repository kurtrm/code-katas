"""Test the proper parenthetics script."""
import pytest


PARAMS_TABLE = [
    ('()()()()()()()', 0),
    ('((((((()))))))', 0),
    (')))))(((((', -1),
    (')))))((((((', -1),
    ('(((((()))))', 1),
    ('((((())))))', -1),
    ('((()()(()((())))(', 1),
    ('(()))(()()()(()(())(()))', -1),
    ('()()()()((((())))))(((()(()()', -1),
    ('((()))()()((())())()())()', 0)
]


@pytest.mark.parametrize('parentheses, result', PARAMS_TABLE)
def test_against_params(parentheses, result):
    """Test against the generated tests."""
    from proper_parenthetics import parenthetics
    assert parenthetics(parentheses) == result
