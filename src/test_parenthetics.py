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
    ('((()))()()((())())()())()', -1),
    ('((()))()()((())())()()((()))', 0),
    ('(((a))()((()', 1),
    ('(((a))()(fjdksla;dkjfh(()', 1),
    ('asdfjdksla;woei234387371', 'No parentheses in this string.'),
    ('trheadkfej)', -1),
    ('(as;dlkajfa;slk', 1),

]


@pytest.mark.parametrize('parentheses, result', PARAMS_TABLE)
def test_against_params(parentheses, result):
    """Test against the generated tests."""
    from proper_parenthetics import parenthetics
    assert parenthetics(parentheses) == result


def test_type_error():
    """Test that we get the type error if anything but a string is supplied."""
    from proper_parenthetics import parenthetics
    with pytest.raises(TypeError):
        parenthetics(2000)
