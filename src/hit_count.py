"""Kata: Hit Count - Return multidimensional arrays

#1 Best Practices Solution Ben-Hardy & Others

def counter_effect(hit_count):
    return [range(int(i)+1) for i in hit_count]
"""


def counter_effect(hit_count):
    """Return a multi-dimensional array of a number"""
    return [[j for j in range(int(i) + 1)] for i in hit_count]
