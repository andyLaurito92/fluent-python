import unittest
from french_deck import FrenchDeck

class FrenchDeckTest(unittest.TestCase):
    mydeck = FrenchDeck()

    def test_deck_has_52cards(self):
        self.assertEqual(len(self.mydeck), 52)

    def test_deck_contains_only_expected_suits(self):
        self.assertEqual(set([card.suit for card in self.mydeck]), {'spades', 'diamonds', 'clubs', 'hearts'})

    
