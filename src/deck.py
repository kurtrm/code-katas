"""
OOD deck of cards.
"""
import random


class Card:
    """
    class representing a single card in a deck of cards.
    In newer versions of Python, this would be easily represented
    using a data class.
    """
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"Class({self.value}, {self.suit})"


class DeckOfCards:
    """
    Class representing a generic deck of cards.
    """
    suits = ["Diamond", "Heart", "Spade", "Club"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self):
        self.deck = [Card(suit, value) for suit in self.suits
                     for value in self.values]

    def shuffle(self, times=1):
        """
        Shuffle our deck of cards as many times as parameter {times}.
        """
        if times < 1:
            print("Shuffled cards once")
            times = 1
        for _ in range(times):
            random.shuffle(self.deck)

    def sort(self):
        """
        Sort the deck of cards.
        """
        self.deck = self.deck.sort(key=lambda card: card.values)
