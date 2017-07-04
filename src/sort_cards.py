"""Sort a deck of cards."""

# ===== Sans Priority Queue SOlutions =====


def sort_cards(deck):
    """Sort the deck."""
    abstract_sorted = 'A23456789TJQK'
    sorted_deck = []
    list_deck = list(deck)
    for card in abstract_sorted:
        while card in list_deck:
            card_index = list_deck.index(card)
            sorted_deck.append(list_deck.pop(card_index))
    return sorted_deck

abstract_sorted_dict = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13
}



