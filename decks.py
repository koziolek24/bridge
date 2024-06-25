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


def verify(bid, possible_bid, bids):
    if bid not in possible_bid:
        return False
    last_bid = ""
    if bid == "pass" or bid == "counter" or bid == "re-counter":
        return True
    for i in range(len(bids)-1, -1, -1):
        if bids[i] != "pass" and bids[i] != "counter" and bids[i] != "re-counter":
            last_bid = bids[i]
            break
    if last_bid == "":
        return True
    if possible_bid.index(last_bid) < possible_bid.index(bid):
        return True
    return False


def get_bid(bids):
    possible_bids = ["pass", "counter", "re-counter"]
    colors = ["C", "D", "H", "S", "NT"]
    for i in range(1, 8):
        for color in colors:
            bid = str(i) + color
            possible_bids.append(bid)
    while True:
        bid = input("Input your bid: ")
        if verify(bid, possible_bids, bids):
            bids.append(bid)
            return bids
        print("Invalid input\n")
