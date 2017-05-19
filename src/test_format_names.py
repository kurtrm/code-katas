"""Test namelist function
"""

import pytest

PARAMS_TABLE = [
    ([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}],
        'Bart, Lisa, Maggie, Homer & Marge'),
    ([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'}], 'Bart, Lisa & Maggie'),
    ([{'name': 'Bart'},{'name': 'Lisa'}], 'Bart & Lisa'),
    ([{'name': 'Bart'}], 'Bart'),
    ([], ''),
    ([{'name': 'Melissa'}, {'name': 'Marley'}], 'Melissa & Marley'),
    ([{'name': 'Who'}, {'name': 'What'}, {'name': 'When'}, {'name': 'Where'}], 'Who, What, When & Where'),
    ([{'name': 'Toby'}], 'Toby'),
    ([{'name': 'Wes'},{'name': 'Jaron'},{'name': 'Zach'},{'name': 'Matt'},{'name': 'Cameron'}],
        'Wes, Jaron, Zach, Matt & Cameron'),

]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_namelist(l, result):
    """Test namelist function"""
    from format_names import namelist
    assert namelist(l) == result