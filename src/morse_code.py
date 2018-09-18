"""
"""
from string import ascii_lowercase


def uniqueMorseRepresentations(words):
    """
    """
    morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    translations = {letter: trans
                    for letter, trans in zip(ascii_lowercase,
                                             morse)}
    x = len({"".join(translations[letter] for letter in word)
             for word in words})
    return x


if __name__ == "__main__":
    num = uniqueMorseRepresentations(["rwjje","aittjje","auyyn","lqtktn","lmjwn"])
    print(num)
