"""Test the string pyramid functions. Taken from codewars.com."""


def my_count_visible_characters_of_the_pyramid(characters):
    """Return correct number of visible characters."""
    return (2 * len(characters) - 1) ** 2


def my_count_all_characters_of_the_pyramid(characters):
    """Return correct number of visible characters."""
    return sum(a ** 2 for a in range(1, 2 * len(characters), 2))


def test_handles_none():
    """Ensure the function handles none correctly."""
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
    """Ensure none can be passed in and validated."""
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
    """Test a basic bunch of characters."""
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
***''', '''\
 # 
***''', 10, 9)


def test_basic_abc():
    """Test using abc to get a proper pyramid."""
    from string_pyramid import (
        watch_pyramid_from_above,
        watch_pyramid_from_the_side,
        count_visible_characters_of_the_pyramid,
        count_all_characters_of_the_pyramid
    )
    assert (watch_pyramid_from_above('abc'),
            watch_pyramid_from_the_side('abc'),
            count_all_characters_of_the_pyramid('abc'),
            count_visible_characters_of_the_pyramid('abc')) == (
'''\
aaaaa
abbba
abcba
abbba
aaaaa''', '''\
  c  
 bbb 
aaaaa''', 35, 25)


def test_same_characters():
    """Test that same characters return valid pyramid."""
    from string_pyramid import (
        watch_pyramid_from_above,
        watch_pyramid_from_the_side,
        count_visible_characters_of_the_pyramid,
        count_all_characters_of_the_pyramid
    )
    assert (watch_pyramid_from_above('aaa'),
            watch_pyramid_from_the_side('aaa'),
            count_all_characters_of_the_pyramid('aaa'),
            count_visible_characters_of_the_pyramid('aaa')) == (
'''\
aaaaa
aaaaa
aaaaa
aaaaa
aaaaa''', '''\
  a  
 aaa 
aaaaa''', 35, 25)


def test_using_54321():
    """Test that numbers produce a valid pyramid."""
    from string_pyramid import (
        watch_pyramid_from_above,
        watch_pyramid_from_the_side,
        count_visible_characters_of_the_pyramid,
        count_all_characters_of_the_pyramid
    )
    assert (watch_pyramid_from_above('54321'),
            watch_pyramid_from_the_side('54321'),
            count_all_characters_of_the_pyramid('54321'),
            count_visible_characters_of_the_pyramid('54321')) == (
'''\
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555''', '''\
    1    
   222   
  33333  
 4444444 
555555555''', 165, 81)
