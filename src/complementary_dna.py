"""Kata: Complementary DNA - Return complementary sequence of DNA

#1 Best Practices Solution by JustyFY, others

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))
    # Python 3.4 solution || you don't need to import anything :)
    # return dna.translate(str.maketrans("ATCG","TAGC"))

Comment: I liked this one
pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna])
"""


def DNA_strand(dna):
    news = []
    for letter in dna:
        if letter == 'A':
            news.append('T')
        elif letter == 'T':
            news.append('A')
        elif letter == 'C':
            news.append('G')
        elif letter == 'G':
            news.append('C')
        return ''.join(news)
