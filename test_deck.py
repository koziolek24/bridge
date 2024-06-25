import pytest
from game import Deck, Card

def test_deck():
    cards = []
    for i in range(1, 5):
        card = Card(i, 'S')
        cards.append(card)
    deck = Deck(cards)
    assert deck.get_deck() == "1S 2S 3S 4S "