"""
Find the longest common prefix of a list of words.
"""


def longestCommonPrefix(strs):
    """
    """
    if not strs:
        return ""
    longest = strs[0]
    for word in strs[1:]:
        for idx, (prev, nxt) in enumerate(zip(longest, word)):
            if prev != nxt:
                longest = word[:idx]
                break
        else:
            if not longest:
                return ""
            else:
                longest = word if len(word) < len(longest) else longest
    return longest


if __name__ == "__main__":
    longest = longestCommonPrefix(["aaa", "aa", "aaa"])
    print(f'Longest common prefix: "{longest}"')
