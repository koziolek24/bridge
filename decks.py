from game import Card
import random

def get_cards():
    cards = []
    colors = ["S", "C", "D", "H"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    for color in colors:
        for value in values:
            card = Card(value, color)
            cards.append(card)
    return cards


def get_decks():
    cards = get_cards()
    deck1 = []
    deck2 = []
    deck3 = []
    for i in range(13):
        id = random.randrange(len(cards))
        card = cards[id]
        deck1.append(card)
        cards.remove(card)
    for i in range(13):
        id = random.randrange(len(cards))
        card = cards[id]
        deck2.append(card)
        cards.remove(card)
    for i in range(13):
        id = random.randrange(len(cards))
        card = cards[id]
        deck3.append(card)
        cards.remove(card)
    return cards, deck1, deck2, deck3
