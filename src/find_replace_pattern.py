"""
"""


def findAndReplacePattern(words, pattern):
    """
    """
    out = []
    for word in words:
        letter_map = {}
        word_map = {}
        for pat, letter in zip(pattern, word):
            try:
                try:
                    if word_map[letter] != pat:
                        break
                except KeyError:
                    if letter_map[pat] != letter:
                        break
            except KeyError:
                letter_map[pat] = letter
                word_map[letter] = pat
        else:
            out.append(word)

    return out


if __name__ == '__main__':
    words = ["abc", "deq", "mee", "aqq", "dkd", "ccc"]
    print(findAndReplacePattern(words, 'abb'))
