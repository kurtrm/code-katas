"""Kata: Your order, please - Return ordered string based on number in word

#1 Best Practices Solution mikolajtr & Others

def order(sentence):
    return " ".join(sorted(sentence.split(),
    key=lambda x: int(filter(str.isdigit, x))))
"""


def order(sentence):
    """Reorder sentence based on digit in word."""
    split = sentence.split()
    dicty = {int(letter): word for word in split
             for letter in list(word) if letter.isdigit()}
    return ' '.join([dicty[i + 1] for i in range(len(dicty))])
