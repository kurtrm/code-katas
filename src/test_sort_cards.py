"""Test sort cards function(s)."""
import pytest


PARAMS_TABLE = [
    'A', '3', 'T', 'T824Q', 'QKJ6932', 'J69327A8', 'J679J7327A8',
    'TA8AAA24AQA', 'AAAAAAAAAAAAA', '39A5T824Q7J6K', 'Q286JK395A47T',
    '54TQKJ69327A8', 'Q286JK395A47TQ286JK395A47T',
    'Q286JKKKKK395AAA47TQ286JK395A47T',
    'AAAAAAAAAAAAAQ286JK395A47TQ286JK395A47T'
]


def solution(cards):
    """Solution to this kata."""
    return sorted(cards, key='A23456789TJQK'.index)


@pytest.mark.parametrize('deck', PARAMS_TABLE)
def test_sort_cards(deck):
    """Test sorting of cards."""
    from sort_cards import sort_cards
    assert sort_cards(deck) == solution(deck)


@pytest.mark.parametrize('deck', PARAMS_TABLE)
def test_priorityq_sort(deck):
    """Test the priority queue sorting of cards."""
    from sort_cards import CardsPriorityQueue
    sorted_cards = CardsPriorityQueue(deck)
    assert sorted_cards.sort() == solution(deck)
