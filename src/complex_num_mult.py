"""
Given two strings representing complex numbers,
return a string of the result of multiplying two complex numbers.
"""


def complexNumberMultiply(a, b):
    """
    """
    complex_a, complex_b = eval(a.replace('i', 'j')), eval(b.replace('i', 'j'))
    result = complex_a * complex_b
    stringed_result = str(result).replace('j', 'i')
    if len(stringed_result) in [2, 3]:
        return '0+{}'.format(stringed_result)
    if stringed_result[1] == '-':
        return '-' + stringed_result[1:-1][1:].replace('-', '+-')
    return stringed_result[1:-1].replace('-', '+-')
