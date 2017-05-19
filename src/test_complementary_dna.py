"""Test complementary_dna function
"""

import pytest

PARAMS_TABLE = [
    ("AAAA", "TTTT"),
    ("ATTGC", "TAACG"),
    ("GTAT", "CATA"),
    ("AGTATACCGC", "TCATATGGCG"),
    ("TGCATATGCCCA", "ACGTATACGGGT"),
    ("GGGG", "CCCC"),
    ("GGGGCCCCAAAATTTT", "CCCCGGGGTTTTAAAA"),
]


@pytest.mark.parametrize('l, result', PARAMS_TABLE)
def test_complementary_dna(l, result):
    """Test test complementary_dna function"""
    from complementary_dna import DNA_strand
    assert DNA_strand(l) == result