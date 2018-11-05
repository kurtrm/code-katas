"""
"""


def ham_bits(x, y):
    """
    """
    bit_x = '{0:08b}'.format(x)
    bit_y = '{0:08b}'.format(y)
    len_diff = abs(len(bit_x) - len(bit_y))
    total = 0
    if len_diff:
        smaller = bit_x if len(bit_x) < len(bit_y) else bit_y
        larger = bit_x if len(bit_x) > len(bit_y) else bit_y
        extra_bits = '0' * len_diff
        smaller = extra_bits + smaller
        for bit1, bit2 in zip(smaller, larger):
            if bit1 != bit2:
                total += 1
    else:
        for bit1, bit2 in zip(bit_x, bit_y):
            if bit1 != bit2:
                total += 1
    return total
