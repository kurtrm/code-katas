"""
Function that returns index of needle in haystack.
"""


def strStr(haystack, needle):
    """
    Function that accomplishes the same thing as the string method
    'index'.
    """
    # return haystack.index(needle)
    needle_length = len(needle)
    for i, letter in enumerate(haystack):
        if haystack[i:i+needle_length] == needle:
            return i
    return -1


if __name__ == '__main__':
    x = strStr('hello', 'll')
    print(x)
