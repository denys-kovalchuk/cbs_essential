from settings import SUITS, RANKS
import random


class Card:
    """Card in the deck class"""
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    def __init__(self):
        self.deck = []
        self.create_deck()
        self.shuffle_deck()

    def create_deck(self):
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(rank, suit))

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_cards(self):
        return self.deck.pop()
