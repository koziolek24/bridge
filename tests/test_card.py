import pytest
from game import Card

def test_create_card():
    card = Card(4, 'H')
    assert card.get_value() == 4
    assert card.get_color() == 'H'
    assert card.get_card() == '4H'
