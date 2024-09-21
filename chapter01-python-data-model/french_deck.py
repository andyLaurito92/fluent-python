import collections

# Build a class that is a bundle of attributes and nothing more. Think of it as a DB record
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades = 3, hearts = 2, diamonds = 1, clubs = 0)

    def __init__(self):
        self.cards = [Card(rank, suit)
                      for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __repr__(self):
        """ Defining repr() & str() methods to just see the difference between them """
        return f"FrenchDeck()"

    def __str__(self):
        return f"FrenchDeck({self.cards!s})"

    def rank(self, card):
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]


## Examples on what we can do with the above class

deck = FrenchDeck()

# First 3
deck[:3]

# Grab all 4s
deck[2::13]

for card in sorted(deck, key=deck.rank):
    print(card)

from random import choice

print(f"Choice was: {choice(deck)}")
