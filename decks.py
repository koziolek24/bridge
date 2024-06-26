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
        # todo correct bids
        # counter only after bid
        # re-counter only after counter
        if verify(bid, possible_bids, bids):
            bids.append(bid)
            return bids
        print("Invalid input\n")


def get_player(bid, player, bids):
    for i in range(len(bids)):
        if bids[i][-1] == bid[-1] and i % 2 == player % 2:
            return bid, i % 4


def get_bid_info(bids):
    final_bid = ""
    player = 0
    for i in range(len(bids)-1, -1, -1):
        # we backtrack of bids to search last non counter/re-counter bid
        if bids[i] == "re-counter":
            final_bid = "re-counter"
        elif bids[i] == "counter" and final_bid != "re-counter":
            final_bid = "counter"
        elif bids[i] != "pass":
            final_bid += bids[i]
            player = i % 4
            # we know side and contract, now we just need to know who will play
            return get_player(final_bid, player, bids)
    return -1, -1


def get_end(bids):
    # either 3 passes after contract, or 4 passes from the beginning
    pass_cnt = 0
    for i in range(len(bids)-1, -1, -1):
        if bids[i] == "pass":
            pass_cnt += 1
        if pass_cnt == 3 and bids[i] != "pass":
            return True
        if pass_cnt == 4:
            return True
        if pass_cnt != 3 and bids[i] != "pass":
            return False
