from game import Deck

class Player:
    def __init__(self, deck, partner = None, turn = False, is_dummy = False):
        self._deck = deck
        self._partner = partner
        self._turn = turn
        self._is_dummy = is_dummy

    