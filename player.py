from game import Deck
from decks import get_card


class Player:
    def __init__(self, name: str, lastname: str):
        self._deck = Deck()
        self._name = name
        self._lastname = lastname
        self._partner = None
        self._turn = False
        self._is_dummy = False
        self._position = None
        self._side = None

    # todo Partner

    def get_name(self):
        return self._name

    def get_lastname(self):
        return self._lastname

    def get_fullname(self):
        fullname = ""
        fullname += self.get_name()
        fullname += " "
        fullname += self.get_lastname()
        return fullname

    def get_turn(self):
        return self._turn

    def get_is_dummy(self):
        return self._is_dummy

    def set_turn(self, turn):
        if self.verify_bool(turn):
            self._turn = turn
        else:
            raise TypeError("turn has to be boolean\n")

    def set_is_dummy(self, is_dummy):
        if self.verify_bool(is_dummy):
            self._is_dummy = is_dummy
        else:
            raise TypeError("is_dummy has to be boolean\n")

    def verify_bool(self, value):
        if value is True or value is False:
            return True
        else:
            return False

    def get_deck(self):
        return self._deck.get_deck()

    def set_deck(self, deck):
        self._deck.set_deck(deck)

    def play_card(self, card):
        try:
            self._deck.remove_card(card)
        except ValueError:
            raise ValueError("card not in deck")

    def get_side(self):
        return self._side

    def set_side(self, side):
        self._side = side

    def set_partner(self, partner):
        self._partner = partner

    def get_partner(self):
        return self._partner

    def is_empty_deck(self):
        if self._deck.is_empty() is True:
            return True
        return False

    def is_in_deck(self, card):
        return self._deck.is_in_deck(card)

    def is_color_in_deck(self, color):
        return self._deck.is_color_in_deck(color)

    def get_play(self, dummy, color):
        print("Dummy's deck:")
        print(dummy.get_deck())
        print("Your deck:")
        print(self.get_deck())
        card = get_card(self, color)
        self.play_card(card)
        return card

    def dummy_play(self, color):
        print("Your deck:")
        print(self.get_deck())
        print("Dummy's deck:")
        print(self._partner.get_deck())
        card = get_card(self._partner, color)
        self._partner.play_card(card)
        return card

    def play_lead(self):
        print("Your deck:")
        print(self.get_deck())
        card = get_card(self, None)
        self.play_card(card)
        return card
