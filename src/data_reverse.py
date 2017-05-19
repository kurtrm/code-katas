"""Kata: Data Reverse = Reverse a selection of bytes

#1 Best Practices Solution zebulan

def data_reverse(data):
    return [b for a in xrange(len(data) - 8, -1, -8) for b in data[a:a + 8]]
"""

def data_reverse(data):
    """Return an reversed set of binary data in byte sized chunks."""
    new = []
    n = len(data) - 8
    while n >= 0:
        new.extend(data[n:n + 8])
        n -= 8
    return new
