"""Functions for the string pyramid kata."""


def watch_pyramid_from_the_side(characters):
    """View the character pyramid from the side."""
    if characters is None:
        return characters
    counter = 1
    listy = []
    for character in characters[::-1]:
        listy.append(character * counter)
        counter += 2
    stringy = ''
    spaces = ((counter) // 2) - 1
    for character in listy:
        if len(character) < counter - 2:
            stringy += '{0}{1}{0}\n'.format(' ' * spaces, character)
            spaces -= 1
        else:
            stringy += character
    return stringy


def watch_pyramid_from_above(characters):
    """View character pyramid from above."""
    if characters is None:
        return characters
    counter = 1
    listy = []
    for character in characters[::-1]:
        listy.append(character * counter)
        counter += 2
    stringy = ''
    top_listy = []
    for index, row in enumerate(listy):
        to_add = len(characters) - (index + 1)
        front = characters[:to_add]
        back = front[::-1]
        stringy += '{0}{1}{2}\n'.format(front, row, back)
        top_listy.append('{}{}{}'.format(front, row, back))
    top_listy = top_listy[::-1]
    top_listy.extend(top_listy[-2::-1])
    return '\n'.join(top_listy)


def count_visible_characters_of_the_pyramid(characters):
    """Return the number of visible letters."""
    if characters is None or len(characters) == 0:
        return -1
    counter = 1
    visible_characters = 1
    for _ in range(1, len(characters)):
        counter += 2
        visible_characters += (counter * 4) - 4
    return visible_characters


def count_all_characters_of_the_pyramid(characters):
    """Return the number of total characters."""
    if characters is None or len(characters) == 0:
        return -1
    counter = 1
    all_characters = 1
    for _ in range(1, len(characters)):
        counter += 2
        all_characters += counter ** 2
    return all_characters
