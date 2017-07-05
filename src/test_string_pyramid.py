"""Test the string pyramid functions. Taken from codewars.com."""
import pytest


def my_count_visible_characters_of_the_pyramid(characters):
    """Return correct number of visible characters."""
    return (2 * len(characters) - 1) ** 2


def my_count_all_characters_of_the_pyramid(characters):
    """Return correct number of visible characters."""
    return sum(a ** 2 for a in range(1, 2 * len(characters), 2))


def test_handles_none():
    """."""
    from string_pyramid import (
        watch_pyramid_from_above,
        watch_pyramid_from_the_side,
        count_visible_characters_of_the_pyramid,
        count_all_characters_of_the_pyramid
    )
    assert (watch_pyramid_from_above(None),
            watch_pyramid_from_the_side(None),
            count_all_characters_of_the_pyramid(None),
            count_visible_characters_of_the_pyramid(None)) == (
        None, None, -1, -1)


def test_handles_empty_string():
    """."""
    from string_pyramid import (
        watch_pyramid_from_above,
        watch_pyramid_from_the_side,
        count_visible_characters_of_the_pyramid,
        count_all_characters_of_the_pyramid
    )
    assert (watch_pyramid_from_above(''),
            watch_pyramid_from_the_side(''),
            count_all_characters_of_the_pyramid(''),
            count_visible_characters_of_the_pyramid('')) == (
        '', '', -1, -1)


def test_basic_characters():
    """."""
    from string_pyramid import (
        watch_pyramid_from_above,
        watch_pyramid_from_the_side,
        count_visible_characters_of_the_pyramid,
        count_all_characters_of_the_pyramid
    )
    assert (watch_pyramid_from_above('*#'),
            watch_pyramid_from_the_side('*#'),
            count_all_characters_of_the_pyramid('*#'),
            count_visible_characters_of_the_pyramid('*#')) == (
'''\
***
*#*
***''','''\
 # 
***''', 10, 9)
