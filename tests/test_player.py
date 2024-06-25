from player import Player
from game import Deck, Card
import pytest

def test_create_player():
    deck = Deck()
    player = Player("Maciej", "Kozłowski", deck)
    assert player.get_name() == "Maciej"
    assert player.get_lastname() == "Kozłowski"
    assert player.get_fullname() == "Maciej Kozłowski"
    assert player.get_turn() == False
    assert player.get_is_dummy() == False
    assert player.get_deck() == ""


def test_player_play_card():
    cards = [Card(i, "S") for i in range(1, 5)]
    deck = Deck(cards)
    player = Player("Maciej", "Kozłowski", deck)
    assert player.get_deck() == "1S 2S 3S 4S "
    card = Card(3, 'S')
    player.play_card(card)
    assert player.get_deck() == "1S 2S 4S "

def test_player_invalid_turn():
    deck = Deck()
    player = Player("Maciej", "Kozłowski", deck)
    assert player.get_turn() == False
    with pytest.raises(TypeError):
        player.set_turn(3)

def test_player_invalid_is_dummy():
    deck = Deck()
    player = Player("Maciej", "Kozłowski", deck)
    assert player.get_is_dummy() == False
    with pytest.raises(TypeError):
        player.set_is_dummy(3)

def test_player_set_turn():
    deck = Deck()
    player = Player("Maciej", "Kozłowski", deck)
    assert player.get_turn() == False
    player.set_turn(True)
    assert player.get_turn() == True

def test_player_set_is_dummy():
    deck = Deck()
    player = Player("Maciej", "Kozłowski", deck)
    assert player.get_is_dummy() == False
    player.set_is_dummy(True)
    assert player.get_is_dummy() == True