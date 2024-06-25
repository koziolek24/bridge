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
    decks = [[], [], [], []]
    for i in range(3):
        for j in range(13):
            index = random.randrange(len(cards))
            card = cards[index]
            decks[i].append(card)
            cards.remove(card)
    decks[3] = cards
    return decks
