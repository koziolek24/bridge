import pytest
from game import card

def test_create_card():
    Card = card(4, 'H')
    assert Card.get_value() == 4
    assert Card.get_color() == 'H'
    assert Card.get_card() == '4H'


