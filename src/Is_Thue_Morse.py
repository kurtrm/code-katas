"""Kata: Is Thue Morse? - Return True if the sequence contains the
correct digits of the Thue Morse sequence, else False.

#1 Best Practices Solution by pyramidka

Comment: This kata was fairly new, so no solutions had been
voted for Best Practices yet. I chose this one as best practice.
Some of those solutions were impractical, though clever.

def is_thue_morse(seq):
    init_seq = [0]
    while len(init_seq) < len(seq):
        init_seq += [1 if n == 0 else 0 for n in init_seq]
    return init_seq[:len(seq)] == seq
"""


def is_thue_morse(seq):
    """Test if sequence abides by Thue Morse sequence"""
    news = [0]
    while len(news) < len(seq):
        news.extend([1 if dig == 0 else 0 for dig in news])
    for i, _ in enumerate(seq):
        if seq[i] != news[i]:
            return False
    return True
