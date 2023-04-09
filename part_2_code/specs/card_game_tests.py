import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 2)
        self.cards = [self.card1, self.card2]

    def test_check_for_ace(self):
        card_game = CardGame()
        result = card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_highest_card(self):
        card_game = CardGame()
        result = card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        card_game = CardGame()
        result = card_game.cards_total(self.cards)
        expected_result = "You have a total of 3"
        self.assertEqual(expected_result, result) 


if __name__ == '__main__':
    unittest.main()