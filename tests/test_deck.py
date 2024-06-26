from game import Deck, Card


def test_deck():
    cards = []
    for i in range(1, 5):
        card = Card(i, 'S')
        cards.append(card)
    deck = Deck(cards)
    assert deck.get_deck() == "1S 2S 3S 4S "


def test_remove_from_deck():
    cards = []
    for i in range(1, 5):
        card = Card(i, 'S')
        cards.append(card)
    deck = Deck(cards)
    assert deck.get_deck() == "1S 2S 3S 4S "
    card = Card(2, 'S')
    deck.remove_card(card)
    assert deck.get_deck() == "1S 3S 4S "


def test_deck_set_deck():
    cards = []
    deck = Deck(cards)
    assert deck.get_deck() == ""
    for i in range(1, 5):
        card = Card(i, 'S')
        cards.append(card)
    deck.set_deck(cards)
    assert deck.get_deck() == "1S 2S 3S 4S "
