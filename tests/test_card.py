import pytest
from game import Card

def test_create_card():
    card = Card(4, 'H')
    assert card.get_value() == 4
    assert card.get_color() == 'H'
    assert card.get_card() == '4H'

def test_create_card_not_numeral():
    card = Card("A", "S")
    assert card.get_value() == "A"
    assert card.get_color() == 'S'
    assert card.get_card() == 'AS'
